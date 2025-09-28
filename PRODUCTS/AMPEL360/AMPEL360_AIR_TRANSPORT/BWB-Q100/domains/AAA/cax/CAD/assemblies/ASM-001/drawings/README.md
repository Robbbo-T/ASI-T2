# ASM-001 OML Master Surface — Technical Drawings

## Drawing Index

### Primary Views
- `BWB-Q100-ASM-001-GA-001` — General Arrangement (3-view)
- `BWB-Q100-ASM-001-GA-002` — Isometric Views
- `BWB-Q100-ASM-001-GA-003` — Station Reference Grid

### Surface Definition
- `BWB-Q100-ASM-001-SD-001` — Loft Sections (STA 0–2000)
- `BWB-Q100-ASM-001-SD-002` — Loft Sections (STA 2000–4000)
- `BWB-Q100-ASM-001-SD-003` — Planform & Twist Distribution
- `BWB-Q100-ASM-001-SD-004` — Blend Region Geometry

### Interface Control
- `BWB-Q100-ASM-001-IC-001` — ASM-002/003/004 Join Lines
- `BWB-Q100-ASM-001-IC-002` — Control Surface Cutouts
- `BWB-Q100-ASM-001-IC-003` — Systems Penetrations

### Manufacturing
- `BWB-Q100-ASM-001-MF-001` — Surface Tolerance Map
- `BWB-Q100-ASM-001-MF-002` — Tooling Reference Points

---

## Standards
- **Formats:** PDF/A-1b (archival), DWG (native)
- **Units:** metric (mm)
- **Tolerance standard:** AS9100D
- **Coordinate frame:** Aircraft reference (X aft, Y right, Z up)
- **File naming:** `BWB-Q100-ASM-001-[TYPE]-[###]-[REV].[ext]` (ex: `BWB-Q100-ASM-001-GA-001-A.pdf`)

## Revision Control
| Drawing | Rev | Date | ECN | Description |
|--------:|:---:|:----:|:---:|-------------|
| GA-001  |  A  | TBD  |  –  | Initial release |

## Dependencies & Impact
- **Requires:** Station grid from `domains/AAA/references/`
- **Drives updates to:** ASM-002 … ASM-032 OML-dependent surfaces
- **Validation:** CFD mesh generation per `domains/AAA/cax/CFD/`

## Folder Map
- `GA/` — General arrangements
- `SD/` — Surface definition
- `IC/` — Interface control
- `MF/` — Manufacturing
- `drawing_register.json` — Register (authoritative ID list & next numbers)
