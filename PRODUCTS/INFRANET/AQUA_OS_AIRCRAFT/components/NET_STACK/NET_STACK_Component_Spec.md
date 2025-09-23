---
id: ASIT2-AQUAOS-AIR-NETSTACK-COMP
project: ASI-T2
artifact: NET_STACK Deterministic Network (AQUA OS — Aircraft Extension)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: EDI (Avionics/Net), OOO (OS)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  quantum_boundaries: out-of-loop-only
  dal_level: A
  partition_type: platform-service
canonical_hash: pending
---

# AQUA OS (Aircraft Extension) — NET_STACK Component Specification

| | |
| :--- | :--- |
| **ID** | `ASIT2-AQUAOS-AIR-NETSTACK-COMP` |
| **Revision** | `1.0` |
| **Component** | NET_STACK Deterministic Network (AQUA OS — Aircraft Extension) |
| **Classification** | INTERNAL–EVIDENCE-REQUIRED |
| **Level** | DO-178C DAL-A Platform; AFDX/TSN/TTE |
| **Owners** | **EDI** (Avionics/Net), **OOO** (OS) |
| **Bridge** | `CB→QB→UE→FE→FWD→QS` |

## 1. Overview

The **NET_STACK (Deterministic Network Stack)** provides real-time, deterministic networking services for AQUA OS Aircraft Extension, supporting AFDX, TSN, and TTE protocols with guaranteed Quality of Service (QoS) and dual-network failover capabilities.

## 2. Architectural Placement within AQUA OS

The NET_STACK operates as a platform-level network service layer:

* **AQUA Kernel / Hypervisor (Core OS Services)**
    * A653_PM Partition Manager
    * **NET_STACK Deterministic Network (this component, DAL-A platform)**
    * TIME_SYNC Service (GM/PTP coordination)
    * Security & Secrets Management
    * Health Monitoring & Logging
* **Network Interfaces**
    * Dual-redundant Ethernet (NET-A, NET-B)
    * Virtual Link (VL) management and QoS enforcement
    * MAC/Authentication layer integration

## 3. Component Service Contract

### 3.1 Services Provided by NET_STACK

| Service | Description |
| :--- | :--- |
| **VL Management** | Virtual Link creation, bandwidth allocation, QoS enforcement |
| **Dual-Net Failover** | Seamless failover between redundant networks (≤3 lost frames) |
| **Traffic Policing** | Rate limiting, burst control, priority scheduling |
| **Message Authentication** | MAC-128 integrity checking for critical topics |
| **Network Health** | Link status monitoring, statistics collection |

### 3.2 Services Required from AQUA OS

| Service | Requirement |
| :--- | :--- |
| **Time Synchronization** | PTP/TTE timebase for deterministic scheduling |
| **Security/KMS** | Session keys and MAC computation for message authentication |
| **Partition Management** | Integration with A653_PM for network resource isolation |
| **Health Monitoring** | Fault reporting and network status to HLTH_WD |

## 4. Partitioning and Scheduling Contract (PSSC)

NET_STACK operates as a platform service with dedicated network processing resources.

## 5. Interfaces (ICD Summary)

NET_STACK provides network transport for all AQUA OS topics while publishing its own status information.

## 6. Functional Requirements (MoSCoW)

* **MUST**
    * Support AFDX, TSN, and TTE protocols with deterministic latency
    * Provide dual-network redundancy with seamless failover (≤3 lost frames)
    * Enforce VL bandwidth allocation and QoS policies
    * Support MTU up to 1518 bytes per VL
    * Implement traffic policing with configurable rate limits
    * Provide GMAC-128 authentication for critical safety topics
    * Maintain network statistics and health monitoring
* **SHOULD**
    * Optimize for low-latency forwarding (≤100μs per hop)
    * Support network topology discovery and auto-configuration
* **COULD**
    * Implement adaptive QoS based on network conditions
* **WON'T (baseline)**
    * Support dynamic VL reconfiguration during flight
    * Implement packet-level encryption (authentication only)

## 7. Verification and Conformance Strategy

* **Unit Testing**: VL management, QoS enforcement, failover mechanisms
* **Integration Testing**: Multi-component network traffic, timing verification
* **Certification Testing**: DO-178C DAL-A evidence, determinism proofs

## 8. Cross-Product Binding (BWB-Q100 Example)

When deployed on BWB-Q100, NET_STACK carries QAFbW control topics, navigation data, and HMI information across dual-redundant avionics networks with guaranteed deterministic delivery.

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*