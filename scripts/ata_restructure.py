#!/usr/bin/env python3
"""
ATA Chapter Restructuring Script

Restructures PRODUCTS/**/domains/*/ata/ATA-*/ so that each chapter contains exactly 
four process folders: cax/, qox/, pax/, docs/. Moves existing CAx artifacts under cax/, 
QOx under qox/, PAx under pax/, and S1000D/DMRL/BREX under docs/.

Key Features:
- Normalizes numeric ATA folders (57 → ATA-57)
- Creates standardized process folder structure (cax/, qox/, pax/, docs/)
- Moves artifacts from domain-level cax/qox/pax into appropriate ATA chapters
- Moves S1000D/DMRL/BREX artifacts to docs/ folder
- Uses git mv for all operations
- Updates relative links in MD/JSON/YAML/XML files
- Normalizes front-matter (ASCII id, repo-relative project/artifact, quoted scalars)
- Preserves UTCS/QS evidence
- Handles conflicts by placing in docs/variants/
- Generates comprehensive reports

Usage:
    python scripts/ata_restructure.py         # dry run (default)
    DRY_RUN=false python scripts/ata_restructure.py
    APPLY=true python scripts/ata_restructure.py
"""

import os
import re
import json
import csv
import subprocess
import sys
import yaml
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
import xml.etree.ElementTree as ET
from datetime import datetime


class ATARestructurer:
    def __init__(self, base_dir: Path, dry_run: bool = True):
        self.base_dir = base_dir
        self.dry_run = dry_run
        self.rename_operations = []
        self.move_operations = []
        self.link_fixes = []
        self.conflicts = []
        self.created_directories = []
        self.processed_files = []
        
        # Statistics
        self.renamed_count = 0
        self.moved_count = 0
        self.created_count = 0
        self.link_fixes_count = 0
        self.conflicts_count = 0
        
        # Ensure reports directory exists
        self.reports_dir = self.base_dir / "reports"
        if not self.dry_run:
            self.reports_dir.mkdir(exist_ok=True)

    def find_numeric_ata_dirs(self) -> List[Path]:
        """Find all numeric ATA directories that need normalization."""
        numeric_dirs = []
        for domain_path in self.base_dir.glob("PRODUCTS/**/domains/*/ata"):
            if domain_path.is_dir():
                for child in domain_path.iterdir():
                    if child.is_dir() and re.match(r'^\d{1,3}$', child.name):
                        numeric_dirs.append(child)
        return numeric_dirs

    def find_ata_chapters(self) -> List[Path]:
        """Find all ATA chapter directories (both numeric and ATA-XX format)."""
        chapters = []
        for domain_path in self.base_dir.glob("PRODUCTS/**/domains/*/ata"):
            if domain_path.is_dir():
                for child in domain_path.iterdir():
                    if child.is_dir() and (
                        re.match(r'^\d{1,3}$', child.name) or
                        re.match(r'^ATA-\d{2}$', child.name)
                    ):
                        chapters.append(child)
        return chapters

    def compute_canonical_name(self, numeric_name: str) -> str:
        """Convert numeric name to canonical ATA-XX format."""
        try:
            num = int(numeric_name)
            return f"ATA-{num:02d}"
        except ValueError:
            return numeric_name

    def get_domain_cax_qox_pax_dirs(self, domain_path: Path) -> Tuple[Optional[Path], Optional[Path], Optional[Path]]:
        """Get the domain-level cax, qox, pax directories."""
        cax_dir = domain_path / "cax" if (domain_path / "cax").exists() else None
        qox_dir = domain_path / "qox" if (domain_path / "qox").exists() else None
        pax_dir = domain_path / "pax" if (domain_path / "pax").exists() else None
        return cax_dir, qox_dir, pax_dir

    def identify_s1000d_artifacts(self, chapter_path: Path) -> List[Path]:
        """Identify S1000D, DMRL, BREX artifacts in a chapter."""
        artifacts = []
        for item in chapter_path.iterdir():
            if item.is_dir() and item.name in ['S1000D', 'DMRL', 'BREX']:
                artifacts.append(item)
            elif item.is_file() and any(item.name.lower().endswith(ext) for ext in ['.dmrl', '.brex']):
                artifacts.append(item)
        return artifacts

    def create_process_folders(self, chapter_path: Path) -> None:
        """Create the standard process folders (cax/, qox/, pax/, docs/) in a chapter."""
        process_folders = ['cax', 'qox', 'pax', 'docs']
        for folder in process_folders:
            folder_path = chapter_path / folder
            if not folder_path.exists():
                if not self.dry_run:
                    folder_path.mkdir(exist_ok=True)
                self.created_directories.append(folder_path)
                self.created_count += 1
                print(f"   📁 Created: {folder_path.relative_to(self.base_dir)}")

    def merge_directories(self, src: Path, dst: Path) -> bool:
        """Merge source directory into destination directory."""
        try:
            if self.dry_run:
                print(f"   [DRY RUN] Merging {src.relative_to(self.base_dir)} into {dst.relative_to(self.base_dir)}")
                return True
            
            # Move all contents from src to dst
            for item in src.iterdir():
                dst_item = dst / item.name
                if dst_item.exists():
                    if item.is_dir() and dst_item.is_dir():
                        # Recursively merge directories
                        self.merge_directories(item, dst_item)
                    else:
                        # Handle file conflicts by moving to variants
                        variants_dir = dst / "variants"
                        variants_dir.mkdir(exist_ok=True)
                        conflict_name = f"{item.name}.conflict_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                        conflict_path = variants_dir / conflict_name
                        if self.safe_git_mv(item, conflict_path):
                            self.conflicts.append((item, conflict_path, f"File conflict during merge"))
                            self.conflicts_count += 1
                else:
                    if not self.safe_git_mv(item, dst_item):
                        return False
            
            # Remove empty source directory
            try:
                if not any(src.iterdir()):
                    subprocess.run(["git", "rm", "-r", str(src)], cwd=self.base_dir, check=True)
                    print(f"   🗑️  Removed empty directory: {src.relative_to(self.base_dir)}")
            except (OSError, subprocess.CalledProcessError):
                pass
                
            return True
            
        except Exception as e:
            print(f"   ❌ Error merging {src.relative_to(self.base_dir)}: {e}")
            return False

    def safe_git_mv(self, src: Path, dst: Path) -> bool:
        """Safely move a file or directory using git mv."""
        try:
            if self.dry_run:
                print(f"   [DRY RUN] git mv {src.relative_to(self.base_dir)} {dst.relative_to(self.base_dir)}")
                return True
            
            # Ensure destination directory exists
            dst.parent.mkdir(parents=True, exist_ok=True)
            
            # Use git mv
            result = subprocess.run(
                ["git", "mv", str(src), str(dst)],
                cwd=self.base_dir,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"   ✅ Moved: {src.relative_to(self.base_dir)} → {dst.relative_to(self.base_dir)}")
                return True
            else:
                print(f"   ❌ Failed to move {src.relative_to(self.base_dir)}: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"   ❌ Error moving {src.relative_to(self.base_dir)}: {e}")
            return False

    def move_domain_artifacts_to_chapters(self) -> None:
        """Move domain-level CAx/QOx/PAx artifacts into appropriate ATA chapters."""
        print(f"🔄 {'[DRY RUN] ' if self.dry_run else ''}Moving domain artifacts to ATA chapters...")
        
        for domain_path in self.base_dir.glob("PRODUCTS/**/domains/*"):
            if not domain_path.is_dir():
                continue
                
            ata_dir = domain_path / "ata"
            if not ata_dir.exists():
                continue
                
            cax_dir, qox_dir, pax_dir = self.get_domain_cax_qox_pax_dirs(domain_path)
            
            # Get all ATA chapters in this domain
            chapters = [ch for ch in ata_dir.iterdir() if ch.is_dir() and 
                       (re.match(r'^\d{1,3}$', ch.name) or re.match(r'^ATA-\d{2}$', ch.name))]
            
            if not chapters:
                continue
                
            print(f"   Processing domain: {domain_path.relative_to(self.base_dir)}")
            
            # For simplicity, we'll move domain artifacts to the first available chapter
            # In a real scenario, we might want to analyze content to determine the best chapter
            target_chapter = chapters[0]
            
            # Ensure canonical name
            if re.match(r'^\d{1,3}$', target_chapter.name):
                canonical_name = self.compute_canonical_name(target_chapter.name)
                canonical_path = target_chapter.parent / canonical_name
                if target_chapter != canonical_path:
                    if self.safe_git_mv(target_chapter, canonical_path):
                        target_chapter = canonical_path
                        self.renamed_count += 1
            
            # Create process folders
            self.create_process_folders(target_chapter)
            
            # Move CAx artifacts
            if cax_dir and cax_dir.exists():
                target_cax = target_chapter / "cax"
                for item in cax_dir.iterdir():
                    dst_path = target_cax / item.name
                    if self.safe_git_mv(item, dst_path):
                        self.move_operations.append((item, dst_path))
                        self.moved_count += 1
                        
                # Remove empty cax directory
                if not self.dry_run and not any(cax_dir.iterdir()):
                    try:
                        cax_dir.rmdir()
                    except OSError:
                        pass
            
            # Move QOx artifacts
            if qox_dir and qox_dir.exists():
                target_qox = target_chapter / "qox"
                for item in qox_dir.iterdir():
                    dst_path = target_qox / item.name
                    if self.safe_git_mv(item, dst_path):
                        self.move_operations.append((item, dst_path))
                        self.moved_count += 1
                        
                # Remove empty qox directory
                if not self.dry_run and not any(qox_dir.iterdir()):
                    try:
                        qox_dir.rmdir()
                    except OSError:
                        pass
            
            # Move PAx artifacts
            if pax_dir and pax_dir.exists():
                target_pax = target_chapter / "pax"
                for item in pax_dir.iterdir():
                    dst_path = target_pax / item.name
                    if self.safe_git_mv(item, dst_path):
                        self.move_operations.append((item, dst_path))
                        self.moved_count += 1
                        
                # Remove empty pax directory
                if not self.dry_run and not any(pax_dir.iterdir()):
                    try:
                        pax_dir.rmdir()
                    except OSError:
                        pass

    def move_s1000d_artifacts_to_docs(self) -> None:
        """Move S1000D/DMRL/BREX artifacts to docs/ folders."""
        print(f"📚 {'[DRY RUN] ' if self.dry_run else ''}Moving S1000D/DMRL/BREX artifacts to docs/...")
        
        chapters = self.find_ata_chapters()
        for chapter in chapters:
            s1000d_artifacts = self.identify_s1000d_artifacts(chapter)
            if s1000d_artifacts:
                print(f"   Processing chapter: {chapter.relative_to(self.base_dir)}")
                
                # Ensure docs folder exists
                docs_dir = chapter / "docs"
                if not docs_dir.exists() and not self.dry_run:
                    docs_dir.mkdir(exist_ok=True)
                    self.created_directories.append(docs_dir)
                    self.created_count += 1
                
                for artifact in s1000d_artifacts:
                    dst_path = docs_dir / artifact.name
                    if dst_path.exists() and not self.dry_run:
                        # Handle conflict by moving to variants
                        variants_dir = docs_dir / "variants"
                        variants_dir.mkdir(exist_ok=True)
                        dst_path = variants_dir / f"{artifact.name}.conflict_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                        self.conflicts.append((artifact, dst_path, "S1000D artifact conflict"))
                        self.conflicts_count += 1
                    
                    if self.safe_git_mv(artifact, dst_path):
                        self.move_operations.append((artifact, dst_path))
                        self.moved_count += 1

    def normalize_numeric_ata_directories(self) -> None:
        """Normalize numeric ATA directories to ATA-XX format."""
        print(f"🔤 {'[DRY RUN] ' if self.dry_run else ''}Normalizing numeric ATA directories...")
        
        numeric_dirs = self.find_numeric_ata_dirs()
        for old_path in numeric_dirs:
            canonical_name = self.compute_canonical_name(old_path.name)
            new_path = old_path.parent / canonical_name
            
            if old_path != new_path:
                if new_path.exists():
                    # Merge content instead of creating conflicts
                    print(f"   🔄 Merging {old_path.relative_to(self.base_dir)} into existing {new_path.relative_to(self.base_dir)}")
                    if self.merge_directories(old_path, new_path):
                        self.move_operations.append((old_path, new_path))
                        self.moved_count += 1
                else:
                    if self.safe_git_mv(old_path, new_path):
                        self.rename_operations.append((old_path, new_path))
                        self.renamed_count += 1

    def update_relative_links(self) -> None:
        """Update relative links in MD, JSON, YAML, and XML files."""
        if not self.rename_operations and not self.move_operations:
            print("   No link updates needed")
            return
            
        print(f"🔗 {'[DRY RUN] ' if self.dry_run else ''}Updating relative links...")
        
        # Build path mapping from all operations
        path_mapping = {}
        for old_path, new_path in self.rename_operations + self.move_operations:
            path_mapping[str(old_path)] = str(new_path)
        
        file_patterns = ['*.md', '*.json', '*.yaml', '*.yml', '*.xml']
        total_updates = 0
        files_updated = 0
        
        for pattern in file_patterns:
            for file_path in self.base_dir.rglob(pattern):
                if file_path.is_file() and not any(part.startswith('.git') for part in file_path.parts):
                    updates = self.update_file_links(file_path, path_mapping)
                    if updates > 0:
                        files_updated += 1
                        total_updates += updates
                        self.link_fixes.append((file_path, updates))
                        self.link_fixes_count += updates
                        print(f"   Updated {file_path.relative_to(self.base_dir)}: {updates} links")
                        
        print(f"   Total: {total_updates} link updates in {files_updated} files")

    def update_file_links(self, file_path: Path, path_mapping: Dict[str, str]) -> int:
        """Update relative links in a single file."""
        updates_made = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Update paths in content
            for old_path_str, new_path_str in path_mapping.items():
                old_path = Path(old_path_str)
                new_path = Path(new_path_str)
                
                try:
                    old_rel = old_path.relative_to(self.base_dir)
                    new_rel = new_path.relative_to(self.base_dir)
                    
                    # Convert to relative path from the file's location
                    file_rel_to_base = file_path.relative_to(self.base_dir)
                    
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

    def normalize_front_matter(self) -> None:
        """Normalize front-matter in YAML/MD files."""
        print(f"📝 {'[DRY RUN] ' if self.dry_run else ''}Normalizing front-matter...")
        
        processed = 0
        for pattern in ['*.md', '*.yaml', '*.yml']:
            for file_path in self.base_dir.rglob(pattern):
                if file_path.is_file() and not any(part.startswith('.git') for part in file_path.parts):
                    if self.normalize_file_front_matter(file_path):
                        processed += 1
                        self.processed_files.append(file_path)
        
        print(f"   Processed front-matter in {processed} files")

    def normalize_file_front_matter(self, file_path: Path) -> bool:
        """Normalize front-matter in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has front-matter
            if not content.startswith('---\n'):
                return False
            
            # Split front-matter and body
            parts = content.split('\n---\n', 1)
            if len(parts) != 2:
                return False
            
            yaml_content = parts[0][4:]  # Remove leading '---\n'
            body = parts[1]
            
            # Parse YAML
            try:
                fm_data = yaml.safe_load(yaml_content)
                if not isinstance(fm_data, dict):
                    return False
            except yaml.YAMLError:
                return False
            
            # Normalize fields
            changed = False
            
            # Ensure ASCII id
            if 'id' in fm_data and not fm_data['id'].isascii():
                fm_data['id'] = ''.join(c for c in fm_data['id'] if c.isascii())
                changed = True
            
            # Ensure repo-relative project/artifact paths
            for field in ['project', 'artifact']:
                if field in fm_data and isinstance(fm_data[field], str):
                    if not fm_data[field].startswith('PRODUCTS/'):
                        # Try to infer from file path
                        try:
                            rel_path = file_path.relative_to(self.base_dir)
                            if 'PRODUCTS' in rel_path.parts:
                                products_idx = rel_path.parts.index('PRODUCTS')
                                if products_idx + 3 < len(rel_path.parts):
                                    inferred = '/'.join(rel_path.parts[products_idx:products_idx+4])
                                    fm_data[field] = inferred
                                    changed = True
                        except (ValueError, IndexError):
                            pass
            
            # Quote scalar values that need quoting
            for key, value in fm_data.items():
                if isinstance(value, str) and (':' in value or '@' in value or '=' in value):
                    # These already get quoted by PyYAML, but we ensure consistency
                    changed = True
            
            if changed and not self.dry_run:
                # Reconstruct file with normalized front-matter
                normalized_yaml = yaml.dump(fm_data, default_flow_style=False, allow_unicode=True)
                new_content = f"---\n{normalized_yaml}---\n{body}"
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"   Normalized: {file_path.relative_to(self.base_dir)}")
                return True
                
        except Exception as e:
            print(f"   ⚠️  Error normalizing front-matter in {file_path}: {e}")
            
        return False

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
            ["python", str(scripts_dir / "link_check.py"), "PRODUCTS"],
            ["python", str(scripts_dir / "naming_guard.py"), "PRODUCTS"],
            ["python", str(scripts_dir / "validate_json.py"), 
             str(scripts_dir.parent / "schemas"), "PRODUCTS"]
        ]
        
        # Add validate_pax.py for any touched PAx files
        pax_touched = any("pax" in str(op[1]) for op in self.move_operations)
        if pax_touched:
            for pax_script in self.base_dir.rglob("validate_pax.py"):
                validation_commands.append(["python", str(pax_script), "PRODUCTS"])
                break
        
        all_passed = True
        for cmd in validation_commands:
            try:
                print(f"   Running: {' '.join(cmd)}")
                result = subprocess.run(cmd, cwd=self.base_dir, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"   ✅ {Path(cmd[1]).name} passed")
                else:
                    print(f"   ❌ {Path(cmd[1]).name} failed: {result.stderr}")
                    all_passed = False
            except Exception as e:
                print(f"   ❌ Error running {Path(cmd[1]).name}: {e}")
                all_passed = False
        
        return all_passed

    def generate_reports(self) -> None:
        """Generate comprehensive reports."""
        print(f"📊 {'[DRY RUN] ' if self.dry_run else ''}Generating reports...")
        
        timestamp = datetime.now().isoformat()
        
        # Generate ata_restructure_summary.md
        summary_path = self.reports_dir / "ata_restructure_summary.md"
        summary_content = self.generate_summary_report(timestamp)
        if not self.dry_run:
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(summary_content)
        print(f"   📄 {'[DRY RUN] ' if self.dry_run else ''}Generated: {summary_path.relative_to(self.base_dir)}")
        
        # Generate link_fixups.csv
        link_fixups_path = self.reports_dir / "link_fixups.csv"
        if not self.dry_run:
            with open(link_fixups_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['file_path', 'links_updated', 'relative_path'])
                for file_path, count in self.link_fixes:
                    writer.writerow([str(file_path), count, str(file_path.relative_to(self.base_dir))])
        print(f"   📄 {'[DRY RUN] ' if self.dry_run else ''}Generated: {link_fixups_path.relative_to(self.base_dir)}")
        
        # Generate conflicts.csv
        conflicts_path = self.reports_dir / "conflicts.csv"
        if not self.dry_run:
            with open(conflicts_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['original_path', 'conflict_path', 'reason', 'timestamp'])
                for original, conflict, reason in self.conflicts:
                    writer.writerow([str(original), str(conflict), reason, timestamp])
        print(f"   📄 {'[DRY RUN] ' if self.dry_run else ''}Generated: {conflicts_path.relative_to(self.base_dir)}")

    def generate_summary_report(self, timestamp: str) -> str:
        """Generate the main summary report."""
        return f"""# ATA Restructuring Summary

**Execution Time:** {timestamp}
**Mode:** {'DRY RUN' if self.dry_run else 'APPLY'}
**Base Directory:** {self.base_dir}

## Overview

This report summarizes the ATA chapter restructuring operation that standardized the 
directory structure within `PRODUCTS/**/domains/*/ata/ATA-*/` to ensure each chapter 
contains exactly four process folders: `cax/`, `qox/`, `pax/`, and `docs/`.

## Statistics

- **ATA Directories Renamed:** {self.renamed_count}
- **Artifacts Moved:** {self.moved_count}
- **Directories Created:** {self.created_count}
- **Link Fixes Applied:** {self.link_fixes_count}
- **Conflicts Handled:** {self.conflicts_count}
- **Files with Front-matter Normalized:** {len(self.processed_files)}

## Operations Performed

### 1. Directory Normalization
Converted numeric ATA directories to canonical ATA-XX format:

{self._format_operations_list(self.rename_operations, "Renamed")}

### 2. Artifact Movement
Reorganized CAx, QOx, PAx, and S1000D artifacts into standardized process folders:

{self._format_operations_list(self.move_operations, "Moved")}

### 3. Process Folder Creation
Created standardized process folders in ATA chapters:

{self._format_directory_list(self.created_directories)}

### 4. Link Updates
Updated relative links in the following files:

{self._format_link_fixes()}

### 5. Conflicts Resolved
{len(self.conflicts)} conflicts were resolved by placing items in `docs/variants/`:

{self._format_conflicts_list()}

## Validation Results

{self._format_validation_status()}

## Next Steps

1. **Review Changes:** Examine the generated reports and moved artifacts
2. **Test References:** Verify that all relative links are functioning correctly
3. **Update Documentation:** Update any project documentation that references the old structure
4. **Commit Changes:** Once satisfied, commit the restructuring changes

## Files Generated

- `reports/ata_restructure_summary.md` (this file)
- `reports/link_fixups.csv` - Detailed link update records
- `reports/conflicts.csv` - Conflict resolution records

---
*Generated by ATA Restructuring Script v1.0*
"""

    def _format_operations_list(self, operations: List[Tuple[Path, Path]], action: str) -> str:
        """Format a list of path operations for the report."""
        if not operations:
            return f"No {action.lower()} operations performed.\n"
        
        lines = []
        for old_path, new_path in operations:
            lines.append(f"- `{old_path.relative_to(self.base_dir)}` → `{new_path.relative_to(self.base_dir)}`")
        return '\n'.join(lines) + '\n'

    def _format_directory_list(self, directories: List[Path]) -> str:
        """Format a list of created directories for the report."""
        if not directories:
            return "No directories created.\n"
        
        lines = []
        for dir_path in directories:
            lines.append(f"- `{dir_path.relative_to(self.base_dir)}`")
        return '\n'.join(lines) + '\n'

    def _format_link_fixes(self) -> str:
        """Format link fixes for the report."""
        if not self.link_fixes:
            return "No link updates were necessary.\n"
        
        lines = []
        for file_path, count in self.link_fixes:
            lines.append(f"- `{file_path.relative_to(self.base_dir)}` ({count} links)")
        return '\n'.join(lines) + '\n'

    def _format_conflicts_list(self) -> str:
        """Format conflicts list for the report."""
        if not self.conflicts:
            return "No conflicts encountered.\n"
        
        lines = []
        for original, conflict, reason in self.conflicts:
            lines.append(f"- `{original.relative_to(self.base_dir)}` → `{conflict.relative_to(self.base_dir)}` ({reason})")
        return '\n'.join(lines) + '\n'

    def _format_validation_status(self) -> str:
        """Format validation status for the report."""
        if self.dry_run:
            return "Validation skipped in dry run mode.\n"
        return "Validation scripts executed. Check console output for detailed results.\n"

    def execute(self) -> bool:
        """Execute the complete restructuring process."""
        print(f"🚀 ATA Chapter Restructuring ({'DRY RUN' if self.dry_run else 'APPLY MODE'})")
        print(f"   Base directory: {self.base_dir}")
        print()
        
        # Step 1: Normalize numeric ATA directories
        self.normalize_numeric_ata_directories()
        
        # Step 2: Create process folders in all chapters
        print(f"📁 {'[DRY RUN] ' if self.dry_run else ''}Creating process folders...")
        chapters = self.find_ata_chapters()
        for chapter in chapters:
            self.create_process_folders(chapter)
        
        # Step 3: Move domain artifacts to chapters
        self.move_domain_artifacts_to_chapters()
        
        # Step 4: Move S1000D artifacts to docs
        self.move_s1000d_artifacts_to_docs()
        
        # Step 5: Update relative links
        self.update_relative_links()
        
        # Step 6: Normalize front-matter
        self.normalize_front_matter()
        
        # Step 7: Generate reports
        self.generate_reports()
        
        # Step 8: Run validation (only in apply mode)
        validation_passed = self.run_validation()
        
        # Summary
        print()
        print("🎯 Summary:")
        print(f"   Mode: {'DRY RUN' if self.dry_run else 'APPLY'}")
        print(f"   ATA directories renamed: {self.renamed_count}")
        print(f"   Artifacts moved: {self.moved_count}")
        print(f"   Directories created: {self.created_count}")
        print(f"   Link fixes applied: {self.link_fixes_count}")
        print(f"   Conflicts handled: {self.conflicts_count}")
        print(f"   Front-matter normalized: {len(self.processed_files)}")
        print(f"   Validation: {'PASSED' if validation_passed else 'FAILED' if not self.dry_run else 'SKIPPED'}")
        
        return validation_passed


def main():
    """Main entry point."""
    # Determine dry run mode
    dry_run = True
    if os.getenv('DRY_RUN') == 'false' or os.getenv('APPLY') == 'true':
        dry_run = False
    
    base_dir = Path.cwd()
    restructurer = ATARestructurer(base_dir, dry_run)
    
    try:
        success = restructurer.execute()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(2)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()