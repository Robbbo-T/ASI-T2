---
id: ASIT2-GAIA-AIR-HYDROBOTS-DOMAINS-OV-0001
rev: 0
project: PRODUCTS/GAIA-AIR/HYDROBOTS
artifact: PRODUCTS/GAIA-AIR/HYDROBOTS/domains/README.md
llc: SYSTEMS
title: "Domains — HYDROBOTS (GAIA-AIR)"
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-01-15
maintainer: "ASI-T Architecture Team"
licenses:
  docs: "CC-BY-4.0"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
provenance:
  policy_hash: "sha256:TBD"
  model_sha: "sha256:TBD"
  data_manifest_hash: "sha256:TBD"
  operator_id: "UTCS:OP:copilot-gen"
---

# Domains — HYDROBOTS

Landing page for **engineering domains** of the HYDROBOTS hydrogen UAM/UAV program.  
Each domain follows the **CAx (classical)** → **QOx (quantum)** → **PAx (packaging)** path and organizes certification evidence under **ATA**.

> **Link policy:** relative links only; directory links end with `/`; file links include full names.

---

## Quick Navigation

- **AAA — Aerodynamics & Airframes** → [`./AAA/`](./AAA/)
  - ATA (standards) → [`./AAA/ata/`](./AAA/ata/)
  - CAx (CAD/CAE/CFD/VP) → [`./AAA/cax/`](./AAA/cax/)
  - QOx (optimization) → [`./AAA/qox/`](./AAA/qox/)
  - PAx (packaging) → [`./AAA/pax/`](./AAA/pax/)
  - Quality/Evidence → [`./AAA/quality/`](./AAA/quality/)
- **LCC — Linkages, Control & Comms** → [`./LCC/`](./LCC/)
- **EEE — Electrification & Power** → [`./EEE/`](./EEE/)
- **PPP — Propulsion & Fuel Systems** → [`./PPP/`](./PPP/)
- **CQH — Cryogenics, Quantum & H₂** → [`./CQH/`](./CQH/)
- **IIS — Integrated Intelligence & Software** → [`./IIS/`](./IIS/)
- **MEC — Mechanical Systems** → [`./MEC/`](./MEC/)
- **DDD — Digital & Data Defense** → [`./DDD/`](./DDD/)

> If a folder is not yet present, create it with a README that follows the **“Domain README pattern”** below.

---

## Domain README pattern (required in every data module)

Each `domains/<CODE>/README.md` **must** include:

1. **Front-matter (UTCS)**: `id`, `rev`, `artifact`, `llc`, `title`, `classification`, `bridge`, `ethics_guard`, `utcs_mi`, `canonical_hash`, `provenance`.
2. **Table of Contents** with anchors.
3. **Purpose & Scope** (what the domain owns; what it excludes).
4. **Breakdown & Routing** (hyperlinks):
   - `ata/` (chapter index and per-chapter routes)
   - `cax/` (CAD, CAE, CFD, VP)
   - `qox/` (QUBO/BQM, QAOA, Annealing)
   - `pax/` (OB/OFF packaging, schemas, scripts)
   - `quality/` (forms, templates, QS evidence)
5. **Interfaces** (links to sibling domains and shared constraints).
6. **Traceability & QS** (where evidence lives; forms; hashes).
7. **Revision History** table.

---

## Standard module map (applies to each domain)

```

domains/<CODE>/
├─ ata/         # Standards & compliance (ATA chapters)
├─ cax/         # CAD / CAE / CFD / VP
├─ qox/         # QUBO/BQM, QAOA, annealing specs & runs
├─ pax/         # Packaging (OB/OFF), schemas, scripts
└─ quality/     # Forms, checklists, QS/UTCS evidence

```

**Routing examples**
- ATA chapter landing → `./AAA/ata/57/README.md`
- CAE report hub → `./AAA/cax/CAE/`
- QUBO standard → `./AAA/qox/qubo/README.md`
- PAx schema → `./AAA/pax/schemas/package.schema.json`
- QS forms → `./AAA/quality/forms/`

---

## Breadcrumbs

- HYDROBOTS root → [`../`](../)  
- **You are here** → `domains/`  
- Next: pick a domain (e.g., AAA) → [`./AAA/`](./AAA/)

---

## Revision History

| Rev | Date       | Description                     | QS/UTCS Ref |
|-----|------------|---------------------------------|-------------|
| 0   | 2025-01-15 | Initial HYDROBOTS domains index | `TBD`       |

---
*HYDROBOTS • Domains index. Subject to MAL-EEM and UTCS/QS evidence policy.*
```
