---
artifact: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/ATA_Impact_Analysis.md
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-AQUAOS-AIR-ATA-IMPACT
llc: SYSTEMS
maintainer: OOO (OS), LCC (Control Laws), EDI (Avionics)
project: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/ATA_Impact_Analysis.md
release_date: 2024-09-23
version: 1.0
---

# AQUA OS (Aircraft) — ATA Impact Analysis

## Overview

This document analyzes the impact of AQUA OS Aircraft Extension components across ATA (Air Transport Association) chapters and subjects, providing guidance for DMRL (Data Module Requirements List), PM (Publication Module) structure, and S1000D cross-references.

## 1. Component → ATA Chapter Mapping

| Component | Primary ATA | Secondary ATA | Impact Synopsis |
|-----------|-------------|---------------|-----------------|
| **QAFbW** | 27 Flight Controls | 22 Auto Flight, 31 Indicating/Recording, 42 IMA, 46 Info Systems, 24 Electrical, 57 Wings | Control laws, modes, envelope protection; exposes mode status to HMI; uses IMA platform; power/thermal & wiring; structural interfaces |
| **A653_PM** | 42 Integrated Modular Avionics | 31, 46 | Time & memory partitioning; certification assumptions; health reporting |
| **NET_STACK** | 42, 46 Information Systems | 31, 27 | VL/QoS, dual-net failover; network ICDs carrying safety-critical topics |
| **TIME_SYNC** | 42, 34 Navigation | 31 | Timebase distribution; GM switchover; affects timestamped signals and recorded data |
| **SEC_KMS** | 46 | 45 Central Maintenance, 31 | Secure boot & message auth; ground procedures and security logs |
| **UTCS_QS** | 46, 45 | 31 | Build/run sealing, provable config; maintenance audit trail |
| **HLTH_WD** | 45, 31 | 42 | Partition HB, BITE, dead-man actions; cockpit/CMC messages |
| **IO_ABS** | 42, 27 | 31 | Typed sensor/actuator endpoints; bounds/validity; wiring viewpoints |
| **LOG_TEL** | 31, 45 | 46 | DFDR/FOQA, prioritized DAL-A logs; maintenance retrieval |
| **MX_DIAG** | 45 | 31, 46 | CBIT/IBIT orchestration; fault injection guards; test interfaces |
| **CFG_STORE** | 46, 31 | 45 | Certified parameter sets; guarded updates; config hashes |
| **SW_UPDATE** | 46, 45 | 31 | Dual-bank image, rollback, sign/verify; maintenance tasks |
| **NAVSYS** | 34 Navigation | 27, 31, 42 | EKF/UKF fused state to QAFbW; degraded modes; status annunciations |
| **ACTR_GW** | 27, 24 (EHA) / 29 (EHSV) | 31, 42 | Bus endpoints, timeouts→safe; actuator feedback; power/hydraulic baseline |
| **HMI_BRIDGE** | 31 | 22, 27 | Mode and limits indication; inhibits on ground tests |
| **SIM_BRIDGE** | 45 | 31, 42 | Stimulus/capture interfaces; ground-only guards |
| **IETP_BRIDGE** | 45, 46 | 00/General | Opens DM/PM by ID; evidence of access if needed |
| **QAS_SUITE** | 46, 34 | 27 (read-only assist), 31 | Out-of-loop QRNG/QKD/sensors; benign-fail boundaries |

## 2. ATA Chapter Analysis

### ATA 27 — Flight Controls (Primary for QAFbW/ACTR_GW)

**Subjects:**
- 27-10 Aileron/Roll (elevon split for BWB)
- 27-20 Elevator/Pitch (elevon split for BWB) 
- 27-30 Yaw/Drag-rudder (if fitted)
- 27-50 High-Lift/Flaps (if present)
- 27-60 Spoilers/Speedbrakes (if applicable)
- 27-90 Control Laws/Feel/Trim

**Required Data Modules:**
- **Descriptive (D):** QAFbW Functional Architecture (modes, voter, envelope)
- **Schematic (S):** Network/Signal ICD (topics, VLs, timing, MAC)
- **Procedural (P):** Ground Tests (mode transitions, actuator loopback)
- **Test (T):** HIL/Iron Bird Acceptance Tests
- **Fault Isolation (F):** Fault Isolation (sensor loss, byzantine channel, timeout→safe)
- **Schematic (S):** Wiring/Interface to ACTR_GW & actuators

**Cross-References:**
- ↔ ATA 42 (IMA platform), 46 (ICDs), 34 (state inputs), 57 (structure attach/limits)
- ↔ ATA 24 or 29 (consistent with EHA/EHSV option)

### ATA 57 — Wings (Structure)

**Subjects:**
- 57-10 Wing Box
- 57-20 Ribs/Spars  
- 57-30 Control Surface Structures
- 57-40 Hinge/Actuator Fittings

**Required Data Modules:**
- **Descriptive (D):** Hinge-line geometry & envelope limits (structural)
- **Schematic (S):** Actuator mount loads & fastener specs
- **Procedural (P):** Inspection/torque procedures
- **Fault Isolation (F):** Structural fault indications vs control behavior

**Cross-References:**
- ↔ ATA 27 (command limits/envelope, actuator type/force, modes affecting load spectra)
- ↔ ATA 24/29 (service lines)
- ↔ ATA 45 (inspection procedures)

### ATA 24 — Electrical Power (EHA path)

**Subjects:**
- 24-00 General
- 24-20 AC Gen/Dist (if used)
- 24-30/40 DC Gen/Dist (incl. 270V HVDC)
- 24-50 Load Shedding/Quality

**Required Data Modules:**
- **Descriptive (D):** HVDC bus qualities, transients, PIU behavior
- **Schematic (S):** Power wiring to actuators, filters/EMI
- **Procedural/Test (P/T):** Bus sag/surge tests under worst-case QAFbW demand
- **Fault Isolation (F):** Power quality induced faults on control performance

**Cross-References:**
- ↔ ATA 27 (actuator loads), 42/46 (network/OS), 31 (annunciations), 45 (test procedures)

### ATA 29 — Hydraulics (EHSV path)

**Subjects:**
- 29-10 Power Sources (pumps)
- 29-20 Reservoirs
- 29-30 Accumulators
- 29-40 Distribution
- 29-50 Indications

**Required Data Modules:**
- **Descriptive (D):** Hyd circuit architecture feeding control surfaces
- **Schematic (S):** Line routing, clamps, contamination control
- **Procedural/Test (P/T):** Pressure/flow/thermal performance tests during flight-controls duty cycle
- **Fault Isolation (F):** Leak/jam/pressure loss effect on modes & reversion

**Cross-References:**
- ↔ ATA 27 (valves/servo specs), 57 (routing), 31 (indications), 45 (test procedures)

### ATA 31 — Indicating/Recording (HMI/Recording)

**Subjects:**
- 31-20 Displays/Annunciations
- 31-30 Recording (DFDR/QAR)
- 31-40 CMC messages

**Required Data Modules:**
- **Descriptive (D):** HMI mapping of QAFbW ModeStatus, limits, advisories
- **Schematic (S):** Recorded parameter lists (timestamps, rates)
- **Procedural (P):** Ground test display/CMC verification
- **Fault Isolation (F):** Indication-driven maintenance flows

**Cross-References:**
- ↔ ATA 27, 22 (mode status), 42 TIME_SYNC (timestamps), 46 LOG/UTCS (parameters), 45 (maintenance)

### ATA 22 — Auto Flight (if autopilot engages QAFbW)

**Subjects:**
- 22-10 Autopilot
- 22-20 Flight Director  
- 22-30 Autothrottle (if applicable)

**Required Data Modules:**
- **Descriptive (D):** Interface contract between A/P and QAFbW (authority, limits)
- **Procedural/Test (P/T):** Mode transitions with A/P engaged (no surprises)
- **Fault Isolation (F):** Disengage/limits behaviors and annunciations

**Cross-References:**
- ↔ ATA 27, 31 (mode interfaces), 45 (test procedures), 34 (navigation inputs)

### ATA 34 — Navigation (NAVSYS & time coupling)

**Subjects:**
- 34-10 Air Data
- 34-20 IRS/IMU
- 34-30 Radio Nav/GNSS

**Required Data Modules:**
- **Descriptive (D):** EKF/UKF fusion used by QAFbW; validity flags
- **Schematic (S):** Sensor interface specs (rates, accuracy, latency)
- **Procedural/Test (P/T):** Degraded nav modes effect on control
- **Fault Isolation (F):** Sensor miscompare handling

**Cross-References:**
- ↔ ATA 27 (navigation inputs), 42 NET/TIME_SYNC (sensor interfaces), 31 (status), 45 (testing)

### ATA 42 — Integrated Modular Avionics (platform)

**Subjects:**
- 42-10 Cabinet/Modules
- 42-20 Backplane/Network
- 42-30 Time Partitioning

**Required Data Modules:**
- **Descriptive (D):** A653 partitions (budgets), interference proofs
- **Schematic (S):** Network VL/QoS plan hosting critical topics
- **Test (T):** Overrun/overload tests; GM switchover

**Cross-References:**
- ↔ ATA 27, 46 (partition interfaces), 45 (testing), 31 (health reporting)

### ATA 45 — Central Maintenance System

**Subjects:**
- 45-10 CMC Architecture
- 45-20 BITE/Reports
- 45-30 Test Routines

**Required Data Modules:**
- **Descriptive (D):** Health & watchdog policy; event taxonomy
- **Procedural/Test (P/T):** IBIT/CBIT procedures; HIL/Iron Bird scripts
- **Fault Isolation (F):** Fault tree & isolation to LRU/SRU

**Cross-References:**
- ↔ ATA 27, 31, 46 (health monitoring), 24/29 (power/hydraulic testing)

### ATA 46 — Information Systems (ICDs, Security, Evidence)

**Subjects:**
- 46-10 Data Distribution
- 46-20 Security
- 46-30 Configuration/Update
- 46-40 Evidence/Trace

**Required Data Modules:**
- **Descriptive (D):** ICD master (topics, payloads, auth/MAC)
- **Descriptive (D):** Security architecture (boot, KMS, keys)
- **Procedural (P):** SW load/update & rollback procedures
- **Descriptive (D):** UTCS/QS sealing workflow; audit retrieval

**Cross-References:**
- ↔ ATA 27, 42 (ICDs), 45, 31 (security events, software updates)

## 3. Critical Cross-Reference Patterns

### 27 ↔ 57 "Story" (Flight Controls ↔ Wings)

**Key Bidirectional Links:**
- ATA-27 "Control Surface Authority & Limits (QAFbW)" ↔ ATA-57 "Hinge/Actuator Structural Limits"
  - *Reason:* Command envelopes must not exceed structural limits
- ATA-27 "Actuator Interface & Loads" ↔ ATA-57 "Actuator Fitting Load Paths & Fasteners"  
  - *Reason:* Mounting and torsion paths must align with commanded torques
- ATA-27 "Ground Functional Test – Surfaces" ↔ ATA-57 "Post-Adjustment Inspection/Torque"
  - *Reason:* Every rigging/repair step must verify command/response integrity

### Option A vs B Impact (EHA vs EHSV)

| Area | EHA (270V HVDC) | EHSV (5000 psi Hyd.) |
|------|-----------------|----------------------|
| **Primary power chapter** | ATA 24 heavy (quality, EMC, thermal near actuators) | ATA 29 heavy (routing, contamination, leak safety) |
| **Wiring/Schemes** | 24 (HVDC harness, filters) + 27 | 29 (pressure lines, fittings) + 27 |
| **Faults** | Voltage sag/surge → 27 modes | Pressure loss/jam → 27 modes |
| **Tests** | Bus transient under max duty (24/27/45) | Pressure/flow/thermal cycles (29/27/45) |

## 4. DMRL Seed Content

**ATA-27 (Flight Controls):**
- D: QAFbW Functional Architecture & Modes
- D: Network & Signal ICD for Flight-Controls Topics
- S: Actuator Interface & Feedback (EHA/EHSV variant)
- P: Ground Functional Test – Mode Transitions & Limits
- T: HIL Acceptance – Latency/Jitter/Failover
- F: Fault Isolation – Sensor Disagree/Timeout/Byzantine

**ATA-57 (Wings):**
- D: Control Surface Structure & Hinge-Line Geometry
- S: Actuator Mounting & Load Path Specification
- P: Inspection & Torque after Rigging/Repair
- F: Structural Fault Indications & Control Effects

**ATA-24/29 (Power):**
- D: (24) HVDC Bus Spec & EMI Mitigation or (29) Hyd Circuit Architecture
- P/T: Transient/Pressure-Flow Endurance during Control Duty
- F: Power-Induced Effects on Control Modes

**ATA-31 (Indicating/Recording):**
- D: Annunciations for QAFbW Modes & Envelope Events
- S: DFDR/QAR Parameter Set & Timebase
- P: CMC Verification – Events & Codes

**ATA-42 (IMA):**
- D: Partition Budgets & Interference Protections
- S: VL/QoS Plan Hosting Critical Topics
- T: Overrun/GM Switchover Robustness

**ATA-45 (Maintenance):**
- D: BITE/Event Taxonomy, Health Policies
- P: IBIT/CBIT & Iron Bird Script Library
- F: Fault Trees to LRU/SRU level

**ATA-46 (Info Systems/Security/Evidence):**
- D: ICD Master & Auth/MAC Profiles
- D: Security Architecture (Boot/KMS/Keys)
- P: SW Load/Update & Rollback
- D: UTCS/QS Evidence & Retrieval

**ATA-34 (Navigation):**
- D: NAVSYS Fusion & Validity Flags
- P/T: Degraded Nav Impact on QAFbW
- F: Sensor Miscompare Handling

## 5. S1000D IETP Integration Guidelines

### Cross-Reference Implementation
- Use explicit `<dmRef>` in ATA-27 and ATA-57 DMs where surface authority/limits or actuator mounts are discussed
- Include `<crossRefs>` blocks in ATA-27 PM "Interfaces" chapter referencing ATA-24/29, ATA-42/46, ATA-34, ATA-31
- Generate `dm_index.xml` from DMRL/CSV for automatic External Reference population
- Maintain reverse links in ATA-24/29/42/46 when carrying QAFbW-critical contracts

### Publication Module Structure
- Organize PMs by ATA chapter with consistent `<content>`, `<refs>`, and `<crossRefs>` blocks
- Ensure bidirectional linking between related chapters (especially 27↔57)
- Use conditional references for optional content (EHA vs EHSV variants)

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*