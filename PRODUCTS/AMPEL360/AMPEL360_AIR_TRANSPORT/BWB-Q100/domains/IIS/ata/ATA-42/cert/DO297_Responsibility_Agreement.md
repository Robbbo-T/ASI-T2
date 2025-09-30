---
id: BWB-Q100-ATA42-DO297-RA
project: AMPEL360_AIR_TRANSPORT / BWB-Q100
artifact: DO-297 IMA Responsibility Agreement (Roles, Interfaces, Evidence)
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

# DO‑297 IMA Responsibility Agreement — BWB‑Q100 (ATA‑42)

**Back to ATA‑42:** [../README.md](../README.md)  
**Related plans:** [DO‑178C PSAC](../verification/DO178C_PSAC.md) · [DO‑254 HDP](DO254_Plan.md) · [DO‑160G Summary](DO160G_Qual_Summary.md)  
**Interfaces:** [AFDX VL table](../buses/afdx/vl_table.csv) · [ARINC‑429 channel map](../buses/a429/channel_map.csv) · [HSI Spec](../interfaces/HSI/HSI_Spec.md)

> This agreement defines **responsibilities, interfaces, independence, and evidence** across the **IMA Platform Supplier**, **Application Software Supplier(s)**, and the **Aircraft OEM/System Integrator** for BWB‑Q100, consistent with **DO‑297/ED‑124** guidance. It aims to avoid "responsibility gaps," ensure traceable **partition isolation**, and streamline **certification credit** with authorities.

---

## 1) Parties & Roles

| Role | Abbrev | Responsibilities (high‑level) |
|------|--------|-------------------------------|
| Aircraft OEM / System Integrator | OEM | System safety allocation, IMA platform selection, ICD ownership, integration, flight test, certification liaison |
| IMA Platform Supplier | PLAT | ARINC‑653 RTOS, backplane/chassis HW, health monitoring, partition isolation, DO‑178C/DO‑254 for platform SW/HW |
| Application Software Suppliers | APP | Partition code (P‑FBW, P‑NAV, P‑DISP, P‑MAINT, P‑SEC), DO‑178C per partition DAL, functional test data |
| Certification Authority | AUTH | Issue Type Certificate (TC) or Supplemental TC (STC), approve MOC/SOI, witness key tests |

---

## 2) System-Level Safety Allocation (OEM)

**Owner:** OEM  
**Deliverables:**
- FHA/PSSA/SSA per ARP4754A (see [`../safety/FHA_PSSA_SSA.md`](../safety/FHA_PSSA_SSA.md))
- DAL allocation to partitions (P‑FBW → DAL‑A, P‑NAV → DAL‑B, etc.)
- IMA resource budgets (CPU%, RAM, I/O) derived from safety analysis

**Interface to PLAT:**
- OEM specifies partition isolation requirements (time/space, memory protection, I/O segregation)
- PLAT demonstrates compliance via ARINC‑653 conformance test + health monitoring

**Interface to APP:**
- OEM provides partition functional requirements and DAL
- APP develops to DO‑178C per assigned DAL

---

## 3) IMA Platform Responsibilities (PLAT)

**Owner:** IMA Platform Supplier  
**Scope:**
- ARINC‑653 RTOS (kernel, scheduler, health monitor, partition manager)
- Hardware: chassis, backplane, CM/CCMs, power, cooling, AFDX/A429 I/O cards
- DO‑178C (DAL‑A for kernel), DO‑254 (for complex HW — FPGAs), DO‑160G environmental

**Deliverables:**
- ARINC‑653 configuration table (schedules, memory maps, port definitions) — see [`../os/schedule.xml`](../os/schedule.xml)
- Health Monitoring (HM) table — partition error responses (restart, shutdown, etc.)
- Hardware/Software Integration (HSI) document — memory-mapped I/O, API, timing constraints
- PSAC/SAS for platform SW, HDP/HAS for platform HW

**Interfaces:**
- **To OEM:** ICD for backplane power, cooling airflow, mounting dimensions
- **To APP:** HSI, ARINC‑653 API (APEX), port definitions (sampling/queueing)

**Certification credit:**
- PLAT supplies SAS/HAS to OEM; OEM integrates into system-level cert dossier
- No "black box" — all lifecycle data (requirements, design, test) traceable per DO‑297

---

## 4) Application Software Responsibilities (APP)

**Owner:** Each partition supplier (may be OEM internal or external)

| Partition | Supplier (example) | DAL | Deliverables |
|-----------|-------------------|-----|--------------|
| P‑FBW | OEM or Tier-1 | A | PSAC, SAS, DO‑178C artifacts (SCMP/SQA/SVP/SCI) |
| P‑NAV | Avionics supplier | B | PSAC, SAS, DO‑178C artifacts (reduced per DAL‑B) |
| P‑DISP | Display OEM | C | PSAC, SAS, DO‑178C artifacts (reduced per DAL‑C) |
| P‑MAINT | Maintenance SW vendor | D | PSAC, SAS, minimal verification |
| P‑SEC | Security module supplier | B | PSAC, SAS, DO‑356A security verification |

**Interface to PLAT:**
- APP uses ARINC‑653 API (APEX) only — no direct HW access
- APP provides partition budgets (CPU%, RAM, ports) for scheduling
- APP validates partition behavior on target RTOS via integration test

**Interface to OEM:**
- APP delivers object code + SAS
- OEM performs integration test (cross-partition, AFDX/A429 end-to-end)

**Certification credit:**
- Each APP supplies standalone SAS; OEM bundles into aircraft-level cert package
- Independence: APP verification team independent of APP design team

---

## 5) Interfaces & ICDs

| ICD | Owner | Content | Link |
|-----|-------|---------|------|
| AFDX Virtual Links | OEM | VL table, BAG, sinks, redundancy | [`../buses/afdx/vl_table.csv`](../buses/afdx/vl_table.csv) |
| ARINC‑429 Channels | OEM | RX/TX channels, labels, rates | [`../buses/a429/channel_map.csv`](../buses/a429/channel_map.csv) |
| HSI (HW/SW Interface) | PLAT | Memory map, I/O registers, timing | `../interfaces/HSI/HSI_Spec.md` |
| Partition APIs | PLAT | ARINC‑653 APEX calls, error codes | `../interfaces/APEX/APEX_Ref.md` |
| Health Monitoring | PLAT | HM table, partition restart policy | `../os/HM_Table.xml` |

---

## 6) Partition Isolation Verification

**Responsibility:** PLAT (with OEM witness)

**Methods:**
- **Time isolation:** schedule analysis (windows non-overlapping, deterministic)
- **Space isolation:** MMU/MPU config, memory access tests (write to other partition → HM error)
- **I/O isolation:** AFDX VL policing, ARINC‑429 channel assignment
- **Interference testing:** resource exhaustion (one partition hogs CPU/RAM → no impact on others)

**Evidence:**
- Partition interference test report
- ARINC‑653 conformance test results
- Static analysis of schedule (tool-based)

**Document:** `../verification/Partition_Isolation_Report.pdf`

---

## 7) Configuration Management & Change Control

**Ownership:**

| Item | Owner | Change Control |
|------|-------|----------------|
| System requirements (FHA/PSSA) | OEM | OEM CCB |
| IMA platform SW/HW baseline | PLAT | PLAT CCB → OEM notified |
| Partition SW baseline | APP | APP CCB → OEM notified |
| ARINC‑653 config (schedule, HM) | OEM | OEM CCB (with PLAT/APP input) |
| AFDX/A429 ICDs | OEM | OEM CCB |

**Traceability:** All baselines tracked in CM tool (DOORS, Jira, ALM); changes linked to PRs/CRs.

---

## 8) Certification Liaison & Authority Engagement

**Lead:** OEM (with PLAT/APP support)

**Activities:**
- **Stage of Involvement (SOI):** early meetings with FAA/EASA DER on novel IMA usage
- **Means of Compliance (MOC):** agree on DO‑178C/DO‑254 applicability per partition
- **Compliance Checklist:** per AC 20-170 or EASA CM-SWCEH-001
- **Witness tests:** authority may witness partition isolation, environmental (DO‑160G), or flight tests

**Documents:**
- `cert/SOI_Meeting_Minutes/`
- `cert/Compliance_Checklist.xlsx`

---

## 9) Evidence Flow & Deliverables

```
  OEM (System Integrator)
    ├─ FHA/PSSA/SSA (ARP4754A)
    ├─ Integration Test Reports
    ├─ Flight Test Data
    └─ Aircraft-level PSAC
        ├─ PLAT SAS/HAS (DO‑178C/DO‑254)
        ├─ APP1 SAS (P‑FBW, DAL‑A)
        ├─ APP2 SAS (P‑NAV, DAL‑B)
        ├─ APP3 SAS (P‑DISP, DAL‑C)
        ├─ APP4 SAS (P‑MAINT, DAL‑D)
        └─ APP5 SAS (P‑SEC, DAL‑B)
```

**Format:** Each SAS includes:
- Software Accomplishment Summary (SAS) or Hardware Accomplishment Summary (HAS)
- Verification results, coverage data, tool qualification
- Configuration index, problem reports summary

---

## 10) Responsibility Matrix

| Activity | OEM | PLAT | APP | AUTH |
|----------|-----|------|-----|------|
| System safety (FHA/PSSA/SSA) | **R** | C | C | A |
| DAL allocation | **R** | C | I | A |
| IMA platform SW/HW development | I | **R** | I | A |
| Partition SW development | C | I | **R** | A |
| ARINC‑653 config (schedule/HM) | **R** | C | C | A |
| Integration test | **R** | C | C | I |
| Flight test | **R** | I | I | A |
| Certification package assembly | **R** | C | C | — |
| Authority approval | I | I | I | **R** |

**Legend:** R = Responsible, A = Approves, C = Contributes, I = Informed

---

## 11) Independence Requirements

**DO‑178C/DO‑254 independence:**
- Verification activities independent of design (different person/team)
- QA independent of project management

**Inter-party independence:**
- APP verification team ≠ APP design team
- PLAT verification team ≠ PLAT design team
- OEM integration test team ≠ system design team (if practical)

---

## 12) UTCS/QS Evidence Chain

- All lifecycle data (requirements, design, test) signed with UTCS DET anchors
- Traceability maintained in CM tool with SHA-256 hashes
- Each party (OEM/PLAT/APP) maintains provenance logs per `../configs/sbom/`

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.2.0 | 2025-09-29 | IIS | Expanded DO‑297 agreement with detailed roles and evidence flow |
| 0.1.0 | 2025-09-28 | IIS | Initial placeholder |