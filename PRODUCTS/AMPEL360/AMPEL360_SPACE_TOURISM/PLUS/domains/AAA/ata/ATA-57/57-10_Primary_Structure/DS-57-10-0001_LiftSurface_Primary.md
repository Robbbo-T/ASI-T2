---
id: ASIT-PLUS-AAA-DS-57-10-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/ATA-57/57-10_Primary_Structure/DS-57-10-0001_LiftSurface_Primary.md
llc: DESIGN
title: "Design Specification — Lifting Surface Primary Structure (ATA-57-10)"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "Structures Engineering Team"
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

# DS-57-10-0001 — Lifting Surface Primary Structure

Design specification for **AMPEL360 PLUS** lifting-surface primary structure (wings/strakes/fins) covering spars, ribs, skins, joints, interfaces, stiffness, strength, durability, and TPS integration for suborbital missions.

---

## 1. Purpose

Define quantitative, auditable requirements for the **primary structure** of lifting surfaces to ensure safety, performance, reusability, and seamless integration with TPS, actuation, and vehicle body structure.

## 2. Scope & Interfaces

**In scope**
- Primary load-path members: front/rear spars, ribs, skins, close-outs, carry-through.
- Joints & fittings: root attachments, hinge/actuator hard-points, system brackets.
- Mass properties & stiffness targets; modal behavior; damage tolerance; fatigue life.
- TPS interface geometry and back-face thermal constraints at acreage and leading edges.

**Out of scope**
- Control-surface design (see ATA-55).
- TPS materials/process details (see [57-20 Leading Edges](../57-20_Leading_Edges/) and [57-30 TPS Integration](../57-30_TPS_Integration/)).
- Actuation systems (see LCC/ATA-27).

**Key interfaces**
- **ATA-53** (Body): Wing-to-fuselage carry-through, load distribution, access panels.
- **ATA-55** (Control surfaces): Hinge-line reinforcement, actuator brackets, thermal gaps.
- **ATA-57-20** (Leading edges): RCC attachment, seal interfaces, thermal expansion.
- **ATA-57-30** (TPS acreage): Bondline thermal limits, gap management, carrier panels.

---

## 3. Requirements

### 3.1 Structural Requirements

**Load Cases**
- **Ascent**: ≤ 3.5g longitudinal, ≤ 2.0g lateral, ≤ 1.5g vertical (plus dynamic amplification).
- **Reentry**: ≤ 2.5g longitudinal, ≤ 1.8g lateral, ≤ 2.2g vertical (thermal gradient superposition).
- **Landing**: ≤ 2.0g sink-rate loads, crosswind cases, asymmetric touchdown.
- **Ground handling**: Transportation, lifting, jacking, maintenance access loads.

**Safety factors**
- **Ultimate**: 1.5× limit loads (no structural failure).
- **Yield**: 1.0× limit loads (no permanent deformation).
- **Fatigue**: 4× design life (100 missions baseline, 400 mission target).

**Material properties** (minimum design values)
- **Carbon-fiber composite**: Ftu ≥ 600 MPa, Fcu ≥ 500 MPa, E ≥ 130 GPa.
- **Aluminum (secondary)**: 2024-T3 or 7075-T6, per aerospace standards.
- **Fasteners**: Ti-6Al-4V or Inconel 718, per AS/NAS specifications.

### 3.2 Mass & Stiffness

**Mass targets**
- **Primary structure**: ≤ 180 kg per lifting surface (excluding TPS, systems).
- **Center of gravity**: Within ±50 mm of design intent (X, Y, Z coordinates).
- **Moment of inertia**: Ixx, Iyy, Izz within ±5% of FEM predictions.

**Stiffness requirements**
- **First bending mode**: ≥ 15 Hz (avoid coupling with vehicle body modes).
- **First torsion mode**: ≥ 25 Hz (control-surface actuation decoupling).
- **Tip deflection**: ≤ 25 mm under 1g+ maximum design loads.

### 3.3 Thermal Requirements

**Operating temperatures**
- **Structure core**: -70°C to +150°C (operational), -100°C to +200°C (survival).
- **TPS interface**: ≤ 180°C sustained, ≤ 250°C transient (behind acreage TPS).
- **Leading edge interface**: ≤ 350°C sustained, ≤ 500°C transient (behind RCC).

**Thermal cycling**
- **Design life**: 400 thermal cycles (-70°C to +150°C).
- **Thermal gradient**: ≤ 5°C/cm within primary structure during reentry.
- **Expansion joints**: Accommodate ±12 mm differential expansion at TPS interfaces.

### 3.4 Damage Tolerance

**Inspection intervals**
- **Visual**: Every flight (external surface, fasteners, joints).
- **NDI (ultrasonic)**: Every 10 flights (bondlines, core disbonds).
- **Detailed**: Every 50 flights (structural teardown, internal inspection).

**Damage scenarios**
- **Impact**: 25 J (tool drop), 100 J (ground handling), no growth over 10 flights.
- **Fatigue**: Crack growth rate ≤ 0.1 mm/1000 cycles, residual strength ≥ limit load.
- **Environmental**: UV degradation, thermal cycling, moisture absorption limits.

---

## 4. Design Details

### 4.1 Structural Configuration

**Spar arrangement**
- **Front spar**: 20% chord, continuous from root to tip, primary bending loads.
- **Rear spar**: 70% chord, hinge-line attachment, torsion box closure.
- **Auxiliary spar**: 50% chord (optional), systems routing, damage arrest.

**Rib spacing**
- **Inboard**: 400 mm (high-load region, system interfaces).
- **Outboard**: 600 mm (weight optimization, manufacturing efficiency).
- **Special**: Close-pitch at hinge lines, actuator brackets, system penetrations.

**Skin panels**
- **Upper surface**: 8-ply quasi-isotropic carbon-fiber, co-cured to spars/ribs.
- **Lower surface**: 6-ply carbon-fiber, removable panels for access.
- **Core**: Nomex honeycomb, 6 mm thickness, flame-resistant grade.

### 4.2 Joints & Attachments

**Root attachment** (wing-to-body)
- **Type**: Bolted joint, 4× main fittings, fail-safe design.
- **Fasteners**: Ti-6Al-4V bolts, M12 × 1.75, preloaded to 85% ultimate.
- **Bushings**: Bronze-lined, self-lubricating, corrosion-resistant.
- **Access**: Removable panels, torque verification ports.

**Hinge line** (control surface interface)
- **Type**: Piano hinge, continuous along span, sealed against reentry heating.
- **Material**: Inconel 718, machined from solid, shot-peened finish.
- **Lubrication**: Dry-film MoS₂, reapplication every 25 flights.
- **Thermal barriers**: Inconel shields, 2 mm air gap, radiation protection.

### 4.3 TPS Integration

**Acreage interface**
- **Substructure**: Aluminum honeycomb carriers, bonded to primary structure.
- **Standoffs**: Ti-6Al-4V posts, 15 mm height, thermal isolation.
- **Bondline**: RTV silicone, room-temperature cure, ≤ 180°C service.
- **Expansion joints**: Silicone seals, ±12 mm movement, pressure-tight.

**Leading edge interface**
- **Attachment**: Mechanical fasteners + high-temp adhesive bond.
- **Sealing**: Inconel wire mesh + ceramic fiber, 1200°C capability.
- **Inspection**: Removable access panels, borescope ports, leak check fittings.

---

## 5. Verification & Validation

### 5.1 Analysis Requirements

**Finite Element Model (FEM)**
- **Mesh density**: ≤ 10 mm elements in high-stress regions.
- **Boundary conditions**: Validated against test data, load transfer verified.
- **Materials**: Temperature-dependent properties, nonlinear analysis for ultimate loads.
- **Verification**: Modal test correlation ≤ ±5%, stress validation ≤ ±10%.

**Load cases**
- **Static**: All flight and ground load cases, combined thermal/mechanical.
- **Dynamic**: Gust response, landing impact, control-surface excitation.
- **Fatigue**: Spectrum loading, crack growth analysis, safe-life demonstration.

### 5.2 Testing Requirements

**Coupon testing**
- **Material characterization**: Strength, stiffness, fatigue (per ASTM standards).
- **Joint testing**: Fastener pull-out, bearing strength, environmental effects.
- **Thermal cycling**: Bondline integrity, dimensional stability, property retention.

**Component testing**
- **Rib testing**: Compression, shear, combined loads, damage tolerance.
- **Spar testing**: Bending, torsion, fatigue, hinge-line attachment loads.
- **Panel testing**: Compression, shear buckling, impact damage, repair validation.

**Assembly testing**
- **Ground vibration**: Modal survey, damping measurement, FEM correlation.
- **Static testing**: Ultimate load demonstration, permanent set measurement.
- **Fatigue testing**: 4× design life, crack inspection, residual strength.

---

## 6. Quality Assurance

### 6.1 Manufacturing Controls

**Material controls**
- **Incoming**: Certification review, sampling inspection, property verification.
- **Storage**: Temperature/humidity control, shelf-life tracking, FIFO rotation.
- **Preparation**: Clean-room environment, contamination prevention, tool calibration.

**Process controls**
- **Layup**: Ply orientation verification, fiber volume fraction, void content ≤ 2%.
- **Cure cycle**: Temperature/pressure monitoring, heat-up rate ≤ 3°C/min.
- **Machining**: Tool wear monitoring, dimensional inspection, surface finish Ra ≤ 1.6 μm.

### 6.2 Inspection Requirements

**In-process inspection**
- **Layup**: 100% ply-by-ply verification, orientation, splice locations.
- **Cure**: Thermocouple monitoring, pressure verification, cure degree ≥ 95%.
- **Machining**: First-article inspection, ongoing dimensional checks, tool verification.

**Final inspection**
- **Dimensional**: ±0.5 mm tolerance on primary features, ±1.0 mm on secondary.
- **NDI**: 100% ultrasonic scan, delamination/void detection, thickness verification.
- **Surface**: Visual inspection, foreign object detection, protective coating integrity.

---

## 7. Documentation & Configuration

### 7.1 Design Data

**Drawings**: 3D CAD models, 2D manufacturing drawings, assembly instructions.
**Analysis**: FEM files, load cases, stress reports, margin summaries.
**Testing**: Test plans, procedures, results, correlation studies.
**Materials**: Specifications, certifications, process controls, quality records.

### 7.2 Configuration Control

**Baseline**: Engineering drawings, specifications, test results locked at CDR.
**Changes**: ECO process, impact assessment, verification requirements, approval levels.
**Traceability**: Serial number tracking, build records, inspection results, maintenance history.

---

## 8. Compliance & Traceability

**Regulatory**: FAA/AST 14 CFR Parts 450/460, EASA/CS-SC (where applicable).
**Standards**: ASTM, AMS, AS/NAS, ISO aerospace quality standards.
**Internal**: UTCS/QS quality system, design review process, verification procedures.

**Evidence management**: All requirements linked to verification methods, test results, analysis reports stored in UTCS database with unique identifiers and approval signatures.

---

*This specification establishes the foundation for safe, reliable, reusable lifting-surface primary structure supporting AMPEL360 PLUS suborbital operations.*