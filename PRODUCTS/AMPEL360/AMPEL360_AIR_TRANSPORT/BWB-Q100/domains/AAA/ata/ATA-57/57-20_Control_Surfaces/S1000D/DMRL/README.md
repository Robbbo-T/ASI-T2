# DMRL (Data Module Requirements List)

This directory contains the DMRL for ATA-57-20 Control Surfaces.

## DMRL.xml

The Data Module Requirements List (`DMRL-57-20-001`) is a comprehensive, CSDB-friendly specification that defines all required data modules for the BWB-Q100 control surfaces system.

### Structure

The DMRL includes:

1. **Identification Section**
   - DMRL Number: `DMRL-57-20-001`
   - Title: ATA-57-20 Control Surfaces — DMRL (slim)
   - Issue: 001/00

2. **Effectivity Shells** (reusable applicability definitions)
   - `BWB-Q100-ALL`: All MSNs (001-999)
   - `BWB-Q100-BLOCK-001-050`: Block 001–050
   - `BWB-Q100-BLOCK-051-999`: Block 051–999
   - `OPT-HS`: High-speed option
   - `OPT-ICE`: Ice-protection option
   - `SIDE-LH` / `SIDE-RH`: Left/Right-hand sides

3. **Data Module Requirements** (26 total requirements)
   - **System level (57-20-00)**: 5 DMs covering general descriptions, inspections, and IPD
   - **Elevons (57-20-10)**: 5 DMs for descriptions, inspections, repair, R/I, and IPD
   - **Flaperons (57-20-20)**: 5 DMs for descriptions, inspections, repair, R/I, and IPD
   - **Spoilers (57-20-30)**: 5 DMs for descriptions, inspections, repair, R/I, and IPD
   - **Tabs (57-20-40)**: 6 DMs for descriptions, inspections, balance, R/I, and IPD

### Information Codes

- **040A**: Descriptive Information
- **520A**: Procedural - Inspection/Repair Procedures
- **720A**: Procedural - Removal/Installation Procedures
- **941A**: Illustrated Parts Data (IPD)

### Requirement Status

- **required**: Core descriptions, inspections, removal/installation, and IPD modules
- **optional**: Detailed repair procedures (marked as optional to accommodate MRB policy variations)

### DMC Format

All Data Module Codes (DMCs) follow the S1000D standard with fully 2-digit fields:
- Model: `BWQ1`
- System: `57` (Structures)
- SubSystem: `20` (Control Surfaces)
- SubSubSystem: `00/10/20/30/40` (System level / Elevons / Flaperons / Spoilers / Tabs)

## Usage

The DMRL serves as:
- The authoritative master list of all required technical documentation for control surfaces
- A guide for the authoring process and content planning
- A reference for applicability and effectivity management
- A foundation for configuration management and delivery planning

### Effectivity Management

The reusable effectivity shells allow for flexible applicability assignment:
- Currently, all DMs apply to `BWB-Q100-ALL` (all MSNs)
- The shells can be swapped or composed with `AND/OR` logic as variants solidify
- Options and block splits are ready for activation when needed

## Related Documents

- [Data Modules](../DMC/) - Actual data module implementations
- [BREX Rules](../BREX/) - Business rules for validation
- [Main README](../../README.md) - ATA-57-20 overview
