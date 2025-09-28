---
id: ASIT-PLUS-AAA-ICD-57-40-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/ATA-57/57-40_Control_Interfaces/ICD-57-40-0001_ControlSurfaceInterfaces.md
llc: SYSTEMS
title: "Interface Control Document — Control Surface Interfaces (ATA-57-40)"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "AAA Structures & LCC Integration"
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

# ICD-57-40-0001 — Control Surface Interfaces

Interface Control Document (ICD) defining **mechanical**, **electrical/power**, **data/control**, and **thermal/TPS** interfaces between **lifting surfaces** and their **actuation & control systems** for **AMPEL360 PLUS**.

> **Related**  
> • Primary structure: [DS-57-10-0001](../57-10_Primary_Structure/DS-57-10-0001_LiftSurface_Primary.md)  
> • TPS acreage: [PS-57-30-0001](../57-30_TPS_Integration/PS-57-30-0001_TPS_AcreageInstallation.md)  
> • Leading edges: [PS-57-20-0001](../57-20_Leading_Edges/PS-57-20-0001_RCC_Handling_Bonding.md)  
> • Actuation system: [../../../LCC/ata/27/](../../../LCC/ata/27/)  
> • Control surfaces: [../55/](../55/)  
> • CAx overviews: [../../cax/CAD/](../../cax/CAD/), [../../cax/CAE/](../../cax/CAE/), [../../cax/CFD/](../../cax/CFD/)

---

## 1. Purpose & Scope

### 1.1 Purpose
Define quantitative, auditable interface requirements between **lifting-surface primary structure** and **control-surface actuation** to ensure:
- **Mechanical compatibility**: Load paths, deflection limits, structural integration.
- **Thermal protection**: Sealed gaps, high-temperature operation, reentry survival.
- **Control integration**: Actuation forces, position feedback, failure modes.
- **Maintenance access**: Inspection ports, component replacement, adjustment procedures.

### 1.2 Scope
**In scope**
- **Hinge-line interfaces**: Mechanical attachment, thermal sealing, lubrication systems.
- **Actuator hard-points**: Mounting brackets, load transfer, structural reinforcement.
- **Control linkages**: Push-pull rods, bellcranks, position sensors, emergency disconnect.
- **TPS gap management**: Seals, barriers, thermal expansion accommodation.
- **Electrical interfaces**: Power routing, signal cables, connector specifications.

**Out of scope**
- **Actuation system design**: Motors, gearboxes, control electronics (see LCC/ATA-27).
- **Control surface aerodynamics**: Surface design, balance, flutter (see ATA-55).
- **Flight control software**: Command processing, feedback loops, failure detection.

---

## 2. Interface Identification

### 2.1 Physical Interfaces

**Interface ID: IF-57-40-001 — Hinge Line Assembly**
- **Description**: Continuous piano hinge connecting control surface to lifting-surface trailing edge.
- **Location**: Wing station WS-2.5 to WS-7.8 (5.3 m span), elevator/rudder equivalent.
- **Function**: Transmit actuation loads, maintain aerodynamic continuity, seal against reentry heating.

**Interface ID: IF-57-40-002 — Primary Actuator Bracket**
- **Description**: Main structural attachment for primary flight control actuator.
- **Location**: Wing station WS-5.0 (center of pressure), reinforced rib attachment.
- **Function**: React actuation loads (±15 kN), provide fail-safe load path, enable maintenance access.

**Interface ID: IF-57-40-003 — Secondary Actuator Bracket**
- **Description**: Backup/trim actuator attachment for redundant control authority.
- **Location**: Wing station WS-4.0, independent load path from primary actuator.
- **Function**: React backup loads (±8 kN), provide dissimilar actuation mode, emergency operation.

**Interface ID: IF-57-40-004 — Position Sensor Mount**
- **Description**: Rotary position sensor installation for control surface angle feedback.
- **Location**: Hinge line centerline, environmentally protected enclosure.
- **Function**: Provide ±0.1° position accuracy, operate -55°C to +125°C, survive reentry heating.

### 2.2 Functional Interfaces

**Interface ID: IF-57-40-101 — Control Authority**
- **Description**: Required control surface deflection range and rate capability.
- **Specification**: ±25° deflection, 30°/second rate, 5° trim authority.
- **Function**: Enable vehicle control throughout flight envelope, provide upset recovery capability.

**Interface ID: IF-57-40-102 — Load Transfer**
- **Description**: Structural load paths between control surface and lifting surface.
- **Specification**: ±15 kN hinge moments, ±8 kN side loads, safety factor 1.5× ultimate.
- **Function**: React aerodynamic loads, prevent structural failure, maintain control authority.

**Interface ID: IF-57-40-103 — Thermal Protection**
- **Description**: TPS continuity across hinge line and actuator penetrations.
- **Specification**: ≤1200°C surface temperature, ≤2°C/min heating rate, sealed against plasma.
- **Function**: Protect structure during reentry, maintain pressure seal, prevent thermal damage.

---

## 3. Interface Requirements

### 3.1 Mechanical Requirements

**Hinge Line (IF-57-40-001)**

*Geometric constraints*
- **Hinge axis alignment**: ±0.5 mm over 5.3 m span, parallel to wing reference plane.
- **Pin diameter**: 12 mm Ti-6Al-4V, precision ground, 0.025 mm maximum runout.
- **Bearing clearance**: 0.05–0.15 mm radial, self-lubricating bronze bushings.
- **End play**: 1–3 mm total, spring-loaded to eliminate backlash.

*Load requirements*
- **Hinge moment**: ±15 kN·m ultimate, ±10 kN·m limit, uniform distribution.
- **Side loads**: ±8 kN ultimate (gusts, maneuvering), fail-safe design.
- **Fatigue life**: 50,000 cycles to limit load, 12,500 cycles to ultimate.
- **Deflection limits**: ≤2 mm hinge line sag under limit loads.

*Material & manufacturing*
- **Hinge material**: Inconel 718, solution-treated and aged, shot-peened finish.
- **Pin material**: Ti-6Al-4V, hardness 35–42 HRC, nitrided surface treatment.
- **Bushings**: Phosphor bronze with PTFE liner, dry-film MoS₂ topcoat.
- **Tolerances**: ±0.025 mm on bearing surfaces, ±0.1 mm on mounting features.

**Primary Actuator Bracket (IF-57-40-002)**

*Mounting configuration*
- **Attachment**: 8× M10 Ti-6Al-4V bolts, preloaded to 75% ultimate strength.
- **Interface**: Spherical bearing, ±15° misalignment capability, grease lubrication.
- **Reinforcement**: Local rib thickness increased 50%, load distribution plates.
- **Access**: Removable panel for actuator replacement, torque verification.

*Load capability*
- **Primary loads**: ±15 kN axial (actuation), ±5 kN lateral (side loads).
- **Ultimate loads**: 1.5× primary with no structural failure.
- **Fatigue**: 4× design life (200,000 cycles), crack initiation analysis.
- **Stiffness**: ≤1 mm deflection at limit load, maintain control precision.

*Environmental requirements*
- **Temperature**: -65°C to +150°C operational, -85°C to +200°C survival.
- **Vibration**: 20g RMS, 5–2000 Hz, random spectrum per MIL-STD-810.
- **Corrosion**: Salt spray exposure 500 hours, no loss of function.
- **Sealing**: IP65 rating minimum, environmental protection for bearings.

### 3.2 Thermal Requirements

**TPS Integration (IF-57-40-103)**

*Temperature limits*
- **Hinge line surface**: ≤1200°C during reentry, ≤1400°C emergency.
- **Actuator bracket**: ≤150°C during reentry, ≤200°C emergency.
- **Control surface gap**: ≤800°C at gap edges, sealed against plasma intrusion.
- **Internal structure**: ≤120°C behind TPS, ≤150°C transient.

*Thermal barriers*
- **Hinge line shield**: Inconel 718 plates, 2 mm thickness, radiation barriers.
- **Actuator thermal protection**: Ceramic blanket insulation, removable for maintenance.
- **Gap sealing**: Inconel wire mesh + ceramic fiber, compressible seal design.
- **Cooling passages**: Natural convection paths, no active cooling required.

*Thermal expansion*
- **Hinge line growth**: ±12 mm over 5.3 m span, accommodate without binding.
- **Actuator bracket**: ±3 mm movement at attachment point, spherical bearing accommodation.
- **Control surface**: ±8 mm chord-wise expansion, gap management at trailing edge.
- **Seal compression**: 25–75% of original thickness, maintain sealing effectiveness.

### 3.3 Control System Requirements

**Position Feedback (IF-57-40-004)**

*Sensor specifications*
- **Type**: Rotary variable differential transformer (RVDT), absolute position.
- **Range**: ±30° mechanical, ±25° electrical active range.
- **Accuracy**: ±0.1° over temperature range, ±0.05° at room temperature.
- **Resolution**: 0.01° minimum, 12-bit ADC conversion.

*Environmental capability*
- **Temperature**: -55°C to +125°C operational, thermal cycling qualified.
- **Vibration**: 50g shock, 20g random, frequency range 5–2000 Hz.
- **EMI/EMC**: MIL-STD-461 compliance, shielded cables, filtered power.
- **Reliability**: 0.999 probability of success, 10⁶ operating cycles minimum.

*Installation requirements*
- **Mounting**: Precision alignment ±0.1°, rigid connection to hinge axis.
- **Wiring**: Shielded twisted pair, MIL-DTL-38999 connectors.
- **Calibration**: Field-adjustable zero/span, software linearization capability.
- **Redundancy**: Dual sensors for critical control surfaces, dissimilar failure modes.

**Control Authority (IF-57-40-101)**

*Deflection capability*
- **Range**: +25°/-20° (asymmetric for reentry trim), mechanical stops at ±27°.
- **Rate**: 30°/second no-load, 20°/second at limit hinge moment.
- **Acceleration**: 150°/second² minimum, step response ≤0.5 seconds to 90%.
- **Precision**: ±0.2° steady-state accuracy, ±0.5° dynamic tracking.

*Load reaction*
- **Hinge moment**: ±15 kN·m maximum (reentry/landing), ±10 kN·m normal flight.
- **Control force**: ≤5 kN actuator force at maximum hinge moment.
- **Breakout force**: ≤500 N to initiate motion from any position.
- **Backdrive**: Manual control capability, ≤200 N pilot force for emergency.

---

## 4. Interface Design

### 4.1 Hinge Line Configuration

**Piano hinge design**
- **Leaf thickness**: 8 mm (wing side), 6 mm (control surface side).
- **Pin retention**: Rolled pins at 500 mm intervals, removable for maintenance.
- **Lubrication**: Dry-film MoS₂, reapplication every 50 flights.
- **Sealing**: Labyrinth seals at ends, pressure-tight during reentry.

**Thermal protection integration**
- **TPS overlap**: 25 mm minimum at hinge line, sealed gap design.
- **Expansion joints**: Compressible seals, maintain continuity during thermal cycling.
- **Inspection access**: Removable covers for hinge pin examination.
- **Replacement**: Modular design enables field replacement of hinge segments.

### 4.2 Actuator Integration

**Primary actuator installation**
- **Type**: Electric motor-driven ballscrew, fail-safe design.
- **Mounting**: Spherical bearing interface, accommodate thermal growth.
- **Backup power**: Battery operation for emergency extension/retraction.
- **Position indication**: Integrated RVDT, backup limit switches.

**Control linkage**
- **Type**: Push-pull rod, spherical bearings both ends.
- **Material**: Ti-6Al-4V tube, 25 mm OD × 2 mm wall thickness.
- **Length**: Adjustable threaded connection, ±25 mm range.
- **Safety**: Positive connection, no single-point failures.

### 4.3 Electrical Integration

**Power distribution**
- **Voltage**: 28 VDC primary, 115 VAC backup for high-power actuators.
- **Current**: 30 A maximum per actuator, circuit protection provided.
- **Cables**: MIL-DTL-27500 aerospace grade, 125°C temperature rating.
- **Routing**: Protected conduits, separation from hydraulic lines.

**Signal interfaces**
- **Position feedback**: 4-wire RVDT connection, 5 kHz excitation.
- **Control commands**: Digital interface, CAN bus protocol.
- **Status monitoring**: Built-in test capability, fault reporting.
- **Emergency**: Hardwired backup control, independent of main computer.

---

## 5. Test & Verification

### 5.1 Interface Testing

**Mechanical testing**
- **Hinge moment**: Apply ±15 kN·m ultimate loads, verify no permanent deformation.
- **Side loads**: Apply ±8 kN lateral loads, check bearing integrity.
- **Fatigue**: 200,000 cycles at limit loads, inspect for crack initiation.
- **Environmental**: Temperature cycling, vibration, shock per specifications.

**Thermal testing**
- **Reentry simulation**: Radiant heating to 1200°C surface temperature.
- **Expansion**: Measure actual growth, verify accommodation.
- **Seal integrity**: Pressure decay testing at operating temperatures.
- **Cool-down**: Verify operation after thermal cycling.

**Functional testing**
- **Control authority**: Verify ±25° deflection range, 30°/second rate.
- **Position accuracy**: Confirm ±0.1° feedback precision.
- **Load reaction**: Measure actual hinge moments throughout range.
- **Emergency operation**: Test manual reversion, backup power systems.

### 5.2 Interface Validation

**Design verification**
- **Analysis correlation**: Compare test results to finite element predictions.
- **Requirements compliance**: Verify all interface requirements met.
- **Margin assessment**: Document actual vs. required performance margins.
- **Failure modes**: Confirm fail-safe operation under single failures.

**Flight qualification**
- **Ground test**: Full system integration testing before first flight.
- **Flight test**: Incremental envelope expansion, performance verification.
- **Operational experience**: Monitor performance over fleet operations.
- **Continuous improvement**: Update requirements based on service experience.

---

## 6. Manufacturing & Quality

### 6.1 Manufacturing Requirements

**Precision machining**
- **Hinge components**: CNC machining, ±0.025 mm tolerance on critical features.
- **Surface finish**: Ra ≤1.6 μm on bearing surfaces, shot peening where specified.
- **Material traceability**: Full certification chain for aerospace materials.
- **Process control**: Statistical process control, first article inspection.

**Assembly procedures**
- **Hinge pin installation**: Precision fitting, controlled interference fit.
- **Bushing installation**: Press fit, proper orientation and lubrication.
- **Actuator mounting**: Torque specification compliance, thread locking compound.
- **Final alignment**: Coordinate measurement, adjustment procedures.

### 6.2 Quality Assurance

**Inspection requirements**
- **Dimensional**: 100% inspection of critical features, statistical sampling of others.
- **Non-destructive**: Penetrant inspection of high-stress areas.
- **Functional**: End-of-line testing, all functions verified.
- **Documentation**: Complete traceability records, approval signatures.

**Acceptance testing**
- **Performance**: Verify all interface requirements prior to delivery.
- **Environmental**: Sample testing to qualification levels.
- **Reliability**: Life testing on representative components.
- **Configuration**: Verification of as-built configuration vs. design.

---

## 7. Operations & Maintenance

### 7.1 Operational Procedures

**Pre-flight inspection**
- **Visual examination**: Hinge line condition, actuator attachment, seal integrity.
- **Functional check**: Control surface movement, position indication accuracy.
- **Lubrication**: Verify adequate lubrication, reapply if necessary.
- **Clearances**: Check for interference, proper gap dimensions.

**Post-flight inspection**
- **Damage assessment**: Look for thermal damage, mechanical wear, crack initiation.
- **Performance check**: Verify continued normal operation.
- **Seal condition**: Inspect TPS gaps, replace seals if damaged.
- **Documentation**: Record any anomalies, corrective actions taken.

### 7.2 Maintenance Requirements

**Scheduled maintenance**
- **Lubrication**: Every 25 flights, dry-film MoS₂ reapplication.
- **Inspection**: Every 50 flights, detailed examination with borescope.
- **Replacement**: Hinge pins every 500 flights, bushings every 1000 flights.
- **Calibration**: Position sensors every 100 flights, adjust zero/span as needed.

**Unscheduled maintenance**
- **Damage repair**: Minor damage field-repairable, major damage requires factory return.
- **Component replacement**: Modular design enables line replacement of major components.
- **Emergency procedures**: Manual control reversion, backup system activation.
- **Troubleshooting**: Built-in test equipment, fault isolation procedures.

---

## 8. Configuration Management

### 8.1 Interface Control

**Drawing control**
- **Interface drawings**: Detailed specifications for all physical interfaces.
- **Tolerance stack-up**: Analysis to ensure assembly compatibility.
- **Change control**: Engineering change process for interface modifications.
- **Configuration baseline**: Frozen configuration for production hardware.

**Software interfaces**
- **Control laws**: Interface specifications for flight control software.
- **Calibration data**: Position sensor scaling, temperature compensation.
- **Fault detection**: Interface monitoring, failure indication protocols.
- **Version control**: Software configuration management, interface compatibility.

### 8.2 Supplier Management

**Interface agreements**
- **Specification flow-down**: Ensure suppliers understand interface requirements.
- **Test requirements**: Specify interface testing at supplier level.
- **Quality agreements**: Interface quality standards, inspection requirements.
- **Configuration control**: Supplier change notification, approval process.

**Interface verification**
- **Supplier testing**: Witness testing of interface compliance.
- **Receiving inspection**: Verify interface dimensions, functionality.
- **Integration testing**: Full system testing with actual flight hardware.
- **First article approval**: Complete interface verification before production.

---

## 9. Safety & Risk Management

### 9.1 Safety Analysis

**Failure modes**
- **Hinge failure**: Loss of control surface, potential structural damage.
- **Actuator failure**: Reduced control authority, manual reversion required.
- **Position sensor failure**: Loss of feedback, open-loop control mode.
- **Thermal protection failure**: Structural damage, loss of vehicle.

**Risk mitigation**
- **Redundancy**: Dual actuators, independent control paths.
- **Fail-safe design**: Failure modes result in safe configuration.
- **Emergency procedures**: Manual control reversion, backup systems.
- **Monitoring**: Real-time health monitoring, early fault detection.

### 9.2 Hazard Analysis

**Hazard identification**
- **Mechanical**: Structural failure, control surface departure.
- **Thermal**: Overheating, thermal protection failure.
- **Electrical**: Short circuits, electromagnetic interference.
- **Human factors**: Maintenance errors, incorrect assembly.

**Hazard controls**
- **Design**: Inherently safe design, fail-safe operation.
- **Procedures**: Detailed maintenance procedures, inspection requirements.
- **Training**: Technician certification, recurring training.
- **Verification**: Independent inspection, functional testing.

---

## 10. Compliance & Certification

### 10.1 Regulatory Requirements

**FAA/AST compliance**
- **14 CFR Part 450**: Reusable launch vehicle requirements.
- **14 CFR Part 460**: Human spaceflight requirements.
- **Advisory Circulars**: Applicable guidance for commercial spaceflight.
- **Special conditions**: Vehicle-specific requirements as needed.

**International standards**
- **ECSS**: European Cooperation for Space Standardization (where applicable).
- **ISO**: International standards for quality, environmental management.
- **RTCA/EUROCAE**: Aviation standards for electronic systems.

### 10.2 Certification Evidence

**Design compliance**
- **Analysis reports**: Structural, thermal, functional analysis.
- **Test reports**: Component, subsystem, system level testing.
- **Quality records**: Manufacturing, inspection, configuration control.
- **Safety documentation**: Hazard analysis, failure modes, risk assessment.

**Operational compliance**
- **Flight test data**: Performance verification, envelope expansion.
- **Service experience**: Fleet operations, reliability data.
- **Maintenance procedures**: Demonstrated maintenance capability.
- **Training records**: Personnel certification, competency demonstration.

---

**Integration with UTCS/QS**: All interface requirements, test results, and operational data integrated into the Unified Technical Control System with full traceability to vehicle serial numbers, flight history, and maintenance records. Configuration control ensures interface compatibility throughout vehicle lifetime.**

---

*This Interface Control Document ensures seamless, safe, and reliable integration between lifting surface structure and control surface actuation systems, supporting successful AMPEL360 PLUS suborbital operations.*