#!/usr/bin/env python3
"""
Quantum Boundary (QB) Contract Validator

Validates QB advisory contracts to ensure proper isolation and safety boundaries.
Enforces time budgets, validation predicates, and fallback mechanisms.

Usage:
  python validate_qb_contract.py <contract_file>
"""

import argparse
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple

import yaml


def load_contract(contract_path: Path) -> Dict[str, Any]:
    """Load QB contract YAML file"""
    try:
        with open(contract_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading contract {contract_path}: {e}")
        sys.exit(1)


def validate_basic_structure(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate basic contract structure"""
    
    issues = []
    required_fields = ['role', 'topics_in', 'topics_out', 'accept_predicates', 
                      'max_age_s', 'fallback', 'utcs']
    
    for field in required_fields:
        if field not in contract:
            issues.append(f"Missing required field: {field}")
    
    # Role must be advisory
    if contract.get('role') != 'advisory':
        issues.append(f"Role must be 'advisory', got: {contract.get('role')}")
    
    return len(issues) == 0, issues


def validate_time_constraints(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate time constraints and budgets"""
    
    issues = []
    max_age_s = contract.get('max_age_s', 0)
    
    if max_age_s <= 0:
        issues.append("max_age_s must be positive")
    elif max_age_s > 60:
        issues.append(f"max_age_s {max_age_s}s exceeds recommended maximum of 60s")
    
    return len(issues) == 0, issues


def validate_predicates(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate acceptance predicates for safety"""
    
    issues = []
    predicates = contract.get('accept_predicates', [])
    
    if not predicates:
        issues.append("No acceptance predicates defined")
        return False, issues
    
    # Check for safety-critical predicates
    safety_patterns = [
        r'min_separation_nm\s*>=\s*\d+',
        r'terrain_clear\s*==\s*true',
        r'fuel.*<=.*\d+',
        r'time_to_conflict\s*>=\s*\d+'
    ]
    
    predicate_text = ' '.join(predicates)
    
    for pattern in safety_patterns:
        if not re.search(pattern, predicate_text):
            issues.append(f"Missing safety predicate pattern: {pattern}")
    
    # Validate individual predicates
    for i, predicate in enumerate(predicates):
        if not predicate.strip():
            issues.append(f"Empty predicate at index {i}")
        
        # Check for potentially unsafe operations (but allow safe comparisons)
        if ' > ' in predicate and not any(safe in predicate for safe in ['time_to_conflict', 'separation', 'altitude']):
            issues.append(f"Potentially unsafe predicate: {predicate}")
        if '!=' in predicate and 'true' not in predicate:
            issues.append(f"Potentially unsafe predicate: {predicate}")
        if '== false' in predicate:
            issues.append(f"Potentially unsafe predicate: {predicate}")
    
    return len(issues) == 0, issues


def validate_topics(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate topic configuration"""
    
    issues = []
    topics_in = contract.get('topics_in', [])
    topics_out = contract.get('topics_out', [])
    
    if not topics_in:
        issues.append("No input topics defined")
    
    if not topics_out:
        issues.append("No output topics defined")
    
    # Check topic naming conventions
    for topic in topics_in:
        if not re.match(r'^[a-z][a-z0-9/_]*[a-z0-9]$', topic):
            issues.append(f"Invalid input topic name: {topic}")
    
    for topic in topics_out:
        if not re.match(r'^[a-z][a-z0-9/_]*[a-z0-9]$', topic):
            issues.append(f"Invalid output topic name: {topic}")
    
    return len(issues) == 0, issues


def validate_utcs_requirements(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate UTCS/QS requirements"""
    
    issues = []
    utcs = contract.get('utcs', {})
    
    if not isinstance(utcs, dict):
        issues.append("UTCS section must be a dictionary")
        return False, issues
    
    required_utcs_fields = ['require_signature', 'record_backend']
    for field in required_utcs_fields:
        if field not in utcs:
            issues.append(f"Missing UTCS field: {field}")
        elif not isinstance(utcs[field], bool):
            issues.append(f"UTCS field {field} must be boolean")
    
    # Both should be true for safety
    if not utcs.get('require_signature', False):
        issues.append("UTCS signature requirement should be enabled")
    
    if not utcs.get('record_backend', False):
        issues.append("UTCS backend recording should be enabled")
    
    return len(issues) == 0, issues


def validate_fallback(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate fallback mechanism"""
    
    issues = []
    fallback = contract.get('fallback', '')
    
    if not fallback:
        issues.append("Fallback mechanism not defined")
    elif fallback.lower() in ['none', 'null', 'undefined']:
        issues.append("Unsafe fallback mechanism")
    
    return len(issues) == 0, issues


def main():
    parser = argparse.ArgumentParser(description='Validate QB advisory contract')
    parser.add_argument('contract_file', type=Path, help='QB contract YAML file')
    
    args = parser.parse_args()
    
    print("🔍 QB Contract Validation")
    print(f"Contract: {args.contract_file}")
    print("=" * 50)
    
    # Load contract
    contract = load_contract(args.contract_file)
    
    all_passed = True
    validators = [
        ("Basic Structure", validate_basic_structure),
        ("Time Constraints", validate_time_constraints),
        ("Predicates", validate_predicates),
        ("Topics", validate_topics),
        ("UTCS", validate_utcs_requirements),
        ("Fallback", validate_fallback)
    ]
    
    for name, validator in validators:
        valid, issues = validator(contract)
        print(f"{name}: {'PASS' if valid else 'FAIL'}")
        
        if not valid:
            for issue in issues:
                print(f"  ❌ {issue}")
            all_passed = False
    
    if all_passed:
        print("\n✅ SUCCESS: QB contract validated successfully")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: QB contract validation failed")
        sys.exit(1)


if __name__ == "__main__":
    main()