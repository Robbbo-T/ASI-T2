#!/usr/bin/env python3
"""
Link Checker for CAD Domain

Validates relative paths in JSON manifests and README files:
- CAD manifest references to ATA documents and schemas
- Export file paths in manifests
- Schema references in JSON files
- Cross-references in README files

Usage:
  python link_check.py <base_dir>
  python link_check.py CAD/
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import List, Set, Tuple, Dict, Any

def find_json_files(base_dir: Path) -> List[Path]:
    """Find all JSON files in directory tree."""
    return list(base_dir.rglob("*.json"))

def find_markdown_files(base_dir: Path) -> List[Path]:
    """Find all Markdown files in directory tree."""
    return list(base_dir.rglob("*.md"))

def extract_paths_from_json(json_file: Path) -> List[Tuple[str, str]]:
    """Extract relative paths from JSON file with context."""
    paths = []
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract paths recursively
        def extract_recursive(obj: Any, path_context: str = ""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_context = f"{path_context}.{key}" if path_context else key
                    
                    if key in ["path", "export", "ref", "ata_practices", "ata_structures", "s1000d_dms"]:
                        if isinstance(value, str):
                            paths.append((value, new_context))
                        elif isinstance(value, list):
                            for item in value:
                                if isinstance(item, str):
                                    paths.append((item, new_context))
                    
                    extract_recursive(value, new_context)
                    
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    extract_recursive(item, f"{path_context}[{i}]")
        
        extract_recursive(data)
        
    except Exception as e:
        print(f"WARNING: Could not parse {json_file}: {e}")
    
    return paths

def extract_paths_from_markdown(md_file: Path) -> List[Tuple[str, str]]:
    """Extract relative paths from Markdown file."""
    paths = []
    
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find relative path patterns
        patterns = [
            (r'`([^`]*\.(?:json|xml|yaml|yml|step|iges|x_t))`', 'code block'),
            (r'\[([^\]]*)\]\(([^)]*)\)', 'markdown link'),
            (r'href="([^"]*)"', 'HTML link'),
            (r'src="([^"]*)"', 'HTML src'),
            (r'→\s*([^\s\n]*\.(?:json|xml|yaml|yml))', 'arrow reference')
        ]
        
        for pattern, context in patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                # Handle different capture group patterns
                if context == 'markdown link':
                    path = match.group(2)  # Second group for markdown links
                else:
                    path = match.group(1)  # First group for all others
                if path and not path.startswith(('http://', 'https://', 'mailto:', '#')):
                    paths.append((path, f"{context} (line {content[:match.start()].count(chr(10)) + 1})"))
    
    except Exception as e:
        print(f"WARNING: Could not parse {md_file}: {e}")
    
    return paths

def check_path_exists(base_path: Path, relative_path: str) -> bool:
    """Check if relative path exists from base directory."""
    try:
        # Handle different path separators and clean path
        clean_path = relative_path.replace('\\', '/').strip()
        
        # Remove schema references
        if clean_path.startswith('#'):
            return True  # Fragment identifiers are not file paths
        
        # Remove URL parameters
        if '?' in clean_path:
            clean_path = clean_path.split('?')[0]
        
        if '#' in clean_path:
            clean_path = clean_path.split('#')[0]
        
        # Skip empty paths
        if not clean_path:
            return True
        
        # Resolve path relative to base
        full_path = (base_path / clean_path).resolve()
        return full_path.exists()
        
    except Exception:
        return False

def validate_links_in_file(file_path: Path, base_dir: Path) -> List[Tuple[str, str]]:
    """Validate all links in a single file."""
    broken_links = []
    
    if file_path.suffix == '.json':
        paths = extract_paths_from_json(file_path)
    elif file_path.suffix == '.md':
        paths = extract_paths_from_markdown(file_path)
    else:
        return broken_links
    
    for path, context in paths:
        if not check_path_exists(file_path.parent, path):
            broken_links.append((path, context))
    
    return broken_links

def check_schema_references(base_dir: Path) -> List[Tuple[Path, str, str]]:
    """Check $schema references in JSON files."""
    schema_errors = []
    
    for json_file in find_json_files(base_dir):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if '$schema' in data:
                schema_ref = data['$schema']
                if not schema_ref.startswith('http'):
                    # Local schema reference
                    if not check_path_exists(json_file.parent, schema_ref):
                        schema_errors.append((json_file, schema_ref, "$schema reference"))
        
        except Exception as e:
            print(f"WARNING: Could not check schema in {json_file}: {e}")
    
    return schema_errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python link_check.py <base_dir>")
        print("\nExample:")
        print("  python link_check.py CAD/")
        sys.exit(1)
    
    base_dir = Path(sys.argv[1]).resolve()
    
    if not base_dir.exists():
        print(f"ERROR: Directory {base_dir} does not exist")
        sys.exit(1)
    
    print("🔗 Link Validation")
    print("=" * 50)
    print(f"Base directory: {base_dir}")
    
    total_files = 0
    files_with_errors = 0
    total_broken_links = 0
    
    # Check JSON files
    print("\n📄 Checking JSON files...")
    json_files = find_json_files(base_dir)
    for json_file in json_files:
        total_files += 1
        broken_links = validate_links_in_file(json_file, base_dir)
        
        if broken_links:
            files_with_errors += 1
            print(f"  ❌ {json_file.relative_to(base_dir)}")
            for path, context in broken_links:
                print(f"     Broken link: {path} (in {context})")
                total_broken_links += 1
        else:
            print(f"  ✅ {json_file.relative_to(base_dir)}")
    
    # Check schema references
    print("\n📋 Checking schema references...")
    schema_errors = check_schema_references(base_dir)
    for json_file, schema_ref, context in schema_errors:
        print(f"  ❌ {json_file.relative_to(base_dir)}")
        print(f"     Broken schema: {schema_ref} (in {context})")
        total_broken_links += 1
    
    # Check Markdown files
    print("\n📝 Checking Markdown files...")
    md_files = find_markdown_files(base_dir)
    for md_file in md_files:
        total_files += 1
        broken_links = validate_links_in_file(md_file, base_dir)
        
        if broken_links:
            files_with_errors += 1
            print(f"  ❌ {md_file.relative_to(base_dir)}")
            for path, context in broken_links:
                print(f"     Broken link: {path} (in {context})")
                total_broken_links += 1
        else:
            print(f"  ✅ {md_file.relative_to(base_dir)}")
    
    # Summary
    print(f"\n📊 Summary")
    print("=" * 50)
    if total_broken_links == 0:
        print(f"  ✅ All links valid in {total_files} files")
        sys.exit(0)
    else:
        print(f"  ❌ {total_broken_links} broken links in {files_with_errors}/{total_files} files")
        sys.exit(1)

if __name__ == "__main__":
    main()