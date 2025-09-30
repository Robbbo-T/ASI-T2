# ARINC 653 Operating System Configuration — ATA-42 IMA

**Parent:** [../README.md](../README.md)  
**Related:** [../partitions/](../partitions/) · [../interfaces/](../interfaces/)

## Purpose

ARINC 653 RTOS configuration files including partition scheduling, health monitoring, and memory maps for the BWB-Q100 IMA system.

## Contents

- **`schedule.xml`** — Partition scheduling configuration (major frame, windows, ordering)
- **`HM_Table.xml`** *(planned)* — Health Monitoring table (error responses, recovery actions)
- **`memory_map.xml`** *(planned)* — Memory allocation per partition (RAM, heap, stack)
- **`config_validation.md`** *(planned)* — Configuration rules and validation procedures

## Key Files

| File | Description | Status |
|------|-------------|--------|
| `schedule.xml` | ARINC 653 partition schedule (8ms major frame) | ✅ Active |

## Schedule Configuration

**Major frame:** 8 ms (aligned with AFDX Class-A traffic)

**Partition execution order** (causal flow):
1. **P-NAV** (0-2ms): Navigation data computation → outputs to P-FBW & P-DISP
2. **P-FBW** (2-4ms): Flight control laws using fresh nav data → outputs to actuators
3. **P-SEC** (4-5ms): Security services and attestation
4. **P-DISP** (5-7ms): Display rendering using fresh nav & FBW data
5. **P-MAINT** (7-8ms): Maintenance logging

**Total utilization:** 8ms / 8ms = 100% (deterministic, no idle time in baseline)

## Standards

- **ARINC 653** — Avionics Application Software Standard Interface
- **Time partitioning:** Deterministic scheduling, non-preemptive windows
- **Space partitioning:** MMU/MPU enforced memory isolation
- **Health monitoring:** Partition error detection and recovery

## Design Constraints

- Each partition executes once per major frame
- Windows must not overlap
- Total window duration ≤ major frame
- Causal ordering: data producers before consumers
- No idle time (continuous execution)

## Validation

ARINC 653 configuration validated by `../tools/ci/validate_schedule.py` (planned):
- Window sum ≤ major frame
- No overlaps
- Causal ordering maintained

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial OS directory README |
