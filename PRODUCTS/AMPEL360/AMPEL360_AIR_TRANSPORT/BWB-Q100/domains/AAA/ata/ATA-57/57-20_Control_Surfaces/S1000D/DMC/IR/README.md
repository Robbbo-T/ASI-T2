# IR - Illustrated Repairs

This directory contains S1000D Illustrated Repair data modules for ATA-57-20 Control Surfaces.

## Purpose

Illustrated Repair modules provide:
- Step-by-step repair procedures with illustrations
- Repair limits and acceptability criteria
- Material and tooling requirements
- Repair templates and patterns
- Non-destructive testing requirements
- Post-repair inspection criteria

## Content Organization

IR modules follow S1000D Issue 6.0 naming conventions:
- DMC-BWB-Q100-A-57-20-XX-XXX-520A-D-EN-US.xml

Where:
- **520A** = Repair information code
- **D** = Descriptive content type
- **EN-US** = English (US) language

## Repair Categories

### Standard Repairs
- **IR-001**: Control surface skin repairs (scarf patches)
- **IR-002**: Core replacement repairs
- **IR-003**: Hinge fitting repairs
- **IR-004**: Balance weight attachment repairs
- **IR-005**: Edge seal repairs

### Damage Assessment
- **IR-010**: Damage assessment procedures
- **IR-011**: Repair vs. replace decision criteria
- **IR-012**: Temporary repair procedures

### Post-Repair Actions
- **IR-020**: NDT inspection procedures (UT, RT, thermography)
- **IR-021**: Post-repair acceptance testing
- **IR-022**: Return to service criteria

## Repair Standards

All repairs must:
- Follow ATA-20 standard practices
- Use approved materials and processes
- Meet structural acceptance criteria (CO-3.13)
- Include proper documentation and sign-off
- Reference applicable engineering orders

## Links to ATA-20 Forms

Mandatory forms for repairs:
- **FORM-QA-20-10-01**: Composite Fastening
- **FORM-QA-20-10-02**: Adhesive Bonding
- **FORM-QA-20-50-01**: Surface Finish & Aerodynamic Smoothness

See: `../../../../20/20-10_Structural_Practices/forms/`

## Validation

All IR modules must:
- Validate against S1000D 6.0 schema
- Comply with BREX rules (../BREX/BREX.xml)
- Include proper warnings and cautions
- Reference correct tool and material specifications
- Include effectivity and applicability

## Related Directories

- **PR/** - Procedural data modules (general procedures)
- **DS/** - Descriptive data modules
- **IPD/** - Illustrated parts data
- **../../evidence/** - Repair test evidence

---
*Part of ATA-57-20 Control Surfaces S1000D documentation.*
