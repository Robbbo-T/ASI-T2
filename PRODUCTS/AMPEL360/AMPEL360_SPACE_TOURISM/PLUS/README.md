---
id: ASIT2-SPACE-TOURISM-PLUS-0001-OV
rev: 0
field: space-tourism
environment: space
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: "MAL-EEM"
---

# PLUS — AMPEL360PLUS Space Tourism Aircraft

AMPEL360PLUS space tourism vehicle designed for safe, sustainable suborbital passenger experiences. This README follows the **Domain → Process (CAx/QOx) → ATA** organizational pattern for consistency with other AMPEL360 products.

---

## Quick Nav

* [Overview](#overview)
* [Development Roadmap](#development-roadmap)
* [Safety & Compliance](#safety--compliance)
* [Domain Structure](#domain-structure)
* [Sustainability Targets](#sustainability-targets)
* [Contact & Ownership](#contact--ownership)

---

## Overview

**Target:** Suborbital space tourism vehicle optimized for passenger safety, experience quality, and environmental sustainability.

**Key Features:**
- Passenger capacity: TBD (target 6-12 passengers)
- Flight profile: Suborbital trajectory with weightlessness experience
- Safety-first design with multiple redundancy systems
- Sustainable propulsion systems
- Enhanced passenger comfort and experience

**Scope anchors:**
* **Field:** Space Tourism
* **Environment:** Space (suborbital)
* **Lifecycle:** Domains to be decomposed into CAx processes with **QAIM-2** quantum augmentation (QOx)
* **Documentation:** ATA-aligned folders per domain (following BWB-Q100 pattern)

---

## Development Roadmap

**Phase 1 - Requirements & Safety Analysis (Current)**
- [ ] Safety requirements definition
- [ ] Passenger experience requirements
- [ ] Regulatory compliance analysis
- [ ] Environmental impact targets

**Phase 2 - Preliminary Design**
- [ ] Domain structure establishment
- [ ] Initial configuration studies
- [ ] Technology selection
- [ ] Risk assessment

**Phase 3 - Detailed Engineering**
- [ ] CAx/QOx domain implementations
- [ ] Systems integration
- [ ] Testing protocols
- [ ] Certification preparation

**Phase 4 - Testing & Certification**
- [ ] Ground testing
- [ ] Flight testing
- [ ] Safety certification
- [ ] Operational approval

---

## Safety & Compliance

**Primary Standards:**
- Commercial space flight regulations (FAA/AST)
- Passenger safety requirements
- Environmental compliance
- International space law compliance

**Safety Philosophy:**
- Fail-safe design principles
- Multiple independent safety systems
- Comprehensive testing and validation
- Continuous safety monitoring

---

## Domain Structure

Following the AMPEL360 domain → process (CAx/QOx) → ATA pattern, PLUS implements:

### Domain Index

* [AAA — Aerodynamics & Airframes](./domains/AAA/) — Space vehicle structures and reentry aerodynamics
* [PPP — Propulsion & Fuel Systems](./domains/PPP/) — Sustainable space propulsion and fuel management
* [CCC — Cockpit, Cabin & Cargo](./domains/CCC/) — Passenger experience and life support systems
* [EEE — Ecological Efficient Electrification](./domains/EEE/) — Sustainable power systems
* [LCC — Linkages, Control & Communications](./domains/LCC/) — Flight control and communication systems
* [MEC — Mechanical Systems Modules](./domains/MEC/) — Mechanical components and actuators
* [IIS — Integrated Intelligence & Software](./domains/IIS/) — Autonomous systems and software

### Directory Map (Domain → Process → ATA)

```
AMPEL360_SPACE_TOURISM/PLUS/
└── domains/
    ├── AAA/
    │   ├── cax/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   ├── CFD/
    │   │   ├── VP/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   └── CFD/
    │   └── ata/
    │       ├── ATA-20/
    │       ├── ATA-32/
    │       ├── ATA-51/
    │       ├── ATA-53/
    │       ├── ATA-55/
    │       └── ATA-57/
    ├── PPP/
    │   ├── cax/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   ├── CFD/
    │   │   ├── VP/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   └── CFD/
    │   └── ata/
    │       ├── ATA-71/
    │       ├── ATA-72/
    │       ├── ATA-73/
    │       ├── ATA-74/
    │       ├── ATA-75/
    │       ├── ATA-76/
    │       ├── ATA-77/
    │       └── ATA-78/
    ├── CCC/
    │   ├── cax/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   ├── VP/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   ├── CAD/
    │   │   └── VP/
    │   └── ata/
    │       ├── ATA-25/
    │       ├── ATA-31/
    │       ├── ATA-33/
    │       ├── ATA-35/
    │       ├── ATA-38/
    │       └── ATA-11/
    ├── EEE/
    │   ├── cax/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   ├── VP/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   ├── CAD/
    │   │   └── CAE/
    │   └── ata/
    │       ├── ATA-24/
    │       ├── ATA-33/
    │       └── ATA-42/
    ├── LCC/
    │   ├── cax/
    │   │   ├── CAI/
    │   │   ├── VP/
    │   │   └── CASE/
    │   ├── qox/
    │   │   └── CAI/
    │   └── ata/
    │       ├── ATA-22/
    │       ├── ATA-23/
    │       ├── ATA-27/
    │       ├── ATA-34/
    │       └── ATA-46/
    ├── MEC/
    │   ├── cax/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   ├── VP/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   ├── CAD/
    │   │   └── CAE/
    │   └── ata/
    │       ├── ATA-26/
    │       ├── ATA-28/
    │       ├── ATA-36/
    │       └── ATA-47/
    └── IIS/
        ├── cax/
        │   ├── CAI/
        │   ├── CASE/
        │   └── KBE/
        ├── qox/
        │   ├── CAI/
        │   └── KBE/
        └── ata/
            ├── ATA-46/
            ├── ATA-42/
            ├── ATA-22/
            └── ATA-45/
```

### Domains ↔ Processes (CAx/QOx) ↔ ATA

| Domain | CAx (links) | QOx (links) | ATA docs (links) - Space Tourism Adapted |
| ------ | ----------- | ----------- | ---------------------------------------- |
| **AAA** | [CAD](./domains/AAA/cax/CAD/) · [CAE](./domains/AAA/cax/CAE/) · [CFD](./domains/AAA/cax/CFD/) · [VP](./domains/AAA/cax/VP/) · [PDM-PLM](./domains/AAA/cax/PDM-PLM/) | [CAD](./domains/AAA/qox/CAD/) · [CAE](./domains/AAA/qox/CAE/) · [CFD](./domains/AAA/qox/CFD/) | [ATA-20](./domains/AAA/ata/ATA-20/) · [ATA-32](./domains/AAA/ata/ATA-32/) · [ATA-51](./domains/AAA/ata/ATA-51/) · [ATA-53](./domains/AAA/ata/ATA-53/) · [ATA-55](./domains/AAA/ata/ATA-55/) · [ATA-57](./domains/AAA/ata/ATA-57/) |
| **PPP** | [CAD](./domains/PPP/cax/CAD/) · [CAE](./domains/PPP/cax/CAE/) · [CFD](./domains/PPP/cax/CFD/) · [VP](./domains/PPP/cax/VP/) · [PDM-PLM](./domains/PPP/cax/PDM-PLM/) | [CAD](./domains/PPP/qox/CAD/) · [CAE](./domains/PPP/qox/CAE/) · [CFD](./domains/PPP/qox/CFD/) | [ATA-71](./domains/LIB/ata/ATA-71/) · [ATA-72](./domains/LIB/ata/ATA-72/) · [ATA-73](./domains/LIB/ata/ATA-73/) · [ATA-74](./domains/LIB/ata/ATA-74/) · [ATA-75](./domains/LIB/ata/ATA-75/) · [ATA-76](./domains/LIB/ata/ATA-76/) · [ATA-77](./domains/LIB/ata/ATA-77/) · [ATA-78](./domains/EER/ata/ATA-78/) |
| **CCC** | [CAD](./domains/CCC/cax/CAD/) · [CAE](./domains/CCC/cax/CAE/) · [VP](./domains/CCC/cax/VP/) · [PDM-PLM](./domains/CCC/cax/PDM-PLM/) | [CAD](./domains/CCC/qox/CAD/) · [VP](./domains/CCC/qox/VP/) | [ATA-25](./domains/CCC/ata/ATA-25/) · [ATA-31](./domains/CCC/ata/ATA-31/) · [ATA-33](./domains/CCC/ata/ATA-33/) · [ATA-35](./domains/AAP/ata/ATA-35/) · [ATA-38](./domains/CCC/ata/ATA-38/) · [ATA-11](./domains/CCC/ata/ATA-11/) |
| **EEE** | [CAD](./domains/EEE/cax/CAD/) · [CAE](./domains/EEE/cax/CAE/) · [VP](./domains/EEE/cax/VP/) · [PDM-PLM](./domains/EEE/cax/PDM-PLM/) | [CAD](./domains/EEE/qox/CAD/) · [CAE](./domains/EEE/qox/CAE/) | [ATA-24](./domains/EEE/ata/ATA-24/) · [ATA-33](./domains/CCC/ata/ATA-33/) · [ATA-42](./domains/DDD/ata/ATA-42/) |
| **LCC** | [CAI](./domains/LCC/cax/CAI/) · [VP](./domains/LCC/cax/VP/) · [CASE](./domains/LCC/cax/CASE/) | [CAI](./domains/LCC/qox/CAI/) | [ATA-22](./domains/IIS/ata/ATA-22/) · [ATA-23](./domains/DDD/ata/ATA-23/) · [ATA-27](./domains/AAA/ata/ATA-27/) · [ATA-34](./domains/AAA/ata/ATA-34/) · [ATA-46](./domains/DDD/ata/ATA-46/) |
| **MEC** | [CAD](./domains/MEC/cax/CAD/) · [CAE](./domains/MEC/cax/CAE/) · [VP](./domains/MEC/cax/VP/) · [PDM-PLM](./domains/MEC/cax/PDM-PLM/) | [CAD](./domains/MEC/qox/CAD/) · [CAE](./domains/MEC/qox/CAE/) | [ATA-26](./domains/CQH/ata/ATA-26/) · [ATA-28](./domains/AAA/ata/ATA-28/) · [ATA-36](./domains/CQH/ata/ATA-36/) · [ATA-47](./domains/CQH/ata/ATA-47/) |
| **IIS** | [CAI](./domains/IIS/cax/CAI/) · [CASE](./domains/IIS/cax/CASE/) · [KBE](./domains/IIS/cax/KBE/) | [CAI](./domains/IIS/qox/CAI/) · [KBE](./domains/IIS/qox/KBE/) | [ATA-46](./domains/DDD/ata/ATA-46/) · [ATA-42](./domains/DDD/ata/ATA-42/) · [ATA-22](./domains/IIS/ata/ATA-22/) · [ATA-45](./domains/DDD/ata/ATA-45/) |

---

## Sustainability Targets

* **Zero net carbon emissions** for operations
* **Circular design** for vehicle components
* **Sustainable fuel** systems (green hydrogen or equivalent)
* **Minimal space debris** generation
* **Efficient resource utilization**

---

## Contact & Ownership

- **Maintainer:** Robbbo-T / ASI-T Architecture Team
- **Domain leads:** To be assigned as development progresses

---

## Changelog

- **0.1.0 — 2025-09-24**  
  Initial PLUS product scaffolding with development roadmap and basic structure definition.