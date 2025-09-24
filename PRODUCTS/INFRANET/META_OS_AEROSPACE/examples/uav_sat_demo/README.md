---
id: ASIT2-INFRANET-METAOS-DEMO
project: ASI-T2
artifact: UAV+SAT Demo Mission
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-24
maintainer: OOO (OS), IIS (Integration)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# Demo Mission: UAV + Satellite Coordination

Este ejemplo demuestra una misión coordinada entre UAV-01 y SAT-LEO-7, mostrando todos los componentes del Meta-OS funcionando en conjunto.

## Escenario

### Assets
- **UAV-01**: Drone de surveillance con FreeRTOS/ROS2
  - Rol: surveillance, relay
  - Constraints: DAL-A partition, 45W power budget
  - QoS: crit-telemetry profile
  
- **SAT-LEO-7**: Satélite LEO con RTEMS
  - Rol: downlink, compute
  - Contact window: T+00:12..T+00:19
  - Protocols: MIL-STD-1553, SpaceWire

### Mission Flow

1. **Detección** (T+00:00)
   - UAV-01 detecta anomalía usando sensores IMU
   - /uav01/imu topic → QoS reliable, 5ms deadline, prioridad 0x0E

2. **Comunicación** (T+00:05)
   - Middleware traduce datos de ROS2 a MIL-STD-1553
   - Gateway ARINC1553 reenvía a SAT-LEO-7

3. **Decisión** (T+00:12)
   - Orquestador central evalúa situación
   - Digital Twin actualiza estado de misión
   - QOx (quantum optimizer) recalcula ruta óptima

4. **FDIR Activation** (T+00:15)
   - Regla LOST_GNSS se activa por timeout
   - Plan automático: set_mode(FAILSAFE) → plan_rtl()
   - Attestation de sensores GNSS

5. **OTA Update** (T+00:20)
   - Estación terrestre prepara parche firmado
   - OTA manifest con signature BASE64-ED25519
   - Deployment en partition A del UAV-01

## Artifacts Utilizados

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

### Con AQUA OS Components
- **A653_PM**: Proporciona particionado base para DAL-A/B
- **NET_STACK**: Foundation para DDS/ROS2 deterministic networking
- **TIME_SYNC**: PTP/TTE synchronization entre UAV y SAT
- **SEC_KMS**: PKI para OTA signing y zero-trust authentication

### Binary/Hex Examples
- **Priority 0x0E** = 1110₂ (14 decimal) → alta prioridad en 4-bit scheme
- **Memory mapping**: 0x80000000..0x8FFFFFFF para UAV partition A
- **Major frame**: 20ms con minor frames [5,5,5,5] para determinismo ARINC-653

---

*Part of INFRANET Meta-OS Aerospace Extension under ASI-T2 portfolio*