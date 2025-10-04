#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
find_domain_dirs.py

Python utility to find directories under PRODUCTS/.../domains/<DOMAIN>/{ata,cax,qox,pax}/
that match specific patterns for ATA chapters, CAx tools, QOx problems, and PAx packages.

This script provides the same functionality as find_domain_dirs.sh but with better
cross-platform compatibility and integration with other Python scripts.

Usage:
    python3 scripts/find_domain_dirs.py [OPTIONS]

Options:
    -r, --root DIR      Root directory to search (default: PRODUCTS)
    -t, --type TYPE     Filter by type: ata, cax, qox, pax, or all (default: all)
    -h, --help          Show this help message
    -v, --verbose       Enable verbose output

Examples:
    # Find all subdirectories under ata/cax/qox/pax
    python3 scripts/find_domain_dirs.py

    # Find only ATA directories
    python3 scripts/find_domain_dirs.py --type ata

    # Search in a different root
    python3 scripts/find_domain_dirs.py --root /path/to/products
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Set


def find_domain_directories(root: Path, dir_type: str = "all", verbose: bool = False) -> List[Path]:
    """
    Find directories matching the pattern: .../domains/<DOMAIN>/(ata|cax|qox|pax)/...
    
    Args:
        root: Root directory to search
        dir_type: Type of directory to find (all, ata, cax, qox, pax)
        verbose: Enable verbose output
        
    Returns:
        List of matching directory paths
    """
    if not root.exists():
        print(f"Error: Root directory '{root}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    # Build regex pattern based on type
    if dir_type == "all":
        pattern = re.compile(r".*/domains/[^/]+/(ata|cax|qox|pax)/.*")
    else:
        pattern = re.compile(rf".*/domains/[^/]+/{dir_type}/.*")
    
    matching_dirs: Set[Path] = set()
    
    if verbose:
        print(f"Searching for {dir_type} directories under {root}/...", file=sys.stderr)
    
    # Walk the directory tree
    for dirpath, dirnames, _ in os.walk(root):
        # Convert to Path for cleaner handling
        dir_path = Path(dirpath)
        
        # Check if current path matches the pattern
        if pattern.match(str(dir_path)):
            matching_dirs.add(dir_path)
    
    # Return sorted list
    return sorted(matching_dirs)


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Find directories under PRODUCTS/.../domains/<DOMAIN>/{ata,cax,qox,pax}/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Find all subdirectories under ata/cax/qox/pax
  %(prog)s

  # Find only ATA directories
  %(prog)s --type ata

  # Search in a different root
  %(prog)s --root /path/to/products

  # Enable verbose output
  %(prog)s --verbose
        """
    )
    
    parser.add_argument(
        "-r", "--root",
        type=Path,
        default=Path("PRODUCTS"),
        help="Root directory to search (default: PRODUCTS)"
    )
    
    parser.add_argument(
        "-t", "--type",
        choices=["all", "ata", "cax", "qox", "pax"],
        default="all",
        help="Filter by type: ata, cax, qox, pax, or all (default: all)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Find matching directories
    try:
        directories = find_domain_directories(args.root, args.type, args.verbose)
        
        # Print results
        for dir_path in directories:
            print(dir_path)
        
        if args.verbose:
            print(f"\nFound {len(directories)} matching directories", file=sys.stderr)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
