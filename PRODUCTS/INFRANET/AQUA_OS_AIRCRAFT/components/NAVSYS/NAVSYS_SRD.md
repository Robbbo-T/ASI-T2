---
id: ASIT2-AQUAOS-AIR-NAVSYS-SRD
canonical_hash: pending
---

# NAVSYS System Requirements (MoSCoW)

## MUST

- NAVSYS-SRD-001 State Output: Output latency ≤5 ms, bounded covariance; degrade gracefully on sensor drops.
- NAVSYS-SRD-002 Fusion: Implement EKF/UKF fusion of IMU, ADC, GNSS with validity flags.
- NAVSYS-SRD-003 Rate: Provide navigation state at 200-500 Hz for flight control consumption.
- NAVSYS-SRD-004 Accuracy: Maintain position accuracy within navigation performance requirements.
- NAVSYS-SRD-005 Redundancy: Support multiple sensor inputs with voting and fault detection.
- NAVSYS-SRD-006 Evidence: All navigation configuration and sensor events sealed via UTCS/QS.

## SHOULD

- NAVSYS-SRD-007 Performance: Optimize computational efficiency for real-time constraints.

## WON'T (baseline)

- NAVSYS-SRD-008 No autonomous navigation functions.
- NAVSYS-SRD-009 No terrain collision avoidance.

## Resource Baseline

- CPU: ≤12% of a core for state estimation
- Memory: ≤48 MiB for filter state and sensor data
- WCET: ≤3 ms for state update cycle

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*