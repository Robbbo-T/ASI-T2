# Forward Spar IPD

This directory contains Illustrated Parts Data (IPD; 941A/B/C) for forward spar assemblies of the AMPEL360 BWB-Q100 wing, structured for S1000D Issue 6.0.

## Data Modules

### DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml (Sheet 1)
**Forward Spar IPD – Master Assembly**
- Main exploded view with 11 callouts
- Primary structure components (caps, web, fittings)
- Standard fasteners and hardware
- QSS sensor patch kit (optional)
- References all sub-assemblies and uses formal `<applic>` blocks for LH/RH parts
- Issue: 001-00 | Date: 2025-10-04 | Location: `CSDB/DMC/`

### DMC-BWQ1-A-57-10-10-00-01A-941B-D-EN-US.xml (Sheet 2)
**Sectional Views (LH/RH by Zone)**
- Inboard (FS-INB), Midspan (FS-MID), Outboard (FS-OUTB) sections: LH and RH with dedicated figures/groups
- Zone-specific part numbers and effectivity
- Formal `<applic>` filtering per group (LH/RH, FS-INB/MID/OUTB)

### DMC-BWQ1-A-57-10-10-00-02A-941C-D-EN-US.xml (Sheet 3)
**QSS Provisioning BOM**
- QSS-only bill of materials for avionics provisioning
- Sensor patch kits by zone (INB, MID, OUTB)
- Harness assembly and controller unit
- Installation materials, hardware, documentation, and tooling kits
- Formal `<applic>` for OPT-QSS-FS option

## Major Assemblies

- Forward spar inboard LH/RH assemblies (FS-INB)
- Forward spar mid sections with shear ties (FS-MID)
- Forward spar outboard sections (FS-OUTB)
- Caps (upper/lower; IM7/8552 composite)
- Webs with composite construction
- Fastener kits by zone (Hi-Lok, washers, nuts)
- Root fittings (metallic, corrosion-protected)
- Quantum Sensorial Skin (QSS) sensor kits (optional)

## Graphics

All IPD sheets reference SVG callout templates located in:
- **graphics/ipd/** — Exploded view templates with consistent callout IDs

See `graphics/ipd/README.md` for detailed template usage instructions.

## Effectivity Management

All IPD sheets use formal S1000D `<applic>` blocks for:
- **LH/RH filtering**: Left-hand vs. right-hand parts
- **Zone filtering**: FS-INB, FS-MID, FS-OUTB regions
- **Option filtering**: OPT-QSS-FS for Quantum Sensorial Skin provisioning

## Additional Resources

- **IMPLEMENTATION_SUMMARY.md**: Complete BOM tables, category summaries, and CAx/CAM/CAV integration guidelines
- **data/forward_spar_bom.csv**: CSV export of all parts for import into PLM/ERP systems

## Schema References

- **IPD schema**: `../../../schema/shims/ipd.xsd`
- **Schema catalog**: `../../../schema/catalog.xml`

---

*Part of ATA-57-10 IPD documentation*