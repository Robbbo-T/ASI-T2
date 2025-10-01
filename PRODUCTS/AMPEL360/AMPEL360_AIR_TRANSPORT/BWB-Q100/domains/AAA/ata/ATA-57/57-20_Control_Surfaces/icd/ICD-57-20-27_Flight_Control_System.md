# ICD — ATA-57-20 ↔ ATA-27 (Flight Controls)

Defines mechanical/geometric/clearance interfaces and hinge moment sign conventions.

## Interface Scope

This ICD defines the interfaces between:
- **ATA-57-20**: Control surface structural elements
- **ATA-27**: Flight control system (actuation, kinematics, signaling)

## Mechanical Interfaces

### Control Surface Kinematics
- Angular range of motion (deflection limits)
- Rotational axes and hinge line definitions
- Clearance envelopes during motion
- Stop positions and mechanical limits

### Hinge Moment Convention
- Sign convention for hinge moments
- Positive/negative directions
- Reference axes and coordinate systems
- Moment arm definitions

### Actuator Interface Points
- Attachment locations on control surfaces
- Rod-end and clevis specifications
- Load transfer mechanisms
- Mechanical tolerances

## Functional Requirements

### From ATA-27 to ATA-57-20
- Maximum actuation force requirements
- Frequency response requirements
- Position accuracy requirements
- Rate of motion requirements

### From ATA-57-20 to ATA-27
- Hinge moment envelopes (all flight conditions)
- Inertia properties (mass, CG, moments of inertia)
- Natural frequencies and damping
- Structural stiffness at actuator attachment points

## Validation & Acceptance

### Interface Verification
- Fit checks and clearance verification
- Kinematic validation tests
- Load path verification
- Actuation force measurements

### Acceptance Criteria
- Maximum hinge friction: ≤ 0.5 Nm (typical)
- Position accuracy: ±0.5 mm
- Clearance margins: minimum 5 mm (all conditions)

## References

- ATA-27-XX Flight Control System ICD
- Control Surface Load Specifications (compliance/loads_index.md)
- Hinge Design Specifications (contracts/schemas/hinge.schema.json)

---
*Part of BWB-Q100 ICD framework. Controlled under configuration management.*
