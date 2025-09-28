#!/usr/bin/env python3
"""
ATA Chapter Folder Normalization Script

Normalizes numeric ATA chapter folders to canonical ATA-XX format.
- Scope: PRODUCTS/**/domains/*/ata/<numeric_name> where numeric_name matches ^\\d{1,3}$
- Target format: ATA-XX (uppercase ATA, hyphen, zero-padded two digits)
- Uses git mv for all renames
- Updates relative links in MD/JSON/YAML/XML files
- Generates detailed reports

Usage:
    python scripts/normalize_ata_chapters.py         # dry run (default)
    DRY_RUN=false python scripts/normalize_ata_chapters.py
    APPLY=true python scripts/normalize_ata_chapters.py
"""

import os
import re
import json
import csv
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set
import xml.etree.ElementTree as ET


class ATANormalizer:
    def __init__(self, base_dir: Path, dry_run: bool = True):
        self.base_dir = base_dir
        self.dry_run = dry_run
        self.reports_dir = base_dir / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        
        # Results tracking
        self.rename_map: Dict[str, str] = {}
        self.conflicts: List[Dict[str, str]] = []
        self.renamed_count = 0
        self.skipped_count = 0
        
    def find_numeric_ata_dirs(self) -> List[Path]:
        """Find all numeric ATA directories that need normalization."""
        numeric_dirs = []
        
        # Pattern: PRODUCTS/**/domains/*/ata/<numeric>
        for ata_parent in self.base_dir.glob("PRODUCTS/**/domains/*/ata"):
            if not ata_parent.is_dir():
                continue
                
            for child in ata_parent.iterdir():
                if child.is_dir() and re.match(r'^\d{1,3}$', child.name):
                    numeric_dirs.append(child)
                    
        return sorted(numeric_dirs)
    
    def compute_canonical_name(self, numeric_name: str) -> str:
        """Convert numeric name to canonical ATA-XX format."""
        try:
            num = int(numeric_name.lstrip('0') or '0')
            if 1 <= num <= 99:
                return f"ATA-{num:02d}"
            else:
                return None  # Out of valid range
        except ValueError:
            return None
    
    def check_target_conflicts(self, old_path: Path, new_name: str) -> bool:
        """Check if target path already exists with different content."""
        target_path = old_path.parent / new_name
        
        if not target_path.exists():
            return False
            
        # If target exists, it's a conflict - we won't overwrite
        return True
    
    def inventory_renames(self) -> None:
        """Create inventory of all required renames."""
        print("🔍 Creating inventory of numeric ATA directories...")
        
        numeric_dirs = self.find_numeric_ata_dirs()
        print(f"   Found {len(numeric_dirs)} numeric ATA directories")
        
        for old_path in numeric_dirs:
            canonical_name = self.compute_canonical_name(old_path.name)
            
            if canonical_name is None:
                # Skip directories with numbers outside 01-99 range
                self.conflicts.append({
                    'old_path': str(old_path),
                    'reason': f'Number {old_path.name} outside valid range 01-99',
                    'action': 'skipped'
                })
                self.skipped_count += 1
                continue
                
            # Check for conflicts
            if self.check_target_conflicts(old_path, canonical_name):
                self.conflicts.append({
                    'old_path': str(old_path),
                    'new_path': str(old_path.parent / canonical_name),
                    'reason': 'Target directory already exists',
                    'action': 'blocked'
                })
                self.skipped_count += 1
                continue
                
            # Valid rename candidate
            new_path = old_path.parent / canonical_name
            self.rename_map[str(old_path)] = str(new_path)
            
        print(f"   Ready to rename: {len(self.rename_map)} directories")
        print(f"   Conflicts/skipped: {self.skipped_count} directories")
    
    def perform_renames(self) -> None:
        """Execute git mv operations for all planned renames."""
        if not self.rename_map:
            print("   No renames to perform")
            return
            
        print(f"📁 {'[DRY RUN] ' if self.dry_run else ''}Performing directory renames...")
        
        for old_path, new_path in self.rename_map.items():
            old_rel = Path(old_path).relative_to(self.base_dir)
            new_rel = Path(new_path).relative_to(self.base_dir)
            
            print(f"   {old_rel} → {new_rel}")
            
            if not self.dry_run:
                try:
                    result = subprocess.run([
                        'git', 'mv', old_path, new_path
                    ], capture_output=True, text=True, cwd=self.base_dir)
                    
                    if result.returncode != 0:
                        print(f"   ❌ Git mv failed: {result.stderr}")
                        self.conflicts.append({
                            'old_path': old_path,
                            'new_path': new_path,
                            'reason': f'git mv failed: {result.stderr}',
                            'action': 'failed'
                        })
                        continue
                        
                    self.renamed_count += 1
                    
                except Exception as e:
                    print(f"   ❌ Exception during git mv: {e}")
                    self.conflicts.append({
                        'old_path': old_path,
                        'new_path': new_path,
                        'reason': f'Exception: {e}',
                        'action': 'failed'
                    })
            else:
                self.renamed_count += 1
    
    def update_file_links(self, file_path: Path) -> int:
        """Update relative links in a single file."""
        updates_made = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Update paths in content
            for old_path, new_path in self.rename_map.items():
                old_rel = Path(old_path).relative_to(self.base_dir)
                new_rel = Path(new_path).relative_to(self.base_dir)
                
                # Convert to relative path from the file's location
                try:
                    file_rel_to_base = file_path.relative_to(self.base_dir)
                    file_parent_depth = len(file_rel_to_base.parents) - 1
                    
                    # Create different possible relative path patterns
                    patterns = [
                        str(old_rel),
                        f"./{old_rel}",
                        f"../{old_rel}",
                        f"../../{old_rel}",
                        f"../../../{old_rel}",
                    ]
                    
                    replacements = [
                        str(new_rel),
                        f"./{new_rel}",
                        f"../{new_rel}",
                        f"../../{new_rel}",
                        f"../../../{new_rel}",
                    ]
                    
                    for old_pattern, new_pattern in zip(patterns, replacements):
                        if old_pattern in content:
                            content = content.replace(old_pattern, new_pattern)
                            updates_made += 1
                            
                except ValueError:
                    # File is not under base_dir, skip relative path computation
                    pass
                    
            # Write back if changes were made
            if content != original_content and not self.dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
        except Exception as e:
            print(f"   ⚠️  Error updating {file_path}: {e}")
            
        return updates_made
    
    def update_relative_links(self) -> None:
        """Update relative links in MD, JSON, YAML, and XML files."""
        if not self.rename_map:
            print("   No link updates needed")
            return
            
        print(f"🔗 {'[DRY RUN] ' if self.dry_run else ''}Updating relative links...")
        
        file_patterns = ['*.md', '*.json', '*.yaml', '*.yml', '*.xml']
        total_updates = 0
        files_updated = 0
        
        for pattern in file_patterns:
            for file_path in self.base_dir.rglob(pattern):
                if file_path.is_file() and not any(part.startswith('.git') for part in file_path.parts):
                    updates = self.update_file_links(file_path)
                    if updates > 0:
                        files_updated += 1
                        total_updates += updates
                        print(f"   Updated {file_path.relative_to(self.base_dir)}: {updates} links")
                        
        print(f"   Total: {total_updates} link updates in {files_updated} files")
    
    def generate_reports(self) -> None:
        """Generate all required report files."""
        print("📊 Generating reports...")
        
        # 1. Renames CSV
        renames_csv = self.reports_dir / "ata_renames.csv"
        with open(renames_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['old_path', 'new_path'])
            for old_path, new_path in self.rename_map.items():
                old_rel = Path(old_path).relative_to(self.base_dir)
                new_rel = Path(new_path).relative_to(self.base_dir)
                writer.writerow([old_rel, new_rel])
        
        # 2. Conflicts CSV
        conflicts_csv = self.reports_dir / "ata_naming_conflicts.csv"
        with open(conflicts_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['old_path', 'new_path', 'reason', 'action'])
            writer.writeheader()
            for conflict in self.conflicts:
                # Make paths relative for reporting
                conflict_report = conflict.copy()
                if 'old_path' in conflict_report:
                    try:
                        old_rel = Path(conflict_report['old_path']).relative_to(self.base_dir)
                        conflict_report['old_path'] = str(old_rel)
                    except ValueError:
                        pass
                if 'new_path' in conflict_report:
                    try:
                        new_rel = Path(conflict_report['new_path']).relative_to(self.base_dir)
                        conflict_report['new_path'] = str(new_rel)
                    except ValueError:
                        pass
                writer.writerow(conflict_report)
        
        # 3. Summary markdown
        summary_md = self.reports_dir / "ata_naming_summary.md"
        with open(summary_md, 'w', encoding='utf-8') as f:
            f.write("# ATA Chapter Normalization Summary\n\n")
            f.write(f"**Execution mode:** {'DRY RUN' if self.dry_run else 'APPLY'}\n\n")
            f.write("## Summary Statistics\n\n")
            f.write(f"- **Directories renamed:** {self.renamed_count}\n")
            f.write(f"- **Directories skipped:** {self.skipped_count}\n")
            f.write(f"- **Total conflicts:** {len(self.conflicts)}\n\n")
            
            if self.rename_map:
                f.write("## Successful Renames\n\n")
                f.write("| Old Path | New Path |\n")
                f.write("|----------|----------|\n")
                for old_path, new_path in sorted(self.rename_map.items()):
                    old_rel = Path(old_path).relative_to(self.base_dir)
                    new_rel = Path(new_path).relative_to(self.base_dir)
                    f.write(f"| `{old_rel}` | `{new_rel}` |\n")
                f.write("\n")
            
            if self.conflicts:
                f.write("## Conflicts and Skipped Items\n\n")
                f.write("| Path | Reason | Action |\n")
                f.write("|------|--------|--------|\n")
                for conflict in self.conflicts:
                    path = conflict.get('old_path', conflict.get('new_path', ''))
                    try:
                        path_rel = Path(path).relative_to(self.base_dir)
                        path = str(path_rel)
                    except (ValueError, TypeError):
                        pass
                    reason = conflict.get('reason', '')
                    action = conflict.get('action', '')
                    f.write(f"| `{path}` | {reason} | {action} |\n")
        
        print(f"   📄 Reports generated:")
        print(f"   - {renames_csv}")
        print(f"   - {conflicts_csv}")
        print(f"   - {summary_md}")
    
    def run_validation(self) -> bool:
        """Run the required validation scripts."""
        if self.dry_run:
            print("⏭️  Skipping validation in dry run mode")
            return True
            
        print("✅ Running validation scripts...")
        
        # Locate the scripts
        scripts_dir = self.base_dir / "PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/cax/CAD/scripts"
        if not scripts_dir.exists():
            print(f"   ⚠️  Scripts directory not found: {scripts_dir}")
            return False
        
        validation_commands = [
            ["python", scripts_dir / "link_check.py", "PRODUCTS"],
            ["python", scripts_dir / "naming_guard.py", "PRODUCTS"],
            ["python", scripts_dir / "validate_json.py", 
             "PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/cax/CAD/schemas", 
             "PRODUCTS"]
        ]
        
        all_passed = True
        
        for cmd in validation_commands:
            print(f"   Running: {' '.join(str(c) for c in cmd)}")
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.base_dir)
                if result.returncode == 0:
                    print(f"   ✅ Passed")
                else:
                    print(f"   ❌ Failed with exit code {result.returncode}")
                    if result.stdout:
                        print(f"      stdout: {result.stdout[:200]}...")
                    if result.stderr:
                        print(f"      stderr: {result.stderr[:200]}...")
                    all_passed = False
            except Exception as e:
                print(f"   ❌ Exception running validation: {e}")
                all_passed = False
        
        return all_passed
    
    def execute(self) -> bool:
        """Execute the complete normalization process."""
        print(f"🚀 ATA Chapter Normalization ({'DRY RUN' if self.dry_run else 'APPLY MODE'})")
        print(f"   Base directory: {self.base_dir}")
        print()
        
        # Step 1: Inventory
        self.inventory_renames()
        
        # Step 2: Perform renames
        self.perform_renames()
        
        # Step 3: Update links
        self.update_relative_links()
        
        # Step 4: Generate reports
        self.generate_reports()
        
        # Step 5: Validate (only in apply mode)
        validation_passed = self.run_validation()
        
        # Summary
        print()
        print("🎯 Summary:")
        print(f"   Mode: {'DRY RUN' if self.dry_run else 'APPLY'}")
        print(f"   Renamed: {self.renamed_count} directories")
        print(f"   Skipped: {self.skipped_count} directories")
        print(f"   Conflicts: {len(self.conflicts)}")
        
        if not self.dry_run:
            print(f"   Validation: {'✅ PASSED' if validation_passed else '❌ FAILED'}")
            return validation_passed
        
        return True


def main():
    # Determine execution mode
    dry_run = True
    if os.getenv('DRY_RUN', '').lower() == 'false' or os.getenv('APPLY', '').lower() == 'true':
        dry_run = False
    
    # Get base directory
    base_dir = Path(__file__).parent.parent
    if not (base_dir / "PRODUCTS").exists():
        print("❌ PRODUCTS directory not found. Run from repository root.")
        sys.exit(1)
    
    # Execute normalization
    normalizer = ATANormalizer(base_dir, dry_run=dry_run)
    success = normalizer.execute()
    
    if not success:
        print("❌ Normalization completed with validation errors")
        sys.exit(1)
    else:
        print("✅ Normalization completed successfully")


if __name__ == "__main__":
    main()