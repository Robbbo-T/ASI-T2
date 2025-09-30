---
title: "AFDX vs Standard Ethernet Comparison"
document_id: REF-AFDX-ETH-COMP-001
version: 1.0
date: 2025-09-30
---

# AFDX vs Standard Ethernet Comparison

## Executive Summary
While AFDX is based on standard Ethernet technology, it includes significant enhancements to meet avionics requirements for determinism, reliability, and certification. This document compares AFDX with standard Ethernet to highlight the key differences.

## Fundamental Differences

### Determinism

#### Standard Ethernet
- **Best-effort delivery**: No bandwidth guarantees
- **Variable latency**: Depends on network load
- **Unpredictable jitter**: Can vary significantly
- **Collision domain**: CSMA/CD (legacy) or switched
- **Use case**: General-purpose networking

#### AFDX
- **Guaranteed bandwidth**: Per-VL allocation via BAG
- **Bounded latency**: Maximum latency defined per VL
- **Bounded jitter**: Typically ≤1% of BAG
- **No collisions**: Full-duplex switched only
- **Use case**: Safety-critical avionics

### Configuration

#### Standard Ethernet
- **Dynamic configuration**: DHCP, auto-discovery
- **Plug-and-play**: Automatic network configuration
- **Flexible**: Can add/remove devices easily
- **Learning switches**: MAC address learning
- **Management**: SNMP, web interfaces

#### AFDX
- **Static configuration**: All VLs pre-defined
- **Fixed topology**: No dynamic changes
- **Rigid**: Changes require reconfiguration
- **Configured switches**: No MAC learning
- **Management**: Custom tools only

### Redundancy

#### Standard Ethernet
- **Optional**: STP, RSTP, link aggregation
- **Variable recovery**: Seconds to minutes
- **Software-based**: Protocol-dependent
- **Single path**: Typically one active path
- **Failure detection**: Link state, keepalives

#### AFDX
- **Built-in**: Dual networks (A and B) standard
- **Fast recovery**: < 100 ms
- **Hardware-based**: Physical redundancy
- **Dual-active**: Both paths active simultaneously
- **Failure detection**: Continuous monitoring

## Detailed Technical Comparison

### Physical Layer

| Feature | Standard Ethernet | AFDX |
|---------|------------------|------|
| Media | Cat 5e/6/7, fiber | Cat 5e or better |
| Speed | 10/100/1000 Mbps+ | 100 Mbps only |
| Duplex | Half or full | Full-duplex only |
| Auto-negotiation | Enabled | Disabled |
| Distance | 100m (copper) | 100m (copper) |

### Data Link Layer

| Feature | Standard Ethernet | AFDX |
|---------|------------------|------|
| Frame format | IEEE 802.3 | IEEE 802.3 + ARINC 664 |
| Frame size | 64-1518 bytes | 64-1518 bytes |
| CRC | 32-bit | 32-bit |
| Sequence numbers | Optional | Mandatory |
| Addressing | MAC addresses | VL identifiers |
| VLANs | 802.1Q optional | Can be used |

### Network Layer

| Feature | Standard Ethernet | AFDX |
|---------|------------------|------|
| Protocol | IP (IPv4/IPv6) | IP (subset) |
| Routing | Dynamic routing | Static routing |
| Fragmentation | Supported | Not used |
| QoS | DiffServ, 802.1p | 8 priority levels |

### Transport Layer

| Feature | Standard Ethernet | AFDX |
|---------|------------------|------|
| Protocol | TCP, UDP, others | UDP only |
| Ports | Dynamic allocation | Static configuration |
| Flow control | TCP, pause frames | None (BAG control) |
| Reliability | TCP retransmission | Application level |

### Quality of Service

| Feature | Standard Ethernet | AFDX |
|---------|------------------|------|
| Priority levels | 0-7 (802.1p) | 0-7 (mandatory) |
| Scheduling | Various algorithms | Strict priority |
| Bandwidth control | Rate limiting | BAG enforcement |
| Traffic shaping | Software-based | Hardware-based |
| Enforcement | Switch-dependent | Mandatory at all ports |

### Reliability Features

| Feature | Standard Ethernet | AFDX |
|---------|------------------|------|
| Error detection | CRC | CRC + sequence |
| Error correction | Upper layers | Upper layers |
| Redundancy | Optional protocols | Built-in dual network |
| Failover | Seconds | < 100 ms |
| Health monitoring | SNMP, custom | Mandatory, continuous |

## Operational Comparison

### Network Design

#### Standard Ethernet
- **Flexibility**: Easy to modify, add devices
- **Scalability**: Easily scales to large networks
- **Complexity**: Can become complex with growth
- **Planning**: Less upfront planning required
- **Documentation**: Can be minimal

#### AFDX
- **Rigidity**: Changes require recertification
- **Scalability**: Limited by static configuration
- **Simplicity**: Well-defined, documented
- **Planning**: Extensive upfront planning required
- **Documentation**: Comprehensive, mandatory

### Installation

#### Standard Ethernet
- **Ease**: Generally straightforward
- **Tools**: Standard network tools
- **Testing**: Basic connectivity tests
- **Commissioning**: Quick
- **Training**: General IT knowledge

#### AFDX
- **Complexity**: Requires aviation expertise
- **Tools**: Specialized AFDX tools
- **Testing**: Comprehensive testing required
- **Commissioning**: Lengthy process
- **Training**: Specialized training required

### Maintenance

#### Standard Ethernet
- **Monitoring**: Standard SNMP, syslog
- **Troubleshooting**: Standard tools available
- **Spare parts**: Commercially available
- **Updates**: Regular firmware updates
- **Support**: Vendor support available

#### AFDX
- **Monitoring**: Specialized monitoring tools
- **Troubleshooting**: AFDX-specific tools
- **Spare parts**: Aviation-grade, certified
- **Updates**: Controlled, certified updates
- **Support**: Aviation-specific support

### Certification

#### Standard Ethernet
- **Requirements**: None for most applications
- **Testing**: Functional testing only
- **Documentation**: Minimal
- **Standards**: IEEE standards
- **Approval**: Not required

#### AFDX
- **Requirements**: DO-178C, DO-254, DO-160
- **Testing**: Extensive qualification testing
- **Documentation**: Comprehensive evidence
- **Standards**: ARINC 664 + DO-xxx
- **Approval**: FAA/EASA certification required

## Performance Comparison

### Throughput

| Metric | Standard Ethernet | AFDX |
|--------|------------------|------|
| Theoretical max | 100 Mbps | 100 Mbps |
| Typical utilization | 60-80% | 20-50% |
| Maximum recommended | 80-90% | 75% |
| Burst capability | High | Limited by BAG |

### Latency

| Metric | Standard Ethernet | AFDX |
|--------|------------------|------|
| Typical latency | 1-10 ms | 0.1-1 ms |
| Worst-case latency | Unbounded | Bounded |
| Jitter | Variable, high | Bounded, low |
| Consistency | Low | High |

### Reliability

| Metric | Standard Ethernet | AFDX |
|--------|------------------|------|
| Frame loss | Variable | Near zero |
| Error rate | 10^-9 typical | 10^-12 required |
| Availability | 99.9% typical | 99.999%+ required |
| MTBF | Hours-years | Years-decades |

## Cost Comparison

### Initial Costs

| Component | Standard Ethernet | AFDX |
|-----------|------------------|------|
| Hardware | Low | High |
| Software | Low | High |
| Tools | Low | High |
| Design | Low | High |
| Integration | Low | High |

### Lifecycle Costs

| Component | Standard Ethernet | AFDX |
|-----------|------------------|------|
| Maintenance | Low | Moderate |
| Upgrades | Easy, low cost | Complex, high cost |
| Certification | N/A | High |
| Training | Low | High |
| Support | Readily available | Specialized |

## Use Case Suitability

### Standard Ethernet Best For:
- General-purpose networking
- Office and enterprise networks
- Non-critical applications
- Flexible, changing environments
- Cost-sensitive applications
- High-bandwidth requirements

### AFDX Best For:
- Safety-critical avionics
- Flight control systems
- Mission-critical communications
- Deterministic requirements
- Certification requirements
- High-reliability requirements

## Migration Considerations

### From Standard Ethernet to AFDX
**Challenges:**
- Complete redesign required
- Static configuration vs. dynamic
- Specialized hardware needed
- Certification effort
- Training requirements

**Benefits:**
- Deterministic behavior
- Built-in redundancy
- Certification credit
- High reliability
- Industry standard for avionics

### From AFDX to Standard Ethernet
**Challenges:**
- Loss of determinism guarantees
- Loss of built-in redundancy
- Loss of certification credit
- Need to implement redundancy
- Performance variability

**Benefits:**
- Lower hardware costs
- Greater flexibility
- Standard tools and support
- Easier maintenance
- Higher bandwidth options

## Conclusion

AFDX and Standard Ethernet serve different purposes:

**Standard Ethernet** is excellent for general-purpose networking where flexibility, ease of use, and cost are primary concerns.

**AFDX** is specifically designed for avionics applications where determinism, reliability, and certification are mandatory requirements.

The choice between them should be based on:
1. Safety criticality of the application
2. Determinism requirements
3. Certification requirements
4. Budget constraints
5. Operational environment

For safety-critical avionics applications like the BWB-Q100, AFDX is the appropriate choice despite higher costs and complexity.

## References
- IEEE 802.3: Ethernet Standard
- ARINC 664 Part 7: Avionics Full-Duplex Switched Ethernet
- DO-178C: Software Considerations in Airborne Systems
- [ARINC 664 Specification Summary](./ARINC664_spec.md)
- [AFDX Implementation Guide](./AFDX_implementation_guide.md)
