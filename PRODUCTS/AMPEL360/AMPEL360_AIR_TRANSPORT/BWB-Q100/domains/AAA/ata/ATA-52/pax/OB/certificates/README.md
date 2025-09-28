---
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/OB/certificates/README.md
bridge: CB→QB→UE→FWD→QS
canonical_hash: TBD
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: AAA-PAX-OB-CERTIFICATES-OV-0001
llc: SYSTEMS
maintainer: ASI-T Architecture Team
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100
release_date: '2025-01-23'
utcs_mi: v5.0
version: 0.1.0
---

# OB Certificates - Packaging

This directory contains OB (On-Board) certificates and cryptographic signatures for BWB-Q100 AAA domain packaging verification.

## Purpose

Manages security certificates and signatures including:

- Digital signatures for package verification (cosign/in-toto)
- X.509 certificate chains for trust establishment
- SLSA attestations for supply chain security
- Cryptographic verification artifacts

## Certificate Contents

- **Package signatures** - Cosign/in-toto signatures for OB artifacts and partitions
- **Trust chains** - X.509 certificate chains for signature verification
- **Attestations** - SLSA Level 3 attestations for build provenance
- **Verification keys** - Public keys for signature validation

## Security Integration

OB certificates support:

- Automated signature verification in deployment pipelines
- Trust chain validation for security compliance
- Supply chain integrity verification (SLSA framework)
- Runtime signature checking for OB partition loading