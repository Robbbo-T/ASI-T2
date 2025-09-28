#!/usr/bin/env python3
"""
Naming Convention Guard for CAD Domain

Enforces naming conventions for AMPEL360 PLUS space vehicle design files:
- CAD exports: PLUS-<MODULE>-<FEATURE>-<REV>.<ext>
- JSON manifests: PLUS-<TYPE>-<ID>.json
- Problem definitions: PLUS-<DOMAIN>-<PROBLEM>-QUBO-<ID>.json
- Package names: PLUS-CAD-<TYPE>-<ID>

Usage:
  python naming_guard.py <base_dir>
  python naming_guard.py CAD/
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Pattern

# Naming patterns for different file types
NAMING_PATTERNS = {
    # CAD export files
    'cad_exports': {
        # Regex pattern components for CAD export files:
        #   ^PLUS-           : Start of string, literal 'PLUS-'
        #   [A-Z0-9]+        : <MODULE> (uppercase letters and digits, one or more)
        #   -                : Literal dash
        #   [a-zA-Z0-9_]+    : <FEATURE> (letters, digits, or underscore, one or more)
        #   -                : Literal dash
        #   [A-Z][0-9]{2}    : <REV> (uppercase letter followed by two digits)
        #   \.               : Literal dot
        #   (step|iges|x_t|stl|parasolid) : Allowed file extensions
        #   $                : End of string
        'pattern': re.compile(
            r'^'                       # Start of string
            r'PLUS-'                   # Literal 'PLUS-'
            r'(?P<module>[A-Z0-9]+)'   # <MODULE>
            r'-'
            r'(?P<feature>[a-zA-Z0-9_]+)' # <FEATURE>
            r'-'
            r'(?P<rev>[A-Z][0-9]{2})'  # <REV>
            r'\.'
            r'(?P<ext>step|iges|x_t|stl|parasolid)' # Extension
            r'$',
            re.IGNORECASE
        ),
        'description': 'CAD exports should follow: PLUS-<MODULE>-<FEATURE>-<REV>.<ext>',
        'examples': ['PLUS-OML-window-A02.step', 'PLUS-TPS-tiling-v05.iges'],
        'directories': ['geometry/exports', 'structure/exports', 'tps/exports']
    },
    
    # CAD manifest files
    'cad_manifests': {
        'pattern': re.compile(r'^PLUS-[A-Z0-9]+-[A-Z0-9]+(\.cad)?\.json$'),
        'description': 'CAD manifests should follow: PLUS-<TYPE>-<ID>.json or PLUS-<TYPE>-<ID>.cad.json',
        'examples': ['PLUS-OML-A02.cad.json', 'PLUS-STRUCT-B03.json'],
        'directories': ['geometry/metadata', 'structure/metadata', 'tps/metadata']
    },
    
    # QOx problem files
    'qox_problems': {
        'pattern': re.compile(r'^PLUS-[A-Z0-9]+-[A-Z0-9]+-QUBO-[0-9]{3}\.json$'),
        'description': 'QOx problems should follow: PLUS-<DOMAIN>-<PROBLEM>-QUBO-<ID>.json',
        'examples': ['PLUS-TPS-TILING-QUBO-001.json', 'PLUS-STRUCT-TOPOLOGY-QUBO-002.json'],
        'directories': ['qox_bridge/problems']
    },
    
    # Package manifest files
    'package_manifests': {
        'pattern': re.compile(r'^PLUS-CAD-[A-Z0-9-]+\.json$'),
        'description': 'Package manifests should follow: PLUS-CAD-<TYPE>-<ID>.json',
        'examples': ['PLUS-CAD-EXPORTER-001.json', 'PLUS-CAD-VALIDATOR-A02.json'],
        'directories': ['pax/OB/manifests', 'pax/OFF/manifests']
    },
    
    # YAML configuration files
    'yaml_configs': {
        'pattern': re.compile(r'^[a-z0-9_.-]+\.(yaml|yml)$'),
        'description': 'YAML configs should use lowercase with hyphens/underscores/dots',
        'examples': ['partition.example.yaml', 'cad-ci.exporter.yaml'],
        'directories': ['pax/OB/manifests', 'pax/OFF/oci']
    }
}

# Directory-specific naming rules
DIRECTORY_PATTERNS = {
    'geometry': re.compile(r'^[a-z_]+$'),
    'structure': re.compile(r'^[a-z_]+$'),
    'tps': re.compile(r'^[a-z_]+$'),
    'mdo': re.compile(r'^[a-z_]+$'),
    'interfaces': re.compile(r'^[a-z_]+$'),
    'qox_bridge': re.compile(r'^[a-z_]+$')
}

def find_files_in_directories(base_dir: Path, directories: List[str], extensions: List[str] = None) -> List[Path]:
    """Find files in specified directories with optional extension filtering."""
    files = []
    
    for dir_pattern in directories:
        for match_dir in base_dir.rglob(dir_pattern):
            if match_dir.is_dir():
                for file_path in match_dir.iterdir():
                    if file_path.is_file():
                        if extensions is None or file_path.suffix.lower().lstrip('.') in extensions:
                            files.append(file_path)
    
    return files

def check_pattern_compliance(files: List[Path], pattern_info: Dict) -> List[Tuple[Path, str]]:
    """Check files against naming pattern."""
    violations = []
    pattern = pattern_info['pattern']
    description = pattern_info['description']
    
    for file_path in files:
        if not pattern.match(file_path.name):
            violations.append((file_path, description))
    
    return violations

def check_directory_naming(base_dir: Path) -> List[Tuple[Path, str]]:
    """Check directory naming conventions."""
    violations = []
    
    for dir_path in base_dir.rglob('*'):
        if dir_path.is_dir() and dir_path != base_dir:
            # Skip hidden directories and git directories
            if dir_path.name.startswith('.'):
                continue
            
            # Check if directory name follows conventions
            parent_name = dir_path.parent.name
            if parent_name in DIRECTORY_PATTERNS:
                pattern = DIRECTORY_PATTERNS[parent_name]
                if not pattern.match(dir_path.name):
                    violations.append((dir_path, f"Directory should match pattern: {pattern.pattern}"))
    
    return violations

def check_file_naming(base_dir: Path) -> Dict[str, List[Tuple[Path, str]]]:
    """Check file naming conventions across all categories."""
    all_violations = {}
    
    for category, pattern_info in NAMING_PATTERNS.items():
        print(f"\n📁 Checking {category.replace('_', ' ').title()}")
        print("-" * 40)
        
        # Determine file extensions to check
        extensions = None
        if 'cad_exports' in category:
            extensions = ['step', 'iges', 'x_t', 'stl', 'parasolid']
        elif 'json' in category or 'manifest' in category:
            extensions = ['json']
        elif 'yaml' in category:
            extensions = ['yaml', 'yml']
        
        # Find relevant files
        files = find_files_in_directories(base_dir, pattern_info['directories'], extensions)
        
        if not files:
            print(f"  ℹ️  No files found in: {pattern_info['directories']}")
            continue
        
        # Check naming compliance
        violations = check_pattern_compliance(files, pattern_info)
        
        if violations:
            all_violations[category] = violations
            for file_path, description in violations:
                print(f"  ❌ {file_path.relative_to(base_dir)}")
                print(f"     {description}")
                print(f"     Examples: {', '.join(pattern_info['examples'])}")
        else:
            print(f"  ✅ All {len(files)} files comply with naming convention")
            for file_path in files:
                print(f"     ✓ {file_path.name}")
    
    return all_violations

def validate_special_cases(base_dir: Path) -> List[Tuple[Path, str]]:
    """Check special naming cases and business rules."""
    violations = []
    
    # Check that PLUS prefix is consistent
    for json_file in base_dir.rglob("*.json"):
        if json_file.parent.name in ['metadata', 'problems', 'manifests']:
            if not json_file.name.startswith('PLUS-'):
                violations.append((json_file, "JSON files in metadata/problems/manifests should start with 'PLUS-'"))
    
    # Check revision format in exports
    for export_file in base_dir.rglob("*"):
        if export_file.suffix.lower() in ['.step', '.iges', '.x_t', '.stl']:
            # Extract revision from filename
            rev_match = re.search(r'-([A-Z][0-9]{2})\.[a-z]+$', export_file.name, re.IGNORECASE)
            if rev_match:
                rev = rev_match.group(1)
                if not re.match(r'^[A-Z][0-9]{2}$', rev):
                    violations.append((export_file, f"Revision '{rev}' should follow format: [A-Z][0-9][0-9] (e.g., A02, B15)"))
    
    return violations

def main():
    if len(sys.argv) != 2:
        print("Usage: python naming_guard.py <base_dir>")
        print("\nExample:")
        print("  python naming_guard.py CAD/")
        sys.exit(1)
    
    base_dir = Path(sys.argv[1]).resolve()
    
    if not base_dir.exists():
        print(f"ERROR: Directory {base_dir} does not exist")
        sys.exit(1)
    
    print("📛 Naming Convention Validation")
    print("=" * 50)
    print(f"Base directory: {base_dir}")
    
    # Check file naming
    file_violations = check_file_naming(base_dir)
    
    # Check directory naming
    print(f"\n📂 Checking Directory Naming")
    print("-" * 40)
    dir_violations = check_directory_naming(base_dir)
    
    if dir_violations:
        for dir_path, description in dir_violations:
            print(f"  ❌ {dir_path.relative_to(base_dir)}")
            print(f"     {description}")
    else:
        print("  ✅ All directories follow naming conventions")
    
    # Check special cases
    print(f"\n🔍 Checking Special Cases")
    print("-" * 40)
    special_violations = validate_special_cases(base_dir)
    
    if special_violations:
        for file_path, description in special_violations:
            print(f"  ❌ {file_path.relative_to(base_dir)}")
            print(f"     {description}")
    else:
        print("  ✅ All special naming rules satisfied")
    
    # Summary
    total_violations = len(dir_violations) + len(special_violations)
    for violations in file_violations.values():
        total_violations += len(violations)
    
    print(f"\n📊 Summary")
    print("=" * 50)
    if total_violations == 0:
        print("  ✅ All files and directories follow naming conventions")
        sys.exit(0)
    else:
        print(f"  ❌ {total_violations} naming violations found")
        print("\n💡 Naming Convention Summary:")
        for category, pattern_info in NAMING_PATTERNS.items():
            print(f"  • {category.replace('_', ' ').title()}: {pattern_info['description']}")
        sys.exit(1)

if __name__ == "__main__":
    main()