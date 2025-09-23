---
id: ASIT2-AQUAOS-AIR-HLTHWD-COMP
project: ASI-T2
artifact: HLTH_WD Health & Watchdog (AQUA OS — Aircraft Extension)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: IIS (Integration), EDI (Avionics)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  quantum_boundaries: out-of-loop-only
  dal_level: A
  partition_type: platform-service
canonical_hash: pending
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