# Certification Documentation — ATA-42 IMA

**Parent:** [../README.md](../README.md)  
**Related:** [../verification/](../verification/) · [../safety/](../safety/) · [../security/](../security/)

## Purpose

Certification evidence, plans, and compliance documentation for the BWB-Q100 IMA system per aviation standards.

## Contents

This directory contains certification plans and evidence per:
- **DO-254** — Hardware Development
- **DO-297** — IMA Responsibility Agreement
- **DO-160G** — Environmental Qualification

## Key Files

| File | Description | Standard | Status |
|------|-------------|----------|--------|
| `DO254_Plan.md` | Hardware Development Plan (14 sections) | DO-254/ED-80 | ✅ Active |
| `DO297_Responsibility_Agreement.md` | IMA roles, interfaces, evidence (12 sections) | DO-297/ED-124 | ✅ Active |
| `DO160G_Qual_Summary.md` | Environmental qualification matrix (15+ categories) | DO-160G | ✅ Active |

## Standards Coverage

### DO-254: Hardware Development
- Applicability & DAL: Level A (complex electronic hardware)
- Lifecycle processes: Requirements → Design → Implementation → Verification
- FPGA development for AFDX switch, ARINC-429 I/O, partition health monitor

### DO-297: IMA Responsibility Agreement
- Parties: OEM/System Integrator, IMA Platform Supplier, Application Software Suppliers
- Partition isolation verification
- Evidence flow and certification credit

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
