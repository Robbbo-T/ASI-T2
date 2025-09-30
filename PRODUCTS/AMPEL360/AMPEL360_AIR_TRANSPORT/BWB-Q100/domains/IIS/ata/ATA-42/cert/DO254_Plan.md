---
id: BWB-Q100-ATA42-DO254-HDP
project: AMPEL360_AIR_TRANSPORT / BWB-Q100
artifact: DO-254 Hardware Development Plan (HDP)
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

# DO‑254 Hardware Development Plan (HDP) — ATA‑42 · IMA

**Back to ATA‑42:** [../README.md](../README.md)  
**Related planning docs:** [PHAC — Plan for Hardware Aspects of Certification](PHAC.md) *(if separate)* · [HVVP — Hardware Verification & Validation Plan](HVVP.md) · [CMP — Configuration Management Plan](CMP.md) · [PAP — Process Assurance Plan](PAP.md)  
**Environmental:** [DO‑160G Summary](DO160G_Qual_Summary.md) · **Buses:** [AFDX VL table](../buses/afdx/vl_table.csv), [ARINC‑429 channel map](../buses/a429/channel_map.csv)  
**Software:** [DO‑178C PSAC](../verification/DO178C_PSAC.md) *(for software partitions running on IMA)*

> Scope: complex electronic hardware (CEH) within the IMA (e.g., FPGA‑based AFDX/A429 I/O, backplane controllers, timing/synchronization logic). This plan defines lifecycle processes, data, roles, independence, and verification objectives to satisfy DO‑254/ED‑80 and authority guidance (e.g., FAA/EASA).

---

## 1) Applicability & DAL

| Item | Value |
|------|-------|
| Certification basis | DO‑254 / ED‑80, with EASA AMC 20‑152A / FAA guidance as applicable |
| Hardware scope | FPGAs for AFDX switch, ARINC‑429 I/O, partition health monitor, timing/sync |
| Design Assurance Level | Level A (flight-critical functions via P‑FBW partition) |
| Simple/Complex | **Complex** — programmable logic, ASIC, custom state machines |

---

## 2) Hardware Life Cycle Overview

```
Requirements → Design → Implementation → Verification → Transition to Production
   ↑              ↑           ↑              ↑                     ↑
   └──────────────┴───────────┴──────────────┴─────────────────────┘
                    Configuration Management + Process Assurance
```

**Planning documents:**
- Hardware Development Plan (HDP) — *this document*
- PHAC (Plan for Hardware Aspects of Certification) — certification liaison
- HVVP (Hardware Verification Plan) — test & analysis strategy
- CMP (Configuration Management Plan) — baselines, change control
- PAP (Process Assurance Plan) — independence, audits, reviews

---

## 3) Requirements Capture & Traceability

**Sources:**
- System requirements from ATA‑42 README (partition isolation, timing, I/O rates)
- Derived requirements: FPGA clock domains, power sequencing, error detection
- Interface requirements: ARINC‑653 HSI, AFDX frames, ARINC‑429 labels

**Tools:**
- DOORS or equivalent for requirement management
- Traceability matrix: `HW_Req_Trace.xlsx`

**Review gates:**
- Preliminary Design Review (PDR)
- Critical Design Review (CDR)

---

## 4) Design (HDL, Schematics, Timing)

**Deliverables:**
- FPGA HDL source (VHDL/Verilog) with coding standards (e.g., ESA guidelines)
- Block diagrams, state machines, timing diagrams
- ASIC/FPGA constraints (clock frequency, I/O loading, power)
- Interface Control Documents (ICDs) for AFDX, ARINC‑429, backplane

**Standards:**
- FPGA coding: no latches, synchronous resets, clock domain crossing mitigation
- Safety patterns: redundancy, watchdog timers, parity/ECC

---

## 5) Implementation & Synthesis

**Process:**
- Synthesis with vendor tools (Xilinx Vivado, Intel Quartus, etc.)
- Place & route with timing closure
- Bitstream generation with checksum/signature

**Validation:**
- Logic equivalence checking (LEC) between RTL and netlist
- Timing analysis (static timing analysis — STA)
- Power analysis

---

## 6) Verification (DO‑254 Tables A‑1 to A‑10)

**Methods:**
- **Requirements-based testing** — functional test cases per HW requirement
- **Hardware/software integration testing** — ARINC‑653 partition I/O
- **Worst-case analysis** — timing margins, power supply variation
- **Fault injection** — SEU/bit-flip, stuck-at faults (if applicable)

**Coverage:**
- Structural coverage (MCDC for Level A per DO‑254 Supplement)
- Functional coverage per HVVP

**Independence:**
- Verification team independent of design team (organizational or contract)

---

## 7) Configuration Management

**Baseline items:**
- Requirements documents
- HDL source code
- Synthesis/P&R scripts
- Test procedures and results
- FPGA bitstreams (signed, with SHA-256 hash)

**Change control:**
- Problem reports (PR), change requests (CR) tracked in tool (Jira, ALM)
- CCB (Configuration Control Board) approval for baseline changes

---

## 8) Process Assurance & Quality

**Activities:**
- Audits of lifecycle data for completeness
- Reviews: PDR, CDR, Test Readiness Review (TRR)
- Tool qualification if automated (per DO‑330 for software tools, by analogy for HW)

**Independence:**
- QA reports directly to program management (not design lead)

---

## 9) Hardware/Software Interface (HSI)

**Coordination with DO‑178C (Software):**
- Partition memory maps, I/O register definitions
- Timing constraints for ARINC‑653 windows
- Health monitor API and error reporting

**Document:** `interfaces/HSI/HSI_Spec.md`

---

## 10) Certification Liaison

**Authority engagement:**
- Stage of Involvement (SOI) — early consultation on novel FPGA usage
- Means of Compliance (MOC) — clarify DO‑254 applicability for AFDX switch logic
- SOI meetings documented in `cert/SOI_Meeting_Minutes/`

---

## 11) Transition to Production

**Deliverables:**
- Acceptance Test Procedures (ATP) for production units
- Hardware Accomplishment Summary (HAS)
- Hardware Configuration Index (HCI)
- Hardware Life Cycle Environment Configuration Index (HLECI)

**Production control:**
- FPGA bitstream programming and verification
- Board-level test (BIT/BIST execution)

---

## 12) Roles & Responsibilities

| Role | Responsibility |
|------|----------------|
| HW Project Manager | Schedule, budget, resource allocation |
| HW Design Lead | Architecture, HDL design, design reviews |
| Verification Lead | HVVP execution, test case development |
| Configuration Manager | Baseline control, change tracking |
| Quality Assurance | Process audits, independence verification |
| Certification Engineer | Authority liaison, SOI/MOC coordination |

---

## 13) Schedule & Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| HDP approval | 2025-Q1 | Planned |
| PDR | 2025-Q2 | Planned |
| CDR | 2025-Q3 | Planned |
| Verification complete | 2026-Q1 | Planned |
| HAS/HCI delivery | 2026-Q2 | Planned |

---

## 14) UTCS/QS Evidence

- All lifecycle data signed with QS anchors
- Traceability to DO‑254 objectives maintained in tool
- Independent verification results archived with DET anchors

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.2.0 | 2025-09-29 | IIS | Expanded HDP with DO‑254 structure and roles |
| 0.1.0 | 2025-09-28 | IIS | Initial placeholder |