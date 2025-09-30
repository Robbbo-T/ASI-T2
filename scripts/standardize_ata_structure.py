#!/usr/bin/env python3
"""
ATA Canonical Structure Standardization Script

Creates and manages canonical ATA chapter directories in 2-DOMAINS-LEVELS/
and ensures product trees have proper symlinks.

Usage:
    python scripts/standardize_ata_structure.py --help
    python scripts/standardize_ata_structure.py --atas ATA-42 --domain IIS --create
    python scripts/standardize_ata_structure.py --validate
    python scripts/standardize_ata_structure.py --atas ATA-42 --include-shared --verbose
"""

import argparse
import os
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import shutil


class ATAStructureManager:
    """Manages canonical ATA structure creation and validation."""
    
    # Standard directory structure for canonical ATA folders
    STANDARD_STRUCTURE = [
        "governance/change_control",
        "governance/baselines",
        "governance/risk_management",
        "governance/audits",
        "os/S1000D",
        "os/design/architecture",
        "os/design/icd",
        "os/design/diagrams",
        "os/configuration/manifests",
        "os/testing",
        "os/compliance/certification",
        "os/compliance/verification",
        "manufacturing/bom",
        "manufacturing/process",
        "manufacturing/quality",
        "manufacturing/tooling",
        "manufacturing/test",
        "manufacturing/packaging/manifests",
        "sustainment/service_mro",
        "sustainment/spares",
        "sustainment/reliability",
        "sustainment/obsolescence",
        "sustainment/cas_security",
        "sustainment/recycling_disposal/weee_rohs_reach",
        "sustainment/recycling_disposal/data_sanitization",
        "sustainment/recycling_disposal/manifests",
        "assets",
        "scripts",
        "docs",
    ]
    
    def __init__(self, repo_root: Path, verbose: bool = False, dry_run: bool = False):
        self.repo_root = repo_root
        self.verbose = verbose
        self.dry_run = dry_run
        self.resources_dir = repo_root / "8-RESOURCES" / "ATA_CANONICAL"
        self.canonical_base = repo_root / "2-DOMAINS-LEVELS"
        
        # Load registry
        self.registry = self._load_registry()
        
    def _load_registry(self) -> Dict:
        """Load ATA registry from resources."""
        registry_path = self.resources_dir / "ATA_REGISTRY.yaml"
        if not registry_path.exists():
            self._error(f"Registry not found: {registry_path}")
            return {"ata_chapters": [], "domains": []}
        
        with open(registry_path, 'r') as f:
            return yaml.safe_load(f)
    
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
    
    def _error(self, message: str, exit_code: int = 1):
        """Log error and exit."""
        self._log(message, "ERROR")
        sys.exit(exit_code)
    
    def get_ata_info(self, ata: str) -> Optional[Dict]:
        """Get ATA chapter information from registry."""
        for chapter in self.registry.get("ata_chapters", []):
            if chapter["ata"] == ata:
                return chapter
        return None
    
    def get_domain_info(self, domain_code: str) -> Optional[Dict]:
        """Get domain information from registry."""
        for domain in self.registry.get("domains", []):
            if domain["code"] == domain_code:
                return domain
        return None
    
    def create_canonical_structure(self, ata: str, domain: Optional[str] = None) -> Path:
        """Create canonical ATA structure."""
        # Get ATA info
        ata_info = self.get_ata_info(ata)
        if not ata_info:
            self._error(f"ATA {ata} not found in registry")
        
        # Determine domain
        if domain is None:
            domain = ata_info["canonical_domain"]
        
        canonical_path = self.canonical_base / domain / "ata" / ata
        
        if canonical_path.exists():
            self._log(f"Canonical path already exists: {canonical_path}", "WARNING")
            return canonical_path
        
        self._log(f"Creating canonical structure for {ata} in domain {domain}")
        
        if self.dry_run:
            self._log(f"[DRY RUN] Would create: {canonical_path}", "DEBUG")
            return canonical_path
        
        # Create base directory
        canonical_path.mkdir(parents=True, exist_ok=True)
        
        # Create standard subdirectories
        for subdir in self.STANDARD_STRUCTURE:
            dir_path = canonical_path / subdir
            dir_path.mkdir(parents=True, exist_ok=True)
            self._log(f"  Created: {subdir}", "DEBUG")
        
        # Copy and customize README
        self._create_readme(canonical_path, ata, domain, ata_info)
        
        # Copy and customize CONVENTIONS
        self._create_conventions(canonical_path, ata, domain)
        
        # Create empty cross_references.yaml
        self._create_cross_references(canonical_path)
        
        self._log(f"Created canonical structure at {canonical_path}", "SUCCESS")
        return canonical_path
    
    def _create_readme(self, canonical_path: Path, ata: str, domain: str, ata_info: Dict):
        """Create README from template."""
        template_path = self.resources_dir / "ATA_README_TEMPLATE.md"
        readme_path = canonical_path / "README.md"
        
        if not template_path.exists():
            self._log(f"Template not found: {template_path}", "WARNING")
            return
        
        with open(template_path, 'r') as f:
            content = f.read()
        
        # Replace placeholders
        ata_number = ata.replace("ATA-", "")
        content = content.replace("<DOMAIN>", domain)
        content = content.replace("<ATA>", ata)
        content = content.replace("<Short Title>", ata_info.get("title", ""))
        content = content.replace("<DOMAIN TEAM>", f"{domain} Team")
        
        # Add shared domains info if applicable
        shared = ata_info.get("shared_domains", [])
        if shared:
            shared_str = ", ".join(shared)
            content = content.replace("[<DOM?>, ...]", f"[{shared_str}]")
        
        with open(readme_path, 'w') as f:
            f.write(content)
        
        self._log(f"  Created README.md", "DEBUG")
    
    def _create_conventions(self, canonical_path: Path, ata: str, domain: str):
        """Create CONVENTIONS from template."""
        template_path = self.resources_dir / "CONVENTIONS_TEMPLATE.md"
        conventions_path = canonical_path / "CONVENTIONS.md"
        
        if not template_path.exists():
            self._log(f"Template not found: {template_path}", "WARNING")
            return
        
        with open(template_path, 'r') as f:
            content = f.read()
        
        # Replace placeholders
        from datetime import date
        ata_number = ata.replace("ATA-", "")
        content = content.replace("<ATA_NUMBER>", ata_number)
        content = content.replace("<DOMAIN>", domain)
        content = content.replace("<DATE>", date.today().isoformat())
        content = content.replace("<ATA>", ata)
        
        with open(conventions_path, 'w') as f:
            f.write(content)
        
        self._log(f"  Created CONVENTIONS.md", "DEBUG")
    
    def _create_cross_references(self, canonical_path: Path):
        """Create empty cross_references.yaml."""
        xref_path = canonical_path / "governance" / "cross_references.yaml"
        
        content = """# Cross-References
# See schema in 8-RESOURCES/ATA_CANONICAL/XREF_MASTER.yaml

xrefs: []
"""
        
        with open(xref_path, 'w') as f:
            f.write(content)
        
        self._log(f"  Created governance/cross_references.yaml", "DEBUG")
    
    def find_product_ata_dirs(self, ata: str, domain: str) -> List[Path]:
        """Find product directories that should link to this canonical ATA."""
        product_dirs = []
        products_base = self.repo_root / "PRODUCTS"
        
        if not products_base.exists():
            return product_dirs
        
        # Search for matching domain/ata directories in products
        pattern = f"**/domains/{domain}/ata/{ata}"
        for path in products_base.glob(pattern):
            if path.is_dir() and not path.is_symlink():
                product_dirs.append(path)
        
        return product_dirs
    
    def create_symlinks(self, ata: str, domain: str) -> int:
        """Create symlinks from product trees to canonical location."""
        canonical_path = self.canonical_base / domain / "ata" / ata
        
        if not canonical_path.exists():
            self._log(f"Canonical path does not exist: {canonical_path}", "WARNING")
            return 0
        
        product_dirs = self.find_product_ata_dirs(ata, domain)
        
        if not product_dirs:
            self._log(f"No product directories found for {domain}/{ata}")
            return 0
        
        self._log(f"Found {len(product_dirs)} product directories to convert to symlinks")
        
        created = 0
        for product_dir in product_dirs:
            # Calculate relative path from product dir to canonical
            # Product: PRODUCTS/.../domains/DOMAIN/ata/ATA
            # Canonical: 2-DOMAINS-LEVELS/DOMAIN/ata/ATA
            
            # Get relative path
            try:
                # Count levels up from product_dir to repo root
                rel_to_root = os.path.relpath(self.repo_root, product_dir)
                # Then down to canonical
                rel_canonical = canonical_path.relative_to(self.repo_root)
                symlink_target = Path(rel_to_root) / rel_canonical
                
                if self.dry_run:
                    self._log(f"[DRY RUN] Would create symlink: {product_dir} -> {symlink_target}", "DEBUG")
                    created += 1
                else:
                    # Check if it's already a symlink
                    if product_dir.is_symlink():
                        self._log(f"  Already a symlink: {product_dir}", "DEBUG")
                        continue
                    
                    # Backup existing directory
                    if product_dir.exists():
                        backup_path = product_dir.parent / f"{product_dir.name}.backup"
                        self._log(f"  Backing up existing: {product_dir} -> {backup_path}", "DEBUG")
                        if backup_path.exists():
                            shutil.rmtree(backup_path)
                        shutil.move(str(product_dir), str(backup_path))
                    
                    # Create symlink
                    product_dir.symlink_to(symlink_target)
                    self._log(f"  Created symlink: {product_dir.relative_to(self.repo_root)}", "SUCCESS")
                    created += 1
                    
            except Exception as e:
                self._log(f"Failed to create symlink for {product_dir}: {e}", "ERROR")
        
        return created
    
    def validate_structure(self, ata: str, domain: str) -> Tuple[bool, List[str]]:
        """Validate canonical ATA structure."""
        canonical_path = self.canonical_base / domain / "ata" / ata
        
        if not canonical_path.exists():
            return False, [f"Canonical path does not exist: {canonical_path}"]
        
        errors = []
        
        # Check required files
        required_files = ["README.md", "CONVENTIONS.md"]
        for filename in required_files:
            if not (canonical_path / filename).exists():
                errors.append(f"Missing required file: {filename}")
        
        # Check required directories
        for subdir in self.STANDARD_STRUCTURE:
            dir_path = canonical_path / subdir
            if not dir_path.exists():
                errors.append(f"Missing required directory: {subdir}")
        
        # Check cross_references.yaml
        xref_path = canonical_path / "governance" / "cross_references.yaml"
        if not xref_path.exists():
            errors.append("Missing governance/cross_references.yaml")
        
        return len(errors) == 0, errors
    
    def list_canonical_atas(self) -> List[Tuple[str, str, Path]]:
        """List all existing canonical ATA directories."""
        canonical_atas = []
        
        if not self.canonical_base.exists():
            return canonical_atas
        
        for domain_dir in self.canonical_base.iterdir():
            if not domain_dir.is_dir():
                continue
            
            ata_base = domain_dir / "ata"
            if not ata_base.exists():
                continue
            
            for ata_dir in ata_base.iterdir():
                if ata_dir.is_dir() and ata_dir.name.startswith("ATA-"):
                    canonical_atas.append((ata_dir.name, domain_dir.name, ata_dir))
        
        return sorted(canonical_atas)


def main():
    parser = argparse.ArgumentParser(
        description="Standardize ATA canonical structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create canonical structure for ATA-42 in IIS domain
  python scripts/standardize_ata_structure.py --atas ATA-42 --domain IIS --create

  # Validate existing canonical structure
  python scripts/standardize_ata_structure.py --atas ATA-42 --domain IIS --validate

  # List all canonical ATAs
  python scripts/standardize_ata_structure.py --list

  # Create structure and symlinks (dry run)
  python scripts/standardize_ata_structure.py --atas ATA-42 --create --symlinks --dry-run

  # Process multiple ATAs
  python scripts/standardize_ata_structure.py --atas ATA-42,ATA-45 --include-shared --verbose
        """
    )
    
    parser.add_argument(
        "--atas",
        help="Comma-separated list of ATA chapters (e.g., ATA-42,ATA-45)"
    )
    parser.add_argument(
        "--domain",
        help="Override canonical domain (uses registry by default)"
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create canonical structure"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate canonical structure"
    )
    parser.add_argument(
        "--symlinks",
        action="store_true",
        help="Create symlinks from product trees"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List existing canonical ATAs"
    )
    parser.add_argument(
        "--include-shared",
        action="store_true",
        help="Process shared domains too"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Dry run - don't make changes"
    )
    
    args = parser.parse_args()
    
    # Get repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    manager = ATAStructureManager(repo_root, verbose=args.verbose, dry_run=args.dry_run)
    
    # List mode
    if args.list:
        canonical_atas = manager.list_canonical_atas()
        if not canonical_atas:
            print("No canonical ATA directories found.")
            return 0
        
        print(f"\nFound {len(canonical_atas)} canonical ATA directories:\n")
        print(f"{'ATA':<10} {'Domain':<10} {'Path'}")
        print("-" * 80)
        for ata, domain, path in canonical_atas:
            rel_path = path.relative_to(repo_root)
            print(f"{ata:<10} {domain:<10} {rel_path}")
        return 0
    
    # Require --atas for other operations
    if not args.atas and not args.list:
        parser.error("--atas is required (or use --list)")
    
    # Parse ATAs
    atas = [a.strip() for a in args.atas.split(",")]
    
    # Process each ATA
    success_count = 0
    error_count = 0
    
    for ata in atas:
        print(f"\n{'='*80}")
        print(f"Processing {ata}")
        print(f"{'='*80}\n")
        
        # Get ATA info
        ata_info = manager.get_ata_info(ata)
        if not ata_info:
            manager._log(f"ATA {ata} not found in registry", "ERROR")
            error_count += 1
            continue
        
        # Determine domains to process
        domains_to_process = []
        if args.domain:
            domains_to_process.append(args.domain)
        else:
            domains_to_process.append(ata_info["canonical_domain"])
            if args.include_shared:
                domains_to_process.extend(ata_info.get("shared_domains", []))
        
        # Process each domain
        for domain in domains_to_process:
            print(f"\nDomain: {domain}")
            print("-" * 40)
            
            try:
                # Create structure
                if args.create:
                    canonical_path = manager.create_canonical_structure(ata, domain)
                
                # Validate
                if args.validate or args.create:
                    valid, errors = manager.validate_structure(ata, domain)
                    if valid:
                        manager._log(f"Structure validation passed", "SUCCESS")
                    else:
                        manager._log(f"Structure validation failed:", "ERROR")
                        for error in errors:
                            manager._log(f"  - {error}", "ERROR")
                        error_count += 1
                        continue
                
                # Create symlinks
                if args.symlinks:
                    created = manager.create_symlinks(ata, domain)
                    if created > 0:
                        manager._log(f"Created {created} symlinks", "SUCCESS")
                
                success_count += 1
                
            except Exception as e:
                manager._log(f"Error processing {ata}/{domain}: {e}", "ERROR")
                error_count += 1
                if args.verbose:
                    import traceback
                    traceback.print_exc()
    
    # Summary
    print(f"\n{'='*80}")
    print(f"Summary")
    print(f"{'='*80}\n")
    print(f"✅ Successful: {success_count}")
    print(f"❌ Errors: {error_count}")
    
    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
