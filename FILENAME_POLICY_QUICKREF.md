# ASI-T2 Filename Policy - Quick Reference

## Pattern Templates

### S1000D Data Module
```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC><DAC>-<IC><ICV>-<ILC>-<LANG>-<COUNTRY>.xml
```

### CAx Engineering File
```
<DISC>-<MIC>-<DOMAIN><ATA>-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-r<REV>.<EXT>
```

## Domain Reference

| Domain | Purpose | Object Types |
|--------|---------|--------------|
| **CAD** | Design | ASSY, PRT, DRW, MBD |
| **CAE** | Analysis | FEM, CFD, EMI |
| **CAM** | Manufacturing | NC, APT, OPR, FIX, TOOL, SET |
| **CAV** | Quality V&V | QIP, QIF, DMIS, MEAS, MSA, CERT |
| **CMP** | EoL/Recycling | EPR, RECY, TREAT, DISP, MATREC |

## Field Guide

- **MIC**: Model ID (3-4 chars) - `BWQ1`, `Q100`
- **ATA**: 4-digit code - `5710` (Wing Structure)
- **SCOPE**: UPPERCASE kebab-case - `FWD-SPAR-OP10`
- **HAND**: `LH` | `RH` | `CEN`
- **EFFT**: `APPL-<model>-<range>` or `E<range>`
- **LIFE**: `GA` | `STAT` | `UL` | `FAT` | `DTA` | `CERT` | `VNV` | `QC` | `EOL`
- **REV**: `r###` (3 digits) - `r012`

## Quick Examples

```bash
# CAD Design
ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step
PRT-BWQ1-CAD5710-UPPER-CAP-LH-r007.sldprt

# CAE Analysis
FEM-BWQ1-CAE5710-FS-BOX-STAT-r006.inp
CFD-BWQ1-CAE5710-WING-TIP-r015.cas

# CAM Manufacturing
NC-BWQ1-CAM5710-FWD-SPAR-OP10-r003.nc
FIX-BWQ1-CAM5710-FS-BOX-VISE-GA-r001.step

# CAV Quality
QIP-BWQ1-CAV5710-FWD-SPAR-DIM-PLAN-r006.pdf
DMIS-BWQ1-CAV5710-FWD-SPAR-CMM-r002.dmis

# CMP End-of-Life
EPR-BWQ1-CMP5710-FWD-SPAR-EOL-PLAN-r001.pdf
RECY-BWQ1-CMP5710-FWD-SPAR-AL-RECYCLE-r003.csv

# S1000D
DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml
```

## Common Commands

```bash
# Validate files
python3 tools/lint_names.py .
python3 tools/lint_names.py file1.step file2.xml

# Migrate legacy codes
python3 scripts/migrate_ata_shortcode.py --dry-run .
python3 scripts/migrate_ata_shortcode.py /path/to/files

# Install pre-commit hook
pip install pre-commit
pre-commit install

# Run pre-commit manually
pre-commit run asi-t2-filename-policy --all-files
```

## Common Errors

❌ **Use 4-digit ATA**
```
Bad:  ASSY-BWQ1-CAD571-FWD-SPAR-r001.step
Good: ASSY-BWQ1-CAD5710-FWD-SPAR-r001.step
```

❌ **Use short ATA, not long**
```
Bad:  ASSY-BWQ1-CAD571010-FWD-SPAR-r001.step
Good: ASSY-BWQ1-CAD5710-FWD-SPAR-r001.step
```

❌ **No consecutive dashes in SCOPE**
```
Bad:  ASSY-BWQ1-CAD5710--FWD-SPAR-r001.step
Good: ASSY-BWQ1-CAD5710-FWD-SPAR-r001.step
```

❌ **SCOPE must be UPPERCASE**
```
Bad:  ASSY-BWQ1-CAD5710-fwd-spar-r001.step
Good: ASSY-BWQ1-CAD5710-FWD-SPAR-r001.step
```

❌ **DISC must match domain**
```
Bad:  MBD-BWQ1-CAE5710-PART-r001.dat  (MBD is CAD)
Good: MBD-BWQ1-CAD5710-PART-r001.dat
```

## QSS Prefix (Quality/Repair)

```bash
PRT-BWQ1-CAD5710-QSS-PATCH-FS-INB-LH-r002.sldprt
FEM-BWQ1-CAE5710-QSS-PATCH-LOCAL-STAT-r001.inp
QIP-BWQ1-CAV5710-QSS-PATCH-DIM-PLAN-r001.pdf
```

## Resources

- **Full Guide**: `tools/README.md`
- **Examples**: `tools/examples/README.md`
- **Schematron**: `schematron/README.md`
- **Summary**: `FILENAME_POLICY_SUMMARY.md`

---
**Version**: 1.0.0 | **Updated**: 2025-10-04
