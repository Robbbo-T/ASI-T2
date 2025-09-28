---
artifact: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-AQUAOS-AIR-SECKMS-SRD
llc: SYSTEMS
maintainer: DDD (Security), OOO (OS)
project: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
release_date: 2024-09-23
utcs_mi: 'component: SEC_KMS Security & Key Management (AQUA OS — Aircraft Extension)

  level: DO-178C DAL-A; DO-326A/356A

  bridges: CB→QB→UE→FE→FWD→QS

  status: BASELINED

  '
version: 1.0
---

# SEC_KMS System Requirements (MoSCoW)

## MUST

- SECKMS-SRD-001 Secure Boot: Refuse unsigned code; verify boot chain integrity; generate attestation measurements.
- SECKMS-SRD-002 Key Rotation: Rotate session keys on power-up; support graceful key rollover without service disruption.
- SECKMS-SRD-003 Cryptography: Provide FIPS-grade PRF, MAC, and signature operations with hardware acceleration.
- SECKMS-SRD-004 Message Auth: Support GMAC-128 computation for safety-critical network messages.
- SECKMS-SRD-005 PKI: Validate certificate chains; maintain root certificate store with secure updates.
- SECKMS-SRD-006 Hardware Security: Utilize hardware security modules and secure storage when available.
- SECKMS-SRD-007 Attestation: Generate system integrity measurements; report security status.
- SECKMS-SRD-008 Key Distribution: Securely distribute session keys to authorized partitions and services.
- SECKMS-SRD-009 Audit Trail: Log all security events and key operations for forensic analysis.
- SECKMS-SRD-010 Evidence: All security configurations and events sealed via UTCS/QS.

## SHOULD

- SECKMS-SRD-011 QKD Integration: Optionally use QRNG/QKD entropy to strengthen crypto sessions (out-of-loop).
- SECKMS-SRD-012 Performance: Optimize cryptographic operations for minimal latency impact.

## COULD

- SECKMS-SRD-013 Quantum Resistance: Support post-quantum cryptographic algorithms for future-proofing.

## WON'T (baseline)

- SECKMS-SRD-014 No software-only long-term key storage.
- SECKMS-SRD-015 No runtime cryptographic algorithm negotiation.

## Resource Baseline

- CPU: ≤4% of a core for cryptographic operations
- Memory: ≤12 MiB for key storage and certificate cache
- Hardware: Cryptographic accelerator and secure storage recommended

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*