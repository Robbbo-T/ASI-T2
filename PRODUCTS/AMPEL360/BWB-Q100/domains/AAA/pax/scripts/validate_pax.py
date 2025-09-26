import json
import os
import sys
from jsonschema import validate, ValidationError

# --- Configuration ---
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))
SCHEMA_PATH = os.path.join(REPO_ROOT, 'PRODUCTS', 'AMPEL360', 'BWB-Q100', 'domains', 'AAA', 'pax', 'schemas', 'package.schema.json')

# Mandatory fields required for UTCS/QS seal compliance
MANDATORY_FIELDS = [
    'canonical_hash',
    'sbom_hash',
    'utcs_signature',
    'security_policy_id'
]

def load_json(file_path):
    """Loads a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Schema file not found at {file_path}")
        sys.exit(1)
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
    missing = [field for field in MANDATORY_FIELDS if field not in manifest_data or not manifest_data[field]]
    if missing:
        return False, f"UTCS/QS compliance failed: Missing or empty mandatory fields: {', '.join(missing)}"
    return True, "UTCS/QS compliance check passed."

def validate_pax_manifest(manifest_path, schema):
    """Performs full validation on a single manifest."""
    print(f"\n--- Validating {manifest_path} ---")
    manifest = load_json(manifest_path)

    # 1. Schema Validation
    schema_ok, msg = validate_manifest_schema(manifest, schema)
    print(f"Schema Check: {'PASS' if schema_ok else 'FAIL'} - {msg}")
    
    # 2. QS Compliance Check (Only if schema passed to avoid cascaded errors)
    qs_ok, qs_msg = False, "Skipped due to schema failure."
    if schema_ok:
        qs_ok, qs_msg = validate_qs_compliance(manifest)
        print(f"QS Check: {'PASS' if qs_ok else 'FAIL'} - {qs_msg}")

    return schema_ok and qs_ok

def main(manifest_paths):
    """Main entry point to load schema and validate manifests."""
    if not manifest_paths:
        print("Usage: python validate_pax.py <manifest_file1> [<manifest_file2>...]")
        sys.exit(1)

    print(f"Loading PAx Schema from: {SCHEMA_PATH}")
    schema = load_json(SCHEMA_PATH)
    
    all_passed = True
    for path in manifest_paths:
        if not validate_pax_manifest(path, schema):
            all_passed = False

    if all_passed:
        print("\nSUCCESS: All PAx manifests validated successfully against schema and UTCS/QS requirements.")
        sys.exit(0)
    else:
        print("\nFAILURE: One or more PAx manifests failed validation.")
        sys.exit(1)

if __name__ == '__main__':
    # Simulating usage: requires manifest files as arguments
    # Example usage: python validate_pax.py ./pax/OB/manifests/partition.example.yaml
    main(sys.argv[1:])

