---
id: ATA-57-20-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-20_Control_Surfaces/README.md
llc: SYSTEMS
title: "ATA-57-20: Control Surfaces — BWB-Q100"
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

# ATA-57-20 — Control Surfaces (BWB-Q100)

Control surfaces structure: elevons, flaperons, spoilers, their attachment mechanisms, hinges, and structural provisions for actuation.  
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
- Control surface structures: elevons, flaperons, spoilers, tabs
- Hinge mechanisms and fittings
- Actuator attachment provisions and load paths
- Control surface balance systems (mass, aerodynamic)
- Structural lightning provisions for control surfaces
- Surface finish and aerodynamic smoothness requirements
- Structural repairs baseline rules (link to chapter-specific repair DMs under S1000D)

**Excludes**
- Flight control system functionality and signaling (ATA-27)
- Hydraulic/electric actuation systems (ATA-29/24)
- Control surface aerodynamic design (referenced via ICDs)

---

## Directory Breakdown (Pattern-Compliant)

> **Pattern:** 4-digit subchapter folder with S1000D below it. CAX/QOX artifacts are *referenced*, not stored here.

```
57-20_Control_Surfaces/
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
│   ├── flutter_index.md
│   ├── loads_index.md
│   └── balance_index.md
├── icd/                            # Interfaces with adjacent chapters/systems
│   ├── ICD-57-20-27_Flight_Control_System.md
│   ├── ICD-57-20-29_Hydraulic_System.md
│   ├── ICD-57-20-57-10_Wing_Structure.md
│   └── ICD-57-20-57-30_High_Lift.md
├── evidence/                       # Links to results (no heavy data); UTCS/QS anchors
│   ├── hinge_tests_index.md
│   ├── fatigue_tests_index.md
│   └── surface_finish_index.md
├── contracts/                      # JSON schemas/ICDs for manifests & acceptance
│   ├── schemas/
│   │   ├── hinge.schema.json
│   │   ├── control_surface.schema.json
│   │   ├── actuator_attachment.schema.json
│   │   ├── balance_weight.schema.json
│   │   └── acceptance.metric.schema.json
│   └── ICD-AAA-ATA-57-20.md
└── io/
    └── routing.manifest.yaml       # Inputs/outputs references (CAX/QOX/PAx/ATA linkage)
```

> **References out to compute/deploy (examples, do not store here):**  
> - `../../../cax/CAD/ControlSurfaces_v*/` (OML, structural defs)  
> - `../../../cax/CFD/ControlSurface_Aero_v*/` (aerodynamic loads)  
> - `../../../cax/FEA/ControlSurfaceLoads_v*/` (structural loads, margins)  
> - `../../../qox/opt/hinge_layout/` (QUBO/BQM runs, reports)  
> - `../../../pax/OB|OFF/` (packages, SBOM, signatures)

---

## Interfaces & Dependencies

- **ATA-57-10** (Wing Primary Structure): attachment points, load transfer, tolerances.  
- **ATA-27** (Flight Controls): control surface kinematics, actuation requirements.  
- **ATA-29** (Hydraulic Systems): hydraulic actuation interfaces, pressure requirements.  
- **ATA-57-30** (High-Lift Devices): integration with flaps and slats.  
- **ATA-20** (Standard Practices): fastening, bonding, sealing, material handling.  
- **ATA-04 (IPD)**: figures/items for spares; see 360IPCirq linkage for interchangeability/reusability.

---

## Mandatory Forms (ATA-20) — Links

Use canonical forms; do **not** duplicate in ATA-57-20:

- Composite Fastening — `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`  
- Adhesive Bonding — `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`  
- Surface Finish & Aerodynamic Smoothness — `../../20/20-50_Surface_Finish/forms/FORM-QA-20-50-01_Surface_Finish_Aerodynamic_Smoothness.md`  
- Balance Weight Installation — `../../20/20-60_Balance_and_Alignment/forms/FORM-QA-20-60-01_Balance_Weight_Installation.md`  
- Hinge Installation & Adjustment — `../../20/20-70_Mechanical_Linkages/forms/FORM-QA-20-70-01_Hinge_Installation_Adjustment.md`

---

## Configuration Breakdown — CBS → CI → CO

### L0 — Capability (System)
**CI-0.0** `57-20_Control_Surfaces` — Control surfaces structure for BWB-Q100 wing.

### L1 — Major Configuration Groups
**CI-1.1 Control Surface Structures** (elevons, flaperons, spoilers)  
**CI-1.2 Hinge Mechanisms** (fittings, bearings, attachments)  
**CI-1.3 Actuator Attachments** (fittings, load paths, provisions)  
**CI-1.4 Balance Systems** (mass balance, aerodynamic balance)  
**CI-1.5 Surface Finish & Aerodynamics** (smoothness, sealing)  
**CI-1.6 Loads & Flutter** (design envelope, flutter characteristics)  
**CI-1.7 Repairs** (standard structural repairs catalog)  
**CI-1.8 Effectivity & Options** (block/variant rules)  
**CI-1.9 Evidence & QA** (hinge tests, fatigue tests, surface finish)  
**CI-1.10 Schemas & Interfaces** (contracts, manifests, ICDs)

### L2 — Subsystems & Containers

#### CI-1.1 Control Surface Structures
- **CI-2.1** Elevons — structure, skins, ribs, internal structure.  
- **CI-2.2** Flaperons — structure, skins, ribs, internal structure.  
- **CI-2.3** Spoilers — structure, skins, ribs, internal structure.  
- **CI-2.4** Tabs — structure, attachment mechanisms.

#### CI-1.2 Hinge Mechanisms
- **CI-2.5** Hinge Fittings — lugs, bearings, attachment points.  
- **CI-2.6** Hinge Bearings — types, materials, lubrication requirements.  
- **CI-2.7** Hinge Attachments — to wing structure, load paths.

#### CI-1.3 Actuator Attachments
- **CI-2.8** Actuator Fittings — attachment points, load paths.  
- **CI-2.9** Actuator Provisions — mounting interfaces, clearances.  
- **CI-2.10** Load Path Reinforcements — local structure reinforcement.

#### CI-1.4 Balance Systems
- **CI-2.11** Mass Balance Weights — types, locations, attachment methods.  
- **CI-2.12** Aerodynamic Balance Features — horn balance, set-back hinge.  
- **CI-2.13** Balance Adjustment Mechanisms — adjustable weights, trim tabs.

#### CI-1.5 Surface Finish & Aerodynamics
- **CI-2.14** Surface Finish Requirements — smoothness, tolerances.  
- **CI-2.15** Sealing Provisions — gap sealing, edge sealing.  
- **CI-2.16** Aerodynamic Features — vortex generators, seals.

#### CI-1.6 Loads & Flutter
- **CI-2.17** Load Cases — limit/ultimate, fatigue spectra, gust/maneuver.  
- **CI-2.18** Flutter Characteristics — natural frequencies, damping.  
- **CI-2.19** Control Surface Hinge Moments — actuation requirements.

#### CI-1.7 Repairs
- **CI-2.20** Standard Repairs — scarf/patch, core replacement, insert repairs.  
- **CI-2.21** Acceptance Limits — post-repair metrics (UT/thermography/margins).

#### CI-1.8 Effectivity & Options
- **CI-2.22** Effectivity Sets — MSN ranges, blocks.  
- **CI-2.23** Options — variant flags (e.g., high-speed option, balance option).

#### CI-1.9 Evidence & QA
- **CI-2.24** Hinge Tests — wear, load capacity, friction measurements.  
- **CI-2.25** Fatigue Tests — control surface fatigue test results.  
- **CI-2.26** Surface Finish Measurements — profile measurements, visual inspection.  
- **CI-2.27** QA Forms Linkage — ATA-20 mandatory forms.

#### CI-1.10 Schemas & Interfaces
- **CI-2.28** JSON Schemas — hinge, control surface, actuator attachment, balance weight, acceptance metric.  
- **CI-2.29** ICDs — with ATA-27 / 29 / 57-10 / 57-30.  
- **CI-2.30** Routing Manifest — inputs/outputs linkage, UTCS/QS anchors.

### L3 — Leaf Configurable Objects (CO)

> Atomic definition points for design/manufacturing/inspection; version-pinned & sealed.

1. **Control Surface Panel (CO-3.1)** → `surface_id`, `type(elevon/flaperon/spoiler)`, `geometry_ref`, `laminate_code`, `thickness_map`, `material_spec`, `effectivity_expr`
2. **Hinge Fitting (CO-3.2)** → `hinge_id`, `type(over/under/special)`, `material_spec`, `bearing_type`, `load_capacity`, `attachment_method`
3. **Hinge Bearing (CO-3.3)** → `bearing_id`, `type(ball/roller/sleeve)`, `material_spec`, `lubrication_req`, `service_interval`
4. **Actuator Attachment Fitting (CO-3.4)** → `fitting_id`, `actuator_type`, `load_capacity`, `attachment_method`, `material_spec`
5. **Mass Balance Weight (CO-3.5)** → `weight_id`, `mass_kg`, `location_ref`, `attachment_method`, `adjustment_range`
6. **Aerodynamic Balance Feature (CO-3.6)** → `balance_id`, `type(horn/setback)`, `geometry_ref`, `effectiveness_factor`
7. **Surface Finish Requirement (CO-3.7)** → `finish_id`, `area_ref`, `smoothness_class`, `measurement_method`, `acceptance_criteria`
8. **Sealing Provision (CO-3.8)** → `seal_id`, `type(gap/edge)`, `material_spec`, `application_method`, `service_requirements`
9. **Load Case (CO-3.9)** → `case_id`, `description`, `limit/ultimate`, `flight_condition`, `control_surface_deflection`
10. **Flutter Characteristic (CO-3.10)** → `flutter_id`, `mode_shape`, `frequency_hz`, `damping_ratio`, `margin`
11. **Hinge Moment (CO-3.11)** → `moment_id`, `flight_condition`, `deflection_deg`, `moment_Nm`, `actuation_power_req`
12. **Standard Repair (CO-3.12)** → `repair_id`, `type(scarf/patch/core/insert)`, `ply_schedule`, `adhesive_ref`, `acceptance_ref`, `effectivity_expr`
13. **Acceptance Metric (CO-3.13)** → `metric_id`, `feature(friction/finish/alignment)`, `threshold`, `method`, `evidence_ref`
14. **Effectivity Rule (CO-3.14)** → `expr`, `start`, `end`, `options[]`, `exclusions[]`
15. **Option Flag (CO-3.15)** → `option_code`, `name`, `dependencies[]`, `exclusions[]`
16. **Tool Ref (CO-3.16)** → `tool_code`, `description`, `alt_tool[]`, `calibration_due`
17. **Material Ref (CO-3.17)** → `mat_code`, `spec`, `batch_required{Y/N}`, `shelf_life`, `storage_class`
18. **Lubrication Parameter (CO-3.18)** → `lubricant_code`, `application_method`, `interval_hours`, `quantity`  *(Form link)*
19. **Balance Adjustment (CO-3.19)** → `adjustment_id`, `method`, `tool_required`, `measurement_required`, `tolerance`  *(Form link)*
20. **Hinge Installation Parameter (CO-3.20)** → `hinge_code`, `torque_Nm`, `alignment_tolerance`, `clearance_spec`  *(Form link)*
21. **Evidence File Ref (CO-3.21)** → `type(hinge_test/fatigue/finish)`, `uri`, `sha256`, `form_link`
22. **QA Form Link (CO-3.22)** → `form_id`, `rev`, `path`, `required_in_steps[]`
23. **QS/UTCS Anchor (CO-3.23)** → `canonical_hash`, `sbom_uri`, `signer`, `timestamp`

> **Schemas** for COs are pinned in `contracts/schemas/*.schema.json` and referenced from `io/routing.manifest.yaml`.

---

## Acceptance & Inspection

| Feature / Metric                   | Minimum Requirement (unless drawing/spec overrides)          | Method                          |
| ---                                | ---                                                          | ---                             |
| Hinge friction                     | ≤ 0.5 Nm (typical)                                          | Torque measurement, test rig    |
| Hinge free play                    | ≤ 0.1 mm                                                    | Dial indicator, feeler gauge    |
| Control surface alignment          | ±0.5 mm (typical)                                           | Laser alignment, tooling        |
| Surface smoothness                 | Ra ≤ 1.6 µm (Class B)                                       | Profilometer, visual inspection |
| Gap uniformity                     | ±0.2 mm (typical)                                           | Gap gauges, visual inspection   |
| Balance weight accuracy            | ±5 g (typical)                                              | Weighing scale, balance rig     |
| Actuator attachment preload        | Per design specification                                     | Load cell, torque wrench        |
| Post-repair NDT                    | No critical indications; per CO-3.13 acceptance              | UT/RT/thermography              |

> When generic limits conflict with model/drawing, the **model/drawing governs**.

---

## Evidence & QS

- **Forms (linked):**  
  - Composite Fastening → `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`  
  - Adhesive Bonding → `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`  
  - Surface Finish & Aerodynamic Smoothness → `../../20/20-50_Surface_Finish/forms/FORM-QA-20-50-01_Surface_Finish_Aerodynamic_Smoothness.md`
  - Balance Weight Installation → `../../20/20-60_Balance_and_Alignment/forms/FORM-QA-20-60-01_Balance_Weight_Installation.md`
  - Hinge Installation & Adjustment → `../../20/20-70_Mechanical_Linkages/forms/FORM-QA-20-70-01_Hinge_Installation_Adjustment.md`
- **Traceability:** material lots, OOC timers, hinge test results, balance measurements → linked via **CO-3.21/CO-3.23** and sealed with **UTCS/QS**.

---

## Change Control

Any deviation from ATA-20 or drawing/spec must be approved by **M&P** and **MRB** and recorded here. Releases follow PDM-PLM CNs; manifests and signatures are updated under `io/` and `evidence/`.

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
