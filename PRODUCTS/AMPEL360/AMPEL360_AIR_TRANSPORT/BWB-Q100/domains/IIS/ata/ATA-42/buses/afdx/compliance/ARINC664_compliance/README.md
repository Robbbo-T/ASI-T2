# ARINC 664 Compliance Evidence

This directory contains evidence demonstrating compliance with ARINC 664 Part 7 (AFDX) specification requirements.

## Purpose

Provides comprehensive documentation that the AFDX implementation meets all ARINC 664 Part 7 requirements for:
- Virtual Link configuration and operation
- Bandwidth Allocation Gap (BAG) enforcement
- Dual-active redundancy
- Quality of Service (QoS) and priority handling
- Frame format and integrity
- Network performance and determinism

## Contents

| Document | Description |
|----------|-------------|
| `arinc664_compliance_report.md` | Comprehensive ARINC 664 Part 7 compliance report |

## Compliance Coverage

The compliance report demonstrates:

### Virtual Links (VL-001 through VL-004)
- ✅ Unique VL identifiers assigned
- ✅ BAG values from standard set {1,2,4,8,16,32,64,128} ms
- ✅ Frame sizes within 64-1518 byte limits
- ✅ Priority handling per specification

### Redundancy (RED-001 through RED-003)
- ✅ Dual-active networks (A and B)
- ✅ Integrity checking (CRC + sequence numbers)
- ✅ Failover < 100 ms

### Network Operation (NET-001, NET-002)
- ✅ 100 Mbps full-duplex operation
- ✅ Store-and-forward switching

### Quality of Service (QOS-001, QOS-002)
- ✅ 8-level priority queuing
- ✅ Bandwidth allocation per VL

## Test Evidence

Compliance is supported by test results in:
- [../../testing/test_results/](../../testing/test_results/)

## Related Standards

- **ARINC 664 Part 7**: Avionics Full-Duplex Switched Ethernet
- **ARINC 664 Part 2**: Network Configuration Data
- **DO-178C**: Software considerations (see [../DO-178C_evidence/](../DO-178C_evidence/))

## Related Files

- Parent Documentation: [../../README.md](../../README.md)
- Test Results: [../../testing/test_results/](../../testing/test_results/)
- Configuration: [../../configuration/](../../configuration/)
