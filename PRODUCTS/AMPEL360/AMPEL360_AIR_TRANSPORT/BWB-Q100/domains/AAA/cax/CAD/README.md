# AAA/CAx/CAD — Aerodynamic & Airframe Computer-Aided Design

Geometry design, topology optimization, and parametric modeling for BWB-Q100 aerodynamic and structural components.

## Process Overview

Computer-aided design processes for aerodynamic surfaces, airframe structures, and integrated BWB geometry optimization.

**Primary Focus**: Wing geometry, fuselage integration, structural layout, parametric modeling, and design optimization.

## Key Activities

### Design Development
- Parametric wing geometry modeling
- Blended wing-body integration design
- Structural topology definition
- Manufacturing constraint integration

### Optimization Targets
- Aerodynamic surface optimization for drag reduction
- Structural weight minimization
- Manufacturing feasibility integration
- Multi-disciplinary design optimization (MDO)

### Integration Points
- **QOx/CAD**: Quantum topology optimization (QUBO/BQM → QAOA/Annealing)
- **CAE**: Structural validation of CAD geometries
- **CFD**: Aerodynamic validation of surface designs
- **Manufacturing**: DfM constraint integration

## Quantum Transition Path (CAx → QOx)

**Classical Limitations**: Large combinatorial design spaces, multi-objective trade-offs
**Quantum Opportunity**: Discrete topology choices, layout optimization
**Expected Benefits**: 5-15% improvement in design efficiency, expanded design space exploration

### QUBO Formulation Examples
1. **Wing Rib Placement**: Binary variables for rib locations, structural/weight objectives
2. **Panel Configuration**: Discrete panel sizes and orientations for manufacturing
3. **Joint Location**: Optimal structural joint placement for load distribution

## Deliverables

### Design Artifacts
- Parametric CAD models (CATIA, NX, Fusion 360)
- Design trade study results
- Geometry optimization reports
- Manufacturing constraint documentation

### QOx Integration
- QUBO problem formulations for discrete design choices
- Quantum optimization input files
- Classical-quantum hybrid workflow documentation

---

## Assemblies (airframes only)

**Quick links:**

* 📦 **Assemblies folder:** [`assemblies/`](assemblies/)
* 📜 **Manifest:** [`assemblies.manifest.yaml`](assemblies.manifest.yaml)
* 🧩 **Control surfaces:** [`wing_baseline_model/control_surfaces/`](wing_baseline_model/control_surfaces/) →
  [`elevons.yaml`](wing_baseline_model/control_surfaces/elevons.yaml) ·
  [`flaperons.yaml`](wing_baseline_model/control_surfaces/flaperons.yaml) ·
  [`spoilers.yaml`](wing_baseline_model/control_surfaces/spoilers.yaml) ·
  [`trim_surfaces.yaml`](wing_baseline_model/control_surfaces/trim_surfaces.yaml)

> Each assembly folder should include: `models/` (3D), `drawings/` (2D), `icd/` (interfaces), and `metadata.yaml`.

### Core wing & centerbody structure

* [**ASM-001 — OML Surface Set**](assemblies/ASM-001/) · *ATA-57* · [3D](assemblies/ASM-001/models/) | [2D](assemblies/ASM-001/drawings/) | [ICD](assemblies/ASM-001/icd/)
* [**ASM-002 — Centerbody Primary Box**](assemblies/ASM-002/) · *ATA-53* · [3D](assemblies/ASM-002/models/) | [2D](assemblies/ASM-002/drawings/) | [ICD](assemblies/ASM-002/icd/)
* [**ASM-003 — Mid-Span Wing Box**](assemblies/ASM-003/) · *ATA-57* · [3D](assemblies/ASM-003/models/) | [2D](assemblies/ASM-003/drawings/) | [ICD](assemblies/ASM-003/icd/)
* [**ASM-004 — Outboard Wing Box**](assemblies/ASM-004/) · *ATA-57* · [3D](assemblies/ASM-004/models/) | [2D](assemblies/ASM-004/drawings/) | [ICD](assemblies/ASM-004/icd/)
* [**ASM-005 — Pressure Deck & Keel Beam**](assemblies/ASM-005/) · *ATA-53* · [3D](assemblies/ASM-005/models/) | [2D](assemblies/ASM-005/drawings/) | [ICD](assemblies/ASM-005/icd/)
* [**ASM-006 — Leading-Edge Primary Structure**](assemblies/ASM-006/) · *ATA-57* · [3D](assemblies/ASM-006/models/) | [2D](assemblies/ASM-006/drawings/) | [ICD](assemblies/ASM-006/icd/)
* [**ASM-007 — Trailing-Edge Primary Structure**](assemblies/ASM-007/) · *ATA-57* · [3D](assemblies/ASM-007/models/) | [2D](assemblies/ASM-007/drawings/) | [ICD](assemblies/ASM-007/icd/)
* [**ASM-018 — Wing Carry-Through Spars**](assemblies/ASM-018/) · *ATA-57* · [3D](assemblies/ASM-018/models/) | [2D](assemblies/ASM-018/drawings/) | [ICD](assemblies/ASM-018/icd/)
* [**ASM-031 — Centerbody Transition Structure**](assemblies/ASM-031/) · *ATA-53* · [3D](assemblies/ASM-031/models/) | [2D](assemblies/ASM-031/drawings/) | [ICD](assemblies/ASM-031/icd/)

### Control-surface structures

* [**ASM-008 — Elevon/Flap Boxes**](assemblies/ASM-008/) · *ATA-57* · [3D](assemblies/ASM-008/models/) | [2D](assemblies/ASM-008/drawings/) | [ICD](assemblies/ASM-008/icd/)
  ↳ [`elevons.yaml`](wing_baseline_model/control_surfaces/elevons.yaml) · [`flaperons.yaml`](wing_baseline_model/control_surfaces/flaperons.yaml) · [`trim_surfaces.yaml`](wing_baseline_model/control_surfaces/trim_surfaces.yaml)
* [**ASM-009 — Spoiler/Airbrake Boxes**](assemblies/ASM-009/) · *ATA-57* · [3D](assemblies/ASM-009/models/) | [2D](assemblies/ASM-009/drawings/) | [ICD](assemblies/ASM-009/icd/)
  ↳ [`spoilers.yaml`](wing_baseline_model/control_surfaces/spoilers.yaml)
* [**ASM-010 — Trim/Tab Structure**](assemblies/ASM-010/) · *ATA-57* · [3D](assemblies/ASM-010/models/) | [2D](assemblies/ASM-010/drawings/) | [ICD](assemblies/ASM-010/icd/)
  ↳ [`trim_surfaces.yaml`](wing_baseline_model/control_surfaces/trim_surfaces.yaml)

### Interfaces & attachments (structural)

* [**ASM-012 — Wing–Fuselage Mating Fittings**](assemblies/ASM-012/) · *ATA-53/57* · [3D](assemblies/ASM-012/models/) | [2D](assemblies/ASM-012/drawings/) | [ICD](assemblies/ASM-012/icd/)
* [**ASM-019 — Pylon/Hardpoint Structure**](assemblies/ASM-019/) · *ATA-54* · [3D](assemblies/ASM-019/models/) | [2D](assemblies/ASM-019/drawings/) | [ICD](assemblies/ASM-019/icd/)
* [**ASM-026 — Engine/Nacelle Attach Structure**](assemblies/ASM-026/) · *ATA-54/71* · [3D](assemblies/ASM-026/models/) | [2D](assemblies/ASM-026/drawings/) | [ICD](assemblies/ASM-026/icd/)

### Bulkheads, doors & windows (airframe)

* [**ASM-016 — Pressure Bulkheads**](assemblies/ASM-016/) · *ATA-53* · [3D](assemblies/ASM-016/models/) | [2D](assemblies/ASM-016/drawings/) | [ICD](assemblies/ASM-016/icd/)
* [**ASM-017 — Door Sills & Frames**](assemblies/ASM-017/) · *ATA-52* · [3D](assemblies/ASM-017/models/) | [2D](assemblies/ASM-017/drawings/) | [ICD](assemblies/ASM-017/icd/)
* [**ASM-028 — Window Frames & Supports**](assemblies/ASM-028/) · *ATA-56* · [3D](assemblies/ASM-028/models/) | [2D](assemblies/ASM-028/drawings/) | [ICD](assemblies/ASM-028/icd/)

### Tips & fairings

* [**ASM-027 — Wingtip/Tip-Device Structure**](assemblies/ASM-027/) · *ATA-57* · [3D](assemblies/ASM-027/models/) | [2D](assemblies/ASM-027/drawings/) | [ICD](assemblies/ASM-027/icd/)
* [**ASM-032 — Spanwise Blend Fairings**](assemblies/ASM-032/) · *ATA-57* · [3D](assemblies/ASM-032/models/) | [2D](assemblies/ASM-032/drawings/) | [ICD](assemblies/ASM-032/icd/)

> **Out of scope (not listed here):** ATA-20/21/23/24/25/27/28/31/32/34/49 items (bonding & lightning, ECS mounts, avionics racks, fuel systems/venting, emergency equipment mounts, actuator bays, gear bays, APU bay, etc.).

---

### Assembly workflow pointers

* 📋 **Manufacturing/assembly sequence:** see `assembly_sequence` in [`assemblies.manifest.yaml`](assemblies.manifest.yaml)
* 🧮 **QOx variables per assembly:** `qox_variables` section in [`assemblies.manifest.yaml`](assemblies.manifest.yaml)
* 🔗 **Interface control docs (ICDs):** each `assemblies/ASM-xxx/` includes `icd/` (auto-generated or stub)

> **Tip:** If a link 404s, create the folder with the team template:
> `assemblies/ASM-0xx/{metadata.yaml, icd/README.md, models/, drawings/}`

---

*Interfaces with QOx/CAD for quantum-enhanced topology optimization.*
*Part of AAA Domain under BWB-Q100 Transport Civil × Air.*