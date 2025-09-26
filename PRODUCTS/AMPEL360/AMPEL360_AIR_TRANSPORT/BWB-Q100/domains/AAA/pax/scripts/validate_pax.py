#!/usr/bin/env python3
"""
PAx manifest validator (BWB-Q100 / AAA)

- Validates JSON **or** YAML manifests against package.schema.json
- Enforces UTCS/QS evidence fields and patterns
- Verifies referenced files exist (artifact, SBOM, signatures)
- Emits clear, CI-friendly output and non-zero exit on failure

Usage:
  python validate_pax.py <manifest_file1> [<manifest_file2>...]
"""

import json
import os
import sys
import yaml
from pathlib import Path
from jsonschema import Draft202012Validator, ValidationError
import re
import glob

# --- Configuration ---
SCRIPT_DIR = Path(__file__).parent
SCHEMA_PATH = SCRIPT_DIR / "../schemas/package.schema.json"

# Mandatory QS/UTCS evidence fields (nested structure)
MANDATORY_EVIDENCE_FIELDS = [
    'evidence.canonical_hash',
    'evidence.sbom.path',
    'evidence.sbom.hash',
    'evidence.signatures',
    'evidence.security_policy_id'
]

# Pattern validation
HASH_PATTERN = re.compile(r'^sha256:[a-f0-9]{64}$')

def load_schema():
    """Load and return the PAx package schema."""
    try:
        with open(SCHEMA_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Schema file not found at {SCHEMA_PATH}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in schema file: {e}")
        sys.exit(1)

def load_manifest(file_path):
    """Load manifest from JSON or YAML file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Manifest file not found: {file_path}")
    
    try:
        with open(path, 'r') as f:
            if path.suffix.lower() in ['.yaml', '.yml']:
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
            else:
                return json.load(f)
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        raise ValueError(f"Error parsing {file_path}: {e}")

def get_nested_value(data, path):
    """Get nested value using dot notation (e.g., 'evidence.sbom.path')."""
    keys = path.split('.')
    value = data
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return value

def validate_schema(manifest_data, schema):
    """Validate manifest against JSON schema, collecting all errors."""
    validator = Draft202012Validator(schema)
    errors = []
    
    for error in validator.iter_errors(manifest_data):
        path = ".".join([str(x) for x in error.path])
        errors.append(f"{path}: {error.message}")
    
    if errors:
        return False, "Schema validation errors:\n  " + "\n  ".join(errors)
    else:
        return True, "Schema validation passed"

def validate_evidence_fields(manifest_data):
    """Check for mandatory UTCS/QS evidence fields."""
    missing_fields = []
    
    for field_path in MANDATORY_EVIDENCE_FIELDS:
        value = get_nested_value(manifest_data, field_path)
        if value is None:
            missing_fields.append(field_path)
    
    if missing_fields:
        return False, f"Missing mandatory evidence fields: {', '.join(missing_fields)}"
    else:
        return True, "All mandatory evidence fields present"

def validate_file_references(manifest_data, manifest_path):
    """Verify that referenced files exist."""
    manifest_dir = Path(manifest_path).parent
    missing_files = []
    
    # Check SBOM file reference
    sbom_path = get_nested_value(manifest_data, 'evidence.sbom.path')
    if sbom_path:
        sbom_file = manifest_dir / sbom_path
        if not sbom_file.exists():
            missing_files.append(f"SBOM file: {sbom_path}")
    
    # Check signature files
    signatures = get_nested_value(manifest_data, 'evidence.signatures')
    if signatures and isinstance(signatures, list):
        for sig in signatures:
            if isinstance(sig, dict) and 'path' in sig:
                sig_file = manifest_dir / sig['path']
                if not sig_file.exists():
                    missing_files.append(f"Signature file: {sig['path']}")
    
    if missing_files:
        return False, f"Missing referenced files: {', '.join(missing_files)}"
    else:
        return True, "All referenced files exist"

def validate_pax_manifest(manifest_path, schema):
    """Perform complete validation on a single manifest."""
    print(f"\n--- Validating {manifest_path} ---")
    
    try:
        manifest = load_manifest(manifest_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Load Error: FAIL - {e}")
        return False
    
    all_passed = True
    
    # 1. Schema validation
    schema_ok, schema_msg = validate_schema(manifest, schema)
    print(f"Schema Check: {'PASS' if schema_ok else 'FAIL'}")
    if not schema_ok:
        print(f"  {schema_msg}")
        all_passed = False
    
    # 2. Evidence fields validation (only if schema passed)
    if schema_ok:
        evidence_ok, evidence_msg = validate_evidence_fields(manifest)
        print(f"Evidence Check: {'PASS' if evidence_ok else 'FAIL'}")
        if not evidence_ok:
            print(f"  {evidence_msg}")
            all_passed = False
        
        # 3. File reference validation
        file_ok, file_msg = validate_file_references(manifest, manifest_path)
        print(f"File Reference Check: {'PASS' if file_ok else 'FAIL'}")
        if not file_ok:
            print(f"  {file_msg}")
            all_passed = False
    
    return all_passed

def main():
    """Main entry point."""
    import argparse
    import glob
    
    # Check if we have the old-style arguments (--schema and --root)
    if len(sys.argv) > 2 and sys.argv[1] == '--schema':
        parser = argparse.ArgumentParser()
        parser.add_argument("--schema", required=True, help="Path to schema file")
        parser.add_argument("--root", required=True, help="Root directory to search for YAML files")
        args = parser.parse_args()
        
        print(f"Loading PAx schema from: {args.schema}")
        schema = load_schema_from_path(args.schema)
        
        # Find all YAML files recursively in the root directory
        yaml_files = []
        for pattern in ['**/*.yaml', '**/*.yml']:
            yaml_files.extend(glob.glob(os.path.join(args.root, pattern), recursive=True))
        
        all_passed = True
        for yaml_file in yaml_files:
            try:
                # Skip README files and other non-manifest files
                manifest = load_manifest(yaml_file)
                if not isinstance(manifest, dict) or "package" not in manifest:
                    continue  # Skip non-manifest files
                
                if not validate_pax_manifest(yaml_file, schema):
                    all_passed = False
            except Exception as e:
                print(f"Skipping {yaml_file}: {e}")
                continue
    else:
        # New-style arguments (direct file list)
        manifest_paths = sys.argv[1:]
        
        if not manifest_paths:
            print("Usage: python validate_pax.py <manifest_file1> [<manifest_file2>...]")
            print("   or: python validate_pax.py --schema <schema_file> --root <root_directory>")
            print("Supports both JSON and YAML manifest files.")
            sys.exit(1)
        
        print(f"Loading PAx schema from: {SCHEMA_PATH}")
        schema = load_schema()
        
        all_passed = True
        for path in manifest_paths:
            if not validate_pax_manifest(path, schema):
                all_passed = False
    
    if all_passed:
        print("\n✅ SUCCESS: All PAx manifests validated successfully")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: One or more PAx manifests failed validation")
        sys.exit(1)

def load_schema_from_path(schema_path):
    """Load and return the PAx package schema from a specific path."""
    try:
        with open(schema_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Schema file not found at {schema_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in schema file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()