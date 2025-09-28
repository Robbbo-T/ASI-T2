#!/usr/bin/env python3
"""Validate airframes-only assemblies: structure, links, metadata, ATA scope, and control-surface mapping."""

import argparse
import json
import sys
from pathlib import Path

import yaml

AIRFRAMES_ATA = {"ATA-51", "ATA-52", "ATA-53", "ATA-54", "ATA-55", "ATA-56", "ATA-57"}
CTRL_ASMS = {"ASM-008", "ASM-009", "ASM-010"}


def load_yaml(p: Path):
    try:
        with p.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}
    except Exception as e:
        return {"__yaml_error__": f"{p}: {e}"}


def validate_assembly_structure(asm_dir: Path):
    errors, warnings = [], []
    required_dirs = ["models", "drawings", "icd"]
    required_files = ["metadata.yaml"]

    for d in required_dirs:
        if not (asm_dir / d).exists():
            errors.append(f"Missing {d}/ directory")

    for f in required_files:
        if not (asm_dir / f).exists():
            errors.append(f"Missing {f}")

    # Metadata checks
    meta_p = asm_dir / "metadata.yaml"
    meta = load_yaml(meta_p)
    if "__yaml_error__" in meta:
        errors.append(f"metadata.yaml unreadable: {meta['__yaml_error__']}")
        return errors, warnings, {}

    folder_id = asm_dir.name  # e.g., ASM-001
    meta_id = meta.get("assembly_id")
    if meta_id and meta_id != folder_id:
        errors.append(f"assembly_id mismatch (metadata={meta_id}, folder={folder_id})")
    elif not meta_id:
        warnings.append("assembly_id missing in metadata.yaml")

    ata = meta.get("ata_chapter")
    if ata and ata not in AIRFRAMES_ATA:
        errors.append(f"Non-airframe ATA in airframes scope: {ata}")
    elif not ata:
        warnings.append("ata_chapter missing in metadata.yaml")

    # Linked components (relative to the assembly folder)
    links = meta.get("linked_components", []) or []
    for rel in links:
        target = (asm_dir / rel).resolve()
        if not target.exists():
            errors.append(f"Broken link: {rel}")

    # ICD stub presence is helpful
    if (asm_dir / "icd").exists() and not (asm_dir / "icd/README.md").exists():
        warnings.append("icd/README.md missing")

    return errors, warnings, meta


def validate_manifest(base: Path):
    manifest_p = base / "assemblies.manifest.yaml"
    manifest = load_yaml(manifest_p)
    if not manifest:
        return [f"Manifest not found or empty: {manifest_p}"], [], {}
    if "__yaml_error__" in manifest:
        return [f"Manifest unreadable: {manifest['__yaml_error__']}"], [], {}

    errors, warnings = [], []
    # Optional: enforce airframes-only by scanning any declared ATA lists if present
    for sec in ("assemblies", "assemblies_index"):
        for entry in (manifest.get(sec) or []):
            ata = (entry or {}).get("ata_chapter")
            asm_id = (entry or {}).get("id") or (entry or {}).get("assembly_id")
            if ata and ata not in AIRFRAMES_ATA:
                errors.append(f"{asm_id or 'UNSET'} in {sec} has non-airframe ATA: {ata}")

    # Control-surface mapping sanity
    csm = (manifest.get("control_surface_mapping") or {})
    for asm_id, cfg in csm.items():
        if asm_id not in CTRL_ASMS:
            warnings.append(f"control_surface_mapping references non-control ASM: {asm_id}")
        files = cfg.get("config_files") or []
        for rel in files:
            p = (base / rel).resolve()
            if not p.exists():
                errors.append(f"Mapping config file missing: {rel}")
        # If surfaces explicitly listed, ensure non-empty
        if "surfaces" in cfg and not (cfg.get("surfaces") or []):
            errors.append(f"{asm_id} has empty 'surfaces' list in control_surface_mapping")
        # If surfaces_from used, file must exist (checked above)
        if "surfaces_from" in cfg and not cfg.get("surfaces_from"):
            errors.append(f"{asm_id} has empty 'surfaces_from' in control_surface_mapping")

    return errors, warnings, manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--base",
        default="domains/AAA/cax/CAD",
        help="Base path containing assemblies/ and assemblies.manifest.yaml",
    )
    ap.add_argument("--json", action="store_true", help="Emit JSON summary and exit non-zero on errors")
    args = ap.parse_args()

    base = Path(args.base).resolve()
    asms_dir = base / "assemblies"
    errors_all, warnings_all = [], []
    report = {"assemblies": {}}

    man_errors, man_warns, manifest = validate_manifest(base)
    errors_all += man_errors
    warnings_all += man_warns

    if not asms_dir.exists():
        errors_all.append(f"Assemblies folder not found: {asms_dir}")
    else:
        for asm_dir in sorted(asms_dir.glob("ASM-*")):
            if not asm_dir.is_dir():
                continue
            errs, warns, meta = validate_assembly_structure(asm_dir)
            report["assemblies"][asm_dir.name] = {
                "errors": errs,
                "warnings": warns,
                "metadata": meta,
            }
            errors_all += [f"{asm_dir.name}: {e}" for e in errs]
            warnings_all += [f"{asm_dir.name}: {w}" for w in warns]

    summary = {
        "base": str(base),
        "total_assemblies": len(report["assemblies"]),
        "errors": errors_all,
        "warnings": warnings_all,
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        for e in errors_all:
            print(f"❌ {e}")
        for w in warnings_all:
            print(f"⚠️  {w}")
        ok = [k for k, v in report["assemblies"].items() if not v["errors"]]
        for k in ok:
            print(f"✅ {k}: Valid")

        print(
            f"\nSummary: {len(errors_all)} error(s), {len(warnings_all)} warning(s), "
            f"{len(ok)}/{len(report['assemblies'])} assemblies valid"
        )

    sys.exit(1 if errors_all else 0)


if __name__ == "__main__":
    main()