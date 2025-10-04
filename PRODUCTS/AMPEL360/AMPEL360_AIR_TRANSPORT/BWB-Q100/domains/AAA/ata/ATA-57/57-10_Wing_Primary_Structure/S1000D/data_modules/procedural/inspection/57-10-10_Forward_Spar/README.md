# Forward Spar Inspection Procedures

This directory contains inspection procedural data modules (520A) for the forward spar structure.

## Data Modules

### DMC-BWQ1-A-57-10-10-00-00A-520A-D-EN-US.xml
**Forward Spar Inspection - Visual, NDT methods, intervals**
- General inspection philosophy
- Inspection zones and access requirements
- Visual inspection criteria
- NDT method selection (UT, EC, thermography)
- Inspection intervals per MPD
- Tools and equipment required

### DMC-BWQ1-A-57-10-10-01-00A-520A-D-EN-US.xml
**Inboard Section LH Inspection**
- Critical zones for crack initiation
- Attachment fitting inspection (dye penetrant)
- Web-to-cap bondline inspection (ultrasonic)
- Fastener hole inspection (eddy current)

### DMC-BWQ1-A-57-10-10-02-00A-520A-D-EN-US.xml
**Inboard Section RH Inspection**
- Critical zones symmetric to LH
- Fuel tank seal verification

### DMC-BWQ1-A-57-10-10-03-00A-520A-D-EN-US.xml
**Mid Section LH Inspection**
- Splice joint eddy current procedure
- Bolt hole inspection
- Load transfer verification

### DMC-BWQ1-A-57-10-10-04-00A-520A-D-EN-US.xml
**Mid Section RH Inspection**
- Splice joint inspection

### DMC-BWQ1-A-57-10-10-05-00A-520A-D-EN-US.xml
**Outboard Section LH Inspection**
- Tip attachment ultrasonic inspection
- Hinge fitting condition check

### DMC-BWQ1-A-57-10-10-06-00A-520A-D-EN-US.xml
**Outboard Section RH Inspection**
- Tip attachment ultrasonic inspection

## Inspection Focus Areas

### Critical Zones
- Wing-to-fuselage attachment fittings
- Splice joints (high stress concentration)
- Cap-to-web bondlines
- Load introduction points
- Fastener holes in high-cycle areas

### Visual Inspection
- Surface condition (scratches, erosion, corrosion)
- Impact damage
- Fuel leaks or staining
- Fastener condition (missing, loose, protruding heads)
- Sealant condition

### NDT Methods

#### Ultrasonic (UT)
- Cap-to-web bondline integrity
- Laminate delaminations
- Thickness measurements
- Internal voids

#### Eddy Current (EC)
- Fastener hole cracks
- Surface and subsurface cracks in metallic fittings
- Splice bolt hole inspection

#### Thermography
- Large area disbond/delamination screening
- Rapid survey method

#### Dye Penetrant (PT)
- Surface cracks in metallic fittings
- Attachment fitting bolt holes

## Acceptance Criteria

Defined in `../../../../contracts/schemas/acceptance.metric.schema.json`:
- No cracks in critical areas
- Delaminations < 1 inch in non-critical areas
- Bondline voids < 0.5% of area
- Fuel leak: none detectable
- Corrosion: none in critical areas, minor in non-critical

## Inspection Intervals

Per Maintenance Planning Document (MPD):
- **A-Check**: Visual inspection of accessible areas
- **C-Check**: Detailed visual + NDT sample
- **D-Check**: Complete NDT survey
- **Special**: Post-incident, post-repair, pre-flight after maintenance

## Evidence Capture

All inspection results documented in:
- `../../../../evidence/ndt/` index
- Inspection forms (component-specific)
- NDT reports with technician certification
- Photographic evidence for findings

## References

- **Schema Files**:
  - Procedural schema: `../../../../schema/shims/procedural.xsd`
  - Schema catalog: `../../../../schema/catalog.xml`
- **Descriptive module**: `../../descriptive/57-10-10_Forward_Spar/`
- **Acceptance criteria**: `../../../../contracts/schemas/acceptance.metric.schema.json`
- **Evidence storage**: `../../../../evidence/ndt/`

---

*Part of ATA-57-10 procedural inspection documentation*
