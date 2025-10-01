# Manifests

Evidence manifests with configuration hashes, SBOM references, and QS anchors.

## Files

- **manifest.yaml** — Primary evidence manifest

## Manifest Structure

```yaml
manifest:
  id: string                      # Unique manifest identifier
  version: string                 # Manifest version
  date: ISO8601                   # Creation timestamp
  product: "GAIA-AIR/IDRO_WALL"
  domain: "IIS"
  ata_chapter: "ATA-42"
  
  configuration:
    - artifact: path              # Relative path
      hash: sha256:...            # SHA-256 hash
      version: string             # Artifact version
      description: string
  
  sbom:                           # Software Bill of Materials
    - component: string           # Component name
      version: string
      license: string
      supplier: string
      hash: sha256:...
  
  testing:
    - test_report: path
      hash: sha256:...
      status: PASS|FAIL
      coverage: percentage
  
  approvals:
    - approver: string
      role: string
      date: ISO8601
      signature: string
  
  mal_eem:
    guard_version: string         # MAL-EEM ethics guard version
    policy_hash: sha256:...       # Policy pack hash
  
  utcs_mi: string                 # UTCS-MI version
  qs_anchor: string               # Quantum seal anchor for immutability
```

## Purpose

Provides cryptographically verifiable evidence bundle linking:
- Configuration files to their approved states
- Test results to configurations
- SBOM components to security assessments
- Approvals to specific artifact versions
