# Rear Spar - Descriptive Data Modules

This directory contains descriptive data modules (040A) for the rear spar structure of the BWB-Q100 wing.

## Scope

The rear spar is the aft primary load-bearing member, providing structural support for control surfaces and transferring flight control loads into the wing box. It also interfaces with the landing gear beam in the inboard section.

## Data Modules

### DMC-BWQ1-A-57-10-20-00-00A-040A-D-EN-US.xml
**Rear Spar - General Description & Load Paths**
- Overall configuration and structural function
- Load paths and design philosophy
- Material specifications
- Section breakdown
- Control surface interface philosophy

### DMC-BWQ1-A-57-10-20-01-00A-040A-D-EN-US.xml
**Rear Spar Inboard Section LH**
- Landing gear beam interface details
- Heavy-duty fitting provisions
- Material layup

### DMC-BWQ1-A-57-10-20-02-00A-040A-D-EN-US.xml
**Rear Spar Inboard Section RH**
- Landing gear beam interface details
- Symmetric configuration to LH

### DMC-BWQ1-A-57-10-20-03-00A-040A-D-EN-US.xml
**Rear Spar Mid Section LH**
- Control surface hinge locations
- Elevon attachment provisions
- Actuator cutouts

### DMC-BWQ1-A-57-10-20-04-00A-040A-D-EN-US.xml
**Rear Spar Mid Section RH**
- Control surface hinge locations
- Symmetric configuration

### DMC-BWQ1-A-57-10-20-05-00A-040A-D-EN-US.xml
**Rear Spar Outboard Section LH**
- Aileron support structure
- Taper and tip details

### DMC-BWQ1-A-57-10-20-06-00A-040A-D-EN-US.xml
**Rear Spar Outboard Section RH**
- Aileron support structure

### DMC-BWQ1-A-57-10-20-07-00A-040A-D-EN-US.xml
**Rear Spar Upper Cap**
- Tension loads in flight
- Splice design and load transfer
- Composite layup

### DMC-BWQ1-A-57-10-20-08-00A-040A-D-EN-US.xml
**Rear Spar Lower Cap**
- Compression loads in flight
- Anti-buckling provisions
- Stiffener integration

### DMC-BWQ1-A-57-10-20-09-00A-040A-D-EN-US.xml
**Rear Spar Web**
- Shear transfer mechanisms
- Actuator cutout reinforcements
- Hinge fitting attachment provisions

## Key Features

- **Material**: Carbon fiber epoxy composite with metallic fittings
- **Load Function**: Aft closure of wing box, flight control load transfer
- **Critical Areas**: Hinge fittings, landing gear beam interface, actuator cutouts
- **Interfaces**: Control surfaces (ATA-57-20), landing gear (ATA-32), forward spar (57-10-10)

## References

- **Procedural Modules**: 
  - Inspection: `../../procedural/inspection/57-10-20_Rear_Spar/`
  - R/I: `../../procedural/removal_installation/57-10-20_Rear_Spar/`
  - Repair: `../../procedural/repair/57-10-20_Rear_Spar/`
- **IPD**: `../../ipd/57-10-20_Rear_Spar/`
- **ICD**: `../../../../icd/ICD-57-10-57-20_Control_Surfaces.md`
- **Schemas**: `../../../../contracts/schemas/attachment.fitting.schema.json`

## Compliance Links

- Load cases: `../../../../compliance/loads/`
- Stress analysis: `../../../../compliance/stress/`
- Material allowables: `../../../../compliance/allowables/`

---

*Part of ATA-57-10 Wing Primary Structure descriptive documentation*
