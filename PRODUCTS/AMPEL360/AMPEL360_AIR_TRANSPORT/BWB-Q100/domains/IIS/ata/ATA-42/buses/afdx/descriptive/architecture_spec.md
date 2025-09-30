---
title: "AFDX Architecture Specification"
document_id: DESC-AFDX-ARCH-001
version: 1.0
date: 2025-09-30
---

# AFDX Architecture Specification

## System Overview

The BWB-Q100 AFDX network provides deterministic, high-bandwidth communication between critical avionics systems. The architecture consists of dual-redundant networks, four switches, and multiple end systems communicating via Virtual Links.

## Network Topology

### Physical Architecture

```
Network A:                    Network B:
┌─────────────┐              ┌─────────────┐
│  SW-A-1     │              │  SW-B-1     │
│  (Forward)  │              │  (Forward)  │
└─────────────┘              └─────────────┘
      │                            │
      ├───── End Systems ──────────┤
      │                            │
┌─────────────┐              ┌─────────────┐
│  SW-A-2     │              │  SW-B-2     │
│  (Aft)      │              │  (Aft)      │
└─────────────┘              └─────────────┘
      │                            │
      └───── End Systems ──────────┘
```

### Network Segregation

- **Network A**: Independent physical infrastructure
- **Network B**: Independent physical infrastructure
- **No cross-connections**: Networks physically isolated
- **Separate power**: Independent power sources
- **Separate routing**: Different cable paths

## End Systems

### Critical Flight Systems
- **Flight Control Computer (FCC)**
  - VL Source: VL-1001 (Flight_Control_Data)
  - VL Sink: VL-1002, VL-1003, VL-1004
  - Redundancy: A+B
  - Priority: 7

- **Navigation System**
  - VL Source: VL-1002 (Navigation_Data)
  - VL Sink: VL-1001
  - Redundancy: A+B
  - Priority: 6

- **Air Data Computer**
  - VL Source: VL-1003 (Air_Data)
  - VL Sink: VL-1001, VL-1004
  - Redundancy: A+B
  - Priority: 7

### Engine Systems
- **Engine Control Unit**
  - VL Source: VL-1004 (Engine_Parameters)
  - VL Sink: VL-1001, VL-1005
  - Redundancy: A+B
  - Priority: 5

### Monitoring Systems
- **System Monitor**
  - VL Source: VL-1005 (System_Status)
  - VL Sink: VL-1006
  - Redundancy: A
  - Priority: 3

- **Maintenance System**
  - VL Source: VL-1006 (Maintenance_Data)
  - VL Sink: VL-1005
  - Redundancy: A
  - Priority: 2

## Virtual Links Architecture

### VL-1001: Flight_Control_Data
- **Purpose**: Critical flight control commands
- **Source**: Flight Control Computer
- **Destinations**: Actuator Control, Display System, Maintenance System
- **BAG**: 2 ms
- **Frame Size**: 1518 bytes
- **Bandwidth**: 6.072 Mbps
- **Redundancy**: A+B (dual-active)
- **Priority**: 7 (highest)
- **DAL**: A (catastrophic)

### VL-1002: Navigation_Data
- **Purpose**: Navigation state information
- **Source**: Navigation System
- **Destinations**: FCC, Display System, Autopilot
- **BAG**: 20 ms
- **Frame Size**: 1518 bytes
- **Bandwidth**: 607.2 kbps
- **Redundancy**: A+B (dual-active)
- **Priority**: 6
- **DAL**: A (catastrophic)

### VL-1003: Air_Data
- **Purpose**: Airspeed, altitude, temperature
- **Source**: Air Data Computer
- **Destinations**: FCC, Engine Control, Display System
- **BAG**: 10 ms
- **Frame Size**: 1518 bytes
- **Bandwidth**: 1.214 Mbps
- **Redundancy**: A+B (dual-active)
- **Priority**: 7 (highest)
- **DAL**: A (catastrophic)

### VL-1004: Engine_Parameters
- **Purpose**: Engine performance data
- **Source**: Engine Control Unit
- **Destinations**: FCC, Display System, Maintenance System
- **BAG**: 50 ms
- **Frame Size**: 1518 bytes
- **Bandwidth**: 242.9 kbps
- **Redundancy**: A+B (dual-active)
- **Priority**: 5
- **DAL**: B (hazardous)

### VL-1005: System_Status
- **Purpose**: Health monitoring data
- **Source**: System Monitor
- **Destinations**: Display System, Maintenance System, Ground Station
- **BAG**: 100 ms
- **Frame Size**: 1518 bytes
- **Bandwidth**: 121.4 kbps
- **Redundancy**: A (single)
- **Priority**: 3
- **DAL**: C (major)

### VL-1006: Maintenance_Data
- **Purpose**: Diagnostic and logging data
- **Source**: Maintenance System
- **Destinations**: Ground Station, Display System
- **BAG**: 1000 ms
- **Frame Size**: 1518 bytes
- **Bandwidth**: 12.1 kbps
- **Redundancy**: A (single)
- **Priority**: 2
- **DAL**: E (no effect)

## Switch Architecture

### Switch Specifications
- **Model**: Certified AFDX switch
- **Ports**: 24 × 100BASE-TX
- **Buffer**: 2 MB per switch
- **Priority Queues**: 8 levels (0-7)
- **Traffic Policing**: Hardware-based BAG enforcement
- **Redundancy**: Hot-standby configuration

### Switch Configuration

#### SW-A-1 (Forward, Network A)
- **Location**: Forward equipment bay
- **Connected Systems**: 
  - FCC (Port 1-2)
  - Navigation (Port 3-4)
  - Air Data (Port 5-6)
  - Display System (Port 7-8)
- **Management**: Port 24
- **Redundancy Partner**: SW-B-1

#### SW-B-1 (Forward, Network B)
- **Location**: Forward equipment bay
- **Connected Systems**: Same as SW-A-1
- **Management**: Port 24
- **Redundancy Partner**: SW-A-1

#### SW-A-2 (Aft, Network A)
- **Location**: Aft equipment bay
- **Connected Systems**:
  - Engine Control (Port 1-2)
  - System Monitor (Port 3)
  - Maintenance System (Port 4)
  - Actuator Control (Port 5-10)
- **Management**: Port 24
- **Redundancy Partner**: SW-B-2

#### SW-B-2 (Aft, Network B)
- **Location**: Aft equipment bay
- **Connected Systems**: Same as SW-A-2
- **Management**: Port 24
- **Redundancy Partner**: SW-A-2

## Bandwidth Allocation

### Total Network Capacity
- **Link Speed**: 100 Mbps per network
- **Reserved**: 10 Mbps for management
- **Available**: 90 Mbps for VLs

### Utilization by Priority

| Priority | Allocation | Usage | Utilization |
|----------|-----------|-------|-------------|
| 7 (Critical) | 40 Mbps | 7.3 Mbps | 18.2% |
| 6 (High) | 20 Mbps | 0.6 Mbps | 3.0% |
| 5 (Medium) | 15 Mbps | 0.2 Mbps | 1.5% |
| 3 (Low) | 10 Mbps | 0.1 Mbps | 1.2% |
| 2 (Lowest) | 5 Mbps | 0.01 Mbps | 0.2% |
| **Total** | **90 Mbps** | **8.2 Mbps** | **9.1%** |

### Growth Capacity
- **Current Usage**: 8.2 Mbps (9.1%)
- **Available**: 81.8 Mbps (90.9%)
- **Headroom**: Sufficient for 10× growth

## Redundancy Management

### Dual-Active Operation
1. **Normal Operation**:
   - Frames transmitted on both networks
   - First valid frame accepted
   - Duplicate discarded via sequence numbers

2. **Network A Failure**:
   - Detection time: < 15 ms
   - Continue on Network B only
   - Frame loss: < 0.1%
   - Recovery time: < 100 ms

3. **Network B Failure**:
   - Detection time: < 15 ms
   - Continue on Network A only
   - Frame loss: < 0.1%
   - Recovery time: < 100 ms

4. **Network Recovery**:
   - Automatic resynchronization
   - Resume dual-active operation
   - No manual intervention required

### Health Monitoring
- **Monitoring Interval**: 10 ms
- **Metrics**:
  - Link status (up/down)
  - Frame counters (tx/rx)
  - Error counters (CRC, sequence)
  - Bandwidth utilization
- **Alarms**:
  - Link down (immediate)
  - High error rate (> 0.1%)
  - High utilization (> 75%)
  - BAG violation

## Quality of Service

### Priority Levels
| Priority | Class | Typical Use | Max Latency |
|----------|-------|-------------|-------------|
| 7 | Critical | Flight control | 100 µs |
| 6 | High | Navigation | 500 µs |
| 5 | Medium | Engine | 1 ms |
| 4 | Medium-low | - | 2 ms |
| 3 | Low | Monitoring | 5 ms |
| 2 | Very low | Maintenance | 10 ms |
| 1 | - | Reserved | - |
| 0 | - | Reserved | - |

### Scheduling
- **Algorithm**: Strict priority
- **Preemption**: Higher priority preempts lower
- **Starvation Prevention**: BAG enforcement ensures fairness
- **Queue Management**: Tail drop for overflow

## Security Architecture

### Network Isolation
- **Physical**: Networks A and B physically separate
- **Logical**: VLs cannot interfere with each other
- **Access Control**: Managed switch ports only
- **Management**: Separate management network

### Data Integrity
- **CRC**: 32-bit CRC on all frames
- **Sequence Numbers**: Detect duplicates and missing frames
- **VL Validation**: Check VL ID on reception
- **Frame Validation**: Verify frame size and format

### Domain Segregation
- **Critical Systems**: Isolated on AFDX
- **Cabin Systems**: Separate CabinNet network
- **Gateway**: One-way filtered gateway
- **Whitelisted Signals**: Only approved data crosses domains

## Performance Characteristics

### Latency Budget
| Component | Latency | Accumulation |
|-----------|---------|--------------|
| End system TX | 50 µs | 50 µs |
| Switch queuing | 20 µs | 70 µs |
| Transmission | 10 µs | 80 µs |
| Switch queuing | 20 µs | 100 µs |
| End system RX | 50 µs | 150 µs |
| **Total** | - | **150 µs** |

### Jitter Analysis
- **VL-1001 (2ms BAG)**: < 50 µs (2.5%)
- **VL-1002 (20ms BAG)**: < 200 µs (1.0%)
- **VL-1003 (10ms BAG)**: < 100 µs (1.0%)
- **VL-1004 (50ms BAG)**: < 500 µs (1.0%)

### Reliability Metrics
- **Frame Error Rate**: < 10^-12
- **Availability**: > 99.999%
- **MTBF**: > 10,000 hours per switch
- **MTTR**: < 30 minutes

## Related Documentation
- [AFDX Overview](./afdx_overview.md)
- [Implementation Guide](./implementation_guide.md)
- [Virtual Links Configuration](../configuration/virtual_links.yaml)
- [Switch Configuration](../configuration/switch_configuration.json)
