---
artifact: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: pending
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: ASIT2-AQUAOS-AIR-NETSTACK-SRD
llc: SYSTEMS
maintainer: EDI (Avionics/Net), OOO (OS)
project: PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/components
release_date: 2024-09-23
utcs_mi: 'component: NET_STACK Deterministic Network (AQUA OS — Aircraft Extension)

  level: DO-178C DAL-A; AFDX/TSN/TTE protocols

  bridges: CB→QB→UE→FE→FWD→QS

  status: BASELINED

  '
version: 1.0
---

# NET_STACK System Requirements (MoSCoW)

## MUST

- NETSTACK-SRD-001 Protocol Support: Implement AFDX, TSN, and TTE deterministic networking protocols with guaranteed latency bounds.
- NETSTACK-SRD-002 Dual Redundancy: Provide seamless failover between NET-A and NET-B with ≤3 lost frames during transition.
- NETSTACK-SRD-003 VL Management: Support Virtual Link (VL) creation, bandwidth allocation, and QoS enforcement per configuration.
- NETSTACK-SRD-004 MTU Support: Handle frame sizes up to 1518 bytes with proper fragmentation/reassembly if needed.
- NETSTACK-SRD-005 Traffic Policing: Enforce rate limiting, burst control, and priority scheduling per VL configuration.
- NETSTACK-SRD-006 Authentication: Provide GMAC-128 message authentication for safety-critical topics using KMS keys.
- NETSTACK-SRD-007 Latency Guarantee: Achieve deterministic forwarding latency ≤100μs per network hop.
- NETSTACK-SRD-008 Health Monitoring: Monitor link status, collect traffic statistics, report network faults.
- NETSTACK-SRD-009 Time Synchronization: Integrate with TIME_SYNC for PTP/TTE timebase coordination.
- NETSTACK-SRD-010 Evidence Sealing: All network configurations and fault events sealed via UTCS/QS.

## SHOULD

- NETSTACK-SRD-011 Performance: Optimize packet processing for minimum CPU overhead and maximum throughput.
- NETSTACK-SRD-012 Diagnostics: Provide detailed network statistics, VL utilization, and performance metrics.

## COULD

- NETSTACK-SRD-013 Adaptive QoS: Dynamically adjust QoS parameters based on network conditions (ground-only).

## WON'T (baseline)

- NETSTACK-SRD-014 No dynamic VL reconfiguration during flight operations.
- NETSTACK-SRD-015 No packet-level encryption (authentication via MAC only).

## Resource Baseline

- CPU: ≤8% of a core for network processing and VL management
- Memory: ≤16 MiB for buffers, VL tables, and statistics
- Network: Support for 2 redundant Gigabit Ethernet interfaces

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*