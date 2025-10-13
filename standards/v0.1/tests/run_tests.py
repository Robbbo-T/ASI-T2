#!/usr/bin/env python3
import json
import sys
import pathlib
from jsonschema import Draft7Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "context.schema.json"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def validate_case(path, should_pass):
    schema = load(SCHEMA)
    data = load(path)
    errs = list(Draft7Validator(schema).iter_errors(data))
    ok = (len(errs) == 0)
    label = "✓" if ok else "✗"
    name = path.relative_to(ROOT).as_posix()
    if ok and should_pass:
        print(f"{label} {name}")
        return True
    if (not ok) and (not should_pass):
        print(f"{label} {name}  [EXPECTED FAIL]")
        return True
    # print first error for clarity
    if errs:
        print(f"ERROR {name}: {errs[0].message}")
    return False

def main():
    valid = ROOT / "tests" / "conformance" / "valid"
    invalid = ROOT / "tests" / "conformance" / "invalid"
    pass_ok = sum(validate_case(p, True) for p in valid.glob("*.json"))
    fail_ok = sum(validate_case(p, False) for p in invalid.glob("*.json"))
    print(f"PASS: {pass_ok} valid, {fail_ok} invalid caught")
    return 0 if (pass_ok == len(list(valid.glob('*.json'))) and
                 fail_ok == len(list(invalid.glob('*.json')))) else 1

if __name__ == "__main__":
    raise SystemExit(main())
