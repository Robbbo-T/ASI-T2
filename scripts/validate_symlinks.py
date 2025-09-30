#!/usr/bin/env python3
"""
Symlink Validator

Validates relative symlinks in product trees that point to canonical ATA directories.

Usage:
    python scripts/validate_symlinks.py
    python scripts/validate_symlinks.py --fix
    python scripts/validate_symlinks.py --product BWB-Q100
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class SymlinkValidator:
    """Validates ATA symlinks in product trees."""
    
    def __init__(self, repo_root: Path, verbose: bool = False, fix: bool = False):
        self.repo_root = repo_root
        self.verbose = verbose
        self.fix = fix
        self.products_base = repo_root / "PRODUCTS"
        self.canonical_base = repo_root / "2-DOMAINS-LEVELS"
    
    def _log(self, message: str, level: str = "INFO"):
        """Log a message."""
        prefix = {
            "INFO": "ℹ️ ",
            "SUCCESS": "✅",
            "WARNING": "⚠️ ",
            "ERROR": "❌",
            "DEBUG": "🔍",
            "FIX": "🔧",
        }.get(level, "  ")
        
        if level == "DEBUG" and not self.verbose:
            return
            
        print(f"{prefix} {message}")
    
    def find_ata_symlinks(self, product: Optional[str] = None) -> List[Path]:
        """Find all ATA symlinks in product trees."""
        symlinks = []
        
        if not self.products_base.exists():
            return symlinks
        
        # Build search pattern
        if product:
            search_base = self.products_base / "**" / product
        else:
            search_base = self.products_base
        
        # Find all ata directories
        pattern = "**/domains/*/ata/*"
        for path in search_base.glob(pattern):
            if path.is_symlink():
                symlinks.append(path)
        
        return sorted(symlinks)
    
    def validate_symlink(self, symlink_path: Path) -> Tuple[bool, str, Optional[Path]]:
        """
        Validate a single symlink.
        
        Returns: (is_valid, error_message, expected_target)
        """
        if not symlink_path.is_symlink():
            return False, "Not a symlink", None
        
        # Get symlink target
        try:
            target = symlink_path.readlink()
        except Exception as e:
            return False, f"Cannot read symlink: {e}", None
        
        # Check if target exists
        resolved = symlink_path.resolve()
        if not resolved.exists():
            return False, f"Broken symlink: target does not exist: {target}", None
        
        # Check if target is in canonical location
        try:
            rel_to_canonical = resolved.relative_to(self.canonical_base)
        except ValueError:
            return False, f"Target is not in canonical location: {resolved}", None
        
        # Parse symlink path to get expected target
        # symlink_path: PRODUCTS/.../domains/DOMAIN/ata/ATA
        # expected: 2-DOMAINS-LEVELS/DOMAIN/ata/ATA
        
        parts = symlink_path.parts
        try:
            ata_idx = parts.index("ata")
            domain_idx = parts.index("domains")
            
            domain = parts[domain_idx + 1]
            ata = parts[ata_idx + 1]
            
            expected_canonical = self.canonical_base / domain / "ata" / ata
            
            # Check if resolved path matches expected
            if resolved != expected_canonical:
                return False, f"Points to wrong location: {resolved} (expected: {expected_canonical})", expected_canonical
            
            # Validate that symlink is relative
            if target.is_absolute():
                return False, f"Symlink should be relative, not absolute: {target}", expected_canonical
            
            # Verify relative path correctness
            # Calculate expected relative path
            rel_to_root = os.path.relpath(self.repo_root, symlink_path.parent)
            rel_canonical = expected_canonical.relative_to(self.repo_root)
            expected_rel_target = Path(rel_to_root) / rel_canonical
            
            if target != expected_rel_target:
                # Normalize and compare
                target_normalized = os.path.normpath(target)
                expected_normalized = os.path.normpath(expected_rel_target)
                
                if target_normalized != expected_normalized:
                    return False, f"Relative path incorrect: {target} (expected: {expected_rel_target})", expected_canonical
            
            return True, "", expected_canonical
            
        except (ValueError, IndexError) as e:
            return False, f"Cannot parse symlink path: {e}", None
    
    def fix_symlink(self, symlink_path: Path, expected_target: Path) -> bool:
        """Fix a broken or incorrect symlink."""
        try:
            # Calculate correct relative path
            rel_to_root = os.path.relpath(self.repo_root, symlink_path.parent)
            rel_canonical = expected_target.relative_to(self.repo_root)
            correct_rel_target = Path(rel_to_root) / rel_canonical
            
            # Remove old symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                symlink_path.unlink()
            
            # Create new symlink
            symlink_path.symlink_to(correct_rel_target)
            
            self._log(f"Fixed: {symlink_path.relative_to(self.repo_root)}", "FIX")
            return True
            
        except Exception as e:
            self._log(f"Failed to fix {symlink_path}: {e}", "ERROR")
            return False
    
    def validate_all(self, product: Optional[str] = None) -> Tuple[int, int, int]:
        """
        Validate all symlinks.
        
        Returns: (valid_count, invalid_count, fixed_count)
        """
        symlinks = self.find_ata_symlinks(product)
        
        if not symlinks:
            self._log("No ATA symlinks found in product trees")
            return 0, 0, 0
        
        self._log(f"Found {len(symlinks)} ATA symlinks to validate\n")
        
        valid_count = 0
        invalid_count = 0
        fixed_count = 0
        
        for symlink in symlinks:
            rel_path = symlink.relative_to(self.repo_root)
            
            is_valid, error_msg, expected_target = self.validate_symlink(symlink)
            
            if is_valid:
                self._log(f"✅ {rel_path}", "DEBUG")
                valid_count += 1
            else:
                self._log(f"❌ {rel_path}", "ERROR")
                self._log(f"   {error_msg}", "ERROR")
                invalid_count += 1
                
                # Attempt fix if requested and we have an expected target
                if self.fix and expected_target:
                    if self.fix_symlink(symlink, expected_target):
                        fixed_count += 1
                        invalid_count -= 1
                        valid_count += 1
        
        return valid_count, invalid_count, fixed_count


def main():
    parser = argparse.ArgumentParser(
        description="Validate ATA symlinks in product trees",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This script validates that:
1. Symlinks exist and are not broken
2. Symlinks point to correct canonical locations
3. Symlinks use relative paths (not absolute)
4. Relative paths are correctly calculated

Examples:
  # Validate all symlinks
  python scripts/validate_symlinks.py

  # Validate and fix broken symlinks
  python scripts/validate_symlinks.py --fix

  # Validate symlinks for specific product
  python scripts/validate_symlinks.py --product BWB-Q100

  # Verbose output
  python scripts/validate_symlinks.py --verbose
        """
    )
    
    parser.add_argument(
        "--product",
        help="Limit validation to specific product (e.g., BWB-Q100)"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to fix broken or incorrect symlinks"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output (show all symlinks, not just errors)"
    )
    
    args = parser.parse_args()
    
    # Get repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    validator = SymlinkValidator(repo_root, verbose=args.verbose, fix=args.fix)
    
    print("=" * 80)
    print("ATA Symlink Validation")
    if args.product:
        print(f"Product: {args.product}")
    if args.fix:
        print("Mode: Fix broken symlinks")
    print("=" * 80)
    print()
    
    valid, invalid, fixed = validator.validate_all(args.product)
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print(f"✅ Valid symlinks:    {valid}")
    print(f"❌ Invalid symlinks:  {invalid}")
    
    if args.fix and fixed > 0:
        print(f"🔧 Fixed symlinks:    {fixed}")
    
    print()
    
    if invalid == 0:
        validator._log("All symlinks are valid", "SUCCESS")
        return 0
    else:
        validator._log(f"{invalid} invalid symlink(s) found", "ERROR")
        if not args.fix:
            validator._log("Run with --fix to attempt repairs", "INFO")
        return 1


if __name__ == "__main__":
    sys.exit(main())
