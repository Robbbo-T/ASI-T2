# 🚀 IDEALE.eu — Intelligence • Defense • Energy • Aerospace • Logistics • ESG

[**IDEALE.eu**](https://ideale.eu) is a federated **brand & standards** program for **verifiable critical systems**. We prioritize **evidence over assertions** and publish portable formats and vendor-neutral CI hooks.

> **Principle:** If it didn’t run in **CI**, it doesn’t count as **evidence**.

- **Public framework:** [**IDEALE Evidence Framework (IEF)**](#ideale-evidence-framework-ief)  
- **Primary sector profile:** [**TFA (Aerospace)**](#tfa--aerospace-domain-profile)  
- **Reference implementation (code/templates):** [**ASI-T2**](#asi%E2%80%91t2-reference-implementation)

---

## 📚 Quick Nav

- [What is IDEALE?](#what-is-ideale)
- [Naming Canon](#naming-canon)
- [IDEALE Evidence Framework (IEF)](#ideale-evidence-framework-ief)
- [Sector Profiles](#sector-profiles)
- [ASI-T2 (Reference Implementation)](#asi%E2%80%91t2-reference-implementation)
- [Programs & Families (Aerospace-first)](#programs--families-aerospace-first)
- [Evidence Objects](#evidence-objects)
- [Conformance Ladder](#conformance-ladder)
- [Roadmap Phases](#roadmap-phases)
- [Contact & Pilots](#contact--pilots)
- [Link Map](#link-map-for-clustered-keywords)

---

## What is IDEALE?

**IDEALE.eu** is an open **brand + standards** initiative that enables **verifiability** across Europe’s strategic sectors (Intelligence, Defense, Energy, Aerospace, Logistics, ESG). The specifications let teams produce **verifiable artifacts** that travel between tools and organizations without vendor lock-in.

> **Bridge flow (TFA canon):** **QS→FWD→UE→FE→CB→QB**.

---

## Naming Canon

**Entity types**

- **Family** — related products sharing a common baseline (e.g., **AMPEL360**)  
- **Model** — concrete configuration within a family (e.g., **BWB-Q100**)  
- **Variant** — specialization of a model (e.g., **AMPEL360 PLUS**)  
- **Program** — sustained line of work (e.g., **INFRANET**, **HYDROBOTS** under GAIA-AIR)

**Canonical truths**

- **AMPEL360** is a **family of aircraft models**. **BWB-Q100** is a **model**; **AMPEL360 PLUS** is a **variant** (Space Tourism).  
- **GAIA** is a **family of multi-domain robotic systems** with sub-families **GAIA-AIR/SEA/SPACE**. **HYDROBOTS** is a **program under GAIA-AIR**.  
- **QAIM-2** is the **CAx ↔ QOx bridge**, emitting **signed attestations** consumable by **UTCS/CXP**.  
- **INFRANET** groups **infrastructure & OS** products (e.g., **AQUA_OS_AIRCRAFT**, **LH2_CORRIDOR**).

---

## IDEALE Evidence Framework (IEF)

A reusable **evidence & verification layer** adoptable in stages.

- **Manifests:** **UTCS** (UiX Threading Context/Content/Cache & Structure/Style/Sheet) / **CXP** (Context Exchange Profile)  
- **SBOM:** **SPDX 2.3 JSON**  
- **Verify & Replay:** policy-pinned verification, hash-chained logs, reproducibility  
- **Badges:** human-readable status + machine endpoints for procurement/regulatory portals

**Open evidence flow (UTCS → SPDX → Verify → Badge)**

1) **UTCS/CXP** anchor who/what/where/when/why.  
2) **SPDX SBOM** records components & licenses.  
3) **Verify (CI)** enforces policy and emits a replayable log.  
4) **Badge** publishes status and links to evidence blobs.

---

## Sector Profiles

Profiles specialize IEF per regulatory domain. First up:

### TFA — Aerospace Domain Profile

- Aligns **UTCS** fields to aviation semantics (ATA, safety, maintainability)  
- Adds aerospace-specific **policy pins** and **conformance gates**  
- Ships **reference badges** and **regulatory report layouts**

---

## ASI-T2 (Reference Implementation)

**ASI-T2** is the **reference repository** showing how to wire IEF in a real organization (templates, workflows, examples).

- **Bundle:** `UTCS_BUNDLE/` (manifests, attestations)  
- **Docs:** `WHITEPAPERS/` (architecture & interfaces)  
- **Profiles:** TFA (aerospace)  
- **Evidence:** `sbom/`, `badges/`, `.github/workflows/` (Verify)

> Treat it as a **living reference**: copy what you need; keep your own governance.

---

## Programs & Families (Aerospace-first)

- <a id="ampel360"></a>**AMPEL360 — Family of aircraft models**  
  **Sub-family & models:** **AMPEL360 Air Transport** → **BWB-Q100** (model).  
  **Variant:** **AMPEL360 PLUS** (Space Tourism). Evidence wiring: **UTCS → SPDX → Verify → Badge** aligned to **ATA**.

- <a id="gaia-systems"></a>**GAIA — Family of multi-domain robotic systems**  
  **Sub-families:** **GAIA-AIR** (UAV/UAM; includes **ETHICS-EMPATHY-UAV**, **HYDROBOTS**), **GAIA-SEA** (e.g., **GAIA-SOUND**), **GAIA-SPACE** (e.g., **ORBITAL-MACHINES**, **SAT-CONSTELLATIONS**). All expose **IEF badges** for readiness and safety lifecycle states.

- <a id="qaim-2"></a>**QAIM-2 — CAx ↔ QOx bridge**  
  Integrates classical engineering pipelines with quantum/hybrid optimization and generates **signed attestations** for **UTCS/CXP** replay.

- <a id="hydrobots"></a>**HYDROBOTS — (under GAIA-AIR)**  
  Program for autonomous platforms with **evidence-first** maintenance, safety logs, and provenance manifests (lives in `GAIA-AIR/HYDROBOTS`).

- **INFRANET — Infrastructure & OS**  
  Includes **AQUA_OS_AIRCRAFT** (ARINC/IMA partitions, AFDX/TSN/TTE, UTCS/QS sealing) and **LH2_CORRIDOR** (H₂ infrastructure). **QAIM** also lives here as a cross-cutting bridge.

---

## Evidence Objects

- **UTCS / CXP** — machine-readable context (e.g., `UTCS/context.manifest.json`)  
- **SPDX SBOM** — generated on build/release (`sbom/`)  
- **Verify (CI)** — policy-pinned workflows under `.github/workflows/`  
- **Badge + Replay** — status + links to replayable logs (`badges/`)

### UTCS (Universal Trust Context Spec)
Defines **who/what/where/when/why**; portable, CI-friendly schemas.

### CXP (Context Exchange Profile)
Transport profile that wraps UTCS for inter-org evidence exchange.

---

## Conformance Ladder

| Level | Name         | Requirements (summary) |
|-----:|--------------|-------------------------|
| 1    | **Baseline** | Valid **UTCS** + one **SPDX** per release + visible **Badge** |
| 2    | **Replayable** | Policy-pinned **Verify** + hash-chained logs + retention policy |
| 3    | **Assured**  | Third-party attestation + sector **profile** (e.g., **TFA**) + revocation |
| 4    | **Certified** | **IDEALE Trust Mark** aligned to EU frameworks |

> Progress is **evidence-driven**; each level adds traceability without lock-in.

---

## Roadmap Phases

1. **Standards** — freeze **MVS v0.1** (UTCS/CXP schema, SPDX baseline, Verify action, Badge endpoint)  
2. **Services** — Verification-as-a-Service (SaaS), data residency, signed attestations  
3. **Trust Mark** — Levels, controls, assessor marketplace, revocation  
4. **Policy Alignment** — Map primitives to EU requirements; public-sector pilots

---

## Contact & Pilots

Interested in a 2-week pilot (Aerospace/Energy/Defense/Logistics)?

- Email: **[pilots@ideale.eu](mailto:pilots@ideale.eu)**  
- Issues: **[Open a Pilot request](https://github.com/Robbbo-T/IDEALE-IEF/issues/new?title=Pilot%3A%20Org)**

---

## Link Map (for clustered keywords)

- **IDEALE.eu** → https://ideale.eu  
- **IEF** → #ideale-evidence-framework-ief  
- **ASI-T2** → #asi%E2%80%91t2-reference-implementation  
- **TFA** → #tfa--aerospace-domain-profile  
- **UTCS** → #evidence-objects  
- **CXP** → #evidence-objects  
- **SPDX** → https://spdx.dev  
- **SBOM** → #evidence-objects  
- **Verify** → #evidence-objects  
- **Badge** → #evidence-objects  
- **AMPEL360** → #ampel360  
- **GAIA** → #gaia-systems  
- **QAIM-2** → #qaim-2  
- **HYDROBOTS** → #hydrobots


