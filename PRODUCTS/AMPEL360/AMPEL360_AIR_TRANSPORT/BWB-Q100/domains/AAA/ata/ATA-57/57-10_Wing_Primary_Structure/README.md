---
id: ATA-57-10-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-10_Wing_Primary_Structure/README.md
llc: SYSTEMS
title: "ATA-57-10: Wing Primary Structure — BWB-Q100"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# ATA-57-10 — Wing Primary Structure (BWB-Q100)

Primary load-bearing structure: wingbox (skins, spars, ribs, stringers), wing-to-centerbody attachments, primary joints, and structural lightning provisions.  
**Golden rule:** knowledge lives here (ATA); compute lives in **CAX/QOX**; deployable packages in **PAx**.

---

## Quick Nav

- [Scope](#scope)
- [Directory Breakdown (Pattern-Compliant)](#directory-breakdown-pattern-compliant)
- [Interfaces & Dependencies](#interfaces--dependencies)
- [Mandatory Forms (ATA-20) — Links](#mandatory-forms-ata-20--links)
- [Configuration Breakdown — CBS → CI → CO](#configuration-breakdown--cbs--ci--co)
- [Acceptance & Inspection](#acceptance--inspection)
- [Evidence & QS](#evidence--qs)
- [Change Control](#change-control)

---

## Scope

**Includes**
- Wingbox: upper/lower skins, front/rear spars, ribs, stringers, joints, fittings.
- Wing-to-fuselage/centerbody attachments and primary load paths.
- Composite/metallic hybrid details, lightning strike protection (structural provisions).
- Structural repairs baseline rules (link to chapter-specific repair DMs under S1000D).

**Excludes**
- Moveable surfaces (57-20), high-lift (57-30), systems routings (referenced via ICDs).

---

## Directory Breakdown (Pattern-Compliant)

> **Pattern:** 4-digit subchapter folder with S1000D below it. CAX/QOX artifacts are *referenced*, not stored here.

```
57-10_Wing_Primary_Structure/
├── README.md
├── S1000D/                         # DMRL/BREX/DMs/IPD/IETP assets (controlled)
│   ├── DMRL/
│   ├── BREX/
│   ├── DMC/
│   │   ├── PR/                     # Procedures (R/I, inspections, repairs)
│   │   ├── DS/                     # Descriptive/structure data
│   │   ├── IPD/                    # Illustrated Parts Data (figures/items)
│   │   └── IR/                     # Illustrated Repairs (if applicable)
│   └── pubs/
├── compliance/                     # Substantiation & regulatory evidence (indexes only)
│   ├── allowables/
│   │   └── index.md
│   ├── loads/
│   │   └── index.md
│   └── stress/
│       └── index.md
├── icd/                            # Interfaces with adjacent chapters/systems
│   ├── ICD-57-10-53_Fuselage_Attachments.md
│   ├── ICD-57-10-57-20_Control_Surfaces.md
│   └── ICD-57-10-57-50_Systems_Provisions.md
├── evidence/                       # Links to results (no heavy data); UTCS/QS anchors
│   ├── coupons/
│   │   └── index.md
│   ├── ndt/
│   │   └── index.md
│   └── tests/
│       └── index.md
├── contracts/                      # JSON schemas/ICDs for manifests & acceptance
│   ├── ICD-AAA-ATA-57-10.md
│   └── schemas/
│       ├── acceptance.metric.schema.json
│       ├── attachment.fitting.schema.json
│       ├── fastener.set.schema.json
│       ├── joint.schema.json
│       └── laminate.stack.schema.json
└── io/
    └── routing.manifest.yaml       # Inputs/outputs references (CAX/QOX/PAx/ATA linkage)
```

> **References out to compute/deploy (examples, do not store here):**  
> - `../../../cax/CAD/WingBox_v*/` (OML, structural defs)  
> - `../../../cax/FEA/WingBoxLoads_v*/` (loads, margins)  
> - `../../../qox/opt/fastener_layout/` (QUBO/BQM runs, reports)  
> - `../../../pax/OB|OFF/` (packages, SBOM, signatures)

---

## Interfaces & Dependencies

- **ATA-53** (Fuselage/Centerbody): attachment fittings, load transfer, tolerances.  
- **ATA-57-20/57-30** (Moveables/High-lift): hinge/actuator hard-points, seal lands.  
- **ATA-20** (Standard Practices): fastening, bonding, sealing, material handling, EMI/bonding.  
- **ATA-04 (IPD)**: figures/items for spares; see 360IPCirq linkage for interchangeability/reusability.

---

## Mandatory Forms (ATA-20) — Links

Use canonical forms; do **not** duplicate in ATA-57:

- Composite Fastening — `../../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`  
- Adhesive Bonding — `../../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`  
- Cabin Integrity / Leak Test — `../../ATA-20/20-20_Sealing_and_Pressurization/forms/FORM-QA-20-20-01_Cabin_Integrity_Leak_Test.md`  
- Material Handling & OOC Log — `../../ATA-20/20-30_Material_Handling/forms/FORM-QA-20-30-01_Material_Handling_OOC_Log.md`  
- Bonding / EMI Continuity — `../../ATA-20/20-40_Electrical_Bonding/forms/FORM-QA-20-40-01_Bonding_EMI_Continuity.md`

---

## Configuration Breakdown — CBS → CI → CO

### L0 — Capability (System)
**CI-0.0** `57-10_Wing_Primary_Structure` — Primary static structure for BWB-Q100 wing/centerbody.

### L1 — Major Configuration Groups
**CI-1.1 Structural Members** (skins, spars, ribs, stringers)  
**CI-1.2 Joints & Fasteners** (mechanical/adhesive hybrid)  
**CI-1.3 Attachments** (to fuselage/centerbody & system hard-points)  
**CI-1.4 Lightning/EMI Provisions** (structural LSP/grounding)  
**CI-1.5 Loads & Allowables** (design envelope, material allowables)  
**CI-1.6 Repairs** (standard structural repairs catalog)  
**CI-1.7 Effectivity & Options** (block/variant rules)  
**CI-1.8 Evidence & QA** (coupons, NDT, test traces, ATA-20 forms)  
**CI-1.9 Schemas & Interfaces** (contracts, manifests, ICDs)

### L2 — Subsystems & Containers

#### CI-1.1 Structural Members
- **CI-2.1** Skins (upper/lower) — laminate stacks, thickness maps.  
- **CI-2.2** Spars (front/rear) — web/cap build-ups, taper laws.  
- **CI-2.3** Ribs — lightening holes, cutouts, local reinforcements.  
- **CI-2.4** Stringers/Integrals — hat/T/I/omega, runouts, joggles.

#### CI-1.2 Joints & Fasteners
- **CI-2.5** Mechanical joints — hole classes, countersinks, fastener sets.  
- **CI-2.6** Adhesive bonds — bondline control, surface prep, cure profiles.  
- **CI-2.7** Hybrid joints — co-bond/secondary bond with fasteners.

#### CI-1.3 Attachments
- **CI-2.8** Fittings — lugs/clevises, frames interface.  
- **CI-2.9** Hard-points — hinges, actuator brackets, system provisions.

#### CI-1.4 Lightning/EMI Provisions
- **CI-2.10** LSP meshes/foils — coverage, bonding, terminations.  
- **CI-2.11** Down-bonds — resistance targets, inspection points.

#### CI-1.5 Loads & Allowables
- **CI-2.12** Loads sets — limit/ultimate, fatigue spectra, gust/taxi/pressurization.  
- **CI-2.13** Allowables — material/joint allowables, temperature/humidity knock-downs.

#### CI-1.6 Repairs
- **CI-2.14** Standard repairs — scarf/patch, core replacement, insert repairs.  
- **CI-2.15** Acceptance limits — post-repair metrics (UT/thermography/margins).

#### CI-1.7 Effectivity & Options
- **CI-2.16** Effectivity sets — MSN ranges, blocks.  
- **CI-2.17** Options — variant flags (e.g., fuel volume option, LSP class).

#### CI-1.8 Evidence & QA
- **CI-2.18** Coupons & tests — ply drop, open/filled hole, bearing/bypass.  
- **CI-2.19** NDT plans & results — UT, tap-test, thermography, radiography.  
- **CI-2.20** QA forms linkage — ATA-20 mandatory forms.

#### CI-1.9 Schemas & Interfaces
- **CI-2.21** JSON schemas — joint, laminate stack, fastener set, fitting, acceptance metric.  
- **CI-2.22** ICDs — with ATA-53 / 57-20 / 57-50.  
- **CI-2.23** Routing manifest — inputs/outputs linkage, UTCS/QS anchors.

### L3 — Leaf Configurable Objects (CO)

> Atomic definition points for design/manufacturing/inspection; version-pinned & sealed.

1. **Skin Panel (CO-3.1)** → `panel_id`, `geometry_ref`, `laminate_code`, `thickness_map`, `material_spec`, `cure_profile_ref`, `effectivity_expr`
2. **Spar Segment (CO-3.2)** → `spar_id`, `segment_sta`, `web_thk`, `cap_stack`, `cutout_defs[]`, `material_spec`
3. **Rib (CO-3.3)** → `rib_id`, `station`, `web_thk`, `flange_stack`, `lightening_holes[]`, `stiffener_refs[]`
4. **Stringer Run (CO-3.4)** → `run_id`, `type(hat/T/I/omega)`, `pitch`, `runout_law`, `joggle_defs[]`, `laminate_code`
5. **Joint Definition (CO-3.5)** → `joint_id`, `type(mech/adhesive/hybrid)`, `members[]`, `load_class`, `env_class`, `acceptance_ref`
6. **Fastener Set (CO-3.6)** → `set_id`, `fastener_code`, `dia`, `grip`, `material`, `finish`, `torque_ref`, `hole_class`, `countersink_depth`
7. **Adhesive Bondline (CO-3.7)** → `bond_id`, `adhesive_code`, `target_thk`, `control_method(scrim/beads/shim)`, `surface_prep`, `cure_profile_ref`, `coupon_req{Y/N}`
8. **Hybrid Joint Rule (CO-3.8)** → `rule_id`, `fastener_set_ref`, `bondline_ref`, `sequencing`, `sealant_req{Y/N}`
9. **Attachment Fitting (CO-3.9)** → `fitting_id`, `type(lug/clevis)`, `material`, `bushings[]`, `pin_size`, `tolerance_class`, `icd_ref`
10. **Hard-point (CO-3.10)** → `hp_id`, `purpose(hinge/actuator/service)`, `load_limit`, `stiffener_ties[]`, `icd_ref`
11. **LSP Mesh/Strip (CO-3.11)** → `lsp_id`, `coverage_area`, `mesh_spec`, `bond_resistance_target`, `termination_points[]`
12. **Down-bond (CO-3.12)** → `bond_id`, `location`, `target_resistance_mΩ`, `test_method`, `rework_rule_ref`
13. **Load Case (CO-3.13)** → `case_id`, `description`, `limit/ultimate`, `temperature/RH`, `spectra_ref`
14. **Allowable Entry (CO-3.14)** → `allow_id`, `type(material/joint)`, `value`, `knockdowns`, `method(S-Basis/A-/B-)`, `source`
15. **Standard Repair (CO-3.15)** → `repair_id`, `type(scarf/patch/core/insert)`, `ply_schedule`, `adhesive_ref`, `acceptance_ref`, `effectivity_expr`
16. **Acceptance Metric (CO-3.16)** → `metric_id`, `feature(leak_rate/bond_void/flushness/bond_resistance)`, `threshold`, `method`, `evidence_ref`
17. **Effectivity Rule (CO-3.17)** → `expr`, `start`, `end`, `options[]`, `exclusions[]`
18. **Option Flag (CO-3.18)** → `option_code`, `name`, `dependencies[]`, `exclusions[]`
19. **Tool Ref (CO-3.19)** → `tool_code`, `description`, `alt_tool[]`, `calibration_due`
20. **Material Ref (CO-3.20)** → `mat_code`, `spec`, `batch_required{Y/N}`, `shelf_life`, `storage_class`
21. **Torque Parameter (CO-3.21)** → `fastener_code`, `torque_Nm`, `angle_deg?`, `lube_cond`, `witness_req{Y/N}`  *(Form link)*
22. **Cure Profile (CO-3.22)** → `profile_id`, `temp/time/pressure`, `vacuum_req`, `ramp/soak`, `log_req`  *(Form link)*
23. **Sealant Parameter (CO-3.23)** → `sealant_code`, `bead_size`, `surface_prep`, `WBT_req{Y/N}`
24. **Evidence File Ref (CO-3.24)** → `type(OOC/torque/cure/NDT/bond/EMI)`, `uri`, `sha256`, `form_link`
25. **QA Form Link (CO-3.25)** → `form_id`, `rev`, `path`, `required_in_steps[]`
26. **QS/UTCS Anchor (CO-3.26)** → `canonical_hash`, `sbom_uri`, `signer`, `timestamp`

> **Schemas** for COs are pinned in `contracts/schemas/*.schema.json` and referenced from `io/routing.manifest.yaml`.

---

## Acceptance & Inspection

| Feature / Metric                   | Minimum Requirement (unless drawing/spec overrides)          | Method                          |
| ---                                | ---                                                          | ---                             |
| Hole roundness                     | ≤ 0.03 mm                                                   | Plug/bore gauge, CMM            |
| Countersink depth/finish           | ±0.05 mm; no fiber breakout; Ra ≤ 3.2 µm                     | Depth gauge, visual             |
| Fastener head flushness            | 0.00 to +0.10 mm proud (typical)                             | Flushness gauge                 |
| Bondline thickness                 | Per spec (typ. 0.20–0.30 mm)                                 | Shims/coupons                   |
| Bond voids                         | No void > 1 mm²; cumulative area < 0.5%                      | UT/thermography                 |
| Bond resistance (down-bonds)       | Per location class (ref. CO-3.12)                            | Bond meter                      |
| Post-repair NDT                    | No critical indications; per CO-3.16 acceptance              | UT/RT/thermography              |

> When generic limits conflict with model/drawing, the **model/drawing governs**.

---

## Evidence & QS

- **Forms (linked):**  
  - Composite Fastening → `../../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`  
  - Adhesive Bonding → `../../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`  
  - Bonding/EMI Continuity → `../../ATA-20/20-40_Electrical_Bonding/forms/FORM-QA-20-40-01_Bonding_EMI_Continuity.md`
- **Traceability:** material lots, OOC timers, torque/cure logs, NDT results → linked via **CO-3.24/CO-3.26** and sealed with **UTCS/QS**.

---

## Change Control

Any deviation from ATA-20 or drawing/spec must be approved by **M&P** and **MRB** and recorded here. Releases follow PDM-PLM CNs; manifests and signatures are updated under `io/` and `evidence/`.

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
