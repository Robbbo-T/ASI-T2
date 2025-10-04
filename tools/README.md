# ASI-T2 Filename Policy Tools

This directory contains tools for enforcing standardized filename conventions across S1000D Data Modules (DM) and CAx engineering files.

## Overview

The ASI-T2 project standardizes on:
- **ATA short-code**: 5710 (4-digit form representing ATA 57-10, Wing Structure)
- **S1000D DM**: Issue 5.0/6.0 naming convention
- **CAx domains**: CAD, CAE, CAM, CAV, CMP

## Tools

### lint_names.py

Validates filenames against ASI-T2 standards with actionable error messages.

**Usage:**
```bash
# Check specific files
python3 tools/lint_names.py file1.step file2.xml

# Check directory recursively
python3 tools/lint_names.py .

# Check specific path
python3 tools/lint_names.py PRODUCTS/AMPEL360/
```

**Supported Patterns:**

#### S1000D Data Modules
```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC><DAC>-<IC><ICV>-<ILC>-<LANG>-<COUNTRY>.xml
```

Example: `DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml`

#### CAx Engineering Files
```
<DISC>-<MIC>-<DOMAIN><ATA>-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-r<REV>.<EXT>
```

Examples:
```
ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step
PRT-BWQ1-CAD5710-UPPER-CAP-LH-r007.sldprt
FEM-BWQ1-CAE5710-FS-BOX-STAT-r006.inp
NC-BWQ1-CAM5710-FWD-SPAR-OP10-MILL-r003.nc
QIP-BWQ1-CAV5710-FWD-SPAR-DIM-PLAN-r006.pdf
EPR-BWQ1-CMP5710-FWD-SPAR-EOL-PLAN-r001.pdf
```

**Domain/DISC Mapping:**

| Domain | Purpose | Object Types (DISC) |
|--------|---------|---------------------|
| CAD | Design | ASSY, PRT, DRW, MBD |
| CAE | Analysis | FEM, CFD, EMI |
| CAM | Manufacturing | NC, APT, OPR, FIX, TOOL, SET |
| CAV | Quality V&V/Certification | QIP, QIF, DMIS, MEAS, MSA, CERT |
| CMP | EoL/Recycling | EPR, RECY, TREAT, DISP, MATREC |

**Field Definitions:**

- **DISC**: Object type (see table above)
- **MIC**: Model Identification Code (3-4 chars, e.g., BWQ1, Q100)
- **DOMAIN**: CAD, CAE, CAM, CAV, or CMP
- **ATA**: 4-digit ATA code (57xx, e.g., 5710)
- **SCOPE**: UPPERCASE kebab-case descriptor (A-Z, 0-9, -)
- **HAND** (optional): LH, RH, or CEN (Left/Right/Center)
- **EFFT** (optional): Effectivity (e.g., APPL-BWBQ100-0001-0999, E0001-0999)
- **LIFE** (optional): Lifecycle tag (GA, STAT, UL, FAT, DTA, CERT, VNV, QC, EOL)
- **REV**: 3-digit revision (e.g., r012)
- **EXT**: File extension (domain-specific)

**Validation Features:**

✅ S1000D DMC pattern compliance  
✅ CAx pattern compliance (all domains)  
✅ SCOPE kebab-case rules (no leading/trailing/consecutive dashes)  
✅ Domain/DISC consistency checks  
✅ Domain/extension validation  
✅ Helpful error messages for common mistakes  
✅ Legacy code detection (571, 571010)  
✅ Optional UTCS sidecar validation  

**Exit Codes:**
- `0` - All files compliant
- `1` - Non-compliant files found

## Migration Script

See [../scripts/migrate_ata_shortcode.py](../scripts/migrate_ata_shortcode.py) for migrating legacy 571/571010 codes to 5710.

## Schematron Validation

See [../schematron/asi-t2-dmfile.sch](../schematron/asi-t2-dmfile.sch) for BREX/CSDB validation rules.

## CI/CD Integration

### Pre-commit Hook

The filename policy is enforced via pre-commit hook:

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run asi-t2-filename-policy --all-files
```

See [../.pre-commit-config.yaml](../.pre-commit-config.yaml)

### GitHub Actions

Automatic validation on pull requests and pushes:

See [../.github/workflows/filename-policy.yml](../.github/workflows/filename-policy.yml)

## QSS Prefix Convention

For quick filtering of quality/repair items, use QSS- prefix in SCOPE:

```
PRT-BWQ1-CAD5710-QSS-PATCH-FS-INB-LH-r002.sldprt
ASSY-BWQ1-CAD5710-QSS-PATCH-KIT-GA-r004.step
FEM-BWQ1-CAE5710-QSS-PATCH-LOCAL-STAT-r001.inp
```

## Optional JSON Sidecar

CAx files can have optional JSON sidecars with metadata:

```json
{
  "dmRefs": [
    "DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml",
    "DMC-BWQ1-A-57-10-10-00A-520A-D-EN-US.xml"
  ],
  "utcsAnchor": "sha256:abc123...",
  "effectivity": "APPL-BWBQ100-0001-0999",
  "loadsCase": "STAT-UL-1.5g",
  
  "cam": {
    "machine": "HERMLE-C42",
    "controller": "Heidenhain iTNC",
    "post": "UGPost 4.2"
  },
  
  "cav": {
    "metrology": "CMM Zeiss ACCURA",
    "program": "DMIS r002",
    "qifVersion": "3.0"
  },
  
  "eol": {
    "treatmentCode": "RECY-AL",
    "recyclateFraction": 0.98
  }
}
```

The linter validates `utcsAnchor` SHA256 checksums if present.

## Common Errors

### Use short ATA (5710), not long (571010)
**Old:** `ASSY-BWQ1-CAD571010-FWD-SPAR-r001.step`  
**New:** `ASSY-BWQ1-CAD5710-FWD-SPAR-r001.step`

### Use 4-digit ATA (57xx), not very short (571)
**Old:** `ASSY-BWQ1-CAD571-FWD-SPAR-r001.step`  
**New:** `ASSY-BWQ1-CAD5710-FWD-SPAR-r001.step`

### SCOPE must not start/end with '-'
**Bad:** `ASSY-BWQ1-CAD5710--FWD-SPAR-r001.step`  
**Good:** `ASSY-BWQ1-CAD5710-FWD-SPAR-r001.step`

### DISC must match domain
**Bad:** `MBD-BWQ1-CAE5710-PART-r001.dat` (MBD is CAD, not CAE)  
**Good:** `MBD-BWQ1-CAD5710-PART-r001.dat`

## Rollout Notes

The linter currently accepts any 57xx ATA code. To enforce 5710 only during rollout, uncomment this line in `lint_names.py`:

```python
# if ata != '5710':
#     fail(name, "ATA must be 5710 during rollout")
#     ok = False
```

## References

- S1000D Issue 5.0/6.0 Specification
- ATA iSpec 2200 (Chapter 57: Wings)
- UTCS-MI v5.0 (Canonical Hash)
- MAL-EEM Ethics Guard

---

**Version:** 1.0.0  
**Maintainer:** ASI-T Architecture Team  
**Last Updated:** 2025-10-04
