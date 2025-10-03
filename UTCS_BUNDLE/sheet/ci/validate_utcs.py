#!/usr/bin/env python3
"""
UTCS v5.0 Bundle Validator

Validates UTCS bundles against the v5.0 manifest schema and enforcement rules.

Usage:
    python validate_utcs.py --manifest manifest.utcs.yaml [--check-crosswalk]
    python validate_utcs.py --help
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

try:
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    print("ERROR: jsonschema not installed. Install with: pip install jsonschema")
    sys.exit(1)


# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
BUNDLE_ROOT = (SCRIPT_DIR / "../..").resolve()

SCHEMA_V5_PATH = BUNDLE_ROOT / "content/schemas/utcs.manifest.v5.json"
SHA256_PATTERN = re.compile(r"^[a-f0-9]{64}$", re.IGNORECASE)
BRIDGE_PATTERN = re.compile(r"^QS→FWD→UE→FE→CB→QB$")
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")

# Required UiX sections
REQUIRED_UIX_SECTIONS = ["context", "content", "structure", "style", "sheet"]

# Valid TFA layers
TFA_LAYERS = {"QS", "FWD", "UE", "FE", "CB", "QB"}

# Valid PAx subpackages (OB/OFF only)
PAX_SUBPACKAGES = {"OB", "OFF"}


# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------
def load_yaml(path: Path) -> Dict[str, Any]:
    """Load YAML file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR: Failed to load YAML from {path}: {e}")
        sys.exit(1)


def load_json(path: Path) -> Dict[str, Any]:
    """Load JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to load JSON from {path}: {e}")
        sys.exit(1)


def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"WARNING: Failed to compute hash for {file_path}: {e}")
        return ""


# -----------------------------------------------------------------------------
# Validation Functions
# -----------------------------------------------------------------------------
def validate_schema(manifest: Dict[str, Any], schema: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate manifest against JSON schema."""
    issues = []
    try:
        validator = Draft202012Validator(schema)
        errors = list(validator.iter_errors(manifest))
        for error in errors:
            path = ".".join(str(p) for p in error.path) if error.path else "root"
            issues.append(f"Schema validation error at {path}: {error.message}")
    except Exception as e:
        issues.append(f"Schema validation exception: {e}")
    
    return len(issues) == 0, issues


def validate_basic_structure(manifest: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate basic manifest structure."""
    issues = []
    
    # Check required top-level fields
    required_fields = ["bundle_id", "schema", "program", "semver", "created_utc", "uix", "hashes"]
    for field in required_fields:
        if field not in manifest:
            issues.append(f"Missing required field: {field}")
    
    # Validate schema version
    if manifest.get("schema") != "utcs.manifest.v5":
        issues.append(f"Invalid schema version: {manifest.get('schema')} (expected: utcs.manifest.v5)")
    
    # Validate bundle_id pattern
    bundle_id = manifest.get("bundle_id", "")
    if not bundle_id.startswith("utcs-bundle-"):
        issues.append(f"Invalid bundle_id format: {bundle_id} (must start with 'utcs-bundle-')")
    
    # Validate semver
    semver = manifest.get("semver", "")
    if not SEMVER_PATTERN.match(str(semver)):
        issues.append(f"Invalid semver format: {semver} (expected: X.Y.Z)")
    
    # Validate bridge if present
    bridge = manifest.get("bridge", "")
    if bridge and not BRIDGE_PATTERN.match(bridge):
        issues.append(f"Invalid bridge format: {bridge} (expected: QS→FWD→UE→FE→CB→QB)")
    
    return len(issues) == 0, issues


def validate_uix_sections(manifest: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate UiX threading sections."""
    issues = []
    
    uix = manifest.get("uix", {})
    if not isinstance(uix, dict):
        issues.append("UiX section must be a dictionary")
        return False, issues
    
    # Check required sections
    for section in REQUIRED_UIX_SECTIONS:
        if section not in uix:
            issues.append(f"Missing required UiX section: {section}")
        elif not isinstance(uix[section], list):
            issues.append(f"UiX section '{section}' must be a list")
    
    return len(issues) == 0, issues


def validate_file_references(manifest: Dict[str, Any], bundle_root: Path) -> Tuple[bool, List[str]]:
    """Validate that referenced files exist."""
    issues = []
    
    # Check UiX file references
    uix = manifest.get("uix", {})
    for section, files in uix.items():
        if isinstance(files, list):
            for file_path in files:
                full_path = bundle_root / file_path
                if not full_path.exists():
                    issues.append(f"UiX {section} file not found: {file_path}")
    
    # Check SBOM
    attestations = manifest.get("attestations", {})
    sbom_path = attestations.get("sbom")
    if sbom_path:
        full_path = bundle_root / sbom_path
        if not full_path.exists():
            issues.append(f"SBOM file not found: {sbom_path}")
    
    # Check signatures
    signatures = attestations.get("signatures", [])
    for sig_path in signatures:
        if isinstance(sig_path, str):
            full_path = bundle_root / sig_path
            if not full_path.exists():
                issues.append(f"Signature file not found: {sig_path}")
    
    return len(issues) == 0, issues


def validate_hashes(manifest: Dict[str, Any], bundle_root: Path) -> Tuple[bool, List[str]]:
    """Validate file hashes."""
    issues = []
    
    hashes_section = manifest.get("hashes", {})
    algo = hashes_section.get("algo")
    
    if algo != "sha256":
        issues.append(f"Unsupported hash algorithm: {algo} (only sha256 supported)")
        return False, issues
    
    files = hashes_section.get("files", [])
    for file_entry in files:
        if not isinstance(file_entry, dict):
            continue
        
        file_path = file_entry.get("path")
        expected_digest = file_entry.get("digest")
        
        if not file_path or not expected_digest:
            continue
        
        # Skip 'pending' hashes
        if expected_digest == "pending":
            continue
        
        # Validate digest format
        if not SHA256_PATTERN.match(expected_digest):
            issues.append(f"Invalid SHA-256 hash format for {file_path}: {expected_digest}")
            continue
        
        # Compute actual hash
        full_path = bundle_root / file_path
        if not full_path.exists():
            issues.append(f"Hash entry references non-existent file: {file_path}")
            continue
        
        actual_digest = compute_sha256(full_path)
        if actual_digest and actual_digest != expected_digest:
            issues.append(f"Hash mismatch for {file_path}: expected {expected_digest[:8]}..., got {actual_digest[:8]}...")
    
    return len(issues) == 0, issues


def validate_crosswalk(manifest: Dict[str, Any], bundle_root: Path) -> Tuple[bool, List[str]]:
    """Validate crosswalk table completeness (optional check)."""
    issues = []
    
    # Check if crosswalk files exist
    grammar_path = bundle_root / "structure/tfa_grammar.md"
    hierarchy_path = bundle_root / "structure/topic_hierarchy.md"
    
    if not grammar_path.exists():
        issues.append("Missing TFA grammar file: structure/tfa_grammar.md")
    
    if not hierarchy_path.exists():
        issues.append("Missing topic hierarchy file: structure/topic_hierarchy.md")
    
    # Basic content validation
    if grammar_path.exists():
        content = grammar_path.read_text(encoding="utf-8")
        if "domains/<DOMAIN_CODE>/ATA-" not in content:
            issues.append("TFA grammar file missing path pattern definition")
    
    if hierarchy_path.exists():
        content = hierarchy_path.read_text(encoding="utf-8")
        if "MAP Topic" not in content:
            issues.append("Topic hierarchy file missing MAP Topic column")
    
    return len(issues) == 0, issues


def validate_ethics_guard(manifest: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate ethics guard configuration."""
    issues = []
    
    ethics_guard = manifest.get("ethics_guard", [])
    if not ethics_guard:
        issues.append("Missing ethics_guard configuration")
    else:
        valid_guards = {"MAL-EEM", "MAP-EEM"}
        if isinstance(ethics_guard, list):
            for guard in ethics_guard:
                if guard not in valid_guards:
                    issues.append(f"Invalid ethics guard: {guard} (expected: MAL-EEM or MAP-EEM)")
        else:
            issues.append("ethics_guard must be a list")
    
    return len(issues) == 0, issues


# -----------------------------------------------------------------------------
# Main Validation
# -----------------------------------------------------------------------------
def validate_bundle(manifest_path: Path, check_crosswalk: bool = False) -> bool:
    """Run all validation checks."""
    print("=" * 70)
    print("UTCS v5.0 Bundle Validation")
    print("=" * 70)
    print(f"Manifest: {manifest_path}")
    print()
    
    # Load manifest
    manifest = load_yaml(manifest_path)
    bundle_root = manifest_path.parent
    
    # Load schema
    if not SCHEMA_V5_PATH.exists():
        print(f"ERROR: Schema file not found: {SCHEMA_V5_PATH}")
        return False
    
    schema = load_json(SCHEMA_V5_PATH)
    
    # Run validation checks
    all_passed = True
    validators = [
        ("Basic Structure", lambda: validate_basic_structure(manifest)),
        ("JSON Schema", lambda: validate_schema(manifest, schema)),
        ("UiX Sections", lambda: validate_uix_sections(manifest)),
        ("File References", lambda: validate_file_references(manifest, bundle_root)),
        ("File Hashes", lambda: validate_hashes(manifest, bundle_root)),
        ("Ethics Guard", lambda: validate_ethics_guard(manifest)),
    ]
    
    if check_crosswalk:
        validators.append(("Crosswalk Completeness", lambda: validate_crosswalk(manifest, bundle_root)))
    
    for name, validator in validators:
        valid, issues = validator()
        status = "✓ PASS" if valid else "✗ FAIL"
        print(f"{name:.<50} {status}")
        
        if not valid:
            for issue in issues:
                print(f"  → {issue}")
            all_passed = False
    
    print()
    if all_passed:
        print("✓ SUCCESS: UTCS bundle validated successfully")
        return True
    else:
        print("✗ FAILURE: UTCS bundle validation failed")
        return False


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="UTCS v5.0 Bundle Validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=BUNDLE_ROOT / "manifest.utcs.yaml",
        help="Path to manifest.utcs.yaml (default: UTCS_BUNDLE/manifest.utcs.yaml)",
    )
    parser.add_argument(
        "--check-crosswalk",
        action="store_true",
        help="Enable crosswalk table completeness validation",
    )
    
    args = parser.parse_args()
    
    if not args.manifest.exists():
        print(f"ERROR: Manifest file not found: {args.manifest}")
        sys.exit(1)
    
    success = validate_bundle(args.manifest, args.check_crosswalk)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
