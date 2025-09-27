#!/usr/bin/env python3
"""
PAx manifest validator (BWB-Q100 / LCC)

Enhanced version for LCC domain with BWB-specific validations.
Extends the AAA domain validator with autopilot-specific checks.

Usage:
  python validate_pax.py <manifest1> [<manifest2> ...]
  python validate_pax.py --root <directory>
"""

import json
import os
import sys
import re
import glob
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

import yaml
from jsonschema import Draft202012Validator


# -----------------------------------------------------------------------------
# ATA22 Health Monitor for AQUA OS Integration
# -----------------------------------------------------------------------------
class ATA22HealthMonitor:
    """AQUA OS validator for autopilot health monitoring"""
    
    def __init__(self):
        self.health_data = {}
    
    def _max_skew_ms(self) -> float:
        """Get maximum surface synchronization skew"""
        return self.health_data.get('sync_skew_ms_p95', 0.0)
    
    def _voter_ok(self) -> bool:
        """Check sensor redundancy voter status"""
        return self.health_data.get('sensor_redundancy', True)
    
    def _lag_ok_us(self) -> bool:
        """Check actuator response lag"""
        return self.health_data.get('actuator_lag_us', 0) < 100
    
    def _span_load_err(self) -> float:
        """Get span load distribution error"""
        return self.health_data.get('span_load_error', 0.0)
    
    def _cross_coupling_ratio(self) -> float:
        """Get cross-axis coupling ratio"""
        return self.health_data.get('cross_coupling_max', 0.0)
    
    def aggregate_health_score(self, checks: Dict[str, bool]) -> float:
        """Aggregate health checks into single score"""
        if not checks:
            return 0.0
        
        passed = sum(1 for result in checks.values() if result)
        return passed / len(checks)
    
    def validate_autopilot_health(self) -> float:
        """Validate autopilot health according to BWB-Q100 requirements"""
        checks = {
            'control_surface_sync': self._max_skew_ms() <= 5,
            'sensor_redundancy': self._voter_ok(),
            'actuator_response': self._lag_ok_us(),
            'span_load_distribution': self._span_load_err() <= 0.05,
            'elevon_coupling': self._cross_coupling_ratio() <= 0.15
        }
        return self.aggregate_health_score(checks)


# -----------------------------------------------------------------------------
# PAx Validation Functions
# -----------------------------------------------------------------------------
def validate_lcc_specific(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate LCC domain specific requirements"""
    issues = []
    
    # Check for BWB-specific fields
    if 'bwb_config' in manifest:
        bwb_config = manifest['bwb_config']
        
        # Validate surface count
        surfaces = bwb_config.get('surfaces', 0)
        if surfaces != 35:
            issues.append(f"BWB-Q100 requires 35 surfaces, got {surfaces}")
        
        # Validate control law type
        control_law = bwb_config.get('control_law', '')
        if control_law != 'QAFbW':
            issues.append(f"Expected QAFbW control law, got {control_law}")
    
    # Check for ARINC-653 compliance
    if 'partition' in manifest:
        partition = manifest['partition']
        dal = partition.get('dal', '')
        if dal != 'A':
            issues.append(f"LCC domain requires DAL A, got {dal}")
    
    return len(issues) == 0, '\n'.join(issues)


def validate_evidence_present(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate required evidence fields are present"""
    required_evidence = [
        'utcs.canonical_hash',
        'verification.mcdc',
        'verification.hil_runs',
        'qb_advisory.enabled'
    ]
    
    issues = []
    for field_path in required_evidence:
        obj = manifest
        for key in field_path.split('.'):
            if isinstance(obj, dict) and key in obj:
                obj = obj[key]
            else:
                issues.append(f"Missing evidence field: {field_path}")
                break
    
    return len(issues) == 0, '\n'.join(issues)


def validate_evidence_patterns(manifest: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate evidence field patterns and values"""
    issues = []
    
    verification = manifest.get('verification', {})
    
    # MC/DC coverage must be 1.0
    mcdc = verification.get('mcdc', 0.0)
    if mcdc != 1.0:
        issues.append(f"MC/DC coverage must be 1.0, got {mcdc}")
    
    # Deadline misses must be 0
    deadline_misses = verification.get('deadline_misses', -1)
    if deadline_misses != 0:
        issues.append(f"Deadline misses must be 0, got {deadline_misses}")
    
    # Cross-axis coupling limit
    coupling = verification.get('cross_axis_coupling_max', 1.0)
    if coupling > 0.15:
        issues.append(f"Cross-axis coupling {coupling} exceeds limit 0.15")
    
    return len(issues) == 0, '\n'.join(issues)


def validate_file_references(manifest: Dict[str, Any], manifest_path: Path) -> Tuple[bool, str]:
    """Validate referenced files exist"""
    issues = []
    base_dir = manifest_path.parent
    
    # Check SBOM reference
    utcs = manifest.get('utcs', {})
    sbom_path = utcs.get('sbom', '')
    if sbom_path:
        full_path = base_dir / sbom_path
        if not full_path.exists() and os.getenv('PAX_STRICT_FILES') == '1':
            issues.append(f"Missing SBOM file: {sbom_path}")
    
    return len(issues) == 0, '\n'.join(issues)


def validate_one_manifest(manifest_path: Path, schema: Optional[Dict[str, Any]] = None) -> bool:
    """Validate a single PAx manifest"""
    print(f"\n🔍 Validating: {manifest_path.name}")
    
    try:
        with open(manifest_path, 'r') as f:
            if manifest_path.suffix.lower() == '.json':
                manifest = json.load(f)
            else:
                manifest = yaml.safe_load(f)
    except Exception as e:
        print(f"  ❌ Failed to load manifest: {e}")
        return False
    
    ok = True
    
    # Schema validation
    if schema:
        validator = Draft202012Validator(schema)
        errors = list(validator.iter_errors(manifest))
        if errors:
            print("  ❌ Schema validation failed:")
            for error in errors[:3]:  # Limit output
                print(f"    {error.message}")
            ok = False
        else:
            print("  ✅ Schema validation passed")
    
    # LCC-specific validation
    lcc_ok, lcc_msg = validate_lcc_specific(manifest)
    print(f"  {'✅' if lcc_ok else '❌'} LCC validation: {'PASS' if lcc_ok else 'FAIL'}")
    if not lcc_ok:
        print(f"    {lcc_msg.replace(chr(10), chr(10) + '    ')}")
        ok = False
    
    # Evidence validation
    e_ok, e_msg = validate_evidence_present(manifest)
    print(f"  {'✅' if e_ok else '❌'} Evidence present: {'PASS' if e_ok else 'FAIL'}")
    if not e_ok:
        print(f"    {e_msg.replace(chr(10), chr(10) + '    ')}")
        ok = False
    
    r_ok, r_msg = validate_evidence_patterns(manifest)
    print(f"  {'✅' if r_ok else '❌'} Evidence patterns: {'PASS' if r_ok else 'FAIL'}")
    if not r_ok:
        print(f"    {r_msg.replace(chr(10), chr(10) + '    ')}")
        ok = False
    
    f_ok, f_msg = validate_file_references(manifest, manifest_path)
    print(f"  {'✅' if f_ok else '❌'} File references: {'PASS' if f_ok else 'FAIL'}")
    if not f_ok:
        print(f"    {f_msg.replace(chr(10), chr(10) + '    ')}")
        ok = False
    
    return ok


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate PAx manifests (LCC domain)')
    parser.add_argument('manifests', nargs='*', help='Manifest files to validate')
    parser.add_argument('--root', type=Path, help='Root directory to search for manifests')
    parser.add_argument('--schema', type=Path, help='JSON schema file')
    
    args = parser.parse_args()
    
    print("🔍 PAx Validation (LCC Domain)")
    print("=" * 50)
    
    # Load schema if provided
    schema = None
    if args.schema and args.schema.exists():
        with open(args.schema, 'r') as f:
            schema = json.load(f)
        print(f"Schema: {args.schema}")
    
    # Collect manifests
    manifests = []
    if args.root:
        for ext in ['*.json', '*.yaml', '*.yml']:
            manifests.extend(Path(args.root).rglob(ext))
    
    manifests.extend(Path(p) for p in args.manifests)
    
    if not manifests:
        print("❌ No manifests found to validate")
        sys.exit(1)
    
    all_passed = True
    for manifest_path in manifests:
        if manifest_path.exists():
            if not validate_one_manifest(manifest_path, schema):
                all_passed = False
        else:
            print(f"❌ Manifest not found: {manifest_path}")
            all_passed = False
    
    if all_passed:
        print("\n✅ SUCCESS: All PAx manifests validated successfully")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: One or more PAx manifests failed validation")
        sys.exit(1)


if __name__ == "__main__":
    main()