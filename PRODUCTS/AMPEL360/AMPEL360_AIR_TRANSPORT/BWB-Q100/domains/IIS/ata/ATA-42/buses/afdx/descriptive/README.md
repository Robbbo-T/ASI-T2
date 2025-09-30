# AFDX Descriptive Documentation

This directory contains descriptive documentation for the AFDX bus implementation in Markdown format.

## Purpose

Provides comprehensive technical descriptions of the AFDX system architecture, design, and implementation. These documents explain the "what" and "why" of the AFDX implementation.

## Contents

| Document | Description |
|----------|-------------|
| `afdx_overview.md` | High-level overview of AFDX system features and capabilities |
| `architecture_spec.md` | Detailed architecture specification with network topology and performance budgets |

## Document Structure

### AFDX Overview
Covers fundamental concepts:
- Deterministic behavior and guaranteed bandwidth
- Dual-active redundancy
- Quality of Service (QoS) with 8 priority levels
- Virtual Links definition and configuration
- Bandwidth Allocation Gap (BAG) enforcement
- Reliability features and error detection
- Benefits for BWB-Q100 aircraft

### Architecture Specification
Provides detailed technical information:
- Network topology (dual networks A and B)
- End system descriptions (FCC, Navigation, Air Data, etc.)
- Virtual Links specifications (6 VLs with full parameters)
- Switch architecture (4 switches in dual-redundant topology)
- Bandwidth allocation and utilization
- Redundancy management (dual-active operation, failover, recovery)
- Quality of Service implementation
- Performance characteristics (latency, jitter, reliability)

## Technical Highlights

### Network Architecture
- **Topology**: Dual-redundant networks (A and B)
- **Switches**: 4 switches (2 per network)
- **Speed**: 100 Mbps per link
- **Utilization**: 18.02% (excellent headroom)

### Performance
- **Max Latency**: 150 µs end-to-end (critical VLs)
- **Jitter**: < 1% of BAG (all VLs)
- **Frame Loss**: 0% in normal operation
- **Availability**: > 99.999%

## Related Files

- Parent Documentation: [../README.md](../README.md)
- Configuration: [../configuration/](../configuration/)
- Reference Documents: [../references/](../references/)
- Test Results: [../testing/test_results/](../testing/test_results/)
