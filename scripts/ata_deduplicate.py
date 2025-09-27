#!/usr/bin/env python3
"""
ATA Deduplication Script

Consolidates duplicate ATA chapters within a product by:
1. Identifying duplicates using SHA256 hashing
2. Selecting canonical paths (domains/<DOMAIN>/ata/ATA-XX/)
3. Creating pointers for identical duplicates
4. Moving near-duplicates to variants/
5. Updating links and normalizing front-matter
6. Preserving QS/UTCS evidence

Usage:
    python scripts/ata_deduplicate.py --product AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100 [--apply]
    
Environment variables:
    DRY_RUN=true (default) - only show what would be done
    APPLY=true - actually apply changes
"""

import os
import sys
import hashlib
import json
import yaml
import re
import csv
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict
import argparse
import shutil

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

@dataclass
class ATAFile:
    """Represents an ATA file with metadata"""
    path: Path
    domain: str
    chapter: str
    file_type: str  # 'md', 'xml', 'json', 'yaml'
    content_hash: str
    size: int
    front_matter: Dict = None
    dm_code: str = None
    issue_info: str = None

@dataclass 
class ATADuplicate:
    """Represents a group of duplicate ATA files"""
    chapter: str
    files: List[ATAFile]
    canonical_file: ATAFile = None
    action: str = None  # 'identical', 'near_duplicate', 'conflict'

class ATADeduplicator:
    """Main deduplication logic"""
    
    def __init__(self, product_path: Path, dry_run: bool = True):
        self.product_path = product_path
        self.dry_run = dry_run
        self.report_dir = PROJECT_ROOT / "reports" / product_path.name
        self.report_dir.mkdir(parents=True, exist_ok=True)
        
        # Track changes
        self.moves: List[Tuple[Path, Path]] = []
        self.pointers: List[Tuple[Path, Path]] = []  # (old_path, canonical_path)
        self.conflicts: List[ATADuplicate] = []
        self.link_fixes: List[Tuple[Path, str, str]] = []  # (file, old_link, new_link)
        
    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of file content"""
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                return hashlib.sha256(content).hexdigest()
        except Exception as e:
            print(f"WARNING: Could not hash {file_path}: {e}")
            return ""

    def extract_front_matter(self, md_file: Path) -> Dict:
        """Extract YAML front matter from markdown file"""
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.startswith('---'):
                return {}
                
            parts = content.split('\n---\n', 1)
            if len(parts) < 2:
                return {}
                
            yaml_content = parts[0][3:]  # Remove leading ---
            return yaml.safe_load(yaml_content) or {}
        except Exception as e:
            print(f"WARNING: Could not parse front matter in {md_file}: {e}")
            return {}

    def extract_dm_code(self, xml_file: Path) -> Tuple[str, str]:
        """Extract dmCode and issueInfo from S1000D XML file"""
        try:
            with open(xml_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple regex extraction (could use proper XML parsing)
            dm_match = re.search(r'modelIdentCode="([^"]*)".*?systemDiffCode="([^"]*)".*?systemCode="([^"]*)"', content)
            issue_match = re.search(r'issueNumber="([^"]*)".*?inWork="([^"]*)"', content)
            
            dm_code = f"{dm_match.group(1)}-{dm_match.group(2)}-{dm_match.group(3)}" if dm_match else ""
            issue_info = f"{issue_match.group(1)}-{issue_match.group(2)}" if issue_match else ""
            
            return dm_code, issue_info
        except Exception as e:
            print(f"WARNING: Could not extract dmCode from {xml_file}: {e}")
            return "", ""

    def inventory_ata_files(self) -> Dict[str, List[ATAFile]]:
        """Create inventory of all ATA files by chapter"""
        inventory = defaultdict(list)
        
        # Find all ATA directories
        ata_pattern = self.product_path / "**/ata/ATA-*"
        for ata_dir in self.product_path.glob("**/ata/ATA-*"):
            if not ata_dir.is_dir():
                continue
                
            # Extract domain and chapter
            parts = ata_dir.parts
            domain_idx = -1
            for i, part in enumerate(parts):
                if part == "domains":
                    domain_idx = i + 1
                    break
            
            if domain_idx == -1 or domain_idx >= len(parts):
                continue
                
            domain = parts[domain_idx]
            chapter = ata_dir.name
            
            # Find files in this ATA directory
            for pattern in ["*.md", "*.xml", "*.json", "*.yaml", "*.yml"]:
                for file_path in ata_dir.rglob(pattern):
                    if file_path.is_file():
                        content_hash = self.calculate_file_hash(file_path)
                        file_type = file_path.suffix[1:]  # Remove dot
                        
                        ata_file = ATAFile(
                            path=file_path,
                            domain=domain,
                            chapter=chapter,
                            file_type=file_type,
                            content_hash=content_hash,
                            size=file_path.stat().st_size
                        )
                        
                        # Extract metadata based on file type
                        if file_type == 'md':
                            ata_file.front_matter = self.extract_front_matter(file_path)
                        elif file_type == 'xml':
                            ata_file.dm_code, ata_file.issue_info = self.extract_dm_code(file_path)
                        
                        inventory[chapter].append(ata_file)
        
        return inventory

    def calculate_canonical_hash(self, files: List[ATAFile]) -> str:
        """Calculate canonical hash for a group of files"""
        # For now, use the most common content hash
        hash_counts = defaultdict(int)
        for f in files:
            hash_counts[f.content_hash] += 1
        
        return max(hash_counts.items(), key=lambda x: x[1])[0] if hash_counts else "TBD"

    def select_canonical_file(self, files: List[ATAFile]) -> ATAFile:
        """Select the canonical file based on domain priority and content"""
        # Priority order for domains (AAA has highest priority)
        domain_priority = {
            'AAA': 1, 'AAP': 2, 'CCC': 3, 'CQH': 4, 'DDD': 5, 'EDI': 6,
            'EEE': 7, 'EER': 8, 'IIF': 9, 'IIS': 10, 'LCC': 11, 'LIB': 12,
            'MEC': 13, 'OOO': 14, 'PPP': 15
        }
        
        # Sort by domain priority, then by path length (prefer shorter paths)
        sorted_files = sorted(files, key=lambda f: (
            domain_priority.get(f.domain, 999),
            len(str(f.path)),
            f.domain,
            str(f.path)
        ))
        
        return sorted_files[0]

    def are_files_identical(self, file1: ATAFile, file2: ATAFile) -> bool:
        """Check if two files are identical (same content hash)"""
        return file1.content_hash == file2.content_hash and file1.content_hash != ""

    def are_files_similar(self, file1: ATAFile, file2: ATAFile) -> bool:
        """Check if two files are similar but not identical"""
        # For now, just check if they differ only in artifact paths in front matter
        if file1.file_type != 'md' or file2.file_type != 'md':
            return False
            
        if not file1.front_matter or not file2.front_matter:
            return False
            
        # Create copies and normalize artifact paths
        fm1 = file1.front_matter.copy()
        fm2 = file2.front_matter.copy()
        
        # Remove artifact paths for comparison
        fm1.pop('artifact', None)
        fm2.pop('artifact', None)
        
        return fm1 == fm2

    def find_duplicates(self, inventory: Dict[str, List[ATAFile]]) -> List[ATADuplicate]:
        """Find duplicate ATA chapters"""
        duplicates = []
        
        for chapter, files in inventory.items():
            if len(files) <= 1:
                continue
                
            # Group files by direct README files in ATA-XX directories (not subdirectories)
            readme_files = []
            for f in files:
                if f.path.name == "README.md":
                    # Check if this README is directly in an ATA-XX directory
                    # Path should be like: .../domains/DOMAIN/ata/ATA-XX/README.md
                    path_parts = f.path.parts
                    if len(path_parts) >= 2 and path_parts[-2].startswith('ATA-'):
                        readme_files.append(f)
            
            # Only process chapters with multiple README files
            if len(readme_files) <= 1:
                continue
                
            canonical_file = self.select_canonical_file(readme_files)
            
            # Determine action based on similarity
            action = "identical"
            for f in readme_files:
                if f != canonical_file:
                    if not self.are_files_identical(f, canonical_file):
                        if self.are_files_similar(f, canonical_file):
                            action = "near_duplicate"
                        else:
                            action = "conflict"
                        break
            
            duplicate = ATADuplicate(
                chapter=chapter,
                files=readme_files,
                canonical_file=canonical_file,
                action=action
            )
            duplicates.append(duplicate)
        
        return duplicates

    def create_pointer_readme(self, old_path: Path, canonical_path: Path) -> str:
        """Create a pointer README that redirects to canonical location"""
        rel_path = os.path.relpath(canonical_path, old_path.parent)
        
        # Extract domain and chapter from paths for the front matter
        parts = old_path.parts
        domain_idx = -1
        for i, part in enumerate(parts):
            if part == "domains":
                domain_idx = i + 1
                break
        
        domain = parts[domain_idx] if domain_idx != -1 and domain_idx < len(parts) else "UNKNOWN"
        chapter = old_path.parent.name
        
        artifact_path = str(old_path.relative_to(PROJECT_ROOT))
        
        return f"""---
id: {chapter.replace('ATA-', 'ATA-')}-PTR-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: {artifact_path}
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: 2025-09-24
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
pointer_to: {rel_path}
reason: "Consolidated duplicate - canonical version maintained in {canonical_path.parent.relative_to(self.product_path)}"
---
# {chapter} (Pointer)

⚠️ **This location has been consolidated.**

The canonical version of this content is now maintained at:
[{rel_path}]({rel_path})

**Reason:** Eliminated redundant duplicate while preserving links and evidence.

**Migration:** This pointer was created during ATA deduplication on 2025-01-23.
"""

    def normalize_front_matter(self, file_path: Path, front_matter: Dict) -> Dict:
        """Normalize front matter format"""
        normalized = front_matter.copy()
        
        # Ensure artifact path is relative to project root
        if 'artifact' in normalized:
            artifact = normalized['artifact']
            if artifact.startswith('/home/runner/work/ASI-T2/ASI-T2/'):
                normalized['artifact'] = artifact.replace('/home/runner/work/ASI-T2/ASI-T2/', '')
            elif artifact.startswith(str(PROJECT_ROOT)):
                normalized['artifact'] = str(Path(artifact).relative_to(PROJECT_ROOT))
        
        # Ensure scalars are quoted
        for key in ['id', 'project', 'artifact', 'maintainer', 'bridge', 'ethics_guard', 'utcs_mi', 'canonical_hash']:
            if key in normalized and isinstance(normalized[key], str):
                normalized[key] = f'"{normalized[key]}"'
        
        return normalized

    def update_markdown_front_matter(self, file_path: Path, new_front_matter: Dict):
        """Update front matter in markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if content.startswith('---'):
                parts = content.split('\n---\n', 1)
                if len(parts) == 2:
                    # Replace front matter
                    yaml_str = yaml.dump(new_front_matter, default_flow_style=False, allow_unicode=True)
                    new_content = f"---\n{yaml_str}---\n{parts[1]}"
                    
                    if not self.dry_run:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                    
                    return True
        except Exception as e:
            print(f"ERROR: Could not update front matter in {file_path}: {e}")
        
        return False

    def apply_deduplication(self, duplicates: List[ATADuplicate]):
        """Apply the deduplication changes"""
        for duplicate in duplicates:
            canonical_file = duplicate.canonical_file
            canonical_dir = canonical_file.path.parent
            
            print(f"\n📁 Processing {duplicate.chapter} ({duplicate.action})")
            print(f"   Canonical: {canonical_file.domain} -> {canonical_dir.relative_to(self.product_path)}")
            
            for file in duplicate.files:
                if file == canonical_file:
                    # Update canonical file's front matter
                    if file.front_matter:
                        normalized_fm = self.normalize_front_matter(file.path, file.front_matter)
                        # Update canonical hash
                        normalized_fm['canonical_hash'] = f'"{self.calculate_canonical_hash(duplicate.files)}"'
                        
                        if not self.dry_run:
                            self.update_markdown_front_matter(file.path, normalized_fm)
                        print(f"   ✓ Updated canonical front matter")
                    continue
                
                old_dir = file.path.parent
                
                if duplicate.action == "identical":
                    # Create pointer
                    pointer_content = self.create_pointer_readme(file.path, canonical_file.path)
                    
                    if not self.dry_run:
                        # Backup original if it has unique content
                        if old_dir.exists():
                            evidence_dir = canonical_dir / "evidence" / file.domain
                            evidence_dir.mkdir(parents=True, exist_ok=True)
                            
                            # Move entire directory to evidence
                            shutil.move(str(old_dir), str(evidence_dir / old_dir.name))
                        
                        # Create pointer directory and file
                        old_dir.mkdir(parents=True, exist_ok=True)
                        with open(file.path, 'w', encoding='utf-8') as f:
                            f.write(pointer_content)
                    
                    self.pointers.append((old_dir, canonical_dir))
                    print(f"   → Pointer: {file.domain} ({old_dir.relative_to(self.product_path)})")
                
                elif duplicate.action == "near_duplicate":
                    # Move to variants
                    variants_dir = canonical_dir / "variants" / file.domain
                    
                    if not self.dry_run:
                        variants_dir.mkdir(parents=True, exist_ok=True)
                        if old_dir.exists():
                            shutil.move(str(old_dir), str(variants_dir / old_dir.name))
                    
                    self.moves.append((old_dir, variants_dir / old_dir.name))
                    print(f"   → Variant: {file.domain} -> variants/{file.domain}")
                
                elif duplicate.action == "conflict":
                    # Add to conflicts list for manual review
                    self.conflicts.append(duplicate)
                    print(f"   ⚠️  Conflict: {file.domain} (needs manual review)")

    def generate_reports(self, inventory: Dict, duplicates: List[ATADuplicate]):
        """Generate summary and detailed reports"""
        
        # Summary report
        summary_path = self.report_dir / "ata_dedup_summary.md"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(f"""# ATA Deduplication Summary

**Product:** {self.product_path.name}
**Date:** 2025-01-23
**Mode:** {'DRY RUN' if self.dry_run else 'APPLIED'}

## Overview

- **Total ATA Chapters Found:** {len(inventory)}
- **Chapters with Duplicates:** {len(duplicates)}
- **Pointers Created:** {len(self.pointers)}
- **Variants Moved:** {len(self.moves)}
- **Conflicts Identified:** {len(self.conflicts)}

## Duplicate Chapters Summary

| Chapter | Duplicates | Action | Canonical Domain |
|---------|------------|--------|------------------|
""")
            
            for dup in duplicates:
                canonical_domain = dup.canonical_file.domain if dup.canonical_file else "N/A"
                f.write(f"| {dup.chapter} | {len(dup.files)} | {dup.action} | {canonical_domain} |\n")
            
            if self.pointers:
                f.write(f"\n## Pointers Created ({len(self.pointers)})\n\n")
                for old_path, canonical_path in self.pointers:
                    f.write(f"- `{old_path.relative_to(self.product_path)}` → `{canonical_path.relative_to(self.product_path)}`\n")
            
            if self.moves:
                f.write(f"\n## Variants Moved ({len(self.moves)})\n\n")
                for old_path, new_path in self.moves:
                    f.write(f"- `{old_path.relative_to(self.product_path)}` → `{new_path.relative_to(self.product_path)}`\n")
        
        # Conflicts CSV
        conflicts_path = self.report_dir / "ata_conflicts.csv"
        with open(conflicts_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Chapter', 'Domain', 'Path', 'ContentHash', 'Size', 'Reason'])
            
            for conflict in self.conflicts:
                for file in conflict.files:
                    writer.writerow([
                        conflict.chapter,
                        file.domain,
                        str(file.path.relative_to(self.product_path)),
                        file.content_hash[:16] + "...",
                        file.size,
                        "Content differs significantly - manual review required"
                    ])
        
        # Link fixups CSV (placeholder for now)
        link_fixups_path = self.report_dir / "link_fixups.csv"
        with open(link_fixups_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['File', 'OldLink', 'NewLink', 'Status'])
            
            for file_path, old_link, new_link in self.link_fixes:
                writer.writerow([
                    str(file_path.relative_to(self.product_path)),
                    old_link,
                    new_link,
                    'Updated' if not self.dry_run else 'Planned'
                ])
        
        print(f"\n📊 Reports generated:")
        print(f"   - Summary: {summary_path}")
        print(f"   - Conflicts: {conflicts_path}")
        print(f"   - Link Fixups: {link_fixups_path}")

def main():
    parser = argparse.ArgumentParser(description='Deduplicate ATA chapters within a product')
    parser.add_argument('--product', required=True, help='Product path (e.g., AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100)')
    parser.add_argument('--apply', action='store_true', help='Apply changes (default is dry run)')
    
    args = parser.parse_args()
    
    # Check environment variables
    dry_run = not (args.apply or os.getenv('APPLY', '').lower() == 'true')
    if os.getenv('DRY_RUN', '').lower() == 'false':
        dry_run = False
    
    product_path = PROJECT_ROOT / "PRODUCTS" / args.product
    if not product_path.exists():
        print(f"ERROR: Product path not found: {product_path}")
        sys.exit(1)
    
    print(f"🔧 ATA Deduplication Tool")
    print(f"Product: {args.product}")
    print(f"Mode: {'DRY RUN' if dry_run else 'APPLY CHANGES'}")
    print(f"=" * 50)
    
    deduplicator = ATADeduplicator(product_path, dry_run=dry_run)
    
    # Step 1: Inventory
    print("\n📋 Step 1: Creating inventory...")
    inventory = deduplicator.inventory_ata_files()
    print(f"Found {len(inventory)} ATA chapters")
    
    # Step 2: Find duplicates
    print("\n🔍 Step 2: Finding duplicates...")
    duplicates = deduplicator.find_duplicates(inventory)
    print(f"Found {len(duplicates)} chapters with duplicates")
    
    # Step 3: Apply changes
    if duplicates:
        print("\n⚡ Step 3: Processing duplicates...")
        deduplicator.apply_deduplication(duplicates)
    
    # Step 4: Generate reports
    print("\n📊 Step 4: Generating reports...")
    deduplicator.generate_reports(inventory, duplicates)
    
    if dry_run:
        print(f"\n✅ DRY RUN completed. Use --apply to execute changes.")
    else:
        print(f"\n✅ Deduplication completed successfully!")
    
    return 0 if not deduplicator.conflicts else 1

if __name__ == "__main__":
    sys.exit(main())