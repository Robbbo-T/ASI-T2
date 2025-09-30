# Certification Documentation — ATA-42 IMA

**Parent:** [../README.md](../README.md)  
**Related:** [../verification/](../verification/) · [../safety/](../safety/) · [../security/](../security/)

## Purpose

Certification evidence, plans, and compliance documentation for the BWB-Q100 IMA system per aviation standards.

## Contents

This directory contains certification plans and evidence per:
- **DO-178C / ED-12C** — Airborne Software
- **DO-254 / ED-80** — Airborne Electronic Hardware
- **DO-297 / ED-124** — IMA Development & Certification
- **DO-330 / ED-215** — Software Tool Qualification
- **ARP4754B / ED-79B** — Development of Civil Aircraft & Systems
- **ARP4761A / ED-135** — Safety Assessment Process
- **DO-326A / ED-202A** — Airworthiness Security Process
- **DO-356A / ED-203A** — Security Methods & Considerations
- **DO-355 / ED-204A** — Continuing Airworthiness Security
- **DO-160G** — Environmental Qualification
- **AMC 20-115D** — EASA AMC for DO-178C
- **AMC 20-152A** — EASA AMC for DO-254

## Key Files

| File | Description | Standard | Status |
|------|-------------|----------|--------|
| `DO254_Plan.md` | Hardware Development Plan (14 sections) | DO-254/ED-80 | ✅ Active |
| `DO297_Responsibility_Agreement.md` | IMA roles, interfaces, evidence (12 sections) | DO-297/ED-124 | ✅ Active |
| `DO160G_Qual_Summary.md` | Environmental qualification matrix (15+ categories) | DO-160G | ✅ Active |
| `plans/certification_plan.yaml` | Overall certification plan | Multiple | 📋 New |
| `procedures/airworthiness_security.yaml` | Security certification procedures | DO-326A/356A/355 | 📋 New |

## 📚 Standards References

| Standard | Summary | File |
|----------|---------|------|
| DO-178C / ED-12C | Airborne software | [📄](./references/DO-178C.md) |
| DO-254 / ED-80 | Airborne electronic hardware | [📄](./references/DO-254.md) |
| **DO-297 / ED-124** | IMA development & certification | [📄](./references/DO-297.md) |
| **DO-330 / ED-215** | Software tool qualification (TQL) | [📄](./references/DO-330.md) |
| **ARP4754B / ED-79B (2023)** | Development of civil aircraft & systems | [📄](./references/ARP4754B.md) |
| **ARP4761A / ED-135 (2023)** | Safety assessment process | [📄](./references/ARP4761A.md) |
| **DO-326A / ED-202A** | Airworthiness security process | [📄](./references/DO-326A_ED-202A.md) |
| **DO-356A / ED-203A** | Security methods & considerations | [📄](./references/DO-356A_ED-203A.md) |
| **DO-355 / ED-204A** | Continuing airworthiness security | [📄](./references/DO-355_ED-204A.md) |
| **AMC 20-115D** | EASA AMC for DO-178C | [📄](./references/AMC_20-115D.md) |
| **AMC 20-152A** | EASA AMC for DO-254 | [📄](./references/AMC_20-152A.md) |

## Standards Coverage

### DO-178C: Software Considerations
- Applicability & DAL: Level A (critical software)
- Software planning, requirements, design, code, integration, verification
- Configuration management and quality assurance

### DO-254: Hardware Development
- Applicability & DAL: Level A (complex electronic hardware)
- Lifecycle processes: Requirements → Design → Implementation → Verification
- FPGA development for AFDX switch, ARINC-429 I/O, partition health monitor

### DO-297: IMA Responsibility Agreement
- Parties: OEM/System Integrator, IMA Platform Supplier, Application Software Suppliers
- Partition isolation verification
- Evidence flow and certification credit

### DO-330: Tool Qualification
- Tool Qualification Levels (TQL)
- Tool operational requirements and software tool qualification data

### ARP4754B: Aircraft & Systems Development
- System development assurance process
- Requirements capture, architecture, and design
- Integration with safety assessment process

### ARP4761A: Safety Assessment
- Functional Hazard Assessment (FHA)
- Preliminary/System Safety Assessment (PSSA/SSA)
- Common Cause Analysis (CCA)

### DO-326A/356A/355: Airworthiness Security
- Security planning and threat assessment
- Security methods and penetration testing
- Continuing airworthiness security monitoring

### DO-160G: Environmental Qualification
- Temperature & altitude, vibration, shock, EMC/EMI
- Lightning, power quality, waterproofness
- Test categories per avionics bay installation

## Cross-References

- **Software certification:** [../verification/DO178C_PSAC.md](../verification/DO178C_PSAC.md)
- **Safety analysis:** [../safety/FHA_PSSA_SSA.md](../safety/FHA_PSSA_SSA.md)
- **Security plans:** [../security/SEC_Plans.md](../security/SEC_Plans.md)

## Deliverables

- Hardware Accomplishment Summary (HAS)
- Hardware Configuration Index (HCI)
- Environmental test reports
- Stage of Involvement (SOI) meeting minutes
- Means of Compliance (MOC) agreements

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial certification directory README |
