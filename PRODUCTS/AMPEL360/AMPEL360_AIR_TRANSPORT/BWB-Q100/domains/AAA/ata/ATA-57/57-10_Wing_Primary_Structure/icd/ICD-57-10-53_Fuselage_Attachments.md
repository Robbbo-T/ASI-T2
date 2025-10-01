# ICD-57-10-53: Wing Primary Structure to Fuselage/Centerbody Attachments

**Document ID:** ICD-57-10-53_Fuselage_Attachments  
**Revision:** 0.1.0  
**Date:** 2025-01-01  
**Status:** Baseline

---

## Purpose

This Interface Control Document (ICD) defines the physical, functional, and performance interfaces between the wing primary structure (ATA-57-10) and the fuselage/centerbody structure (ATA-53).

---

## Scope

### Physical Interfaces
- Wing-to-fuselage attachment fittings (forward, mid, rear)
- Load introduction points and load paths
- Fastener patterns and torque requirements
- Sealing provisions (fuel tank boundary)

### Functional Interfaces
- Load transfer (vertical, lateral, longitudinal, bending, torsion)
- Fuel containment boundary
- System provisions pass-through (hydraulics, electrical)

---

## Interface Requirements

### Geometry
- **Datum Reference:** Fuselage centerline (Y=0), waterline (Z=0), fuselage station (X)
- **Fitting Locations:**
  - Forward attach: FS 450
  - Mid attach: FS 520
  - Rear attach: FS 600
- **Tolerances:** ±0.5 mm at final assembly, ±1.0 mm at subassembly

### Load Capabilities
- **Ultimate Vertical Load:** 150 kN per attach point
- **Ultimate Lateral Load:** 80 kN per attach point
- **Ultimate Fore-Aft Load:** 60 kN per attach point
- **Ultimate Bending Moment:** 200 kN·m per attach section
- **Ultimate Torque:** 150 kN·m per attach section

### Materials
- **Wing Fitting:** Ti-6Al-4V (AMS 4928)
- **Fuselage Fitting:** Ti-6Al-4V (AMS 4928)
- **Bushings:** Steel 300M
- **Fasteners:** Steel A286, cadmium plated

### Sealing
- **Fuel Sealant:** PR-1422 Class B
- **Wet Assembly:** All fasteners in fuel tank area
- **Leak Test:** 3 psi for 10 minutes, leak rate < 0.1 SCFH

---

## Interface Control

### Responsible Organizations
- **ATA-57 (Wing):** ASI-T Wing Structures Team
- **ATA-53 (Fuselage):** ASI-T Fuselage Structures Team

### Change Control
- All interface changes require joint review and approval
- Changes affecting form/fit/function require ECP (Engineering Change Proposal)
- Minor clarifications may be incorporated via revision letter

### Coordination
- Weekly interface coordination meetings during design phase
- Monthly reviews during manufacturing phase
- Issue tracking via shared ICD issue log

---

## Acceptance Criteria

### Dimensional
- Hole-to-hole spacing: ±0.10 mm
- Bolt hole perpendicularity: ±0.5°
- Surface finish: Ra ≤ 3.2 µm on mating surfaces

### Fastener Installation
- Torque: 80 ± 5 N·m (verify with torque wrench)
- Witness marks: Required on all critical fasteners
- Lockwire: Per ATA-20-10 requirements

### Sealing
- Visual inspection: 100% coverage, no voids > 1 mm
- Leak test: Pass criteria per requirement above

---

## References

- ATA-20-10: Standard Practices - Fastening
- ATA-20-20: Standard Practices - Sealing
- ATA-53: Fuselage structure documentation
- Drawing: BWB-Q100-57-10-001 (Wing Attach Fittings)
- Drawing: BWB-Q100-53-01-002 (Fuselage Attach Fittings)

---

## Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 0.1.0 | 2025-01-01 | Initial baseline | TBD |

---
*This ICD is configuration-controlled and subject to joint approval by ATA-53 and ATA-57 teams.*
