---
id: ASIT2-AQUAOS-AIR-NAVSYS-COMP
project: ASI-T2
artifact: NAVSYS Navigation & Air Data (AQUA OS — Aircraft Extension)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: EDI (Avionics), IIS (Integration)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  quantum_boundaries: out-of-loop-only
  dal_level: B
  partition_type: application
canonical_hash: pending
---

# AQUA OS (Aircraft Extension) — NAVSYS Component Specification

| | |
| :--- | :--- |
| **ID** | `ASIT2-AQUAOS-AIR-NAVSYS-COMP` |
| **Revision** | `1.0` |
| **Component** | NAVSYS Navigation & Air Data (AQUA OS — Aircraft Extension) |
| **Classification** | INTERNAL–EVIDENCE-REQUIRED |
| **Level** | DO-178C DAL-B; Navigation Systems |
| **Owners** | **EDI** (Avionics), **IIS** (Integration) |
| **Bridge** | `CB→QB→UE→FE→FWD→QS` |

## 1. Overview

The **NAVSYS (Navigation & Air Data Systems)** provides fused navigation state estimation using Extended/Unscented Kalman Filtering (EKF/UKF) of IMU, Air Data Computer (ADC), and optional GNSS inputs for consumption by QAFbW and other flight systems.

## 2. Functional Requirements (MoSCoW)

* **MUST**
    * Output fused navigation state at 200-500 Hz with latency ≤5 ms
    * Implement EKF/UKF sensor fusion for IMU, ADC, and GNSS
    * Maintain bounded covariance estimates for state uncertainty
    * Degrade gracefully on sensor failures with validity flags
    * Provide position, velocity, attitude, and angular rates
    * Support multiple sensor redundancy and voting
* **SHOULD**
    * Optimize computational efficiency for real-time operation
    * Provide predictive state estimates for control systems
* **WON'T (baseline)**
    * Implement autonomous navigation without pilot oversight
    * Provide terrain collision avoidance functions

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*