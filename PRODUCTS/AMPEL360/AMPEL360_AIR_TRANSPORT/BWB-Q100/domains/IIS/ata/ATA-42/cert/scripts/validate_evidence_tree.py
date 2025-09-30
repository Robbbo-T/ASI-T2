#!/usr/bin/env python3
"""
Validate evidence tree structure and compliance with certification standards.
"""

import argparse
import json
import os
import sys
import yaml
from pathlib import Path

def load_evidence_rules(rules_file):
    """Load evidence validation rules from YAML file."""
    with open(rules_file, 'r') as f:
        return yaml.safe_load(f)

def validate_evidence_tree(evidence_root, rules):
    """Validate evidence tree structure against rules."""
    results = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'info': []
    }
    
    evidence_path = Path(evidence_root)
    
    if not evidence_path.exists():
        results['errors'].append(f"Evidence root directory does not exist: {evidence_root}")
        results['valid'] = False
        return results
    
    # Check required top-level directories
    required_dirs = rules.get('required_directories', [])
    for dir_name in required_dirs:
        dir_path = evidence_path / dir_name
        if not dir_path.exists():
            results['errors'].append(f"Required directory missing: {dir_name}")
            results['valid'] = False
        else:
            results['info'].append(f"Required directory found: {dir_name}")
    
    # Check for deprecated directories
    deprecated_dirs = rules.get('deprecated_directories', [])
    for dir_name in deprecated_dirs:
        dir_path = evidence_path / dir_name
        if dir_path.exists():
            results['warnings'].append(f"Deprecated directory found: {dir_name}")
    
    # Validate standard-specific requirements
    standard_rules = rules.get('standards', {})
    for standard, std_rules in standard_rules.items():
        std_path = evidence_path / standard
        if std_path.exists():
            validate_standard(std_path, std_rules, results, standard)
        else:
            results['warnings'].append(f"Standard directory not found: {standard}")
    
    return results

def validate_standard(std_path, rules, results, standard_name):
    """Validate a specific standard's evidence structure."""
    required_subdirs = rules.get('required_subdirectories', [])
    for subdir in required_subdirs:
        subdir_path = std_path / subdir
        if not subdir_path.exists():
            results['errors'].append(f"Required subdirectory missing for {standard_name}: {subdir}")
            results['valid'] = False
        else:
            # Check for evidence files
            has_files = False
            for item in subdir_path.rglob('*'):
                if item.is_file():
                    has_files = True
                    break
            
            if not has_files:
                results['warnings'].append(f"No evidence files in {standard_name}/{subdir}")
    
    # Check for required files
    required_files = rules.get('required_files', [])
    for file_pattern in required_files:
        if not list(std_path.glob(file_pattern)):
            results['warnings'].append(f"No files matching pattern {file_pattern} in {standard_name}")

def print_results(results):
    """Print validation results in a readable format."""
    print("\n" + "="*60)
    print("EVIDENCE TREE VALIDATION RESULTS")
    print("="*60)
    
    if results['info']:
        print("\n✅ INFO:")
        for info in results['info']:
            print(f"  • {info}")
    
    if results['warnings']:
        print("\n⚠️  WARNINGS:")
        for warning in results['warnings']:
            print(f"  • {warning}")
    
    if results['errors']:
        print("\n❌ ERRORS:")
        for error in results['errors']:
            print(f"  • {error}")
    
    print("\n" + "="*60)
    if results['valid']:
        print("✅ VALIDATION PASSED")
    else:
        print("❌ VALIDATION FAILED")
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description='Validate evidence tree structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Example usage:
  python validate_evidence_tree.py --root evidence --rules schemas/evidence_rules.yaml
  python validate_evidence_tree.py --root evidence --rules schemas/evidence_rules.yaml --json
        '''
    )
    parser.add_argument('--root', required=True, help='Root directory of evidence tree')
    parser.add_argument('--rules', required=True, help='YAML file with validation rules')
    parser.add_argument('--json', action='store_true', help='Output results as JSON')
    args = parser.parse_args()
    
    try:
        rules = load_evidence_rules(args.rules)
        results = validate_evidence_tree(args.root, rules)
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print_results(results)
        
        if not results['valid']:
            sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML rules file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
