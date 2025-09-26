import json
import os
import sys
from jsonschema import validate, ValidationError

# --- Configuration: FINAL PATH FIX ---
# Calculate the path by moving up the known directory structure from the script's location.
# Script location: .../AAA/pax/scripts/validate_pax.py
# Schema location: .../AAA/pax/schemas/package.schema.json

# __file__ -> .../AAA/pax/scripts/validate_pax.py
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# SCRIPT_DIR -> .../AAA/pax/scripts/
# Move up one level (..) to .../AAA/pax/
PAX_DIR = os.path.join(SCRIPT_DIR, '..')

# SCHEMA_PATH -> .../AAA/pax/schemas/package.schema.json
SCHEMA_PATH = os.path.join(PAX_DIR, 'schemas', 'package.schema.json')

# Mandatory fields required for UTCS/QS seal compliance
MANDATORY_FIELDS = [
    'canonical_hash',
    'sbom_hash',
    'utcs_signature',
    'security_policy_id'
]

def load_json(file_path):
    """Loads a JSON file."""
    # Ensure path exists before opening
    if not os.path.exists(file_path):
        print(f"FATAL ERROR: Schema file not found at {file_path}")
        sys.exit(1)

    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        sys.exit(1)

def validate_manifest_schema(manifest_data, schema):
    """Validates manifest data against the JSON schema."""
    try:
        validate(instance=manifest_data, schema=schema)
        return True, "Schema validation passed."
    except ValidationError as e:
        return False, f"Schema validation failed: {e.message} in instance path {e.json_path}"

def validate_qs_compliance(manifest_data):
    """Checks for mandatory QS/UTCS fields."""
    manifest_keys = manifest_data.keys()
    missing = [field for field in MANDATORY_FIELDS if field not in manifest_keys or not manifest_data.get(field)]
    if missing:
        return False, f"UTCS/QS compliance failed: Missing or empty mandatory fields: {', '.join(missing)}"
    return True, "UTCS/QS compliance check passed."

def validate_pax_manifest(manifest_path, schema):
    """Performs full validation on a single manifest."""
    print(f"\n--- Validating {manifest_path} ---")
    
    # Use the local load_json function which includes existence check
    manifest = load_json(manifest_path) 

    # 1. Schema Validation
    schema_ok, msg = validate_manifest_schema(manifest, schema)
    print(f"Schema Check: {'PASS' if schema_ok else 'FAIL'} - {msg}")
    
    # 2. QS Compliance Check 
    qs_ok, qs_msg = False, "Skipped due to schema failure."
    if schema_ok:
        qs_ok, qs_msg = validate_qs_compliance(manifest)
        print(f"QS Check: {'PASS' if qs_ok else 'FAIL'} - {qs_msg}")

    return schema_ok and qs_ok

def main():
    """Entry point to load schema and validate manifests provided via CLI args."""
    manifest_paths = sys.argv[1:] 

    if not manifest_paths:
        print("Usage: python validate_pax.py <manifest_file1> [<manifest_file2>...]")
        sys.exit(1)

    print(f"Attempting to load PAx Schema from: {SCHEMA_PATH}")
    # Load schema; load_json will exit on failure
    schema = load_json(SCHEMA_PATH) 

    all_passed = True
    for path in manifest_paths:
        if not validate_pax_manifest(path, schema):
            all_passed = False

    if all_passed:
        print("\nSUCCESS: All PAx manifests validated successfully against schema and UTCS/QS requirements (TFA compliant).")
        sys.exit(0)
    else:
        print("\nFAILURE: One or more PAx manifests failed validation.")
        sys.exit(1)

if __name__ == '__main__':
    main()
