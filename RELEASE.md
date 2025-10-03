# Release v0.1.0 — QS/UTCS Framework Scaffolding

**Release Date:** 2025-10-03  
**Bundle ID:** utcs-bundle-bwb-q100-2025-10-03  
**Program:** BWB-Q100 (Blended Wing Body - Quantum Optimization 100)  
**Bridge:** QS→FWD→UE→FE→CB→QB

---

## Highlights

This release introduces the UTCS v5.0 scaffolding for the ASI-T2 ecosystem:

- ✓ **UTCS v5.0 manifest schema** and bundle structure
- ✓ **UiX Threading model**: Context/Content/Cache & Structure/Style/Sheet
- ✓ **Evidence taps** for MAP.v1 contracts (control, telemetry, log)
- ✓ **TFA bridge mappings** across all six layers (QS/FWD/UE/FE/CB/QB)
- ✓ **FCR-1 checks** wired into CI pipeline
- ✓ **JSON schemas** for manifest, MAP control, and MAP telemetry
- ✓ **Crosswalk tables** linking MAP topics ↔ TFA paths ↔ S1000D DMCs
- ✓ **Validation tooling** with comprehensive checks
- ✓ **Ethics guards** (MAL-EEM, MAP-EEM) enabled by default

---

## Artifacts

### Primary Bundle
- **Archive:** `UTCS_BUNDLE.tar.gz`
- **SHA-256:** (to be computed on bundle creation)

### Attestations
- **SBOM:** `attestations/sbom.spdx.json` (placeholder - regenerate with syft)
- **Signature:** `attestations/bundle.sig` (placeholder - replace with Ed25519 signature)
- **DOI:** TBA (DataCite registration pending)

### Schemas
- `content/schemas/utcs.manifest.v5.json` — UTCS v5.0 manifest schema
- `content/schemas/map.control.v1.json` — MAP control contract schema
- `content/schemas/map.telemetry.v1.json` — MAP telemetry contract schema

### Documentation
- `context/MASTER_WHITEPAPER_1.md` — TFA V2 Architecture
- `context/MASTER_WHITEPAPER_3_UTCS.md` — QS/UTCS Provenance & Evidence Framework
- `structure/tfa_grammar.md` — TFA path grammar and validation rules
- `structure/topic_hierarchy.md` — MAP topic crosswalk tables

---

## Installation

### Prerequisites
- Python 3.8+
- jsonschema, PyYAML

### Validation

```bash
cd UTCS_BUNDLE
make validate
```

Or directly:

```bash
python sheet/ci/validate_utcs.py --manifest manifest.utcs.yaml
```

### Full Validation (with crosswalk checks)

```bash
make validate-full
```

---

## Checksums

To verify bundle integrity after download:

```bash
# Compute SHA-256 of bundle
sha256sum UTCS_BUNDLE.tar.gz

# Compare with published checksum
cat UTCS_BUNDLE.tar.gz.sha256
```

---

## Known Limitations (H0 Phase)

This is an H0 (0-90 days) scaffolding release with the following limitations:

1. **SBOM:** Placeholder SBOM provided. Regenerate with `syft dir:. -o spdx-json` for production use.
2. **Signatures:** Placeholder signature file. Replace with real Ed25519 signatures using cosign.
3. **Hashes:** File hashes in manifest are marked as "pending". Update after final content freeze.
4. **DOI:** DOI registration with DataCite is pending.
5. **Hall of Records:** Not yet implemented (planned for H0 completion).

---

## Migration from Previous Versions

This is the first UTCS v5.0 release. No migration required.

**Legacy UTCS v4.x users:** The v5.0 UiX Threading model replaces the previous "Universal Traceability & Crypto Signatures" semantics. See Master Whitepaper #3 for mapping details.

---

## Roadmap

### H0 (0–90 days) — Current Phase
- [x] UTCS v5.0 manifest schema
- [x] CLI validation tooling
- [x] CI/CD integration (GitHub Actions)
- [x] Crosswalk generator (TFA paths ↔ MAP topics ↔ S1000D DMCs)
- [ ] UTCS CLI tool (`utcs` command)
- [ ] Hall of Records (append-only registry)
- [ ] Real SBOM generation pipeline
- [ ] Ed25519 signature workflow

### H1 (3–9 months)
- X25519 encryption for sensitive bundles
- Delta-bundles for efficient updates
- Automated DOI registration with DataCite
- Dashboard for bundle verification
- Third-party verification endpoints

### H2 (9–24 months)
- Formal verification of manifest schemas
- Multi-organization federated Hall of Records
- External audits and compliance certifications
- Public datasets with reproducible notebooks

---

## How to Cite

```bibtex
@techreport{pelliccia2025utcs,
  author = {Pelliccia, Amedeo},
  title = {QS/UTCS Provenance \& Evidence Framework},
  institution = {ASI-T Architecture Team},
  year = {2025},
  version = {0.1.0},
  doi = {TBA},
  url = {https://github.com/Robbbo-T/ASI-T2}
}
```

Or in plain text:

> Pelliccia, A. (2025). *QS/UTCS Provenance & Evidence Framework*. v0.1.0. DOI: TBA.

Machine-readable metadata is available in `CITATION.cff` within this bundle.

---

## Support

For questions, issues, or contributions:

- **GitHub:** https://github.com/Robbbo-T/ASI-T2
- **Issues:** https://github.com/Robbbo-T/ASI-T2/issues
- **Maintainer:** ASI-T Architecture Team

---

## License

Proprietary with Responsible Use clause. See `style/NOTICE` for details.

**Ethics & Compliance:** This framework MUST NOT be used to facilitate weaponisation. Dual-use is controlled under MAL-EEM/MAP-EEM. All use must comply with EU 2021/821, ITAR/EAR, AS9100-lite controls, and applicable law.
