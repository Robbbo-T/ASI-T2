---
id: ASIT2-AQUAOS-AIR-HLTHWD-SRD
canonical_hash: pending
---

# HLTH_WD System Requirements (MoSCoW)

## MUST

- HLTHWD-SRD-001 Heartbeat: Monitor partition heartbeat at ≥10 Hz; detect missed heartbeats within 200ms.
- HLTHWD-SRD-002 Dead-man Action: Execute configurable dead-man actions (log/restart/isolate) per partition.
- HLTHWD-SRD-003 BITE: Coordinate Built-In Test Equipment and provide fault summary reporting.
- HLTHWD-SRD-004 Integration: Interface with A653_PM for partition overrun and deadline miss detection.
- HLTHWD-SRD-005 Fault Reporting: Report health events to maintenance and logging systems.
- HLTHWD-SRD-006 Evidence: All health events and configuration sealed via UTCS/QS.

## SHOULD

- HLTHWD-SRD-007 Performance: Minimize monitoring overhead (≤3% CPU utilization).

## WON'T (baseline)

- HLTHWD-SRD-008 No automatic partition recovery during flight.
- HLTHWD-SRD-009 No ML-based fault prediction.

## Resource Baseline

- CPU: ≤3% of a core for health monitoring
- Memory: ≤8 MiB for health data and fault tables

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*