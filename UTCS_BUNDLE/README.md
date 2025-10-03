# UTCS Bundle — BWB-Q100

**Bundle ID:** utcs-bundle-bwb-q100-2025-10-03  
**Schema:** utcs.manifest.v5  
**Program:** BWB-Q100 (Blended Wing Body - Quantum Optimization 100)  
**Version:** 0.1.0  
**Bridge:** QS→FWD→UE→FE→CB→QB

---

## Overview

This is a **UTCS v5.0 bundle** providing the authoritative provenance spine for the ASI-T2 BWB-Q100 program. It implements the **UiX Threading** model (Context/Content/Cache & Structure/Style/Sheet) with deterministic bundling, making releases verifiable, reproducible, and ethically governed.

### Key Properties

- **Determinism** — Same inputs → same bundles (hash-stable)
- **Traceability** — End-to-end lineage (source → build → artifact → demo → audit)
- **Policy-first** — MAL-EEM/MAP-EEM enforce allow-lists, ethical scope, and revocation
- **Standards-aligned** — S1000D/ATA grammar, DO-178C/ECSS guidance, SLSA-lite attestations

---

## Bundle Structure

```
UTCS_BUNDLE/
├── manifest.utcs.yaml           # REQUIRED — canonical manifest
├── hashes/                      # REQUIRED — per-file digests (SHA-256)
├── context/                     # narratives & overview docs
│   ├── MASTER_WHITEPAPER_1.md
│   └── MASTER_WHITEPAPER_3_UTCS.md
├── content/                     # schemas, code, contracts
│   └── schemas/
│       ├── utcs.manifest.v5.json
│       ├── map.control.v1.json
│       └── map.telemetry.v1.json
├── cache/                       # examples, test vectors, data
│   └── examples/
│       └── fcr1-demo.json
├── structure/                   # grammar, mappings, path validators
│   ├── tfa_grammar.md
│   └── topic_hierarchy.md
├── style/                       # CSL, headers, NOTICE, LICENCE
│   ├── citation.csl
│   └── NOTICE
├── sheet/                       # Makefile, CI, reproducibility scripts
│   ├── Makefile
│   └── ci/
│       └── validate_utcs.py
└── attestations/                # SBOM, signatures, SLSA-lite, DOIs
    ├── sbom.spdx.json
    └── bundle.sig
```

---

## Quick Start

### Prerequisites

- Python 3.8+
- jsonschema, PyYAML

Install dependencies:

```bash
pip install jsonschema PyYAML
```

### Validation

Run basic validation:

```bash
cd UTCS_BUNDLE
python sheet/ci/validate_utcs.py --manifest manifest.utcs.yaml
```

Or use make:

```bash
make validate
```

Full validation with crosswalk checks:

```bash
make validate-full
```

---

## UiX Threading Model

The bundle follows the **UiX v5.0** model with six sections:

### Threading (Input)
- **Context** — Narrative documents, whitepapers, overviews
- **Content** — Schemas, code, contracts, specifications
- **Cache** — Examples, test vectors, recordings, synthetic data

### Binding (Output)
- **Structure** — Directory grammar, topic & DMC mappings, path validators
- **Style** — Citation styles, lints, legal headers, formatting rules
- **Sheet** — Build scripts, CI jobs, reproducibility recipes

---

## TFA Bridge Integration

This bundle supports the complete TFA V2 bridge flow:

```
QS → FWD → UE → FE → CB → QB
```

Each layer has dedicated evidence hooks and topic mappings:

- **QS** — Primordial anchor and ordering of state
- **FWD** — Forward Wave Dynamics (prediction/probability)
- **UE** — Unit Element / Collapse (measurement)
- **FE** — Federation Entanglement / Contracting
- **CB** — Classical Bit / Companion Binary
- **QB** — Bit Cubic (non-quantum advisory)

See `structure/topic_hierarchy.md` for complete MAP topic → TFA path → S1000D DMC crosswalk.

---

## Validation Checks

The bundle includes comprehensive validation:

1. **Schema Validation** — JSON Schema validation against utcs.manifest.v5.json
2. **Structure Validation** — Required fields, patterns, and formats
3. **UiX Validation** — All six sections present with correct types
4. **File Reference Validation** — All referenced files exist
5. **Hash Validation** — SHA-256 hashes match actual files
6. **Ethics Guard Validation** — MAL-EEM/MAP-EEM configured
7. **Crosswalk Validation** — TFA grammar and topic hierarchy complete

---

## CI/CD Integration

This bundle includes GitHub Actions workflow for automated validation:

- `.github/workflows/utcs-validate.yml` — Validates on push/PR
- Runs on: `ubuntu-latest` with Python 3.12
- Checks: manifest validation, schema validation, SBOM verification

---

## Evidence & Attestations

### SBOM (Software Bill of Materials)

Located at `attestations/sbom.spdx.json` in SPDX 2.3 format.

**Note:** Current SBOM is a placeholder. Regenerate with:

```bash
syft dir:. -o spdx-json > attestations/sbom.spdx.json
```

### Signatures

Located at `attestations/bundle.sig`.

**Note:** Current signature is a placeholder. Generate real Ed25519 signature with:

```bash
# Install cosign
# Generate keypair
cosign generate-key-pair

# Create bundle archive
tar -czf UTCS_BUNDLE.tar.gz UTCS_BUNDLE/

# Sign
cosign sign-blob --key cosign.key UTCS_BUNDLE.tar.gz > attestations/bundle.sig

# Verify
cosign verify-blob --key cosign.pub --signature attestations/bundle.sig UTCS_BUNDLE.tar.gz
```

### DOI (Digital Object Identifier)

**Status:** TBA (DataCite registration pending)

DOI will be registered through DataCite for permanent citation and retrieval.

---

## Schemas

Three JSON schemas are included:

1. **utcs.manifest.v5.json** — UTCS v5.0 manifest schema (canonical)
2. **map.control.v1.json** — ASI-T2 MAP control contract schema
3. **map.telemetry.v1.json** — ASI-T2 MAP telemetry contract schema

All schemas follow JSON Schema Draft 2020-12.

---

## Crosswalk Tables

### TFA Grammar (`structure/tfa_grammar.md`)

Defines the canonical path grammar:

```
domains/<DOMAIN_CODE>/ATA-XX/<XX-XX>_<DESC>/S1000D/<LAYER>/<PACK>/<SUBPACK>
```

With validation rules for:
- ATA chapter alignment
- Layer selection (QS/FWD/UE/FE/CB/QB)
- Pack types (CAx/QOx/PAx)
- Subpackage constraints (PAx uses ONLY OB/OFF)

### Topic Hierarchy (`structure/topic_hierarchy.md`)

Maps:
- MAP Topics (e.g., `map/1/log/BWB-Q100/AAA/STATES/QS/QS`)
- TFA Paths (e.g., `domains/AAA/ATA-57/57-10_Wing/S1000D/QS/PAx/OB/`)
- S1000D DMCs (e.g., `DMC-BWB-Q100-A-57-10-00-00A-QS0A-D`)

---

## Ethics & Compliance

### Responsible Use

This framework **MUST NOT** be used to facilitate weaponisation. Dual-use is controlled under **MAL-EEM/MAP-EEM**.

### Compliance

- **Quality:** AS9100-lite controls (configuration, V&V, non-conformities)
- **Export:** EU 2021/821 assessment; ITAR/EAR when applicable
- **Privacy/Security:** Least-privilege access; immutable decision logging; redaction rules

See `style/NOTICE` for complete ethics and compliance information.

---

## References

- [Master Whitepaper #1](context/MASTER_WHITEPAPER_1.md) — TFA V2 Architecture
- [Master Whitepaper #3](context/MASTER_WHITEPAPER_3_UTCS.md) — QS/UTCS Provenance Framework
- [RELEASE.md](../RELEASE.md) — Release notes and checksums
- [CITATION.cff](../CITATION.cff) — Machine-readable citation metadata

---

## Support

For questions, issues, or contributions:

- **GitHub:** https://github.com/Robbbo-T/ASI-T2
- **Issues:** https://github.com/Robbbo-T/ASI-T2/issues
- **Maintainer:** ASI-T Architecture Team

---

## License

Proprietary with Responsible Use clause. See `style/NOTICE` for complete license information.
