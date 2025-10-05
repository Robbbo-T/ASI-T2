# Verify Spec — IEF v0.1

A conforming verifier MUST:

1) **Validate manifest**
- JSON parse
- Conform to `schemas/context.schema.json`
- `exports.*` paths exist on disk

2) **Validate SBOM**
- File exists at `exports.sbom`
- Parses as SPDX 2.3
- At least one package present

3) **Validate checksums** (if `checksums.sha256` present)
- Format: `<sha256>  <path>`
- All paths exist
- Recomputed hashes match

4) **Reproducibility**
- Checksum list sorted by path (LC_ALL=C)
- Reject archives that encode non-deterministic metadata (domain profiles may enforce)

**Output.** Verifier SHOULD emit JSON summary with pass/fail per check and an overall status.
