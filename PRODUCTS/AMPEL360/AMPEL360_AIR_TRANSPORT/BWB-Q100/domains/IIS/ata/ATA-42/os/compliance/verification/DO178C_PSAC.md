---
id: BWB-Q100-ATA42-DO178C-PSAC
project: AMPEL360_AIR_TRANSPORT / BWB-Q100
artifact: DO-178C Plan for Software Aspects of Certification (PSAC)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.3.0
release_date: 2025-09-29
maintainer: IIS (Avionics / IMA)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# DO‑178C Plan for Software Aspects of Certification (PSAC)

**Back to ATA‑42:** [../README.md](../README.md)  
**Related:** [DO‑254 Hardware Dev Plan](../cert/DO254_Plan.md) · [DO‑160G Summary](../cert/DO160G_Qual_Summary.md) · [DO‑297 Responsibility Agreement](../cert/DO297_Responsibility_Agreement.md) · [Security Plans (DO‑326A/356A)](../security/SEC_Plans.md)  
**Interfaces:** [ARINC‑653 schedule](../os/schedule.xml) · [AFDX VL table](../buses/afdx/vl_table.csv) · [ARINC‑429 channel map](../buses/a429/channel_map.csv)

> Scope: This PSAC defines processes, data, roles, and evidence for the **Integrated Modular Avionics (IMA)** software partitions of **BWB‑Q100** to comply with **DO‑178C/ED‑12C**. It covers planning, development, verification, configuration management, quality assurance, and certification liaison. Hardware aspects are addressed in DO‑254; airworthiness security in DO‑326A/356A.

---

## 1) Software Items & DAL Allocation

| Partition (SW Item) | Function (summary) | DAL | Standards/Notes |
|---------------------|-------------------|-----|-----------------|
| P‑FBW | Flight‑by‑wire control laws, monitors, command limiting | A | Highest integrity; MC/DC; independence; deterministic timing |
| P‑NAV | INS/GNSS fusion, attitude/airspeed computation | B | MC/DC not required; decision coverage; reduced verification |
| P‑DISP | PFD/ND rendering, crew alerting | C | Statement coverage; simplified verification |
| P‑MAINT | ACMS/CMS logging, snapshot archival | D | Minimal verification; functional test only |
| P‑SEC | Cryptographic services, key mgmt, attestation | B | MC/DC not required; security-focused review; FIPS 140-2 compliance |
| ARINC‑653 RTOS | Kernel, scheduler, health monitor, partition manager | A | Platform SW (supplier); critical for partition isolation |

**Rationale:** DAL derived from FHA (see [`../safety/FHA_PSSA_SSA.md`](../safety/FHA_PSSA_SSA.md)). P‑FBW failure → Catastrophic → DAL‑A. P‑NAV/P‑SEC failure → Hazardous → DAL‑B. P‑DISP failure → Major → DAL‑C. P‑MAINT failure → Minor → DAL‑D.

---

## 2) Software Life Cycle Overview

```
Planning → Requirements → Design → Implementation → Integration → Verification → Transition to Production
   ↑           ↑             ↑           ↑                ↑              ↑                   ↑
   └───────────┴─────────────┴───────────┴────────────────┴──────────────┴───────────────────┘
                    Configuration Management + Quality Assurance + Certification Liaison
```

**Supporting processes (per DO‑178C § 11):**
- Software Configuration Management (SCM) — baselines, change control
- Software Quality Assurance (SQA) — audits, reviews, independence
- Certification Liaison (CL) — authority engagement, SOI/MOC

---

## 3) Software Development Plan (SDP)

**Objective:** Define lifecycle processes, standards, and tools for each partition.

### 3.1) Development Standards

**Coding:**
- **Language:** C (ISO/IEC 9899:2011, subset per MISRA C:2012)
- **Style:** Max cyclomatic complexity 15, function length ≤200 LOC, no recursion (DAL‑A/B)
- **Libraries:** Qualified math library (libm subset), no dynamic allocation in DAL‑A/B

**Design:**
- Structured design (data flow diagrams, state machines)
- Low-level requirements (LLR) traceable to high-level requirements (HLR)
- Design representation: UML or equivalent, reviewed at CDR

**Tools:**
- Compiler: GCC or IAR (qualified per DO‑330 if Level A)
- Static analyzer: Polyspace or Coverity (must detect MISRA violations)
- Version control: Git with signed commits

### 3.2) Development Environment

**Platform:** Linux (development), ARINC‑653 target (Integrity RTOS or equivalent)

**Tool Qualification (DO‑330):**
- Compiler (if code-generation errors not detected by test): **TQL‑1** (DAL‑A), **TQL‑2** (DAL‑B)
- Static analyzer (if used to eliminate verification): **TQL‑5**
- Tool qualification data: `tools/qual/`

### 3.3) Independence

**Requirement:** Verification activities independent of development (DO‑178C § 10.2.2)

**Implementation:**
- DAL‑A (P‑FBW, RTOS): verification team organizationally separate from design team
- DAL‑B (P‑NAV, P‑SEC): verification lead ≠ design lead (minimum)
- DAL‑C/D: self-verification allowed with review

---

## 4) Software Requirements Process

**Objective:** Capture and trace requirements from system to code.

### 4.1) Requirements Flow

```
System Requirements (FHA/PSSA)
   ↓
High-Level Requirements (HLR) — partition functional spec
   ↓
Low-Level Requirements (LLR) — module/function spec
   ↓
Source Code
```

**Traceability:** DOORS or equivalent; bidirectional links HLR↔LLR, LLR↔Code

### 4.2) Requirements Standards

**HLR:**
- Shall/shall not language
- Verifiable (testable)
- No ambiguity (reviewed by independent party)
- Safety requirements highlighted (e.g., "SR‑FBW‑001")

**LLR:**
- Derived from HLR or design
- Algorithm specifications (e.g., control law gains, filter coefficients)
- Timing constraints (e.g., "compute within 1 ms")

**Review gates:**
- Software Requirements Review (SRR) — HLR completeness
- Preliminary Design Review (PDR) — HLR↔LLR trace
- Critical Design Review (CDR) — LLR↔Code trace

---

## 5) Software Design Process

**Objective:** Architecture and detailed design per DO‑178C § 5.3.

### 5.1) Architecture (HLD — High-Level Design)

**Partitions as components:**
- Each partition is a separate SW item with ARINC‑653 API boundary
- Inter-partition communication via VLs (AFDX) or APEX ports only
- No shared memory (enforced by ARINC‑653 MMU)

**Design patterns:**
- State machines for mode logic (e.g., P‑FBW control law selection)
- Data flow for sensor fusion (P‑NAV)
- Event-driven for alerts (P‑DISP)

**Document:** `partitions/<P-name>/Design_Spec.md`

### 5.2) Detailed Design (LLD — Low-Level Design)

**Per module:**
- Function signatures, input/output specs
- Data structures (struct/enum definitions)
- Algorithm pseudocode or flowcharts

**Safety-critical modules (DAL‑A):**
- Redundancy: dual-channel computations with cross-check
- Watchdog: partition self-monitors for timing violations

---

## 6) Software Implementation (Coding)

**Objective:** Translate design to source code per standards.

### 6.1) Coding Practices

**MISRA C compliance:**
- Mandatory rules: 100% compliance (or deviation with rationale)
- Advisory rules: target 95% compliance
- Checker: Polyspace or Coverity (run in CI)

**Defensive programming (DAL‑A):**
- Range checks on all inputs (sensors, AFDX frames)
- Assertions for invariants (disabled in production, logged in dev)
- No undefined behavior (per ISO C undefined list)

**Partition-specific:**
- P‑FBW: deterministic execution (no loops with variable iteration count)
- P‑NAV: numerical stability (fixed-point or IEEE 754 with rounding checks)
- P‑SEC: constant-time crypto (no data-dependent branches)

### 6.2) Code Reviews

**Frequency:** Every module before integration

**Checklist:**
- HLR/LLR trace
- MISRA compliance
- Complexity within limits
- Error handling adequate
- Comments match code

**Independence:** DAL‑A reviews by separate team; DAL‑B by different developer

---

## 7) Software Verification Process

**Objective:** Demonstrate compliance with requirements (DO‑178C § 6).

### 7.1) Verification Methods

| Method | DAL‑A | DAL‑B | DAL‑C | DAL‑D |
|--------|-------|-------|-------|-------|
| Requirements-based test | ✓ | ✓ | ✓ | ✓ |
| Structural coverage (MC/DC) | ✓ | — | — | — |
| Structural coverage (decision) | — | ✓ | — | — |
| Structural coverage (statement) | — | — | ✓ | — |
| Reviews (design, code) | ✓ | ✓ | ✓ | (reduced) |
| Analysis (data/control flow) | ✓ | ✓ | (reduced) | — |

### 7.2) Test Approach

**Levels:**
1. **Unit test** — function/module in isolation (host environment)
2. **Integration test** — partition running on target RTOS (ARINC‑653 simulator or real HW)
3. **System test** — all partitions + IMA platform (HW-in-loop or aircraft)

**Test cases:**
- Normal operation (nominal inputs, expected outputs)
- Boundary conditions (min/max values)
- Failure modes (sensor loss, AFDX frame corruption)

**Coverage:**
- **MC/DC (DAL‑A):** every condition independently affects decision outcome
  - Tool: Cantata++ or LDRA
  - Target: 100% with rationale for uncovered (e.g., defensive code)
- **Decision (DAL‑B):** every decision outcome exercised (True/False)
- **Statement (DAL‑C):** every line executed at least once

### 7.3) Independence (Verification)

**DAL‑A:**
- Verification lead ≠ design lead
- Test cases developed by separate team (or reviewed by independent party)
- Test execution witnessed by QA

**DAL‑B/C:**
- Verification lead ≠ design lead (minimum)
- Test cases peer-reviewed

---

## 8) Software Configuration Management Plan (SCMP)

**Objective:** Control baselines, manage changes (DO‑178C § 7).

### 8.1) Configuration Items (CI)

**Baseline artifacts:**
- Requirements documents (HLR, LLR)
- Design documents (HLD, LLD)
- Source code (per module)
- Executable object code (per partition)
- Test procedures and results
- PSAC, SDP, SVP, SCMP, SQAP (plans)

**Naming convention:** `<Partition>_<Type>_<Version>.ext`  
Example: `P-FBW_HLR_v2.3.pdf`

### 8.2) Change Control

**Process:**
1. Problem Report (PR) raised (bug, requirement change)
2. Change Request (CR) approved by Configuration Control Board (CCB)
3. Impact analysis (safety, verification re-run needed?)
4. Change implemented, re-verified, re-baselined

**CCB membership:** Project manager, design lead, verification lead, safety engineer, QA

**Traceability:** CR linked to PR, PR linked to test failures or audits

### 8.3) Archive & Retrieval

**Repository:** Git (with signed tags per release)

**Backup:** Daily incremental, weekly full to off-site storage

**Retrieval:** Any baseline reproducible from tag + build instructions

---

## 9) Software Quality Assurance Plan (SQAP)

**Objective:** Ensure compliance with plans (DO‑178C § 8).

### 9.1) QA Activities

**Audits:**
- Process audit (lifecycle data completeness) — at PDR, CDR, TRR
- Product audit (code vs. standards) — sample 10% of modules

**Reviews:**
- SRR, PDR, CDR, TRR — QA attendance mandatory
- Sign-off: QA approves transition to next phase

**Independence:** QA reports to program manager, not design lead

### 9.2) Conformity

**Checklists:**
- DO‑178C Table A‑1 to A‑10 (objectives per DAL)
- Each objective: evidence location, review status, approval

**Nonconformities:**
- Logged as PR, escalated to CCB
- Closure verified by QA before release

---

## 10) Certification Liaison Process

**Objective:** Engage authority early, agree on MOC (DO‑178C § 9).

### 10.1) Stage of Involvement (SOI)

**Milestones:**
- **SOI‑1 (Planning):** Review PSAC, agree on DAL allocation
- **SOI‑2 (Development):** Witness CDR, sample code reviews
- **SOI‑3 (Verification):** Witness integration test, review coverage data
- **SOI‑4 (Completion):** Review SAS, approve for installation

**Authority:** FAA DER or EASA IDAL (as applicable)

### 10.2) Means of Compliance (MOC)

**Clarifications:**
- Tool qualification approach (DO‑330 credit)
- Object code without source (if COTS libraries used)
- Partitioning credit (DO‑297 responsibilities)

**Document:** `cert/MOC_Agreements.md`

---

## 11) Transition to Airborne System

**Deliverables:**
- **Software Accomplishment Summary (SAS)** — compliance summary per DO‑178C § 10.4
- **Software Configuration Index (SCI)** — list of all CIs with versions
- **Software Life Cycle Environment Configuration Index (SECI)** — tools, compilers, OS versions
- **Problem Reports Summary** — open/closed PRs, impact analysis

**Installation:**
- Partition binaries signed with OEM certificate
- Loaded via ARINC‑653 configuration loader (secure boot verified)
- Post-load BIT/BIST executed to confirm operational

---

## 12) Roles & Responsibilities

| Role | Responsibility |
|------|----------------|
| SW Project Manager | Schedule, budget, resource allocation |
| SW Design Lead (per partition) | HLR/LLR/design/code |
| Verification Lead (per partition) | Test plans, test execution, coverage analysis |
| Configuration Manager | Baseline control, CCB support |
| Quality Assurance | Audits, reviews, nonconformity tracking |
| Safety Engineer | Safety requirements review, DAL validation |
| Certification Engineer | Authority liaison, SOI/MOC coordination |

---

## 13) Schedule & Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| PSAC approval | 2025-Q1 | Planned |
| SRR (HLR complete) | 2025-Q2 | Planned |
| PDR (design baseline) | 2025-Q3 | Planned |
| CDR (code baseline) | 2025-Q4 | Planned |
| Integration test complete | 2026-Q1 | Planned |
| SAS delivery | 2026-Q2 | Planned |

---

## 14) UTCS/QS Evidence

- All lifecycle data signed with UTCS DET anchors
- Traceability maintained in DOORS with SHA-256 hashes
- Independent verification results archived per QS policy

---

## 15) Cross-References

- **System architecture:** [ATA‑42 README](../README.md)
- **Safety:** [FHA/PSSA/SSA](../safety/FHA_PSSA_SSA.md)
- **Hardware:** [DO‑254 Plan](../cert/DO254_Plan.md)
- **Environmental:** [DO‑160G Summary](../cert/DO160G_Qual_Summary.md)
- **Responsibility:** [DO‑297 Agreement](../cert/DO297_Responsibility_Agreement.md)
- **Security:** [DO‑326A/356A Plans](../security/SEC_Plans.md)

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.3.0 | 2025-09-29 | IIS | Expanded PSAC with DO‑178C structure and detailed processes |
| 0.2.0 | 2025-09-28 | IIS | Added partition DAL table |
| 0.1.0 | 2025-09-28 | IIS | Initial placeholder |