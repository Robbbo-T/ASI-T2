#!/usr/bin/env python3
"""
Legacy ATA Short-Code Migrator

Normalizes legacy 571/571010 ATA codes to the standardized 5710 format
in CAx filenames (CAD/CAE/CAM/CAV/CMP).

Usage:
    python3 scripts/migrate_ata_shortcode.py [root_path]
    python3 scripts/migrate_ata_shortcode.py .  # default

This script will:
- Find all CAx files with legacy ATA codes (571, 571010)
- Rename them to use the standardized 5710 code
- Report the changes made
"""

import re
import sys
import pathlib
from typing import Tuple, Optional

# Match any CAx filename with potentially old ATA codes
CAx_ANY = re.compile(
    r'^(ASSY|PRT|DRW|FEM|CFD|MBD|EMI|NC|APT|OPR|FIX|TOOL|SET|QIP|QIF|DMIS|MEAS|MSA|CERT|EPR|RECY|TREAT|DISP|MATREC)-'
    r'([A-Z0-9]{3,4})-'
    r'(CAD|CAE|CAM|CAV|CMP)'
    r'(57\d{1,4})-'  # Match 571, 5710, 571010, or any 57xx
    r'(.*)$'  # Rest of the filename
)


def normalize_ata_code(code: str) -> str:
    """
    Normalize ATA code to 5710 standard.
    
    Examples:
        571 -> 5710
        5710 -> 5710
        571010 -> 5710
        5720 -> 5720 (other 57xx unchanged)
    """
    if code == '571':
        return '5710'
    if code == '5710':
        return '5710'
    if code == '571010':
        return '5710'
    # Other 57xx codes: keep as-is if already 4 digits, otherwise truncate to 4
    return code if len(code) == 4 else code[:4]


def should_skip_path(path: pathlib.Path) -> bool:
    """Check if path should be skipped (hidden, build artifacts, etc.)."""
    # Skip hidden files/directories
    if any(part.startswith('.') for part in path.parts):
        return True
    
    # Skip common build/dependency directories
    skip_dirs = {'node_modules', '__pycache__', '.venv', 'venv', 'build', 'dist'}
    if any(skip_dir in path.parts for skip_dir in skip_dirs):
        return True
    
    return False


def migrate_file(path: pathlib.Path, dry_run: bool = False) -> Tuple[bool, Optional[str]]:
    """
    Migrate a single file if needed.
    
    Returns:
        (changed, new_name) - whether file was changed and what the new name would be
    """
    m = CAx_ANY.match(path.name)
    if not m:
        return False, None
    
    disc, mic, domain, ata, rest = m.groups()
    new_ata = normalize_ata_code(ata)
    
    if new_ata != ata:
        new_name = f"{disc}-{mic}-{domain}{new_ata}-{rest}"
        if not dry_run:
            new_path = path.with_name(new_name)
            if new_path.exists():
                print(f"⚠️  WARNING: Target already exists, skipping: {path.name} -> {new_name}")
                return False, None
            path.rename(new_path)
        return True, new_name
    
    return False, None


def main(root: str = '.', dry_run: bool = False) -> int:
    """Main migration function."""
    root_path = pathlib.Path(root).resolve()
    
    if not root_path.exists():
        print(f"❌ ERROR: Path does not exist: {root}")
        return 1
    
    print(f"{'🔍 DRY RUN: ' if dry_run else '🔧 '}Scanning for legacy ATA codes in: {root_path}")
    print("=" * 70)
    
    changed = 0
    scanned = 0
    
    for p in root_path.rglob('*'):
        if not p.is_file() or should_skip_path(p):
            continue
        
        # Only check files that might be CAx files
        if not any(p.name.startswith(prefix) for prefix in [
            'ASSY-', 'PRT-', 'DRW-', 'FEM-', 'CFD-', 'MBD-', 'EMI-',
            'NC-', 'APT-', 'OPR-', 'FIX-', 'TOOL-', 'SET-',
            'QIP-', 'QIF-', 'DMIS-', 'MEAS-', 'MSA-', 'CERT-',
            'EPR-', 'RECY-', 'TREAT-', 'DISP-', 'MATREC-'
        ]):
            continue
        
        scanned += 1
        was_changed, new_name = migrate_file(p, dry_run)
        
        if was_changed:
            action = "would rename" if dry_run else "renamed"
            print(f"✓ {action}: {p.name} -> {new_name}")
            changed += 1
    
    print("=" * 70)
    print(f"📊 Summary:")
    print(f"   Files scanned: {scanned}")
    print(f"   Files {'that would be ' if dry_run else ''}changed: {changed}")
    
    if dry_run and changed > 0:
        print(f"\n💡 Run without --dry-run to apply changes")
    
    return 0


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Migrate legacy ATA short-codes (571/571010) to standardized 5710'
    )
    parser.add_argument(
        'root',
        nargs='?',
        default='.',
        help='Root directory to scan (default: current directory)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without actually renaming files'
    )
    
    args = parser.parse_args()
    sys.exit(main(args.root, args.dry_run))
