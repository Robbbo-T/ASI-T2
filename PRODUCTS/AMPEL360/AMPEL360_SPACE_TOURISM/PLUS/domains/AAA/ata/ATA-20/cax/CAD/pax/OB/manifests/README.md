# PAx On-Board Manifests

This directory contains ARINC 653 partition manifests for on-board CAD visualization and processing tools deployed in space vehicle avionics systems.

## Purpose

Defines on-board software partitions that run CAD-related visualization, geometry processing, and display functions within the integrated modular avionics (IMA) architecture of the AMPEL360 PLUS space vehicle.

## File Types

- **`*.yaml`** - ARINC 653 partition manifests for on-board CAD tools
- Each manifest specifies partition configuration, resource allocation, interfaces, and health monitoring

## Contents

### Current Manifests

- **`partition.example.yaml`** - CAD display partition for flight displays
  - ARINC 653 partition with major frame scheduling (100ms/15ms)
  - ARINC 664 virtual links for CAD geometry data
  - ARINC 429 interfaces for vehicle attitude/position
  - Sampling ports for real-time geometry updates
  - Health monitoring and fault tolerance

## ARINC 653 Compliance

All manifests follow ARINC 653 standards for:
- **Partitioning**: Spatial and temporal isolation
- **Scheduling**: Major frame and window allocation
- **Resource Management**: Memory, CPU, and I/O allocation
- **Health Monitoring**: Watchdog and built-in test (BIT)

## Interfaces

### ARINC 664 (Ethernet)
- Virtual links for CAD geometry data exchange
- Bandwidth Allocation Gap (BAG) scheduling
- End system addressing for avionics backbone

### ARINC 429 (Serial)
- Vehicle attitude and position data (octal labels)
- Source/sink configuration with SDI addressing
- Rate-based data transmission (10-50 Hz)

### Sampling Ports
- Real-time geometry data interfaces
- Message-based communication with deterministic timing
- Source/destination port configuration

## Security & Evidence

All manifests include:
- **SBOM**: Software Bill of Materials (SPDX format)
- **Signatures**: Cosign digital signatures for integrity
- **UTCS**: Canonical hash and provenance tracking
- **Evidence**: Paths to quality assurance artifacts

## Validation

Validate manifests using:
```bash
python ../scripts/validate_pax.py partition.example.yaml
```

## Integration

- **CAD Data Flow**: geometry/ → partition → flight displays
- **Avionics Interface**: ARINC 664/429 backbone integration
- **Evidence Chain**: Links to ../../evidence/ for audit trails