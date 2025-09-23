---
id: ASIT2-AQUAOS-AIR-QAFBW-COMP
project: ASI-T2
artifact: QAFbW Control Stack (AQUA OS — Aircraft Extension)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: OOO (OS), LCC (Control Laws), EDI (Avionics/Net), IIS (Software), MEC (Actuation)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  quantum_boundaries: out-of-loop-only
  dal_level: A
  partition_type: ARINC-653
canonical_hash: pending
---

# AQUA OS (Aircraft Extension) — QAFbW Component Specification

| | |
| :--- | :--- |
| **ID** | `ASIT2-AQUAOS-AIR-QAFBW-COMP` |
| **Revision** | `1.0` |
| **Component** | QAFbW Control Stack (AQUA OS — Aircraft Extension) |
| **Classification** | INTERNAL–EVIDENCE-REQUIRED |
| **Level** | DO-178C DAL-A Application; DO-326A/356A |
| **Owners** | **OOO** (OS), **LCC** (Control Laws), **EDI** (Avionics/Net), **IIS** (Software), **MEC** (Actuation) |
| **Bridge** | `CB→QB→UE→FE→FWD→QS` |

---

## 1. Purpose and Scope

This document defines the component-level contract for integrating the **Quantum-Assisted Fly-by-Wire (QAFbW)** stack into the **AQUA OS – Aircraft Extension**. It specifies the services, interfaces, partitioning requirements, security posture, and verification criteria for the component.

Quantum capabilities, such as QRNG, QKD, or quantum sensing, are treated as **optional, out-of-loop assistive services** consumed by the QAFbW component. They must not reside in the hard real-time control path or affect DAL-A determinism.

---

## 2. Architectural Placement within AQUA OS

The QAFbW component operates as a high-criticality, partitioned application running on top of the core AQUA OS kernel and services.

* **AQUA Kernel / Hypervisor (Core OS Services)**
    * Time & Sync Service (e.g., PTP/TTE)
    * Deterministic Network Stack (e.g., AFDX/TSN)
    * Security & Secrets Management (PKI, KMS, optional QKD ingest)
    * Storage & UTCS/QS Evidence Sealing
    * Health Monitoring, Watchdogs, and Logging
    * Abstracted I/O (Sensors / Actuators)
* **ARINC-653 Partitions**
    * **P1: QAFbW Control Stack (this component, DAL-A)**
    * P2: Navigation & Air Data Systems (e.g., DAL-B)
    * P3: Human-Machine Interface & Annunciations (e.g., DAL-B)
    * P4: Maintenance & Diagnostics (e.g., DAL-C)
    * **P5: Quantum Assist Services (QAS) (DAL-C/B, out-of-loop)**

---

## 3. Component Service Contract

### 3.1 Services Provided by QAFbW

| Service | Description |
| :--- | :--- |
| `FCL.CommandOut` | A 200–500 Hz stream of actuator commands (position/rate/force). |
| `FCL.ModeStatus` | The current operational mode (`NORMAL`, `ALTERNATE`, `DIRECT`, `REVERSIONARY`) with transition reasons. |
| `FCL.EnvelopeStatus` | The status of flight envelope protections (active, relaxed, limits engaged). |
| `FCL.Health` | The health of the component, including voter state (2oo3), channel disagreement, timing margins, and sensor validity. |

### 3.2 Services Required from AQUA OS

| Service | Requirement |
| :--- | :--- |
| **Time/Sync** | Access to a monotonic clock; must tolerate Grandmaster switchover without violating jitter budgets. |
| **Deterministic Network** | Guaranteed bandwidth and latency on physically independent A/B networks (VL/QoS per ICD). |
| **I/O Abstraction** | Typed data frames for sensors and access to actuator endpoints with guaranteed timeout behaviors. |
| **Security/Secrets** | A verified boot environment, code-signing validation, and access to session keys. |
| **UTCS/QS** | An API to seal evidence for builds, configurations, test runs, and critical logs. |
| **Health/Watchdog** | A per-partition heartbeat mechanism with a defined dead-man policy. |

---

## 4. Partitioning and Scheduling Contract (PSSC)

* **Criticality**: **DAL-A**. The component must be hosted in a memory-protected ARINC-653 partition.
* **CPU Budget**: ≥ 30% of a core, scheduled with a fixed-priority, preemptive policy.
* **Memory Budget**: ≥ 64 MiB of private, non-swappable RAM.
* **WCET**: End-to-end control loop latency (sensor-to-actuator) must be **≤ 15 ms**.
* **Jitter**: Network jitter for all critical VLs must be within ICD limits (e.g., ≤ 500 µs peak-to-peak).
* **Freedom from Interference**: The component shall not use shared writable memory with partitions of a different DAL. All I/O is mediated by the AQUA OS kernel.

---

## 5. Interfaces (ICD Summary)

The component communicates via logical topics managed by the AQUA OS deterministic network stack.

| Topic ID | Direction | Rate (Hz) | Payload Example |
| :--- | :--- | :--- | :--- |
| `aqua.fcl.sensor.imu` | IN | 500 | `{timestamp, gyro[3], accel[3], flags}` |
| `aqua.fcl.sensor.airdata` | IN | 200 | `{timestamp, p_static, p_total, flags}` |
| `aqua.fcl.command` | OUT | 200–500 | `{timestamp, pos_cmd[], rate_cmd[], mode}` |
| `aqua.fcl.mode_status` | OUT | 50 | `{mode, substate, reason, timers}` |
| `aqua.fcl.health` | OUT | 10 | `{voter, disagree, wcet, jitter, sensor_validity}` |
| `aqua.qas.aux` (optional) | IN | ≤ 50 | `{kind, quality, value, ttl}` |

All frames must carry a CRC, sequence number, and validity flags. The time base is provided by AQUA OS.

---

## 6. Functional Requirements (MoSCoW)

* **MUST**
    * Achieve a catastrophic command integrity failure rate of ≤ 1×10⁻⁹ per flight hour (per CS-25.1309).
    * Implement `NORMAL`, `ALTERNATE`, `DIRECT`, and `REVERSIONARY` modes with bounded, non-oscillatory transitions.
    * Utilize a 2-out-of-3 voter that freezes on sustained disagreement per a defined safety policy.
    * Operate within the defined PSSC latency (≤ 15 ms WCET) and rate (200-500 Hz) budgets.
    * **Not block or alter FCL timing** based on the availability or quality of the optional Quantum Assist Services (QAS).
    * Pass secure boot and code-signing validation provided by AQUA OS.
* **SHOULD**
    * Detect and mitigate critical faults within 50 ms.
    * Provide built-in, maintenance-guarded fault injection capabilities.
* **COULD**
    * Use entropy from QRNG (via QAS) to enhance the security of cryptographic operations.
* **WON'T**
    * Implement any in-loop quantum control algorithms in the certification baseline.
    * Use an on-aircraft blockchain ledger within the DAL-A partition.

---

## 7. Verification and Conformance Strategy

Verification is performed against the AQUA OS contract.

| Category | Verification Method |
| :--- | :--- |
| **Platform & Scheduling** | Timing and jitter analysis over ≥10,000 major frames under worst-case load. Partition interference tests by stressing adjacent partitions. |
| **Network & I/O** | Conformance tests for the deterministic network profile, including A/B failover. Actuator and sensor dropout injection tests. |
| **Safety & Modes** | HIL-based fault-injection campaigns covering all specified failure modes. Pilot-in-the-loop evaluation of mode transitions and HMI cues. |
| **Security** | Positive and negative testing of secure boot and message authentication (e.g., tampering, replay attacks). |
| **Quantum Boundaries** | Tests demonstrating that the loss or degradation of QAS inputs has a benign impact and does not affect control loop timing or mode. |
| **Evidence & Traceability** | All verification artifacts (procedures, results, logs) are sealed via UTCS/QS. A VCRM links every requirement to its test case and result. |

---

## 8. Cross-Product Binding (BWB-Q100 Example)

This AQUA OS component is generic. It is adapted for a specific product like the **AMPEL360 BWB-Q100** through a **Product Binding Package**. This package, located in the product's domain folders (e.g., `LCC/ata/ATA-27`), contains:

1.  **ICDs**: The mapping of logical topics (e.g., `aqua.fcl.sensor.imu`) to the physical sensors and buses of the BWB-Q100.
2.  **Tuning Parameters**: The specific control law gains, envelope limits, and actuator models for the BWB-Q100 airframe.
3.  **Product-Specific Tests**: HIL and Iron Bird test campaigns that validate the component's performance on the target hardware.

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*