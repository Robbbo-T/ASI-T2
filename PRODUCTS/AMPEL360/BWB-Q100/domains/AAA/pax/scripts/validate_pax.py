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
                return yaml.safe_load(f)
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
    errors = list(validator.iter_errors(manifest_data))
    
    if not errors:
        return True, "Schema validation passed"
    
    error_messages = []
    for error in errors:
        path = ".".join(str(p) for p in error.path) if error.path else "root"
        error_messages.append(f"Path '{path}': {error.message}")
    
    return False, f"Schema validation failed:\n  " + "\n  ".join(error_messages)

def validate_evidence_fields(manifest_data):
    """Check for mandatory UTCS/QS evidence fields."""
    missing = []
    invalid_patterns = []
    
    for field_path in MANDATORY_EVIDENCE_FIELDS:
        value = get_nested_value(manifest_data, field_path)
        if value is None or (isinstance(value, str) and not value.strip()):
            missing.append(field_path)
        elif field_path.endswith('.hash') and isinstance(value, str):
            if not HASH_PATTERN.match(value):
                invalid_patterns.append(f"{field_path}: '{value}' (expected sha256:...)")
    
    errors = []
    if missing:
        errors.append(f"Missing mandatory fields: {', '.join(missing)}")
    if invalid_patterns:
        errors.append(f"Invalid hash patterns: {', '.join(invalid_patterns)}")
    
    if errors:
        return False, "UTCS/QS evidence validation failed:\n  " + "\n  ".join(errors)
    
    return True, "UTCS/QS evidence validation passed"

def validate_file_references(manifest_data, manifest_path):
    """Verify that referenced files exist."""
    manifest_dir = Path(manifest_path).parent
    missing_files = []
    
    # Check SBOM file
    sbom_path = get_nested_value(manifest_data, 'evidence.sbom.path')
    if sbom_path:
        sbom_file = manifest_dir / sbom_path
        if not sbom_file.exists():
            missing_files.append(f"SBOM file: {sbom_path}")
    
    # Check signature files
    signatures = get_nested_value(manifest_data, 'evidence.signatures')
    if isinstance(signatures, list):
        for sig in signatures:
            if isinstance(sig, dict) and 'path' in sig:
                sig_file = manifest_dir / sig['path']
                if not sig_file.exists():
                    missing_files.append(f"Signature file: {sig['path']}")
    
    # Check artifact files
    artifacts = get_nested_value(manifest_data, 'artifacts')
    if isinstance(artifacts, list):
        for artifact in artifacts:
            if isinstance(artifact, dict) and 'path' in artifact:
                artifact_file = manifest_dir / artifact['path']
                if not artifact_file.exists():
                    missing_files.append(f"Artifact file: {artifact['path']}")
    
    if missing_files:
        return False, f"Referenced files not found:\n  " + "\n  ".join(missing_files)
    
    return True, "File reference validation passed"

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
        files_ok, files_msg = validate_file_references(manifest, manifest_path)
        print(f"File References: {'PASS' if files_ok else 'FAIL'}")
        if not files_ok:
            print(f"  {files_msg}")
            all_passed = False
    else:
        print("Evidence Check: SKIP - Schema validation failed")
        print("File References: SKIP - Schema validation failed")
    
    return all_passed

def main():
    """Main entry point."""
    manifest_paths = sys.argv[1:]
    
    if not manifest_paths:
        print("Usage: python validate_pax.py <manifest_file1> [<manifest_file2>...]")
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

if __name__ == '__main__':
    main()

