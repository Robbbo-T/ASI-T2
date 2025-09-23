---
id: ASIT2-AQUAOS-AIR-QAFBW-SRD
project: ASI-T2
artifact: QAFbW Control Stack (AQUA OS — Aircraft Extension) SRD
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: OOO (OS), LCC (Control Laws), EDI (Avionics/Net), IIS (Software), MEC (Actuation)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  component: QAFbW Control Stack (AQUA OS — Aircraft Extension)
  level: DO-178C DAL-A; DO-297; DO-326A/356A
  bridges: CB→QB→UE→FE→FWD→QS
  status: BASELINED
canonical_hash: pending
---

# QAFbW System Requirements (MoSCoW)

## MUST
- QAFBW-SRD-001 Determinism & Latency: End-to-end loop ≤10 ms typical, ≤15 ms WCET @200–500 Hz, ≥20% CPU headroom.
- QAFBW-SRD-002 Modes & Transitions: NORMAL/ALTERNATE/DIRECT/REVERSIONARY with bounded, annunciated, non-oscillatory transitions.
- QAFBW-SRD-003 Voting & Faults: DAL-A 2oo3 voter; freeze on sustained disagree (policy & hysteresis defined); safe actuator defaults on timeout.
- QAFBW-SRD-004 Envelope: Envelope protection active (NORMAL/ALTERNATE) and relaxed (DIRECT) with preserved pilot authority.
- QAFBW-SRD-005 Quantum Boundary: QAS inputs are advisory/out-of-loop; loss/degradation shall not affect timing, modes, or dispatch.
- QAFBW-SRD-006 Security: Secure boot, code signing, link auth/integrity (replay-protected) per DO-326A/356A; partition attestation to AQUA OS policy.
- QAFBW-SRD-007 Partitioning: ARINC-653 partition; freedom-from-interference to different DAL partitions; no shared writable memory.
- QAFBW-SRD-008 Networks: Deterministic A/B networks; GM/PTP switchover without jitter budget violation; VL QoS per ICD.
- QAFBW-SRD-009 Evidence/Trace: All releases/tests/logs sealed via UTCS/QS; reproducible build & SBOM.
- QAFBW-SRD-010 Diagnostics: Health API (wcet, jitter, voter state, sensor validity) + structured logs.

## SHOULD
- QAFBW-SRD-011 Fault Reaction: Detect/mitigate critical faults ≤50 ms; maintain stable handling in transients.
- QAFBW-SRD-012 Maintenance FI: Ground-only, guarded fault injection for HIL/Iron Bird.

## COULD
- QAFBW-SRD-013 QRNG/QKD Use: Use QRNG/QKD entropy to strengthen crypto sessions (out-of-loop).

## WON'T (baseline)
- QAFBW-SRD-014 No in-loop quantum control in cert baseline.
- QAFBW-SRD-015 No on-aircraft blockchain ledger in DAL-A partition.

## Resource Baseline
- CPU ≥30% of a core; Mem ≥64 MiB private; Net ≥2 Mbps deterministic reserved.

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*