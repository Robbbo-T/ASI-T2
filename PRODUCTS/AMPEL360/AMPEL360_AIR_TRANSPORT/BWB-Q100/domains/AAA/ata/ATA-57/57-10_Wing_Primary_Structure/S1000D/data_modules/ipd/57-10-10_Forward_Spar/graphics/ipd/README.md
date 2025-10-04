# Forward Spar IPD Graphics

This directory contains SVG callout templates for Forward Spar Illustrated Parts Data (IPD) documentation.

## SVG Templates

All SVG files in this directory are **callout templates** for technical illustrators. The geometry is placeholder only; actual detailed spar geometry should replace the placeholder elements while preserving the callout structure and IDs.

### Template Files

#### Sheet 1 - Overall Assembly
- **FS_exploded.svg** - Main assembly exploded view with 11 callouts
  - Callout 1: Forward Spar Assembly
  - Callout 2: Upper Cap, LH
  - Callout 3: Upper Cap, RH
  - Callout 4: Lower Cap, LH
  - Callout 5: Lower Cap, RH
  - Callout 6: Web, Composite
  - Callout 7: Root Fitting, Inboard
  - Callout 8: Shear Tie, Midspan (typical)
  - Callout 9: Attachment Bracket, Rib (typical)
  - Callout 10: Fastener Set (Hi-Lok/Washer/Nut), typical
  - Callout 11: QSS Sensor Patch Kit (optional)

#### Sheet 2 - Sectional Views (LH/RH by Zone)

##### Inboard Section
- **FS_INB_LH_exploded.svg** - Inboard LH section with 6 callouts
  - Callout 1: Upper Cap, LH (INB)
  - Callout 2: Lower Cap, LH (INB)
  - Callout 3: Web, Composite (INB)
  - Callout 4: Root Fitting LH
  - Callout 5: Rib Bracket (typ)
  - Callout 6: QSS Patch (optional)

- **FS_INB_RH_exploded.svg** - Inboard RH section with 6 callouts
  - Callout 1: Upper Cap, RH (INB)
  - Callout 2: Lower Cap, RH (INB)
  - Callout 3: Web, Composite (INB)
  - Callout 4: Root Fitting RH
  - Callout 5: Rib Bracket (typ)
  - Callout 6: QSS Patch (optional)

##### Midspan Section
- **FS_MID_LH_exploded.svg** - Midspan LH section with 6 callouts
  - Callout 1: Upper Cap, LH (MID)
  - Callout 2: Lower Cap, LH (MID)
  - Callout 3: Web, Composite (MID)
  - Callout 4: Shear Tie (typ)
  - Callout 5: Rib Bracket (typ)
  - Callout 6: QSS Patch (optional)

- **FS_MID_RH_exploded.svg** - Midspan RH section with 6 callouts
  - Callout 1: Upper Cap, RH (MID)
  - Callout 2: Lower Cap, RH (MID)
  - Callout 3: Web, Composite (MID)
  - Callout 4: Shear Tie (typ)
  - Callout 5: Rib Bracket (typ)
  - Callout 6: QSS Patch (optional)

##### Outboard Section
- **FS_OUTB_LH_exploded.svg** - Outboard LH section with 5 callouts
  - Callout 1: Upper Cap, LH (OUTB)
  - Callout 2: Lower Cap, LH (OUTB)
  - Callout 3: Web, Composite (OUTB)
  - Callout 4: Rib Bracket (typ)
  - Callout 5: QSS Patch (optional)

- **FS_OUTB_RH_exploded.svg** - Outboard RH section with 5 callouts
  - Callout 1: Upper Cap, RH (OUTB)
  - Callout 2: Lower Cap, RH (OUTB)
  - Callout 3: Web, Composite (OUTB)
  - Callout 4: Rib Bracket (typ)
  - Callout 5: QSS Patch (optional)

#### Sheet 3 - QSS Provisioning
- **QSS_FS_assembly.svg** - QSS sensor assembly with 8 callouts
  - Callout 1: QSS Sensor Patch Kit (INB)
  - Callout 2: QSS Sensor Patch Kit (MID)
  - Callout 3: QSS Sensor Patch Kit (OUTB)
  - Callout 4: QSS Harness Assembly (Forward Spar)
  - Callout 5: QSS Controller Bracket
  - Callout 6: QSS Controller Unit
  - Callout 7: Adhesive Kit (Sensor Bonding)
  - Callout 8: Mounting Hardware Kit

## Usage Instructions for Technical Illustrators

### Important: Preserve Callout IDs

When replacing placeholder geometry with detailed spar drawings:

1. **DO NOT** change the `id` attributes on callout elements (e.g., `id="callout-1"`)
2. **DO NOT** alter the structure of callout groups (`<g id="callout-X">`)
3. **DO** replace the `geometry-placeholder` group contents with actual geometry
4. **DO** adjust callout positions (x, y coordinates) to point to correct features
5. **DO** maintain consistent visual style across all sheets

### Callout Structure

Each callout consists of:
- A numbered circle (blue for structural parts, orange for QSS)
- A leader line pointing to the feature
- A text label describing the part

Example:
```xml
<g id="callout-1">
  <circle cx="200" cy="200" r="15" fill="white" stroke="#0066cc" stroke-width="2"/>
  <text x="200" y="206" font-size="16" font-weight="bold" text-anchor="middle" fill="#0066cc">1</text>
  <line x1="215" y1="200" x2="280" y2="180" stroke="#0066cc" stroke-width="1.5"/>
  <text x="285" y="183" font-size="12" fill="#333">Upper Cap, LH (INB)</text>
</g>
```

### Workflow

1. Open the SVG template in your preferred vector graphics editor (Illustrator, Inkscape, etc.)
2. Replace the placeholder geometry with detailed technical drawings
3. Adjust callout positions to point to the correct features
4. Verify all callout IDs remain unchanged
5. Save the file maintaining the same filename
6. Validate the SVG renders correctly in a web browser

### Color Scheme

- **Structural parts**: Blue callouts (`#0066cc`)
- **QSS/Optional parts**: Orange callouts (`#cc6600`)
- **Background**: Light gray (`#f5f5f5`)
- **Text**: Dark gray (`#333`) for labels, medium gray (`#666`) for notes

### Quality Checks

Before finalizing:
- [ ] All callout IDs preserved
- [ ] Callouts point to correct features
- [ ] Text is readable at expected viewing sizes
- [ ] SVG validates and renders in web browsers
- [ ] File size is reasonable (<2MB per file)
- [ ] Consistent style across all related sheets

## Cross-References

These graphics are referenced in the following Data Modules:
- **DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml** (Sheet 1)
- **DMC-BWQ1-A-57-10-10-00-01A-941B-D-EN-US.xml** (Sheet 2)
- **DMC-BWQ1-A-57-10-10-00-02A-941C-D-EN-US.xml** (Sheet 3)

## Revision History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0 | 2025-10-04 | Initial template creation | Auto-generated |

---

*Part of BWQ1 S1000D IPD documentation for ATA-57-10 Forward Spar*
