---
title: "AFDX Implementation Guide"
document_id: REF-AFDX-IMPL-001
version: 1.0
date: 2025-09-30
---

# AFDX Implementation Guide

## Introduction
This guide provides practical guidance for implementing AFDX networks in avionics systems, based on ARINC 664 Part 7 and industry best practices.

## Planning Phase

### Requirements Analysis
1. **Identify Data Flows**
   - Map all data communications between systems
   - Identify source and destination end systems
   - Determine data rates and latency requirements
   - Classify criticality (DAL A, B, C, D, E)

2. **Network Sizing**
   - Calculate total bandwidth requirements
   - Determine number of Virtual Links needed
   - Plan for future growth (20-30% headroom)
   - Size switch capacity

3. **Redundancy Requirements**
   - Identify critical data paths
   - Determine redundancy needs (A, B, or A+B)
   - Plan network topology
   - Consider failure modes

### Design Considerations

#### Virtual Link Design
- **Unique Identifiers**: Assign VL IDs from agreed range
- **BAG Selection**: Choose smallest BAG that meets latency requirements
- **Frame Sizing**: Use appropriate frame size for data volume
- **Priority Assignment**: Assign based on criticality
- **Multicast**: Use for data needed by multiple destinations

#### Network Topology
- **Physical Layout**: Plan cable routing
- **Switch Placement**: Central equipment bay vs. distributed
- **Cable Categories**: Use Cat 5e or Cat 6
- **Connector Types**: RJ-45 standard
- **EMI Considerations**: Follow DO-160 guidance

## Configuration Phase

### Virtual Link Configuration

#### Configuration File Format
Use YAML or JSON for VL definitions:

```yaml
virtual_links:
  - vl_id: 1001
    name: "Flight_Control_Data"
    source: "FCC"
    destinations: ["Actuator_Control", "Display_System"]
    bag_ms: 2
    max_frame_size_bytes: 1518
    priority: 7
    redundancy: "A+B"
```

#### Configuration Validation
1. **Syntax Validation**: Check YAML/JSON syntax
2. **Schema Validation**: Validate against JSON schema
3. **Semantic Validation**: Check BAG values, frame sizes
4. **Bandwidth Validation**: Ensure total < 75% capacity

### Switch Configuration

#### Port Configuration
- **Speed**: 100 Mbps full-duplex
- **Auto-negotiation**: Disabled (fixed configuration)
- **Flow control**: Disabled for AFDX
- **VLANs**: Configure if used

#### QoS Configuration
- **Priority Queues**: Configure 8 levels (0-7)
- **Queue Sizes**: Size based on traffic patterns
- **Scheduling**: Strict priority
- **Buffer Allocation**: Adequate for BAG window

#### Traffic Policing
- **BAG Enforcement**: Hardware policing at each port
- **Bandwidth Limits**: Per-VL bandwidth allocation
- **Frame Size**: Validate 64-1518 bytes
- **Drop Policy**: Drop non-conforming frames

## Integration Phase

### End System Integration

#### Hardware Interface
- **PHY**: 100BASE-TX Ethernet PHY
- **MAC**: Standard Ethernet MAC
- **Buffers**: Size for worst-case BAG
- **DMA**: For efficient data transfer

#### Software Driver
- **VL Management**: Track VL state
- **Sequence Numbers**: Generate and validate
- **Redundancy Management**: Handle A/B networks
- **Error Handling**: Detect and report errors

#### Application Interface
- **API Design**: Simple send/receive interface
- **Data Formatting**: Handle frame format
- **Timing**: Meet BAG requirements
- **Error Reporting**: Provide status to application

### Network Integration

#### Cabling
- **Installation**: Follow aircraft wiring standards
- **Separation**: Adequate separation from power cables
- **Shielding**: Use shielded cables if required
- **Connectors**: Secure, vibration-resistant

#### Switch Installation
- **Mounting**: Secure mounting in equipment bay
- **Cooling**: Ensure adequate ventilation
- **Power**: Redundant power sources
- **Access**: Accessible for maintenance

#### Testing
- **Continuity**: Test all cables
- **Connectivity**: Verify all links
- **Configuration**: Load and verify configuration
- **Functional**: Test data transfer

## Verification Phase

### Functional Testing

#### VL Establishment
- Verify all VLs establish correctly
- Check source and destination connectivity
- Validate multicast distribution
- Verify VL ID uniqueness

#### Data Transfer
- Send test data on each VL
- Verify correct reception
- Check frame integrity (CRC)
- Validate sequence numbers

#### Priority Handling
- Generate traffic at different priorities
- Verify higher priority served first
- Check for starvation of lower priority
- Measure queuing delays

### Performance Testing

#### Bandwidth Measurement
- Measure bandwidth per VL
- Verify BAG enforcement
- Check total network utilization
- Validate bandwidth allocation

#### Latency Testing
- Measure end-to-end latency
- Verify meets requirements
- Check worst-case latency
- Identify bottlenecks

#### Jitter Analysis
- Measure jitter per VL
- Verify within specification
- Identify sources of jitter
- Optimize if necessary

### Redundancy Testing

#### Normal Operation
- Verify both networks operational
- Check frame distribution
- Validate duplicate elimination
- Monitor network health

#### Failover Testing
- Disconnect Network A
- Verify automatic failover to B
- Measure failover time
- Check data continuity

#### Recovery Testing
- Restore Network A
- Verify automatic resynchronization
- Check for duplicate frames
- Validate steady-state operation

## Certification Phase

### Documentation

#### Design Documentation
- Network architecture diagrams
- VL configuration tables
- Switch configuration files
- Cable routing diagrams

#### Test Reports
- Functional test results
- Performance test results
- Redundancy test results
- Stress test results

#### Compliance Evidence
- ARINC 664 compliance matrix
- DO-178C evidence (if software)
- DO-254 evidence (if hardware)
- DO-160 environmental test results

### Certification Activities

#### Authority Coordination
- Submit certification plan
- Provide technical documentation
- Schedule reviews and audits
- Address findings

#### Verification Reviews
- Design review
- Implementation review
- Test review
- Certification review

## Maintenance Phase

### Health Monitoring

#### Real-time Monitoring
- Link status (up/down)
- Frame counters (tx/rx)
- Error counters (CRC, sequence)
- Bandwidth utilization

#### Periodic Checks
- Configuration validation
- Performance baseline comparison
- Cable integrity testing
- Switch health verification

### Troubleshooting

#### Common Issues
1. **Link Down**: Check cables, connectors, PHY
2. **High Latency**: Check bandwidth utilization, priority
3. **Frame Loss**: Check BAG compliance, switch buffers
4. **CRC Errors**: Check cable quality, EMI

#### Diagnostic Tools
- Network analyzer (e.g., Wireshark)
- AFDX analyzer (specialized tool)
- Switch management interface
- End system diagnostics

## Best Practices

### Design
- Start with clear requirements
- Plan for 20-30% growth
- Use standard BAG values
- Document all decisions

### Configuration
- Use version control for configs
- Validate before deployment
- Test in lab environment
- Document all changes

### Testing
- Test early and often
- Use systematic approach
- Document all results
- Address all issues before certification

### Operations
- Monitor continuously
- Maintain spare parts
- Keep configuration backups
- Train maintenance personnel

## Common Pitfalls

### Design Issues
- **Insufficient Bandwidth**: Not planning for growth
- **Poor VL Design**: Too many small VLs
- **Inadequate Redundancy**: Critical paths not redundant

### Configuration Issues
- **Invalid BAG**: Non-standard BAG values
- **Bandwidth Overrun**: Total > capacity
- **Priority Mismatch**: Critical data low priority

### Integration Issues
- **Cable Quality**: Poor quality cables
- **EMI Problems**: Inadequate shielding
- **Configuration Errors**: Mismatched configs

## References
- ARINC 664 Part 7: Avionics Full-Duplex Switched Ethernet Network
- ARINC 664 Part 2: Network Configuration Data
- DO-178C: Software Considerations in Airborne Systems
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware
- DO-160: Environmental Conditions and Test Procedures

## Related Documentation
- [ARINC 664 Specification Summary](./ARINC664_spec.md)
- [AFDX Overview](../descriptive/afdx_overview.md)
- [Virtual Links Configuration](../configuration/virtual_links.yaml)
