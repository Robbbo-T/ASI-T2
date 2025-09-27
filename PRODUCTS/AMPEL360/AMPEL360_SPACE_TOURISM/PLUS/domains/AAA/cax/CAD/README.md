---
id: ASIT-PLUS-AAA-CAX-CAD-OV-0001
rev: 1
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/cax/CAD/README.md
llc: SYSTEMS
title: "AAA — CAx/CAD: Space Vehicle Computer-Aided Design (AMPEL360 PLUS)"
configuration: baseline
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "0.2.0"
release_date: 2025-09-27
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

# AAA/CAx/CAD — Space Vehicle Computer-Aided Design (AMPEL360 PLUS)

Geometry design, structural modeling, and thermal-protection integration for **AMPEL360 PLUS** suborbital space tourism vehicles.

---

## 0) Path Root (TFA)
`PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/cax/CAD/`

---

## 1) Process Overview
Computer-aided design flows for **space-vehicle OML (outer-mold-line)**, **primary/secondary structure**, and **TPS** (thermal protection systems), with manufacturability and safety constraints for ascent, micro-g profiles, reentry, and landing.

**Objectives**
- Certifiable geometry baselines (traceable to ATA & S1000D where applicable).
- MDO-friendly parametrics (CFD/CAE/thermal co-design).
- Clean **CAx → QOx** transition hooks (QAIM-2).

---

## 2) Directory Map (Domain → Process → Assets)

```

CAD/
├── geometry/                 # Parametric OML, fairings, windows, doors, hatches
│   ├── models/               # Native CAD (CATIA/NX/Fusion) - not tracked in Git if binary
│   ├── exports/              # STEP/IGES/Parasolid for CAE/CFD
│   └── metadata/             # \*.cad.json (see schema)
├── structure/                # Frames, ribs, spars, longerons, fittings
│   ├── topology/             # Topology candidates (lattice, truss, ribs)
│   └── joints/               # Joints/fasteners interfaces
├── tps/                      # Tiles/panels/blankets, seams & seals
│   ├── layout/               # Panelization maps, tiling indices
│   └── materials/            # RCC/CMC/ABLATOR specs (refs only)
├── interfaces/               # Seats, restraints, hatches, docking, landing gear
├── mdo/                      # MDO configs (CFD/FEA coupling), design spaces
├── qox_bridge/               # QUBO/BQM encodings, QAIM-2 configs
│   └── problems/             # TPS tiling, joint placement, layout selection
├── pax/                      # Packaging (OB/OFF), schemas, scripts (see §7)
│   ├── OB/manifests/
│   ├── OFF/oci/
│   ├── schemas/
│   └── scripts/
├── schemas/                  # JSON schemas (cad_manifest.schema.json, qox_problem.schema.json)
├── scripts/                  # Validators (naming, links, schema validation)
└── README.md                 # (this file)

```

---

## 3) Key Activities

### 3.1 Design Development
- Space-vehicle geometry for suborbital profiles (ascent/reentry visibility constraints).
- TPS design & integration (tiles/panels/blankets, seals, RCC/CMC).
- Structural topology under ascent/reentry/landing load envelopes.
- Passenger safety interfaces (hatches, seats, restraints, life-support paths).

### 3.2 Optimization Targets
- **Aerodynamics:** OML smoothness & control authority in high-α reentry.
- **Structures:** Mass minimization with cert margins & load paths.
- **Thermal:** TPS performance, maintainability, refurbishment cost.
- **Ops:** Turn-time and inspection accessibility.

### 3.3 Integration Points
- **CFD:** mesh-ready exports + boundary/trajectory tags.
- **CAE:** laminate/metallic stacks, joints, thermal-structural coupling.
- **Manufacturing:** space-grade processes & allowable databases.
- **IETP/S1000D:** link practices (ATA-20), structure (ATA-57) via references.

---

## 4) CAx → QOx Transition (QAIM-2)

**Classical pain:** combinatorial layouts (tiles, ribs, joints), conflicting multi-objective constraints (thermal/weight/maintainability).  
**Quantum opportunity:** encode discrete choices as **QUBO/BQM**, solve with **QAOA/Annealing**, hybrid-loop back to CAE/CFD.

### 4.1 QUBO Seeds (examples)
1. **TPS Panel Placement:** binary `x_{i}` for tile i; costs: thermal margin, weight, cut count, seam length; constraints: coverage, max panel size.
2. **Structural Topology:** binary `y_{e}` for element e; objectives: compliance, buckling reserve, manufacturability; constraints: connectivity, symmetry.
3. **Control-Surface Layout:** `z_{k}` for candidate hinge lines; objectives: moment authority in reentry envelope; constraints: interference, clearance.
4. **Landing Gear Footprint:** `g_{p}` for gear location pattern p; objectives: tip-back margin, runway load limits; constraints: volume, CG window.

See `qox_bridge/problems/` for machine-readable definitions.

---

## 5) Deliverables

### 5.1 Design Artifacts
- Parametric CAD baselines (CATIA/NX/Fusion) → **exports/** (STEP/IGES/XT).
- TPS panelization drawings + material stacks.
- Structural topology candidates + joint catalogs.
- Mass properties & CG envelopes per mission segment.

### 5.2 QOx Integration
- QUBO specs (`*.qubo.json`) and hybrid loop configs.
- Convergence plots, sensitivity maps, and pareto fronts.
- Reproducible notebooks (text-only metadata kept; binaries out-of-repo).

---

## 6) Space Tourism Considerations
- **Passenger Safety:** emergency egress, restraint load paths, cabin pressure/TPS interface, human-rated factors.
- **Reusability:** turnaround refurb thresholds, NDI access (bondlines/seams).
- **Thermal Comfort:** TPS + internal insulation, heat-soak transients, cabin gradients.
- **Landing Performance:** autonomous landing interfaces, ground handling envelopes.

---

## 7) PAx — Packaging & Evidence

**Structure**
```

pax/
├── OB/manifests/partition.example.yaml     # If any OB visualisation/sim tools ship to EFB/LRU
├── OFF/oci/cad-ci.exporter.yaml            # OCI image descriptors/attestations
├── schemas/package.schema.json             # For OB/OFF manifests
└── scripts/validate_pax.py                 # CI validator

```

**Quality**
- **SBOM mandatory:** CycloneDX/SPDX for any distributed tool/image.
- **Signatures:** cosign + in-toto attestations (SLSA-L3 intent).
- **UTCS/QS:** stamp `canonical_hash` at release; propagate to DMs that consume CAD views.

---

## 8) Naming & Metadata Conventions

### 8.1 File naming
```

<vehicle>-<module>-<feature>-<rev>.<ext>
PLUS-OML-window-A02.step
PLUS-TPS-tiling-v05.json
PLUS-STRUCT-topoRibs-2025Q3.iges

```

### 8.2 CAD Manifest (JSON)
Schema: `schemas/cad_manifest.schema.json`

```json
{
  "$schema": "../../schemas/cad_manifest.schema.json",
  "id": "PLUS-OML-A02",
  "vehicle": "AMPEL360_PLUS",
  "kind": "OML",
  "rev": "A02",
  "exports": [
    {"path": "../exports/PLUS-OML-A02.step", "format": "STEP", "units": "mm"},
    {"path": "../exports/PLUS-OML-A02.iges", "format": "IGES", "units": "mm"}
  ],
  "refs": {
    "ata_practices": ["../../ata/ATA-20/S1000D/data_modules/descriptive/DMC-PLS1-A-20-10-00-00A-040A-D-EN-US.xml"],
    "ata_structures": ["../../../../ata/ATA-57/S1000D/..."]
  },
  "utcs": {
    "canonical_hash": "TBD",
    "provenance": "ASIT-PLUS-AAA-CAX-CAD-OV-0001"
  }
}
```

---

## 9) QOx Problem Spec (JSON)

Schema: `schemas/qox_problem.schema.json`

```json
{
  "$schema": "../../schemas/qox_problem.schema.json",
  "id": "PLUS-TPS-TILING-QUBO-001",
  "goal": "TPS panel placement for reentry segment R1",
  "variables": {
    "x_i": {"count": 480, "domain": "binary", "meaning": "tile selection"}
  },
  "objective": [
    {"term": "thermal_margin", "weight": -2.0},
    {"term": "mass", "weight": 1.0},
    {"term": "seam_length", "weight": 0.5},
    {"term": "maintainability", "weight": -0.3}
  ],
  "constraints": [
    {"type": "coverage", "weight": 8.0},
    {"type": "max_panel_size", "weight": 4.0},
    {"type": "no_conflict", "weight": 6.0}
  ],
  "bridge": "CAx→QOx (QAIM-2)",
  "roundtrip": {
    "exports": ["../../geometry/exports/PLUS-OML-A02.step"],
    "validation": ["CAE/thermal", "CFD/aero"]
  }
}
```

---

## 10) CI / Pre-Commit

Add these to repo CI and local hooks:

```bash
# Validate JSON schemas (cad manifests, qox problems)
python scripts/validate_json.py CAD/schemas CAD/**/metadata CAD/**/qox_bridge/problems

# Check links (relative paths to ATA DMs, schemas)
python scripts/link_check.py CAD

# Enforce naming (PLUS-*)
python scripts/naming_guard.py CAD

# PAx validation
python CAD/pax/scripts/validate_pax.py CAD/pax
```

> **Policy gates:** Fail closed on missing schema, broken links, or absent `canonical_hash` at release.

---

## 11) Cross-References (ATA/S1000D)

* **ATA-20 (Standard Practices—Airframe):** torque, sealants, bonding
  `../../ata/ATA-20/` → BREX & descriptive DMs (no duplication here).
* **ATA-57 (Wings/Primary Structure):** structure interfaces to PLUS lifting body.
  `../../ata/ATA-57/` (when available).
* **IETP Navigation:** DMRL consumes stable exports (STEP/IGES) and hyperlinks back to CAD manifest IDs.

---

## 12) Governance & Ethics

* **MAL-EEM:** respect safety, inclusivity, and environmental stewardship in design trade-offs.
* **UTCS/QS:** every baseline and optimization result must be reproducible and evidence-sealed.
* **Data Hygiene:** strip sensitive geometry before external sharing; publish only derived exports.

---

## 13) Mermaid — Flow Overview

```mermaid
flowchart LR
  A[CAD Parametrics\n(OML/Structure/TPS)] --> B[Exports\nSTEP/IGES/XT]
  B --> C[CFD/CAE/Thermal\nValidation]
  A --> D[QUBO Builder\n(qox_bridge)]
  D --> E[QAIM-2 Solve\n(QAOA/Annealing)]
  E --> F[Candidate Layouts]
  F --> C
  C --> G[PAx Pack\n(OB/OFF + SBOM + QS/UTCS)]
  G --> H[IETP / DMRL Refs\n(ATA-20/57)]
```

---

## 14) Changelog

* **v0.2.0 (2025-09-27):** Expanded structure, QOx schemas, PAx, CI guards, ATA cross-refs, Mermaid flow.
* **v0.1.0 (2025-09-26):** Initial draft.