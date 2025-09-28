# ASM-008 — Elevon/Flap Boxes Interface Control (ICD)

Interface control for **ASM-008 · Elevon/Flap Boxes** with trailing edge structure and adjacent control surfaces for the BWB-Q100.
This ICD specifies **control surface integration**, **actuator interfaces**, and **systems routing** coordination.

> **Scope:** Control surface structural interfaces (ATA-57), actuator mounting (ATA-27), and basic systems integration points.

---

## 1) Directory Layout

```
ASM-008/
└── icd/
    ├── README.md                           # This document
    ├── control_surface_matrix.yaml        # Master control surface definitions
    ├── IC-101_trailing_edge/
    │   ├── IC-101_hinge_line_interface.step
    │   ├── IC-101_seal_requirements.yaml
    │   └── IC-101_load_transfer.step
    ├── IC-102_elevons/
    │   ├── IC-102_EL1_geometry.step
    │   ├── IC-102_EL2_geometry.step
    │   ├── IC-102_EL3_geometry.step
    │   └── IC-102_deflection_envelopes.yaml
    ├── IC-103_flaps/
    │   ├── IC-103_FLAP1_geometry.step
    │   ├── IC-103_FLAP2_geometry.step
    │   └── IC-103_high_lift_config.yaml
    ├── IC-104_actuators/
    │   ├── IC-104_hydraulic_interfaces.step
    │   ├── IC-104_electric_interfaces.step
    │   └── IC-104_mounting_provisions.yaml
    ├── IC-105_adjacent_surfaces/
    │   ├── IC-105_spoiler_coordination.yaml
    │   └── IC-105_trim_tab_interfaces.step
    └── validation/
        ├── surface_continuity_check.log
        ├── deflection_clash_analysis.json
        └── actuator_envelope_validation.step
```

---

## 2) Control Surface Interface Matrix

| Surface ID | Type | Interface Partner | Hinge Line | Actuator Type | Max Deflection |
|------------|------|------------------|------------|---------------|----------------|
| EL1_L | Elevon | ASM-007 (TE) | Straight | Hydraulic | ±25° |
| EL1_R | Elevon | ASM-007 (TE) | Straight | Hydraulic | ±25° |
| EL2_L | Elevon | ASM-007 (TE) | Straight | Hydraulic | ±20° |
| EL2_R | Elevon | ASM-007 (TE) | Straight | Hydraulic | ±20° |
| EL3_L | Elevon | ASM-007 (TE) | Straight | EHA | ±15° |
| EL3_R | Elevon | ASM-007 (TE) | Straight | EHA | ±15° |
| FLAP1_L | Flap | ASM-007 (TE) | Curved | Hydraulic | 0°/+35° |
| FLAP1_R | Flap | ASM-007 (TE) | Curved | Hydraulic | 0°/+35° |
| FLAP2_L | Flap | ASM-007 (TE) | Curved | Hydraulic | 0°/+30° |
| FLAP2_R | Flap | ASM-007 (TE) | Curved | Hydraulic | 0°/+30° |

---

## 3) Interface Requirements

### 3.1) Structural Interface (IC-101)
**With ASM-007 Trailing Edge:**
- **Hinge line attachment:** Continuous piano hinge, titanium construction
- **Load transfer:** Ultimate design loads per CS-25.301
- **Sealing:** Dynamic seals for pressure differential
- **Access:** Maintenance provisions per MSG-3 requirements

**Interface Data:**
```yaml
# IC-101_seal_requirements.yaml
sealing:
  static_seals:
    - location: "hinge_line_upper"
      type: "elastomeric_seal"
      pressure_rating: "8.6_psi"
  dynamic_seals:
    - location: "control_surface_edges"
      type: "flexible_seal"
      deflection_range: "±25_degrees"
```

### 3.2) Control Surface Geometry (IC-102, IC-103)
**Surface Definition Requirements:**
- **G1 continuity:** At hinge lines with ASM-007
- **Gap management:** 3-6mm operational gaps
- **Seal integration:** Continuous sealing at all edges
- **Aerodynamic requirements:** Clean external surfaces

**Deflection Envelopes:**
```yaml
# IC-102_deflection_envelopes.yaml
elevons:
  EL1:
    max_up: 25.0      # degrees
    max_down: -25.0   # degrees
    rate_limit: 60.0  # deg/sec
  EL2:
    max_up: 20.0
    max_down: -20.0
    rate_limit: 60.0
  EL3:
    max_up: 15.0
    max_down: -15.0
    rate_limit: 45.0
```

### 3.3) Actuator Integration (IC-104)
**Hydraulic System Interface:**
- **Primary:** 3000 psi hydraulic system
- **Backup:** Independent EHA (Electro-Hydraulic Actuator)
- **Control:** FADEC interface, dual-redundant
- **Emergency:** Manual reversion capability

**Mounting Requirements:**
- **Actuator loads:** Design ultimate per CS-25.395
- **Vibration isolation:** Per RTCA DO-160
- **Maintenance access:** 24-inch minimum clearance
- **System routing:** Hydraulic lines, electrical harnesses

---

## 4) Configuration Management

### 4.1) Control Surface Mapping Integration
**Configuration Files:**
- [elevons.yaml](../../wing_baseline_model/control_surfaces/elevons.yaml) — Primary elevon definitions
- [flaperons.yaml](../../wing_baseline_model/control_surfaces/flaperons.yaml) — Flap configuration

**Automated Validation:**
```bash
# Control surface validation commands
python validate_control_surfaces.py --config elevons.yaml --geometry IC-102/
python check_deflection_envelopes.py --surfaces IC-102_deflection_envelopes.yaml
python validate_actuator_clearance.py --assembly ASM-008 --actuators IC-104/
```

### 4.2) QOx Integration Variables
**Quantum Optimization Parameters:**
- **hinge_line_optimization:** Discrete hinge line positioning choices
- **actuator_placement:** Optimal actuator mounting locations
- **surface_segmentation:** Control surface break optimization

**Integration with QOx Process:**
```yaml
# QOx variable mapping
qox_variables:
  hinge_line_positions:
    - candidate_locations: [pos1, pos2, pos3]
    - optimization_objective: "weight_minimization + actuator_efficiency"
  actuator_mounting:
    - discrete_options: [mount_config_A, mount_config_B, mount_config_C]
    - constraints: ["maintenance_access", "load_path_efficiency"]
```

---

## 5) Validation & Testing

### 5.1) Geometric Validation
- **Surface continuity:** G1 minimum at all interfaces
- **Deflection envelope:** No interference through full range
- **Actuator clearance:** Minimum envelope compliance
- **Systems routing:** Cable/hose routing validation

### 5.2) Performance Validation
- **Aerodynamic effectiveness:** Control authority verification
- **Structural integrity:** Load path validation
- **System integration:** Actuator performance testing
- **Manufacturing feasibility:** Assembly sequence validation

### 5.3) Change Impact Assessment
| Change Type | Validation Required | Affected Systems |
|-------------|-------------------|------------------|
| Surface geometry | Aerodynamic analysis | Flight controls, CFD |
| Hinge line position | Structural analysis | ASM-007 interface |
| Actuator placement | System integration | Hydraulics, electrical |
| Control authority | Flight test validation | Flight control laws |

---

## 6) Related Documentation
- `../metadata.yaml` — Assembly QOx variables and constraints
- `../../assemblies.manifest.yaml` — Control surface mapping definitions
- Flight control system ICDs (domains/AAA/systems/)
- Hydraulic system interfaces (ATA-29 documentation)
