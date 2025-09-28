# ARINC 653 Partition Manifests

This directory contains ARINC 653 partition manifests for Auto Flight Control System (AFCS) components deployed in the integrated modular avionics (IMA) architecture of the BWB-Q100 aircraft.

## Purpose

Defines AFCS software partitions that run autopilot, flight director, autothrottle, and protection functions within the ARINC 653 compliant avionics architecture, ensuring deterministic timing and spatial isolation for DAL-A critical functions.

## File Types

- **YAML partition manifests** - ARINC 653 partition manifests for AFCS components
- Each manifest specifies partition configuration, resource allocation, interfaces, and health monitoring for Auto Flight functions

## Contents

### Current Manifests

- **`AFCS.partition.yaml`** - Auto Flight Control System partition for flight guidance functions
  - ARINC 653 partition with 20ms major frame scheduling
  - DAL-A criticality for safety-critical autopilot functions
  - ARINC 664 virtual links for flight guidance command distribution
  - ARINC 429 interfaces for roll/pitch command and monitoring
  - Health monitoring with 100ms watchdog and built-in test capability
  - UTCS evidence integration for canonical hash traceability

## ARINC 653 Compliance

All manifests follow ARINC 653 standards for:
- **Partitioning**: Spatial and temporal isolation between AFCS and other avionics functions
- **Scheduling**: Deterministic major frame and window allocation for flight-critical timing
- **Resource Management**: Memory (32MB), CPU (40%), and I/O allocation for AFCS operations
- **Health Monitoring**: Watchdog timers and built-in test for fault detection and isolation

## Interfaces

### ARINC 664 (Ethernet)
- Virtual links for AFCS command distribution to QAFbW and flight surfaces
- Bandwidth Allocation Gap (BAG) scheduling for deterministic data exchange
- End system addressing for avionics backbone integration with NET_STACK

### ARINC 429 (Serial)
- Flight command data transmission (roll/pitch/yaw command labels)
- Source/sink configuration with SDI addressing for redundant channels
- Rate-based data transmission (50 Hz) for real-time control authority

### Sampling Ports
- Real-time sensor data interfaces from NAVSYS and air data systems
- Message-based communication with deterministic timing constraints
- Source/destination port configuration for FMS and HMI_BRIDGE integration

## Security & Evidence

All manifests include:
- **SBOM**: Software Bill of Materials (SPDX format) for AFCS partition components
- **Signatures**: Cosign digital signatures for integrity verification
- **UTCS**: Canonical hash and provenance tracking linked to ATA-22-OV-0001
- **Evidence**: Paths to quality assurance artifacts and test logs
- **MAL-EEM**: Ethics guard compliance markers for crew safety prioritization

## Validation

Validate manifests using AQUA_OS_AIRCRAFT partition manager validation tools and ensure integration with:
- INFRANET/AQUA_OS_AIRCRAFT/components/A653_PM for partition management
- INFRANET/AQUA_OS_AIRCRAFT/components/QAFbW for flight control integration

## Integration

- **AFCS Data Flow**: sensor inputs → AFCS partition → flight command outputs → QAFbW
- **Avionics Interface**: ARINC 664/429 backbone integration with deterministic timing
- **Evidence Chain**: Links to ../../evidence/ for UTCS/QS audit trails and certification compliance
- **Cross-Domain**: Integration with NAVSYS navigation, HMI_BRIDGE displays, and NET_STACK communication