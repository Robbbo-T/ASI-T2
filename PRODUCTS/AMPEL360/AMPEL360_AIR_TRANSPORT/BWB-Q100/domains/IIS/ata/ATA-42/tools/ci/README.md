# CI Templates for ATA-42 IMA

## Structure Validation
- Directory structure compliance
- File naming conventions
- Link integrity checks

## AFDX Validation
- VL table schema compliance
- BAG and redundancy validation
- Payload size verification

## ARINC 653 Validation
- Schedule validation (windows sum ≤ major frame)
- Partition budget compliance
- Memory allocation verification

## Security Validation
- Cryptographic implementation checks
- Key management compliance
- Attestation verification

## SBOM and Provenance
- Build artifact signing
- SBOM difference tracking
- QS signature verification

**Usage:** These templates should be integrated into the CI/CD pipeline
**Status:** Template definitions - to be implemented in CI system