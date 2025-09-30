# Descriptive Documentation

This directory contains high-level descriptive documentation for the AQUA-OS operating system.

## Documents

| Document | Description | File |
|----------|-------------|------|
| OS Overview | System capabilities and architecture summary | [os_overview.md](./os_overview.md) |
| Architecture Spec | Detailed technical architecture | [architecture_spec.md](./architecture_spec.md) |
| Security Model | Security architecture and controls | [security_model.md](./security_model.md) |

## OS Overview

Provides a high-level overview including:

- System capabilities (partitioning, real-time, safety, security)
- Architecture summary with diagrams
- Partition overview
- Standards compliance
- Performance characteristics

## Architecture Specification

Details the technical architecture:

- Microkernel and separation kernel design
- Memory architecture and protection
- Scheduling architecture (cyclic, deterministic)
- Communication architecture (sampling/queuing ports)
- I/O architecture
- Health monitoring architecture

## Security Model

Comprehensive security documentation:

- Quantum-ready cryptography (Kyber, Dilithium)
- Secure boot chain
- Access control models (MLS, RBAC, MAC)
- Key management
- Security monitoring and intrusion detection

## Related Documents

- [S1000D Publications](../S1000D/publications/)
- [Configuration](../configuration/)
- [Compliance Evidence](../compliance/)
- [Main README](../README.md)
