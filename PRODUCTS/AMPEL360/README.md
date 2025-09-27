---
id: AMPEL360-PRODUCTS-OV-0001
project: AMPEL360
artifact: ASI-T2/PRODUCTS/AMPEL360/README.md
llc: GENESIS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.2.0
release_date: 2025-09-24
maintainer: "Robbbo-T / ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# AMPEL360 — Aerospace Manned Products Ending Line (360° circularity assurance)

This space groups **crewed AMPEL360 products** under a single, auditable hub with **360° circularity assurance** objectives and AQUA-OPEN bridges for classical→quantum extensibility.

---

## Quick navigation

- **AMPEL360_AIR_TRANSPORT** → `./AMPEL360_AIR_TRANSPORT/`
  - **BWB-Q100 (Transport Civil × Air)** → `./AMPEL360_AIR_TRANSPORT/BWB-Q100/`
    - CAD Wing Baseline (AAA→cax→CAD) → `./AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model/`
    - PAx Packaging (AAA→pax) → `./AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/pax/`
      - On-Board Packaging → `./AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/pax/OB/`
      - Off-Board Packaging → `./AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/pax/OFF/`
    - Master Params → `./AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model/master_model/params.yaml`
    - (Optional) ATA-57 S1000D → `./AMPEL360_AIR_TRANSPORT/BWB-Q100/ata/57/`
- **AMPEL360_SPACE_TOURISM** → `./AMPEL360_SPACE_TOURISM/`
  - **PLUS (Space Tourism Aircraft AMPEL360PLUS)** → `./AMPEL360_SPACE_TOURISM/PLUS/`
- **Evidence & QS anchors** → see [Evidence & Provenance](#evidence--provenance-qsutcs).

---

## Scope & objectives

**Scope:** Manned AMPEL360 products and their configurations, artifacts, and certification evidence across the lifecycle.

**Objectives:**
- Verifiable sustainability (SIM KPIs) with circularity-by-design.
- Certifiable safety & compliance (CS-25 family, ARP4754A/4761).
- Reproducible data flows across **CB→QB→UE→FE→FWD→QS** with UTCS/DET provenance.

---

## Product family (current)

- **AMPEL360_AIR_TRANSPORT** — Air transport products *(active)*
  - **BWB-Q100** — Baseline passenger configuration *(active)*  
    Path: `./AMPEL360_AIR_TRANSPORT/BWB-Q100/`
- **AMPEL360_SPACE_TOURISM** — Space tourism products *(in development)*
  - **PLUS** — Space Tourism Aircraft AMPEL360PLUS *(in development)*
    Path: `./AMPEL360_SPACE_TOURISM/PLUS/`

_Reserved:_ additional variants can be added as subfolders under each product line following the same governance pattern.

---

## Directory layout (product hub)

```

ASI-T2/PRODUCTS/AMPEL360/
├─ README.md                                    # This file (UTCS-headed)
├─ AMPEL360_AIR_TRANSPORT/                      # Air transport products
│  ├─ README.md                                 # Air transport hub
│  └─ BWB-Q100/                                 # Product instance (baseline)
│     ├─ domains/AAA/                          # Engineering domain AAA
│     │  ├─ cax/CAD/wing\_baseline\_model/...  # Classical CAD models
│     │  ├─ qox/ ...                           # Quantum optimization
│     │  └─ pax/                               # Packaging & Applications
│     │     ├─ OB/                             # On-Board (ARINC 653/IMA, A661, A664)
│     │     │  ├─ manifests/                   # Partition manifests
│     │     │  ├─ sbom/                        # SPDX/CycloneDX SBOM
│     │     │  └─ certificates/                # Signatures, X.509 chains
│     │     ├─ OFF/                            # Off-Board (OCI/edge/cloud)
│     │     │  ├─ oci/                         # OCI descriptors/attestations
│     │     │  └─ sbom/                        # Container SBOM
│     │     ├─ schemas/                        # JSON schemas for manifests
│     │     └─ scripts/                        # Validators/linters
│     ├─ QS/ ...                               # Evidence, signatures, KPIs
│     └─ ata/57/ ...                           # S1000D/ATA seeds (optional)
└─ AMPEL360_SPACE_TOURISM/                      # Space tourism products
   ├─ README.md                                 # Space tourism hub
   └─ PLUS/                                     # Space tourism aircraft
      ├─ domains/ ...                          # Engineering domains (to be developed)
      ├─ QS/ ...                               # Evidence, signatures, KPIs (to be developed)
      └─ ata/ ...                              # S1000D/ATA seeds (to be developed)

```

---

## Domain → Process → ATA entry points

**Air Transport (BWB-Q100):**
- **AAA / cax / CAD** (geometry & structures)  
  `./AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model/`
- Additional entries (add as they materialize):  
  **PPP / cax / CAE** (structures), **QQQ / cax / CFD** (aero), **ATA-57** publications.

**Space Tourism (PLUS):**
- Domain structure in development following BWB-Q100 pattern
- Target domains: **AAA**, **PPP**, **CCC**, **EEE**, **LCC**, **MEC**, **IIS**

---

## Sustainability KPI pack (SIM)

Track at product level; store under **QS** with UTCS headers:

- **Core:** CO₂e/RPK, Energy/RPK, LCA (cradle→grave), Circularity Index (materials reuse), SAF/H₂ share.
- **Operations:** NOx vs ref, noise margins, maintenance waste, supply-chain risk.
- **Governance:** audit trail of assumptions, datasets, and model versions.

> Suggested path: `./BWB-Q100/QS/kpis.yaml` (UTCS-MI v5.0 + `canonical_hash`).

---

## Compliance & certification stack

- **Airworthiness:** CS-25, ARP4754A (development assurance), ARP4761 (safety).  
- **Avionics SW/HW (if applicable):** DO-178C / DO-254.  
- **Data & docs:** S1000D Issue 6.0, ATA Spec mappings.  
- **Provenance:** UTCS/DET anchors; reproducible pipelines with CI logs archived in QS.

---

## Evidence & Provenance (QS/UTCS)

- **DET anchor:** Set `canonical_hash` for each UTCS-headed artifact at release cut (SHA-256 of content).  
- **Signatures:** Store EIP-712-style signature blocks in `./BWB-Q100/QS/` alongside artifact manifests.  
- **Reproducibility:** Derived geometry/meshes must trace to `master_model/params.yaml` with deterministic build steps.

---

## CI & automation hooks

- **Validation:** CI should run schema + grammar checks on both canonical and product-scoped paths, e.g.:
  - Air Transport: `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model`
  - Space Tourism: `PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/...` (as developed)
- **Gates:** UTCS front-matter presence; YAML/JSON schema; path grammar; QS signature verification (when enabled).
- **Outputs:** Attach CI logs as QS evidence for release tags.

---

## Versioning & change control

- Bump `version` semantically (MAJOR.MINOR.PATCH) on governance changes.  
- Update `release_date` and recompute `canonical_hash`.  
- Record deltas in **Changelog** and create a signed QS manifest for each release.

---

## Contribution & PR conventions

- Branch naming: `feat/…`, `fix/…`, `docs/…`, `ci/…`.  
- Commit example:  
  `feat(AAA/CAD): scaffold wing_baseline_model with UTCS headers and param packs`
- PR checklist: UTCS headers, schema pass, CI green, QS updates (when relevant).

---

## Contacts & ownership

- **Maintainer:** Robbbo-T / ASI-T Architecture Team  
- **Domain leads:** 
  - Air Transport (BWB-Q100): listed in `./AMPEL360_AIR_TRANSPORT/BWB-Q100/OWNERS.md` if present
  - Space Tourism (PLUS): to be assigned as development progresses

---

## Changelog

- **0.2.0 — 2025-09-24**  
  Restructured AMPEL360 folder with two main product lines:
  - AMPEL360_AIR_TRANSPORT (moved BWB-Q100 here)
  - AMPEL360_SPACE_TOURISM (added new PLUS space tourism aircraft)
- **0.1.0 — 2025-09-23**  
  Initial AMPEL360 product hub with links to BWB-Q100 CAD baseline, governance sections, and QS/UTCS guidance.
```


