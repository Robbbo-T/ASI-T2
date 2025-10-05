# SBOM Baseline — SPDX 2.3

**Goal.** Ensure a minimal, portable SBOM that downstream verifiers can parse without vendor tooling.

## Required document fields
- `spdxVersion: "SPDX-2.3"`
- `dataLicense: "CC0-1.0"`
- `SPDXID: "SPDXRef-DOCUMENT"`
- `name`
- `documentNamespace` (unique URI)
- `creationInfo.creators[]` (≥1)

## Required package coverage
At least one `packages[]` entry with:
- `SPDXID`
- `name`
- `versionInfo` (if known)
- `downloadLocation` or `NOASSERTION`
- `filesAnalyzed` (true/false)
- `licenseConcluded` or `NOASSERTION`

## File placement
- Path referenced by `exports.sbom` in the IEF manifest.
