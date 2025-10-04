#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deriva estructura ATA / CAx / QOx / PAx desde README(s) de dominios.
Mejoras: rangos ATA (51–57), BREX-lite UTCS-MI, dry-run, logging, índices por dominio y global.
Exit codes: 0 OK, 3 sin cambios, 4 drift (--check), 5 BREX fallo (--brex-strict).
"""

import argparse, datetime, os, re, sys, unicodedata, json, subprocess
from pathlib import Path

# ------------------------------ Regex ----------------------------------------

# ATA: individuales y con subcapítulos (57, 57-10, 57-10-30)
RE_ATA_FULL = re.compile(r"\bATA[-\s]?(\d{2})(?:-(\d{2}))?(?:-(\d{2}))?\b", re.IGNORECASE)
# Rangos ATA por capítulo: "ATA 51–57" / "ATA 51-57" / "ATA 51 a 57" / "ATA 51 to 57"
RE_ATA_RANGE = re.compile(r"\bATA[-\s]?(\d{2})\s*(?:[–-]|a|to)\s*(\d{2})\b", re.IGNORECASE)

CAX_TOKENS = {
    "CAD","CAE","CFD","CAM","CAI","CAP","CASE","CAPP","CAT","VP","MBSE","MBD",
    "PDM","PLM","PDM-PLM","CIM","SCM","MRP-ERP","CAX"
}
RE_CAX = re.compile(r"\b(" + "|".join(sorted(CAX_TOKENS, key=len, reverse=True)) + r")\b", re.IGNORECASE)

QOX_TOKENS = {"QUBO","BQM","QAOA","VQE","HHL","QLSA","ANNEALING","QML","VQA","DMRG","QISKIT","PENNYLANE","CIRQ"}
RE_QOX = re.compile(r"\b(" + "|".join(sorted(QOX_TOKENS)) + r")\b", re.IGNORECASE)

PAX_OB_TOKENS = {"ARINC653","A653","IMA","A661","A664","AFDX","A429","VXWORKS","INTEGRITY","DEOS"}
PAX_OFF_TOKENS = {"OCI","DOCKER","KUBERNETES","HELM","EFB","MRO","EDGE","CLOUD","MICROSERVICE","COMPOSE","KUSTOMIZE"}
RE_PAX_OB = re.compile(r"\b(" + "|".join(sorted(PAX_OB_TOKENS)) + r")\b", re.IGNORECASE)
RE_PAX_OFF = re.compile(r"\b(" + "|".join(sorted(PAX_OFF_TOKENS)) + r")\b", re.IGNORECASE)

# ------------------------------ Utils ----------------------------------------

def log(msg, level="INFO", quiet=False, want="INFO"):
    order = ["ERROR","WARN","INFO","DEBUG"]
    if quiet: return
    if order.index(level) <= order.index(want):
        print(f"[{level}] {msg}")

def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+","-", s).strip("-").lower()
    return s or "item"

def today_iso():
    return datetime.date.today().isoformat()

def utcs_header(id_, project, artifact, llc="SYSTEMS"):
    # en-dash en classification
    return f"""---
id: {id_}
project: {project}
artifact: {artifact}
llc: {llc}
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: {today_iso()}
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---
"""

def write_readme(path: Path, title: str, body_lines: list, project: str, llc="SYSTEMS", dry=False, loglvl="INFO"):
    path = path.resolve()
    if path.exists():
        return False, False
    header = utcs_header(
        id_=f"{title.upper().replace(' ', '-')}-OV-0001",
        project=project,
        artifact=str(path).replace("\\","/"),
        llc=llc,
    )
    content = header + f"# {title}\n\n" + "\n".join(body_lines) + "\n"
    if dry:
        log(f"(dry) would write {path}", "DEBUG", want=loglvl)
        return True, False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True, True

def ensure_dir(path: Path, dry=False, loglvl="INFO"):
    path = path.resolve()
    if dry:
        if not path.exists():
            log(f"(dry) would mkdir -p {path}", "DEBUG", want=loglvl)
        return False
    path.mkdir(parents=True, exist_ok=True)
    return True

def create_or_overwrite(path: Path, text: str, force=False, dry=False, loglvl="INFO"):
    path = path.resolve()
    if path.exists() and not force:
        return False, False
    if dry:
        log(f"(dry) would write {path}", "DEBUG", want=loglvl)
        return True, False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True, True

def git_toplevel():
    try:
        out = subprocess.check_output(["git","rev-parse","--show-toplevel"], stderr=subprocess.DEVNULL)
        return Path(out.decode().strip())
    except Exception:
        return None

def infer_project_from_path(domain_dir: Path):
    parts = list(domain_dir.parts)
    if "PRODUCTS" in parts:
        i = parts.index("PRODUCTS")
        segs = parts[i:i+3] if len(parts) > i+2 else parts[i:]
        return "/".join(segs)
    top = git_toplevel()
    if top:
        try:
            rel = domain_dir.relative_to(top)
            return f"{top.name}/{rel.parts[0]}" if rel.parts else top.name
        except Exception:
            pass
    return "UNKNOWN"

def infer_product_from_path(domain_dir: Path):
    """Extract full product path from domain directory path.
    Returns path up to the product level (before /domains/)."""
    parts = list(domain_dir.parts)
    if "domains" in parts:
        i = parts.index("domains")
        # Find where PRODUCTS starts
        if "PRODUCTS" in parts:
            j = parts.index("PRODUCTS")
            return "/".join(parts[j:i])
        return "/".join(parts[:i])
    if "PRODUCTS" in parts:
        i = parts.index("PRODUCTS")
        # Try to get up to 4 segments after PRODUCTS
        segs = parts[i:i+4] if len(parts) > i+3 else parts[i:]
        return "/".join(segs)
    return "UNKNOWN"

# ------------------------------ YAML mini-dumper ------------------------------

def yaml_dump(obj) -> str:
    def to_yaml(o, indent=0):
        sp = "  " * indent
        if isinstance(o, dict):
            lines=[]
            for k,v in o.items():
                if isinstance(v,(dict,list)):
                    lines.append(f"{sp}{k}:")
                    lines.append(to_yaml(v, indent+1))
                else:
                    lines.append(f"{sp}{k}: {json.dumps(v, ensure_ascii=False)}")
            return "\n".join(lines)
        elif isinstance(o, list):
            lines=[]
            for it in o:
                if isinstance(it,(dict,list)):
                    lines.append(f"{sp}-")
                    lines.append(to_yaml(it, indent+1))
                else:
                    lines.append(f"{sp}- {json.dumps(it, ensure_ascii=False)}")
            return "\n".join(lines)
        else:
            return f"{sp}{json.dumps(o, ensure_ascii=False)}"
    return to_yaml(obj) + "\n"

# ------------------------------ Front-matter BREX-lite ------------------------

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def parse_front_matter(text: str):
    # Muy simple: primera cabecera --- ... ---
    if not text.startswith("---"): return {}
    parts = text.split("\n")
    if parts[0].strip() != "---": return {}
    # busca la siguiente línea '---'
    end = None
    for i in range(1, min(len(parts), 200)):
        if parts[i].strip() == "---":
            end = i
            break
    if end is None: return {}
    header_lines = parts[1:end]
    fm = {}
    for line in header_lines:
        if ":" not in line: continue
        k,v = line.split(":",1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm

def brex_lite_validate(fm: dict):
    """Devuelve (ok, issues[list], warnings[list])."""
    required = ["id","project","artifact","llc","classification","version","release_date",
                "maintainer","bridge","ethics_guard","utcs_mi","canonical_hash"]
    issues, warnings = [], []
    for k in required:
        if k not in fm or not fm[k]:
            issues.append(f"missing:{k}")
    # classification con en-dash
    if "classification" in fm:
        if fm["classification"] != "INTERNAL–EVIDENCE-REQUIRED":
            if "INTERNAL-EVIDENCE-REQUIRED" in fm["classification"]:
                issues.append("classification: use en-dash (–) not hyphen (-)")
            else:
                issues.append("classification: unexpected value")
    # semver
    if "version" in fm and not SEMVER_RE.match(fm["version"]):
        issues.append("version: not semver MAJOR.MINOR.PATCH")
    # fecha ISO
    if "release_date" in fm and not DATE_RE.match(fm["release_date"]):
        issues.append("release_date: not YYYY-MM-DD")
    # bridge exacto
    if "bridge" in fm and fm["bridge"] != "CB→QB→UE→FE→FWD→QS":
        warnings.append("bridge: expected 'CB→QB→UE→FE→FWD→QS'")
    # utcs_mi
    if "utcs_mi" in fm and fm["utcs_mi"].lower() not in {"v5.0","v5"}:
        warnings.append("utcs_mi: expected v5.0")
    return (len(issues)==0, issues, warnings)

# ------------------------------ Extract --------------------------------------

def expand_ata_ranges(text: str):
    """Devuelve lista de dicts {'chapter': '51'} a partir de rangos ATA."""
    entries = []
    for m in RE_ATA_RANGE.finditer(text):
        a = int(m.group(1))
        b = int(m.group(2))
        if a > b: a, b = b, a
        for ch in range(a, b+1):
            entries.append({"chapter": f"{ch:02d}"})
    return entries

def extract_signals(text: str):
    # ATA individuales/subcapítulos
    atas = []
    for m in RE_ATA_FULL.finditer(text):
        ch, sub1, sub2 = m.group(1), m.group(2), m.group(3)
        entry = {"chapter": ch}
        if sub1: entry["section"] = sub1
        if sub2: entry["subject"] = sub2
        atas.append(entry)
    # Rangos por capítulo
    atas += expand_ata_ranges(text)

    # Normaliza duplicados
    dedup = { tuple((k, e[k]) for k in ("chapter","section","subject") if k in e): e for e in atas }
    atas = list(dedup.values())

    # CAx / QOx / PAx
    cax = sorted(set(m.group(1).upper().replace("PDM","PDM-PLM") for m in RE_CAX.finditer(text)))
    qox = sorted(set(m.group(1).upper() for m in RE_QOX.finditer(text)))
    pax_ob = sorted(set(m.group(1).upper() for m in RE_PAX_OB.finditer(text)))
    pax_off = sorted(set(m.group(1).upper() for m in RE_PAX_OFF.finditer(text)))
    return atas, cax, qox, pax_ob, pax_off

# ------------------------------ Pipeline -------------------------------------

def derive_for_domain(domain_dir: Path, force=False, dry=False, loglvl="INFO", brex_strict=False):
    readme = domain_dir / "README.md"
    if not readme.exists():
        log(f"skip: no README in {domain_dir}", "WARN", want=loglvl); 
        return None, False, False  # idx, wrote_any, brex_fail

    try:
        text = readme.read_text(encoding="utf-8-sig", errors="ignore")
    except Exception:
        text = readme.read_text(encoding="utf-8", errors="ignore")

    # BREX-lite
    fm = parse_front_matter(text)
    ok_brex, brex_issues, brex_warn = brex_lite_validate(fm)
    if not ok_brex:
        log(f"BREX issues in {readme}: {brex_issues}", "WARN", want=loglvl)
    if brex_warn:
        log(f"BREX warnings in {readme}: {brex_warn}", "INFO", want=loglvl)

    atas, cax, qox, pax_ob, pax_off = extract_signals(text)
    project = infer_project_from_path(domain_dir)
    product = infer_product_from_path(domain_dir)

    created = {"ata":0,"cax":0,"qox":0,"pax":0,"files":0}
    wrote_any = False

    # ATA tree (57 / 57-10 / 57-10-30)
    ata_root = domain_dir / "ata"
    for a in atas:
        ch = a["chapter"]
        path = ata_root / ch
        ensure_dir(path, dry, loglvl)
        if "section" in a:
            path = path / f"{ch}-{a['section']}"
            ensure_dir(path, dry, loglvl)
        if "subject" in a:
            path = path / f"{ch}-{a['section']}-{a['subject']}"
            ensure_dir(path, dry, loglvl)
        title = "ATA-" + "-".join([a[k] for k in ["chapter","section","subject"] if k in a])
        changed, wrote = write_readme(
            path / "README.md",
            title=title,
            body_lines=[f"Publicaciones y evidencia para **{title}**."],
            project=project, dry=dry, loglvl=loglvl
        )
        if changed:
            created["ata"]+=1; created["files"]+=1; wrote_any |= wrote

    # CAx
    cax_root = domain_dir / "cax"
    for token in cax:
        sub = token.upper()
        sub = "_meta" if sub in {"CAX"} else sub
        ensure_dir(cax_root / sub, dry, loglvl)
        changed, wrote = write_readme(
            cax_root / sub / "README.md",
            title=f"CAx/{sub}",
            body_lines=[f"Entrada de proceso **{sub}** derivada del README de dominio."],
            project=project, dry=dry, loglvl=loglvl
        )
        if changed:
            created["cax"]+=1; created["files"]+=1; wrote_any |= wrote

    # QOx
    qox_root = domain_dir / "qox"
    for token in qox:
        sub = slugify(token)
        ensure_dir(qox_root / sub, dry, loglvl)
        changed, wrote = write_readme(
            qox_root / sub / "README.md",
            title=f"QOx/{token}",
            body_lines=[f"Optimización/cuántica **{token}** detectada en el dominio."],
            project=project, dry=dry, loglvl=loglvl
        )
        if changed:
            created["qox"]+=1; created["files"]+=1; wrote_any |= wrote

    # PAx
    pax_root = domain_dir / "pax"
    created_pax=False
    if pax_ob:
        ensure_dir(pax_root / "OB" / "manifests", dry, loglvl)
        ensure_dir(pax_root / "OB" / "sbom", dry, loglvl)
        ensure_dir(pax_root / "OB" / "certificates", dry, loglvl)
        write_readme(pax_root / "OB" / "README.md", "PAx/OB — On-Board",
                     [f"Términos detectados: {', '.join(pax_ob)}."],
                     project=project, dry=dry, loglvl=loglvl)
        created_pax=True
    if pax_off:
        ensure_dir(pax_root / "OFF" / "oci", dry, loglvl)
        ensure_dir(pax_root / "OFF" / "sbom", dry, loglvl)
        write_readme(pax_root / "OFF" / "README.md", "PAx/OFF — Off-Board",
                     [f"Términos detectados: {', '.join(pax_off)}."],
                     project=project, dry=dry, loglvl=loglvl)
        created_pax=True
    if created_pax:
        changed, wrote = write_readme(
            pax_root / "README.md","PAx — Packaging & Applications",
            ["On-board (ARINC 653/IMA, A661, A664) y off-board (OCI/edge/cloud) con SBOM y QS."],
            project=project, dry=dry, loglvl=loglvl
        )
        if changed:
            created["pax"]+=1; created["files"]+=1; wrote_any |= wrote

    # Índice por dominio
    idx = {
        "schema_version": "1.0",
        "product": product,
        "domain": domain_dir.name,
        "project": project,
        "brex": {
            "ok": bool(ok_brex),
            "issues": brex_issues,
            "warnings": brex_warn
        },
        "extracted": {
            "ATA": atas, "CAx": sorted(list(set(cax))), "QOx": sorted(list(set(qox))),
            "PAx": {"OB": pax_ob, "OFF": pax_off}
        },
        "generated": created,
        "timestamp": datetime.datetime.utcnow().isoformat()+"Z"
    }
    idx_path = domain_dir / "index.extracted.yaml"
    idx_yaml = yaml_dump(idx)
    changed, wrote = create_or_overwrite(idx_path, idx_yaml, force=True, dry=dry, loglvl=loglvl)
    if changed:
        created["files"]+=1; wrote_any |= wrote

    log(f"{domain_dir} → ATA:{len(atas)} CAx:{len(cax)} QOx:{len(qox)} PAx_OB:{len(pax_ob)} PAx_OFF:{len(pax_off)} BREX:{'OK' if ok_brex else 'FAIL'}", "INFO", want=loglvl)
    return idx, wrote_any, (brex_strict and not ok_brex)

def find_domain_roots(search_roots):
    candidates=set()
    for root in search_roots:
        base = Path(root)
        if not base.exists(): continue
        for p in base.rglob("domains/*/README.md"):
            candidates.add(str(p.parent.resolve()))
    if Path("domains").exists():
        for p in Path("domains").glob("*/README.md"):
            candidates.add(str(p.parent.resolve()))
    return [Path(s) for s in sorted(candidates)]

# ------------------------------ Main -----------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Deriva estructura ATA/CAx/QOx/PAx desde README(s) de dominios.")
    ap.add_argument("--roots", nargs="*", default=["PRODUCTS","ASI-T2/PRODUCTS"], help="Raíces a escanear.")
    ap.add_argument("--force", action="store_true", help="Sobrescribir README existentes.")
    ap.add_argument("--dry-run", action="store_true", help="No escribe; solo informa.")
    ap.add_argument("--log-level", default="INFO", choices=["ERROR","WARN","INFO","DEBUG"], help="Nivel de log.")
    ap.add_argument("--emit-index", type=str, help="Ruta para YAML con resumen global.")
    ap.add_argument("--check", action="store_true", help="Solo verifica; si habría cambios, exit 4.")
    ap.add_argument("--brex-strict", action="store_true", help="Fallar (exit 5) si el BREX-lite no pasa en algún dominio.")
    args = ap.parse_args()

    domain_dirs = find_domain_roots(args.roots)
    if not domain_dirs:
        log("No se encontraron dominios bajo las raíces indicadas.", "ERROR", want=args.log_level)
        sys.exit(2)

    global_idx = {"domains":[]}
    wrote_any_global = False
    brex_failed_any = False

    for d in domain_dirs:
        idx, wrote_any, brex_fail = derive_for_domain(
            d, force=args.force, dry=args.dry_run or args.check, loglvl=args.log_level, brex_strict=args.brex_strict
        )
        if idx: 
            global_idx["domains"].append(idx)
            wrote_any_global |= wrote_any
            brex_failed_any |= brex_fail

    if args.emit_index:
        text = yaml_dump(global_idx)
        if args.dry_run or args.check:
            log(f"(dry) would write global index at {args.emit_index}", "DEBUG", want=args.log_level)
        else:
            Path(args.emit_index).parent.mkdir(parents=True, exist_ok=True)
            Path(args.emit_index).write_text(text, encoding="utf-8")
            log(f"wrote {args.emit_index}", "INFO", want=args.log_level)
            wrote_any_global = True or wrote_any_global

    # Exit codes
    if args.check:
        # drift si habría escrituras
        sys.exit(4 if wrote_any_global else 0)
    if brex_failed_any:
        sys.exit(5)
    if not wrote_any_global:
        sys.exit(3)  # sin cambios
    sys.exit(0)

if __name__ == "__main__":
    main()