---
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/OFF/sbom/README.md
bridge: CB→QB→UE→FWD→QS
canonical_hash: TBD
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: AAA-PAX-OFF-SBOM-OV-0001
llc: SYSTEMS
maintainer: ASI-T Architecture Team
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100
release_date: '2025-01-23'
utcs_mi: v5.0
version: 0.1.0
---

# OFF SBOM - Packaging

This directory contains OFF (Off-Board) Software Bill of Materials (SBOM) for BWB-Q100 AAA domain containerized applications.

## Purpose

Manages container and cloud software inventory including:

- SPDX format SBOM files for OCI container images
- CycloneDX format SBOM files for cloud service dependencies
- Container base image and layer dependency tracking
- Cloud service and microservice component inventories

## SBOM Contents

- **Container SBOM** - SPDX/CycloneDX documents for OCI images and layers
- **Service SBOM** - Dependency inventories for cloud and edge services
- **Base image catalogs** - Container base image component tracking
- **Runtime dependencies** - Dynamic dependency discovery and tracking

## Cloud Integration

OFF SBOM supports:

- Automated container security scanning and vulnerability assessment
- Cloud service dependency analysis and risk evaluation
- Kubernetes/OCI registry integration for SBOM distribution
- Supply chain security for edge computing and ground services