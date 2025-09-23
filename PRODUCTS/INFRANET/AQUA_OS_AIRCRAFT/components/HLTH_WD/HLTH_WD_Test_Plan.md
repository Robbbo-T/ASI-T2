---
id: ASIT2-AQUAOS-AIR-HLTHWD-TEST
canonical_hash: pending
---

# HLTH_WD Health & Watchdog Test Plan

## Test Categories

### Unit Tests (UT)
- **UT-HLTHWD-001**: Heartbeat monitoring logic
- **UT-HLTHWD-002**: Dead-man action execution

### Integration Tests (IT)
- **IT-HLTHWD-001**: Multi-partition health monitoring
- **IT-HLTHWD-002**: A653_PM integration

### System Tests (ST)
- **ST-HLTHWD-001**: Full system health monitoring
- **ST-HLTHWD-002**: Fault injection testing

## Pass/Fail Criteria
- Heartbeat detection within 200ms
- CPU overhead ≤3%

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*