<!--
Repo path suggestion:
PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/INDEX.md
-->

# ASM-001 OML Master Surface — Technical Drawings

## Drawing Index

### Primary Views

* [`BWB-Q100-ASM-001-GA-001` — General Arrangement (3-view)](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-GA-001_General_Arrangement.md)
* [`BWB-Q100-ASM-001-GA-002` — Isometric Views](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-GA-002_Isometric_Views.md)
* [`BWB-Q100-ASM-001-GA-003` — Station Reference Grid](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-GA-003_Station_Reference_Grid.md)

### Surface Definition

* [`BWB-Q100-ASM-001-SD-001` — Loft Sections (STA 0–2000)](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-SD-001_Loft_Sections_STA0-2000.md)
* [`BWB-Q100-ASM-001-SD-002` — Loft Sections (STA 2000–4000)](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-SD-002_Loft_Sections_STA2000-4000.md)
* [`BWB-Q100-ASM-001-SD-003` — Planform & Twist Distribution](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-SD-003_Planform_and_Twist_Distribution.md)
* [`BWB-Q100-ASM-001-SD-004` — Blend Region Geometry](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-SD-004_Blend_Region_Geometry.md)

### Interface Control

* [`BWB-Q100-ASM-001-IC-001` — ASM-002/003/004 Join Lines](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-IC-001_Join_Lines_ASM002-004.md)
* [`BWB-Q100-ASM-001-IC-002` — Control Surface Cutouts](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-IC-002_Control_Surface_Cutouts.md)
* [`BWB-Q100-ASM-001-IC-003` — Systems Penetrations](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-IC-003_Systems_Penetrations.md)

### Manufacturing

* [`BWB-Q100-ASM-001-MF-001` — Surface Tolerance Map](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-MF-001_Surface_Tolerance_Map.md)
* [`BWB-Q100-ASM-001-MF-002` — Tooling Reference Points](PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/assemblies/ASM-001/drawings/BWB-Q100-ASM-001-MF-002_Tooling_Reference_Points.md)

---

## Standards

* **Formats:** PDF/A-1b (archival), DWG (native)
* **Units:** metric (mm)
* **Tolerance standard:** AS9100D
* **Coordinate frame:** Aircraft reference (X aft, Y right, Z up)
* **File naming:** `BWB-Q100-ASM-001-[TYPE]-[###]-[REV].[ext]` (ex: `BWB-Q100-ASM-001-GA-001-A.pdf`)

## Revision Control

| Drawing | Rev | Date | ECN | Description     |
| ------: | :-: | :--: | :-: | --------------- |
|  GA-001 |  A  |  TBD |  –  | Initial release |

## Dependencies & Impact

* **Requires:** Station grid from `domains/AAA/references/`
* **Drives updates to:** ASM-002 … ASM-032 OML-dependent surfaces
* **Validation:** CFD mesh generation per `domains/AAA/cax/CFD/`

## Folder Map

* `GA/` — General arrangements
* `SD/` — Surface definition
* `IC/` — Interface control
* `MF/` — Manufacturing
* `drawing_register.json` — Register (authoritative ID list & next numbers)

