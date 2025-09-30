# Safety Analysis — ATA-42 IMA

**Parent:** [../README.md](../README.md)  
**Related:** [../cert/](../cert/) · [../verification/](../verification/)

## Purpose

System-level safety analysis for the BWB-Q100 IMA per ARP4754A and ARP4761, including FHA, PSSA, SSA, and supporting analyses.

## Contents

- **`FHA_PSSA_SSA.md`** — Functional Hazard Assessment, Preliminary System Safety Assessment, System Safety Assessment
- **`analyses/`** *(planned)* — Detailed analyses (FTA, FMEA, CCA, ZSA, PRA)

## Key Files

| File | Description | Standard | Status |
|------|-------------|----------|--------|
| `FHA_PSSA_SSA.md` | Complete safety analysis (9 sections) | ARP4754A/4761 | ✅ Active |

## Safety Analysis Summary

### Functional Hazard Assessment (FHA)
- Function allocation to IMA partitions
- Failure condition classification: Catastrophic, Hazardous, Major, Minor
- DAL derivation: P-FBW (DAL-A), P-NAV/P-SEC (DAL-B), P-DISP (DAL-C), P-MAINT (DAL-D)

### Preliminary System Safety Assessment (PSSA)
- Architecture safety strategy (partition isolation, communication isolation, redundancy)
- Safety requirements allocation
- Preliminary FTA/FMEA

### System Safety Assessment (SSA)
- Verification of safety requirements
- Compliance matrix
- Probabilistic risk assessment

### Common Cause Analysis (CCA)
- Shared resources: CPU, RAM, AFDX backplane, power supply
- Mitigation: time/space isolation, dual networks, health monitoring

### Zonal Safety Analysis (ZSA)
- Avionics bay hazards: fire, smoke, thermal, water ingress
- Mitigations per ATA-26 (fire detection/suppression)

## Safety Objectives

| Failure Condition | Probability Target | DAL |
|-------------------|-------------------|-----|
| Catastrophic | ≤ 10⁻⁹ per flight hour | A |
| Hazardous | ≤ 10⁻⁷ per flight hour | B |
| Major | ≤ 10⁻⁵ per flight hour | C |
| Minor | No quantitative requirement | D |

## Cross-References

- **Hardware certification:** [../cert/DO254_Plan.md](../cert/DO254_Plan.md)
- **Software certification:** [../verification/DO178C_PSAC.md](../verification/DO178C_PSAC.md)
- **IMA responsibilities:** [../cert/DO297_Responsibility_Agreement.md](../cert/DO297_Responsibility_Agreement.md)

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial safety directory README |
