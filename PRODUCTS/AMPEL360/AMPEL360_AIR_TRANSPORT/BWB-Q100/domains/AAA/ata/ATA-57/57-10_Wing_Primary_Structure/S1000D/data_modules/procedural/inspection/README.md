# Inspection Procedures - Wing Primary Structure

This directory contains S1000D inspection procedural data modules (Info Code 520A) for wing primary structure components.

## Purpose

Inspection procedures define:
- Inspection methods (visual, NDT, functional)
- Inspection intervals and triggers
- Acceptance criteria and allowable limits
- Required tools and equipment
- Inspection access requirements
- Discrepancy reporting and documentation

## Inspection Types

### Visual Inspection
- Surface condition assessment
- Corrosion/erosion detection
- Lightning strike damage
- Impact damage
- Fastener condition (protruding heads, missing fasteners)
- Sealant condition
- Paint/coating condition

### Non-Destructive Testing (NDT)
- **Ultrasonic (UT)**: Delamination detection, bondline integrity, thickness measurement
- **Eddy Current (EC)**: Crack detection in metallic fittings and fastener holes
- **Thermography**: Disbond/delamination detection in large areas
- **Tap Test**: Quick disbond screening
- **Dye Penetrant (PT)**: Surface crack detection in metallic parts
- **Magnetic Particle (MT)**: Crack detection in ferrous parts

### Special Inspections
- Fuel leak checks
- Bond resistance measurements (EMI/lightning protection)
- Fastener torque verification (sampling)
- Clearance measurements

## Component Coverage

### 57-10-10 Forward Spar
Inspection focus areas:
- Splice joints (eddy current for cracks)
- Cap-to-web bondlines (ultrasonic)
- Attachment fittings (dye penetrant)
- Critical fastener holes
- Load introduction areas

### 57-10-20 Rear Spar
Inspection focus areas:
- Hinge fitting attachment points
- Landing gear beam bolt holes
- Actuator cutout reinforcements
- Control surface hinge bushings

### 57-10-30 Ribs
Inspection focus areas:
- Web buckling
- Flange cracks at spar attachments
- Fuel tank seal integrity
- Corrosion in metal fittings

### 57-10-40 Skin Panels
Inspection focus areas:
- Lightning strike damage zones
- Impact damage (tool drops, hail, bird strikes)
- Delamination/disbond
- Fuel leak evidence
- Erosion at leading edges

### 57-10-50 Stringers
Inspection focus areas:
- Stringer debonds from skin
- Runout condition
- Crack initiation at terminations

### 57-10-60 Attachments
Inspection focus areas:
- Bearing surface wear
- Crack initiation at stress concentrations
- Bolt hole condition
- Corrosion protection integrity

## Inspection Intervals

Defined in Maintenance Planning Document (MPD):
- A-Check items (daily/weekly)
- C-Check items (18-24 months)
- D-Check items (6-10 years)
- Condition monitoring (continuous/sampling)
- Special inspections (post-incident, modification, repair)

## Quality Forms

All inspection results must be documented on:
- Inspection records (component-specific)
- NDT reports (method-specific)
- Discrepancy logs
- Evidence capture for traceability

## References

- **Descriptive modules**: `../../descriptive/` for component details
- **Acceptance criteria**: `../../../../contracts/schemas/acceptance.metric.schema.json`
- **Evidence storage**: `../../../../evidence/ndt/`
- **ATA-20 forms**: Standard inspection practices

---

*Part of ATA-57-10 procedural documentation*
