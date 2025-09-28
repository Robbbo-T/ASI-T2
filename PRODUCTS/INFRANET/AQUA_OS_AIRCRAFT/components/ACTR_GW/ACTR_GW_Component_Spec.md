---
artifact: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-AQUAOS-AIR-ACTRGW-COMP
llc: SYSTEMS
maintainer: MEC (Actuation), EDI (Avionics)
project: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
release_date: 2024-09-23
utcs_mi: 'quantum_boundaries: out-of-loop-only

  dal_level: A

  partition_type: platform-service

  '
version: 1.0
---

# AQUA OS (Aircraft Extension) — ACTR_GW Component Specification

| | |
| :--- | :--- |
| **ID** | `ASIT2-AQUAOS-AIR-ACTRGW-COMP` |
| **Revision** | `1.0` |
| **Component** | ACTR_GW Actuator Gateway (AQUA OS — Aircraft Extension) |
| **Classification** | INTERNAL–EVIDENCE-REQUIRED |
| **Level** | DO-178C DAL-A; Actuator Interface |
| **Owners** | **MEC** (Actuation), **EDI** (Avionics) |
| **Bridge** | `CB→QB→UE→FE→FWD→QS` |

## 1. Overview

The **ACTR_GW (Actuator Gateway)** provides low-level actuator bus interfaces, command timeout handling, position feedback, and safe-state management for flight control surfaces, supporting both EHA (Electro-Hydraulic Actuator) and EHSV (Electro-Hydraulic Servo Valve) configurations.

## 2. Functional Requirements (MoSCoW)

* **MUST**
    * Provide physical bus endpoints for EHA/EHSV ECU communication
    * Implement command timeout → safe default within ≤15 ms
    * Support actuator position feedback and current monitoring
    * Provide comprehensive bus diagnostics and fault detection
    * Support both EHA (electrical) and EHSV (hydraulic) actuator types
    * Maintain actuator safety interlocks and E-stop functionality
* **SHOULD**
    * Optimize command-to-response latency for control performance
    * Support actuator health monitoring and prognostics
* **WON'T (baseline)**
    * Implement actuator-level control laws (delegated to QAFbW)
    * Support hot-swappable actuator replacement during flight

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*