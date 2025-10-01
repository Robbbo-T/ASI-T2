# Attachments - Descriptive Data Modules

This directory contains descriptive data modules (040A) for major structural attachment fittings of the BWB-Q100 wing.

## Scope

Attachment fittings are critical metallic or hybrid structures that transfer concentrated loads between the wing and other aircraft systems or structures. These fittings are designed as fail-safe, life-limited components with strict inspection requirements.

## Data Modules

### DMC-BWQ1-A-57-10-60-00-00A-040A-D-EN-US.xml
**Attachments - General Description, Fitting Design Philosophy**
- Fitting classification and types
- Material specifications (titanium, high-strength steel)
- Load introduction philosophy
- Fail-safe design principles
- Inspection and life limits

### DMC-BWQ1-A-57-10-60-01-00A-040A-D-EN-US.xml
**Wing-to-Fuselage Fittings**
- Center section main attachment pins
- Fuselage frame interface
- Shear and moment transfer mechanisms
- Bearing surfaces and bushings

### DMC-BWQ1-A-57-10-60-02-00A-040A-D-EN-US.xml
**Engine Mount Fittings**
- Thrust load transfer
- Vertical and lateral load paths
- Pylon interface definition
- Vibration isolation provisions

### DMC-BWQ1-A-57-10-60-03-00A-040A-D-EN-US.xml
**Landing Gear Beam Fittings**
- Main gear attachment points
- Reaction loads (vertical, drag, side)
- Beam-to-spar interface
- Fail-safe features

### DMC-BWQ1-A-57-10-60-04-00A-040A-D-EN-US.xml
**Control Surface Hinge Fittings**
- Hinge moment transfer
- Bushing and bearing details
- Actuator attachment provisions
- Tolerance and clearance requirements

## Key Features

- **Material**: High-strength titanium alloy (Ti-6Al-4V), stainless steel (AM350/PH13-8Mo)
- **Load Function**: Concentrated load introduction, fail-safe load paths
- **Critical Areas**: Bearing surfaces, bolt holes, weld joints, stress concentrations
- **Interfaces**: Fuselage (ATA-53), engines (ATA-71), landing gear (ATA-32), control surfaces (ATA-57-20)

## Design Requirements

- **Fail-Safe**: Multiple load paths or crack-arrest features
- **Life Limits**: Cyclic life based on fatigue spectrum
- **Inspection**: NDT at defined intervals (eddy current, ultrasonic, magnetic particle)
- **Tolerances**: Tight tolerances for bearing fits and pin alignment

## Load Categories

- **Primary Structure**: Wing-to-fuselage, landing gear beam
- **Secondary Structure**: Engine mounts (forward/aft)
- **Flight Control**: Hinge fittings, actuator brackets

## References

- **Procedural Modules**: 
  - Inspection: `../../procedural/inspection/57-10-60_Attachments/`
- **IPD**: `../../ipd/57-10-60_Attachments/`
- **ICDs**: 
  - `../../../../icd/ICD-57-10-53_Fuselage_Attachments.md`
  - `../../../../icd/ICD-57-10-57-20_Control_Surfaces.md`
- **Schemas**: `../../../../contracts/schemas/attachment.fitting.schema.json`

## Compliance Links

- Load cases: `../../../../compliance/loads/`
- Stress analysis: `../../../../compliance/stress/`
- Material allowables: `../../../../compliance/allowables/`
- Fatigue analysis: `../../../../evidence/tests/`

## ATA-20 Forms

- Material Handling: `../../../../ATA-20/20-30_Material_Handling/forms/FORM-QA-20-30-01_Material_Handling_OOC_Log.md`

---

*Part of ATA-57-10 Wing Primary Structure descriptive documentation*
