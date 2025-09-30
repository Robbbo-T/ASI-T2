# ATA Canonical Resources

This directory contains shared resources and templates for canonical ATA chapter management.

## Files

### Templates

* **ATA_README_TEMPLATE.md** - Standard README template for canonical ATA folders
* **CONVENTIONS_TEMPLATE.md** - Standard conventions document template

### Configuration

* **ATA_REGISTRY.yaml** - Master registry of ATA chapters, canonical domains, and shared domains
* **XREF_MASTER.yaml** - Schema for cross-reference YAML files
* **COMPLIANCE_MATRIX.yaml** - Master compliance requirements by ATA chapter

## Usage

### Creating a New Canonical ATA

1. Use the `standardize_ata_structure.py` script:
   ```bash
   python scripts/standardize_ata_structure.py --atas ATA-42 --domain IIS --create
   ```

2. This will:
   - Create the canonical structure in `2-DOMAINS-LEVELS/<DOMAIN>/ata/<ATA>/`
   - Populate README and CONVENTIONS from templates
   - Create required subdirectories
   - Optionally create symlinks from product trees

### Manual Setup

If creating manually:

1. Copy templates:
   ```bash
   cp 8-RESOURCES/ATA_CANONICAL/ATA_README_TEMPLATE.md \
      2-DOMAINS-LEVELS/<DOMAIN>/ata/<ATA>/README.md
   cp 8-RESOURCES/ATA_CANONICAL/CONVENTIONS_TEMPLATE.md \
      2-DOMAINS-LEVELS/<DOMAIN>/ata/<ATA>/CONVENTIONS.md
   ```

2. Replace placeholders:
   - `<DOMAIN>` - Domain code (e.g., IIS, AAA, PPP)
   - `<ATA>` - ATA chapter (e.g., ATA-42)
   - `<ATA_NUMBER>` - Number only (e.g., 42)
   - `<Short Title>` - ATA title (e.g., Integrated Modular Avionics)
   - `<DATE>` - Current date

3. Create directory structure per README §1

## Validation

Validate canonical structure and cross-references:

```bash
# Check structure
python scripts/standardize_ata_structure.py --validate

# Check cross-references
python scripts/validate_cross_references.py --all

# Check compliance mappings
python scripts/map_compliance.py --ata ATA-42

# Verify uniqueness
python scripts/verify_canonical_uniqueness.py

# Validate symlinks
python scripts/validate_symlinks.py
```

## Schema Details

### ATA_REGISTRY.yaml

Defines:
- ATA chapter numbers and titles
- Canonical domain ownership
- Shared domain relationships
- Domain definitions and primary ATAs

### XREF_MASTER.yaml

JSON Schema for `governance/cross_references.yaml` files supporting:
- Overlay references (domain-specific extensions)
- Variant references (alternative implementations)
- Dependency references (functional dependencies)
- Reference links (informational)

### COMPLIANCE_MATRIX.yaml

Defines:
- Applicable standards (DO-178C, DO-254, CS-25, etc.)
- DAL (Design Assurance Level) requirements
- Standard authority and scope
- ATA-specific compliance mappings

## Canonical vs. Product

**Canonical (2-DOMAINS-LEVELS/):**
- Single source of truth
- Domain-owned
- Generic/reusable content
- Formal change control

**Product (PRODUCTS/):**
- Product-specific instances
- Symlinks to canonical where possible
- Product-specific overlays
- Fast iteration

## See Also

- [Repository README](../../README.md)
- [Standardization Script](../../scripts/standardize_ata_structure.py)
- [Validation Scripts](../../scripts/)
