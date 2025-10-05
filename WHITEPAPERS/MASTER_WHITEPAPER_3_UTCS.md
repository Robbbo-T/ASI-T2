---
id: ASIT2-WHITEPAPER-MASTER-3_UTCS
project: ASI-T2
artifact: Master Whitepaper #3 — QS/UTCS Provenance & Evidence Framework
llc: GENESIS
classification: PUBLIC-DRAFT
version: 0.1.0
release_date: "2025-10-03"
author: "Amedeo Pelliccia"
maintainer: "ASI-T Architecture Team"
bridge: "QS→FWD→UE→FE→CB→QB"
ethics_guard: MAL-EEM · MAP-EEM
utcs_mi: v5.0
framework: TFA-V2
status: "Public draft for technical review"
ssot: "ASI-T · Universal Injection Prompt (v1)"
canonical_hash: pending
doi: TBA
---

# **QS/UTCS Provenance & Evidence Framework**

> **IDEALE‑EU — Intelligence, Defense, Energy, Aerospace, Logistics (ESG‑EU)**
> Cross‑cutting strategy informing governance, disclosures, and auditability of ASI‑T2 releases in EU contexts.

---

## Executive Summary

**QS/UTCS** provides the **authoritative provenance spine** for the ASI‑T2 ecosystem. It combines:

* **QS (Primordial)** — the canonical anchor and ordering of state, and
* **UTCS v5.0** — **UiX Threading (Context/Content/Cache) & Structure/Style/Sheet**, a deterministic bundling model that binds all artifacts (docs, schemas, binaries, media, evidence) into **auditable releases**.

Together, QS/UTCS makes each release **verifiable, reproducible, and ethically governed**, with signed tags, SBOMs, DOIs, and immutable ledgers across the TFA bridge **QS→FWD→UE→FE→CB→QB**. UTCS bundles are transport‑agnostic and integrate natively with **ASI‑T2 MAP** contracts and **TFA MAL** layer services.

**Key properties**

* **Determinism** — same inputs → same bundles (hash‑stable).
* **Traceability** — end‑to‑end lineage (source → build → artifact → demo → audit).
* **Policy‑first** — MAL‑EEM/MAP‑EEM enforce allow‑lists, ethical scope, and revocation.
* **Standards‑aligned** — S1000D/ATA grammar, DO‑178C/ECSS guidance, SLSA‑lite attestations.

---

## 0. Normative Language

The key words **MUST**, **SHOULD**, and **MAY** are to be interpreted as normative per RFC‑2119.

---

## 1. Conceptual Model

```mermaid
graph LR
  QS[QS · Primordial State] --> FWD[FWD · Forward Wave Dynamics]
  FWD --> UE[UE · Unit Element / Collapse]
  UE --> FE[FE · Federation Entanglement / Contracting]
  FE --> CB[CB · Classical Bit]
  CB --> QB[QB · Bit Cubic (non‑quantum)]

  subgraph UTCS v5.0
  C[Context]:::ctx
  T[Content]:::ctx
  H[Cache]:::ctx
  S[Structure]:::sty
  Y[Style]:::sty
  X[Sheet]:::sty
  end

  C -.threads.-> S
  T -.threads.-> S
  H -.threads.-> S
  S --> |binds| Y
  S --> |binds| X
  classDef ctx fill:#eef,stroke:#66c;
  classDef sty fill:#efe,stroke:#6c6;
```

**QS** is the **origin/ordering** of state and evidence. **UTCS** is the **bundle grammar** and **manifest** that binds **UiX** layers:

* **Context** — narrative, whitepapers, overviews.
* **Content** — schemas, code, contracts.
* **Cache** — examples, test vectors, recordings, synthetic data.
* **Structure** — directory grammar, topic & DMC mappings.
* **Style** — citation styles, lints, legal headers.
* **Sheet** — build scripts, CI jobs, reproducibility recipes.

*Compatibility note:* legacy alias "**Universal Traceability & Crypto Signatures**" MAY appear in historic artifacts; semantics map to UTCS v5.0.

---

## 2. Bundle Layout & Manifest

### 2.1 Directory layout (normative)

```
UTCS_BUNDLE/
├── manifest.utcs.yaml           # REQUIRED — canonical manifest
├── hashes/                      # REQUIRED — per‑file digests (SHA‑256)
├── context/                     # narratives & overview docs
├── content/                     # schemas, code, contracts
├── cache/                       # examples, test vectors, data
├── structure/                   # grammar, mappings, path validators
├── style/                       # CSL, headers, NOTICE, LICENCE
├── sheet/                       # Makefile, CI, reproducibility scripts
└── attestations/                # SBOM, signatures, SLSA‑lite, DOIs
```

### 2.2 Manifest (authoritative excerpt)

```yaml
# UTCS v5.0 Manifest (authoritative)
bundle_id: utcs-bundle-bwb-q100-2025-10-03
schema: utcs.manifest.v5
program: BWB-Q100
bridge: QS→FWD→UE→FE→CB→QB
semver: 0.1.0
created_utc: 2025-10-03T09:30:00Z
authors:
  - name: Amedeo Pelliccia
    role: Author
ethics_guard: [MAL-EEM, MAP-EEM]
ssot: ASI-T · Universal Injection Prompt (v1)
ideale_eu: true

uix:
  context:
    - context/whitepaper-map-2.md
    - context/whitepaper-utcs-3.md
  content:
    - content/schemas/map.control.v1.json
    - content/schemas/utcs.manifest.v5.json
  cache:
    - cache/examples/fcr1-demo.json
  structure:
    - structure/topic_hierarchy.md
    - structure/tfa_grammar.md
  style:
    - style/citation.csl
    - style/NOTICE
  sheet:
    - sheet/Makefile
    - sheet/ci/validate_utcs.py

attestations:
  sbom: attestations/sbom.spdx.json
  signatures:
    - attestations/bundle.sig
  doi:
    provider: datacite
    id: TBA

hashes:
  algo: sha256
  files:
    - path: content/schemas/map.control.v1.json
      digest: 3f7c...c1
    - path: structure/tfa_grammar.md
      digest: aa04...9b
compat:
  minor_floor: 0.1
  notes: "MINOR versions are wire-compatible. MAJOR may break with migrators."
```

---

## 3. Evidence Plane & Lifecycle

### 3.1 Evidence sources

* **Code lineage:** commits, signed tags, diffs, review metadata.
* **Build lineage:** compilers, flags, env, container digests.
* **Artifact lineage:** binaries, models, media, datasets.
* **Operational lineage:** logs (MAP.v1.log), telemetry (MAP.v1.telemetry).
* **Standards lineage:** S1000D DMCs, ATA chapter paths, CSDB entries.

### 3.2 Release pipeline (normative)

```
1) Tag:         git tag -s vX.Y.Z
2) SBOM:        syft dir:. -o spdx-json > attestations/sbom.spdx.json
3) Build:       make clean all  # reproducible targets only
4) Bundle:      utcs bundle --manifest manifest.utcs.yaml
5) Sign:        cosign sign-blob UTCS_BUNDLE.tar.zst > attestations/bundle.sig
6) DOI:         utcs doi publish --provider datacite --bundle UTCS_BUNDLE.tar.zst
7) Index:       utcs hall index  # Hall of Records update
```

### 3.3 Hall of Records

A versioned registry containing **bundle IDs**, **hashes**, **DOIs**, **tags**, and **audit guides**. It **MUST** be append‑only and signed.

---

## 4. Mappings: S1000D/ATA and Topic Grammar

### 4.1 Path grammar (TFA)

```
domains/<DOMAIN_CODE>/ATA-XX/<XX-XX>_<DESC>/S1000D/<LAYER>/<PACK>/<SUBPACK>
```

* `<LAYER>` ∈ {QS, FWD, UE, FE, CB, QB}
* `<PACK>` ∈ {CAx, QOx, PAx}; **PAx orientation markers are ONLY:** **OB** (Onboard), **OFF** (Outboard).

### 4.2 Topic grammar (ASI‑T2 MAP)

```
map/<major>/<contract>/<program>/<domain>/<component>/<stream>
```

* Examples (BWB‑Q100):

  * `map/1/log/BWB-Q100/AAA/STATES/QS/QS`
  * `map/1/telemetry/BWB-Q100/AAA/WAVES/FWD/FWD`
  * `map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB`

**UTCS bundles MUST** include **crosswalk tables** linking **paths ↔ topics ↔ DMCs**.

---

## 5. Cryptography & Policy

* **Signatures**: **Ed25519** for artifact signing (**REQUIRED** at H0).
* **Digests**: **SHA‑256** (bundle + per‑file).
* **Encryption**: **X25519** envelope (H1+ where sensitivity warrants).
* **Transport security**: TLS 1.3, mTLS where applicable.
* **Policy**: **MAP‑EEM/MAL‑EEM** evaluate subject×action×resource×context; decisions are logged to `map/1/log/*` with redaction where required.

**Threat mitigations**

* Replay: nonce + monotonic `seq` + tight time windows.
* Impersonation: PKI, key rotation, pinning.
* Downgrade: negotiated minor‑compat floor (manifest `compat.minor_floor`).
* Schema poisoning: signed schema distribution + strict validators.

---

## 6. Integration with ASI‑T2 MAP & TFA MAL

* **MAP Contracts** (`MAP.v1.control/telemetry/health/log`) **MUST** emit evidence hooks used by UTCS (egress taps).
* **MAL Services** (QS/FWD/UE/FE/CB/QB) **SHOULD** attach run metadata (models, seeds, solver IDs) to telemetry for bundle inclusion.
* **Programs (TFA MAP)** **MUST NOT** bypass the platform's evidence hooks.

---

## 7. Validation & CI

**Required checks (FCR‑1/FCR‑2 gates)**

* `utcs validate` — manifest schema, hashes, crosswalk completeness.
* `make sbom.check` — SPDX presence + license scan thresholds.
* `map contracts.check` — schema compatibility + topic grammar.
* `tfa path.check` — ATA/S1000D grammar and OB/OFF usage.
* Coverage reports — scenario+line/branch (thresholds per product).

**GitHub Actions skeleton**

```yaml
name: UTCS · Evidence Validation
on: [push, pull_request]
jobs:
  utcs-validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate UTCS
        run: |
          python3 -m pip install -r sheet/ci/requirements.txt
          python sheet/ci/validate_utcs.py --manifest manifest.utcs.yaml
  sbom-verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Verify SBOM
        run: jq '.' attestations/sbom.spdx.json > /dev/null
```

---

## 8. IDEALE‑EU Alignment

UTCS bundles **SHOULD** include ESG‑EU annotations: climate/energy metrics, safety indicators, socio‑economic access, and EU node relevance. Disclosures are published alongside DOIs.

---

## 9. Roadmap

| Horizon              | Deliverables                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **H0 (0–90 days)**   | UTCS v5.0 manifest schema; CLI (`utcs`); SBOM + DOI pipeline; Hall of Records (append‑only); crosswalk generator         |
| **H1 (3–9 months)**  | X25519 encryption; delta‑bundles; DOI automation; dashboards; third‑party verification endpoints                         |
| **H2 (9–24 months)** | Formal verification of manifests; multi‑org federated Hall; external audits; public datasets with reproducible notebooks |

---

## 10. Ethics & Compliance

* **Responsible Use:** this framework **MUST NOT** be used to facilitate weaponisation. Dual‑use is controlled under **MAL‑EEM/MAP‑EEM**.
* **Quality:** AS9100‑lite controls (configuration, V&V, non‑conformities).
* **Export:** EU 2021/821 assessment; ITAR/EAR when applicable.
* **Privacy/Security:** least‑privilege access; immutable decision logging; redaction rules.

> This document does not provide weaponisation instructions nor facilitate harm. All experimentation adheres to MAL‑EEM/MAP‑EEM and applicable law.

---

## 11. How to Cite

> Pelliccia, A. (2025). *QS/UTCS Provenance & Evidence Framework*. v0.1.0. DOI: TBA.
> Machine‑readable metadata will be available in `CITATION.cff` within the UTCS bundle.

---

## 12. Glossary (canonical)

**QS** — *Primordial* anchor and ordering of state.
**UTCS v5.0** — **UiX Threading (Context/Content/Cache) & Structure/Style/Sheet**; deterministic bundle grammar.
**UiX** — User‑Interface eXtended layers grouped by *threading* (Context/Content/Cache) and *binding* (Structure/Style/Sheet).
**TFA Bridge** — **QS→FWD→UE→FE→CB→QB** canonical flow.
**ASI‑T2 MAP** — Master Application **Platform** (wire contracts + transports + evidence taps).
**TFA MAL** — Main Application **Layer** services, bridge‑aligned.
**TFA MAP** — Master Application **Program** (domain applications).
**CAx/QOx/PAx** — Computer‑Aided X / **Quantum Optimizations** / Packaging & Assemblies (**OB/OFF** only).
**CSDB** — Common Source DataBase for digital platforms (AMPEL‑360, GAIA‑AIR/SPACE, H₂‑AIRPORT, BITFINANCE, INTELLIGENCE‑SECRETARY).
**SBOM** — Software Bill of Materials (SPDX JSON).
**DOI** — Digital Object Identifier (DataCite/Zenodo).
**Hall of Records** — append‑only index of bundles, hashes, DOIs, tags, audits.
**IDEALE‑EU** — EU‑aligned ESG framework overlay.

---

## Appendix A — Minimal `manifest.utcs.yaml`

```yaml
bundle_id: utcs-bundle-min
schema: utcs.manifest.v5
program: DEMO
semver: 0.1.0
created_utc: 2025-10-03T00:00:00Z
uix:
  context: [context/overview.md]
  content: [content/schema.json]
  cache: []
  structure: [structure/paths.md]
  style: [style/citation.csl]
  sheet: [sheet/Makefile]
attestations:
  sbom: attestations/sbom.spdx.json
hashes:
  algo: sha256
  files:
    - path: content/schema.json
      digest: deadbeef...
compat:
  minor_floor: 0.1
```

---

## Appendix B — `CITATION.cff` (skeleton)

```yaml
cff-version: 1.2.0
title: QS/UTCS Provenance & Evidence Framework
message: Please cite this software and evidence bundle if you use it.
authors:
  - family-names: Pelliccia
    given-names: Amedeo
version: 0.1.0
doi: TBA
date-released: 2025-10-03
license: MIT-Responsible-Use
```

---

## Appendix C — `RELEASE.md` (skeleton)

```markdown
# Release v0.1.0 — QS/UTCS

## Highlights
- UTCS v5.0 manifest schema and CLI
- Evidence taps for MAP.v1 contracts
- FCR-1 checks wired into CI

## Artifacts
- UTCS bundle: UTCS_BUNDLE.tar.zst (sha256: …)
- SBOM: attestations/sbom.spdx.json
- Signature: attestations/bundle.sig
- DOI: TBA

## Checksums
```

---

## Appendix D — Copilot Agent PR Prompt (UTCS package)

```
You are Copilot Agent. Open a PR that introduces UTCS v5.0 scaffolding.

1) Create `UTCS_BUNDLE/` with folders: context, content, cache, structure, style, sheet, hashes, attestations.
2) Add `manifest.utcs.yaml` per Master Whitepaper #3 (fill program=BWB-Q100, bridge=QS→FWD→UE→FE→CB→QB).
3) Wire `sheet/ci/validate_utcs.py` and `.github/workflows/utcs-validate.yml` as in §7.
4) Generate SBOM with `syft` and place at `attestations/sbom.spdx.json`.
5) Add `structure/tfa_grammar.md` and `structure/topic_hierarchy.md` crosswalks.
6) Update `CITATION.cff` and `RELEASE.md` skeletons.
7) Ensure all new files are referenced in the manifest and hashes are generated.

Title: chore(utcs): introduce UTCS v5.0 scaffolding and CI validation
Labels: evidence, utcs, ci, docs
```
