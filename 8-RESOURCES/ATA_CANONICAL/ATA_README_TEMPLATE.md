---
id: "<DOMAIN>-<ATA>-CANONICAL"
project: "ASI-T2"
artifact: "<ATA> Canonical — <Short Title>"
llc: "SYSTEMS"
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "0.1.0"
release_date: "2025-09-30"
maintainer: "<DOMAIN TEAM>"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: "MAL‑EEM"
canonical_hash: "pending"
-------------------------

# <ATA> — Canonical Home (Domain: <DOMAIN>)

This README defines the **standard structure** and **governance model** for the canonical `<ATA>` folder owned by `<DOMAIN>` within **ASI‑T2**. It is the **single source of truth** for this ATA chapter. Product trees (e.g., `PRODUCTS/AMPEL360/...`) must reference this location via **symlinks**.

**Legend**

* **[CANONICAL]** → Primary ownership (this folder)
* **[SHARED]** → Co‑owned via overlays/variants, documented in `governance/cross_references.yaml`

**Ownership**

* `canonical_domain: <DOMAIN>`
* `shared_domains: [<DOM?>, ...]` (if any, see registry `8-RESOURCES/ATA_CANONICAL/ATA_REGISTRY.yaml`)

---

## 1) Directory Map (Standard)

```
README.md
CONVENTIONS.md

governance/
  change_control/
  baselines/
  risk_management/
  cross_references.yaml
  audits/

os/
  S1000D/
  design/
    architecture/
    icd/
    diagrams/
  configuration/
    manifests/
    schedule.xml
  testing/
  compliance/
    certification/
    verification/

manufacturing/
  bom/
  process/
  quality/
  tooling/
  test/
  packaging/
    manifests/

sustainment/
  service_mro/
  spares/
  reliability/
  obsolescence/
  cas_security/
  recycling_disposal/
    weee_rohs_reach/
    data_sanitization/
    manifests/

assets/
scripts/
docs/
```

---

## 2) Purpose & Scope per Area

**governance/**

* **change_control/**: PR/merge policy, versioning, semantic commits, UTCS anchors.
* **baselines/**: formal baselines (BL‑0, BL‑1…), signed hashes (QS), release notes.
* **risk_management/**: safety/cyber methods (e.g., ARP4761 FHA/FTA/FMEA, STRIDE), mitigations.
* **cross_references.yaml**: overlay/variant links to other domains' ATAs (see §5).
* **audits/**: internal/external findings, CAR/PAR records, evidence.

**os/**

* **S1000D/**: DMRL seeds, BREX, data modules (descriptive/procedural/illustrated), IETP artifacts.
* **design/**: architecture views, ICDs, diagrams (UML/SysML, wiring/labeling, timing).
* **configuration/**: manifests (SBOM/CBOM), `schedule.xml` (build/test/packaging), parameters.
* **testing/**: unit/IL/SIL/HIL, trace matrices, coverage, tool qual outputs (DO‑330).
* **compliance/**: certification and verification evidence (DO‑178C/254/297, CS‑25/CS‑E, etc.).

**manufacturing/**

* **bom/**: EBOM/MBOM, alternates, serialization strategy.
* **process/**: routings, travelers, special processes, heat/lot records.
* **quality/**: control plans, FAIRs, inspection records.
* **tooling/**: jigs/fixtures/tool qualification.
* **test/**: ATP/QTP, acceptance data.
* **packaging/**: handling, logistics, manifests for shipment.

**sustainment/**

* **service_mro/**: maintenance plans, intervals, task cards.
* **spares/**: provisioning, rotables, line‑replaceable units.
* **reliability/**: FRACAS, MTBF/Weibull, fleet analytics.
* **obsolescence/**: DMSMS, alternates, lifecycles.
* **cas_security/**: continued airworthiness & security monitoring (DO‑326A/356A ops).
* **recycling_disposal/**: WEEE/ROHS/REACH, data sanitization, EoL manifests.

**assets/**

* Technical assets (images, CGM/WebCGM, CAD exports). Use metadata and QS hashes.

**scripts/**

* Local automation, e.g., validators, generators (see §6 CI & Validation).

**docs/**

* Design notes, whitepapers, derived guidance.

---

## 3) S1000D & IETP Integration

* **DMRL location:** `os/S1000D/` (per‑ATA)
* **BREX:** place BREX as `os/S1000D/brex/DMC-<MODEL>-A-00-00-00-00A-022A-D-EN-US.xml` (or project BREX in `8-RESOURCES` if shared).
* **Data Modules:** organize by type (descriptive/procedural/illustrated), with consistent DMC keys and ICNs.
* **Illustrations:** prefer WebCGM; hotspots link to procedures by ICN. Store in `assets/` and reference from DMs.

---

## 4) Compliance Matrix Hooks

This canonical folder inherits applicable entries from `8-RESOURCES/ATA_CANONICAL/COMPLIANCE_MATRIX.yaml`. Add per‑ATA specifics in `os/compliance/` if needed.

* **Certification:** DO‑178C/331/330/297 (software); DO‑254 (hardware) — as applicable.
* **Safety:** ARP4754A/ARP4761.
* **Cybersecurity:** DO‑326A/356A.
* **Airworthiness/Systems:** CS‑25/CS‑E (depending on ATA), ARINC specs (e.g., 429/664/661).

---

## 5) Cross‑Domain References (Overlays/Variants)

Define overlays/variants in `governance/cross_references.yaml` using the master schema in `8-RESOURCES/ATA_CANONICAL/XREF_MASTER.yaml`.

**Example stub**

```yaml
xrefs:
  - from: { ata: <ATA>, domain: <DOMAIN> }
    to:   { ata: <ATA>, domain: <OTHER_DOMAIN> }
    type: overlay   # or: variant
    reason: "<short rationale>"
    artifacts:
      - PRODUCTS/AMPEL360/.../<OTHER_DOMAIN>/ata/<ATA>/security/THREATS.md
```

---

## 6) CI & Validation

This canonical folder is provisioned/guarded by scripts in `scripts/` (repo root):

* `scripts/standardize_ata_structure.py` — ensures scaffold and product symlinks exist.
* `scripts/validate_cross_references.py` — schema checks for `cross_references.yaml`.
* `scripts/map_compliance.py` — renders effective compliance matrix for this ATA.
* `scripts/verify_canonical_uniqueness.py` — one canonical per ATA.
* `scripts/validate_symlinks.py` — relative symlink integrity in product trees.

**Pre‑commit/CI expectations**

* No missing required directories (see §1).
* Cross‑refs point to valid domains/paths.
* `COMPLIANCE_MATRIX.yaml` entries resolve for this ATA.
* All `.xml` and `.yaml` files linted.

---

## 7) Symlink Policy (PRODUCTS)

Products must not duplicate canonical content. Create **relative symlinks** into this folder.

**Example (BWB‑Q100)**

```
PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/<DOMAIN>/ata/<ATA> → ../../../../../../2-DOMAINS-LEVELS/<DOMAIN>/ata/<ATA>
```

If the ATA is **shared** with other domains, product‑side overlays remain symlinks to `<DOMAIN>` canonical, with additional overlay assets kept in the consuming domain's product tree and referenced via cross‑refs.

---

## 8) Evidence & QS

All critical artifacts should have **QS (Quantum Seal) hashes** recorded in `governance/baselines/` and linked from release notes. Use UTCS IDs consistently in file headers/front‑matter.

---

## 9) Examples

* **ATA‑32 under MMM** (Landing Gear):

  * Canonical path: `2-DOMAINS-LEVELS/MMM/ata/ATA-32/`
  * Product symlink (BWB‑Q100): `PRODUCTS/.../MMM/ata/ATA-32 → ../../../../../../2-DOMAINS-LEVELS/MMM/ata/ATA-32`
  * Compliance focus: CS‑25 Subpart D, maintenance task cards, EBOM/MBOM for gear/doors/actuation.

* **ATA‑42 under IIS** (Integrated Avionics):

  * Buses/ICD in `os/design/icd/`; S1000D A429/AFDX labeling in `os/S1000D/`.

---

## 10) Conventions

* Treat this folder as **authoritative** for `<ATA>`.
* Keep **derived** or **product‑specific** files out of canonical; place them in product trees and reference via cross‑refs.
* Prefer open, verifiable formats (XML, YAML, CSV, CGM) with clear versioning.

> To initialize or repair this canonical folder and symlinks, run:
>
> ```bash
> python scripts/standardize_ata_structure.py --atas <ATA_NUMBER> --include-shared --verbose
> ```
