#!/usr/bin/env python3
"""
Compliance Matrix Mapper

Renders effective compliance matrix for ATA chapters.

Usage:
    python scripts/map_compliance.py --help
    python scripts/map_compliance.py --ata ATA-42
    python scripts/map_compliance.py --all
    python scripts/map_compliance.py --ata ATA-42 --format markdown
"""

import argparse
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional
import json


class ComplianceMapper:
    """Maps compliance requirements to ATA chapters."""
    
    def __init__(self, repo_root: Path, verbose: bool = False):
        self.repo_root = repo_root
        self.verbose = verbose
        self.resources_dir = repo_root / "8-RESOURCES" / "ATA_CANONICAL"
        
        # Load compliance matrix
        self.matrix = self._load_matrix()
    
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
    
    def _load_matrix(self) -> Dict:
        """Load compliance matrix."""
        matrix_path = self.resources_dir / "COMPLIANCE_MATRIX.yaml"
        if not matrix_path.exists():
            self._log(f"Compliance matrix not found: {matrix_path}", "WARNING")
            return {"compliance_standards": [], "ata_compliance": []}
        
        with open(matrix_path, 'r') as f:
            return yaml.safe_load(f)
    
    def get_standard_info(self, standard_id: str) -> Optional[Dict]:
        """Get information about a compliance standard."""
        for standard in self.matrix.get("compliance_standards", []):
            if standard["id"] == standard_id:
                return standard
        return None
    
    def get_ata_compliance(self, ata: str) -> Optional[Dict]:
        """Get compliance requirements for an ATA."""
        for ata_comp in self.matrix.get("ata_compliance", []):
            if ata_comp["ata"] == ata:
                return ata_comp
        return None
    
    def render_markdown(self, ata: str) -> str:
        """Render compliance matrix as Markdown."""
        ata_comp = self.get_ata_compliance(ata)
        
        if not ata_comp:
            return f"# Compliance Matrix for {ata}\n\nNo specific compliance requirements defined in master matrix.\n"
        
        output = []
        output.append(f"# Compliance Matrix for {ata}")
        output.append("")
        output.append(f"**Title:** {ata_comp.get('title', 'N/A')}")
        
        if "dal" in ata_comp:
            output.append(f"**Design Assurance Level (DAL):** {ata_comp['dal']}")
        
        if "notes" in ata_comp:
            output.append(f"**Notes:** {ata_comp['notes']}")
        
        output.append("")
        output.append("## Applicable Standards")
        output.append("")
        
        standards = ata_comp.get("standards", [])
        if not standards:
            output.append("No standards specified.")
        else:
            output.append("| Standard | Title | Authority | Applies To |")
            output.append("|----------|-------|-----------|------------|")
            
            for std_id in standards:
                std_info = self.get_standard_info(std_id)
                if std_info:
                    title = std_info.get("title", "N/A")
                    authority = std_info.get("authority", "N/A")
                    applies_to = ", ".join(std_info.get("applies_to", []))
                    output.append(f"| {std_id} | {title} | {authority} | {applies_to} |")
                else:
                    output.append(f"| {std_id} | *Not found in matrix* | - | - |")
        
        output.append("")
        output.append("## Standard Details")
        output.append("")
        
        for std_id in standards:
            std_info = self.get_standard_info(std_id)
            if not std_info:
                continue
            
            output.append(f"### {std_id}: {std_info.get('title', 'N/A')}")
            output.append("")
            output.append(f"**Authority:** {std_info.get('authority', 'N/A')}")
            output.append("")
            
            if "applies_to" in std_info:
                output.append(f"**Applies to:** {', '.join(std_info['applies_to'])}")
                output.append("")
            
            if "dal_levels" in std_info:
                output.append(f"**DAL Levels:** {', '.join(std_info['dal_levels'])}")
                output.append("")
            
            if "methods" in std_info:
                output.append(f"**Methods:** {', '.join(std_info['methods'])}")
                output.append("")
        
        return "\n".join(output)
    
    def render_json(self, ata: str) -> str:
        """Render compliance matrix as JSON."""
        ata_comp = self.get_ata_compliance(ata)
        
        if not ata_comp:
            return json.dumps({"ata": ata, "error": "No compliance requirements found"}, indent=2)
        
        # Build enhanced compliance data
        result = {
            "ata": ata,
            "title": ata_comp.get("title", "N/A"),
            "dal": ata_comp.get("dal"),
            "notes": ata_comp.get("notes"),
            "standards": []
        }
        
        for std_id in ata_comp.get("standards", []):
            std_info = self.get_standard_info(std_id)
            if std_info:
                result["standards"].append({
                    "id": std_id,
                    "title": std_info.get("title", "N/A"),
                    "authority": std_info.get("authority", "N/A"),
                    "applies_to": std_info.get("applies_to", []),
                    "dal_levels": std_info.get("dal_levels", []),
                    "methods": std_info.get("methods", [])
                })
            else:
                result["standards"].append({
                    "id": std_id,
                    "error": "Standard not found in matrix"
                })
        
        return json.dumps(result, indent=2)
    
    def render_text(self, ata: str) -> str:
        """Render compliance matrix as plain text."""
        ata_comp = self.get_ata_compliance(ata)
        
        if not ata_comp:
            return f"Compliance Matrix for {ata}\n\nNo specific compliance requirements defined in master matrix.\n"
        
        output = []
        output.append("=" * 80)
        output.append(f"Compliance Matrix for {ata}")
        output.append("=" * 80)
        output.append("")
        output.append(f"Title: {ata_comp.get('title', 'N/A')}")
        
        if "dal" in ata_comp:
            output.append(f"Design Assurance Level (DAL): {ata_comp['dal']}")
        
        if "notes" in ata_comp:
            output.append(f"Notes: {ata_comp['notes']}")
        
        output.append("")
        output.append("-" * 80)
        output.append("Applicable Standards")
        output.append("-" * 80)
        output.append("")
        
        standards = ata_comp.get("standards", [])
        if not standards:
            output.append("No standards specified.")
        else:
            for std_id in standards:
                std_info = self.get_standard_info(std_id)
                if std_info:
                    output.append(f"• {std_id}")
                    output.append(f"  {std_info.get('title', 'N/A')}")
                    output.append(f"  Authority: {std_info.get('authority', 'N/A')}")
                    if "applies_to" in std_info:
                        output.append(f"  Applies to: {', '.join(std_info['applies_to'])}")
                    if "dal_levels" in std_info:
                        output.append(f"  DAL Levels: {', '.join(std_info['dal_levels'])}")
                    output.append("")
                else:
                    output.append(f"• {std_id} (not found in matrix)")
                    output.append("")
        
        return "\n".join(output)
    
    def list_all_atas(self) -> List[str]:
        """List all ATAs with compliance requirements."""
        atas = []
        for ata_comp in self.matrix.get("ata_compliance", []):
            atas.append(ata_comp["ata"])
        return sorted(atas)


def main():
    parser = argparse.ArgumentParser(
        description="Map compliance requirements for ATA chapters",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Show compliance for ATA-42 (default: text format)
  python scripts/map_compliance.py --ata ATA-42

  # Show compliance for ATA-42 as Markdown
  python scripts/map_compliance.py --ata ATA-42 --format markdown

  # Show compliance for ATA-42 as JSON
  python scripts/map_compliance.py --ata ATA-42 --format json

  # List all ATAs with compliance requirements
  python scripts/map_compliance.py --list

  # Show all ATAs (as text)
  python scripts/map_compliance.py --all
        """
    )
    
    parser.add_argument(
        "--ata",
        help="ATA chapter (e.g., ATA-42)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show compliance for all ATAs"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all ATAs with compliance requirements"
    )
    parser.add_argument(
        "--format",
        choices=["text", "markdown", "json"],
        default="text",
        help="Output format (default: text)"
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
    
    mapper = ComplianceMapper(repo_root, verbose=args.verbose)
    
    if args.list:
        atas = mapper.list_all_atas()
        print("\nATAs with Compliance Requirements:")
        print("=" * 40)
        for ata in atas:
            ata_comp = mapper.get_ata_compliance(ata)
            title = ata_comp.get("title", "N/A") if ata_comp else "N/A"
            print(f"  {ata:<10} {title}")
        print()
        return 0
    
    if args.all:
        atas = mapper.list_all_atas()
        for i, ata in enumerate(atas):
            if i > 0:
                print("\n" + "=" * 80 + "\n")
            
            if args.format == "markdown":
                print(mapper.render_markdown(ata))
            elif args.format == "json":
                print(mapper.render_json(ata))
            else:
                print(mapper.render_text(ata))
        
        return 0
    
    if args.ata:
        if args.format == "markdown":
            print(mapper.render_markdown(args.ata))
        elif args.format == "json":
            print(mapper.render_json(args.ata))
        else:
            print(mapper.render_text(args.ata))
        
        return 0
    
    parser.error("Either --ata, --all, or --list is required")


if __name__ == "__main__":
    sys.exit(main())
