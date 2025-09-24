#!/usr/bin/env python3
import os
from pathlib import Path

def create_readme(path, title, description):
    """Create a README.md file with standard structure"""
    
    # Generate ID from path
    parts = path.strip('/').split('/')
    id_parts = ['ASIT2', 'INFRANET', 'METAOS'] + [p.upper().replace('-', '').replace('_', '') for p in parts]
    file_id = '-'.join(id_parts)
    
    content = f'''---
id: {file_id}
project: ASI-T2
artifact: {title}
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-24
maintainer: OOO (OS), IIS (Integration)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# {title}

{description}

## Overview

This component is part of the Meta-OS Aerospace/Defense system, providing specialized functionality for aerospace applications with safety-critical requirements.

## Integration

Integrates with other Meta-OS components through standardized interfaces and follows DO-178C/DO-326A compliance requirements.

## Development

See the main Meta-OS documentation for development guidelines and integration patterns.

---

*Part of INFRANET Meta-OS Aerospace Extension under ASI-T2 portfolio*'''

    readme_path = Path(path) / "README.md"
    readme_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Created {readme_path}")

# Define directories and their descriptions
directories = {
    "certification": ("Certification Framework", "Safety and security certification artifacts for aerospace systems including DO-178C, DO-326A, and ISO-26262 compliance."),
    "certification/do-178c": ("DO-178C Compliance", "Software considerations in airborne systems and equipment certification artifacts and documentation."),
    "certification/do-326a": ("DO-326A Security", "Airworthiness security process specification compliance artifacts for secure aerospace systems."),
    "certification/iso-26262": ("ISO-26262 Functional Safety", "Functional safety standards for automotive-related aerospace applications and urban air mobility."),
    "digital-thread": ("Digital Thread Integration", "End-to-end digital thread connecting design, development, testing, and operations with full lifecycle traceability."),
    "digital-thread/connectors": ("Digital Thread Connectors", "Integration connectors for PLM, MBSE, ALM, and other lifecycle management systems."),
    "digital-thread/twin": ("Digital Twin Services", "Real-time digital twin implementation with state estimation, simulation, and predictive analytics."),
    "docs": ("Documentation", "Comprehensive documentation including architecture decisions, runbooks, and operational procedures."),
    "docs/architecture": ("Architecture Documentation", "Architectural Decision Records (ADRs), system diagrams, and technical specifications."),
    "docs/runbooks": ("Operational Runbooks", "Operational procedures, incident response, and maintenance documentation for Meta-OS systems."),
    "examples": ("Example Implementations", "Complete example implementations and demonstrations of Meta-OS capabilities."),
    "kernels": ("Kernel Abstraction Layer", "Multi-kernel support including RTOS, Linux, and hypervisor configurations for heterogeneous platforms."),
    "kernels/hypervisor": ("Hypervisor Support", "Hypervisor configurations for ARINC-653 partitioning using Jailhouse, Xen, and similar technologies."),
    "kernels/linux": ("Linux Support", "Hardened Linux configurations with PREEMPT_RT, LSM/SELinux, and real-time capabilities."),
    "kernels/rtos": ("RTOS Support", "Real-time operating system support including seL4, VxWorks, RTEMS with safety certifications."),
    "middleware/dds": ("DDS Middleware", "Data Distribution Service implementation with deterministic QoS policies for real-time aerospace applications."),
    "middleware/gateways": ("Protocol Gateways", "Protocol translation gateways bridging aerospace standards with modern communication protocols."),
    "middleware/gateways/arinc1553": ("ARINC-1553 Gateway", "ARINC-1553 to modern protocol gateway for legacy avionics system integration."),
    "middleware/gateways/can": ("CAN Gateway", "Controller Area Network gateway for vehicle system integration and automotive aerospace applications."),
    "middleware/gateways/radio": ("Radio Gateway", "Radio communication gateway supporting various RF protocols and software-defined radio integration."),
    "middleware/gateways/spacewire": ("SpaceWire Gateway", "SpaceWire protocol gateway for spacecraft onboard data handling and satellite communication."),
    "middleware/ros2": ("ROS2 Integration", "Robot Operating System 2 integration for robotics and autonomous system interoperability."),
    "middleware/ros2/launch": ("ROS2 Launch Configuration", "ROS2 launch file configurations for Meta-OS component integration and system startup."),
    "observability": ("Observability Framework", "Comprehensive monitoring, logging, and telemetry collection for aerospace system health monitoring."),
    "observability/logging": ("Logging Services", "Secure logging services with cryptographic integrity and audit trail capabilities."),
    "observability/telemetry": ("Telemetry Management", "Real-time telemetry collection, processing, and distribution with time synchronization."),
    "observability/telemetry/schemas": ("Telemetry Schemas", "Protocol buffer and schema definitions for standardized telemetry data formats."),
    "orchestrator/control-plane": ("Control Plane", "Centralized orchestration control plane with scheduling, placement, and resource management."),
    "orchestrator/edge-agents": ("Edge Agents", "Distributed edge agents running on assets for local orchestration and telemetry collection."),
    "orchestrator/manifests": ("Mission Manifests", "Mission definition manifests and deployment descriptors for aerospace operations."),
    "orchestrator/manifests/mission": ("Mission Definitions", "Specific mission definition files with asset requirements and operational parameters."),
    "platforms/ground": ("Ground Platform Support", "Ground station and mission control platform support with high availability configurations."),
    "platforms/satellite": ("Satellite Platform Support", "Satellite platform support with space-qualified systems and radiation-hardened configurations."),
    "qox": ("Quantum Optimization Layer", "Quantum optimization integration for mission planning, route optimization, and resource allocation."),
    "qox/optimizers": ("Quantum Optimizers", "QAOA and quantum annealing implementations for aerospace optimization problems."),
    "qox/simulators": ("Quantum Simulators", "Quantum processing unit simulators and local quantum algorithm testing frameworks."),
    "qox/simulators/qpu_stub": ("QPU Stub Interface", "Quantum processing unit stub interfaces for quantum algorithm development and testing."),
    "security/attestation": ("Attestation Framework", "Hardware and software attestation using TPM/TEE for system integrity verification."),
    "security/fdir": ("FDIR System", "Fault Detection, Isolation, and Recovery system with automated response capabilities."),
    "security/fdir/rules": ("FDIR Rules", "Fault detection and recovery rule definitions with automated response procedures."),
    "security/ota": ("OTA Update System", "Over-the-air update system with cryptographic signing and secure distribution."),
    "security/ota/update-manifests": ("OTA Manifests", "Over-the-air update manifests with cryptographic signatures and rollback protection."),
    "security/pki": ("PKI Infrastructure", "Public Key Infrastructure for certificate management and cryptographic operations."),
    "security/policies": ("Security Policies", "Security policy definitions using OPA/Rego for access control and authorization."),
    "tooling": ("Development Tools", "Complete toolset for Meta-OS development, testing, and deployment operations."),
    "tooling/cli": ("Command Line Tools", "Command-line interface tools for Meta-OS management, deployment, and diagnostics."),
}

# Create README files
for path, (title, description) in directories.items():
    create_readme(path, title, description)

print(f"Created {len(directories)} README files")
