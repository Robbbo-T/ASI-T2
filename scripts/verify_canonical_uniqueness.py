#!/usr/bin/env python3
"""
Canonical Uniqueness Verifier

Verifies that each ATA chapter has exactly one canonical location.

Usage:
    python scripts/verify_canonical_uniqueness.py
    python scripts/verify_canonical_uniqueness.py --verbose
"""

import argparse
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


class CanonicalUniquenessVerifier:
    """Verifies canonical ATA uniqueness."""
    
    def __init__(self, repo_root: Path, verbose: bool = False):
        self.repo_root = repo_root
        self.verbose = verbose
        self.canonical_base = repo_root / "2-DOMAINS-LEVELS"
        self.resources_dir = repo_root / "8-RESOURCES" / "ATA_CANONICAL"
        
        # Load registry
        self.registry = self._load_registry()
    
    def _log(self, message: str, level: str = "INFO"):
        """Log a message."""
        prefix = {
            "INFO": "ℹ️ ",
            "SUCCESS": "✅",
            "WARNING": "⚠️ ",
            "ERROR": "❌",
            "DEBUG": "🔍",
        }.get(level, "  ")
        
        if level == "DEBUG" and not self.verbose:
            return
            
        print(f"{prefix} {message}")
    
    def _load_registry(self) -> Dict:
        """Load ATA registry."""
        registry_path = self.resources_dir / "ATA_REGISTRY.yaml"
        if not registry_path.exists():
            self._log(f"Registry not found: {registry_path}", "WARNING")
            return {"ata_chapters": [], "domains": []}
        
        with open(registry_path, 'r') as f:
            return yaml.safe_load(f)
    
    def find_all_canonical_atas(self) -> Dict[str, List[Tuple[str, Path]]]:
        """Find all canonical ATA directories and group by ATA number."""
        ata_locations = defaultdict(list)
        
        if not self.canonical_base.exists():
            return ata_locations
        
        # Scan for ATA directories
        for domain_dir in self.canonical_base.iterdir():
            if not domain_dir.is_dir():
                continue
            
            ata_base = domain_dir / "ata"
            if not ata_base.exists():
                continue
            
            for ata_dir in ata_base.iterdir():
                if ata_dir.is_dir() and ata_dir.name.startswith("ATA-"):
                    ata_locations[ata_dir.name].append((domain_dir.name, ata_dir))
        
        return ata_locations
    
    def verify_registry_consistency(self) -> Tuple[bool, List[str]]:
        """Verify registry is internally consistent."""
        errors = []
        
        # Check for duplicate canonical domains
        ata_domains = {}
        for chapter in self.registry.get("ata_chapters", []):
            ata = chapter["ata"]
            domain = chapter["canonical_domain"]
            
            if ata in ata_domains:
                errors.append(
                    f"ATA {ata} has multiple canonical domains in registry: "
                    f"{ata_domains[ata]} and {domain}"
                )
            else:
                ata_domains[ata] = domain
        
        # Check that canonical domains exist in domains list
        valid_domains = set(d["code"] for d in self.registry.get("domains", []))
        for chapter in self.registry.get("ata_chapters", []):
            ata = chapter["ata"]
            domain = chapter["canonical_domain"]
            
            if domain not in valid_domains:
                errors.append(
                    f"ATA {ata} canonical domain '{domain}' not found in domains list"
                )
            
            # Check shared domains
            for shared_domain in chapter.get("shared_domains", []):
                if shared_domain not in valid_domains:
                    errors.append(
                        f"ATA {ata} shared domain '{shared_domain}' not found in domains list"
                    )
        
        return len(errors) == 0, errors
    
    def verify_filesystem_uniqueness(self) -> Tuple[bool, List[str]]:
        """Verify each ATA has at most one canonical location."""
        errors = []
        warnings = []
        
        ata_locations = self.find_all_canonical_atas()
        
        # Check for duplicates
        for ata, locations in ata_locations.items():
            if len(locations) > 1:
                error_msg = f"ATA {ata} has multiple canonical locations:"
                for domain, path in locations:
                    error_msg += f"\n  - {domain}: {path.relative_to(self.repo_root)}"
                errors.append(error_msg)
        
        # Check against registry
        for chapter in self.registry.get("ata_chapters", []):
            ata = chapter["ata"]
            expected_domain = chapter["canonical_domain"]
            
            if ata not in ata_locations:
                warnings.append(
                    f"ATA {ata} defined in registry (domain: {expected_domain}) "
                    f"but no canonical directory found"
                )
                continue
            
            # Check if it's in the right domain
            actual_locations = ata_locations[ata]
            found_in_expected = False
            
            for domain, path in actual_locations:
                if domain == expected_domain:
                    found_in_expected = True
                    break
            
            if not found_in_expected:
                actual_domains = [d for d, _ in actual_locations]
                errors.append(
                    f"ATA {ata} registry says canonical domain is '{expected_domain}' "
                    f"but found in: {', '.join(actual_domains)}"
                )
        
        # Report warnings if verbose
        if warnings and self.verbose:
            for warning in warnings:
                self._log(warning, "WARNING")
        
        return len(errors) == 0, errors
    
    def verify(self) -> Tuple[bool, Dict]:
        """Run all verification checks."""
        results = {
            "registry_consistent": False,
            "filesystem_unique": False,
            "errors": [],
            "summary": {}
        }
        
        # Check registry consistency
        self._log("Checking registry consistency...")
        registry_ok, registry_errors = self.verify_registry_consistency()
        results["registry_consistent"] = registry_ok
        
        if registry_ok:
            self._log("Registry is consistent", "SUCCESS")
        else:
            self._log(f"Registry has {len(registry_errors)} error(s)", "ERROR")
            results["errors"].extend(registry_errors)
        
        # Check filesystem uniqueness
        self._log("\nChecking filesystem uniqueness...")
        fs_ok, fs_errors = self.verify_filesystem_uniqueness()
        results["filesystem_unique"] = fs_ok
        
        if fs_ok:
            self._log("All ATAs have unique canonical locations", "SUCCESS")
        else:
            self._log(f"Found {len(fs_errors)} uniqueness violation(s)", "ERROR")
            results["errors"].extend(fs_errors)
        
        # Generate summary
        ata_locations = self.find_all_canonical_atas()
        results["summary"] = {
            "total_canonical_atas": len(ata_locations),
            "atas_with_duplicates": sum(1 for locs in ata_locations.values() if len(locs) > 1),
            "total_registry_atas": len(self.registry.get("ata_chapters", [])),
        }
        
        return registry_ok and fs_ok, results


def main():
    parser = argparse.ArgumentParser(
        description="Verify canonical ATA uniqueness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This script verifies that:
1. The ATA registry is internally consistent
2. Each ATA chapter has at most one canonical location in 2-DOMAINS-LEVELS/
3. Canonical locations match the registry definitions

Examples:
  # Run verification
  python scripts/verify_canonical_uniqueness.py

  # Verbose output
  python scripts/verify_canonical_uniqueness.py --verbose
        """
    )
    
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    # Get repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    verifier = CanonicalUniquenessVerifier(repo_root, verbose=args.verbose)
    
    print("=" * 80)
    print("Canonical ATA Uniqueness Verification")
    print("=" * 80)
    print()
    
    all_ok, results = verifier.verify()
    
    # Print errors
    if results["errors"]:
        print("\n" + "=" * 80)
        print("ERRORS")
        print("=" * 80)
        print()
        for error in results["errors"]:
            verifier._log(error, "ERROR")
    
    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print(f"Registry Consistent:       {'✅ Yes' if results['registry_consistent'] else '❌ No'}")
    print(f"Filesystem Unique:         {'✅ Yes' if results['filesystem_unique'] else '❌ No'}")
    print(f"Total Canonical ATAs:      {results['summary']['total_canonical_atas']}")
    print(f"ATAs with Duplicates:      {results['summary']['atas_with_duplicates']}")
    print(f"ATAs in Registry:          {results['summary']['total_registry_atas']}")
    print()
    
    if all_ok:
        verifier._log("All verification checks passed", "SUCCESS")
        return 0
    else:
        verifier._log("Verification failed", "ERROR")
        return 1


if __name__ == "__main__":
    sys.exit(main())
