# IEF v0.1 Specifications

Detailed specifications for IEF v0.1 components and requirements.

## Specifications

### SBOM-BASELINE.md

Defines minimum requirements for SPDX 2.3 SBOMs in IEF:

- **Document fields:** `spdxVersion`, `dataLicense`, `SPDXID`, `name`, `documentNamespace`, `creationInfo.creators[]`
- **Package requirements:** At least one package with `SPDXID`, `name`, `downloadLocation`, `filesAnalyzed`, `licenseConcluded`
- **File placement:** Referenced by `exports.sbom` in the manifest

**Goal:** Ensure portable SBOMs that any verifier can parse without vendor tooling.

### VERIFY-SPEC.md

Verification requirements for IEF conformance:

1. **Manifest validation** - JSON parse, schema compliance, path resolution
2. **SBOM validation** - File exists, SPDX 2.3 format, package presence
3. **Checksum validation** - Format verification, path existence, hash matching
4. **Reproducibility** - Deterministic ordering (LC_ALL=C)

**Output:** Verifiers should emit JSON summary with pass/fail per check.

### NAMING-POLICY.md

Recommended naming convention for IEF evidence packs:

```
IEF-<ORG>-<PRODUCT>-<SCOPE>-r<REV>.<EXT>
```

Examples:
- `IEF-ACME-WIDGET-CORE-r001.zip`
- `IEF-ACME-WIDGET-DOCS-r002.tar.gz`

**Status:** Recommended (non-binding) in v0.1. Domain profiles may enforce stricter rules.

## Usage

These specifications guide:

- **Tool developers** - Implement validators and generators
- **Adopters** - Understand requirements and best practices
- **Profile authors** - Extend baseline for domain-specific needs (Aerospace, Energy, Defense)

## Compliance

To be IEF v0.1 compliant, implementations must:

1. ✅ Accept manifests conforming to `../schemas/context.schema.json`
2. ✅ Validate SBOMs per SBOM-BASELINE.md
3. ✅ Support verification checks per VERIFY-SPEC.md
4. 📋 Optionally follow NAMING-POLICY.md

## References

- [Main IEF Specification](../README.md)
- [SPDX 2.3 Specification](https://spdx.github.io/spdx-spec/v2.3/)
