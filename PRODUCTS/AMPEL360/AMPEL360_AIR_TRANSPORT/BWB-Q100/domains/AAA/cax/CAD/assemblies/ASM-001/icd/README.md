# ASM-001 — Interface Control (ICD)

Interface control for **ASM-001 · OML Master Surface** with adjacent airframe assemblies of the BWB-Q100.
This ICD specifies **what** geometry/metadata is exchanged, **where** it lives in the repo, and **how** it's validated.

> **Scope:** Structural/geometry interfaces for ATA-57/53 airframes only. No systems routing, loads, or certification content.

---

## 1) Directory layout

```
ASM-001/
└── icd/
    ├── README.md                      # This document
    ├── matrix.yaml                    # Single source of truth for ICD entries
    ├── IC-001_centerbody/
    │   ├── IC-001_boundary_curves.step
    │   └── IC-001_meta.yaml
    ├── IC-002_midspan/
    │   ├── IC-002_boundary_curves.step
    │   └── IC-002_meta.yaml
    ├── IC-003_outboard/
    │   ├── IC-003_boundary_curves.step
    │   └── IC-003_meta.yaml
    ├── IC-004_ctrl_surfaces/
    │   ├── IC-004_cutouts.step
    │   └── IC-004_labels.csv
    ├── IC-005_spoilers/
    │   └── IC-005_cutouts.step
    ├── IC-006_tip/
    │   └── IC-006_trim_and_blend.step
    ├── IC-007_transition/
    │   ├── IC-007_guides.step
    │   └── IC-007_meta.yaml
    └── IC-008_blend/
        └── IC-008_surfaces.step
```

---

## 2) Interface matrix (summary)

| IC ID | Owner | Counterpart | Description | Geometry deliverable |
|-------|-------|-------------|-------------|---------------------|
| IC-001 | ASM-001 | ASM-002 | OML ↔ Centerbody (root join) | IC-001_boundary_curves.step |
| IC-002 | ASM-001 | ASM-003 | OML ↔ Mid-Span Wing Box | IC-002_boundary_curves.step |
| IC-003 | ASM-001 | ASM-004 | OML ↔ Outboard Wing Box | IC-003_boundary_curves.step |
| IC-004 | ASM-001 | ASM-008 | OML → Control Surface Cutouts | IC-004_cutouts.step |
| IC-005 | ASM-001 | ASM-009 | OML → Spoiler Cutouts | IC-005_cutouts.step |
| IC-006 | ASM-001 | ASM-027 | OML ↔ Wingtip Integration | IC-006_trim_and_blend.step |
| IC-007 | ASM-001 | ASM-031 | OML ↔ Centerbody Transition | IC-007_guides.step |
| IC-008 | ASM-001 | ASM-032 | OML ↔ Spanwise Blend Fairings | IC-008_surfaces.step |

---

## 3) Data exchange protocol

### 3.1) Geometry formats
- **Primary:** STEP AP214 (parametric surfaces)
- **Secondary:** IGES 214 (NURBS surfaces)
- **Mesh:** STL (validation only)

### 3.2) Metadata format
```yaml
# IC-001_meta.yaml example
interface_id: IC-001
owner_assembly: ASM-001
counterpart_assembly: ASM-002
geometry_type: boundary_curves
coordinate_system: BWB_aircraft_ref
units: mm
tolerance: ±0.1
last_updated: 2024-XX-XX
validation_status: pass/fail/pending
checksum_step: sha256_hash_here
```

### 3.3) Validation requirements
- **Geometric continuity:** G1 minimum at all interfaces
- **Tolerance stack-up:** ±0.1mm at assembly joints
- **Surface quality:** Class A surfaces for external OML
- **Mesh compatibility:** STL validation for CFD/FEA downstream

---

## 4) Change control

### 4.1) Update procedure
1. Modify geometry in owner assembly (ASM-001)
2. Regenerate interface geometry → `IC-XXX/`
3. Update metadata → `IC-XXX_meta.yaml`
4. Validate with counterpart assembly
5. Update `matrix.yaml` with new checksums
6. Notify downstream assemblies via PR

### 4.2) Impact assessment
| Interface | Downstream Impact | Validation Required |
|-----------|-------------------|-------------------|
| IC-001 | ASM-002 structure fit | Structural clearance check |
| IC-002/003 | Wing box integration | Load path continuity |
| IC-004/005 | Control surface gaps | Aerodynamic seal validation |
| IC-006 | Tip device mounting | Structural attachment points |
| IC-007/008 | Fairing continuity | Surface smoothness check |

---

## 5) Tools & automation

### 5.1) Validation scripts
- `validate_interfaces.py` — Geometric continuity check
- `check_tolerances.py` — Dimensional validation
- `generate_reports.py` — Interface status summary

### 5.2) CAD integration
- **CATIA V5/V6:** Surface extraction macros
- **NX:** Interface geometry automation
- **Fusion 360:** Export parameter sets

---

## 6) Related documentation
- `../metadata.yaml` — Assembly-level interface summary
- `../../assemblies.manifest.yaml` — Control surface mapping
- `../../../scripts/validate_assembly_links.py` — Automated validation
