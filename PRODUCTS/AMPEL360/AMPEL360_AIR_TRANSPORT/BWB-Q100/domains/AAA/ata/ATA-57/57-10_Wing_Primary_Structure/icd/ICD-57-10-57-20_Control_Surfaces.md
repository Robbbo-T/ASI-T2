# ICD-57-10-57-20: Wing Primary Structure to Control Surfaces

**Document ID:** ICD-57-10-57-20_Control_Surfaces  
**Revision:** 0.1.0  
**Date:** 2025-01-01  
**Status:** Baseline

---

## Purpose

This Interface Control Document (ICD) defines the physical, functional, and performance interfaces between the wing primary structure (ATA-57-10) and control surfaces including ailerons, spoilers, and flaps (ATA-57-20).

---

## Scope

### Physical Interfaces
- Hinge fittings and attachment points
- Actuator hard-points and mounting provisions
- Seal lands and aerodynamic continuity
- Access provisions for installation/removal

### Functional Interfaces
- Hinge moment loads
- Actuator loads and stroke
- Deflection limits and clearances
- Sealing against aerodynamic loads

---

## Interface Requirements

### Hinge Fittings

#### Aileron Hinges
- **Locations:** Wing station (WS) 450, 520, 590
- **Load Capability (per hinge):**
  - Ultimate hinge moment: 25 kN·m
  - Ultimate side load: 15 kN
- **Materials:** Ti-6Al-4V fitting, steel bushings
- **Clearance:** 2.0 mm minimum (installed)

#### Spoiler Hinges
- **Locations:** WS 380, 420, 460, 500, 540
- **Load Capability (per hinge):**
  - Ultimate hinge moment: 15 kN·m
  - Ultimate side load: 10 kN
- **Materials:** Aluminum 7075-T6 fitting, steel bushings

#### Flap Hinges
- **Locations:** WS 150, 200, 250, 300, 350
- **Load Capability (per hinge):**
  - Ultimate hinge moment: 40 kN·m
  - Ultimate side load: 20 kN
- **Materials:** Ti-6Al-4V fitting, steel bushings

### Actuator Hard-Points

#### Aileron Actuators
- **Locations:** WS 485, 555
- **Load Capability (per actuator):**
  - Ultimate push load: 80 kN
  - Ultimate pull load: 80 kN
- **Stroke:** ±50 mm from neutral
- **Attachment:** 4× M12 bolts, Ti-6Al-4V hard-point

#### Spoiler Actuators
- **Locations:** WS 390, 430, 470, 510
- **Load Capability (per actuator):**
  - Ultimate extend load: 60 kN
  - Ultimate retract load: 40 kN
- **Stroke:** 0 to 100 mm (fully retracted to fully extended)

### Seal Lands

- **Surface Finish:** Ra ≤ 1.6 µm
- **Flatness:** ±0.25 mm over any 100 mm length
- **Material Protection:** Erosion-resistant coating or leading edge protection

### Deflection Limits

- **Wing Structure Deflection:** < 1.0 mm at hinge line under limit load
- **Control Surface Clearance:** 3.0 mm minimum (any condition)

---

## Interface Control

### Responsible Organizations
- **ATA-57-10 (Wing Primary Structure):** ASI-T Wing Structures Team
- **ATA-57-20 (Control Surfaces):** ASI-T Flight Controls Team

### Change Control
- Interface changes require joint review and approval
- Changes affecting clearances or loads require stress re-analysis
- Control surface rigging affected by interface changes requires flight test validation

---

## Acceptance Criteria

### Dimensional
- Hinge axis alignment: ±0.15 mm over any 300 mm span
- Actuator mounting hole pattern: ±0.10 mm
- Seal land flatness: per requirement above

### Functional
- Control surface free play: < 1.0 mm (all hinges installed)
- Actuator stroke verification: Full stroke without binding
- Rigging check: Full deflection range verified

### Structural
- Hinge pin fit: Class 3 fit (close running fit)
- Fastener torque: Per drawing requirements
- Lock devices: Verified installed per ATA-20-10

---

## References

- ATA-20-10: Standard Practices - Fastening
- ATA-57-20: Control Surfaces documentation
- Drawing: BWB-Q100-57-10-005 (Hinge Fittings)
- Drawing: BWB-Q100-57-10-006 (Actuator Hard-Points)
- Drawing: BWB-Q100-57-20-001 (Control Surface Attachments)

---

## Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 0.1.0 | 2025-01-01 | Initial baseline | TBD |

---
*This ICD is configuration-controlled and subject to joint approval by ATA-57-10 and ATA-57-20 teams.*
