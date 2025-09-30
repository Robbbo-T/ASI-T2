# ARINC 429 Bus Overview

**Document ID:** DESC-A429-OVW-001  
**Version:** 1.0  
**Date:** 2025-09-30  
**Classification:** INTERNAL–EVIDENCE-REQUIRED

## Introduction

ARINC 429 is a two-wire data bus standard widely used in commercial and military aircraft to transmit digital data between avionics systems. The BWB-Q100 IMA system implements ARINC 429 for critical avionics communication.

## Key Characteristics

### Physical Layer
- **Medium:** Twisted shielded pair
- **Encoding:** Bi-phase Mark (self-clocking)
- **Voltage Levels:**
  - High: +5V to +10V (differential)
  - Low: -5V to -10V (differential)
  - Null: 0V ±0.5V

### Data Rate
- **Low Speed:** 12.5 kbps (±1%)
- **High Speed:** 100 kbps (±1%)

### Word Format
- **Word Length:** 32 bits
- **Structure:**
  - Bits 1-8: Label (octal notation)
  - Bits 9-10: Source/Destination Identifier (SDI)
  - Bits 11-29: Data field
  - Bits 30-31: Sign/Status Matrix (SSM)
  - Bit 32: Parity (odd)

## Protocol Features

### Unidirectional Communication
- One transmitter per wire pair
- Multiple receivers (up to 20)
- No acknowledgment or handshaking

### Data Integrity
- Odd parity bit for error detection
- Self-clocking eliminates need for separate clock
- Predictable timing for critical systems

### Label System
- 256 possible labels (000-377 octal)
- Labels identify data type and parameter
- Standard labels defined by ARINC 429 specification
- Custom labels for specific applications

## BWB-Q100 Implementation

### Applications
- Flight control data
- Navigation information
- Air data parameters
- Engine monitoring
- System status

### Integration Points
- **Sensors → Flight Control:** Angle of Attack, airspeed
- **Navigation → Displays:** Position, altitude, heading
- **Engine Control → Monitoring:** N1/N2 speeds, temperatures
- **Flight Control → Actuators:** Control surface commands

## Advantages

1. **Proven Technology:** Decades of reliable operation
2. **Simplicity:** Easy to implement and maintain
3. **Deterministic:** Predictable timing behavior
4. **Robustness:** Self-clocking and error detection
5. **Industry Standard:** Wide component availability

## Limitations

1. **Bandwidth:** Limited compared to modern protocols
2. **Unidirectional:** Requires separate channels for bidirectional communication
3. **Cable Count:** One wire pair per transmitter

## References

- ARINC Specification 429, Mark 33 Digital Information Transfer System (DITS)
- [Architecture Specification](./architecture_spec.md)
- [Implementation Guide](./implementation_guide.md)
