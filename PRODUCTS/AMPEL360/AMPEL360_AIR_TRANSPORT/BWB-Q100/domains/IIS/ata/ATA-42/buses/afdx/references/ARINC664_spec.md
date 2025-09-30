---
title: "ARINC 664 Specification Summary"
document_id: REF-ARINC664-001
version: 1.0
date: 2025-09-30
---

# ARINC 664 Specification Summary

## Overview
ARINC 664, Aircraft Data Network (ADN), defines a deterministic Ethernet-based network for avionics applications. Part 7 specifically defines Avionics Full-Duplex Switched Ethernet (AFDX).

## Key Characteristics

### Network Architecture
- **Topology**: Full-duplex switched Ethernet
- **Speed**: 100 Mbps per link
- **Redundancy**: Dual independent networks (A and B)
- **Switching**: Store-and-forward with prioritization

### Virtual Links (VLs)
- **Definition**: Logical unidirectional communication channels
- **Characteristics**:
  - Unique VL identifier (1-65535)
  - Guaranteed bandwidth
  - Bounded latency
  - Deterministic behavior

### Bandwidth Allocation Gap (BAG)
- **Purpose**: Regulates transmission rate
- **Standard Values**: 1, 2, 4, 8, 16, 32, 64, 128 ms
- **Enforcement**: Hardware traffic policing at each switch port
- **Jitter**: Typically ≤1% of BAG

### Frame Format
- **Minimum Size**: 64 bytes (including headers and CRC)
- **Maximum Size**: 1518 bytes (including headers and CRC)
- **Components**:
  - Ethernet header (14 bytes)
  - IP header (20 bytes)
  - UDP header (8 bytes)
  - Payload (20-1472 bytes)
  - CRC (4 bytes)

### Quality of Service (QoS)
- **Priority Levels**: 0-7 (7 = highest priority)
- **Traffic Classes**:
  - Class A: BAG ≤ 8 ms (critical)
  - Class B: BAG > 8 ms (non-critical)
- **Scheduling**: Priority-based with FIFO within same priority

### Redundancy Management
- **Mode**: Dual-active redundancy
- **Operation**: Frames transmitted on both networks
- **Reception**: First valid frame accepted, duplicate discarded
- **Integrity**: Sequence numbers for duplicate detection

### Error Handling
- **CRC Checking**: All frames validated
- **Sequence Validation**: Out-of-order and missing frames detected
- **Fault Isolation**: Per-VL policing and error containment
- **Health Monitoring**: Continuous link status monitoring

## Compliance Requirements

### Traffic Policing
- BAG enforcement at transmit and receive
- Bandwidth allocation group (BAG) limits
- Frame size validation
- VL ID validation

### Determinism
- Bounded end-to-end latency
- Bounded jitter
- Guaranteed bandwidth per VL
- No blocking or starvation

### Reliability
- Dual redundancy (A and B networks)
- Automatic failover
- Error detection (CRC, sequence)
- Frame integrity validation

### Interoperability
- Standard Ethernet physical layer (100BASE-TX)
- Standard frame format
- Defined configuration files (ARINC 664 Part 2)
- Standardized testing procedures

## Configuration Management

### Virtual Link Configuration
Required parameters:
- VL identifier
- Source end system
- Destination end system(s)
- BAG value
- Maximum frame size
- Priority/QoS level
- Redundancy (A, B, or A+B)

### Network Configuration
- Switch port assignments
- VL to port mappings
- Bandwidth allocations
- Priority queue configurations
- Redundancy partnerships

## Testing and Validation

### Functional Tests
- VL establishment and data transfer
- BAG enforcement
- Priority handling
- Redundancy operation

### Performance Tests
- Bandwidth utilization
- Latency measurement
- Jitter analysis
- Throughput validation

### Stress Tests
- Maximum load conditions
- Fault injection
- Recovery time measurement
- Long-duration stability

## Comparison with Standard Ethernet

| Feature | AFDX (ARINC 664) | Standard Ethernet |
|---------|------------------|-------------------|
| Determinism | Guaranteed | Best-effort |
| Bandwidth | Allocated per VL | Shared |
| Latency | Bounded | Variable |
| Redundancy | Built-in dual | Optional |
| QoS | Hardware enforced | Software/optional |
| Configuration | Statically defined | Dynamic |
| Reliability | High (certified) | Variable |

## References
- ARINC 664 Part 7: Avionics Full-Duplex Switched Ethernet Network
- ARINC 664 Part 2: Network Configuration Data
- DO-178C: Software Considerations in Airborne Systems
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware

## Related Documentation
- [AFDX Implementation Guide](./AFDX_implementation_guide.md)
- [Ethernet Comparison](./ethernet_comparison.md)
- [Virtual Links Configuration](../configuration/virtual_links.yaml)
