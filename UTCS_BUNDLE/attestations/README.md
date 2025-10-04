# Attestations

This directory contains evidence artifacts for the UTCS v5.0 bundle, including SBOMs, signatures, and DOI references.

## Contents

### SBOM (Software Bill of Materials)

**File:** `sbom.spdx.json`

SPDX 2.3 format SBOM providing complete software inventory for the UTCS bundle. This includes:
- Package information and versions
- License declarations
- Component relationships
- Supplier information

**Current Status:** Placeholder SBOM provided for H0 phase.

**Production Use:** Regenerate with [syft](https://github.com/anchore/syft):

```bash
cd /path/to/UTCS_BUNDLE
syft dir:. -o spdx-json > attestations/sbom.spdx.json
```

### Signatures

**File:** `bundle.sig`

Ed25519 cryptographic signature over the bundle archive for integrity verification.

**Current Status:** Placeholder file with instructions for H0 phase.

**Production Use:** Generate with [cosign](https://docs.sigstore.dev/cosign/installation/):

```bash
# Generate keypair (one time)
cosign generate-key-pair

# Create bundle archive
tar -czf UTCS_BUNDLE.tar.gz UTCS_BUNDLE/

# Sign bundle
cosign sign-blob --key cosign.key UTCS_BUNDLE.tar.gz > attestations/bundle.sig

# Verify signature
cosign verify-blob --key cosign.pub --signature attestations/bundle.sig UTCS_BUNDLE.tar.gz
```

### DOI (Digital Object Identifier)

DOI registration is referenced in `manifest.utcs.yaml` under `attestations.doi`.

**Current Status:** TBA - DataCite registration pending

**Provider:** DataCite  
**Process:** Automated registration planned for H1 phase via `utcs doi publish` command

## Requirements

Per Master Whitepaper #3 §5:

- **Signatures:** Ed25519 required at H0
- **Digests:** SHA-256 for bundle + per-file
- **Encryption:** X25519 envelope (H1+ where sensitivity warrants)
- **Transport security:** TLS 1.3, mTLS where applicable

## Validation

SBOM and signature files are validated by:

```bash
cd UTCS_BUNDLE/sheet
make check
```

Or via CI/CD workflow `.github/workflows/utcs-validate.yml`.

## References

- [Master Whitepaper #3](../context/MASTER_WHITEPAPER_3_UTCS.md) — §3 Evidence Plane & Lifecycle
- [SPDX Specification](https://spdx.dev/specifications/) — SBOM format standard
- [Sigstore](https://www.sigstore.dev/) — Signature tooling (cosign)
- [DataCite](https://datacite.org/) — DOI registration provider
