# Procedural Data Modules - Wing Primary Structure

This directory contains S1000D procedural data modules providing step-by-step instructions for inspection, removal/installation, and repair of wing primary structure components.

## Organization

### Inspection (`inspection/`)
Visual and NDT inspection procedures (Info Code 520A):
- Visual inspection criteria and methods
- Non-destructive testing (NDT) procedures
- Inspection intervals and scheduling
- Acceptance criteria and discrepancy limits
- Special inspection tools and equipment

### Removal/Installation (`removal_installation/`)
Maintenance procedures (Info Code 720A):
- Component removal procedures
- Installation and assembly procedures
- Torque specifications and sequences
- Tooling requirements
- Safety precautions
- Special processes (fuel draining, sealing)

### Repair (`repair/`)
Standard repair procedures (Info Code 520A):
- Damage assessment criteria
- Allowable damage limits
- Standard repair schemes
- Doubler and patch installations
- Composite repair procedures
- Post-repair inspection requirements

## Component Coverage

Procedural modules are organized by component:
- **57-10-10** Forward Spar
- **57-10-20** Rear Spar
- **57-10-30** Ribs
- **57-10-40** Skin Panels
- **57-10-50** Stringers
- **57-10-60** Attachments

## Information Codes

- **520A** - Inspection/Check procedures and standard repairs
- **720A** - Removal/Installation procedures

## 360IPCirq Integration

R/I procedures (720A) are designed for IPC reusability:
- Item keys align with IPD (941A) part references
- Tool numbers match IPD tool callouts
- Consumable items (sealants, fasteners) reference IPD part numbers
- Enables "removal for repair → IPC 360 reusability" workflow

## ATA-20 Integration

All procedures reference applicable ATA-20 standard practices:
- Composite fastening techniques
- Adhesive bonding processes
- Sealing procedures
- Material handling (out-of-time/temperature)
- Electrical bonding verification
- Torque specifications

## Quality Requirements

Procedures must include:
- Prerequisites and precautions
- Required tools and equipment
- Consumable materials with part numbers
- Step-by-step instructions with graphics
- Quality checkpoints and witness points
- Sign-off requirements
- Links to applicable forms (ATA-20)
- Evidence capture requirements

## Validation Requirements

All procedural modules must:
- Validate against S1000D 6.0 proced.xsd schema
- Comply with BREX rules (../../BREX/BREX.xml)
- Reference correct tool and part numbers from IPD
- Include proper warnings and cautions
- Link to acceptance criteria in contracts/schemas

## Cross-References

Procedures should reference:
- **Descriptive modules** (../descriptive/) for component details
- **IPD modules** (../ipd/) for part identification
- **ATA-20 forms** for quality documentation
- **Evidence indexes** (../../../evidence/) for traceability

## Change Control

Procedure changes require:
- Technical review and validation
- Safety assessment
- Update to DMRL if adding new procedures
- Configuration management approval
- Training material updates

---

*Part of ATA-57-10 S1000D documentation — Controlled under DMRL*
