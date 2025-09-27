# Data Module Requirements List (DMRL)

This directory contains the DMRL files that define the complete inventory of data modules required for the ATA-22 Auto Flight Control System.

## Files

- [`DMRL-BWB1-A-22-00-00-00A-001A-D-EN-US.xml`](./DMRL-BWB1-A-22-00-00-00A-001A-D-EN-US.xml) — Data Module Requirements List defining all required data modules with their:
  - DMC (Data Module Code) identifiers using BWB1 ModelIdentCode
  - ATA-22 subsystem coverage (22-10 through 22-90)
  - Information codes: 040 (descriptive), 720/721 (procedural), 940 (fault isolation)
  - Language specifications (EN-US primary, ES mirrors)
  - Status and baseline information
  - Cross-reference relationships with INFRANET/AQUA_OS_AIRCRAFT components

## Purpose

The DMRL serves as the authoritative inventory of all data modules in the ATA-22 Auto Flight chapter, ensuring complete coverage of AFCS requirements and enabling automated validation of content completeness. It supports:

- AFCS project planning and work breakdown (AP, FD, A/T, BITE)
- Content gap analysis and tracking for S1000D Issue 6.0 compliance
- Automated validation of DM coverage against BWB1 requirements
- Integration with authoring and UTCS/QS evidence chain tools
- ARINC 653 partition manifest traceability