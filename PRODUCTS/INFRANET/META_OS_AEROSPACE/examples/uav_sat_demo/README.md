---
artifact: PRODUCTS/INFRANET/META_OS_AEROSPACE/examples
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-INFRANET-METAOS-DEMO
llc: SYSTEMS
maintainer: OOO (OS), IIS (Integration)
project: PRODUCTS/INFRANET/META_OS_AEROSPACE/examples
release_date: 2024-09-24
utcs_mi: v5.0
version: 1.0
---

# Demo Mission: UAV + Satellite Coordination

This example demonstrates a coordinated mission between UAV-01 and SAT-LEO-7, showing all Meta-OS components working together.

## Scenario

### Assets
- **UAV-01**: Surveillance drone with FreeRTOS/ROS2
  - Role: surveillance, relay
  - Constraints: DAL-A partition, 45W power budget
  - QoS: crit-telemetry profile
  
- **SAT-LEO-7**: LEO satellite with RTEMS
  - Role: downlink, compute
  - Contact window: T+00:12..T+00:19
  - Protocols: MIL-STD-1553, SpaceWire

### Mission Flow

1. **Detection** (T+00:00)
   - UAV-01 detects anomaly using IMU sensors
   - /uav01/imu topic → QoS reliable, 5ms deadline, priority 0x0E

2. **Communication** (T+00:05)
   - Middleware translates data from ROS2 to MIL-STD-1553
   - ARINC1553 gateway forwards to SAT-LEO-7

3. **Decision** (T+00:12)
   - Central orchestrator evaluates situation
   - Digital Twin updates mission state
   - QOx (quantum optimizer) recalculates optimal route

4. **FDIR Activation** (T+00:15)
   - LOST_GNSS rule activates due to timeout
   - Automatic plan: set_mode(FAILSAFE) → plan_rtl()
   - GNSS sensor attestation

5. **OTA Update** (T+00:20)
   - Ground station prepares signed patch
   - OTA manifest with BASE64-ED25519 signature
   - Deployment to UAV-01 partition A

## Artifacts Used

- **Mission manifest**: `../../orchestrator/manifests/mission/uav_sat_demo.yaml`
- **QoS policies**: `../../middleware/dds/qos_policies.yaml`
- **FDIR rules**: `../../security/fdir/rules/uav_fdir.yaml`
- **OTA manifest**: `../../security/ota/update-manifests/uav01_2025-09-24.json`
- **Partition map**: `../../platforms/uav/partitions.map`

## Execution

```bash
# Deploy mission with attestation
cd /path/to/META_OS_AEROSPACE
python tooling/cli/metaosctl.py deploy orchestrator/manifests/mission/uav_sat_demo.yaml --require-attestation

# Monitor QoS for UAV-01
python tooling/cli/metaosctl.py qos audit --profile crit-telemetry --asset UAV-01

# Test FDIR scenario
python tooling/cli/metaosctl.py fdir test security/fdir/rules/uav_fdir.yaml --inject LOST_GNSS
```

## Expected Output

```
[deploy] Manifest: orchestrator/manifests/mission/uav_sat_demo.yaml
[deploy] missionId=MS-0x4A3C assets=2
[deploy] Attestation REQUIRED → (stub) verifying TPM/TEE evidence... OK
[deploy] Placement policy: deterministic
[deploy] DONE (stub).
```

## Integration Points

### Integration with AQUA OS Components
- **A653_PM**: Provides base partitioning for DAL-A/B
- **NET_STACK**: Foundation for deterministic DDS/ROS2 networking
- **TIME_SYNC**: PTP/TTE synchronization between UAV and SAT
- **SEC_KMS**: PKI for OTA signing and zero-trust authentication

### Binary/Hex Examples
- **Priority 0x0E** = 1110₂ (14 decimal) → high priority in 4-bit scheme
- **Memory mapping**: 0x80000000..0x8FFFFFFF for UAV partition A
- **Major frame**: 20ms with minor frames [5,5,5,5] for ARINC-653 determinism

---

*Part of INFRANET Meta-OS Aerospace Extension under ASI-T2 portfolio*