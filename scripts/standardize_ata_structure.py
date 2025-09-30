#!/usr/bin/env python3
"""
Standardize ATA-XX Directory Structure Script

This script updates all ATA-XX directories to follow the standardized format:
- Creates the standard directory structure
- Preserves existing reusable artifacts (S1000D, os/, config/, etc.)
- Creates required seed files (README.md, CONVENTIONS.md, manifests)
- Removes non-standard directories/files (except those in preserve list)

Usage:
    python scripts/standardize_ata_structure.py [--dry-run] [--ata-dir PATH]
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import date
import subprocess

# Standard directory structure from the problem statement
STANDARD_STRUCTURE = {
    'governance': ['change_control', 'approvals', 'baselines', 'risk_management', 'audits'],
    'os': {
        'S1000D': {
            'dmodule': [],
            'dmrl': [],
            'brex': [],
            'schemas': {'6.0': []},
            'publications': ['assets']
        },
        'descriptive': [],
        'design': ['requirements', 'architecture', 'interfaces', 'models'],
        'installation': [],
        'configuration': ['static', 'security_policies', 'manifests'],
        'testing': ['test_cases', 'test_data', 'test_results', 'tools'],
        'compliance': [
            'DO-178C_evidence',
            'DO-330_evidence',
            'DO-297_evidence',
            'ARINC653_conformance',
            'ARP4754B_ARP4761A_safety'
        ],
        'safety': [],
        'security': [],
        'buses': ['afdx', 'a429', 'discretes', 'serial'],
        'maintenance': [],
        'tools': ['ci', 'scripts'],
        'references': []
    },
    'manufacturing': {
        'bom': ['ebom', 'mbom'],
        'process': ['plans', 'work_instructions', 'pfmea', 'control_plans'],
        'quality': ['as9102_fair', 'as9145_ppap', 'inspection_plans'],
        'tooling_fixtures': [],
        'provisioning': [],
        'test': ['ict', 'boundary_scan', 'eol'],
        'packaging': ['labels', 'export_compliance', 'manifests']
    },
    'sustainment': {
        'service_mro': [],
        'spares_ipd': [],
        'returns_rma': [],
        'fracas': [],
        'reliability': [],
        'obsolescence': [],
        'as_maintained': [],
        'cas_security': [],
        'recycling_disposal': ['weee_rohs_reach', 'data_sanitization', 'manifests']
    },
    'assets': [],
    'scripts': [],
    'docs': []
}

# Directories/files to preserve during standardization
PRESERVE_PATTERNS = [
    'S1000D',           # S1000D data modules
    'dmodule',          # Data modules
    'dmrl',             # DMRL files
    'brex',             # BREX rules
    'schemas',          # Validation schemas
    'publications',     # Publications
    'figures',          # Figures/diagrams
    'descriptive',      # Descriptive docs
    'design',           # Design docs
    'installation',     # Installation docs
    'configuration',    # Configuration files
    'testing',          # Test artifacts
    'compliance',       # Compliance evidence
    'safety',           # Safety docs
    'security',         # Security docs
    'buses',            # Bus configuration
    'maintenance',      # Maintenance docs
    'references',       # Reference docs
    'os',               # Operating system directory
    'cert',             # Certification (to be moved to compliance)
    'verification',     # Verification (to be moved to compliance)
    'README.md',        # Will be regenerated
    'CONVENTIONS.md',   # Will be created
    'IMPLEMENTATION_SUMMARY.md',  # Keep if exists
    'schedule.xml',     # Legacy ARINC 653 schedule (keep in os/)
    # Domain-specific directories to preserve
    'architecture',     # Architecture docs
    'requirements',     # Requirements
    'software',         # Software artifacts
    'config',           # Configuration (variant)
    'icd',              # Interface Control Documents
    'partitions',       # Partition definitions
    'qox',              # Quality artifacts
    'sitl',             # Software In The Loop
    'scripts',          # Scripts (will be in standard structure too)
    'tools',            # Tools (will be moved)
    'contracts',        # Contract documents
    'io',               # I/O definitions
    'forms',            # Forms
    # ATA subdirectories (section-level)
    '20-',              # ATA-20 subsections
    '21-',              # ATA-21 subsections
    '22-',              # ATA-22 subsections
    '23-',              # ATA-23 subsections
    '24-',              # ATA-24 subsections
    '25-',              # ATA-25 subsections
    '26-',              # ATA-26 subsections
    '27-',              # ATA-27 subsections
    '28-',              # ATA-28 subsections
    '29-',              # ATA-29 subsections
    '30-',              # ATA-30 subsections
    '31-',              # ATA-31 subsections
    '32-',              # ATA-32 subsections
    '33-',              # ATA-33 subsections
    '34-',              # ATA-34 subsections
    '35-',              # ATA-35 subsections
    '36-',              # ATA-36 subsections
    '37-',              # ATA-37 subsections
    '38-',              # ATA-38 subsections
    '39-',              # ATA-39 subsections
    '40-',              # ATA-40 subsections
    '41-',              # ATA-41 subsections
    '42-',              # ATA-42 subsections
    '43-',              # ATA-43 subsections
    '44-',              # ATA-44 subsections
    '45-',              # ATA-45 subsections
    '46-',              # ATA-46 subsections
    '47-',              # ATA-47 subsections
    '48-',              # ATA-48 subsections
    '49-',              # ATA-49 subsections
    '50-',              # ATA-50 subsections
    '51-',              # ATA-51 subsections
    '52-',              # ATA-52 subsections
    '53-',              # ATA-53 subsections
    '54-',              # ATA-54 subsections
    '55-',              # ATA-55 subsections
    '56-',              # ATA-56 subsections
    '57-',              # ATA-57 subsections
    '70-',              # ATA-70 subsections
    '71-',              # ATA-71 subsections
    '72-',              # ATA-72 subsections
    '73-',              # ATA-73 subsections
    '74-',              # ATA-74 subsections
    '75-',              # ATA-75 subsections
    '76-',              # ATA-76 subsections
    '77-',              # ATA-77 subsections
    '78-',              # ATA-78 subsections
    '79-',              # ATA-79 subsections
    # File extensions to preserve
    '.xml',             # Keep XML files
    '.yaml',            # Keep YAML files
    '.yml',             # Keep YML files
    '.json',            # Keep JSON files
    '.xsd',             # Keep schema files
    '.conf',            # Keep configuration files
    '.md',              # Keep markdown files
    '.py',              # Keep Python files
]


def should_preserve(path: Path) -> bool:
    """Check if a file/directory should be preserved."""
    # Check if name matches preserve patterns
    name = path.name
    for pattern in PRESERVE_PATTERNS:
        if pattern.startswith('.'):
            # File extension pattern
            if name.endswith(pattern):
                return True
        else:
            # Directory/file name pattern
            if name == pattern or name.startswith(pattern):
                return True
    return False


def create_directory_structure(base_path: Path, structure: dict, dry_run: bool = False):
    """Recursively create directory structure with .keep files."""
    for name, children in structure.items():
        dir_path = base_path / name
        
        if dry_run:
            print(f"  [DRY-RUN] Would create directory: {dir_path}")
        else:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        if isinstance(children, list):
            # Create subdirectories
            for child in children:
                child_path = dir_path / child
                if dry_run:
                    print(f"  [DRY-RUN] Would create directory: {child_path}")
                else:
                    child_path.mkdir(parents=True, exist_ok=True)
                    keep_file = child_path / '.keep'
                    if not keep_file.exists():
                        keep_file.write_text('# This file preserves the directory structure in Git.\n')
        elif isinstance(children, dict):
            # Recursively create nested structure
            create_directory_structure(dir_path, children, dry_run)
        else:
            # Empty directory, create .keep file
            if not dry_run:
                keep_file = dir_path / '.keep'
                if not keep_file.exists():
                    keep_file.write_text('# This file preserves the directory structure in Git.\n')


def generate_readme(ata_dir: Path, ata_number: str) -> str:
    """Generate README.md content based on the standard template."""
    today = date.today().isoformat()
    
    # Try to infer domain from path
    domain = "DOMAIN"
    path_parts = str(ata_dir).split('/')
    if 'domains' in path_parts:
        domain_idx = path_parts.index('domains') + 1
        if domain_idx < len(path_parts):
            domain = path_parts[domain_idx]
    
    return f"""---
id: ATA-{ata_number}-INDEX
project: ASI-T2
artifact: ATA-{ata_number} System
classification: INTERNAL
version: 0.1.0
release_date: {today}
maintainer: IIS (Integrated Information Systems)
language_default: en-US
enterprise_code: IIS
canonical_hash: pending
ethics_guard: MAL-EEM
canonical_domain: {domain}
---

# ATA-{ata_number} System Documentation

> **[CANONICAL]** `ATA-{ata_number}` folder owned by `{domain}` within **ASI-T2**. It is the **single source of truth** for this ATA chapter. Product trees (e.g., `PRODUCTS/AMPEL360/...`) must reference this location via **symlinks**.

**Legend**

* **[CANONICAL]** → Primary ownership (this folder)
* **[SHARED]** → Co-owned via overlays/variants, documented in `governance/cross_references.yaml`

**Ownership**

* `canonical_domain: {domain}`
* `shared_domains: []` (if any, see registry `8-RESOURCES/ATA_CANONICAL/ATA_REGISTRY.yaml`)

---

## 1) Directory Map (Standard)

```
README.md
CONVENTIONS.md

governance/
  change_control/
  baselines/
  risk_management/
  cross_references.yaml
  audits/

os/
  S1000D/
  design/
    architecture/
    icd/
    diagrams/
  configuration/
    manifests/
    schedule.xml
  testing/
  compliance/
    certification/
    verification/

manufacturing/
  bom/
  process/
  quality/
  tooling/
  test/
  packaging/
    manifests/

sustainment/
  service_mro/
  spares/
  reliability/
  obsolescence/
  cas_security/
  recycling_disposal/
    weee_rohs_reach/
    data_sanitization/
    manifests/

assets/
scripts/
docs/
```

---

## 2) Purpose & Scope per Area

**governance/**

* **change_control/**: PR/merge policy, versioning, semantic commits, UTCS anchors.
* **baselines/**: Formal baselines (BL-0, BL-1…), signed hashes (QS), release notes.
* **risk_management/**: Safety/cyber methods (e.g., ARP4761 FHA/FTA/FMEA, STRIDE/DREAD).
* **cross_references.yaml**: Links to shared artifacts in other domains or products.
* **audits/**: Internal/external audit reports, NCRs, corrective actions.

**os/**

* **S1000D/**: Technical documentation (data modules, DMRL, BREX, schemas, publications).
* **design/**: Requirements (HLR/LLR), architecture diagrams, ICD specs.
* **configuration/**: Static config files, security policies, manifests, ARINC 653 schedules.
* **testing/**: Test cases, data, results, tools (integration & unit tests).
* **compliance/**: DO-178C, DO-254, DO-297, ARINC653, ARP4754B evidence and verification.

**manufacturing/**

* **bom/**: Engineering BOM (EBOM), Manufacturing BOM (MBOM).
* **process/**: Work instructions, PFMEA, control plans.
* **quality/**: AS9102 FAIR, AS9145 PPAP, inspection plans.
* **tooling/**: Fixtures, jigs, test equipment documentation.
* **test/**: ICT, boundary scan, end-of-line test procedures.
* **packaging/**: Labels, export compliance, packaging manifests.

**sustainment/**

* **service_mro/**: Maintenance, repair, overhaul procedures.
* **spares/**: Illustrated Parts Data (IPD), spares management.
* **reliability/**: MTBF, failure tracking, reliability growth.
* **obsolescence/**: Component lifecycle, DMSMS tracking.
* **cas_security/**: Continued Airworthiness & Security monitoring.
* **recycling_disposal/**: WEEE/RoHS/REACH compliance, data sanitization, end-of-life manifests.

---

## 3) Standards Compliance

This documentation package complies with:

* **S1000D**: Technical publication structure (data modules, DMRL, BREX)
* **DO-178C**: Software considerations in airborne systems
* **DO-254**: Hardware considerations in airborne systems
* **DO-297**: Integrated Modular Avionics (IMA) development
* **ARP4754B/ARP4761A**: System development and safety assessment
* **AS9100/AS9145**: Quality management and PPAP
* **WEEE/RoHS/REACH**: Environmental compliance

---

## 4) Conventions

See [CONVENTIONS.md](./CONVENTIONS.md) for:

* Naming conventions (files, branches, commits)
* Version control & branching strategy
* Front-matter YAML requirements
* Hashing, signing, and manifest procedures
* Documentation standards (Markdown, S1000D)

---

## 5) Getting Started

1. **Review** [CONVENTIONS.md](./CONVENTIONS.md) for standards and workflows
2. **Navigate** to area of interest: `os/`, `manufacturing/`, `sustainment/`, `governance/`
3. **Check** `governance/cross_references.yaml` for dependencies on other ATAs or domains
4. **Use scripts** in `scripts/` for validation, manifest generation, or automation
5. **Reference** the canonical registry: `8-RESOURCES/ATA_CANONICAL/ATA_REGISTRY.yaml`

---

## 6) Contact & Ownership

* **Canonical Domain**: {domain}
* **Maintainer**: IIS (Integrated Information Systems)
* **Enterprise Code**: IIS
* **Ethics Guard**: MAL-EEM

For cross-domain collaboration or shared ownership queries, see `governance/cross_references.yaml`.

---

## 7) Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | {today} | Initial standardized structure with canonical ownership |
"""


def generate_conventions() -> str:
    """Generate CONVENTIONS.md content."""
    today = date.today().isoformat()
    
    return f"""---
id: ATA-XX-CONVENTIONS
project: ASI-T2
artifact: ATA-XX Documentation Conventions
classification: INTERNAL
version: 0.1.0
release_date: {today}
maintainer: IIS (Integrated Information Systems)
language_default: en-US
enterprise_code: IIS
canonical_hash: pending
ethics_guard: MAL-EEM
---

# ATA-XX Documentation Conventions

## Overview

This document defines the conventions used throughout the ATA-XX documentation structure, including naming conventions, version control practices, front-matter YAML structure, and hashing/signing procedures.

## File Naming Conventions

### General Files
- Use lowercase with underscores (snake_case)
- Be descriptive but concise
- Include version or date when appropriate
- Examples: `system_requirements.yaml`, `test_report_{today.replace('-', '')}.md`

### S1000D Files
- Follow S1000D naming conventions for DMs and ICNs
- Use the format `DMC-[ModelIdentCode]-[SystemDiffCode]-[SystemCode]-[SubSystemCode]-[SubSubSystemCode]-[AssyCode]-[DisassyCode]-[DisassyCodeVariant]-[InfoCode]-[InfoCodeVariant]-[ItemLocationCode].xml`

### Configuration Files
- Use `.yaml` extension for configuration files
- Use `.json` for schema definitions

### Test Files
- Prefix test cases with `tc_`
- Prefix test data with `td_`

## Version Control

### Branching Strategy
- `main`: Protected branch for released versions
- `develop`: Integration branch for ongoing work
- `feature/*`: Feature branches for new development
- `hotfix/*`: Emergency fixes

### Commit Messages
- Use the imperative mood
- Include issue number when applicable
- Format: `type(scope): description`

### Tagging
- Use semantic versioning (SemVer)
- Format: `v[MAJOR].[MINOR].[PATCH]`

## Front-Matter YAML

### Required Fields
All documentation files must include YAML front-matter with required fields:

```yaml
---
id: [unique identifier]
project: ASI-T2
artifact: [artifact name]
classification: [classification level]
version: [version number]
release_date: [YYYY-MM-DD]
maintainer: [maintainer name]
language_default: [language code]
enterprise_code: [enterprise code]
canonical_hash: [hash value]
ethics_guard: MAL-EEM
---
```

## Hashing and Signing

### File Hashing
- Use SHA-256 for all file hashes
- Store hashes in manifest files
- Update hashes when files change

### Manifest Files
- Use YAML format for manifest files
- Include file paths, hashes, and metadata

## Quality Assurance

### Validation
- Use schema validation for YAML and JSON files
- Use linting tools for Markdown files
- Use XML validation for S1000D files

### Reviews
- All documentation must be reviewed before release
- Use pull requests for changes
- Track review status in project management tools

## Security Considerations

### Access Control
- Restrict access to sensitive information
- Use role-based access control
- Audit access logs regularly

### Ethics Guard
- Apply MAL-EEM ethics guard to all AI-generated content
- Review AI-generated content for accuracy and appropriateness
"""


def move_legacy_content(ata_dir: Path, dry_run: bool = False):
    """Move legacy content to appropriate standard locations."""
    moves = []
    
    # Move cert/ to os/compliance/
    cert_dir = ata_dir / 'cert'
    if cert_dir.exists() and cert_dir.is_dir():
        target = ata_dir / 'os' / 'compliance' / 'certification'
        moves.append((cert_dir, target))
    
    # Move verification/ to os/compliance/
    verification_dir = ata_dir / 'verification'
    if verification_dir.exists() and verification_dir.is_dir():
        target = ata_dir / 'os' / 'compliance' / 'verification'
        moves.append((verification_dir, target))
    
    # Move tools/ to os/tools/ if it doesn't exist there already
    tools_dir = ata_dir / 'tools'
    if tools_dir.exists() and tools_dir.is_dir() and not (ata_dir / 'os' / 'tools').exists():
        target = ata_dir / 'os' / 'tools'
        moves.append((tools_dir, target))
    
    # Execute moves
    for src, dst in moves:
        if dry_run:
            print(f"  [DRY-RUN] Would move {src} -> {dst}")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists():
                shutil.move(str(src), str(dst))
                print(f"  Moved {src.name} -> {dst}")


def clean_non_standard_items(ata_dir: Path, dry_run: bool = False):
    """Remove non-standard directories and files (except preserved ones)."""
    removed = []
    
    # Check all items in ATA directory
    for item in ata_dir.iterdir():
        if item.name in ['.git', '.gitignore']:
            continue
        
        # Check if item should be preserved
        if should_preserve(item):
            continue
        
        # Check if item is in standard structure
        if item.name in STANDARD_STRUCTURE:
            continue
        
        # Not preserved and not standard - mark for removal
        if dry_run:
            print(f"  [DRY-RUN] Would remove: {item}")
        else:
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
            removed.append(item.name)
            print(f"  Removed: {item.name}")
    
    return removed


def standardize_ata_directory(ata_dir: Path, dry_run: bool = False):
    """Standardize a single ATA directory."""
    ata_number = ata_dir.name.replace('ATA-', '')
    print(f"\n{'='*80}")
    print(f"Standardizing: {ata_dir}")
    print(f"{'='*80}")
    
    # 1. Create standard directory structure
    print("\n1. Creating standard directory structure...")
    create_directory_structure(ata_dir, STANDARD_STRUCTURE, dry_run)
    
    # 2. Move legacy content to appropriate locations
    print("\n2. Moving legacy content to standard locations...")
    move_legacy_content(ata_dir, dry_run)
    
    # 3. Generate/update README.md
    print("\n3. Generating README.md...")
    readme_path = ata_dir / 'README.md'
    if dry_run:
        print(f"  [DRY-RUN] Would create/update: {readme_path}")
    else:
        readme_content = generate_readme(ata_dir, ata_number)
        readme_path.write_text(readme_content)
        print(f"  Created: README.md")
    
    # 4. Create CONVENTIONS.md if it doesn't exist
    print("\n4. Creating CONVENTIONS.md...")
    conventions_path = ata_dir / 'CONVENTIONS.md'
    if not conventions_path.exists() or dry_run:
        if dry_run:
            print(f"  [DRY-RUN] Would create: {conventions_path}")
        else:
            conventions_content = generate_conventions()
            conventions_path.write_text(conventions_content)
            print(f"  Created: CONVENTIONS.md")
    
    # 5. Create manifest files
    print("\n5. Creating manifest files...")
    manifest_dirs = [
        ata_dir / 'os' / 'configuration' / 'manifests',
        ata_dir / 'manufacturing' / 'packaging' / 'manifests',
        ata_dir / 'sustainment' / 'recycling_disposal' / 'manifests'
    ]
    
    for manifest_dir in manifest_dirs:
        if dry_run:
            print(f"  [DRY-RUN] Would create manifest in: {manifest_dir}")
        else:
            manifest_dir.mkdir(parents=True, exist_ok=True)
            manifest_file = manifest_dir / 'manifest.yaml'
            if not manifest_file.exists():
                manifest_file.write_text(f"""---
id: ATA-{ata_number}-MANIFEST
project: ASI-T2
artifact: ATA-{ata_number} Manifest
classification: INTERNAL
version: 0.1.0
release_date: {date.today().isoformat()}
maintainer: IIS (Integrated Information Systems)
language_default: en-US
enterprise_code: IIS
canonical_hash: pending
ethics_guard: MAL-EEM
---

# Manifest file for ATA-{ata_number}
# This file tracks configuration items and their hashes
files: []
""")
                print(f"  Created: {manifest_file.relative_to(ata_dir)}")
    
    # 5b. Create governance/cross_references.yaml
    print("\n5b. Creating governance cross-references file...")
    cross_ref_file = ata_dir / 'governance' / 'cross_references.yaml'
    if dry_run:
        print(f"  [DRY-RUN] Would create: {cross_ref_file}")
    else:
        cross_ref_file.parent.mkdir(parents=True, exist_ok=True)
        if not cross_ref_file.exists():
            cross_ref_file.write_text(f"""---
# Cross-References for ATA-{ata_number}
# Lists dependencies on other ATAs, domains, or external artifacts

shared_with_domains: []
  # Example:
  # - domain: PPP
  #   reason: "Shared propulsion integration specs"
  #   artifacts:
  #     - os/design/icd/ATA{ata_number}_to_ATA70.yaml

depends_on_atas: []
  # Example:
  # - ata: ATA-22
  #   reason: "Flight control interface"
  #   artifacts:
  #     - os/design/icd/autoflight_interface.yaml

referenced_by_products: []
  # Example:
  # - product: AMPEL360/BWB-Q100
  #   symlink: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/{domain}/ata/ATA-{ata_number}
  #   notes: "Primary product using this ATA"

external_references: []
  # Example:
  # - type: standard
  #   reference: "DO-297 Section 4.2"
  #   description: "IMA responsibility matrix"
""")
            print(f"  Created: governance/cross_references.yaml")
    
    # 6. Clean non-standard items (careful!)
    print("\n6. Cleaning non-standard items...")
    removed = clean_non_standard_items(ata_dir, dry_run)
    if removed:
        sample = ", ".join(removed[:10])
        suffix = "..." if len(removed) > 10 else ""
        print(f"  Removed {len(removed)} non-standard items: {sample}{suffix}")
    else:
        print(f"  No non-standard items to remove")
    
    print(f"\n✓ Completed standardization of {ata_dir.name}")


def find_all_ata_directories(base_path: Path):
    """Find all ATA-XX directories in the repository."""
    ata_dirs = []
    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            if d.startswith('ATA-'):
                ata_dirs.append(Path(root) / d)
    return sorted(ata_dirs)


def main():
    parser = argparse.ArgumentParser(
        description='Standardize ATA-XX directory structures across the repository'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    parser.add_argument(
        '--ata-dir',
        type=str,
        help='Standardize a specific ATA directory (e.g., PRODUCTS/.../ATA-42)'
    )
    
    args = parser.parse_args()
    
    if args.dry_run:
        print("=" * 80)
        print("DRY RUN MODE - No changes will be made")
        print("=" * 80)
    
    base_path = Path('/home/runner/work/ASI-T2/ASI-T2/PRODUCTS')
    
    if args.ata_dir:
        # Standardize specific directory
        ata_dir = Path(args.ata_dir)
        if not ata_dir.exists():
            print(f"Error: Directory not found: {ata_dir}")
            return 1
        standardize_ata_directory(ata_dir, args.dry_run)
    else:
        # Standardize all ATA directories
        ata_dirs = find_all_ata_directories(base_path)
        print(f"\nFound {len(ata_dirs)} ATA directories to standardize")
        
        for i, ata_dir in enumerate(ata_dirs, 1):
            print(f"\n[{i}/{len(ata_dirs)}]")
            standardize_ata_directory(ata_dir, args.dry_run)
    
    print("\n" + "=" * 80)
    print("Standardization complete!")
    print("=" * 80)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
