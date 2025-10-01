# Stringers - Descriptive Data Modules

This directory contains descriptive data modules (040A) for the stringer structure of the BWB-Q100 wing.

## Scope

Stringers are longitudinal stiffening members bonded or fastened to the inner surface of skin panels. They provide local buckling resistance and enhance the load-carrying capability of the skin.

## Data Modules

### DMC-BWQ1-A-57-10-50-00-00A-040A-D-EN-US.xml
**Stringers - General Description, Spanwise Arrangement**
- Stringer types and cross-sections
- Spacing and arrangement philosophy
- Material specifications
- Load function and design rationale

### DMC-BWQ1-A-57-10-50-01-00A-040A-D-EN-US.xml
**Upper Stringers LH**
- Compression members for upper wing skin
- Section properties (hat, blade, T-section)
- Runout and termination details
- Splice locations

### DMC-BWQ1-A-57-10-50-02-00A-040A-D-EN-US.xml
**Upper Stringers RH**
- Symmetric configuration to LH
- Section properties

### DMC-BWQ1-A-57-10-50-03-00A-040A-D-EN-US.xml
**Lower Stringers LH**
- Tension members for lower wing skin
- Splice design
- Rib intersection details

### DMC-BWQ1-A-57-10-50-04-00A-040A-D-EN-US.xml
**Lower Stringers RH**
- Symmetric configuration
- Section properties

## Key Features

- **Material**: Carbon fiber epoxy composite, typically co-cured or co-bonded with skin
- **Load Function**: Skin panel buckling resistance, axial load sharing
- **Critical Areas**: Runouts, splices, rib intersections
- **Interfaces**: Skins (57-10-40), ribs (57-10-30)

## Stringer Types

- **Hat Section**: Closed section for high compression loads (upper surface)
- **Blade/T Section**: Open section for moderate loads
- **I/Omega Section**: Specialty sections at specific locations

## Design Features

- **Runouts**: Gradual termination to avoid stress concentrations
- **Splices**: Overlap or butt joints with fasteners or bonding
- **Rib Passages**: Continuous through ribs or terminated and restarted
- **Terminations**: At panel edges, large cutouts, and load introduction points

## References

- **Procedural Modules**: 
  - Inspection: `../../procedural/inspection/57-10-50_Stringers/`
- **IPD**: `../../ipd/57-10-50_Stringers/`
- **Schemas**: `../../../../contracts/schemas/laminate.stack.schema.json`

## Compliance Links

- Load cases: `../../../../compliance/loads/`
- Stress analysis: `../../../../compliance/stress/`
- Material allowables: `../../../../compliance/allowables/`

## ATA-20 Forms

- Composite Fastening: `../../../../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`
- Adhesive Bonding: `../../../../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`

---

*Part of ATA-57-10 Wing Primary Structure descriptive documentation*
