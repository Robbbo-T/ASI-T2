---
id: ASIT2-AQUAOS-AIR-ACTRGW-SRD
canonical_hash: pending
---

# ACTR_GW System Requirements (MoSCoW)

## MUST

- ACTRGW-SRD-001 Timeout Safety: Command timeout → safe default ≤15 ms; bus diagnostics; position feedback.
- ACTRGW-SRD-002 Bus Interface: Support EHA/EHSV ECU communication protocols with fault detection.
- ACTRGW-SRD-003 Feedback: Provide actuator position, velocity, and current feedback to control systems.
- ACTRGW-SRD-004 Safety: Implement E-stop and safety interlock functionality.
- ACTRGW-SRD-005 Diagnostics: Monitor actuator health, detect faults, report status.
- ACTRGW-SRD-006 Evidence: All actuator commands and fault events sealed via UTCS/QS.

## SHOULD

- ACTRGW-SRD-007 Performance: Minimize command-to-response latency for optimal control.

## WON'T (baseline)

- ACTRGW-SRD-008 No actuator-level control law implementation.
- ACTRGW-SRD-009 No hot-swap capability during flight.

## Resource Baseline

- CPU: ≤7% of a core for actuator interface processing
- Memory: ≤16 MiB for actuator data and diagnostics
- WCET: ≤2 ms for command processing

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*