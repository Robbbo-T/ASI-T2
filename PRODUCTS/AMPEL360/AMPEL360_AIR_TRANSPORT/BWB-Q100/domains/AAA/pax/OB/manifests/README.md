---
id: AAA-PAX-OB-MANIFESTS-OV-0001
project: AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/OB/manifests/README.md
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

# OB Manifests - Packaging

This directory contains OB (On-Board) manifests for BWB-Q100 AAA domain packaging and containerization.

## Purpose

Manages Open Build packaging manifests including:

- Container image definitions and build specifications
- Dependency management and version control
- Deployment configurations and runtime specifications
- Environment-specific packaging parameters

## Manifest Contents

- **Build manifests** - Container build instructions and dependency specifications
- **Runtime manifests** - Deployment and execution environment configurations
- **Version manifests** - Component version tracking and compatibility matrices
- **Configuration manifests** - Environment-specific parameter definitions

### Example Manifests

- **`partition.example.yaml`** - UTCS-MI v5.0 compliant partition manifest example
  - Demonstrates required UTCS fields: `canonical_hash`, `sbom_hash`, `security_policy_id`
  - Includes evidence section with canonical hash and SBOM hash references
  - Shows proper SHA256 hash format (`sha256:[a-f0-9]{64}`)
  - Reference implementation for on-board ARINC-653 partition packaging

## Integration

OB manifests support:

- Automated build and deployment pipelines for AAA domain tools and models
- Container orchestration and microservice deployment
- Development environment provisioning and consistency
- Quality assurance and testing environment replication