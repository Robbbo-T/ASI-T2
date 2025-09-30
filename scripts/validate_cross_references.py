#!/usr/bin/env python3
"""
Cross-Reference Validation Script

Validates cross_references.yaml files in canonical ATA folders against the master schema.

Usage:
    python scripts/validate_cross_references.py --help
    python scripts/validate_cross_references.py --ata ATA-42 --domain IIS
    python scripts/validate_cross_references.py --all
"""

import argparse
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re


class CrossReferenceValidator:
    """Validates ATA cross-reference files."""
    
    def __init__(self, repo_root: Path, verbose: bool = False):
        self.repo_root = repo_root
        self.verbose = verbose
        self.canonical_base = repo_root / "2-DOMAINS-LEVELS"
        self.resources_dir = repo_root / "8-RESOURCES" / "ATA_CANONICAL"
        
        # Load schema and registry
        self.schema = self._load_schema()
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
    
    def _load_schema(self) -> Dict:
        """Load cross-reference schema."""
        schema_path = self.resources_dir / "XREF_MASTER.yaml"
        if not schema_path.exists():
            self._log(f"Schema not found: {schema_path}", "WARNING")
            return {}
        
        with open(schema_path, 'r') as f:
            return yaml.safe_load(f)
    
    def _load_registry(self) -> Dict:
        """Load ATA registry."""
        registry_path = self.resources_dir / "ATA_REGISTRY.yaml"
        if not registry_path.exists():
            self._log(f"Registry not found: {registry_path}", "WARNING")
            return {"ata_chapters": [], "domains": []}
        
        with open(registry_path, 'r') as f:
            return yaml.safe_load(f)
    
    def _is_valid_ata(self, ata: str) -> bool:
        """Check if ATA chapter exists in registry."""
        if not re.match(r'^ATA-\d{2}$', ata):
            return False
        
        for chapter in self.registry.get("ata_chapters", []):
            if chapter["ata"] == ata:
                return True
        return False
    
    def _is_valid_domain(self, domain: str) -> bool:
        """Check if domain exists in registry."""
        if not re.match(r'^[A-Z]{3}$', domain):
            return False
        
        for d in self.registry.get("domains", []):
            if d["code"] == domain:
                return True
        return False
    
    def _validate_xref_item(self, xref: Dict, file_path: Path) -> List[str]:
        """Validate a single cross-reference item."""
        errors = []
        
        # Required fields
        required = ["from", "to", "type", "reason"]
        for field in required:
            if field not in xref:
                errors.append(f"Missing required field: {field}")
        
        if errors:  # Don't continue if required fields missing
            return errors
        
        # Validate 'from' field
        from_ref = xref.get("from", {})
        if not isinstance(from_ref, dict):
            errors.append("'from' must be an object")
        else:
            if "ata" not in from_ref:
                errors.append("'from' missing 'ata' field")
            elif not self._is_valid_ata(from_ref["ata"]):
                errors.append(f"Invalid ATA in 'from': {from_ref['ata']}")
            
            if "domain" not in from_ref:
                errors.append("'from' missing 'domain' field")
            elif not self._is_valid_domain(from_ref["domain"]):
                errors.append(f"Invalid domain in 'from': {from_ref['domain']}")
        
        # Validate 'to' field
        to_ref = xref.get("to", {})
        if not isinstance(to_ref, dict):
            errors.append("'to' must be an object")
        else:
            if "domain" not in to_ref:
                errors.append("'to' missing 'domain' field")
            elif not self._is_valid_domain(to_ref["domain"]):
                errors.append(f"Invalid domain in 'to': {to_ref['domain']}")
            
            # 'ata' is optional in 'to'
            if "ata" in to_ref and not self._is_valid_ata(to_ref["ata"]):
                errors.append(f"Invalid ATA in 'to': {to_ref['ata']}")
        
        # Validate 'type'
        valid_types = ["overlay", "variant", "dependency", "reference"]
        xref_type = xref.get("type")
        if xref_type not in valid_types:
            errors.append(f"Invalid type '{xref_type}', must be one of: {', '.join(valid_types)}")
        
        # Validate 'reason'
        reason = xref.get("reason", "")
        if not isinstance(reason, str):
            errors.append("'reason' must be a string")
        elif len(reason) < 10:
            errors.append("'reason' must be at least 10 characters")
        elif len(reason) > 500:
            errors.append("'reason' must be at most 500 characters")
        
        # Validate optional 'artifacts'
        artifacts = xref.get("artifacts", [])
        if artifacts is not None:
            if not isinstance(artifacts, list):
                errors.append("'artifacts' must be an array")
            else:
                for i, artifact in enumerate(artifacts):
                    if not isinstance(artifact, str):
                        errors.append(f"artifacts[{i}] must be a string")
                    else:
                        # Check if artifact path exists (relative to repo root)
                        artifact_path = self.repo_root / artifact
                        if not artifact_path.exists():
                            errors.append(f"Referenced artifact does not exist: {artifact}")
        
        # Validate optional 'status'
        if "status" in xref:
            valid_statuses = ["active", "deprecated", "proposed"]
            if xref["status"] not in valid_statuses:
                errors.append(f"Invalid status '{xref['status']}', must be one of: {', '.join(valid_statuses)}")
        
        return errors
    
    def validate_file(self, file_path: Path) -> Tuple[bool, List[str]]:
        """Validate a cross_references.yaml file."""
        if not file_path.exists():
            return False, [f"File not found: {file_path}"]
        
        errors = []
        
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return False, [f"YAML parsing error: {e}"]
        except Exception as e:
            return False, [f"Error reading file: {e}"]
        
        if data is None:
            data = {}
        
        # Check root structure
        if not isinstance(data, dict):
            errors.append("Root must be an object")
            return False, errors
        
        if "xrefs" not in data:
            errors.append("Missing 'xrefs' field")
            return False, errors
        
        xrefs = data["xrefs"]
        if not isinstance(xrefs, list):
            errors.append("'xrefs' must be an array")
            return False, errors
        
        # Validate each cross-reference
        for i, xref in enumerate(xrefs):
            if not isinstance(xref, dict):
                errors.append(f"xrefs[{i}] must be an object")
                continue
            
            xref_errors = self._validate_xref_item(xref, file_path)
            for error in xref_errors:
                errors.append(f"xrefs[{i}]: {error}")
        
        return len(errors) == 0, errors
    
    def validate_canonical_ata(self, ata: str, domain: str) -> Tuple[bool, List[str]]:
        """Validate cross-references for a canonical ATA."""
        canonical_path = self.canonical_base / domain / "ata" / ata
        xref_file = canonical_path / "governance" / "cross_references.yaml"
        
        if not xref_file.exists():
            return False, [f"Cross-references file not found: {xref_file}"]
        
        return self.validate_file(xref_file)
    
    def find_all_xref_files(self) -> List[Path]:
        """Find all cross_references.yaml files in canonical ATAs."""
        xref_files = []
        
        if not self.canonical_base.exists():
            return xref_files
        
        pattern = "**/governance/cross_references.yaml"
        for xref_file in self.canonical_base.glob(pattern):
            if xref_file.is_file():
                xref_files.append(xref_file)
        
        return sorted(xref_files)
    
    def validate_all(self) -> Tuple[int, int]:
        """Validate all cross-reference files."""
        xref_files = self.find_all_xref_files()
        
        if not xref_files:
            self._log("No cross-reference files found")
            return 0, 0
        
        self._log(f"Found {len(xref_files)} cross-reference files to validate\n")
        
        passed = 0
        failed = 0
        
        for xref_file in xref_files:
            rel_path = xref_file.relative_to(self.repo_root)
            print(f"{'='*80}")
            print(f"Validating: {rel_path}")
            print(f"{'='*80}\n")
            
            valid, errors = self.validate_file(xref_file)
            
            if valid:
                self._log("Validation passed", "SUCCESS")
                passed += 1
            else:
                self._log(f"Validation failed with {len(errors)} error(s):", "ERROR")
                for error in errors:
                    self._log(f"  - {error}", "ERROR")
                failed += 1
            
            print()
        
        return passed, failed


def main():
    parser = argparse.ArgumentParser(
        description="Validate ATA cross-reference files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate specific ATA
  python scripts/validate_cross_references.py --ata ATA-42 --domain IIS

  # Validate all cross-reference files
  python scripts/validate_cross_references.py --all

  # Verbose output
  python scripts/validate_cross_references.py --all --verbose
        """
    )
    
    parser.add_argument(
        "--ata",
        help="ATA chapter (e.g., ATA-42)"
    )
    parser.add_argument(
        "--domain",
        help="Domain code (e.g., IIS)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all cross-reference files"
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
    
    validator = CrossReferenceValidator(repo_root, verbose=args.verbose)
    
    if args.all:
        passed, failed = validator.validate_all()
        
        print(f"{'='*80}")
        print(f"Summary")
        print(f"{'='*80}\n")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        
        return 0 if failed == 0 else 1
    
    elif args.ata and args.domain:
        print(f"{'='*80}")
        print(f"Validating: {args.domain}/{args.ata}")
        print(f"{'='*80}\n")
        
        valid, errors = validator.validate_canonical_ata(args.ata, args.domain)
        
        if valid:
            validator._log("Validation passed", "SUCCESS")
            return 0
        else:
            validator._log(f"Validation failed with {len(errors)} error(s):", "ERROR")
            for error in errors:
                validator._log(f"  - {error}", "ERROR")
            return 1
    
    else:
        parser.error("Either --all or both --ata and --domain are required")


if __name__ == "__main__":
    sys.exit(main())
