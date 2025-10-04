-----BEGIN PLACEHOLDER SIGNATURE-----
This is a placeholder signature file for UTCS bundle attestation.

In production, this file would contain:
- Ed25519 signature over the bundle archive
- Generated using: cosign sign-blob UTCS_BUNDLE.tar.zst
- Verifiable with public key from ASI-T2 keyring

Bundle ID: utcs-bundle-bwb-q100-2025-10-03
Timestamp: 2025-10-03T09:30:00Z
Algorithm: Ed25519

To generate real signatures:
1. Install cosign: https://docs.sigstore.dev/cosign/installation/
2. Generate keypair: cosign generate-key-pair
3. Sign bundle: cosign sign-blob --key cosign.key UTCS_BUNDLE.tar.zst > bundle.sig
4. Verify: cosign verify-blob --key cosign.pub --signature bundle.sig UTCS_BUNDLE.tar.zst

For H0 (0-90 days), this is acceptable as placeholder.
For H1+, real signatures are REQUIRED.
-----END PLACEHOLDER SIGNATURE-----
