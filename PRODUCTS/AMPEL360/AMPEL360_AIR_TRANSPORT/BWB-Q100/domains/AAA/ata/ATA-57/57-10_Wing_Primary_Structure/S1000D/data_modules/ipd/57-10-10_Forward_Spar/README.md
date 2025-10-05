# Forward Spar IPD

This directory contains Illustrated Parts Data (941A/B/C) for forward spar assemblies.

## Data Modules

### Sheet 1: DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml
**Forward Spar IPD - Overall Assembly**
- Main exploded view with 11 callouts
- Primary structure components (caps, web, fittings)
- Standard fasteners and hardware
- QSS sensor patch kit (optional)
- Formal `<applic>` blocks for LH/RH parts

### Sheet 2: DMC-BWQ1-A-57-10-10-00-01A-941B-D-EN-US.xml
**Forward Spar IPD - Sectional Views (LH/RH by Zone)**
- Inboard (FS-INB) sections: LH and RH with dedicated figures
- Midspan (FS-MID) sections: LH and RH with dedicated figures
- Outboard (FS-OUTB) sections: LH and RH with dedicated figures
- Zone-specific part numbers and effectivity
- Formal `<applic>` filtering per group (LH/RH, FS-INB/MID/OUTB)

### Sheet 3: DMC-BWQ1-A-57-10-10-00-02A-941C-D-EN-US.xml
**Forward Spar IPD - QSS Provisioning Bill**
- QSS-only bill of materials for avionics provisioning
- Sensor patch kits by zone (INB, MID, OUTB)
- Harness assembly and controller unit
- Installation materials and hardware
- Documentation and tooling kits
- Formal `<applic>` for OPT-QSS-FS option

## Major Assemblies

- Forward spar inboard LH/RH assemblies (FS-INB)
- Forward spar mid sections with shear ties (FS-MID)
- Forward spar outboard sections (FS-OUTB)
- Caps (upper/lower) with composite plies (IM7/8552)
- Webs with composite construction
- Fastener kits by zone (Hi-Lok, washers, nuts)
- Root fittings (metallic, corrosion-protected)
- Quantum Sensorial Skin (QSS) sensor kits (optional)

## Graphics

All IPD sheets reference SVG callout templates located in:
- **graphics/ipd/** — Exploded view templates with consistent callout IDs

See `graphics/ipd/README.md` for detailed template usage instructions.

## Schema References

- **IPD schema**: `../../../schema/shims/ipd.xsd`
- **Schema catalog**: `../../../schema/catalog.xml`

## Effectivity Management

All IPD sheets use formal S1000D `<applic>` blocks for:
- **LH/RH filtering**: Left-hand vs. right-hand parts
- **Zone filtering**: FS-INB, FS-MID, FS-OUTB regions
- **Option filtering**: OPT-QSS-FS for Quantum Sensorial Skin provisioning

---

*Part of ATA-57-10 IPD documentation*
