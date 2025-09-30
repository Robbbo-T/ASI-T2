# S1000D Data Modules

This directory contains S1000D Issue 6.0 compliant data modules for the AFDX bus implementation.

## Purpose

Data modules (DMs) provide structured technical documentation following the S1000D specification. Each DM is uniquely identified by a Data Module Code (DMC) and contains specific technical information.

## Contents

| DMC | Type | Description | Status |
|-----|------|-------------|--------|
| `DMC-Q100-A-42-70-00-00A-010A-D-EN-US.xml` | Descriptive | General AFDX description | ✅ Created |
| `DMC-Q100-A-42-71-00-00A-010A-D-EN-US.xml` | Descriptive | AFDX network architecture | 📝 Planned |
| `DMC-Q100-A-42-72-00-00A-012A-D-EN-US.xml` | Descriptive | Virtual Links configuration | 📝 Planned |
| `DMC-Q100-A-42-73-00-00A-030A-D-EN-US.xml` | Descriptive | AFDX security implementation | 📝 Planned |
| `DMC-Q100-A-42-74-00-00A-020A-P-EN-US.xml` | Procedural | AFDX integration procedures | 📝 Planned |
| `DMC-Q100-A-42-75-00-00A-020A-P-EN-US.xml` | Procedural | AFDX test procedures | 📝 Planned |
| `DMC-Q100-A-42-79-00-00A-022A-D-EN-US.xml` | Descriptive | AFDX compliance documentation | 📝 Planned |

## DMC Structure

The Data Module Code follows S1000D naming conventions:
- **Model ID**: Q100 (BWB-Q100 aircraft)
- **System Diff**: A
- **System Code**: 42 (ATA-42 Integrated Modular Avionics)
- **Sub-system**: 7 (AFDX bus)
- **Info Code**: Varies by DM type
- **Language**: EN-US (English, United States)

## XML Structure

Each data module includes:
- **identAndStatusSection**: DM identification and status information
- **content**: Technical content (description or procedure)
- References to BREX rules, applicability, and security classification

## Validation

Data modules must be validated against:
- S1000D Issue 6.0 schemas (see [../schemas/6.0/](../schemas/6.0/))
- BREX rules (see [../brex/](../brex/))
- DMRL requirements (see [../dmrl/](../dmrl/))

Use the validation target:
```bash
make validate-s1000d
```

## Related Files

- Parent Documentation: [../../README.md](../../README.md)
- Schemas: [../schemas/6.0/](../schemas/6.0/)
- BREX: [../brex/](../brex/)
- Figures: [../figures/](../figures/)
