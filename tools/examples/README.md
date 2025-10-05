# CAx Filename Examples

This directory contains example filenames demonstrating the ASI-T2 naming conventions across all supported domains.

## Valid Examples by Domain

### CAD (Computer-Aided Design)

Design models, assemblies, drawings, and model-based definitions.

```
ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step
PRT-BWQ1-CAD5710-UPPER-CAP-LH-r007.sldprt
PRT-BWQ1-CAD5710-UPPER-CAP-RH-r007.sldprt
DRW-BWQ1-CAD5710-FWD-SPAR-A1-r002.pdf
DRW-BWQ1-CAD5710-FWD-SPAR-A1-r002.dwg
MBD-BWQ1-CAD5710-LEFLAP-INTERFACE-GA-r001.step
```

**With effectivity:**
```
ASSY-BWQ1-CAD5710-FWD-SPAR-APPL-BWBQ100-0001-0999-GA-r005.step
PRT-BWQ1-CAD5710-UPPER-CAP-LH-E0001-0999-r008.sldprt
```

**QSS (Quality/Repair) items:**
```
PRT-BWQ1-CAD5710-QSS-PATCH-FS-INB-LH-r002.sldprt
ASSY-BWQ1-CAD5710-QSS-PATCH-KIT-GA-r004.step
```

### CAE (Computer-Aided Engineering)

Finite element models, computational fluid dynamics, electromagnetic interference analysis.

```
FEM-BWQ1-CAE5710-FS-BOX-STAT-r006.inp
FEM-BWQ1-CAE5710-UPPER-CAP-LH-UL-r003.nas
FEM-BWQ1-CAE5710-FS-BOX-APPL-BWBQ100-0001-0999-STAT-r008.inp
CFD-BWQ1-CAE5710-FS-BOX-GA-r010.cas
CFD-BWQ1-CAE5710-WING-TIP-VORTEX-r015.dat
EMI-BWQ1-CAE5710-FUEL-TANK-SHIELDING-r003.cdb
```

**QSS (Quality/Repair) analysis:**
```
FEM-BWQ1-CAE5710-QSS-PATCH-LOCAL-STAT-r001.inp
```

### CAM (Computer-Aided Manufacturing)

NC programs, tool paths, operation sheets, fixtures, tooling.

```
NC-BWQ1-CAM5710-FWD-SPAR-OP10-MILL-3AX-r003.nc
NC-BWQ1-CAM5710-FWD-SPAR-OP20-DRILL-HERMLE-C42-r002.eia
APT-BWQ1-CAM5710-FWD-SPAR-OP20-ROUGH-PKT-r002.apt
OPR-BWQ1-CAM5710-FWD-SPAR-SETUP-SHEET-r004.pdf
FIX-BWQ1-CAM5710-FS-BOX-MAIN-VISE-GA-r001.step
TOOL-BWQ1-CAM5710-FWD-SPAR-TOOL-LIST-GA-r001.csv
SET-BWQ1-CAM5710-FWD-SPAR-SETUP-INSTR-r003.pdf
```

**With hand/effectivity:**
```
NC-BWQ1-CAM5710-FWD-SPAR-OP30-LH-r005.nc
FIX-BWQ1-CAM5710-UPPER-CAP-LH-DRILL-FIXTURE-r002.step
```

### CAV (Computer-Aided Verification/Validation)

Quality inspection plans, QIF models, CMM programs, measurement results, MSA studies, certificates.

```
QIP-BWQ1-CAV5710-FWD-SPAR-DIM-PLAN-r006.pdf
QIF-BWQ1-CAV5710-FWD-SPAR-MBD-GDTPMI-r003.qif
DMIS-BWQ1-CAV5710-FWD-SPAR-IP-OP10-r002.dmis
MEAS-BWQ1-CAV5710-FWD-SPAR-CMM-RESULTS-r007.csv
MSA-BWQ1-CAV5710-FWD-SPAR-GAGE-RR-r001.pdf
CERT-BWQ1-CAV5710-FWD-SPAR-COC-LOT-2025Q3-r001.pdf
```

**With lifecycle tags:**
```
QIP-BWQ1-CAV5710-FWD-SPAR-DIM-PLAN-FAT-r002.pdf
MEAS-BWQ1-CAV5710-FS-BOX-CMM-RESULTS-DTA-r005.csv
CERT-BWQ1-CAV5710-FWD-SPAR-COA-CERT-r003.pdf
```

**QSS (Quality) verification:**
```
QIP-BWQ1-CAV5710-QSS-PATCH-LOCAL-DIM-PLAN-r001.pdf
DMIS-BWQ1-CAV5710-QSS-PATCH-CMM-PROG-r002.dmis
```

### CMP (CAMPost - End-of-Life Management)

Environmental product reports, recycling routes, treatment plans, disposal traces, material recovery.

```
EPR-BWQ1-CMP5710-FWD-SPAR-EOL-PLAN-r001.pdf
RECY-BWQ1-CMP5710-FWD-SPAR-MATREC-AL7050-98PCT-r003.csv
TREAT-BWQ1-CMP5710-FWD-SPAR-HAZ-COAT-STRIP-REUSE-r002.pdf
DISP-BWQ1-CMP5710-FWD-SPAR-DISPOSAL-TRACE-r001.xml
MATREC-BWQ1-CMP5710-FWD-SPAR-AL-RECOVERY-REPORT-r001.json
CERT-BWQ1-CMP5710-FWD-SPAR-EOL-CERT-r001.pdf
```

**With lifecycle tag:**
```
EPR-BWQ1-CMP5710-FWD-SPAR-EOL-PLAN-EOL-r002.pdf
RECY-BWQ1-CMP5710-UPPER-CAP-CF-RECYCLE-EOL-r001.csv
```

**QSS (Quality) EoL:**
```
RECY-BWQ1-CMP5710-QSS-PATCH-MATREC-CF-RECYCLE-r001.csv
```

## S1000D Data Module Examples

```
DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml
DMC-BWQ1-A-57-10-20-00A-520A-D-EN-US.xml
DMC-Q100-A-42-11-00-00A-010A-D-EN-US.xml
DMC-Q100-A-42-12-00-00A-012A-D-EN-US.xml
```

## Field Breakdown

### Example: `NC-BWQ1-CAM5710-FWD-SPAR-OP10-MILL-3AX-LH-r003.nc`

| Field | Value | Description |
|-------|-------|-------------|
| DISC | NC | NC machine program |
| MIC | BWQ1 | Model Identification Code (BWB-Q100, variant 1) |
| DOMAIN | CAM | Computer-Aided Manufacturing |
| ATA | 5710 | ATA 57-10 (Wing Structure) |
| SCOPE | FWD-SPAR-OP10-MILL-3AX | Forward spar, operation 10, 3-axis mill |
| HAND | LH | Left-hand part |
| REV | r003 | Revision 3 |
| EXT | nc | NC machine code file |

### Example: `FEM-BWQ1-CAE5710-FS-BOX-APPL-BWBQ100-0001-0999-STAT-r008.inp`

| Field | Value | Description |
|-------|-------|-------------|
| DISC | FEM | Finite Element Model |
| MIC | BWQ1 | Model Identification Code |
| DOMAIN | CAE | Computer-Aided Engineering |
| ATA | 5710 | ATA 57-10 (Wing Structure) |
| SCOPE | FS-BOX | Front spar box |
| EFFT | APPL-BWBQ100-0001-0999 | Effectivity: Aircraft BWBQ100, serials 0001-0999 |
| LIFE | STAT | Static analysis |
| REV | r008 | Revision 8 |
| EXT | inp | Abaqus input file |

## Common Patterns

### Handedness
```
-LH   # Left-hand
-RH   # Right-hand
-CEN  # Center (symmetric)
```

### Effectivity
```
-APPL-BWBQ100-0001-0999  # Applicability: Model, serial range
-E0001-0999              # Engineering: serial range
```

### Lifecycle Tags
```
-GA    # General arrangement / general assembly
-STAT  # Static analysis
-UL    # Ultimate load
-FAT   # Fatigue analysis
-DTA   # Damage tolerance analysis
-CERT  # Certification
-VNV   # Verification & Validation
-QC    # Quality control
-EOL   # End of life
```

## Invalid Examples (Will Fail Linting)

```
❌ ASSY-BWQ1-CAD571-FWD-SPAR-r001.step
   (Use 4-digit ATA: 5710, not 571)

❌ ASSY-BWQ1-CAD571010-FWD-SPAR-r001.step
   (Use short ATA: 5710, not long 571010)

❌ ASSY-BWQ1-CAD5710--FWD-SPAR-r001.step
   (No consecutive dashes in SCOPE)

❌ ASSY-BWQ1-CAD5710-fwd-spar-r001.step
   (SCOPE must be UPPERCASE)

❌ MBD-BWQ1-CAE5710-PART-r001.dat
   (MBD is CAD domain, not CAE)

❌ NC-BWQ1-CAD5710-PART-r001.nc
   (NC is CAM domain, not CAD)
```

## Usage

Test these examples with the linter:

```bash
# Create example files (empty is fine for testing)
cd tools/examples
touch ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step
touch NC-BWQ1-CAM5710-FWD-SPAR-OP10-r003.nc
touch QIP-BWQ1-CAV5710-FWD-SPAR-DIM-PLAN-r006.pdf

# Run linter
python3 ../lint_names.py .
```

## JSON Sidecar Example

Optional metadata companion file (same name + .json):

**File:** `ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step.json`

```json
{
  "dmRefs": [
    "DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml",
    "DMC-BWQ1-A-57-10-10-00A-520A-D-EN-US.xml"
  ],
  "utcsAnchor": "sha256:abc123def456...",
  "effectivity": "APPL-BWBQ100-0001-0999",
  "revision": {
    "number": "r012",
    "date": "2025-10-04",
    "author": "J. Smith",
    "description": "Updated forward spar assembly per ECN-2025-057"
  },
  "cad": {
    "software": "SolidWorks 2024",
    "units": "millimeters",
    "mass_kg": 125.6
  }
}
```

---

For more information, see [../README.md](../README.md)
