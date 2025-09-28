# S1000D BREX (Business Rules Exchange)

This directory contains the BREX files that define the business rules and validation criteria for the ATA-22 Auto Flight Control System S1000D data modules.

## Files

- [`DMC-BWB1-A-00-00-00-00A-022A-D-EN-US.xml`](./DMC-BWB1-A-00-00-00-00A-022A-D-EN-US.xml) — Project BREX ruleset defining validation rules for:
  - AFCS mode naming conventions (LAT ENG, VNAV, LNAV, APPR)
  - Timing determinism and partition period documentation
  - ARINC 429 label and ARINC 664 VLID mapping requirements
  - Safety margin and engagement/disengagement threshold specifications
  - UTCS/QS canonical hash embedding requirements
  - MAL-EEM ethics guard compliance markers

## Purpose

BREX files ensure consistency and quality across all ATA-22 Auto Flight data modules by enforcing project-specific rules beyond the standard S1000D schema validation. These rules are automatically applied during validation and content authoring workflows, ensuring BWB1 ModelIdentCode compliance and ARINC 653/664/429 interface standardization.