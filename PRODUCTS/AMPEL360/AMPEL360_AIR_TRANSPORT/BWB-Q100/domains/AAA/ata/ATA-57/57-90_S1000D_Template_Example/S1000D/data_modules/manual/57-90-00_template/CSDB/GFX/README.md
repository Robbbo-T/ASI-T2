# GFX - Graphics

**Parent:** [../](../)

## Purpose

This directory contains all graphics, illustrations, and images referenced by S1000D data modules. Graphics provide visual representation of systems, components, procedures, and parts to support technical documentation.

## Contents

### fig_overview.svg (2.5 KB)

**Type:** System Overview Diagram  
**Format:** SVG (Scalable Vector Graphics)  
**ICN:** ICN-BWQ1-57-90-00-001  
**Referenced by:** Descriptive DM (040A)

**Purpose:** Provides a high-level visual overview of the system showing:
- Main assembly components
- Component relationships
- Interface points
- Fastener locations

**Features:**
- Scalable without quality loss
- Professional styling with labels
- Color-coded components
- Clear callouts and annotations

### ipd_exploded.svg (3.6 KB)

**Type:** Exploded View Diagram  
**Format:** SVG (Scalable Vector Graphics)  
**ICN:** ICN-BWQ1-57-90-00-901  
**Referenced by:** IPD DM (941A)

**Purpose:** Shows exploded view of assembly for parts identification:
- Numbered callouts (1, 2, 3)
- Explosion lines showing assembly relationships
- Assembly direction arrows
- Integrated parts table

**Features:**
- Callout numbers match part sequence in IPD
- Clear spatial relationships
- Assembly/disassembly indicators
- Professional technical illustration style

## Graphic File Formats

### Recommended: SVG (Scalable Vector Graphics)

**Advantages:**
- ✅ Scalable without quality loss
- ✅ Small file size
- ✅ Text remains searchable
- ✅ Editable with vector tools
- ✅ Standards-compliant (SVG 1.1)
- ✅ Renders well on all devices

**Use for:** Technical diagrams, schematics, exploded views, flowcharts

### Also Supported: Raster Formats

**PNG:** Use for photographs, screenshots, complex images  
**JPEG:** Use for photographic content where file size matters

## Graphic Naming Conventions

### Descriptive Names
Use clear, descriptive filenames:
```
fig_overview.svg          (System overview figure)
ipd_exploded.svg          (Exploded view for IPD)
schematic_electrical.svg  (Electrical schematic)
photo_installation.png    (Installation photograph)
```

### Info Entity Ident (ICN)

Each graphic should have a unique ICN for traceability:
```
ICN-<MIC>-<SC>-<SSC>-<SSSC>-<SeqNo>

Examples:
ICN-BWQ1-57-90-00-001    (First graphic)
ICN-BWQ1-57-90-00-002    (Second graphic)
ICN-BWQ1-57-90-00-901    (IPD graphic)
```

## Referencing Graphics from Data Modules

### Basic Reference

```xml
<graphic infoEntityIdent="ICN-BWQ1-57-90-00-001" 
         xlink:href="../GFX/fig_overview.svg" 
         xlink:title="Overview Diagram"/>
```

### Within a Figure

```xml
<figure>
  <title>System Overview</title>
  <graphic infoEntityIdent="ICN-BWQ1-57-90-00-001" 
           xlink:href="../GFX/fig_overview.svg" 
           xlink:title="Overview Diagram"/>
</figure>
```

### With Callouts (IPD)

```xml
<figure id="fig-IPD-1">
  <title>Assembly — Exploded View</title>
  <graphic infoEntityIdent="ICN-BWQ1-57-90-00-901" 
           xlink:href="../GFX/ipd_exploded.svg" 
           xlink:title="Exploded View"/>
</figure>
```

## Adding New Graphics

1. **Create graphic** using appropriate tool:
   - Vector graphics: Inkscape, Adobe Illustrator, etc.
   - Raster graphics: GIMP, Photoshop, etc.

2. **Save in GFX directory** with descriptive filename

3. **Assign ICN** following the convention

4. **Reference from DM** using `<graphic>` element with relative path

5. **Update callouts** if used in IPD

## Graphic Creation Guidelines

### Technical Diagrams
- Use clear, simple lines
- Label all important components
- Include scale or dimensions if relevant
- Use consistent line weights
- Add reference coordinates if applicable

### Exploded Views
- Show clear spatial relationships
- Number parts sequentially
- Use explosion lines to show assembly
- Include assembly direction arrows
- Ensure callout numbers are visible

### Schematics
- Follow industry standards (IEEE, ISO)
- Use standard symbols
- Label all connections
- Include legend if needed
- Show signal/power flow direction

### Photographs
- Use good lighting
- High resolution (300 DPI minimum for print)
- Include scale reference
- Crop to relevant area
- Annotate if necessary

## SVG Best Practices

✅ **Keep it simple** - Avoid unnecessary complexity  
✅ **Optimize paths** - Remove redundant points  
✅ **Use layers** - Organize elements logically  
✅ **Embed fonts** - Or convert text to paths  
✅ **Set viewBox** - For proper scaling  
✅ **Include metadata** - Title, description, ICN

## File Size Considerations

- **SVG files:** Should typically be under 100 KB
- **PNG files:** Optimize for web, balance quality vs. size
- **JPEG files:** Use appropriate compression (80-90% quality)

If files are too large:
- Simplify vector graphics
- Reduce image resolution
- Use appropriate compression
- Consider splitting into multiple graphics

## Validation

Check graphics are valid and accessible:

```bash
# Validate SVG files
for f in *.svg; do
  xmllint --noout "$f" && echo "✓ $f valid"
done

# Check file sizes
du -h *.svg *.png *.jpg 2>/dev/null

# Verify references in DMs
grep -r "xlink:href.*GFX" ../DMC/
```

## Tools for Creating Graphics

### Vector Graphics (Recommended)
- **Inkscape** (Free, open-source)
- **Adobe Illustrator** (Commercial)
- **CorelDRAW** (Commercial)
- **LibreOffice Draw** (Free)

### Raster Graphics
- **GIMP** (Free, open-source)
- **Adobe Photoshop** (Commercial)
- **Krita** (Free)

### Technical Drawing
- **LibreCAD** (Free, 2D CAD)
- **FreeCAD** (Free, 3D CAD)
- **AutoCAD** (Commercial)

## Standards Compliance

- SVG 1.1 specification
- XLink 1.0 for references
- S1000D Issue 6.0 graphics requirements
- ISO 15926 (for technical illustration where applicable)

## Related Documentation

- [CSDB README](../README.md) - Parent directory
- [DMC Directory](../DMC/) - Data modules that reference these graphics
- [S1000D Specification](http://www.s1000d.org) - Graphics requirements

---

**Important:** Always use relative paths (../GFX/filename) when referencing graphics from data modules to ensure portability of the CSDB structure.
