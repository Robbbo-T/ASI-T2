# ARINC 429 Specification Summary

**Document ID:** REF-A429-SPEC-001  
**Version:** Based on ARINC 429 Mark 33  
**Date:** 2025-09-30  
**Classification:** INTERNAL–REFERENCE

## Overview

ARINC 429, "Mark 33 Digital Information Transfer System (DITS)," is the most commonly used data bus standard for commercial and transport aircraft. Published by Aeronautical Radio, Incorporated (ARINC), it defines a two-wire data bus for transmitting digital information between avionics systems.

## Physical Layer

### Transmission Medium
- **Type**: Twisted shielded pair (TSP)
- **Impedance**: 75 Ω ±5%
- **Shielding**: Connected to ground at receiver only
- **Maximum Cable Length**: 100 meters (typical)

### Electrical Characteristics
- **Encoding**: Bi-phase Mark (self-clocking)
- **Voltage Levels** (differential):
  - **High (1)**: +5V to +10V
  - **Low (0)**: -5V to -10V
  - **Null**: 0V ±0.5V
- **Rise/Fall Time**: ≤1.5 µs

### Data Rates
- **Low Speed**: 12.5 kbps (±1%)
- **High Speed**: 100 kbps (±1%)

## Data Link Layer

### Word Format
Each ARINC 429 word consists of 32 bits transmitted LSB first:

```
Bit 1-8:    Label (octal notation)
Bit 9-10:   Source/Destination Identifier (SDI)
Bit 11-29:  Data field (19 bits)
Bit 30-31:  Sign/Status Matrix (SSM)
Bit 32:     Parity (odd)
```

### Label Field (Bits 1-8)
- Identifies the parameter type
- Expressed in octal (000 to 377)
- Transmitted LSB first (bit 8 first, bit 1 last)
- Examples:
  - 001₈: Heading
  - 010₈: Computed Airspeed
  - 020₈: Altitude

### SDI Field (Bits 9-10)
- Source/Destination Identifier
- Used when multiple sources provide same label
- Values: 00, 01, 10, 11
- Common use: Port/starboard differentiation

### Data Field (Bits 11-29)
Three primary encoding formats:

#### Binary (BNR)
- Straight binary or two's complement
- Used for analog values
- Resolution defined per label
- Example: Airspeed, Altitude

#### Binary Coded Decimal (BCD)
- Each 4-bit nibble represents 0-9
- Used for display-oriented data
- Example: Heading in degrees

#### Discrete
- Individual bits represent on/off states
- Used for switch positions, status flags
- Example: Autopilot engagement status

### SSM Field (Bits 30-31)
Sign/Status Matrix indicates data validity and sign:

For BNR data:
- 00: Failure Warning
- 01: No Computed Data
- 10: Functional Test
- 11: Normal Operation

For BCD data:
- Plus, Minus, North, South, East, West, etc.

### Parity Bit (Bit 32)
- Odd parity
- Covers all 32 bits of the word
- Provides error detection capability

## Timing

### Bit Timing
- **100 kbps**: 10 µs per bit ±1%
- **12.5 kbps**: 80 µs per bit ±1%

### Word Timing
- **Synchronization**: High for 4 bit times
- **Word Duration**: 32 bits + sync = 36 bit times
- **Inter-word Gap**: Minimum 4 bit times (null)

## Protocol Characteristics

### Unidirectional Transmission
- One transmitter per bus
- Up to 20 receivers
- No acknowledgment or handshaking
- Simplex communication

### Periodic Transmission
- Data transmitted cyclically
- Update rates depend on parameter type
- Critical data: High rate (e.g., 100 Hz)
- Non-critical data: Low rate (e.g., 1 Hz)

### Deterministic Behavior
- Predictable timing
- No collision detection needed
- Suitable for real-time systems

## Standard Labels

### Navigation Labels
- 001: Magnetic Heading
- 002: True Heading
- 010: Computed Airspeed
- 011: True Airspeed
- 012: Mach Number
- 013: Calibrated Airspeed

### Flight Data Labels
- 020: Pressure Altitude
- 021: Barometric Corrected Altitude
- 030: Vertical Speed
- 031: Inertial Vertical Speed

### Position Labels
- 110-111: Latitude
- 112-113: Longitude
- 114: Track Angle (True)
- 115: Track Angle (Magnetic)

### Engine Labels
- 210-217: Engine N1 (various engines)
- 220-227: Engine N2
- 240-247: Engine EGT

### Flight Control Labels
- 250-257: Control Surface Positions
- 270-277: Autopilot Modes and Status

## Error Detection

### Parity Checking
- Odd parity bit provides single-bit error detection
- Receiver discards words with parity errors

### Synchronization Checking
- Invalid sync pattern indicates transmission error
- Word discarded if sync is invalid

### Timing Monitoring
- Receivers monitor for expected update rates
- Data flagged stale if not updated within timeout

## Advantages

1. **Proven Reliability**: Decades of operational history
2. **Simplicity**: Easy to implement and maintain
3. **Self-Clocking**: No separate clock signal required
4. **Deterministic**: Predictable timing behavior
5. **Wide Adoption**: Extensive component availability
6. **Well-Defined Standard**: Clear specification

## Limitations

1. **Low Bandwidth**: 100 kbps maximum
2. **Unidirectional**: Separate bus for each transmitter
3. **No Acknowledgment**: No confirmation of reception
4. **Limited Error Detection**: Parity only detects single-bit errors
5. **Cable Count**: One twisted pair per transmitter

## Comparison with Modern Standards

| Feature | ARINC 429 | ARINC 664 (AFDX) | MIL-STD-1553 |
|---------|-----------|------------------|--------------|
| Topology | Point-to-multipoint | Switched network | Bus |
| Max Speed | 100 kbps | 100 Mbps | 1 Mbps |
| Direction | Unidirectional | Bidirectional | Bidirectional |
| Max Nodes | 20 receivers | 1000+ | 31 terminals |
| Determinism | High | High | High |
| Complexity | Low | High | Medium |

## Applications

### Commercial Aviation
- Flight management systems
- Navigation systems
- Flight control systems
- Engine monitoring
- Display systems

### Military Aviation
- Mission systems integration
- Weapon systems interfaces
- Tactical data links

### General Aviation
- Glass cockpit displays
- Autopilot systems
- Engine monitoring

## Implementation Considerations

### Hardware
- Dedicated ARINC 429 interface chips available
- FPGA implementations common
- Discrete component implementations possible

### Software
- Driver complexity: Low to Medium
- Real-time requirements: Moderate
- CPU overhead: Low

### Testing
- Protocol analyzers widely available
- Test equipment well-established
- Simulation tools mature

## Regulatory Compliance

### Certification Standards
- DO-178C (Software)
- DO-254 (Hardware)
- DO-160 (Environmental)

### Safety Assessment
- ARP4754A (System development)
- ARP4761 (Safety assessment)

## Evolution and Future

While newer standards (ARINC 664/AFDX) offer higher bandwidth, ARINC 429 remains relevant:
- Legacy system support
- Simple, proven technology
- Cost-effective for lower bandwidth needs
- Expected to remain in use for decades

## References

### Standards Documents
- ARINC Specification 429, Part 1: Functional Description
- ARINC Specification 429, Part 2: Technical Description
- ARINC Specification 429, Part 3: File Structure

### Related Standards
- DO-178C: Software Considerations in Airborne Systems
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware
- DO-160G: Environmental Conditions and Test Procedures

### Industry Resources
- ARINC (Aeronautical Radio, Incorporated)
- SAE International (formerly Society of Automotive Engineers)
- RTCA (Radio Technical Commission for Aeronautics)

## Related Documents

- [A429 Implementation Guide](../descriptive/a429_overview.md)
- [Architecture Specification](../descriptive/architecture_spec.md)
- [Bus Standards Comparison](./bus_standards_comparison.md)
