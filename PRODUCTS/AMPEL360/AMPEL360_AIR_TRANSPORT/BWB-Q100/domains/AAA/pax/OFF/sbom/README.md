---
id: AAA-PAX-OFF-SBOM-OV-0001
project: AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/OFF/sbom/README.md
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: "2025-01-23"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
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