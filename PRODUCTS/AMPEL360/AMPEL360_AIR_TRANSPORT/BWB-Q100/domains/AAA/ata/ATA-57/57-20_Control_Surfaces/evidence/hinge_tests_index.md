# Hinge Tests Evidence

Torque, friction, free play; link to rigs, calibration certs, raw traces; UTCS/QS anchors.

## Hinge Test Types

Document references to:
- Hinge friction and torque measurements
- Free play measurements
- Hinge wear tests
- Load capacity tests
- Bearing performance tests
- Lubrication effectiveness tests

## Test Equipment

Required test equipment and calibration:
- Torque measurement rigs
- Dial indicators for free play
- Load cells for capacity tests
- Temperature monitoring equipment
- Data acquisition systems

## Evidence References

All evidence files are stored externally with references here including:
- Test rig specifications and calibration certificates
- Raw data traces and processed results
- Test procedure references (S1000D DM codes)
- Effectivity information (hinge P/N, S/N)
- Associated acceptance metrics (CO-3.13)
- QS/UTCS anchors

## Format

```yaml
evidence_entry:
  id: HINGE-TEST-001
  type: hinge_friction_test
  description: "Elevon hinge friction measurement, ambient temp"
  hinge_pn: "HNG-ELV-001"
  hinge_sn: "12345"
  test_date: "2025-02-10"
  test_rig: "HINGE-RIG-001"
  calibration_cert: "CAL-2025-001"
  uri: "pdm://BWB-Q100/tests/hinges/friction_test_HNG001_SN12345.csv"
  sha256: "jkl012..."
  acceptance_metric_ref: "ACPT-HINGE-FRICTION-001"
  result: "PASS"
  measured_torque_Nm: 0.35
  utcs_anchor: "sha256:mno345..."
  timestamp: "2025-02-10T16:20:00Z"
```

## Acceptance Criteria

- Hinge friction: ≤ 0.5 Nm (typical)
- Free play: ≤ 0.1 mm
- Load capacity: per specification
- No binding or rough spots throughout range of motion
