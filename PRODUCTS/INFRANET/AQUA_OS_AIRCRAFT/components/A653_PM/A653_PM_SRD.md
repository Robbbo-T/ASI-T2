---
id: ASIT2-AQUAOS-AIR-A653PM-SRD
project: ASI-T2
artifact: A653_PM Partition Manager (AQUA OS — Aircraft Extension) SRD
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: OOO (OS), IIS (Integration)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  component: A653_PM Partition Manager (AQUA OS — Aircraft Extension)
  level: DO-178C DAL-A; DO-297; ARINC-653
  bridges: CB→QB→UE→FE→FWD→QS
  status: BASELINED
canonical_hash: pending
---

# A653_PM System Requirements (MoSCoW)

## MUST

- A653PM-SRD-001 Partitioning: Enforce ARINC-653 spatial partitioning with MMU-backed memory protection; no partition shall access another's memory space.
- A653PM-SRD-002 Scheduling: Implement temporal partitioning with major frame 10-100ms; partition windows must be deterministic and repeatable.
- A653PM-SRD-003 Isolation: Provide freedom from interference between different DAL level partitions per DO-297 requirements.
- A653PM-SRD-004 Overrun Detection: Detect partition CPU overruns and deadline misses within 1ms; report to health monitoring.
- A653PM-SRD-005 Context Switch: Complete partition context switches in ≤50μs worst-case execution time.
- A653PM-SRD-006 API Compliance: Provide ARINC-653 compliant partition management APIs for application partitions.
- A653PM-SRD-007 Health Integration: Interface with HLTH_WD for partition heartbeat monitoring and fault management.
- A653PM-SRD-008 Resource Management: Track and enforce CPU budgets, memory allocations per partition configuration.
- A653PM-SRD-009 Boot Sequence: Support secure, deterministic partition startup with dependency ordering.
- A653PM-SRD-010 Evidence: All configuration changes and fault events sealed via UTCS/QS; reproducible partition tables.

## SHOULD

- A653PM-SRD-011 Performance: Optimize for minimal hypervisor overhead (≤5% CPU utilization for management functions).
- A653PM-SRD-012 Diagnostics: Provide partition performance metrics, utilization statistics, and fault counters.

## COULD

- A653PM-SRD-013 Dynamic Config: Support partition table updates during ground maintenance (with full reboot).

## WON'T (baseline)

- A653PM-SRD-014 No partition migration between processor cores in flight.
- A653PM-SRD-015 No nested hypervisor support.

## Resource Baseline

- CPU: ≤5% of total system capacity for hypervisor overhead
- Memory: ≤16 MiB for hypervisor kernel and partition tables
- Deterministic: All operations must be bounded and predictable

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*