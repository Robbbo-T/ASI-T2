# AFDX Reference Documentation

This directory contains reference documentation including standards summaries, implementation guides, and comparative analyses.

## Purpose

Provides reference materials that support the understanding and implementation of AFDX systems. These documents explain standards, best practices, and provide context for design decisions.

## Contents

| Document | Description |
|----------|-------------|
| `ARINC664_spec.md` | ARINC 664 Part 7 specification summary |
| `AFDX_implementation_guide.md` | Comprehensive implementation guide |
| `ethernet_comparison.md` | Detailed comparison: AFDX vs standard Ethernet |

## Document Summaries

### ARINC 664 Specification Summary
Covers the key aspects of ARINC 664 Part 7:
- Network architecture and characteristics
- Virtual Links definition and configuration
- Bandwidth Allocation Gap (BAG) enforcement
- Frame format and Quality of Service
- Redundancy management
- Configuration management requirements
- Testing and validation procedures

### Implementation Guide
Comprehensive guide covering the full lifecycle:
- **Planning Phase**: Requirements analysis, network sizing, redundancy planning
- **Configuration Phase**: VL configuration, switch setup, traffic policing
- **Integration Phase**: Hardware/software integration, cabling, testing
- **Verification Phase**: Functional testing, performance testing, redundancy testing
- **Certification Phase**: Documentation, compliance evidence, authority coordination
- **Maintenance Phase**: Health monitoring, troubleshooting, best practices

### Ethernet Comparison
Detailed comparison across multiple dimensions:
- Fundamental differences (determinism, configuration, redundancy)
- Technical comparison (physical, data link, network, transport layers)
- Operational comparison (design, installation, maintenance)
- Performance comparison (throughput, latency, reliability)
- Cost comparison (initial and lifecycle costs)
- Use case suitability and migration considerations

## Standards Referenced

- **ARINC 664 Part 7**: Avionics Full-Duplex Switched Ethernet Network
- **ARINC 664 Part 2**: Network Configuration Data
- **DO-178C**: Software Considerations in Airborne Systems
- **DO-254**: Design Assurance Guidance for Airborne Electronic Hardware
- **DO-160**: Environmental Conditions and Test Procedures
- **IEEE 802.3**: Ethernet Standard

## Related Files

- Parent Documentation: [../README.md](../README.md)
- Descriptive Docs: [../descriptive/](../descriptive/)
- Configuration: [../configuration/](../configuration/)
- Compliance Evidence: [../compliance/](../compliance/)
