---
id: BWB-Q100-ATA42-SAF-FHA-PSSA-SSA
project: AMPEL360_AIR_TRANSPORT / BWB-Q100
artifact: Safety Analysis — FHA · PSSA · SSA (ATA-42 · IMA)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.2.0
release_date: 2025-09-29
maintainer: IIS (Avionics / IMA)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# Safety Analysis — ARP4754A/ARP4761 Evidence (ATA‑42 · IMA)

**Back to ATA‑42:** [../README.md](../README.md)  
**Related:** [DO‑178C PSAC](../verification/DO178C_PSAC.md) · [DO‑254 Plan](../cert/DO254_Plan.md) · [DO‑160G Summary](../cert/DO160G_Qual_Summary.md) · [DO‑297 Responsibility Agreement](../cert/DO297_Responsibility_Agreement.md)  
**Interfaces:** [AFDX VL table](../buses/afdx/vl_table.csv) · [ARINC‑429 channel map](../buses/a429/channel_map.csv) · [ARINC‑653 schedule](../os/schedule.xml) · [HSI Spec](../interfaces/HSI/HSI_Spec.md)

> Scope: System‑level safety analysis for **Integrated Modular Avionics (IMA)** on BWB‑Q100, covering **FHA**, **PSSA**, and **SSA**. This document is the entry point; detailed analyses (FTA/FMEA/CCA/ZSA/PRA) are referenced from `safety/analyses/`.

---

## 1) Operational Context & Assumptions

| Item | Value | Notes |
|------|-------|-------|
| Aircraft phase | All phases (TO, climb, cruise, approach, landing) | worst‑case considered per phase |
| Installation | Pressurized avionics bay | DO‑160G categories per summary |
| Architecture | IMA chassis with ARINC‑653 partitions | Time/space isolation verified |
| Redundancy | Dual AFDX networks (A/B), cross-channel monitoring in P‑FBW | Single IMA chassis (future: dual-chassis option) |
| Crew actions | Assume normal crew per operations manual | No single-pilot operations |

---

## 2) Functional Hazard Assessment (FHA)

**Objective:** Identify system-level functions, failure conditions, and severity classification.

### 2.1) Functions Allocated to IMA

| Function ID | Function | Partition(s) | Failure Condition (example) | Severity |
|-------------|----------|--------------|----------------------------|----------|
| F‑FBW‑01 | Primary flight control (pitch/roll/yaw) | P‑FBW | Loss of flight control | **Catastrophic** |
| F‑FBW‑02 | Control law limiting (envelope protection) | P‑FBW | Erroneous limit → control reversal | **Hazardous** |
| F‑NAV‑01 | Attitude/airspeed/altitude computation | P‑NAV | Erroneous attitude → spatial disorientation | **Hazardous** |
| F‑NAV‑02 | GNSS/INS fusion | P‑NAV | Loss of position → navigation error | **Major** |
| F‑DISP‑01 | Primary Flight Display (PFD) | P‑DISP | Loss of PFD → degraded situational awareness | **Major** |
| F‑DISP‑02 | Navigation Display (ND) | P‑DISP | Misleading display → navigation error | **Major** |
| F‑MAINT‑01 | Central Maintenance System (CMS) | P‑MAINT | Loss of fault logging → delayed maintenance | **Minor** |
| F‑SEC‑01 | Cryptographic key management | P‑SEC | Key compromise → integrity loss | **Hazardous** |

**DAL Allocation (per ARP4754A Table 2):**
- **Catastrophic** → DAL‑A (P‑FBW primary control)
- **Hazardous** → DAL‑B (P‑FBW limiting, P‑NAV, P‑SEC)
- **Major** → DAL‑C (P‑DISP)
- **Minor** → DAL‑D (P‑MAINT)

---

## 3) Preliminary System Safety Assessment (PSSA)

**Objective:** Allocate safety requirements, define architecture, identify compliance means.

### 3.1) Architecture Safety Strategy

- **Partition isolation (ARINC‑653):** Time/space partitioning prevents fault propagation
  - MMU/MPU enforces memory boundaries
  - Deterministic scheduling (see [`../os/schedule.xml`](../os/schedule.xml))
  - Health Monitor (HM) detects partition errors and applies recovery (restart/shutdown)

- **Communication isolation:**
  - AFDX VL policing (see [`../buses/afdx/vl_table.csv`](../buses/afdx/vl_table.csv)) — bandwidth-limited, sink-restricted
  - ARINC‑429 channel assignment (no cross-talk)

- **Redundancy:**
  - Dual AFDX networks (A/B) for flight-critical VLs
  - P‑FBW monitors cross-channel for dissimilarity

### 3.2) Safety Requirements (derived)

| Req ID | Requirement | Allocation | Verification Method |
|--------|-------------|------------|---------------------|
| SR‑IMA‑01 | Partition isolation ≥10⁻⁹ per flight hour | ARINC‑653 RTOS | Interference test + analysis |
| SR‑IMA‑02 | P‑FBW timing jitter ≤100 µs | Scheduler | Static timing analysis |
| SR‑IMA‑03 | AFDX frame loss ≤10⁻⁷ | VL policing | Network test |
| SR‑IMA‑04 | Health Monitor detects partition hang ≤2× major frame | HM logic | Fault injection test |
| SR‑IMA‑05 | No single point failure → Catastrophic | System arch | FTA, CCA |

### 3.3) Preliminary FTA/FMEA

**Documents:**
- `safety/analyses/FTA_P-FBW_Loss.pdf` — Fault Tree for loss of P‑FBW
- `safety/analyses/FMEA_IMA_Platform.xlsx` — FMEA for IMA hardware

**Top Event (example):** Loss of Primary Flight Control  
**Intermediate Events:**
- P‑FBW partition fail (OR)
  - SW bug in control law (mitigated by DO‑178C DAL‑A)
  - ARINC‑653 scheduler fail (mitigated by DO‑178C DAL‑A for RTOS)
  - Memory corruption (mitigated by MMU + ECC)
- Actuation commands not transmitted (OR)
  - AFDX switch fail (mitigated by redundancy A/B)
  - VL‑FBW‑CMD corrupted (mitigated by frame CRC)

---

## 4) Common Cause Analysis (CCA)

**Objective:** Ensure partitions with different DALs do not share single-point failures.

### 4.1) Shared Resources

| Resource | Partitions | Mitigation |
|----------|------------|------------|
| CPU | All | Time isolation (ARINC‑653 schedule), HM watchdog |
| RAM | All | Space isolation (MMU), ECC for transient faults |
| AFDX backplane | All | VL policing, dual networks for critical VLs |
| Power supply | All | Input transient protection (DO‑160G), backup 28VDC for HM |

**CCA Conclusion:** No single hardware failure causes loss of both P‑FBW (DAL‑A) and P‑NAV (DAL‑B) due to:
- Partition isolation (SW faults do not propagate)
- Dual AFDX networks (network faults tolerated)
- HM restarts failing partitions without affecting others

### 4.2) Zonal Safety Analysis (ZSA)

**Zone:** Avionics bay (forward fuselage)  
**Hazards:** Fire, smoke, thermal runaway, water ingress  
**Mitigations:**
- Fire detection & suppression per ATA‑26
- Sealed enclosure (DO‑160G waterproofness)
- Thermal monitoring (shutdown if >85°C)

**Document:** `safety/analyses/ZSA_Avionics_Bay.pdf`

---

## 5) System Safety Assessment (SSA)

**Objective:** Verify safety requirements implemented, close safety loop.

### 5.1) Verification Activities

| Activity | Document | Status |
|----------|----------|--------|
| Partition interference test | `../verification/Partition_Isolation_Report.pdf` | Planned 2025‑Q3 |
| AFDX network test (loss rate, latency) | `../verification/AFDX_Network_Test_Report.pdf` | Planned 2025‑Q3 |
| Fault injection (HM response) | `../verification/HM_Fault_Injection_Report.pdf` | Planned 2025‑Q4 |
| FTA quantification | `safety/analyses/FTA_Quantification.xlsx` | Planned 2025‑Q4 |
| Flight test (operational scenarios) | `../verification/Flight_Test_Report.pdf` | Planned 2026‑Q1 |

### 5.2) Compliance Matrix (ARP4754A)

| Objective | Standard | Status | Evidence |
|-----------|----------|--------|----------|
| System development processes | ARP4754A § 4 | In progress | This document (FHA/PSSA/SSA) |
| Safety assessment | ARP4754A § 5 | In progress | FTA/FMEA/CCA/ZSA |
| Requirements capture & traceability | ARP4754A § 6 | In progress | DOORS trace matrix |
| Implementation (HW) | DO‑254 | In progress | [DO‑254 Plan](../cert/DO254_Plan.md) |
| Implementation (SW) | DO‑178C | In progress | [DO‑178C PSAC](../verification/DO178C_PSAC.md) |
| Verification & validation | ARP4754A § 7 | Planned | Integration & flight test |

---

## 6) Probabilistic Risk Assessment (PRA)

**Method:** Combine FTA quantitative results with FMEA failure rates.

**Target:**
- **Catastrophic:** ≤10⁻⁹ per flight hour
- **Hazardous:** ≤10⁻⁷ per flight hour
- **Major:** ≤10⁻⁵ per flight hour

**Assumptions:**
- HW failure rates per MIL-HDBK-217 or supplier data
- SW failure rates per industry consensus (e.g., 10⁻⁴ per hour for DAL‑A with full DO‑178C)

**Document:** `safety/analyses/PRA_Summary.xlsx`

---

## 7) Safety Monitoring & Operational Feedback

**In-service monitoring:**
- P‑MAINT logs HM events (partition restarts, timing violations)
- ACMS data analyzed for trends (e.g., transient memory errors)

**Safety review board:**
- Quarterly review of service bulletins, problem reports
- Trigger for SSA re-assessment if failure rates exceed predictions

---

## 8) UTCS/QS Evidence Chain

- All safety analyses signed with UTCS DET anchors
- Traceability: FHA → PSSA → SSA → verification results
- Independent review by safety engineer (not design team)

---

## 9) Cross-References

- **System architecture:** [ATA‑42 README](../README.md)
- **Hardware:** [DO‑254 Plan](../cert/DO254_Plan.md)
- **Software:** [DO‑178C PSAC](../verification/DO178C_PSAC.md)
- **Environmental:** [DO‑160G Summary](../cert/DO160G_Qual_Summary.md)
- **Responsibility:** [DO‑297 Agreement](../cert/DO297_Responsibility_Agreement.md)

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.2.0 | 2025-09-29 | IIS | Expanded FHA/PSSA/SSA with FTA/CCA/ZSA structure |
| 0.1.0 | 2025-09-28 | IIS | Initial placeholder |