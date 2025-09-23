#!/usr/bin/env python3
# Extended Pages builder:
# - CAD: discovers .gltf/.glb, honors hero model via manifest, extracts metadata,
#        builds /CAD/index.html with search + gallery, writes /CAD/models.index.json
# - S1000D: copies XML, builds /S1000D/index.html with search, adds /S1000D/viewer.html
#           and /S1000D/xslt/dm2html.xsl for client-side XSLT rendering.
#
# No external deps; stdlib only.

from pathlib import Path
import os, shutil, json, html, re, struct

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"

CAD_SEARCH = [
    "PRODUCTS/*/*/domains/*/cax/CAD/wing_baseline_model/surface_geometry",
    "CAD/wing_baseline_model/surface_geometry",
]
DM_SEARCH = [
    "PRODUCTS/*/*/domains/*/ata/*/S1000D",
    "PRODUCTS/*/*/ata/*/S1000D",
    "PRODUCTS/*/*/ata/*/s1000d",
    "ata/57/s1000d",
    "ata/*/S1000D",
]

MANIFEST_CANDIDATES = [
    "pages.manifest.yaml",                    # repo-level manifest
    "CAD/manifest.yaml",                      # fallback
]

def glob_many(patterns):
    out = []
    for pat in patterns:
        out.extend(ROOT.glob(pat))
    # unique, stable
    seen = set(); uniq = []
    for p in out:
        rp = p.resolve()
        if rp not in seen and rp.exists():
            seen.add(rp); uniq.append(rp)
    return uniq

def write(path: Path, text: str, binary=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if binary:
        with open(path, "wb") as f: f.write(text)
    else:
        path.write_text(text, encoding="utf-8")

def build_root():
    # ensure .nojekyll
    write(SITE / ".nojekyll", "")

# ---------------- CAD helpers ----------------

def read_text_safe(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return p.read_text(encoding="utf-8-sig", errors="ignore")

def try_load_manifest():
    for rel in MANIFEST_CANDIDATES:
        p = ROOT / rel
        if p.exists():
            # tiny YAML reader: key: value pairs only
            data = {}
            for line in read_text_safe(p).splitlines():
                if not line.strip() or line.strip().startswith("#"): continue
                if ":" in line:
                    k,v = line.split(":",1)
                    data[k.strip()] = v.strip().strip('"').strip("'")
            return {"_path": str(p.relative_to(ROOT)), **data}
    return None

# GLB JSON chunk extraction (glTF 2.0)
def extract_glb_json(path: Path):
    with open(path, "rb") as f:
        b = f.read()
    if len(b) < 20 or b[0:4] != b"glTF":
        return None
    _, version, length = struct.unpack("<III", b[0:12])
    if version != 2: return None
    # chunk 0 header at 12..20
    json_len, json_type = struct.unpack("<II", b[12:20])
    if json_type != 0x4E4F534A:  # 'JSON'
        return None
    json_bytes = b[20:20+json_len]
    try:
        return json.loads(json_bytes.decode("utf-8"))
    except Exception:
        return None

def gltf_external_uris_from_json(data):
    uris = []
    for buf in data.get("buffers", []):
        u = buf.get("uri")
        if u and not u.startswith("data:"):
            uris.append(u)
    for img in data.get("images", []):
        u = img.get("uri")
        if u and not u.startswith("data:"):
            uris.append(u)
    return sorted(set(uris))

def collect_sidecars(gltf_path: Path):
    if gltf_path.suffix.lower() == ".glb":
        return []  # embedded
    try:
        data = json.loads(gltf_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    rels = gltf_external_uris_from_json(data)
    return [ (gltf_path.parent / rel) for rel in rels ]

def gltf_metadata(path: Path):
    meta = {"name": path.name}
    if path.suffix.lower() == ".gltf":
        # .gltf is plain JSON; count meshes/materials/primitives
        try:
            data = json.loads(read_text_safe(path))
        except Exception:
            return meta
    elif path.suffix.lower() == ".glb":
        data = extract_glb_json(path) or {}
    else:
        return meta
    meshes = data.get("meshes", [])
    materials = data.get("materials", [])
    prims = 0
    for m in meshes:
        for p in m.get("primitives", []):
            prims += 1
    meta.update({
        "meshes": len(meshes),
        "materials": len(materials),
        "primitives": prims
    })
    return meta

def build_cad_section():
    cad_out = SITE / "CAD" / "assets"
    cad_out.mkdir(parents=True, exist_ok=True)

    models = []
    for root in glob_many(CAD_SEARCH):
        for ext in ("*.gltf","*.glb"):
            for f in sorted(root.glob(ext)):
                # dedicated folder per model to avoid collisions
                bucket = cad_out / f.stem
                bucket.mkdir(parents=True, exist_ok=True)

                # copy model file
                shutil.copy2(f, bucket / f.name)

                # copy sidecars for .gltf (textures, .bin) preserving relative paths
                for sc in collect_sidecars(f):
                    rel = sc.relative_to(f.parent)
                    (bucket / rel).parent.mkdir(parents=True, exist_ok=True)
                    if sc.exists():
                        shutil.copy2(sc, bucket / rel)

                m = gltf_metadata(f)
                models.append({
                    "name": f.name,
                    "site_rel": f"./assets/{f.stem}/{f.name}",
                    "src_repo": str(f.relative_to(ROOT)).replace("\\","/"),
                    "meta": m
                })

    # honor hero from manifest (optional)
    manifest = try_load_manifest()
    hero_rel = None
    if manifest and "cad.hero" in manifest:
        hero_rel = manifest["cad.hero"]
        # find the one matching
        for i, m in enumerate(models):
            if m["src_repo"] == hero_rel:
                # move to front
                models.insert(0, models.pop(i))
                break

    # write models index json
    write(SITE / "CAD" / "models.index.json", json.dumps(models, indent=2))

    # HTML
    write(SITE / "CAD" / "index.html", cad_index_html(models, hero_rel, manifest))

def cad_index_html(models, hero_rel, manifest):
    gallery = "".join(
        f'''
        <li class="item" data-name="{html.escape(m["name"])}">
          <a href="{html.escape(m["site_rel"])}">{html.escape(m["name"])}</a>
          <small class="muted">meshes: {m["meta"].get("meshes","?")}, prims: {m["meta"].get("primitives","?")}, mats: {m["meta"].get("materials","?")}</small>
        </li>
        ''' for m in models
    )
    first = models[0]["site_rel"] if models else ""
    hero_note = f"<p class='muted'>Hero model set via manifest: <code>{html.escape(hero_rel)}</code> (<code>{html.escape(manifest['_path'])}</code>)</p>" if hero_rel else ""
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>CAD Viewer</title>
<script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<style>
  body {{ font: 16px/1.45 system-ui, sans-serif; margin: 1rem 1rem 2rem; }}
  .grid {{ display:grid; gap:1rem; grid-template-columns: 1fr; }}
  .card {{ border:1px solid #ddd; border-radius:12px; padding:1rem; }}
  .muted {{ color:#666 }}
  .row {{ display:flex; gap:.5rem; align-items:center; }}
  input[type=search] {{ width: 100%; padding:.5rem .75rem; border-radius:10px; border:1px solid #ccc; }}
  ul {{ padding-left:1.2rem; }}
  li small {{ display:block; }}
</style>
<h1>CAD — WebXR scene & model viewer</h1>
{hero_note}
<div class="grid">
  <div class="card">
    <h2>WebXR (A-Frame)</h2>
    <p class="muted">Enter VR if your browser/device supports WebXR. The scene loads the first (or hero) model.</p>
    <a-scene renderer="antialias:true">
      <a-sky color="#202225"></a-sky>
      <a-plane rotation="-90 0 0" position="0 0 -4" width="10" height="10" color="#444"></a-plane>
      {f'<a-entity gltf-model="{html.escape(first)}" position="0 1.5 -3"></a-entity>' if first else '<p>No models found yet.</p>'}
      <a-entity position="0 1.6 0">
        <a-entity camera look-controls wasd-controls></a-entity>
      </a-entity>
    </a-scene>
  </div>

  <div class="card">
    <h2>Model Viewer (fallback)</h2>
    {f'<model-viewer src="{html.escape(first)}" ar ar-modes="webxr scene-viewer quick-look" camera-controls autoplay style="width:100%;height:420px;"></model-viewer>' if first else '<p>No models found yet.</p>'}
  </div>

  <div class="card">
    <div class="row"><h2 style="margin:0">Available models</h2><input id="q" type="search" placeholder="Filter by name…"/></div>
    <ul id="list">{gallery or "<li>None yet.</li>"}</ul>
  </div>
</div>
<p><a href="../">← Back to site root</a></p>
<script>
const q = document.getElementById('q');
const items = [...document.querySelectorAll('#list .item')];
q?.addEventListener('input', e => {{
  const s = (q.value || '').toLowerCase();
  items.forEach(li => {{
    li.style.display = li.dataset.name.toLowerCase().includes(s) ? '' : 'none';
  }});
}});
</script>
</html>
"""

# ---------------- S1000D helpers ----------------

def build_s1000d_section():
    dm_root = SITE / "S1000D" / "dm"
    dm_root.mkdir(parents=True, exist_ok=True)

    dms = []
    roots = glob_many(DM_SEARCH)
    for idx, root in enumerate(roots):
        base = dm_root / f"root{idx+1}"
        for f in sorted(list(root.rglob("*.xml")) + list(root.rglob("*.XML"))):
            rel = f.relative_to(root)  # keep subfolders
            dest = base / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
            dms.append({
                "name": str(Path(f"root{idx+1}") / rel).replace("\\","/"),  # path key for viewer
                "site_rel": f"./dm/{Path('root'+str(idx+1))/rel}".replace("\\","/"),
                "src_repo": str(f.relative_to(ROOT)).replace("\\","/")
            })

    write(SITE / "S1000D" / "index.html", s1000d_index_html(dms))
    write(SITE / "S1000D" / "viewer.html", s1000d_viewer_html())
    write(SITE / "S1000D" / "xslt" / "dm2html.xsl", XSLT_DM2HTML)

def s1000d_index_html(dms):
    rows = "".join(
        f"<tr class='row' data-name='{html.escape(dm['name'])}'>"
        f"<td>{html.escape(dm['name'])}</td>"
        f"<td><a href='./viewer.html?dm={html.escape(dm['name'])}'>view</a></td>"
        f"<td><a href='{html.escape(dm['site_rel'])}'>raw</a></td></tr>"
        for dm in dms
    )
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>S1000D Data Modules</title>
<style>
  body {{ font: 16px/1.4 system-ui, sans-serif; margin: 2rem; }}
  table {{ border-collapse: collapse; width: 100%; }}
  td, th {{ border: 1px solid #ddd; padding: .5rem; }}
  th {{ background:#f5f5f5; text-align:left; }}
  input[type=search] {{ width: 320px; max-width:100%; padding:.5rem .75rem; border-radius:10px; border:1px solid #ccc; }}
</style>
<h1>S1000D — Data Modules</h1>
<p>These XML files are copied into <code>/S1000D/dm/</code>. Click "view" for styled rendering.</p>
<p><input id="q" type="search" placeholder="Filter by filename…"></p>
<table>
  <thead><tr><th>File</th><th>View</th><th>Raw</th></tr></thead>
  <tbody id="tbody">
    {rows or "<tr><td colspan='3'>No DMs found.</td></tr>"}
  </tbody>
</table>
<p><a href="../">← Back to site root</a></p>
<script>
const q = document.getElementById('q');
const rows = [...document.querySelectorAll('#tbody .row')];
q?.addEventListener('input', () => {{
  const s = (q.value||'').toLowerCase();
  rows.forEach(tr => {{
    tr.style.display = tr.dataset.name.toLowerCase().includes(s) ? '' : 'none';
  }});
}});
</script>
</html>
"""

def s1000d_viewer_html():
    return """<!doctype html>
<html lang="en">
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>S1000D Viewer</title>
<style>
  body { font: 16px/1.5 system-ui, sans-serif; margin: 1rem; }
  #out { border:1px solid #ddd; border-radius:12px; padding:1rem; }
  .muted { color:#666 }
  code { background:#f6f8fa; padding: .1rem .3rem; border-radius: 6px; }
</style>
<h1>S1000D — XML Viewer</h1>
<p class="muted">Applies a minimal XSLT on the client. You can always open the raw XML.</p>
<div id="out">Loading…</div>
<p><a id="raw" href="#">Open raw XML</a> • <a href="./">Back to list</a></p>
<script>
(function(){
  const params = new URLSearchParams(location.search);
  const name = params.get('dm');              // may include subfolders (e.g. root1/publication_modules/PMC-...xml)
  if (!name || name.includes('..')) {         // naive path sanitization
    document.getElementById('out').textContent = 'Invalid DM path.'; 
    document.getElementById('raw').style.display = 'none';
    return;
  }
  const target = `./dm/${name}`;
  const raw = document.getElementById('raw');
  raw.href = target;

  Promise.all([
    fetch(target).then(r => r.text()),
    fetch('./xslt/dm2html.xsl').then(r => r.text())
  ]).then(([xmlText, xslText]) => {
    const parser = new DOMParser();
    const xml = parser.parseFromString(xmlText, 'application/xml');
    const xsl = parser.parseFromString(xslText, 'application/xml');
    const proc = new XSLTProcessor();
    proc.importStylesheet(xsl);
    const frag = proc.transformToFragment(xml, document);
    const out = document.getElementById('out');
    out.textContent = '';
    out.appendChild(frag);
  }).catch(e => {
    document.getElementById('out').textContent = 'Failed to load or transform XML.';
    console.error(e);
  });
})();
</script>
</html>"""

# Very small XSLT to make S1000D-ish DMs readable; extend as needed.
XSLT_DM2HTML = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
 <xsl:output method="html" indent="yes" />
 <xsl:template match="/">
  <div>
    <h2><xsl:value-of select="/*/identAndStatusSection/pmAddress/pmTitle"/> <xsl:text> </xsl:text>
        <small>(<xsl:value-of select="name(/*)"/>)</small></h2>
    <table border="0" cellspacing="0" cellpadding="4">
      <tr><th align="left">Code</th><td><xsl:value-of select="/*/identAndStatusSection/pmAddress/pmCode"/></td></tr>
      <tr><th align="left">Issue</th><td><xsl:value-of select="/*/identAndStatusSection/pmAddress/issueInfo/issueNumber"/></td></tr>
      <tr><th align="left">Language</th><td><xsl:value-of select="/*/@language"/></td></tr>
    </table>
    <hr/>
    <div>
      <xsl:apply-templates select="/*/*[not(self::identAndStatusSection)]"/>
    </div>
  </div>
 </xsl:template>

 <xsl:template match="*">
   <div style="margin: .3rem 0;">
    <strong><xsl:value-of select="name()"/></strong>
    <xsl:if test="normalize-space(text())">
      <div><xsl:value-of select="normalize-space(text())"/></div>
    </xsl:if>
    <xsl:apply-templates select="*"/>
   </div>
 </xsl:template>
</xsl:stylesheet>
"""

def build_root_index(cad_models, dms):
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Project Pages — CAD & S1000D</title>
<style>
  body {{ font: 16px/1.4 system-ui, sans-serif; margin: 2rem; }}
  a.card {{ display:block; padding:1rem; border:1px solid #ddd; border-radius:12px; text-decoration:none; color:inherit; margin-bottom:1rem }}
  .muted {{ color:#666 }}
</style>
<h1>GitHub Pages — CAD & S1000D</h1>
<p class="muted">Static site built from repo contents. Deployed via GitHub Pages.</p>

<a class="card" href="./CAD/">
  <h2>CAD Viewer <small class="muted">(WebXR + model-viewer)</small></h2>
  <p>Interactive VR-ready scene. Detected: {len(cad_models)} model file(s).</p>
</a>

<a class="card" href="./S1000D/">
  <h2>S1000D Data Modules</h2>
  <p>Browse and view XML with client-side XSLT. Detected: {len(dms)} file(s).</p>
</a>
</html>
"""

def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True, exist_ok=True)
    build_root()

    # CAD
    build_cad_section()

    # S1000D
    build_s1000d_section()

    # Root summary
    # count after building
    cad_models = json.loads((SITE / "CAD" / "models.index.json").read_text(encoding="utf-8")) if (SITE / "CAD" / "models.index.json").exists() else []
    dms = list((SITE / "S1000D" / "dm").glob("*.xml"))
    write(SITE / "index.html", build_root_index(cad_models, dms))

if __name__ == "__main__":
    main()