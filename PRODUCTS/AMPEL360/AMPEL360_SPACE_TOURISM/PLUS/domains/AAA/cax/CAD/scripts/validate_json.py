#!/usr/bin/env python3
"""
JSON Schema Validator for CAD Domain

Validates JSON files against their schemas:
- CAD manifests against cad_manifest.schema.json
- QOx problems against qox_problem.schema.json
- PAx packages against package.schema.json

Usage:
  python validate_json.py <schema_dir> <target_dir1> [<target_dir2> ...]
  python validate_json.py schemas/ geometry/metadata/ qox_bridge/problems/
"""

from __future__ import annotations

import json
import sys
import glob
from pathlib import Path
from typing import Dict, List, Tuple, Any

try:
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    print("ERROR: jsonschema package required. Install with: pip install jsonschema")
    sys.exit(1)

# Schema file mappings
SCHEMA_MAPPINGS = {
    "cad_manifest.schema.json": ["**/*.cad.json", "**/metadata/*.json"],
    "qox_problem.schema.json": ["**/*.qubo.json", "**/problems/*.json"],
    "package.schema.json": ["**/manifests/*.json", "**/pax/**/*.json"]
}

def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Load and parse JSON schema file."""
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        return schema
    except Exception as e:
        print(f"ERROR: Failed to load schema {schema_path}: {e}")
        sys.exit(1)

def load_json_file(json_path: Path) -> Dict[str, Any]:
    """Load and parse JSON file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        raise ValueError(f"Invalid JSON: {e}")

def validate_json_against_schema(json_data: Dict[str, Any], schema: Dict[str, Any], json_path: Path) -> Tuple[bool, List[str]]:
    """Validate JSON data against schema."""
    validator = Draft202012Validator(schema)
    errors = []
    
    try:
        validator.validate(json_data)
        return True, []
    except ValidationError as e:
        errors.append(f"Validation error: {e.message}")
        if e.path:
            errors.append(f"  Path: {' -> '.join(str(p) for p in e.path)}")
        return False, errors

def find_json_files(target_dirs: List[Path], patterns: List[str]) -> List[Path]:
    """Find JSON files matching patterns in target directories."""
    json_files = []
    
    for target_dir in target_dirs:
        if not target_dir.exists():
            print(f"WARNING: Directory {target_dir} does not exist")
            continue
            
        for pattern in patterns:
            matches = list(target_dir.glob(pattern))
            json_files.extend([f for f in matches if f.is_file() and f.suffix == '.json'])
    
    return sorted(set(json_files))

def validate_schema_dir(schema_dir: Path, target_dirs: List[Path]) -> bool:
    """Validate all JSON files against appropriate schemas."""
    if not schema_dir.exists():
        print(f"ERROR: Schema directory {schema_dir} does not exist")
        return False
    
    all_valid = True
    total_files = 0
    
    for schema_file, patterns in SCHEMA_MAPPINGS.items():
        schema_path = schema_dir / schema_file
        if not schema_path.exists():
            print(f"WARNING: Schema {schema_path} not found, skipping")
            continue
        
        print(f"\n📋 Validating against {schema_file}")
        print("=" * 50)
        
        schema = load_schema(schema_path)
        json_files = find_json_files(target_dirs, patterns)
        
        if not json_files:
            print(f"  No JSON files found matching patterns: {patterns}")
            continue
        
        schema_valid = True
        for json_file in json_files:
            total_files += 1
            try:
                json_data = load_json_file(json_file)
                is_valid, errors = validate_json_against_schema(json_data, schema, json_file)
                
                if is_valid:
                    print(f"  ✅ {json_file.relative_to(Path.cwd())}")
                else:
                    print(f"  ❌ {json_file.relative_to(Path.cwd())}")
                    for error in errors:
                        print(f"     {error}")
                    schema_valid = False
                    all_valid = False
                    
            except Exception as e:
                print(f"  ❌ {json_file.relative_to(Path.cwd())}: {e}")
                schema_valid = False
                all_valid = False
        
        if schema_valid and json_files:
            print(f"  ✅ All {len(json_files)} files valid for {schema_file}")
    
    print(f"\n📊 Summary")
    print("=" * 50)
    if total_files == 0:
        print("  ⚠️  No JSON files found to validate")
        return True  # Not an error if no files to validate
    elif all_valid:
        print(f"  ✅ All {total_files} JSON files passed validation")
        return True
    else:
        print(f"  ❌ Some files failed validation")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python validate_json.py <schema_dir> <target_dir1> [<target_dir2> ...]")
        print("\nExample:")
        print("  python validate_json.py schemas/ geometry/metadata/ qox_bridge/problems/")
        sys.exit(1)
    
    schema_dir = Path(sys.argv[1]).resolve()
    target_dirs = [Path(d).resolve() for d in sys.argv[2:]]
    
    print("🔍 JSON Schema Validation")
    print("=" * 50)
    print(f"Schema directory: {schema_dir}")
    print(f"Target directories: {[str(d) for d in target_dirs]}")
    
    success = validate_schema_dir(schema_dir, target_dirs)
    
    if success:
        print("\n✅ SUCCESS: JSON validation completed successfully")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: JSON validation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()