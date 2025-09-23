#!/usr/bin/env python3
import sys, json, yaml, argparse, glob, os
from jsonschema import Draft202012Validator

def load_yaml(p):
    with open(p, "r", encoding="utf-8") as f:
        # Handle YAML documents with UTCS frontmatter
        docs = list(yaml.safe_load_all(f))
        if len(docs) == 2:
            # First doc is UTCS header, second is the package data
            utcs_header, package_data = docs
            return {"utcs_header": utcs_header, **package_data}
        elif len(docs) == 1:
            return docs[0]
        else:
            return {}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True)
    ap.add_argument("--root", required=True)
    args = ap.parse_args()

    schema = json.load(open(args.schema, "r", encoding="utf-8"))
    validator = Draft202012Validator(schema)

    errors = 0
    for p in glob.glob(os.path.join(args.root, "**", "*.yaml"), recursive=True):
        data = load_yaml(p)
        if not isinstance(data, dict) or "package" not in data:
            continue  # README, etc.
        for e in validator.iter_errors(data):
            errors += 1
            path = "/".join([str(x) for x in e.path])
            print(f"[SCHEMA] {p}: {path} -> {e.message}")
        if "utcs_header" not in data:
            print(f"[UTCS] {p}: falta 'utcs_header' (usa cabecera YAML + documento)")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()