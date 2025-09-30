---
id: BWB-Q100-ATA42-SEC-PLANS
project: AMPEL360_AIR_TRANSPORT / BWB-Q100
artifact: Security Plans — DO-326A/ED-202A & DO-356A/ED-203A (ATA-42 · IMA)
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

# Security Plans — DO‑326A / DO‑356A (ATA‑42 · IMA)

**Back to ATA‑42:** [../README.md](../README.md)  
**Related:** [DO‑297 Responsibility Agreement](../cert/DO297_Responsibility_Agreement.md) · [DO‑178C PSAC](../verification/DO178C_PSAC.md) · [DO‑254 Plan](../cert/DO254_Plan.md) · [DO‑160G Summary](../cert/DO160G_Qual_Summary.md)  
**Interfaces:** [AFDX VL table](../buses/afdx/vl_table.csv) · [ARINC‑429 channel map](../buses/a429/channel_map.csv) · [ARINC‑653 schedule](../os/schedule.xml) · [HSI Spec](../interfaces/HSI/HSI_Spec.md)

> Scope: planning for the **airworthiness security process** (DO‑326A/ED‑202A) and **security verification** (DO‑356A/ED‑203A) for the BWB‑Q100 **Integrated Modular Avionics (IMA)**. This document defines activities, roles, deliverables, and evidence required to manage security risk throughout the lifecycle.

---

## 1) Governance & Roles (per DO‑297)

| Role | Area | Security Responsibilities |
|------|------|--------------------------|
| OEM / System Integrator | Program | Threat acceptance policy, risk ownership, change control, authority liaison |
| IMA Platform Supplier | Platform | Secure boot/attestation, partition isolation, cryptographic services, vulnerability response |
| Application Suppliers | Partitions | Input validation, least privilege, secure coding, partition-specific threat mitigation |
| Certification Authority | Oversight | Review security plans, approve MOC, witness penetration tests (if required) |

---

## 2) Security Development Process (DO‑326A/ED‑202A)

### 2.1) Process Overview

```
Threat Assessment → Security Requirements → Architecture & Design → Implementation → Verification → Transition to Service
       ↑                     ↑                      ↑                    ↑                ↑              ↑
       └─────────────────────┴──────────────────────┴────────────────────┴────────────────┴──────────────┘
                                    Configuration Management + Security Assurance
```

### 2.2) Threat Assessment

**Method:** STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)

**Assets:**
- Flight control commands (P‑FBW → actuators)
- Navigation data (P‑NAV → P‑FBW, P‑DISP)
- Cryptographic keys (P‑SEC)
- Maintenance logs (P‑MAINT)

**Threat Sources:**
- External: wireless (if present), maintenance port, supply chain
- Internal: malicious insider, compromised partition, HW Trojan

**Threat Scenarios (examples):**

| Threat ID | Scenario | Asset | Severity | Mitigation |
|-----------|----------|-------|----------|------------|
| T‑01 | Spoofed AFDX frame → erroneous nav data | VL‑NAV‑ATT | Hazardous | VL policing, frame CRC, cross-channel monitoring |
| T‑02 | Compromised partition → escalation to P‑FBW | Partition isolation | Catastrophic | ARINC‑653 MMU, HM monitoring, signed partition images |
| T‑03 | Supply chain: Trojan in FPGA bitstream | IMA platform | Catastrophic | Bitstream signing, supply chain audit, HW root of trust |
| T‑04 | Maintenance port: unauthorized SW upload | SW integrity | Hazardous | Secure boot, cryptographic signature verification |
| T‑05 | Denial of Service: AFDX flooding | AFDX bandwidth | Major | BAG policing, rate limiting, dual networks |

**Document:** `security/analyses/Threat_Model.md`

### 2.3) Security Requirements

**Derived from threats:**

| Req ID | Requirement | Mitigation Strategy | Verification |
|--------|-------------|---------------------|--------------|
| SEC‑01 | Partition SW images signed with RSA‑2048 or ECDSA‑P256 | Secure boot in ARINC‑653 RTOS | Boot test with tampered image (expect reject) |
| SEC‑02 | AFDX VL ingress policing (BAG, payload size) | Switch logic | Network fuzzing test |
| SEC‑03 | HW root of trust (e.g., TPM or FPGA PUF) | Platform design | Attestation test |
| SEC‑04 | Cryptographic key storage in P‑SEC with access control | Key management API | Penetration test (unauthorized key read) |
| SEC‑05 | Health Monitor logs security events (tamper attempts) | HM extension | Log analysis after fault injection |

---

## 3) Security Architecture & Design

### 3.1) Defense in Depth

**Layers:**
1. **Physical:** Sealed chassis, tamper-evident seals, avionics bay access control
2. **Hardware:** FPGA bitstream signing, HW root of trust, memory encryption (optional)
3. **Platform (ARINC‑653):** Partition isolation, secure boot, HM monitoring
4. **Network:** AFDX VL policing, ARINC‑429 unidirectional channels (where applicable)
5. **Application:** Input validation, least privilege, secure coding standards

### 3.2) Cryptographic Services (P‑SEC Partition)

**Purpose:** Centralized key management, attestation, secure logging

**Functions:**
- Key generation (RSA, ECDSA, AES)
- Signature verification (partition images, configuration files)
- Attestation (report platform state to ground systems)
- Secure time stamping (for logs)

**Implementation:**
- FIPS 140-2 Level 2 (or equivalent) cryptographic module
- Keys stored in non-volatile memory with access control
- API: ARINC‑653 queueing ports (one-way requests, async responses)

**Document:** `partitions/P-SEC/Crypto_Design.md`

### 3.3) Secure Boot & Configuration

**Process:**
1. Hardware root of trust verifies ARINC‑653 RTOS signature
2. RTOS verifies each partition image signature (P‑FBW, P‑NAV, P‑DISP, P‑MAINT, P‑SEC)
3. RTOS verifies ARINC‑653 configuration (schedule, HM table) signature
4. Boot proceeds only if all signatures valid

**Failure mode:** HM logs error, system halts (or falls back to safe mode if defined)

**Document:** `os/Secure_Boot_Spec.md`

---

## 4) Security Implementation (DO‑356A Objectives)

### 4.1) Secure Coding Practices

**Standards:**
- MISRA C (or equivalent) for platform SW
- Input validation for all external data (AFDX, ARINC‑429, maintenance port)
- Least privilege: partitions use minimal APEX API calls

**Tools:**
- Static analysis (e.g., Coverity, Polyspace)
- Dynamic analysis (ASAN, UBSAN for development builds)

### 4.2) Tool Qualification (DO‑330 by analogy)

**If tools auto-generate security-critical code:**
- Tool qualification per DO‑330 (software tool qualification)
- Rationale: compiler/linker for partition code (if Level A), crypto library (if auto-generated)

---

## 5) Security Verification (DO‑356A)

### 5.1) Verification Activities

| Activity | Method | Target | Document |
|----------|--------|--------|----------|
| Security requirements review | Inspection | All SEC‑* requirements | `security/reviews/Req_Review_Minutes.md` |
| Architecture review | Inspection + threat model walk-through | Defense-in-depth layers | `security/reviews/Arch_Review_Minutes.md` |
| Penetration testing | Black-box + white-box | AFDX, maintenance port, partition API | `security/tests/Pentest_Report.pdf` |
| Fault injection (security) | Inject tampered data, bitflips | Secure boot, VL policing, HM | `security/tests/Fault_Injection_Report.pdf` |
| Vulnerability scan | Automated tools (Nessus, OpenVAS) | Platform SW, network stack | `security/tests/Vuln_Scan_Report.pdf` |
| Code review (security-focused) | Manual inspection | Crypto code, secure boot, HM security hooks | `security/reviews/Code_Review_Checklist.md` |

### 5.2) Penetration Test Scenarios

| Scenario | Attack Vector | Expected Outcome |
|----------|---------------|------------------|
| Tampered partition image | Load modified P‑FBW binary | Secure boot rejects (signature fail) |
| AFDX frame injection | Inject frames on VL‑FBW‑CMD from unauthorized source | VL policing drops frames |
| Partition escape | P‑MAINT attempts to write to P‑FBW memory | MMU triggers HM error, P‑MAINT restarted |
| Key extraction | Debugger attempts to read P‑SEC key storage | Access denied (HW protection) |
| Supply chain: fake LRU | Install counterfeit AFDX card | Attestation fails (no valid cert) |

### 5.3) Residual Risk Acceptance

**Process:**
- If a threat cannot be fully mitigated (e.g., physical access by skilled adversary), document residual risk
- OEM safety board reviews and accepts risk with operational mitigations (e.g., access control, audit trails)
- Authority informed via MOC/SOI process

**Document:** `security/Residual_Risk_Acceptance.md`

---

## 6) Configuration Management (Security)

**Baselines:**
- Threat model (revision-controlled)
- Security requirements (linked to threats)
- Cryptographic key inventory (offline, encrypted storage)
- Partition signatures (signed by OEM CA, archived per QS)

**Change control:**
- Any change to threat model → re-assess impacted requirements
- Key rotation policy: every 12 months or after compromise

---

## 7) Security Assurance (Independence)

**Requirement:** Security verification activities independent of design (per DO‑326A § 5.4)

**Implementation:**
- Penetration test by external red team (or independent OEM team)
- Code review by security SME (not partition developer)
- Threat model review by system safety + security specialists

---

## 8) Operational Security & Monitoring

**In-service:**
- P‑MAINT logs HM security events (tamper attempts, signature failures)
- ACMS data analyzed for anomalies (unexpected partition restarts, network drops)
- Incident response plan: if compromise suspected, ground aircraft, forensic analysis

**Updates:**
- Partition SW updates signed and verified (same secure boot process)
- OTA (over-the-air) updates disabled or heavily restricted (ground-based only)

---

## 9) Certification Liaison

**Authority engagement:**
- MOC for DO‑326A/356A applicability (if novel for type)
- Witness penetration tests (if required by authority)
- Review threat model and residual risk acceptance

**Document:** `cert/Security_Compliance_Checklist.xlsx`

---

## 10) UTCS/QS Evidence Chain

- All security analyses (threat model, pentest reports) signed with UTCS DET anchors
- Traceability: threats → requirements → design → verification
- Independent review per DO‑356A

---

## 11) Cross-References

- **System architecture:** [ATA‑42 README](../README.md)
- **Safety:** [FHA/PSSA/SSA](../safety/FHA_PSSA_SSA.md)
- **Software:** [DO‑178C PSAC](../verification/DO178C_PSAC.md)
- **Hardware:** [DO‑254 Plan](../cert/DO254_Plan.md)
- **Responsibility:** [DO‑297 Agreement](../cert/DO297_Responsibility_Agreement.md)

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.2.0 | 2025-09-29 | IIS | Expanded security plans with DO‑326A/356A structure |
| 0.1.0 | 2025-09-28 | IIS | Initial placeholder |