# ATA Canonical Structure - Quick Start Guide

This guide shows how to use the ATA canonical structure system.

## Overview

The ASI-T2 repository now implements a **canonical ATA structure** where:
- Each ATA chapter has ONE authoritative location in `2-DOMAINS-LEVELS/<DOMAIN>/ata/<ATA>/`
- Products reference canonical via symlinks (no duplication)
- Standard structure, governance, and validation tools

## Quick Start

### 1. Create a New Canonical ATA

```bash
# Create ATA-42 (Integrated Modular Avionics) in IIS domain
python scripts/standardize_ata_structure.py --atas ATA-42 --create

# This creates:
# - 2-DOMAINS-LEVELS/IIS/ata/ATA-42/
# - Standard directory structure
# - README.md and CONVENTIONS.md from templates
# - governance/cross_references.yaml
```

### 2. List Existing Canonical ATAs

```bash
python scripts/standardize_ata_structure.py --list

# Output:
# ATA        Domain     Path
# --------------------------------------------------------------------------
# ATA-42     IIS        2-DOMAINS-LEVELS/IIS/ata/ATA-42
```

### 3. Validate Structure

```bash
# Validate specific ATA
python scripts/standardize_ata_structure.py --atas ATA-42 --validate

# Verify one canonical per ATA
python scripts/verify_canonical_uniqueness.py

# Validate cross-references
python scripts/validate_cross_references.py --all
```

### 4. View Compliance Requirements

```bash
# Show compliance for ATA-42
python scripts/map_compliance.py --ata ATA-42

# List all ATAs with compliance requirements
python scripts/map_compliance.py --list

# Output as JSON
python scripts/map_compliance.py --ata ATA-42 --format json

# Output as Markdown
python scripts/map_compliance.py --ata ATA-42 --format markdown > ATA-42-compliance.md
```

### 5. Create Product Symlinks

```bash
# Create symlinks from product trees to canonical
python scripts/standardize_ata_structure.py --atas ATA-42 --symlinks

# Validate symlinks
python scripts/validate_symlinks.py

# Fix broken symlinks
python scripts/validate_symlinks.py --fix
```

## Directory Structure

Each canonical ATA follows this structure:

```
2-DOMAINS-LEVELS/<DOMAIN>/ata/<ATA>/
├── README.md                     # Canonical home page
├── CONVENTIONS.md                # Conventions
├── governance/                   # Change control, baselines, risks
├── os/                          # Design, S1000D, testing, compliance
├── manufacturing/               # BOM, process, quality, tooling
├── sustainment/                 # Service, spares, reliability
├── assets/                      # Technical assets
├── scripts/                     # Local automation
└── docs/                        # Design notes
```

## Common Tasks

### Add Cross-Domain Reference

Edit `governance/cross_references.yaml`:

```yaml
xrefs:
  - from: 
      ata: ATA-42
      domain: IIS
    to:
      ata: ATA-45
      domain: IIS
    type: dependency
    reason: "IMA platform depends on CMS for health monitoring"
    status: active
```

Validate:
```bash
python scripts/validate_cross_references.py --ata ATA-42 --domain IIS
```

### Create Multiple ATAs

```bash
# Create multiple ATAs at once
python scripts/standardize_ata_structure.py --atas ATA-42,ATA-45,ATA-46 --create

# Include shared domains
python scripts/standardize_ata_structure.py --atas ATA-45 --include-shared --create
```

### Dry Run (Preview)

```bash
# Preview what would be created
python scripts/standardize_ata_structure.py --atas ATA-42 --create --dry-run --verbose
```

## Scripts Reference

### standardize_ata_structure.py

**Purpose:** Create, validate, and manage canonical ATA structure

**Key Options:**
- `--atas ATA-42,ATA-45` - Specify ATAs to process
- `--domain IIS` - Override canonical domain
- `--create` - Create canonical structure
- `--validate` - Validate structure
- `--symlinks` - Create product symlinks
- `--list` - List existing canonical ATAs
- `--include-shared` - Process shared domains
- `--dry-run` - Preview without changes
- `--verbose` - Detailed output

### validate_cross_references.py

**Purpose:** Validate cross_references.yaml files

**Key Options:**
- `--ata ATA-42 --domain IIS` - Validate specific ATA
- `--all` - Validate all cross-reference files
- `--verbose` - Detailed output

### map_compliance.py

**Purpose:** Render compliance requirements for ATAs

**Key Options:**
- `--ata ATA-42` - Show compliance for specific ATA
- `--all` - Show all ATAs
- `--list` - List ATAs with compliance requirements
- `--format text|markdown|json` - Output format

### verify_canonical_uniqueness.py

**Purpose:** Verify each ATA has exactly one canonical location

**Key Options:**
- `--verbose` - Show warnings and details

### validate_symlinks.py

**Purpose:** Validate product symlinks to canonical ATAs

**Key Options:**
- `--product BWB-Q100` - Limit to specific product
- `--fix` - Fix broken symlinks
- `--verbose` - Show all symlinks

## Resources

### Templates
- `8-RESOURCES/ATA_CANONICAL/ATA_README_TEMPLATE.md` - README template
- `8-RESOURCES/ATA_CANONICAL/CONVENTIONS_TEMPLATE.md` - Conventions template

### Configuration
- `8-RESOURCES/ATA_CANONICAL/ATA_REGISTRY.yaml` - ATA definitions (41 chapters)
- `8-RESOURCES/ATA_CANONICAL/COMPLIANCE_MATRIX.yaml` - Compliance requirements
- `8-RESOURCES/ATA_CANONICAL/XREF_MASTER.yaml` - Cross-reference schema

### Documentation
- `2-DOMAINS-LEVELS/README.md` - Canonical structure overview
- `8-RESOURCES/ATA_CANONICAL/README.md` - Resources documentation

## Examples

### Example 1: Create ATA-42 with Full Setup

```bash
# Step 1: Create canonical structure
python scripts/standardize_ata_structure.py --atas ATA-42 --create --verbose

# Step 2: Validate
python scripts/standardize_ata_structure.py --atas ATA-42 --validate

# Step 3: Check compliance
python scripts/map_compliance.py --ata ATA-42

# Step 4: Create symlinks (if products exist)
python scripts/standardize_ata_structure.py --atas ATA-42 --symlinks
```

### Example 2: Batch Create Multiple ATAs

```bash
# Create all avionics ATAs
python scripts/standardize_ata_structure.py \
  --atas ATA-22,ATA-23,ATA-31,ATA-34,ATA-42,ATA-45,ATA-46 \
  --create --verbose

# Verify all created correctly
python scripts/verify_canonical_uniqueness.py
```

### Example 3: Validate Everything

```bash
# Validate all canonical structures
python scripts/standardize_ata_structure.py --list

# Check uniqueness
python scripts/verify_canonical_uniqueness.py

# Validate cross-references
python scripts/validate_cross_references.py --all

# Validate symlinks
python scripts/validate_symlinks.py
```

## Compliance Matrix

The system tracks compliance requirements for 14 ATAs covering:

**Standards:**
- DO-178C, DO-254, DO-297, DO-330, DO-331 (Software/Hardware)
- ARP4754A, ARP4761 (Systems/Safety)
- DO-326A, DO-356A (Cybersecurity)
- CS-25, CS-E, 14-CFR-25 (Airworthiness)
- ARINC-429, ARINC-653, ARINC-661, ARINC-664 (Avionics)

**Example: ATA-42 (IMA) Compliance:**
- DAL A (highest criticality)
- 11 applicable standards
- Focus: DO-297 (IMA), DO-178C/254, ARINC-653/664

Use `python scripts/map_compliance.py --list` for full list.

## Domain Definitions

8 domains covering 41 ATA chapters:

- **AAA** - Airframe & Structures (8 ATAs)
- **CCC** - Cabin & Cargo (2 ATAs)
- **EEE** - Electrical & Environmental (7 ATAs)
- **IIF** - Integrated Flight Systems (1 ATA)
- **IIS** - Integrated Information Systems (7 ATAs)
- **MMM** - Mechanisms & Actuation (1 ATA)
- **OOO** - Operations & Maintenance (shared only)
- **PPP** - Propulsion & Power (14 ATAs)

See `8-RESOURCES/ATA_CANONICAL/ATA_REGISTRY.yaml` for complete mappings.

## Next Steps

1. **Create more canonical ATAs** for your domains
2. **Migrate existing content** from products to canonical
3. **Set up CI validation** to enforce structure
4. **Document cross-references** between ATAs
5. **Add compliance evidence** to canonical folders

## Support

For questions or issues:
1. Check script help: `python scripts/<script>.py --help`
2. Review documentation in `8-RESOURCES/ATA_CANONICAL/`
3. See examples in this guide
4. Examine existing ATA-42 structure

---

**Last Updated:** 2025-09-30  
**Version:** 0.1.0
