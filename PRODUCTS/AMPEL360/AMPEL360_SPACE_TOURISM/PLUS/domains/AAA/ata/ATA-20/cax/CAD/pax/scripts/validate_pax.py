#!/usr/bin/env python3
"""
PAx manifest validator (AMPEL360 PLUS / CAD Domain)

- Validates JSON **or** YAML manifests against package.schema.json
- Enforces UTCS/QS evidence fields and patterns for CAD domain
- Verifies referenced files exist (SBOM, signatures, CAD exports)
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

try:
    import yaml
except ImportError:
    print("❌ ERROR: Missing required package 'PyYAML'. Please install it with 'pip install pyyaml'.")
    sys.exit(1)
from jsonschema import Draft202012Validator

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SCHEMA_PATH = (SCRIPT_DIR / "../schemas/package.schema.json").resolve()

# CAD-specific patterns
CAD_PATTERNS = {
    'package_name': re.compile(r'^PLUS-CAD-[A-Z0-9-]+$'),
    'cad_export': re.compile(r'^PLUS-[A-Z0-9]+-[a-zA-Z0-9_]+-[A-Z][0-9]{2}\.(step|iges|x_t|stl)$', re.IGNORECASE),
    'canonical_hash': re.compile(r'^sha256:[a-f0-9]{64}$'),
    'version': re.compile(r'^\d+\.\d+\.\d+$')
}

# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------
def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Load JSON schema."""
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ ERROR: Cannot load schema {schema_path}: {e}")
        sys.exit(1)

def load_manifest(manifest_path: Path) -> Dict[str, Any]:
    """Load manifest (JSON or YAML)."""
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            if manifest_path.suffix.lower() in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            else:
                return json.load(f)
    except Exception as e:
        raise ValueError(f"Cannot parse manifest: {e}")

# -----------------------------------------------------------------------------
# Validation Functions
# -----------------------------------------------------------------------------
def validate_against_schema(manifest: Dict[str, Any], schema: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate manifest against JSON schema."""
    validator = Draft202012Validator(schema)
    errors = []
    
    try:
        validator.validate(manifest)
        return True, []
    except Exception as e:
        # Collect all validation errors
        for error in validator.iter_errors(manifest):
            error_path = " -> ".join(str(p) for p in error.absolute_path) if error.absolute_path else "root"
            errors.append(f"Schema violation at {error_path}: {error.message}")
        return False, errors

def validate_cad_specific_patterns(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate CAD domain-specific patterns."""
    errors = []
    
    # Check package name pattern
    package_name = manifest.get('package_name', '')
    if not CAD_PATTERNS['package_name'].match(package_name):
        errors.append(f"Package name '{package_name}' should match pattern: PLUS-CAD-<TYPE>-<ID>")
    
    # Check canonical hash format
    canonical_hash = manifest.get('canonical_hash', '')
    if canonical_hash != 'TBD' and not CAD_PATTERNS['canonical_hash'].match(canonical_hash):
        errors.append(f"Canonical hash should be 'TBD' or match sha256 pattern")
    
    # Check UTCS header version
    utcs_header = manifest.get('utcs_header', {})
    version = utcs_header.get('version', '')
    if version and not CAD_PATTERNS['version'].match(version):
        errors.append(f"Version '{version}' should follow semantic versioning (x.y.z)")
    
    # Check CAD-specific package kind
    package = manifest.get('package', {})
    kind = package.get('kind', '')
    valid_kinds = ['OB-CAD-TOOL', 'OFF-CAD-EXPORTER', 'OFF-CAD-VALIDATOR']
    if kind and kind not in valid_kinds:
        errors.append(f"Package kind '{kind}' should be one of: {valid_kinds}")
    
    return len(errors) == 0, '; '.join(errors)

def validate_evidence_present(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate that required evidence fields are present."""
    evidence = manifest.get('evidence', {})
    required_fields = ['canonical_hash', 'sbom', 'signatures', 'security_policy_id']
    missing = [field for field in required_fields if field not in evidence]
    
    if missing:
        return False, f"Missing evidence fields: {missing}"
    
    # Check SBOM structure
    sbom = evidence.get('sbom', {})
    if not isinstance(sbom, dict) or 'path' not in sbom or 'hash' not in sbom:
        return False, "SBOM evidence must have 'path' and 'hash' fields"
    
    return True, ""

def validate_evidence_patterns(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate evidence field patterns."""
    evidence = manifest.get('evidence', {})
    errors = []
    
    # Check canonical hash pattern
    canonical_hash = evidence.get('canonical_hash', '')
    if canonical_hash and not CAD_PATTERNS['canonical_hash'].match(canonical_hash):
        errors.append("Evidence canonical_hash must match sha256 pattern")
    
    # Check SBOM hash pattern
    sbom = evidence.get('sbom', {})
    if isinstance(sbom, dict):
        sbom_hash = sbom.get('hash', '')
        if sbom_hash and not CAD_PATTERNS['canonical_hash'].match(sbom_hash):
            errors.append("SBOM hash must match sha256 pattern")
    
    # Check signature types
    signatures = evidence.get('signatures', [])
    valid_sig_types = ['cosign', 'in-toto', 'x509']
    for sig in signatures:
        if isinstance(sig, dict):
            sig_type = sig.get('type', '')
            if sig_type and sig_type not in valid_sig_types:
                errors.append(f"Invalid signature type '{sig_type}', must be one of: {valid_sig_types}")
    
    return len(errors) == 0, '; '.join(errors)

def validate_file_references(manifest: Dict[str, Any], manifest_path: Path) -> Tuple[bool, str]:
    """Validate that referenced files exist."""
    base_dir = manifest_path.parent
    missing_files = []
    
    # Check SBOM file
    evidence = manifest.get('evidence', {})
    sbom = evidence.get('sbom', {})
    if isinstance(sbom, dict) and 'path' in sbom:
        sbom_path = base_dir / sbom['path']
        if not sbom_path.exists():
            missing_files.append(f"SBOM file: {sbom['path']}")
    
    # Check signature files
    signatures = evidence.get('signatures', [])
    for sig in signatures:
        if isinstance(sig, dict) and 'path' in sig:
            sig_path = base_dir / sig['path']
            if not sig_path.exists():
                missing_files.append(f"Signature file: {sig['path']}")
    
    # Check CAD export references (if any)
    package = manifest.get('package', {})
    cad_specific = package.get('cad_specific', {})
    export_presets = cad_specific.get('export_presets', {})
    
    for preset_name, preset_config in export_presets.items():
        if isinstance(preset_config, dict) and 'output_path' in preset_config:
            export_path = base_dir / preset_config['output_path']
            if not export_path.exists():
                missing_files.append(f"CAD export: {preset_config['output_path']} (preset: {preset_name})")
    
    if missing_files:
        return False, f"Missing files: {missing_files}"
    
    return True, ""

def validate_one_manifest(manifest_path: Path, schema: Dict[str, Any]) -> bool:
    """Validate a single manifest file."""
    print(f"\n🔍 Validating: {manifest_path.name}")
    
    try:
        manifest = load_manifest(manifest_path)
    except Exception as e:
        print(f"  ❌ Failed to load manifest: {e}")
        return False
    
    success = True
    
    # Schema validation
    schema_valid, schema_errors = validate_against_schema(manifest, schema)
    if not schema_valid:
        print("  ❌ Schema validation failed:")
        for error in schema_errors:
            print(f"     • {error}")
        success = False
    else:
        print("  ✅ Schema validation passed")
    
    # CAD-specific pattern validation
    patterns_valid, patterns_error = validate_cad_specific_patterns(manifest)
    if not patterns_valid:
        print(f"  ❌ CAD pattern validation failed: {patterns_error}")
        success = False
    else:
        print("  ✅ CAD patterns valid")
    
    # Evidence presence validation
    evidence_present, evidence_error = validate_evidence_present(manifest)
    if not evidence_present:
        print(f"  ❌ Evidence validation failed: {evidence_error}")
        success = False
    else:
        print("  ✅ Evidence fields present")
    
    # Evidence pattern validation
    evidence_patterns_valid, evidence_patterns_error = validate_evidence_patterns(manifest)
    if not evidence_patterns_valid:
        print(f"  ❌ Evidence pattern validation failed: {evidence_patterns_error}")
        success = False
    else:
        print("  ✅ Evidence patterns valid")
    
    # File reference validation
    files_valid, files_error = validate_file_references(manifest, manifest_path)
    if not files_valid:
        print(f"  ⚠️  File reference validation failed: {files_error}")
        # Note: File references are warnings, not hard failures for CI
        print("     (This is a warning - files may be generated during build)")
    else:
        print("  ✅ File references valid")
    
    if success:
        print(f"  ✅ {manifest_path.name} - ALL VALIDATIONS PASSED")
    else:
        print(f"  ❌ {manifest_path.name} - VALIDATION FAILED")
    
    return success

# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------
def main() -> None:
    # Parse arguments
    if '--schema' in sys.argv:
        schema_idx = sys.argv.index('--schema')
        if schema_idx + 1 >= len(sys.argv):
            print("❌ ERROR: --schema requires a path argument")
            sys.exit(1)
        schema_path = Path(sys.argv[schema_idx + 1]).resolve()
        
        if '--root' in sys.argv:
            root_idx = sys.argv.index('--root')
            if root_idx + 1 >= len(sys.argv):
                print("❌ ERROR: --root requires a path argument")
                sys.exit(1)
            root_dir = Path(sys.argv[root_idx + 1]).resolve()
        else:
            print("❌ ERROR: --root is required when --schema is used")
            sys.exit(1)
        
        # Find all manifest files in root directory
        manifest_files = []
        for pattern in ['**/*.json', '**/*.yaml', '**/*.yml']:
            manifest_files.extend(root_dir.glob(pattern))
        
        schema = load_schema(schema_path)
        all_passed = True
        
        print(f"🔍 PAx Validation (CAD Domain)")
        print(f"Schema: {schema_path}")
        print(f"Root: {root_dir}")
        print("=" * 60)
        
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
        
        print(f"🔍 PAx Validation (CAD Domain)")
        print(f"Schema: {DEFAULT_SCHEMA_PATH}")
        print("=" * 60)
        
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