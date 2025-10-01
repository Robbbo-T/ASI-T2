# S1000D Data Modules - ATA-57-10 Wing Primary Structure

This directory contains all S1000D Issue 6.0 data modules for the BWB-Q100 Wing Primary Structure (ATA-57-10).

## Organization

Data modules are organized by content type and component:

### Descriptive (`descriptive/`)
Technical descriptions, specifications, and design information for wing structural components:
- **57-10-10** Forward Spar
- **57-10-20** Rear Spar
- **57-10-30** Ribs
- **57-10-40** Skin Panels
- **57-10-50** Stringers
- **57-10-60** Attachments

### Procedural (`procedural/`)
Step-by-step procedures organized by task type:
- **inspection/** - Visual and NDT inspection procedures
- **removal_installation/** - R/I procedures for maintenance
- **repair/** - Standard repair procedures

### Illustrated Parts Data (`ipd/`)
Parts identification, illustrated breakdowns, and item-level data for all components.

## Data Module Coding

S1000D data module codes follow the pattern:
```
DMC-BWQ1-A-57-10-XX-YY-ZZA-IIIIA-D-EN-US.xml
```

Where:
- **BWQ1** = BWB-Q100 Model Identifier
- **A** = System Difference Code
- **57-10-XX** = ATA Chapter/Subchapter/Section
- **YY-ZZA** = Assembly/Disassembly/Item
- **IIIIA** = Information Code (040A=Descriptive, 520A=Inspection, 720A=R/I, 941A=IPD)
- **D** = Content Type
- **EN-US** = English (US)

## Information Codes

- **040A** - Descriptive information (technical descriptions, specifications)
- **520A** - Inspection/Check procedures (visual, NDT, acceptance criteria)
- **720A** - Removal/Installation procedures (R/I tasks)
- **941A** - Illustrated Parts Data (IPD figures, part numbers)

## DMRL Compliance

All data modules are defined in the Data Module Requirements List (DMRL):
- Location: `../DMRL/DMRL.xml`
- Each DM must be listed in the DMRL before creation
- DMRL defines module requirements, applicability, and relationships

## BREX Validation

All data modules must validate against Business Rules Exchange (BREX):
- Location: `../BREX/BREX.xml`
- Defines project-specific validation rules
- All DMs must pass BREX validation before release

## 360IPCirq Integration

Removal/Installation (720A) data modules are designed for reusability:
- Item keys match IPD (941A) module references
- Enables "removal for repair → IPC 360 reusability"
- Mapping keys defined in `../../contracts/ICD-AAA-ATA-57-10.md`

## Quality Standards

All data modules must:
- Reference applicable ATA-20 standard practices
- Link to acceptance criteria in `../../contracts/schemas/acceptance.metric.schema.json`
- Include traceability to evidence in `../../evidence/`
- Comply with effectivity rules and configuration control

## Change Control

Data module changes require:
- Update to DMRL if adding/removing modules
- BREX validation
- Configuration management approval
- QS sealing for baseline releases

---

*Part of ATA-57-10 Wing Primary Structure — Configuration controlled under UTCS/QS v5.0*
