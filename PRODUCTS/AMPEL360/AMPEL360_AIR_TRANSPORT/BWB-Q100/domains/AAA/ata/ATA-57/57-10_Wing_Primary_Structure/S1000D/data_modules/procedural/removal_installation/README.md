# Removal/Installation Procedures - Wing Primary Structure

This directory contains S1000D removal and installation procedural data modules (Info Code 720A) for wing primary structure components.

## Purpose

R/I procedures provide step-by-step instructions for:
- Safe removal of components for inspection, repair, or replacement
- Proper installation and assembly
- Required tooling and equipment
- Torque specifications and sequences
- Sealing and bonding processes
- Fuel system precautions
- Quality verification and sign-off

## 360IPCirq Integration

R/I procedures are designed for IPC reusability:
- **Item keys** match IPD (941A) part references exactly
- **Tool callouts** reference IPD tool items
- **Consumables** (fasteners, sealants, shims) use IPD part numbers
- **Removal kits** are defined with same structure as IPC spares packages
- Enables "removal for repair → IPC 360 reusability" workflow

## Component Coverage

### 57-10-10 Forward Spar
R/I procedures cover:
- Inboard, mid, and outboard section removal
- Cap removal (with stringer detachment considerations)
- Web section access
- Fuel drain requirements before removal
- Fastener removal sequence
- Installation torque sequences
- Fuel seal application

### 57-10-20 Rear Spar
R/I procedures cover:
- Section removal (with hinge/actuator detachment)
- Landing gear beam support during spar removal
- Heavy lift procedures for inboard sections
- Control surface disconnection
- Installation alignment procedures

### 57-10-40 Skin Panels
R/I procedures cover:
- Panel removal (fastener sequence, joggle handling)
- Sealing removal and surface preparation
- Panel installation and alignment
- Torque application sequence
- Fuel tank sealant application
- Lightning protection bonding verification
- Leak test requirements

## Procedure Structure

Each R/I procedure includes:

### Prerequisites
- Aircraft configuration requirements
- System safeing (fuel, hydraulic, electrical)
- Access panel removal
- Support equipment setup

### Removal Sequence
1. Disconnections (systems, adjacent structure)
2. Fastener removal sequence
3. Sealant/bond breaking
4. Component extraction
5. Tagging and storage

### Installation Sequence
1. Surface preparation and inspection
2. Sealant/adhesive application
3. Component positioning and alignment
4. Fastener installation (sequence critical)
5. Torque application (values and sequence)
6. Quality verification
7. System reconnections
8. Functional checks

### Special Processes
- Fuel system draining and venting
- Sealant curing requirements
- Bondline thickness control
- Torque verification sampling
- Leak testing

## Tooling Requirements

Procedures specify:
- Special tools (part numbers from IPD)
- Standard tools (torque wrenches, drill motors)
- Support equipment (jacks, fixtures, lifting gear)
- Calibration requirements

## Consumables

All consumables referenced by IPD part number:
- Fasteners (with grip length selection)
- Sealants (with shelf life and OOC tracking)
- Adhesives (with mixing and pot life)
- Shims (thickness selection)
- Cleaning solvents
- Protective coatings

## Quality Checkpoints

R/I procedures include witness points for:
- Surface preparation verification
- Sealant/adhesive application
- Fastener installation
- Torque verification
- Bonding resistance measurement
- Leak test (for fuel tank areas)

## ATA-20 Form References

- **FORM-QA-20-10-01**: Composite Fastening (torque, hole inspection)
- **FORM-QA-20-10-02**: Adhesive Bonding (surface prep, cure)
- **FORM-QA-20-20-01**: Leak Test (fuel tank integrity)
- **FORM-QA-20-30-01**: Material Handling/OOC (sealants, adhesives)
- **FORM-QA-20-40-01**: EMI Continuity (lightning bonding)

## Safety Precautions

All procedures include:
- Hazard warnings (fuel vapors, heavy lifts, pinch points)
- Personal protective equipment requirements
- Fire safety for fuel system work
- Load-bearing structure safeing
- Tool/equipment safety

## References

- **Descriptive modules**: `../../descriptive/` for component details
- **IPD modules**: `../../ipd/` for part identification
- **Schemas**: `../../../../contracts/schemas/fastener.set.schema.json`, `joint.schema.json`
- **Evidence**: `../../../../evidence/` for OOC logs, torque records

---

*Part of ATA-57-10 procedural documentation*
