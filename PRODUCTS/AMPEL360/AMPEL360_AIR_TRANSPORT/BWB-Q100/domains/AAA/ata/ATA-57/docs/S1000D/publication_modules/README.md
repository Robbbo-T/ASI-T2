# Publication Modules

- **DMRL:** [`DML-BWQ1-ATA57-00_EN-US.xml`](./DML-BWQ1-ATA57-00_EN-US.xml)
- **Publication Module (PM):** [`PMC-BWQ1-ATA57-00_001-00_EN-US.xml`](./PMC-BWQ1-ATA57-00_001-00_EN-US.xml)
- **BREX (to add):** `BREX-BWQ1-AAA.xml`

**Workflow**
1) Update DMRL for scope changes.
2) Author/maintain DMs under `data_modules/`.
3) Build PM with the latest indices.

## Purpose

Publication modules control:
- Document structure and organization
- Data module sequencing
- Publication formatting
- Cross-reference management

## Current Publications

### ATA-57 Wings Technical Publication
- **DMRL**: Defines all required data modules for ATA-57 Wings
- **PM**: Organizes modules into complete technical publication
- **Scope**: Complete wing system documentation including:
  - Wing structure (57-10)
  - Flight controls (57-20, 57-30, 57-40)
  - Control surfaces (57-50)

## Integration

Publication modules reference data modules from:
- `../data_modules/descriptive/` - Technical descriptions
- `../data_modules/procedural/` - Maintenance procedures  
- `../data_modules/fault/` - Fault isolation
- `../data_modules/ipd/` - Illustrated parts data

Publication outputs integrate with ASI-T2 systems for traceability and quality control.

## BREX Integration

When BREX module is added:
- Reference in DMRL and PM
- Define business rules for:
  - Information code usage (042/052 restrictions)
  - Classification requirements
  - Content validation rules