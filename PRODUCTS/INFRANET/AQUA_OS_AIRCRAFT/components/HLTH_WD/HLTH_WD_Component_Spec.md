---
artifact: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-AQUAOS-AIR-HLTHWD-COMP
llc: SYSTEMS
maintainer: IIS (Integration), EDI (Avionics)
project: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
release_date: 2024-09-23
utcs_mi: 'quantum_boundaries: out-of-loop-only

  dal_level: A

  partition_type: platform-service

  '
version: 1.0
---

# AQUA OS (Aircraft Extension) — HLTH_WD Component Specification

| | |
| :--- | :--- |
| **ID** | `ASIT2-AQUAOS-AIR-HLTHWD-COMP` |
| **Revision** | `1.0` |
| **Component** | HLTH_WD Health & Watchdog (AQUA OS — Aircraft Extension) |
| **Classification** | INTERNAL–EVIDENCE-REQUIRED |
| **Level** | DO-178C DAL-A Platform; Health Monitoring |
| **Owners** | **IIS** (Integration), **EDI** (Avionics) |
| **Bridge** | `CB→QB→UE→FE→FWD→QS` |

## 1. Overview

The **HLTH_WD (Health & Watchdog Service)** monitors the health of all AQUA OS Aircraft Extension partitions and services, providing heartbeat monitoring, BITE (Built-In Test Equipment) coordination, and dead-man policy enforcement.

## 2. Functional Requirements (MoSCoW)

* **MUST**
    * Monitor partition heartbeat at ≥10 Hz per partition
    * Implement configurable dead-man action table
    * Provide BITE summary and fault reporting
    * Detect partition overruns and deadline misses
    * Coordinate with A653_PM for partition health status
    * Report health status to maintenance systems
* **SHOULD**
    * Optimize for minimal overhead on monitored partitions
    * Provide predictive health analytics
* **WON'T (baseline)**
    * Perform automatic partition recovery during flight
    * Implement machine learning-based fault prediction

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*