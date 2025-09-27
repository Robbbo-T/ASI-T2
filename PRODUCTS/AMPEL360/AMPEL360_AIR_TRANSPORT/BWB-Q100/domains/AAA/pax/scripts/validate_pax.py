#!/usr/bin/env python3
"""
PAx manifest validator (BWB-Q100 / AAA)

- Validates JSON **or** YAML manifests against package.schema.json
- Enforces UTCS/QS evidence fields and patterns
- Verifies referenced files exist (SBOM, signatures)
- Emits clear, CI-friendly output and non-zero exit on failure

Usage:
  python validate_pax.py <manifest1> [<manifest2> ...]
  python validate_pax.py --schema <schema_file> --root <directory>
"""

from __future__ import annotations

import json
import os
import sys
import re
import glob
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

import yaml
from jsonschema import Draft202012Validator

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SCHEMA_PATH = (SCRIPT_DIR / "../schemas/package.schema.json").resolve()

# Mandatory UTCS/QS evidence fields (dot-paths inside the manifest)
MANDATORY_EVIDENCE_FIELDS = [
    "evidence.canonical_hash",
    "evidence.sbom.path",
    "evidence.sbom.hash",
    "evidence.signatures",           # list of {path, type, hash?}
    "evidence.security_policy_id",
]

# Simple pattern checks (extend as needed)
SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$", re.IGNORECASE)


# -----------------------------------------------------------------------------
# IO helpers
# -----------------------------------------------------------------------------
def load_schema(path: Path) -> Dict[str, Any]:
    if not path.exists():
        print(f"Error: Schema file not found at {path}")
        sys.exit(1)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in schema file {path}: {e}")
        sys.exit(1)


def load_manifest(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Manifest file not found: {path}")

    try:
        text = path.read_text(encoding="utf-8")
        if path.suffix.lower() in [".yaml", ".yml"]:
            # Support optional UTCS YAML front matter: two YAML docs in one file
            docs = list(yaml.safe_load_all(text))
            if len(docs) == 2 and isinstance(docs[0], dict) and isinstance(docs[1], dict):
                utcs_header, package_data = docs
                # Keep header under a dedicated key for provenance (doesn't affect schema unless defined)
                return {"utcs_header": utcs_header, **package_data}
            elif len(docs) == 1:
                return docs[0] or {}
            else:
                # Multi-doc YAML not in expected 2-part form; merge best-effort
                merged: Dict[str, Any] = {}
                for d in docs:
                    if isinstance(d, dict):
                        merged.update(d)
                return merged
        else:
            return json.loads(text)
    except (yaml.YAMLError, json.JSONDecodeError) as e:
        raise ValueError(f"Parse error in {path}: {e}")


# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------
def get_nested_value(data: Dict[str, Any], dot_path: str) -> Any:
    cur: Any = data
    for key in dot_path.split("."):
        if isinstance(cur, dict) and key in cur:
            cur = cur[key]
        else:
            return None
    return cur


def validate_schema(manifest: Dict[str, Any], schema: Dict[str, Any]) -> Tuple[bool, str]:
    validator = Draft202012Validator(schema)
    errors = []
    for err in validator.iter_errors(manifest):
        path = ".".join(str(p) for p in err.path)
        errors.append(f"{path or '<root>'}: {err.message}")
    if errors:
        return False, "Schema validation errors:\n  " + "\n  ".join(errors)
    return True, "Schema validation passed."


def validate_evidence_present(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    missing: List[str] = []
    for field in MANDATORY_EVIDENCE_FIELDS:
        if get_nested_value(manifest, field) in (None, "", []):
            missing.append(field)
    if missing:
        return False, f"Missing mandatory evidence fields: {', '.join(missing)}"
    return True, "All mandatory evidence fields present."


def validate_evidence_patterns(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    problems: List[str] = []

    # canonical hash format
    ch = get_nested_value(manifest, "evidence.canonical_hash")
    if ch and not SHA256_PATTERN.match(str(ch)):
        problems.append("evidence.canonical_hash must match sha256:<64-hex>")

    # sbom hash format
    sbom_hash = get_nested_value(manifest, "evidence.sbom.hash")
    if sbom_hash and not SHA256_PATTERN.match(str(sbom_hash)):
        problems.append("evidence.sbom.hash must match sha256:<64-hex>")

    # signatures present and optional hash formats
    sigs = get_nested_value(manifest, "evidence.signatures")
    if isinstance(sigs, list):
        for i, sig in enumerate(sigs):
            if not isinstance(sig, dict) or "path" not in sig:
                problems.append(f"evidence.signatures[{i}] must be an object with 'path'")
            h = sig.get("hash")
            if h and not SHA256_PATTERN.match(str(h)):
                problems.append(f"evidence.signatures[{i}].hash must match sha256:<64-hex>")

    if problems:
        return False, "Evidence pattern errors:\n  " + "\n  ".join(problems)
    return True, "Evidence patterns OK."


def validate_file_references(manifest: Dict[str, Any], manifest_path: Path) -> Tuple[bool, str]:
    base = manifest_path.parent
    missing: List[str] = []

    sbom_rel = get_nested_value(manifest, "evidence.sbom.path")
    if sbom_rel:
        if not (base / sbom_rel).exists():
            missing.append(f"SBOM file missing: {sbom_rel}")

    sigs = get_nested_value(manifest, "evidence.signatures")
    if isinstance(sigs, list):
        for i, sig in enumerate(sigs):
            if isinstance(sig, dict) and "path" in sig:
                if not (base / sig["path"]).exists():
                    missing.append(f"Signature file missing: {sig['path']}")

    if missing:
        return False, "Missing referenced files:\n  " + "\n  ".join(missing)
    return True, "All referenced files exist."


def validate_one_manifest(manifest_path: Path, schema: Dict[str, Any]) -> bool:
    print(f"\n--- Validating {manifest_path} ---")
    try:
        manifest = load_manifest(manifest_path)
    except Exception as e:
        print(f"Load Error: FAIL - {e}")
        return False

    ok = True

    s_ok, s_msg = validate_schema(manifest, schema)
    print(f"Schema Check:   {'PASS' if s_ok else 'FAIL'}")
    if not s_ok:
        print("  " + s_msg.replace("\n", "\n  "))
        ok = False

    if s_ok:
        p_ok, p_msg = validate_evidence_present(manifest)
        print(f"Evidence Check: {'PASS' if p_ok else 'FAIL'}")
        if not p_ok:
            print("  " + p_msg)
            ok = False

        r_ok, r_msg = validate_evidence_patterns(manifest)
        print(f"Pattern Check:  {'PASS' if r_ok else 'FAIL'}")
        if not r_ok:
            print("  " + r_msg.replace("\n", "\n  "))
            ok = False

        f_ok, f_msg = validate_file_references(manifest, manifest_path)
        print(f"Files Check:    {'PASS' if f_ok else 'FAIL'}")
        if not f_ok:
            print("  " + f_msg.replace("\n", "\n  "))
            ok = False

    return ok


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------
def main() -> None:
    import argparse

    # Two modes:
    # 1) Direct file list
    # 2) Sweep mode: --schema <schema> --root <dir>
    if len(sys.argv) > 2 and sys.argv[1] == "--schema":
        parser = argparse.ArgumentParser(description="PAx manifest validator (sweep mode)")
        parser.add_argument("--schema", required=True, help="Path to JSON schema file")
        parser.add_argument("--root", required=True, help="Root directory to search for manifests")
        args = parser.parse_args()

        schema_path = Path(args.schema).resolve()
        schema = load_schema(schema_path)

        # Accept both YAML and JSON; skip obvious non-manifests by quick heuristic
        patterns = ["**/*.yaml", "**/*.yml", "**/*.json"]
        manifest_files: List[Path] = []
        for pat in patterns:
            manifest_files.extend(Path(args.root).rglob(pat))

        all_passed = True
        for mf in manifest_files:
            try:
                # Heuristic: parse and require that it's a dict
                mf_data = load_manifest(mf)
                if not isinstance(mf_data, dict) or not mf_data:
                    continue
            except Exception:
                # Skip files that aren't valid manifests
                continue

            if not validate_one_manifest(mf, schema):
                all_passed = False

    else:
        # Direct file list mode
        manifest_args = sys.argv[1:]
        if not manifest_args:
            print("Usage:")
            print("  python validate_pax.py <manifest1> [<manifest2> ...]")
            print("  python validate_pax.py --schema <schema_file> --root <directory>")
            sys.exit(1)

        schema = load_schema(DEFAULT_SCHEMA_PATH)
        all_passed = True
        for m in manifest_args:
            if not validate_one_manifest(Path(m).resolve(), schema):
                all_passed = False

    if all_passed:
        print("\n✅ SUCCESS: All PAx manifests validated successfully")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: One or more PAx manifests failed validation")
        sys.exit(1)


if __name__ == "__main__":
    main()
