# Forward Spar CAx Integration Guide

## Overview

This directory is designated for CAD models, CAM programs, and CAV measurement plans related to the Forward Spar assembly (ATA 57-10-10) of the AMPEL360 BWB-Q100 wing.

## File Naming Conventions

### CAD (Computer-Aided Design)

Part files should follow this pattern:
```
PRT-BWQ1-CAD5710-<COMPONENT>-<VARIANT>-r<REV>.sldprt
ASM-BWQ1-CAD5710-<ASSEMBLY>-r<REV>.sldasm
```

**Examples:**
- `PRT-BWQ1-CAD5710-UPPER-CAP-LH-r001.sldprt` - Left-hand upper cap part
- `PRT-BWQ1-CAD5710-UPPER-CAP-RH-r001.sldprt` - Right-hand upper cap part
- `PRT-BWQ1-CAD5710-WEB-PANEL-INB-r001.sldprt` - Inboard web panel
- `PRT-BWQ1-CAD5710-WEB-PANEL-MID-r001.sldprt` - Mid section web panel
- `PRT-BWQ1-CAD5710-WEB-PANEL-OUTB-r001.sldprt` - Outboard web panel
- `PRT-BWQ1-CAD5710-RIB-IFACE-FITTING-r001.sldprt` - Rib interface fitting
- `ASM-BWQ1-CAD5710-SPLICE-KIT-BL160-r001.sldasm` - Splice kit assembly at BL160
- `ASM-BWQ1-CAD5710-SPAR-INBOARD-r001.sldasm` - Complete inboard spar assembly

**Variant Codes:**
- `LH` / `RH` - Left-hand / Right-hand
- `INB` - Inboard (BL0-BL160)
- `MID` - Mid section (BL160-BL320)
- `OUTB` - Outboard (BL240-BL400)

### CAM (Computer-Aided Manufacturing)

CNC programs should follow this pattern:
```
NC-BWQ1-CAM5710-<ZONE>-<COMPONENT>-OP<NN>-<OPERATION>-r<REV>.nc
TOOL-BWQ1-CAM5710-<COMPONENT>-<TYPE>-LIST-r<REV>.csv
```

**Examples:**
- `NC-BWQ1-CAM5710-INB-CAP-OP10-MILL-r001.nc` - Inboard cap milling operation 10
- `NC-BWQ1-CAM5710-MID-SPLICE-OP30-DRILL-r001.nc` - Mid splice drilling operation 30
- `NC-BWQ1-CAM5710-OUTB-WEB-OP20-TRIM-r001.nc` - Outboard web trimming operation 20
- `TOOL-BWQ1-CAM5710-FITTING-MILL-LIST-r001.csv` - Tool list for fitting milling

**Operation Codes:**
- `OP10` - Rough machining
- `OP20` - Trim/profile operations
- `OP30` - Hole drilling
- `OP40` - Deburring/finishing

**Operation Types:**
- `MILL` - Milling operations
- `DRILL` - Drilling operations
- `TRIM` - Trimming/profiling
- `BORE` - Boring operations
- `TAP` - Tapping operations

### CAV (Computer-Aided Verification)

Measurement programs and reports should follow this pattern:
```
DMIS-BWQ1-CAV5710-<ZONE>-DIM-<STAGE>-OP<NN>-r<REV>.dmis
MEAS-BWQ1-CAV5710-<ZONE>-<TYPE>-RESULTS-r<REV>.csv
```

**Examples:**
- `DMIS-BWQ1-CAV5710-INBD-DIM-IP-OP10-r001.dmis` - In-process measurement after operation 10
- `DMIS-BWQ1-CAV5710-MID-DIM-OP20-r001.dmis` - Mid section measurement after operation 20
- `MEAS-BWQ1-CAV5710-INBD-DIM-RESULTS-r001.csv` - Inboard dimensional results
- `MEAS-BWQ1-CAV5710-OUTB-CMM-REPORT-r001.pdf` - Outboard CMM measurement report

**Measurement Stages:**
- `IP` - In-process (during manufacturing)
- `FI` - Final inspection
- `AS` - As-built survey

## Metadata Requirements

Each CAx file **must** have an accompanying JSON metadata file:

```
<filename>.meta.json
```

### Metadata Schema

```json
{
  "$schema": "../../../contracts/schemas/cax_manifest.schema.json",
  "id": "BWQ1-CAD-57-10-1001-01",
  "vehicle": "AMPEL360_BWB-Q100",
  "ata_chapter": "57-10-10",
  "part_number": "57-10-1001-01",
  "description": "Upper Cap Assembly, Al-Li",
  "revision": "001",
  "file_type": "CAD",
  "format": "SLDPRT",
  "created": "2025-10-04T00:00:00Z",
  "author": "Engineering",
  "dmRefs": [
    "DMC-BWQ1-A-57-10-10-01-00A-941A-D-EN-US.xml",
    "DMC-BWQ1-A-57-10-10-00-00A-040A-D-EN-US.xml"
  ],
  "utcs": {
    "canonical_hash": "sha256:TBD",
    "provenance": "ASIT-BWQ1-AAA-CAX-CAD-5710-0001",
    "operator_id": "UTCS:OP:engineering-team"
  },
  "effectivity": {
    "aircraft_series": "BWB-Q100",
    "msn_from": "001",
    "config": "Standard"
  },
  "material": {
    "specification": "AA2198-T8",
    "type": "Aluminum-Lithium Alloy"
  },
  "geometry": {
    "units": "mm",
    "coordinate_system": "BWB-Q100-MASTER",
    "bounding_box": {
      "min": [0, 0, 0],
      "max": [1000, 200, 100]
    }
  }
}
```

## Part Number to CAD File Mapping

Based on the IPD (DMC-BWQ1-A-57-10-10-0x-00A-941A-D-EN-US.xml):

### Inboard Section (BL0-BL160)

| Part Number | Description | CAD File |
| ----------- | ----------- | -------- |
| 57-10-1001-01 | Upper Cap Assembly, Al-Li | PRT-BWQ1-CAD5710-UPPER-CAP-INB-r001.sldprt |
| 57-10-1001-02 | Lower Cap Assembly, Al-Li | PRT-BWQ1-CAD5710-LOWER-CAP-INB-r001.sldprt |
| 57-10-1002-01 | Web Panel, Stiffened (BL0-BL80) | PRT-BWQ1-CAD5710-WEB-PANEL-BL0-80-r001.sldprt |
| 57-10-1002-02 | Web Panel, Stiffened (BL80-BL160) | PRT-BWQ1-CAD5710-WEB-PANEL-BL80-160-r001.sldprt |
| 57-10-1003-01 | Rib Interface Fitting (Ti-6Al-4V) | PRT-BWQ1-CAD5710-RIB-IFACE-FITTING-r001.sldprt |

### Mid Section (BL160-BL320)

| Part Number | Description | CAD File |
| ----------- | ----------- | -------- |
| 57-10-2001-01 | Upper Cap, CFRP (BL160-BL240) | PRT-BWQ1-CAD5710-UPPER-CAP-MID-r001.sldprt |
| 57-10-2001-02 | Lower Cap, CFRP (BL160-BL240) | PRT-BWQ1-CAD5710-LOWER-CAP-MID-r001.sldprt |
| 57-10-2002-01 | Web Panel, CFRP Laminate | PRT-BWQ1-CAD5710-WEB-PANEL-MID-r001.sldprt |
| 57-10-2003-01 | Lightening Hole Grommet | PRT-BWQ1-CAD5710-GROMMET-r001.sldprt |
| SK-57-2101 | Inboard/Mid Splice Kit (BL160) | ASM-BWQ1-CAD5710-SPLICE-KIT-BL160-r001.sldasm |
| SK-57-2201 | Mid/Outboard Splice Kit (BL240) | ASM-BWQ1-CAD5710-SPLICE-KIT-BL240-r001.sldasm |

### Outboard Section (BL240-BL400)

| Part Number | Description | CAD File |
| ----------- | ----------- | -------- |
| 57-10-3001-01 | Upper Cap, CFRP UD (BL240-BL400) | PRT-BWQ1-CAD5710-UPPER-CAP-OUTB-r001.sldprt |
| 57-10-3001-02 | Lower Cap, CFRP UD (BL240-BL400) | PRT-BWQ1-CAD5710-LOWER-CAP-OUTB-r001.sldprt |
| 57-10-3002-01 | Web Panel, Reduced Thickness | PRT-BWQ1-CAD5710-WEB-PANEL-OUTB-r001.sldprt |
| 57-10-3002-02 | Web Stringers, Co-cured | PRT-BWQ1-CAD5710-WEB-STRINGERS-r001.sldprt |
| 57-10-3101-01 | Tip Rib Closure Fitting | PRT-BWQ1-CAD5710-TIP-RIB-CLOSURE-r001.sldprt |
| 57-10-3102-01 | Tip Fairing Bracket | PRT-BWQ1-CAD5710-TIP-FAIRING-BRACKET-r001.sldprt |
| 57-10-3103-01 | Navigation Light Mount (Ti) | PRT-BWQ1-CAD5710-NAV-LIGHT-MOUNT-r001.sldprt |
| 57-10-3201-01 | Aileron Hinge Fitting, Outboard | PRT-BWQ1-CAD5710-AILERON-HINGE-FITTING-r001.sldprt |
| 57-10-3201-02 | Hinge Pin, CRES | PRT-BWQ1-CAD5710-HINGE-PIN-r001.sldprt |
| 57-10-3201-03 | Actuator Hardpoint Fitting | PRT-BWQ1-CAD5710-ACTUATOR-HARDPOINT-r001.sldprt |

## Assembly Structure

```
ASM-BWQ1-CAD5710-SPAR-COMPLETE-r001.sldasm
├── ASM-BWQ1-CAD5710-SPAR-INBOARD-r001.sldasm
│   ├── PRT-BWQ1-CAD5710-UPPER-CAP-INB-r001.sldprt
│   ├── PRT-BWQ1-CAD5710-LOWER-CAP-INB-r001.sldprt
│   ├── PRT-BWQ1-CAD5710-WEB-PANEL-BL0-80-r001.sldprt (x4)
│   ├── PRT-BWQ1-CAD5710-WEB-PANEL-BL80-160-r001.sldprt (x4)
│   └── PRT-BWQ1-CAD5710-RIB-IFACE-FITTING-r001.sldprt (x8)
├── ASM-BWQ1-CAD5710-SPLICE-KIT-BL160-r001.sldasm
├── ASM-BWQ1-CAD5710-SPAR-MID-r001.sldasm
│   ├── PRT-BWQ1-CAD5710-UPPER-CAP-MID-r001.sldprt
│   ├── PRT-BWQ1-CAD5710-LOWER-CAP-MID-r001.sldprt
│   ├── PRT-BWQ1-CAD5710-WEB-PANEL-MID-r001.sldprt (x6)
│   └── PRT-BWQ1-CAD5710-GROMMET-r001.sldprt (x24)
├── ASM-BWQ1-CAD5710-SPLICE-KIT-BL240-r001.sldasm
└── ASM-BWQ1-CAD5710-SPAR-OUTBOARD-r001.sldasm
    ├── PRT-BWQ1-CAD5710-UPPER-CAP-OUTB-r001.sldprt
    ├── PRT-BWQ1-CAD5710-LOWER-CAP-OUTB-r001.sldprt
    ├── PRT-BWQ1-CAD5710-WEB-PANEL-OUTB-r001.sldprt (x8)
    ├── PRT-BWQ1-CAD5710-WEB-STRINGERS-r001.sldprt (x16)
    └── [Tip fittings and hinge components]
```

## Integration with S1000D IPD

All CAD files reference the corresponding S1000D IPD data modules:

- **Master IPD**: `DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml`
- **Inboard IPD**: `DMC-BWQ1-A-57-10-10-01-00A-941A-D-EN-US.xml`
- **Mid IPD**: `DMC-BWQ1-A-57-10-10-02-00A-941A-D-EN-US.xml`
- **Outboard IPD**: `DMC-BWQ1-A-57-10-10-03-00A-941A-D-EN-US.xml`

References should be included in the `dmRefs` array of each metadata file.

## Quality Assurance

All CAx files must:

1. ✅ Follow the naming convention documented above
2. ✅ Include accompanying `.meta.json` metadata file
3. ✅ Reference appropriate S1000D data modules
4. ✅ Include UTCS provenance information
5. ✅ Specify effectivity (MSN ranges, configurations)
6. ✅ Define material specifications and properties
7. ✅ Use correct coordinate system (BWB-Q100-MASTER)
8. ✅ Include version/revision tracking

## Export Formats

CAD models should be exported in the following formats for downstream use:

- **STEP** (`.step`, `.stp`) - Primary neutral format for interoperability
- **IGES** (`.iges`, `.igs`) - Legacy format for older systems
- **Parasolid** (`.x_t`) - For high-fidelity transfer
- **STL** (`.stl`) - For visualization and rapid prototyping

Export settings:
- Units: millimeters (mm)
- Coordinate system: BWB-Q100-MASTER
- Assembly structure: Preserve (do not flatten)

## Related Documentation

- **IPD Summary**: `../../../ata/ATA-57/57-10_Wing_Primary_Structure/S1000D/data_modules/ipd/57-10-10_Forward_Spar/IMPLEMENTATION_SUMMARY.md`
- **BOM CSV**: `../../../ata/ATA-57/57-10_Wing_Primary_Structure/S1000D/data_modules/ipd/57-10-10_Forward_Spar/data/forward_spar_bom.csv`
- **Descriptive Modules**: `../../../ata/ATA-57/57-10_Wing_Primary_Structure/S1000D/data_modules/descriptive/57-10-10_Forward_Spar/`

---

*Document version: 1.0*  
*Last updated: 2025-10-04*  
*Part of AMPEL360 BWB-Q100 CAx Integration Documentation*
