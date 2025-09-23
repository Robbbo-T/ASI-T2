---
id: ASIT2-AQUAOS-AIR-TIMESYNC-SRD
project: ASI-T2
artifact: TIME_SYNC Time & Synchronization (AQUA OS — Aircraft Extension) SRD
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: EDI (Avionics), OOO (OS)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  component: TIME_SYNC Time & Synchronization (AQUA OS — Aircraft Extension)
  level: DO-178C DAL-A; PTP/TTE protocols
  bridges: CB→QB→UE→FE→FWD→QS
  status: BASELINED
canonical_hash: pending
---

# TIME_SYNC System Requirements (MoSCoW)

## MUST

- TIMESYNC-SRD-001 Timebase: Provide monotonic timebase with GM switchover ≤300μs, drift ≤50 ppm, jitter budget ≤500μs on subscribed topics.
- TIMESYNC-SRD-002 API: Expose get_time_ns() to ARINC-653 partitions with zero-allocation, deterministic execution time.
- TIMESYNC-SRD-003 Protocol: Support PTP (IEEE 1588) and TTE time synchronization protocols with network integration.
- TIMESYNC-SRD-004 Switchover: Handle Grandmaster switchover with automatic failover and quality assessment.
- TIMESYNC-SRD-005 Resolution: Maintain nanosecond resolution with monotonic guarantee (no backwards time).
- TIMESYNC-SRD-006 Health: Monitor time synchronization quality, report drift and synchronization failures.
- TIMESYNC-SRD-007 Distribution: Distribute time to all system components with consistent timestamps.
- TIMESYNC-SRD-008 Network Integration: Coordinate with NET_STACK for PTP/TTE message transport.
- TIMESYNC-SRD-009 Hardware Interface: Interface with hardware timer sources and interrupt controllers.
- TIMESYNC-SRD-010 Evidence: All time configuration and synchronization events sealed via UTCS/QS.

## SHOULD

- TIMESYNC-SRD-011 Performance: Minimize CPU overhead for time distribution (≤5% core utilization).
- TIMESYNC-SRD-012 Diagnostics: Provide detailed time synchronization metrics and drift analysis.

## COULD

- TIMESYNC-SRD-013 Adaptive: Implement adaptive clock adjustment based on network conditions.

## WON'T (baseline)

- TIMESYNC-SRD-014 No dependency on QAS quantum time inputs in certified baseline.
- TIMESYNC-SRD-015 No leap second handling during flight operations.

## Resource Baseline

- CPU: ≤5% of a core for time synchronization and distribution
- Memory: ≤8 MiB for protocol stacks and time history
- Hardware: High-resolution timer with interrupt capability

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*