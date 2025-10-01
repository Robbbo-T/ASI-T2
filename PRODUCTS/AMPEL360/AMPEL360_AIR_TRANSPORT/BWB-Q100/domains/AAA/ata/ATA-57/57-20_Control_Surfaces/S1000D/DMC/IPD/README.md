# IPD - Illustrated Parts Data

This directory contains S1000D Illustrated Parts Data (IPD) modules for ATA-57-20 Control Surfaces.

## Purpose

Illustrated Parts Data modules provide:
- Exploded view illustrations of control surface assemblies
- Parts lists and nomenclature
- Part numbers and descriptions
- Quantity per assembly information
- Interchangeability data
- Effectivity and applicability

## Content Organization

IPD modules follow S1000D Issue 6.0 naming conventions:
- DMC-BWB-Q100-A-57-20-XX-XXX-941A-D-EN-US.xml

Where:
- **941A** = Illustrated parts breakdown information code
- **D** = Descriptive content type
- **EN-US** = English (US) language

## IPD Coverage

- **IPD-001**: Elevon assembly breakdown
- **IPD-002**: Flaperon assembly breakdown
- **IPD-003**: Spoiler assembly breakdown
- **IPD-004**: Hinge assembly breakdown
- **IPD-005**: Actuator attachment breakdown
- **IPD-006**: Balance weight assembly breakdown

## Integration with ATA-04

IPD modules support:
- 360IPCirq interchangeability queries
- Spare parts provisioning
- Parts catalog generation
- Maintenance planning

## Illustration Standards

All illustrations must:
- Follow ATA iSpec 2200 standards
- Use consistent view angles and scales
- Include callout numbers matching parts lists
- Show assembly relationships clearly
- Include revision status

## Validation

All IPD modules must:
- Validate against S1000D 6.0 schema
- Comply with BREX rules (../BREX/BREX.xml)
- Cross-reference correct part numbers
- Include proper effectivity data

## Related Directories

- **DS/** - Descriptive data modules
- **PR/** - Procedural data modules
- **IR/** - Illustrated repairs
- **../../contracts/schemas/** - Part data schemas

---
*Part of ATA-57-20 Control Surfaces S1000D documentation.*
