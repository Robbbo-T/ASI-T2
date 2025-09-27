# PAx Off-Board OCI Descriptors

This directory contains OCI (Open Container Initiative) image descriptors for off-board CAD processing, export, and validation tools deployed in ground systems, edge computing, and cloud environments.

## Purpose

Defines containerized CAD tools and services that run outside the vehicle in ground support equipment, manufacturing systems, design environments, and CI/CD pipelines for AMPEL360 PLUS development.

## File Types

- **`*.yaml`** - OCI image descriptors and deployment manifests
- Each descriptor specifies container images, resources, networking, and security policies

## Contents

### Current Descriptors

- **`cad-ci.exporter.yaml`** - CAD export CI pipeline container
  - Multi-format CAD export capability (STEP, IGES, X_T, STL)
  - Input format support (CATIA V5, NX Native, Fusion 360)
  - Validation tools (geometry checker, mass properties, naming validator)
  - Resource allocation (2 CPU, 4Gi memory, 10Gi storage)
  - API endpoints for export services and metrics

## Container Specifications

### Platform Support
- **OS**: Linux
- **Architecture**: amd64 (with optional arm64 variants)
- **Base Images**: Minimal distros with CAD libraries

### Resource Management
- **CPU**: Configurable allocation (0.5-4.0 cores typical)
- **Memory**: 2-16Gi depending on CAD model complexity
- **Storage**: Ephemeral + persistent volumes for CAD files
- **GPU**: Optional for visualization and compute-intensive operations

### Networking
- **API Ports**: HTTP/HTTPS endpoints for service interfaces
- **Metrics**: Prometheus-compatible monitoring endpoints
- **Security**: Non-privileged execution, read-only root filesystems

## CAD Tool Integration

### Supported CAD Systems
- **CATIA V5/V6**: Native model processing
- **Siemens NX**: Parasolid kernel integration
- **Fusion 360**: Cloud API and local processing
- **SolidWorks**: SOLIDWORKS API integration
- **Generic**: STEP/IGES universal format support

### Export Capabilities
- **STEP**: ISO 10303 standard (AP203, AP214, AP242)
- **IGES**: Initial Graphics Exchange Specification
- **X_T**: Parasolid native format
- **STL**: Stereolithography for rapid prototyping

### Validation Features
- **Geometry Checking**: Surface continuity, volume closure
- **Mass Properties**: Center of gravity, moments of inertia
- **Naming Validation**: PLUS naming convention enforcement
- **Schema Compliance**: CAD manifest validation

## Security & Evidence

All containers include:
- **SBOM**: CycloneDX/SPDX software bill of materials
- **Signatures**: Cosign + in-toto attestations (SLSA L3 intent)
- **Vulnerability Scanning**: Container image security scanning
- **UTCS Integration**: Canonical hash and provenance tracking

## Deployment Environments

### Ground Systems
- **Design Workstations**: CAD model processing and export
- **PLM Integration**: Product lifecycle management systems
- **Manufacturing Prep**: Tooling and fixture generation

### Cloud/Edge
- **CI/CD Pipelines**: Automated CAD validation and export
- **Batch Processing**: Large-scale geometry processing
- **API Services**: RESTful CAD export services

### Development
- **Local Testing**: Developer environment containers
- **Validation**: Pre-commit CAD model validation
- **Prototyping**: Rapid geometry iteration and testing

## Usage

Deploy containers using:
```bash
# Docker
docker run -v $(pwd):/workspace ghcr.io/ampel360/plus-cad-exporter:v1.2.0

# Kubernetes
kubectl apply -f cad-ci.exporter.yaml

# OCI registry
podman pull ghcr.io/ampel360/plus-cad-exporter:v1.2.0
```

## Integration

- **Input**: CAD models from geometry/ and structure/ directories
- **Output**: Validated exports to geometry/exports/ and structure/exports/
- **Evidence**: Quality assurance artifacts to ../../evidence/
- **Registry**: Container images in ghcr.io/ampel360/ namespace