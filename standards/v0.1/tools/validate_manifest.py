#!/usr/bin/env python3
import json
import sys
import pathlib
from jsonschema import Draft7Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "context.schema.json"

def load_json(p):
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file '{p}': {e}", file=sys.stderr)
        sys.exit(2)

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_manifest.py <path/to/context.manifest.json>", file=sys.stderr)
        return 2
    mpath = pathlib.Path(sys.argv[1]).resolve()
    if not mpath.exists():
        print(f"Manifest not found: {mpath}", file=sys.stderr)
        return 2

    schema = load_json(SCHEMA)
    manifest = load_json(mpath)

    errors = sorted(Draft7Validator(schema).iter_errors(manifest), key=lambda e: e.path)
    if errors:
        for e in errors:
            loc = "/".join([str(x) for x in e.path])
            print(f"Schema error at {loc or '$'}: {e.message}", file=sys.stderr)
        return 1

    # Exports must resolve
    base = mpath.parent
    exports = manifest.get("exports", {})
    missing = []
    for key, rel in exports.items():
        p = (base / rel).resolve()
        if not p.exists():
            missing.append((key, rel))
    if missing:
        for key, rel in missing:
            print(f"Missing export path {key}: {rel}", file=sys.stderr)
        return 1

    print("OK: manifest valid and export paths exist")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
