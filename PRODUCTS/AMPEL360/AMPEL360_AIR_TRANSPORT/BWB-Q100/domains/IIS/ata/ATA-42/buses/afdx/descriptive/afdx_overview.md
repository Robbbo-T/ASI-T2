---
title: "AFDX Overview"
document_id: DESC-AFDX-OV-001
version: 1.0
date: 2025-09-30
---

# AFDX Overview

## Introduction
Avionics Full-Duplex Switched Ethernet (AFDX) is a deterministic, high-speed network protocol used in modern aircraft for transmitting critical data between avionics systems. Based on ARINC 664 Part 7, AFDX extends standard Ethernet to meet the stringent reliability and determinism requirements of avionics applications.

## Key Features

### Deterministic Behavior
Unlike standard Ethernet which uses best-effort delivery, AFDX provides guaranteed bandwidth and bounded latency through:
- Static configuration of Virtual Links (VLs)
- Bandwidth Allocation Gap (BAG) enforcement
- Priority-based Quality of Service (QoS)
- Hardware-enforced traffic policing

### Dual Redundancy
All critical data paths use dual independent networks:
- **Network A**: Primary data path
- **Network B**: Independent redundant path
- Frames transmitted on both networks simultaneously
- First valid frame accepted, duplicate discarded
- Automatic failover on network failure

### Quality of Service
Eight priority levels ensure critical data receives preferential treatment:
- Priority 7: Flight-critical data (Flight Control)
- Priority 6: Navigation-critical data
- Priority 5: Engine control
- Priority 3: System monitoring
- Priority 2: Maintenance and diagnostics

## Virtual Links

### Definition
A Virtual Link (VL) is a logical unidirectional communication channel from one source to one or more destinations. Each VL has:
- Unique identifier (1-65535)
- Guaranteed bandwidth
- Bounded latency and jitter
- Specified priority level
- Defined redundancy (A, B, or A+B)

### Configuration
VLs are statically configured before operation:
- Source end system
- Destination end system(s)
- BAG value (transmission interval)
- Maximum frame size
- Priority/QoS level
- Network redundancy

## Bandwidth Allocation Gap (BAG)

### Purpose
BAG regulates the transmission rate to ensure deterministic behavior:
- Minimum time between frame transmissions
- Standard values: 1, 2, 4, 8, 16, 32, 64, 128 ms
- Hardware-enforced at each port
- Prevents bandwidth overrun

### Traffic Classes
- **Class A**: BAG ≤ 8 ms (critical data)
- **Class B**: BAG > 8 ms (non-critical data)

## Network Architecture

### Physical Topology
- Full-duplex switched Ethernet
- 100BASE-TX physical layer
- Point-to-point connections
- No shared media (no collisions)

### Switch Configuration
- Store-and-forward switching
- Priority-based queuing (8 levels)
- Per-port traffic policing
- VLAN support for management/data segregation

## Reliability Features

### Error Detection
- 32-bit CRC on all frames
- Sequence number validation
- Frame size validation
- VL ID validation

### Fault Tolerance
- Dual redundancy (A/B networks)
- Automatic failover < 100 ms
- Health monitoring (10 ms intervals)
- Comprehensive error logging

### Redundancy Management
- Dual-active transmission
- Integrity checking at receiver
- Duplicate frame elimination
- Automatic resynchronization

## Performance Characteristics

### Latency
- End-to-end latency bounded
- Typical: 100-500 µs for critical VLs
- Maximum: Depends on BAG and priority

### Jitter
- Bounded jitter per VL
- Typical: ≤1% of BAG
- Hardware traffic shaping reduces jitter

### Bandwidth Utilization
- Per-VL bandwidth guaranteed
- Total network utilization typically < 50%
- Significant headroom for expansion

## Comparison with Traditional Avionics Networks

| Feature | AFDX | ARINC 429 | MIL-STD-1553 |
|---------|------|-----------|--------------|
| Speed | 100 Mbps | 100 kbps | 1 Mbps |
| Topology | Switched | Point-to-point | Bus |
| Determinism | Guaranteed | Guaranteed | Guaranteed |
| Redundancy | Dual network | Multiple channels | Dual bus |
| Scalability | High | Low | Low |
| Integration | High | Moderate | Moderate |

## Benefits for BWB-Q100

### Integration
- Single network for multiple systems
- Reduced wiring weight and complexity
- Common infrastructure

### Performance
- High bandwidth (100 Mbps per link)
- Low latency for critical data
- Efficient utilization

### Reliability
- Dual redundancy as standard
- Robust error detection
- Proven in commercial aviation

### Maintenance
- Built-in health monitoring
- Comprehensive diagnostics
- Standard test equipment

## Related Documentation
- [Architecture Specification](./architecture_spec.md)
- [Implementation Guide](./implementation_guide.md)
- [ARINC 664 Specification Summary](../references/ARINC664_spec.md)
- [Virtual Links Configuration](../configuration/virtual_links.yaml)
