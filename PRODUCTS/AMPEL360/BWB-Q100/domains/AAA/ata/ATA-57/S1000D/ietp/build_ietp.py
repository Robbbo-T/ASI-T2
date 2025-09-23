#!/usr/bin/env python3
"""
Static IETP builder for ATA-57 (BWQ1).
- Parses DMRL and indices/dm_index.xml
- Groups by subsystem (57-10/20/30/40/50)
- Buckets by info code (desc/proc/tests/FI/IPD) per program mapping
- Emits static HTML under ietp/site/
Requires: Python 3.9+ (stdlib only). Will optionally use defusedxml if present.
"""
from __future__ import annotations
import html, json, re, sys
from pathlib import Path

# --- paths -------------------------------------------------------------------
S1000D = Path(__file__).resolve().parents[1]
ROOT    = S1000D
OUTDIR  = S1000D / "ietp" / "site"
ASSETS  = S1000D / "ietp" / "assets"
DML     = ROOT / "publication_modules" / "DML-BWQ1-ATA57-00_EN-US.xml"
DM_INDEX= ROOT / "indices" / "dm_index.xml"

# --- XML import shim ---------------------------------------------------------
try:
    import defusedxml.ElementTree as ET
except Exception:
    import xml.etree.ElementTree as ET  # nosec - offline, trusted repo

# --- mapping: categories per info code --------------------------------------
IC_BUCKETS = {
    # Descriptions / tech data (incl. function + 050–056)
    "DESCRIPTION": {"codes": {"040","042","034","050","051","052","053","054","055","056"}},
    # Tests & inspections
    "TESTS":       {"codes": {"310","345","350"}},
    # Removal / install / servicing
    "REMOVAL":     {"range": (500, 599)},
    "SERVICING":   {"range": (600, 699)},
    "INSTALL":     {"range": (700, 799)},
    # Fault isolation
    "FI-GENERAL":  {"codes": {"420"}},
    "FI-SPECIFIC": {"range": (421, 428)},
    # IPD / Parts
    "IPD":         {"codes": {"900","910"}},
}

SUBSYS_NAMES = {
    "10": "57-10 Wing Structure",
    "20": "57-20 Fuel Interfaces",
    "30": "57-30 Control Surfaces",
    "40": "57-40 High-Lift",
    "50": "57-50 Equipment Integration",
}

# --- tiny HTML templates -----------------------------------------------------
LAYOUT = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<link rel="stylesheet" href="../assets/css/ietp.css"/>
<script defer src="../assets/js/ietp.js"></script>
</head><body>
<header class="topbar">
  <a class="brand" href="../index.html">BWB-H₂ Q100 IETP</a>
  <div class="nav-links">
    <a href="../docs/user-guide/User-Guide.md" class="doc-link">📖 Authoring User Guide</a>
  </div>
  <div class="search"><input id="q" placeholder="Search titles & DM keys…"></div>
</header>
<nav class="chips">{chips}</nav>
<main class="content">
{body}
</main>
<footer class="foot">Generated from CSDB · MIC BWQ1 · ATA-57</footer>
</body></html>
"""

INDEX_BODY = """<h1>ATA-57 Interactive Electronic Tech Pub</h1>
<p class="muted">Organized by subsystem and information code (S1000D Issue 6.0).</p>
<section class="cards">
{cards}
</section>
"""

SUBSYS_BODY = """<h1>{subsys_name}</h1>
<p class="muted">Buckets reflect your program's IC mapping (Desc/Tests/R&I/Servicing/FI/IPD).</p>
{groups}
"""

GROUP_BLOCK = """<section class="group">
  <h2>{label}</h2>
  {list}
</section>
"""

DM_LIST = """<ul class="dm-list">
{items}
</ul>
"""

DM_ITEM = """<li class="dm" data-ic="{ic}" data-bucket="{bucket}">
  <a href="../dm/{fname}.html"><strong>{title}</strong></a>
  <div class="meta">
    <code>{key}</code>
    <span class="tag">{ic}</span>
    <span class="bucket">{bucket}</span>
    {status}
  </div>
</li>
"""

DM_PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<link rel="stylesheet" href="../assets/css/ietp.css"/>
<link rel="stylesheet" href="../assets/css/gencms.css"/>
</head><body>
<header class="topbar">
  <a class="brand" href="../index.html">BWB-H₂ Q100 IETP</a>
  <a class="back" href="../subsystem/{subsys}.html">← {subsys_name}</a>
</header>
<main class="content">
  <article class="dm-article">
    <h1>{title}</h1>
    <div class="meta">
      <code>{key}</code>
      <span class="tag">{ic}</span>
      <span class="bucket">{bucket}</span>
      {status}
    </div>
    {html}
    <hr/>
    <p class="muted">Source: <code>{src}</code></p>
  </article>
</main>
<footer class="foot">Generated from CSDB · MIC BWQ1 · ATA-57</footer>
<script defer src="../assets/js/gencms.js"></script>
</body></html>
"""

CHIPS = """
<button class="chip" data-filter="ALL" aria-pressed="true">All</button>
<button class="chip" data-filter="DESCRIPTION">Description</button>
<button class="chip" data-filter="TESTS">Tests & Checks</button>
<button class="chip" data-filter="REMOVAL">Removal (5xx)</button>
<button class="chip" data-filter="INSTALL">Install/Rig (7xx)</button>
<button class="chip" data-filter="SERVICING">Servicing (6xx)</button>
<button class="chip" data-filter="FI-GENERAL">Fault Isolation (420)</button>
<button class="chip" data-filter="FI-SPECIFIC">Fault Isolation (421–428)</button>
<button class="chip" data-filter="IPD">IPD/Parts (900/910)</button>
"""

# --- helpers -----------------------------------------------------------------
def bucket_for_ic(info_code: str) -> str:
    ic = info_code.strip()
    for name, rule in IC_BUCKETS.items():
        if "codes" in rule and ic in rule["codes"]:
            return name
        if "range" in rule:
            lo, hi = rule["range"]
            if ic.isdigit() and lo <= int(ic) <= hi:
                return name
    # fallback
    return "DESCRIPTION" if ic in {"040","042","034"} else "OTHER"

def dm_key_to_subsys(key: str) -> str:
    # DMC-BWQ1-A-57-10-... -> return subSystemCode '10'
    parts = key.split("-")
    return parts[4] if len(parts) > 4 else "10"

def safe(s: str) -> str:
    return html.escape(s or "")

def read_xml(path: Path):
    try:
        return ET.parse(path).getroot()
    except Exception:
        return None

def extract_dm_title(dm_root) -> str:
    try:
        t = dm_root.find(".//dmTitle")
        tech = "".join(t.findtext("techName") or "").strip()
        info = "".join(t.findtext("infoName") or "").strip()
        return (tech + (" — " if tech and info else "") + info) or "Untitled Data Module"
    except Exception:
        return "Untitled Data Module"

def extract_dm_html(dm_root) -> str:
    # Render simple <description> paras + randomList → <ul>
    if dm_root is None:
        return '<p class="muted">No authored content yet.</p>'
    desc = dm_root.find(".//description")
    if desc is None:
        return '<p class="muted">No description section in this DM.</p>'
    out = []
    for lp in desc.findall("./levelledPara"):
        title = lp.findtext("title") or ""
        if title:
            out.append(f"<h2>{safe(title)}</h2>")
        # either a para or a randomList
        para = lp.find("para")
        if para is not None and (para.text or "").strip():
            out.append(f"<p>{safe(para.text)}</p>")
        rl = lp.find("randomList")
        if rl is not None:
            out.append("<ul>")
            for li in rl.findall("./listItem"):
                out.append(f"<li>{safe(li.findtext('para') or '')}</li>")
            out.append("</ul>")
    return "\n".join(out) or '<p class="muted">No text yet.</p>'

# --- load DMRL and index -----------------------------------------------------
def load_dm_requirements() -> list[dict]:
    reqs = []
    if DML.exists():
        dml = read_xml(DML)
        for r in dml.findall(".//dmRequirement"):
            code = r.find("./dmRefIdent/dmCode")
            lang = r.find("./dmRefIdent/language")
            if code is None or lang is None:
                continue
            key = "DMC-{mic}-{sdc}-{sc}-{ssc}-{sssc}-{ac}-{dc}{dcv}-{ic}{icv}-{iloc}-{lang}-{ctry}".format(
                mic=code.get("modelIdentCode"), sdc=code.get("systemDiffCode"),
                sc=code.get("systemCode"), ssc=code.get("subSystemCode"), sssc=code.get("subSubSystemCode"),
                ac=code.get("assyCode"), dc=code.get("disassyCode"), dcv=code.get("disassyCodeVariant"),
                ic=code.get("infoCode"), icv=code.get("infoCodeVariant"),
                iloc=code.get("itemLocationCode"), lang=lang.get("languageIsoCode").upper(),
                ctry=lang.get("countryIsoCode").upper()
            )
            comment = (r.findtext("./reqComment") or "").strip()
            reqs.append({"key": key, "comment": comment})
    return reqs

def index_lookup() -> dict[str, Path]:
    lut = {}
    if DM_INDEX.exists():
        idx = read_xml(DM_INDEX)
        for dm in idx.findall("./dm"):
            lut[dm.get("key")] = ROOT / dm.get("path")
    return lut

# --- build site --------------------------------------------------------------
def copy_assets(src_dir: Path, dst_dir: Path, pattern: str):
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in src_dir.glob(pattern):
        dst_dir.joinpath(src.name).write_text(src.read_text())

def build():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR/"dm").mkdir(exist_ok=True)
    (OUTDIR/"subsystem").mkdir(exist_ok=True)
    (OUTDIR/"docs").mkdir(exist_ok=True)
    
    # copy assets (assume already present)
    copy_assets(ASSETS/"css", OUTDIR/"assets/css", "*.css")
    copy_assets(ASSETS/"js", OUTDIR/"assets/js", "*.js")
    
    # copy docs for User Guide access
    docs_source = ROOT / "docs"
    if docs_source.exists():
        import shutil
        shutil.copytree(docs_source, OUTDIR / "docs", dirs_exist_ok=True)

    reqs = load_dm_requirements()
    lut  = index_lookup()

    # augment with any index entries not in DMRL (safety-net)
    for key, path in lut.items():
        if not any(r["key"] == key for r in reqs):
            reqs.append({"key": key, "comment": ""})

    # model → structure {subsys -> {bucket -> [entries]}}
    model: dict[str, dict[str, list[dict]]] = {}
    for r in reqs:
        key = r["key"]
        parts = key.split("-")
        if len(parts) < 12:
            # unexpected; skip quietly
            continue
        info_code = parts[8][:-1]  # e.g., 040A -> 040
        subsys = parts[4]          # '10', '20', ...
        bucket = bucket_for_ic(info_code)
        model.setdefault(subsys, {}).setdefault(bucket, [])
        model[subsys][bucket].append({
            "key": key,
            "info_code": info_code,
            "bucket": bucket,
            "path": lut.get(key),
            "fname": re.sub(r"[^A-Za-z0-9_-]", "_", key),  # for dm page filename
            "title": r["comment"] or key,
        })

    # subsystem pages + DM pages
    index_cards = []
    site_index = []
    for subsys in sorted(model.keys()):
        subsys_name = SUBSYS_NAMES.get(subsys, f"57-{subsys} (Unmapped)")
        groups_html = []
        for label in ["DESCRIPTION","TESTS","REMOVAL","INSTALL","SERVICING","FI-GENERAL","FI-SPECIFIC","IPD"]:
            items = model[subsys].get(label, [])
            if not items: 
                continue
            items_html = []
            for it in sorted(items, key=lambda x: (x["info_code"], x["key"])):
                status = '<span class="status ok">authored</span>' if it["path"] and it["path"].exists() else '<span class="status todo">pending</span>'
                items_html.append(DM_ITEM.format(
                    ic=it["info_code"], bucket=label, key=safe(it["key"]),
                    title=safe(it["title"]), fname=it["fname"], status=status
                ))
                # emit DM page
                dm_html_content = ""
                title = it["title"]
                if it["path"] and it["path"].exists():
                    dm_root = read_xml(it["path"])
                    title = extract_dm_title(dm_root) or title
                    dm_html_content = extract_dm_html(dm_root)
                else:
                    dm_html_content = '<p class="muted">DM file not authored yet. This page will render content once the XML exists in CSDB.</p>'
                (OUTDIR/"dm"/f"{it['fname']}.html").write_text(DM_PAGE.format(
                    title=safe(title),
                    key=safe(it["key"]),
                    ic=it["info_code"],
                    bucket=label,
                    status=('' if (it["path"] and it["path"].exists()) else '<span class="status todo">pending</span>'),
                    html=dm_html_content,
                    src=(str(it["path"].relative_to(ROOT)) if it["path"] else "MISSING"),
                    subsys=f"57-{subsys}",
                    subsys_name=subsys_name
                ))
                site_index.append({"t": title, "k": it["key"], "s": subsys_name, "b": label})
            groups_html.append(GROUP_BLOCK.format(label=label.replace("-"," — "), list=DM_LIST.format(items="\n".join(items_html))))
        # write subsystem page
        body = SUBSYS_BODY.format(subsys_name=subsys_name, groups="\n".join(groups_html) or "<p>No requirements in this area.</p>")
        (OUTDIR/"subsystem"/f"57-{subsys}.html").write_text(LAYOUT.format(title=subsys_name, chips=CHIPS, body=body))
        # card for index
        index_cards.append(f"""<a class="card" href="subsystem/57-{subsys}.html">
  <div class="card-title">{html.escape(subsys_name)}</div>
  <div class="card-sub">{sum(len(v) for v in model[subsys].values())} modules</div>
</a>""")

    # index page
    index_html = INDEX_BODY.format(cards="\n".join(index_cards) or "<p>No requirements found.</p>")
    (OUTDIR/"index.html").write_text(LAYOUT.format(title="ATA-57 IETP", chips=CHIPS, body=index_html))
    # search index for client JS
    (OUTDIR/"site_index.json").write_text(json.dumps(site_index, ensure_ascii=False, indent=2))
    print(f"IETP built → {OUTDIR}")

if __name__ == "__main__":
    build()