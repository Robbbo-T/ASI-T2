# Software Verification — ATA-42 IMA

**Parent:** [../README.md](../README.md)  
**Related:** [../cert/](../cert/) · [../safety/](../safety/)

## Purpose

Software certification planning and verification evidence for the BWB-Q100 IMA partitions per DO-178C.

## Contents

- **`DO178C_PSAC.md`** — Plan for Software Aspects of Certification (15 sections)
- **`test_procedures/`** *(planned)* — Unit, integration, and system test procedures
- **`test_results/`** *(planned)* — Coverage data, test logs, verification reports
- **`reviews/`** *(planned)* — Design review minutes, code review checklists

## Key Files

| File | Description | Standard | Status |
|------|-------------|----------|--------|
| `DO178C_PSAC.md` | Software certification plan | DO-178C/ED-12C | ✅ Active |

## Software Items & DAL Allocation

| Partition | Function | DAL | Verification |
|-----------|----------|-----|--------------|
| P-FBW | Flight-by-wire control laws | A | MC/DC coverage, full independence |
| P-NAV | INS/GNSS fusion, attitude computation | B | Decision coverage, reduced requirements |
| P-DISP | PFD/ND rendering, crew alerting | C | Statement coverage |
| P-MAINT | ACMS/CMS logging | D | Functional test only |
| P-SEC | Cryptographic services, key management | B | Decision coverage, security review |
| ARINC-653 RTOS | Kernel, scheduler, health monitor | A | MC/DC coverage (platform supplier) |

## Verification Methods

### DAL-A (P-FBW, RTOS)
- ✅ Requirements-based testing
- ✅ MC/DC structural coverage
- ✅ Reviews (design, code)
- ✅ Data/control flow analysis
- ✅ Independent verification team

### DAL-B (P-NAV, P-SEC)
- ✅ Requirements-based testing
- ✅ Decision coverage
- ✅ Reviews (design, code)
- ✅ Data/control flow analysis (reduced)
- ✅ Independent verification lead

### DAL-C (P-DISP)
- ✅ Requirements-based testing
- ✅ Statement coverage
- ✅ Reviews (reduced)

### DAL-D (P-MAINT)
- ✅ Functional testing

## Development Standards

- **Language:** C (ISO/IEC 9899:2011, MISRA C:2012 subset)
- **Style:** Max cyclomatic complexity 15, function length ≤200 LOC, no recursion (DAL-A/B)
- **Tools:** GCC/IAR (qualified per DO-330), Polyspace/Coverity (static analysis)

## Supporting Processes

- **SDP:** Software Development Plan
- **SVP:** Software Verification Plan  
- **SCMP:** Software Configuration Management Plan
- **SQAP:** Software Quality Assurance Plan

## Deliverables

- Software Accomplishment Summary (SAS)
- Software Configuration Index (SCI)
- Software Life Cycle Environment Configuration Index (SECI)
- Problem Reports Summary

## Cross-References

- **Hardware certification:** [../cert/DO254_Plan.md](../cert/DO254_Plan.md)
- **Safety analysis:** [../safety/FHA_PSSA_SSA.md](../safety/FHA_PSSA_SSA.md)
- **Security plans:** [../security/SEC_Plans.md](../security/SEC_Plans.md)
- **IMA responsibilities:** [../cert/DO297_Responsibility_Agreement.md](../cert/DO297_Responsibility_Agreement.md)

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial verification directory README |
