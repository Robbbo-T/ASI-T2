# ASM-008 Elevon/Flap Boxes — Technical Drawings

## Drawing Index

### Primary Views
- `BWB-Q100-ASM-008-GA-001` — General Arrangement (Control Surface Layout)
- `BWB-Q100-ASM-008-GA-002` — Installation Views (Hinge Line Configuration)
- `BWB-Q100-ASM-008-GA-003` — Actuator Integration Layout

### Structural Definition
- `BWB-Q100-ASM-008-ST-001` — Primary Structure (Spars & Ribs)
- `BWB-Q100-ASM-008-ST-002` — Hinge Bracket Details
- `BWB-Q100-ASM-008-ST-003` — Actuator Mount Details
- `BWB-Q100-ASM-008-ST-004` — Load Path Definition

### Control Surface Mapping
- `BWB-Q100-ASM-008-CS-001` — Elevon Surfaces (EL1-EL3 L/R)
- `BWB-Q100-ASM-008-CS-002` — Flap Surfaces (FLAP1-FLAP2 L/R)
- `BWB-Q100-ASM-008-CS-003` — Surface Travel Envelopes
- `BWB-Q100-ASM-008-CS-004` — Gap & Seal Requirements

### Interface Control
- `BWB-Q100-ASM-008-IC-001` — ASM-007 Trailing Edge Interface
- `BWB-Q100-ASM-008-IC-002` — ASM-009/010 Adjacent Surface Coordination
- `BWB-Q100-ASM-008-IC-003` — Systems Integration (Hydraulics/Electric)

### Manufacturing
- `BWB-Q100-ASM-008-MF-001` — Composite Layup Sequences
- `BWB-Q100-ASM-008-MF-002` — Assembly Sequence & Tooling
- `BWB-Q100-ASM-008-MF-003` — Quality Control Points

---

## Control Surface Configuration

### Elevon Surfaces
| Surface ID | Span Location | Chord % | Max Deflection | Primary Function |
|------------|---------------|---------|----------------|------------------|
| EL1_L/R | Inboard | 25% | ±25° | Pitch + Roll |
| EL2_L/R | Mid-span | 30% | ±20° | Pitch + Roll |
| EL3_L/R | Outboard | 25% | ±15° | Roll Primary |

### Flap Surfaces
| Surface ID | Span Location | Chord % | Max Deflection | Primary Function |
|------------|---------------|---------|----------------|------------------|
| FLAP1_L/R | Inboard | 40% | 0°/+35° | High Lift |
| FLAP2_L/R | Mid-span | 35% | 0°/+30° | High Lift |

---

## Standards
- **Formats:** PDF/A-1b (archival), DWG (native)
- **Units:** metric (mm)
- **Tolerance standard:** AS9100D + AMS-STD-401 (composites)
- **Coordinate frame:** Aircraft reference (X aft, Y right, Z up)
- **File naming:** `BWB-Q100-ASM-008-[TYPE]-[###]-[REV].[ext]`

## Revision Control
| Drawing | Rev | Date | ECN | Description |
|--------:|:---:|:----:|:---:|-------------|
| GA-001  |  A  | TBD  |  –  | Initial release |
| ST-001  |  A  | TBD  |  –  | Primary structure definition |
| CS-001  |  A  | TBD  |  –  | Control surface mapping |

## Dependencies & Impact
- **Requires:** ASM-007 trailing edge interface definitions
- **Config files:** [elevons.yaml](../../wing_baseline_model/control_surfaces/elevons.yaml), [flaperons.yaml](../../wing_baseline_model/control_surfaces/flaperons.yaml)
- **Drives updates to:** Flight control system interface specifications
- **QOx variables:** Hinge line optimization, actuator placement

## Folder Map
- `GA/` — General arrangements
- `ST/` — Structural definition
- `CS/` — Control surface details
- `IC/` — Interface control
- `MF/` — Manufacturing
- `drawing_register.json` — Register & revision tracking
