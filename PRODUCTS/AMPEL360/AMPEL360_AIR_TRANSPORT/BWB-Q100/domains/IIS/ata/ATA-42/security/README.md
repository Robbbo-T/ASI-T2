# Security Plans & Analysis — ATA-42 IMA

**Parent:** [../README.md](../README.md)  
**Related:** [../safety/](../safety/) · [../cert/](../cert/)

## Purpose

Airworthiness security planning and verification for the BWB-Q100 IMA per DO-326A and DO-356A.

## Contents

- **`SEC_Plans.md`** — Security development and verification plans (11 sections)
- **`analyses/`** *(planned)* — Threat models, attack trees, vulnerability assessments
- **`tests/`** *(planned)* — Penetration test reports, fault injection results

## Key Files

| File | Description | Standard | Status |
|------|-------------|----------|--------|
| `SEC_Plans.md` | Security plans (DO-326A/356A) | DO-326A/ED-202A, DO-356A/ED-203A | ✅ Active |

## Security Planning Summary

### DO-326A: Airworthiness Security Process
- Threat assessment (STRIDE methodology)
- Security requirements derivation
- Security risk management

### DO-356A: Airworthiness Security Verification
- Security requirements review
- Architecture review
- Penetration testing
- Fault injection (security-focused)
- Vulnerability scanning
- Code review (security-focused)

## Threat Model

**Attack surfaces:**
- AFDX network (frame spoofing, flooding)
- Maintenance port (unauthorized software upload)
- Supply chain (hardware Trojans, compromised components)
- Partition escalation (compromise leading to isolation bypass)

**Key mitigations:**
- Secure boot with signature verification
- AFDX VL policing and BAG enforcement
- Partition isolation (ARINC-653 MMU/MPU)
- Hardware root of trust
- Cryptographic services (P-SEC partition)

## Security Requirements

| Req ID | Requirement | Mitigation |
|--------|-------------|------------|
| SEC-01 | Partition SW images signed (RSA-2048/ECDSA-P256) | Secure boot |
| SEC-02 | AFDX VL ingress policing (BAG, payload) | Switch logic |
| SEC-03 | Hardware root of trust (TPM/FPGA PUF) | Platform design |
| SEC-04 | Cryptographic key storage with access control | P-SEC partition |
| SEC-05 | Security event logging | Health Monitor extension |

## Verification Activities

- **Penetration testing:** Black-box and white-box testing of AFDX, maintenance port, partition APIs
- **Fault injection:** Tampered images, bit flips, malformed frames
- **Vulnerability scanning:** Automated tools (Nessus, OpenVAS)
- **Code review:** Security-focused review of crypto, secure boot, HM security hooks

## Cross-References

- **Safety analysis:** [../safety/FHA_PSSA_SSA.md](../safety/FHA_PSSA_SSA.md)
- **Software certification:** [../verification/DO178C_PSAC.md](../verification/DO178C_PSAC.md)
- **IMA responsibilities:** [../cert/DO297_Responsibility_Agreement.md](../cert/DO297_Responsibility_Agreement.md)

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial security directory README |
