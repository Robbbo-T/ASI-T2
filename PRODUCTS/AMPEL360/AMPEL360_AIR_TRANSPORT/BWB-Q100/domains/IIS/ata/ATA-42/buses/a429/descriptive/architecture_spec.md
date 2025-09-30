# ARINC 429 Architecture Specification

**Document ID:** DESC-A429-ARC-002  
**Version:** 1.0  
**Date:** 2025-09-30  
**Classification:** INTERNAL–EVIDENCE-REQUIRED

## System Architecture

### Overview
The BWB-Q100 ARINC 429 implementation consists of multiple independent buses connecting various avionics systems within the Integrated Modular Avionics (IMA) architecture.

## Bus Configuration

### Physical Architecture

#### Channel Allocation
- **Total Channels:** 16 ARINC 429 channels
- **Receive Channels:** 8 (RX-1 through RX-8)
- **Transmit Channels:** 8 (TX-1 through TX-8)

#### Speed Distribution
- **High Speed (100 kbps):** 12 channels
- **Low Speed (12.5 kbps):** 4 channels

### Logical Architecture

#### Data Flow Diagram
```
Sensors → [RX-1] → P-FBW → [TX-1] → Actuators
         (AoA)              (Commands)

P-NAV → [TX-2] → Displays
       (Position, Altitude)

Air Data → [RX-2] → P-FBW
          (Airspeed, Altitude)

Engine Control → [TX-3] → Displays, Maintenance
                (N1, N2, EGT)
```

## Interface Specifications

### Electrical Specifications
- **Line Impedance:** 75 Ω ±5%
- **Termination:** 75 Ω at receiver
- **Maximum Cable Length:** 100 meters
- **Rise/Fall Time:** ≤1.5 µs

### Timing Specifications
- **Bit Time (100 kbps):** 10 µs ±0.5 µs
- **Bit Time (12.5 kbps):** 80 µs ±4 µs
- **Sync Pattern:** High for 4 bit times
- **Inter-word Gap:** Minimum 4 bit times

### Data Word Structure

#### Label (Bits 1-8)
- Transmitted LSB first
- Octal notation (e.g., 203₈, 312₈)
- Identifies parameter type

#### SDI (Bits 9-10)
- Source/Destination Identifier
- Used for multi-channel systems
- Values: 00, 01, 10, 11

#### Data Field (Bits 11-29)
- 19 bits of payload
- Format depends on label:
  - BNR (Binary)
  - BCD (Binary Coded Decimal)
  - Discrete (bit fields)

#### SSM (Bits 30-31)
- Sign/Status Matrix
- Indicates data validity and sign

#### Parity (Bit 32)
- Odd parity
- Covers all 32 bits

## Integration with IMA

### ARINC 653 Partitions
- **P-FBW:** Flight control processing
- **P-NAV:** Navigation processing
- **P-DISP:** Display management
- **P-MAINT:** Maintenance and diagnostics

### Port Mapping
Each partition has dedicated ARINC 429 ports:
- Sampling ports for periodic data
- Queuing ports for event-driven data

### Scheduling
- ARINC 429 processing in minor frames
- Guaranteed processing time for critical labels
- Priority-based label handling

## Redundancy and Fault Tolerance

### Dual Channel Architecture
- Critical data transmitted on redundant channels
- Cross-channel monitoring
- Automatic failover capability

### Error Handling
- Parity error detection
- Timeout detection
- Data staleness monitoring
- Fault logging and reporting

## Performance Requirements

### Latency
- **Critical Data (Flight Control):** <10 ms end-to-end
- **Navigation Data:** <50 ms
- **Maintenance Data:** <200 ms

### Update Rates
- **Flight Control Commands:** 100 Hz
- **Navigation Data:** 10 Hz
- **Engine Data:** 5 Hz
- **Maintenance Data:** 1 Hz

## Compliance

- ARINC 429 Mark 33 specification
- DO-178C Level A (flight-critical functions)
- DO-254 Level A (hardware)
- ARP4754A safety assessment

## Related Documents

- [A429 Overview](./a429_overview.md)
- [Implementation Guide](./implementation_guide.md)
- [Label Definitions](../configuration/label_definitions.yaml)
