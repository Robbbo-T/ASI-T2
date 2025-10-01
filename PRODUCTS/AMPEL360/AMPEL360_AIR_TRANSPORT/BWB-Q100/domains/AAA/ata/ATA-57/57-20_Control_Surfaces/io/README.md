# IO - Input/Output Routing

This directory contains UTCS/QS routing manifests and input/output definitions for ATA-57-20 Control Surfaces.

## Purpose

The IO directory provides:
- UTCS/QS integration manifest
- Input/output path definitions
- Provenance and traceability
- SBOM references
- Quality sealing anchors

## Contents

### routing.manifest.yaml
Master routing manifest defining:
- **Source**: Repository path and commit hash
- **Inputs**: CAX/QOX artifact references
  - CAD models (geometry, OML definitions)
  - FEA analysis (structural loads, margins)
  - CFD analysis (aerodynamic loads)
  - QOX optimization (hinge layout, QUBO/BQM runs)
- **Outputs**: Generated artifacts
  - S1000D data modules
  - Compliance reports
  - ICDs
  - JSON schemas
- **Evidence**: Test and measurement indexes
- **Provenance**: SBOM, signatures, QS anchors

## UTCS/QS Integration

The routing manifest enables:
- **Universal Trusted Configuration System (UTCS)**: Version 5.0 integration
- **Quality Sealing (QS)**: Cryptographic sealing of artifacts
- **Bridge**: CB→QB→UE→FE→FWD→QS pipeline
- **Ethics Guard**: MAL-EEM compliance

## Input References

Inputs are referenced, not stored:
```yaml
inputs:
  - path: ../../../cax/CAD/ControlSurfaces_v*/
    description: Model geometry, OML definitions
  - path: ../../../cax/FEA/ControlSurfaceLoads_v*/
    description: Structural loads, stress margins
```

## Output Tracking

Outputs are tracked for:
- Configuration baseline status
- Version control
- Change management
- Quality gates
- Release readiness

## Provenance

Provenance tracking includes:
- **SBOM**: Software Bill of Materials (SPDX format)
- **Signatures**: Digital signatures for QS
- **Anchors**: SHA256 hashes for integrity
- **Timestamps**: Creation and modification times

## Usage

### Updating Manifest
When adding new inputs/outputs:
1. Update routing.manifest.yaml
2. Reference correct paths (relative to manifest)
3. Include descriptions
4. Update commit hash after changes
5. Regenerate QS anchors

### QS Integration
For quality sealing:
1. Generate SBOM (`../../../pax/OFF/sbom/`)
2. Update QS anchor (SHA256)
3. Digital signature by authorized signer
4. Timestamp recording

## Related Directories

- **../contracts/** - JSON schemas and examples
- **../evidence/** - Test evidence indexes
- **../compliance/** - Compliance evidence
- **../S1000D/** - S1000D data modules
- **../../../pax/OFF/** - PAX packages and SBOMs

---
*Part of ATA-57-20 Control Surfaces UTCS/QS framework.*
