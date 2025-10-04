# Forward Spar IPD

This directory contains Illustrated Parts Data (941A) for forward spar assemblies.

## Data Modules

### DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml
**Forward Spar IPD - Master Assembly**
- Master IPD with references to all sub-assemblies
- Issue: 001-00
- Date: 2025-10-04
- Location: `CSDB/DMC/`

### DMC-BWQ1-A-57-10-10-01-00A-941A-D-EN-US.xml
**Inboard Sections IPD - Part numbers, quantities**
- Covers BL0-BL160 zone
- Includes structural components, fastener kits, and QSS components
- Issue: 002-00
- Date: 2025-09-15
- Location: `CSDB/DMC/`
- 9 parts cataloged

### DMC-BWQ1-A-57-10-10-02-00A-941A-D-EN-US.xml
**Mid Sections IPD - Splice kit components**
- Covers BL160-BL320 zone
- Includes CFRP components, splice kits, fasteners, and QSS components
- Issue: 002-01
- Date: 2025-09-28
- Location: `CSDB/DMC/`
- 11 parts cataloged

### DMC-BWQ1-A-57-10-10-03-00A-941A-D-EN-US.xml
**Outboard Sections IPD - Tip attachments**
- Covers BL240-BL400 zone (wing tip)
- Includes tip fittings, aileron hinges, fasteners, and QSS components
- Issue: 001-02
- Date: 2025-08-22
- Location: `CSDB/DMC/`
- 16 parts cataloged

## Major Assemblies

- Forward spar inboard LH/RH assemblies
- Forward spar mid sections with splice kits
- Forward spar outboard sections
- Caps (upper/lower) with composite plies
- Webs with stiffeners
- Fastener kits by zone
- Splice hardware kits

## Additional Resources

- **IMPLEMENTATION_SUMMARY.md**: Complete BOM tables, category summaries, and CAx/CAM/CAV integration guidelines
- **data/forward_spar_bom.csv**: CSV export of all parts for import into PLM/ERP systems

## Schema References

- **IPD schema**: `../../../schema/shims/ipd.xsd`
- **Schema catalog**: `../../../schema/catalog.xml`

## Statistics

- **Total Parts**: 36 unique part numbers
- **Total DMCs**: 3 detailed IPD modules + 1 master
- **Categories**: Structural (18+32+38), Fastener Kits (2+2+3), QSS Components (6+10+7), Splice Kits (2)

---

*Part of ATA-57-10 IPD documentation*
