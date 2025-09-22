---
id: ASIT2-TRANSCIVIL-AIR-BWB-Q100-0001-OV
rev: 0
field: transport-civil
environment: air
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.3.1"
release\_date: 2025-09-22
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics\_guard: "MAL-EEM"
---

# BWB-Q100 — Transport Civil × Air

Blended Wing Body Q100 passenger aircraft under the ASI-T2 portfolio. This README is organized **Domain → Process (CAx/QOx) → ATA** for clean navigation and traceability.

---

## Quick Nav

* [Overview](#overview)
* [Directory Map (Domain → Process → ATA)](#directory-map-domain--process--ata)
* [Domain Index](#domain-index)
* [Domains ↔ Processes (CAx/QOx) ↔ ATA](#domains--processes-caxqox--ata)
* [QAIM-2: CAx → QOx Matrix (SIM)](#qaim-2-cax--qox-matrix-sim)
* [Workflows](#workflows)
* [Evidence & Compliance](#evidence--compliance)
* [Glossary & Acronyms](#glossary--acronyms)
* [FAQ](#FAQ)

---

## Overview

Target: \~100-passenger BWB optimized for fuel burn ↓, emissions ↓, noise ↓, and circularity ↑. Engineering follows TFA-ONLY path grammar, UIX.v1, and MAL-EEM ethics. Every milestone emits QS/UTCS evidence.

**Scope anchors**

* **Field:** Transport Civil
* **Environment:** Air
* **Lifecycle:** Domains decomposed into CAx processes with **QAIM-2** quantum augmentation (QOx)
* **Documentation:** ATA-aligned folders per domain

---

## Directory Map (Domain → Process → ATA)

```
Product_Line_AMPEL360/Model_BWB/variant-Q100/conf_000_baseline/MSN[0001-9999]
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
    │       ├── ATA-52/
    │       ├── ATA-53/
    │       ├── ATA-54/
    │       ├── ATA-55/
    │       ├── ATA-56/
    │       └── ATA-57/
    ├── AAP/
    │   ├── cax/
    │   │   ├── SCM/
    │   │   ├── MRP-ERP/
    │   │   ├── CIM/
    │   │   └── CAPP/
    │   ├── qox/
    │   │   ├── SCM/
    │   │   └── CIM/
    │   └── ata/
    │       ├── ATA-10/
    │       ├── ATA-12/
    │       ├── ATA-28/
    │       └── ATA-35/
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
    │       ├── ATA-11/
    │       ├── ATA-25/
    │       ├── ATA-31/
    │       ├── ATA-33/
    │       └── ATA-38/
    ├── CQH/
    │   ├── cax/
    │   │   ├── CAE/
    │   │   ├── CAI/
    │   │   ├── VP/
    │   │   └── CAT/
    │   ├── qox/
    │   │   ├── CAE/
    │   │   └── CAI/
    │   └── ata/
    │       ├── ATA-21/
    │       ├── ATA-26/
    │       ├── ATA-28/
    │       ├── ATA-36/
    │       └── ATA-47/
    ├── DDD/
    │   ├── cax/
    │   │   ├── CAI/
    │   │   ├── CASE/
    │   │   ├── KBE/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   ├── CAI/
    │   │   └── KBE/
    │   └── ata/
    │       ├── ATA-23/
    │       ├── ATA-31/
    │       ├── ATA-42/
    │       ├── ATA-45/
    │       └── ATA-46/
    ├── EDI/
    │   ├── cax/
    │   │   ├── CAI/
    │   │   ├── CASE/
    │   │   └── VP/
    │   ├── qox/
    │   │   ├── CAI/
    │   │   └── CASE/
    │   └── ata/
    │       ├── ATA-23/
    │       ├── ATA-31/
    │       ├── ATA-33/
    │       ├── ATA-34/
    │       ├── ATA-42/
    │       └── ATA-46/
    ├── EEE/
    │   ├── cax/
    │   │   ├── CAE/
    │   │   ├── CAD/
    │   │   ├── CAM/
    │   │   ├── PDM-PLM/
    │   │   └── CAI/
    │   ├── qox/
    │   │   ├── CAE/
    │   │   └── CAM/
    │   └── ata/
    │       ├── ATA-21/
    │       ├── ATA-24/
    │       └── ATA-30/
    ├── EER/
    │   ├── cax/
    │   │   ├── KBE/
    │   │   ├── VP/
    │   │   ├── CASE/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   └── KBE/
    │   └── ata/
    │       ├── ATA-21/
    │       ├── ATA-31/
    │       ├── ATA-38/
    │       └── ATA-78/
    ├── IIF/
    │   ├── cax/
    │   │   ├── CAPP/
    │   │   ├── CAM/
    │   │   ├── CIM/
    │   │   ├── MRP-ERP/
    │   │   └── CAA/
    │   ├── qox/
    │   │   ├── CAM/
    │   │   └── CIM/
    │   └── ata/
    │       ├── ATA-20/
    │       └── ATA-51/
    ├── IIS/
    │   ├── cax/
    │   │   ├── CAI/
    │   │   ├── CASE/
    │   │   └── KBE/
    │   ├── qox/
    │   │   ├── CAI/
    │   │   └── KBE/
    │   └── ata/
    │       ├── ATA-22/
    │       ├── ATA-42/
    │       ├── ATA-45/
    │       └── ATA-46/
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
    ├── LIB/
    │   ├── cax/
    │   │   ├── SCM/
    │   │   ├── MRP-ERP/
    │   │   └── PDM-PLM/
    │   ├── qox/
    │   │   ├── SCM/
    │   │   └── MRP-ERP/
    │   └── ata/
    │       ├── ATA-20/
    │       ├── ATA-51/
    │       ├── ATA-52/
    │       ├── ATA-53/
    │       ├── ATA-54/
    │       ├── ATA-55/
    │       ├── ATA-56/
    │       ├── ATA-57/
    │       ├── ATA-70/
    │       ├── ATA-71/
    │       ├── ATA-72/
    │       ├── ATA-73/
    │       ├── ATA-74/
    │       ├── ATA-75/
    │       ├── ATA-76/
    │       ├── ATA-77/
    │       ├── ATA-78/
    │       └── ATA-79/
    ├── MEC/
    │   ├── cax/
    │   │   ├── CAD/
    │   │   ├── CAE/
    │   │   ├── CAM/
    │   │   ├── CAPP/
    │   │   └── VP/
    │   ├── qox/
    │   │   └── CAE/
    │   └── ata/
    │       ├── ATA-21/
    │       ├── ATA-27/
    │       ├── ATA-29/
    │       ├── ATA-30/
    │       ├── ATA-32/
    │       ├── ATA-35/
    │       ├── ATA-36/
    │       └── ATA-38/
    ├── OOO/
    │   ├── cax/
    │   │   ├── PDM-PLM/
    │   │   ├── CAI/
    │   │   ├── CASE/
    │   │   └── KBE/
    │   ├── qox/
    │   │   └── KBE/
    │   └── ata/
    │       ├── ATA-45/
    │       └── ATA-46/
    └── PPP/
        ├── cax/
        │   ├── CAD/
        │   ├── CAE/
        │   ├── CFD/
        │   ├── CAM/
        │   └── VP/
        ├── qox/
        │   ├── CAD/
        │   ├── CAE/
        │   └── CFD/
        └── ata/
            ├── ATA-28/
            ├── ATA-49/
            ├── ATA-70/
            ├── ATA-71/
            ├── ATA-72/
            ├── ATA-73/
            ├── ATA-74/
            ├── ATA-75/
            ├── ATA-76/
            ├── ATA-77/
            ├── ATA-78/
            └── ATA-79/
```

---

## Domain Index

* [AAA — Aerodynamics & Airframes](./domains/AAA/)
* [AAP — Airport Adaptable Platforms](./domains/AAP/)
* [CCC — Cockpit, Cabin & Cargo](./domains/CCC/)
* [CQH — Cryogenics, Quantum & H₂](./domains/CQH/)
* [DDD — Digital & Data Defense](./domains/DDD/)
* [EDI — Electronics & Digital Instruments](./domains/EDI/)
* [EEE — Ecological Efficient Electrification](./domains/EEE/)
* [EER — Environmental, Emissions & Remediation](./domains/EER/)
* [IIF — Industrial Infrastructure & Facilities](./domains/IIF/)
* [IIS — Integrated Intelligence & Software](./domains/IIS/)
* [LCC — Linkages, Control & Communications](./domains/LCC/)
* [LIB — Logistics, Inventory & Blockchain](./domains/LIB/)
* [MEC — Mechanical Systems Modules](./domains/MEC/)
* [OOO — OS, Ontologies & Office Interfaces](./domains/OOO/)
* [PPP — Propulsion & Fuel System](./domains/PPP/)

---

## Domains ↔ Processes (CAx/QOx) ↔ ATA

| Domain  | CAx (links)                                                                                                                                                             | QOx (links)                                                                                   | ATA docs (links)                                                                                                                                                                                                                                                                                                                                    |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AAA** | [CAD](./domains/AAA/cax/CAD/) · [CAE](./domains/AAA/cax/CAE/) · [CFD](./domains/AAA/cax/CFD/) · [VP](./domains/AAA/cax/VP/) · [PDM-PLM](./domains/AAA/cax/PDM-PLM/)     | [CAD](./domains/AAA/qox/CAD/) · [CAE](./domains/AAA/qox/CAE/) · [CFD](./domains/AAA/qox/CFD/) | [ATA-51](./domains/AAA/ata/ATA-51/) · [ATA-52](./domains/AAA/ata/ATA-52/) · [ATA-53](./domains/AAA/ata/ATA-53/) · [ATA-54](./domains/AAA/ata/ATA-54/) · [ATA-55](./domains/AAA/ata/ATA-55/) · [ATA-56](./domains/AAA/ata/ATA-56/) · [ATA-57](./domains/AAA/ata/ATA-57/) · [ATA-32](./domains/AAA/ata/ATA-32/) · [ATA-20](./domains/AAA/ata/ATA-20/) |
| **AAP** | [SCM](./domains/AAP/cax/SCM/) · [MRP-ERP](./domains/AAP/cax/MRP-ERP/) · [CIM](./domains/AAP/cax/CIM/) · [CAPP](./domains/AAP/cax/CAPP/)                                 | [SCM](./domains/AAP/qox/SCM/) · [CIM](./domains/AAP/qox/CIM/)                                 | [ATA-10](./domains/AAP/ata/ATA-10/) · [ATA-12](./domains/AAP/ata/ATA-12/) · [ATA-28](./domains/AAP/ata/ATA-28/) · [ATA-35](./domains/AAP/ata/ATA-35/)                                                                                                                                                                                               |
| **CCC** | [CAD](./domains/CCC/cax/CAD/) · [CAE](./domains/CCC/cax/CAE/) · [VP](./domains/CCC/cax/VP/) · [PDM-PLM](./domains/CCC/cax/PDM-PLM/)                                     | [CAD](./domains/CCC/qox/CAD/) · [VP](./domains/CCC/qox/VP/)                                   | [ATA-25](./domains/CCC/ata/ATA-25/) · [ATA-31](./domains/CCC/ata/ATA-31/) · [ATA-33](./domains/CCC/ata/ATA-33/) · [ATA-38](./domains/CCC/ata/ATA-38/) · [ATA-11](./domains/CCC/ata/ATA-11/)                                                                                                                                                         |
| **CQH** | [CAE](./domains/CQH/cax/CAE/) · [CAI](./domains/CQH/cax/CAI/) · [VP](./domains/CQH/cax/VP/) · [CAT](./domains/CQH/cax/CAT/)                                             | [CAE](./domains/CQH/qox/CAE/) · [CAI](./domains/CQH/qox/CAI/)                                 | [ATA-28](./domains/CQH/ata/ATA-28/) · [ATA-21](./domains/CQH/ata/ATA-21/) · [ATA-26](./domains/CQH/ata/ATA-26/) · [ATA-36](./domains/CQH/ata/ATA-36/) · [ATA-47](./domains/CQH/ata/ATA-47/)                                                                                                                                                         |
| **DDD** | [CAI](./domains/DDD/cax/CAI/) · [CASE](./domains/DDD/cax/CASE/) · [KBE](./domains/DDD/cax/KBE/) · [PDM-PLM](./domains/DDD/cax/PDM-PLM/)                                 | [CAI](./domains/DDD/qox/CAI/) · [KBE](./domains/DDD/qox/KBE/)                                 | [ATA-46](./domains/DDD/ata/ATA-46/) · [ATA-45](./domains/DDD/ata/ATA-45/) · [ATA-31](./domains/DDD/ata/ATA-31/) · [ATA-23](./domains/DDD/ata/ATA-23/) · [ATA-42](./domains/DDD/ata/ATA-42/)                                                                                                                                                         |
| **EDI** | [CAI](./domains/EDI/cax/CAI/) · [CASE](./domains/EDI/cax/CASE/) · [VP](./domains/EDI/cax/VP/)                                                                           | [CAI](./domains/EDI/qox/CAI/) · [CASE](./domains/EDI/qox/CASE/)                               | [ATA-31](./domains/EDI/ata/ATA-31/) · [ATA-23](./domains/EDI/ata/ATA-23/) · [ATA-34](./domains/EDI/ata/ATA-34/) · [ATA-46](./domains/EDI/ata/ATA-46/) · [ATA-42](./domains/EDI/ata/ATA-42/) · [ATA-33](./domains/EDI/ata/ATA-33/)                                                                                                                   |
| **EEE** | [CAE](./domains/EEE/cax/CAE/) · [CAD](./domains/EEE/cax/CAD/) · [CAM](./domains/EEE/cax/CAM/) · [PDM-PLM](./domains/EEE/cax/PDM-PLM/) · [CAI](./domains/EEE/cax/CAI/)   | [CAE](./domains/EEE/qox/CAE/) · [CAM](./domains/EEE/qox/CAM/)                                 | [ATA-24](./domains/EEE/ata/ATA-24/) · [ATA-21](./domains/EEE/ata/ATA-21/) · [ATA-30](./domains/EEE/ata/ATA-30/)                                                                                                                                                                                                                                     |
| **EER** | [KBE](./domains/EER/cax/KBE/) · [VP](./domains/EER/cax/VP/) · [CASE](./domains/EER/cax/CASE/) · [PDM-PLM](./domains/EER/cax/PDM-PLM/)                                   | [KBE](./domains/EER/qox/KBE/)                                                                 | [ATA-21](./domains/EER/ata/ATA-21/) · [ATA-31](./domains/EER/ata/ATA-31/) · [ATA-38](./domains/EER/ata/ATA-38/) · [ATA-78](./domains/EER/ata/ATA-78/)                                                                                                                                                                                               |
| **IIF** | [CAPP](./domains/IIF/cax/CAPP/) · [CAM](./domains/IIF/cax/CAM/) · [CIM](./domains/IIF/cax/CIM/) · [MRP-ERP](./domains/IIF/cax/MRP-ERP/) · [CAA](./domains/IIF/cax/CAA/) | [CAM](./domains/IIF/qox/CAM/) · [CIM](./domains/IIF/qox/CIM/)                                 | [ATA-20](./domains/IIF/ata/ATA-20/) · [ATA-51](./domains/IIF/ata/ATA-51/)                                                                                                                                                                                                                                                                           |
| **IIS** | [CAI](./domains/IIS/cax/CAI/) · [CASE](./domains/IIS/cax/CASE/) · [KBE](./domains/IIS/cax/KBE/)                                                                         | [CAI](./domains/IIS/qox/CAI/) · [KBE](./domains/IIS/qox/KBE/)                                 | [ATA-46](./domains/IIS/ata/ATA-46/) · [ATA-42](./domains/IIS/ata/ATA-42/) · [ATA-22](./domains/IIS/ata/ATA-22/) · [ATA-45](./domains/IIS/ata/ATA-45/)                                                                                                                                                                                               |
| **LCC** | [CAI](./domains/LCC/cax/CAI/) · [VP](./domains/LCC/cax/VP/) · [CASE](./domains/LCC/cax/CASE/)                                                                           | [CAI](./domains/LCC/qox/CAI/)                                                                 | [ATA-22](./domains/LCC/ata/ATA-22/) · [ATA-23](./domains/LCC/ata/ATA-23/) · [ATA-27](./domains/LCC/ata/ATA-27/) · [ATA-34](./domains/LCC/ata/ATA-34/) · [ATA-46](./domains/LCC/ata/ATA-46/)                                                                                                                                                         |
| **LIB** | [SCM](./domains/LIB/cax/SCM/) · [MRP-ERP](./domains/LIB/cax/MRP-ERP/) · [PDM-PLM](./domains/LIB/cax/PDM-PLM/)                                                           | [SCM](./domains/LIB/qox/SCM/) · [MRP-ERP](./domains/LIB/qox/MRP-ERP/)                         | [ATA-20](./domains/LIB/ata/ATA-20/) · 51–57 · 70–79                                                                                                                                                                                                                                                                                                 |
| **MEC** | [CAD](./domains/MEC/cax/CAD/) · [CAE](./domains/MEC/cax/CAE/) · [CAM](./domains/MEC/cax/CAM/) · [CAPP](./domains/MEC/cax/CAPP/) · [VP](./domains/MEC/cax/VP/)           | [CAE](./domains/MEC/qox/CAE/)                                                                 | [ATA-27](./domains/MEC/ata/ATA-27/) · [ATA-29](./domains/MEC/ata/ATA-29/) · [ATA-32](./domains/MEC/ata/ATA-32/) · [ATA-30](./domains/MEC/ata/ATA-30/) · [ATA-36](./domains/MEC/ata/ATA-36/) · [ATA-35](./domains/MEC/ata/ATA-35/) · [ATA-21](./domains/MEC/ata/ATA-21/) · [ATA-38](./domains/MEC/ata/ATA-38/)                                       |
| **OOO** | [PDM-PLM](./domains/OOO/cax/PDM-PLM/) · [CAI](./domains/OOO/cax/CAI/) · [CASE](./domains/OOO/cax/CASE/) · [KBE](./domains/OOO/cax/KBE/)                                 | [KBE](./domains/OOO/qox/KBE/)                                                                 | [ATA-46](./domains/OOO/ata/ATA-46/) · [ATA-45](./domains/OOO/ata/ATA-45/)                                                                                                                                                                                                                                                                           |
| **PPP** | [CAD](./domains/PPP/cax/CAD/) · [CAE](./domains/PPP/cax/CAE/) · [CFD](./domains/PPP/cax/CFD/) · [CAM](./domains/PPP/cax/CAM/) · [VP](./domains/PPP/cax/VP/)             | [CAD](./domains/PPP/qox/CAD/) · [CAE](./domains/PPP/qox/CAE/) · [CFD](./domains/PPP/qox/CFD/) | [ATA-70](./domains/PPP/ata/ATA-70/) · … · [ATA-79](./domains/PPP/ata/ATA-79/) · [ATA-28](./domains/PPP/ata/ATA-28/) · [ATA-49](./domains/PPP/ata/ATA-49/)                                                                                                                                                                                           |

---

## QAIM-2: CAx → QOx Matrix (SIM)

*(i)* optimization target · *(ii)* quantum mapping · *(iii)* SIM lever · *(iv)* maturity

| CAx domain | (i) What to optimize            | (ii) Quantum mapping                       | (iii) SIM lever                  | (iv) Maturity  |
| ---------- | ------------------------------- | ------------------------------------------ | -------------------------------- | -------------- |
| CAD        | Layout/topology                 | QUBO/BQM → QAOA/Annealing; VQE subproblems | Material use ↓; drag ↓           | Pilot/Research |
| CAE        | Topology & sizing               | QUBO/BQM; exploratory QLSA/HHL             | Mass ↓ with safety ↑             | Research       |
| CFD        | Operating points; DOE           | QUBO for DOE; exploratory QLSA/HHL         | Fuel burn ↓; emissions ↓         | Research       |
| KBE        | Rule Max-SAT                    | QUBO Max-SAT → QAOA/Annealing              | Right-first-time ↑               | Pilot          |
| VP         | Test plan selection             | QUBO/BQM → QAOA/Annealing                  | Test time/energy ↓               | Pilot          |
| CAM        | Toolpath batch, sequencing      | QUBO/BQM (job/flow shop)                   | Energy/idle ↓; throughput ↑      | Pilot          |
| CAPP       | Routing; takt balance           | QUBO/BQM                                   | WIP ↓; takt adherence ↑          | Pilot          |
| MRP-ERP    | Inventory/capacity/lot sizing   | Multi-objective QUBO (hybrid)              | Stockouts/waste ↓; service ↑     | Pilot          |
| CIM        | Plant meta-schedule             | Global schedule QUBO                       | Energy/CO₂ per unit ↓            | Pilot          |
| SCM        | VRP/mVRP/network                | Routing QUBO → Annealing/QAOA (hybrid)     | Transport emissions ↓; OTIF ↑    | Now/Pilot      |
| PDM-PLM    | BOM variants; change impact     | QUBO/BQM                                   | Rework ↓; circularity ↑          | Pilot          |
| CAI        | Embedding portfolio (multi-obj) | Weighted-objective QUBO → QAOA             | Energy efficiency ↑; abatement ↑ | Pilot          |
| CAA        | Robot/cell allocation & timing  | Assignment/scheduling QUBO                 | Utilization ↑; energy ↓          | Pilot          |

---

## Workflows

1. Model (CAx) → commit in `domains/<CODE>/cax/<PHASE>/`.
2. Encode (QOx) → emit QUBO/BQM into `domains/<CODE>/qox/<PHASE>/problems/`.
3. Solve → run `qaoa/` or `annealing/`; save to `domains/<CODE>/qox/<PHASE>/runs/<YYYYMMDD-HHMMSS>/` (auto-QS/UTCS).
4. Document (ATA) → update `domains/<CODE>/ata/ATA-XX/` with references and evidence.
5. Gate → PR includes UTCS anchors; MAL-EEM enforced.

**in other words**:

1. Model (CAx): An engineer performs a standard task using a classical tool, such as designing a component in CAD or analyzing airflow in CFD.

2. Encode (QOx): A difficult optimization problem from the CAx study (e.g., finding the absolute best winglet topology to reduce drag or the most efficient manufacturing schedule) is mathematically encoded into a format suitable for a quantum computer. This is typically a Quadratic Unconstrained Binary Optimization (QUBO) problem.

3. Solve (QOx): The QUBO problem is solved using a quantum algorithm, such as the Quantum Approximate Optimization Algorithm (QAOA) or Quantum Annealing. This process explores a vast number of potential solutions simultaneously to find a high-quality or optimal result.

4. Document (ATA): The results from both the classical and quantum runs are documented in the relevant ATA chapter, providing a complete record of the work.

5. Commit

---

## Evidence & Compliance

* UTCS/QS: deterministic evidence (hashes, operator, policy/model/data) per run.
* Ethics: MAL-EEM guard active across all agents.
* Standards: ATA folders carry the authoritative documentation for audits.

---

### Glossary & Acronyms

#### Domains

* **AAA — Aerodynamics & Airframes Architectures**
* **AAP — Airport Adaptable Platforms**
* **CCC — Cockpit, Cabin & Cargo**
* **CQH — Cryogenics, Quantum & H₂**
* **DDD — Digital & Data Defense**
* **EDI — Electronics & Digital Instruments**
* **EEE — Ecological Efficient Electrification**
* **EER — Environmental, Emissions & Remediation**
* **IIF — Industrial Infrastructure & Facilities**
* **IIS — Integrated Intelligence & Software**
* **LCC — Linkages, Control & Communications**
* **LIB — Logistics, Inventory & Blockchain**
* **MEC — Mechanical Systems Modules**
* **OOO — OS, Ontologies & Office Interfaces**
* **PPP — Propulsion & Fuel System**

#### Core architecture & governance

* **ASI-T2** — Artificial Super Intelligence Transponders for Aerospace Sustainable Industry Transition.
* **BWB** — Blended Wing Body (integrated wing–fuselage airframe).
* **TFA** — **Top Federation Algorithm / Threading Final Assembly**; federated architecture and execution thread tying all layers (Systems→States) into a single, auditable final-assembly flow (design → manufacture → integration → test → certification).
* **UTCS / QS** — Universal Traceability & Configuration System / Quantum Seal; deterministic provenance anchors and immutable evidence blobs.
* **UIX** — Universal Injection Prompt; mandatory pre-flight rules for human/AI agents.
* **MAL-EEM** — Ethics & Empathy Module; safety/ethical guardrails (fail-closed).

#### CAx terms (Computer-Aided *x*)

* **CAD — Computer-Aided Design**: geometry/topology, layouts, parametric models, BoMs; manufacturing definitions.
* **CAE — Computer-Aided Engineering**: structural/thermal/dynamic analyses (FEA, **MBD**), sizing & safety margins.
* **CFD — Computational Fluid Dynamics**: external/internal flows, aero/thermal performance, drag/noise trades, mesh & **DOE** strategies.
* **CAM — Computer-Aided Manufacturing**: toolpaths, NC programs, fixturing, machining strategies, additive build files.
* **CAPP — Computer-Aided Process Planning**: routing, work instructions, takt/line balance, station sequencing, process **FMEA**s.
* **VP — Virtual Prototyping**: system-level sims (**SIL/HIL**), campaign design, digital test plans prior to physical builds.
* **PDM-PLM — Product/Process Data & Lifecycle Management**: configuration control, variants, change impact, digital thread.
* **SCM — Supply Chain Management**: sourcing, logistics networks, supplier risk, material passports, **OTIF** performance.
* **MRP-ERP — Materials/Enterprise Resource Planning**: demand/capacity/lot sizing, inventory policies, cost & lead-time control.
* **CIM — Computer-Integrated Manufacturing**: plant-level orchestration, schedule optimization, energy/CO₂ per-unit tracking.
* **CAI — HW·SW·AI Embedding**: integration of electronics/software/AI with hardware (avionics, controls, autonomy).
* **CAA — Computer-Aided Automation**: robots/cells/**AGV**s scheduling, path/time optimization, safe automation envelopes.
* **CASE — Computer-Aided Software Engineering**: requirements↔tests traceability, test selection/triage, coverage metrics.
* **KBE / KLM — Knowledge-Based Engineering / Knowledge Lifecycle Management**: design rules, certification constraints, reusable logic.
* **CAT — Computer-Aided Testing**: environmental/functional/safety test execution and results curation (bench, rig, flight).

#### QOx terms (Quantum-Optimized *x* — per-phase quantum counterparts)

* **QOx/CAD** — Layout/topology encodings; **QUBO**/**BQM** → **QAOA**/annealing; materials sub-problems via **VQE**.
* **QOx/CAE** — Topology/sizing trade encodings; **QUBO/BQM** today, exploratory linear/PDE sub-solves via **HHL/QLSA**.
* **QOx/CFD** — **DOE** & operating-point selection as **QUBO**; long-term linear solves via **HHL/QLSA** research.
* **QOx/CAM** — Job/flow-shop batching & sequencing; **QUBO/BQM → QAOA/annealing** with hybrid post-processing.
* **QOx/CAPP** — Routing/takt/line-balance encodings; **QUBO/BQM** solved with variational/annealing hybrids.
* **QOx/VP** — Test-campaign/**DOE** selection; **QUBO/BQM** with explainable trade outputs to **SIM/LCA**.
* **QOx/PDM-PLM** — Variant/change-impact minimization; multi-objective **QUBO/BQM** portfolios.
* **QOx/SCM** — **VRP/mVRP**/network design; **QUBO/BQM →** annealing/**QAOA** plus classical heuristics.
* **QOx/MRP-ERP** — Inventory/capacity/lot sizing; multi-objective **QUBO/BQM** with hybrid decomposition.
* **QOx/CIM** — Plant meta-schedule/global orchestration; large-scale **QUBO/BQM** with hierarchical solves.
* **QOx/CAI** — Architecture/feature portfolio & controller tuning; weighted-objective **QUBO/BQM → QAOA**.
* **QOx/CAA** — Robot/cell assignment & timing; **QUBO/BQM** for resource-constrained scheduling.
* **QOx/CASE** — Test-set minimization/triage (coverage vs. risk); **QUBO/BQM → QAOA/annealing**.
* **QOx/KBE** — Rule/constraint satisfaction (**Max-SAT**); **QUBO** Max-SAT → **QAOA**/annealing.
* **QOx/CAT** — Test-sequence optimization & sensor selection; **QUBO/BQM** with reliability/**ESG** weighting.

#### Quantum & optimization methods

* **QUBO — Quadratic Unconstrained Binary Optimization**: binary decision vector with quadratic cost; standard encoding for routing, assignment, scheduling.
* **BQM — Binary Quadratic Model**: general form (binary or spin) equivalent to QUBO/Ising with pairwise interactions.
* **Ising Model** — Spin-based energy formulation equivalent to BQM; native to annealers.
* **QAOA — Quantum Approximate Optimization Algorithm**: variational, gate-model heuristic for combinatorial problems.
* **Quantum Annealing** — Energy-landscape minimization on Ising/BQM Hamiltonians (physical/analog or simulated).
* **VQE — Variational Quantum Eigensolver**: approximate ground states for chemistry/materials/physics sub-problems.
* **HHL / QLSA** — Quantum linear-system solvers; future-leaning for PDE/CFD/CAE kernels.
* **Max-SAT — Maximum Satisfiability**: optimization variant of SAT; maximize satisfied clauses under constraints.
* **DOE — Design of Experiments**: active selection of experiments/sim points (e.g., fractional factorial, Latin hypercube, Bayesian DOE).

#### Sustainability & operations

* **SIM — Sustainable Industry Model**: decision framework where CAx/QOx outcomes feed sustainability levers and KPIs.
* **LCA — Life Cycle Assessment**: ISO 14040/44 cradle-to-grave impact accounting (materials, manufacturing, use, EoL).
* **GHG Protocol** — Corporate greenhouse-gas accounting across **Scopes 1/2/3** (direct, energy, value-chain).
* **OTIF — On-Time In-Full**: supply-chain service KPI.
* **FMEA — Failure Modes & Effects Analysis**: risk assessment for process/product.
* **SIL / HIL — Software/Hardware-in-the-Loop**: closed-loop simulation with real code/hardware.
* **MBD — Multi-Body Dynamics**: dynamic simulation of interconnected rigid/flexible bodies.
* **BOM — Bill of Materials**: structured parts list for a configuration.
* **AGV — Automated Guided Vehicle**: mobile platform for intralogistics/assembly.
* **APU — Auxiliary Power Unit**: on-board power/air source (ATA-49).

## BWB-Q100 — FAQ 

**Q1. What’s the mission of BWB-Q100?**
A \~100-passenger blended-wing-body optimized for **fuel burn ↓, emissions ↓, noise ↓, circularity ↑**. Work follows **TFA** (Top Federation Algorithm / Threading Final Assembly), **UIX.v1**, and **MAL-EEM**, with QS/UTCS provenance at every gate.

**Q2. Where do I work for a given topic?**
Navigate **Domain → Process (CAx/QOx) → ATA** under:
`domains/<CODE>/{cax|qox}/<PHASE>/…` and `domains/<CODE>/ata/ATA-XX/…`.
Examples:

* Wing CFD: `domains/AAA/cax/CFD/` → quantum DOE in `domains/AAA/qox/CFD/` → docs in `domains/AAA/ata/ATA-57/`.
* Landing gear: `domains/MEC/…` and docs in `domains/MEC/ata/ATA-32/`.

**Q3. How do I add a new CAx study?**
Create a folder in the owning domain: `domains/<CODE>/cax/<PHASE>/…` with a short `README.md`, inputs, configs, and results. Commit with UTCS anchors.

**Q4. How do I produce a QOx run from a CAx study?**
Encode the decision as **QUBO/BQM**:
`domains/<CODE>/qox/<PHASE>/problems/<slug>.json`
Solve with `qaoa/` or `annealing/`; outputs go to:
`domains/<CODE>/qox/<PHASE>/runs/<YYYYMMDD-HHMMSS>/`
Each run emits QS/UTCS (policy/model/data/operator hashes).

**Q5. Where do ATA documents live and how do I link evidence?**
Per domain in `domains/<CODE>/ata/ATA-XX/`. Reference CAx/QOx artefacts by relative links and include their QS/UTCS digests in the doc’s evidence section.

**Q6. What if my work spans multiple domains?**
Put **primary ownership** in the most responsible domain (e.g., propulsion in **PPP**). Cross-link secondary impacts from their ATA folders (e.g., nacelle structures in **AAA/ATA-54**).

**Q7. How do revisions work (HOV)?**
Baseline lives in the product root. For **rev ≥ 1**, create:
`_revisions/REV_<LETTER>/HOV_<MSN_RANGE>_<PHASES>/…` mirroring the same domain/process/ATA structure. Keep filenames stable (no letters); encode rev in the path.

**Q8. Where do SIM/LCA results go?**
Attach **SIM** metrics (LCA per ISO 14040/44, GHG Scopes 1/2/3) alongside each QOx run:
`domains/<CODE>/qox/<PHASE>/runs/<ts>/sim_lca/` and cite in ATA docs.

**Q9. What’s the minimal PR that passes gates?**

* New/updated CAx content with short README.
* Matching QOx problem (if applicable) and at least one run.
* QS/UTCS evidence blobs for the run(s).
* Updated ATA doc with links & hashes.
* Title/labels per styleguide; MAL-EEM must pass.

**Q10. Quick map for common systems**

* **Autoflight (ATA-22):** `domains/LCC` (controls) / `domains/IIS` (software).
* **Information Systems (ATA-46):** `domains/DDD` and `domains/IIS`.
* **Electrical Power (ATA-24):** `domains/EEE`.
* **Fuel/H₂ (ATA-28):** `domains/PPP` (on-board) and `domains/AAP` (ground).
* **Structures (ATA-51–57):** `domains/AAA` (airframe), `domains/MEC` (mech modules).

**Q11. Which quantum method should I pick?**

* **Routing/scheduling/layout:** QUBO/BQM → **Annealing/QAOA**.
* **Materials/chemistry:** **VQE**.
* **Large linear/PDE kernels:** **HHL/QLSA** (exploratory).

**Q12. Where do I put compliance & safety test artefacts?**
Under the **owning CAx phase** (`cax/CAT`, `cax/VP`, etc.) with links to the relevant **ATA** chapter folder; mirror any optimization in `qox/<PHASE>/…` and attach QS/UTCS.
