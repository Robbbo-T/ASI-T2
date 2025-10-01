# ICD-57-10-57-50: Wing Primary Structure to Systems Provisions

**Document ID:** ICD-57-10-57-50_Systems_Provisions  
**Revision:** 0.1.0  
**Date:** 2025-01-01  
**Status:** Baseline

---

## Purpose

This Interface Control Document (ICD) defines the physical, functional, and performance interfaces between the wing primary structure (ATA-57-10) and systems provisions/interfaces (ATA-57-50) including hydraulics, electrical, fuel, and other systems.

---

## Scope

### Physical Interfaces
- System routing provisions (holes, cutouts, channels)
- Mounting provisions for system components
- Sealing and protection requirements
- Access provisions for installation and maintenance

### Functional Interfaces
- Load-bearing capability of system mounting points
- Clearances for system installation and operation
- Electrical bonding and grounding
- Thermal management provisions

---

## Interface Requirements

### Hydraulic System Provisions

#### Routing
- **Locations:** Spar web pass-throughs at WS 200, 300, 400, 500
- **Hole Size:** 50 mm diameter (nominal) with grommets
- **Sealing:** Fuel-resistant sealant at all penetrations in fuel tank area
- **Protection:** Abrasion guards, chafe protection

#### Component Mounting
- **Hydraulic Pump:** Hard-point at WS 350, forward spar
  - Ultimate load capability: 50 kN (all directions)
  - Vibration isolation: Per ATA-29 requirements
  - Access: Removable access panel required

### Electrical System Provisions

#### Wire Routing
- **Locations:** Stringer channels, spar caps
- **Capacity:** Up to 200 wires per channel
- **Protection:** Wire bundles clipped every 150 mm maximum
- **Separation:** Hydraulics and electrical separated by 25 mm minimum

#### Electrical Bonding
- **Down-Bonds:** Every 3 meters along span
- **Resistance:** < 2.5 mΩ per bond
- **Test Points:** Accessible for bond resistance measurement
- **Protection:** Corrosion-resistant finishes on bonding surfaces

#### Lightning Strike Protection (LSP)
- **Mesh Coverage:** 100% on outer mold line
- **Terminations:** At every down-bond location
- **Bonding:** Continuous mesh-to-structure bond, < 2.5 mΩ
- **Test:** Resistance test required after installation

### Fuel System Provisions

#### Fuel Tank Structure
- **Boundaries:** Integral structure, sealed per ATA-28
- **Sealant:** PR-1422 Class B on all internal surfaces
- **Leak Test:** 3 psi for 10 minutes, leak rate < 0.1 SCFH per zone
- **Access:** Internal access required for sealing inspection

#### Fuel Quantity Probes
- **Mounting:** Non-load-bearing, isolated mounts
- **Locations:** Per ATA-28 fuel quantity indication system
- **Clearance:** 10 mm minimum from structure in all positions

### Environmental Control System (ECS)

#### Anti-Ice Provisions
- **Leading Edge:** Piccolo tubes or electrothermal mats
- **Mounting:** Non-structural, thermally isolated
- **Clearances:** 5 mm minimum from primary structure

---

## Structural Requirements

### Cutouts and Penetrations
- **Stress Concentration:** All cutouts require local reinforcement
- **Analysis:** FEA required for all cutouts > 25 mm
- **Sealing:** All penetrations in pressurized/fuel areas require sealing

### Mounting Provisions
- **Ultimate Load Capability:** Per system component requirements
- **Fatigue Life:** Minimum 2× design service goal
- **Corrosion Protection:** Cadmium plating or equivalent on all fasteners

---

## Interface Control

### Responsible Organizations
- **ATA-57-10 (Wing Primary Structure):** ASI-T Wing Structures Team
- **ATA-57-50 (Systems Provisions):** ASI-T Systems Integration Team
- **ATA-28 (Fuel System):** ASI-T Fuel Systems Team
- **ATA-29 (Hydraulic):** ASI-T Hydraulic Systems Team
- **ATA-24 (Electrical):** ASI-T Electrical Systems Team

### Change Control
- All interface changes require multi-discipline review
- Structural changes require stress analysis
- System changes require functional verification
- Interface changes logged in shared ICD issue tracker

---

## Acceptance Criteria

### Dimensional
- Hole locations: ±1.0 mm
- Hole sizes: +0.5/-0.0 mm
- Surface finish at mounting pads: Ra ≤ 3.2 µm

### Functional
- Electrical bond resistance: < 2.5 mΩ (all bonds)
- Fuel leak test: Pass per requirement
- System component installation: No interference, full clearance

### Structural
- All cutouts have approved stress analysis
- Local reinforcements installed per drawing
- NDT inspection complete and accepted

---

## References

- ATA-20-10: Standard Practices - Fastening
- ATA-20-40: Standard Practices - Electrical Bonding
- ATA-24: Electrical System
- ATA-28: Fuel System
- ATA-29: Hydraulic System
- ATA-30: Ice and Rain Protection

---

## Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 0.1.0 | 2025-01-01 | Initial baseline | TBD |

---
*This ICD is configuration-controlled and requires multi-discipline approval for any changes.*
