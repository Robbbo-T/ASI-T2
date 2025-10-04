# CSDB Graphics Repository

This directory contains graphical assets referenced by S1000D data modules.

## Required Graphics for Forward Spar (57-10-10) Modules

The following graphics are referenced in the Forward Spar data modules and need to be created:

### FIG-57-10-720-REMOVAL
**Referenced in:** DMC-BWBQ100-A-57-10-10-00-01A-720A-D-EN-US.xml  
**Title:** Typical Access Panel — Removal Sequence  
**Description:** Illustrates the step-by-step sequence for removing forward spar access panels  
**Status:** ⚠️ Placeholder - Graphics to be created

### FIG-57-10-720-INSTALL
**Referenced in:** DMC-BWBQ100-A-57-10-10-00-01A-720A-D-EN-US.xml  
**Title:** Typical Access Panel — Installation Sequence  
**Description:** Illustrates the step-by-step sequence for installing forward spar access panels with proper torque sequence  
**Status:** ⚠️ Placeholder - Graphics to be created

### FIG-57-10-10-QSS-PATCHES
**Referenced in:** DMC-BWBQ100-A-57-10-10-00-00A-941A-D-EN-US.xml  
**Title:** QSS Patch Locations — Forward Spar  
**Description:** Illustrates the locations of QSS sensor patches on the forward spar (inboard, mid, and outboard stations)  
**Status:** ⚠️ Placeholder - Graphics to be created

## Graphics Format Standards

All graphics should conform to S1000D Issue 6.0 requirements:
- **Format:** CGM, SVG, PNG, or JPEG
- **Resolution:** Minimum 300 DPI for raster images
- **Color:** Use approved color palette for technical illustrations
- **Naming:** Use `infoEntityIdent` as filename base

## External Publication References

The following external publications are referenced and should be available in the technical library:

### QSS Sensor Patch References
- **QSS-FS-INB-01** - QSS Patch — Inboard Station
- **QSS-FS-MID-01** - QSS Patch — Mid Station
- **QSS-FS-OUTB-01** - QSS Patch — Outboard Station

### Layup and Standard Practices
- **LAYUP-FS-V1** - Forward Spar Layup Schema v1
- **STD-STRUCT-INSPECT** - Structural Inspection Standard Practices
- **STD-STRUCT-TORQUE** - Standard Practices — Fastener Torque and Re-use

## Graphics Creation Workflow

1. Create technical illustration following S1000D standards
2. Save in approved format(s)
3. Place in this directory with `infoEntityIdent` as filename
4. Update this README with status
5. Reference in data module using `<graphic infoEntityIdent="..."/>`

## Integration Notes

Graphics should be stored in the Common Source Database (CSDB) structure:
```
CSDB/
├── DMC/          # Data modules (XML)
└── graphics/     # Referenced graphics
    ├── FIG-57-10-720-REMOVAL.svg
    ├── FIG-57-10-720-INSTALL.svg
    └── FIG-57-10-10-QSS-PATCHES.svg
```

---

*Graphics repository maintained as part of ASI-T2 S1000D CSDB*
