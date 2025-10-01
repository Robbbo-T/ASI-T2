# EVIDENCE-PLANE

Software Bill of Materials, DOIs, attestations, and provenance for ASI-T2 ecosystem.

## Purpose

The Evidence Plane manages all artifacts related to:
- **SBOMs**: Software Bill of Materials (SPDX, CycloneDX)
- **Provenance**: Complete artifact lineage
- **Attestations**: Cryptographic signatures and claims
- **DOIs**: Digital Object Identifiers for citable work
- **UTCS Anchors**: Universal traceability records
- **Audit Trails**: Immutable event logs

## Architecture

```
┌─────────────┐
│  Products   │ (Build artifacts, releases)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    SBOM     │ (Syft, CycloneDX)
│  Generator  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    UTCS     │ (Canonical hash, timestamp)
│   Anchor    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Signature   │ (GPG, SSH signatures)
│   Service   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Evidence   │ (Immutable storage)
│   Archive   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ DOI Minting │ (Zenodo, DataCite)
└─────────────┘
```

## SBOM Generation

### SBOM Formats

**SPDX 2.3** (Software Package Data Exchange):
```json
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "ASI-T2-AMPEL360",
  "packages": [
    {
      "SPDXID": "SPDXRef-Package",
      "name": "ampel360-sim",
      "versionInfo": "1.0.0",
      "supplier": "Organization: ASI-T",
      "licenseConcluded": "Proprietary"
    }
  ]
}
```

**CycloneDX** (alternative format):
- JSON or XML
- Supply chain focus
- Vulnerability tracking

### SBOM Content

SBOMs include:
- All dependencies (direct and transitive)
- License information
- Version information
- Supplier/author information
- Checksums (SHA-256)
- Vulnerability information (where available)

### Generation Workflow

```bash
# Automated SBOM generation
syft dir:. -o spdx-json > sbom.spdx.json

# Or using CycloneDX
cyclonedx-cli sbom . > sbom.cyclonedx.json
```

## UTCS v5.0 Anchors

### Anchor Format

```json
{
  "utcs_version": "v5.0",
  "artifact_type": "release",
  "artifact_id": "AMPEL360-v1.0.0",
  "timestamp": "2025-01-01T00:00:00Z",
  "canonical_hash": "sha256:abc123...",
  "provenance": {
    "repository": "https://github.com/Robbbo-T/ASI-T2",
    "commit": "abc123def456",
    "branch": "main",
    "author": "Robbbo-T",
    "build_date": "2025-01-01T00:00:00Z"
  },
  "attestations": [
    {
      "type": "SBOM",
      "format": "SPDX-2.3",
      "file": "sbom.spdx.json",
      "hash": "sha256:def456..."
    },
    {
      "type": "test_results",
      "file": "test_report.json",
      "hash": "sha256:789abc..."
    }
  ],
  "signatures": [
    {
      "type": "gpg",
      "key_id": "0xABCDEF",
      "signature": "-----BEGIN PGP SIGNATURE-----..."
    }
  ]
}
```

### Canonical Hash Calculation

```bash
# For files
sha256sum artifact.json

# For directories (reproducible)
find . -type f -exec sha256sum {} \; | sort | sha256sum
```

## Attestations

### Attestation Types

**Build Attestations**:
- Build environment
- Build commands
- Build reproducibility
- Dependencies used

**Test Attestations**:
- Test results
- Coverage metrics
- V&V reports
- Safety analysis

**Security Attestations**:
- Vulnerability scans
- Static analysis
- Penetration tests
- Security audits

**Third-Party Attestations**:
- External reviews
- Certifications
- Academic validations
- Industry endorsements

### Signature Verification

```bash
# Verify GPG signature
gpg --verify artifact.sig artifact.json

# Verify SSH signature
ssh-keygen -Y verify -f allowed_signers -I user@example.com -n file -s artifact.sig < artifact.json
```

## DOI Registration

### When to Register

- Major releases (v1.0.0, v2.0.0)
- Significant milestones
- Published papers/reports
- Public datasets
- Demo artifacts for citation

### DOI Services

**Zenodo** (Recommended):
- Free service
- GitHub integration
- Version tracking
- Community support

**DataCite**:
- Research data focus
- Institutional support
- Rich metadata

**Figshare**:
- Academic focus
- Visualization support

### DOI Metadata Example

```json
{
  "title": "ASI-T2 AMPEL360 BWB v1.0.0",
  "creators": [
    {
      "name": "Pelliccia, Amedeo",
      "affiliation": "ASI-T",
      "orcid": "0000-0000-0000-0000"
    }
  ],
  "description": "First release of AMPEL360 BWB digital twin with SIL validation",
  "keywords": ["aerospace", "digital-twin", "blended-wing-body"],
  "related_identifiers": [
    {
      "identifier": "https://github.com/Robbbo-T/ASI-T2/releases/tag/v1.0.0",
      "relation": "isSupplementTo"
    }
  ]
}
```

## Audit Trails

### Event Types

- Build events
- Test executions
- Deployments
- Configuration changes
- Security events
- Access logs

### Event Format

```json
{
  "event_id": "uuid",
  "timestamp": "2025-01-01T00:00:00Z",
  "event_type": "build",
  "actor": "ci-pipeline",
  "action": "build_artifact",
  "resource": "AMPEL360-sim",
  "result": "success",
  "metadata": {
    "commit": "abc123",
    "duration": 300
  },
  "signature": "..."
}
```

### Immutability

Audit trails are:
- Append-only (no modifications)
- Cryptographically signed
- UTCS anchored
- Backed up to cold storage

## Evidence Storage

### Storage Tiers

**Active Evidence** (0-1 year):
- Fast access
- Full indexing
- Query support

**Archive Evidence** (>1 year):
- Cold storage
- Compressed
- UTCS anchored

**Permanent Evidence**:
- Critical releases
- Major milestones
- Certification artifacts
- DOI-linked artifacts

### Retention Policy

- **Releases**: Permanent
- **Test results**: 5 years
- **Audit logs**: 7 years (regulatory)
- **Development artifacts**: 2 years

## Implementation Roadmap

**H0 (0-90 days)**:
- Basic SBOM generation
- UTCS anchor creation
- Git tag signing
- Evidence storage

**H1 (3-9 months)**:
- Automated attestations
- DOI registration
- Third-party reviews
- Audit trail system

**H2 (9-24 months)**:
- Advanced provenance tracking
- Supply chain security
- Formal verification integration
- Regulatory compliance automation
