# CAx Filename Standardization - Implementation Summary

## Overview

Successfully implemented comprehensive filename standardization for ASI-T2 project covering:
- **S1000D Data Modules** (DM) - Issue 5.0/6.0
- **CAx Engineering Files** - CAD/CAE/CAM/CAV/CMP domains
- **ATA Short-Code** - Standardized on 5710 (4-digit format)

## Components Delivered

### 1. Core Linter (`tools/lint_names.py`)

**Features:**
- ✅ S1000D DMC filename validation
- ✅ CAx filename validation (5 domains)
- ✅ Domain/DISC consistency checks
- ✅ SCOPE kebab-case validation
- ✅ GitHub Actions error annotations
- ✅ Helpful error messages for common mistakes
- ✅ Optional UTCS sidecar validation
- ✅ Legacy code detection (571, 571010)

**Domains Supported:**
- **CAD** (Design): ASSY, PRT, DRW, MBD
- **CAE** (Analysis): FEM, CFD, EMI
- **CAM** (Manufacturing): NC, APT, OPR, FIX, TOOL, SET
- **CAV** (Quality V&V): QIP, QIF, DMIS, MEAS, MSA, CERT
- **CMP** (EoL/Recycling): EPR, RECY, TREAT, DISP, MATREC

**Usage:**
```bash
python3 tools/lint_names.py .
python3 tools/lint_names.py file1.step file2.xml
```

### 2. Migration Script (`scripts/migrate_ata_shortcode.py`)

**Purpose:** Convert legacy ATA codes to standardized 5710 format

**Conversions:**
- 571 → 5710
- 571010 → 5710
- Other 57xx → preserved

**Features:**
- Dry-run mode
- Batch processing
- Collision detection
- Progress reporting

**Usage:**
```bash
python3 scripts/migrate_ata_shortcode.py --dry-run .
python3 scripts/migrate_ata_shortcode.py /path/to/cax/files
```

### 3. Schematron Rules (`schematron/asi-t2-dmfile.sch`)

**Validation Patterns:**
1. **DMC Filename Policy** - S1000D pattern compliance
2. **ATA Path Alignment** - Folder structure matches dmCode
3. **Chapter 57 Validation** - Wing structure specific rules
4. **MIC Consistency** - Filename MIC matches internal metadata

**Integration:**
- BREX data modules
- CSDB validation pipelines
- Command-line tools (Saxon, xmllint)

### 4. CI/CD Integration

#### Pre-commit Hook (`.pre-commit-config.yaml`)
```yaml
- id: asi-t2-filename-policy
  name: ASI-T2 filename policy (DM + CAx)
  entry: python3 tools/lint_names.py
  language: system
  pass_filenames: true
```

**Installation:**
```bash
pip install pre-commit
pre-commit install
```

#### GitHub Actions (`.github/workflows/filename-policy.yml`)
- Triggers on PR and push
- Validates changed files in PR mode
- Full scan on push to main/copilot branches
- Generates summary reports
- Provides helpful error annotations

### 5. Documentation

- **`tools/README.md`** - Comprehensive usage guide
- **`tools/examples/README.md`** - 100+ examples with field breakdowns
- **`schematron/README.md`** - BREX integration guide
- Example files for all domains

## Pattern Specifications

### S1000D Data Module Pattern
```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC><DAC>-<IC><ICV>-<ILC>-<LANG>-<COUNTRY>.xml
```

Example: `DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml`

### CAx Filename Pattern
```
<DISC>-<MIC>-<DOMAIN><ATA>-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-r<REV>.<EXT>
```

Examples:
```
ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step                    (CAD)
FEM-BWQ1-CAE5710-FS-BOX-STAT-r006.inp                      (CAE)
NC-BWQ1-CAM5710-FWD-SPAR-OP10-MILL-3AX-r003.nc            (CAM)
QIP-BWQ1-CAV5710-FWD-SPAR-DIM-PLAN-r006.pdf               (CAV)
EPR-BWQ1-CMP5710-FWD-SPAR-EOL-PLAN-r001.pdf               (CMP)
```

## Validation Results

### Integration Tests
```
✓ Linter validation on 6 example files
✓ S1000D validation on 8 existing DM files
✓ Migration script dry-run
✓ Schematron XML well-formedness
✓ YAML configuration syntax
```

### Common Error Detection
```
✓ Legacy code 571 → "Use 4-digit ATA (5710), not 571"
✓ Legacy code 571010 → "Use short ATA (5710), not long (571010)"
✓ Invalid SCOPE → "SCOPE must not contain consecutive '-'"
✓ Domain mismatch → "DISC 'MBD' is not valid for domain 'CAE'"
```

## QSS Prefix Convention

For quality/repair items, use QSS- prefix in SCOPE:
```
PRT-BWQ1-CAD5710-QSS-PATCH-FS-INB-LH-r002.sldprt
FEM-BWQ1-CAE5710-QSS-PATCH-LOCAL-STAT-r001.inp
QIP-BWQ1-CAV5710-QSS-PATCH-LOCAL-DIM-PLAN-r001.pdf
```

## Optional Features

### JSON Sidecar Metadata
Companion `.json` files with:
- DMC references
- UTCS anchor (SHA256)
- Effectivity
- Domain-specific metadata (CAM machine, CAV metrology, EoL treatment)

Example: `ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step.json`

### ATA Rollout Lock
To enforce 5710 only during initial rollout, uncomment in `lint_names.py`:
```python
if ata != '5710':
    fail(name, "ATA must be 5710 during rollout")
```

## Repository Structure

```
ASI-T2/
├── tools/
│   ├── lint_names.py          # Main linter
│   ├── README.md              # Tools documentation
│   └── examples/
│       ├── README.md          # Examples guide
│       ├── ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step
│       ├── NC-BWQ1-CAM5710-FWD-SPAR-OP10-r003.nc
│       ├── QIP-BWQ1-CAV5710-FWD-SPAR-DIM-PLAN-r006.pdf
│       ├── EPR-BWQ1-CMP5710-FWD-SPAR-EOL-PLAN-r001.pdf
│       └── ... (more examples)
├── scripts/
│   └── migrate_ata_shortcode.py  # Migration tool
├── schematron/
│   ├── asi-t2-dmfile.sch      # Schematron rules
│   └── README.md              # Schematron guide
├── .github/workflows/
│   └── filename-policy.yml    # CI workflow
└── .pre-commit-config.yaml    # Pre-commit hook
```

## Adoption Path

### Phase 1: Validation (Current)
- ✅ Linter available for local testing
- ✅ Pre-commit hook (opt-in)
- ✅ GitHub Actions (informational)

### Phase 2: Migration (Optional)
- Use migration script on existing files
- Review and validate changes
- Commit in batches by domain

### Phase 3: Enforcement (Future)
- Enable pre-commit hook mandatory
- GitHub Actions blocks non-compliant files
- BREX/CSDB validation in production

## Testing

Run comprehensive test suite:
```bash
# Test linter
python3 tools/lint_names.py tools/examples/

# Test on existing S1000D files
python3 tools/lint_names.py PRODUCTS/.../ata/.../dmodule/

# Test migration (dry-run)
python3 scripts/migrate_ata_shortcode.py --dry-run .

# Validate Schematron
python3 -c "from xml.etree import ElementTree as ET; ET.parse('schematron/asi-t2-dmfile.sch')"

# Validate configs
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/filename-policy.yml'))"
```

## References

- **S1000D**: Issue 5.0/6.0 Specification
- **ATA iSpec 2200**: Chapter 57 (Wings)
- **UTCS-MI**: v5.0 (Canonical Hash)
- **MAL-EEM**: Ethics Guard

## Support

- **Documentation**: See `tools/README.md`, `schematron/README.md`
- **Examples**: See `tools/examples/README.md`
- **Issues**: File GitHub issues with tag `filename-policy`

---

**Implementation Date:** 2025-10-04  
**Version:** 1.0.0  
**Status:** ✅ Complete and Tested  
**Maintainer:** ASI-T Architecture Team
