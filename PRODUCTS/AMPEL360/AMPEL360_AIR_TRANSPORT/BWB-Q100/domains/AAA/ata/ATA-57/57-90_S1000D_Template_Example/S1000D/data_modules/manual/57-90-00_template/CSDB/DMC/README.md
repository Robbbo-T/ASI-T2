# DMC - Data Module Content

**Parent:** [../](../)

## Purpose

This directory contains the actual S1000D data modules (DMs) that make up the technical documentation. Each data module is a self-contained unit of technical information in XML format, following S1000D Issue 6.0 standards.

## Contents

This template includes three sample data modules demonstrating different S1000D information types:

### 1. DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml

**Type:** Descriptive Data Module  
**Information Code:** 040A (General Description)  
**Purpose:** Provides general description and architecture information

**Contains:**
- Overall configuration and function
- Load paths and structural philosophy
- Materials and specifications
- Section breakdown and stations
- Interface definitions
- Figure references to graphics in GFX/

**Use this as a template for:** System overviews, component descriptions, architectural documentation

### 2. DMC-BWQ1-A-57-90-00-00-00A-520A-D-EN-US.xml

**Type:** Procedural Data Module  
**Information Code:** 520A (Inspection/Check/Operation)  
**Purpose:** Provides step-by-step inspection and operation procedures

**Contains:**
- Preliminary requirements (tools, safety, personnel)
- General inspection philosophy
- Inspection zones and access procedures
- NDT method selection table
- MPD-derived intervals
- Close-out requirements
- External schema references

**Use this as a template for:** Inspection procedures, operational procedures, maintenance tasks

### 3. DMC-BWQ1-A-57-90-00-00-00A-941A-D-EN-US.xml

**Type:** Illustrated Parts Data (IPD)  
**Information Code:** 941A (Illustrated Parts)  
**Purpose:** Provides illustrated parts list with exploded views

**Contains:**
- Catalog sequence numbering
- Part identification (part numbers, manufacturers)
- Quantities per next higher assembly
- Figure references with callouts
- Exploded view graphics

**Use this as a template for:** Parts lists, component catalogs, assembly illustrations

## Data Module Structure

All data modules follow this basic structure:

```xml
<dmodule>
  <identAndStatusSection>
    <dmAddress>
      <dmIdent>...</dmIdent>
      <dmAddressItems>...</dmAddressItems>
    </dmAddress>
    <dmStatus>...</dmStatus>
  </identAndStatusSection>
  <content>
    <!-- Type-specific content -->
  </content>
</dmodule>
```

## Data Module Code (DMC) Naming

Data modules are named using the S1000D DMC convention:

```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC>-<DC><DCV>-<IC><ICV>-<ILC>-<LIC>-<CIC>.xml

Example: DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml

Where:
- MIC: BWQ1 (Model Identification Code)
- SDC: A (System Difference Code)
- SC: 57 (System Code - ATA Chapter)
- SSC: 90 (Sub System Code)
- SSSC: 00 (Sub-Sub System Code)
- AC: 00 (Assembly Code)
- DC: 00 (Disassembly Code)
- DCV: A (Disassembly Code Variant)
- IC: 040/520/941 (Information Code)
- ICV: A (Information Code Variant)
- ILC: D (Item Location Code - Descriptive)
- LIC: EN (Language ISO Code)
- CIC: US (Country ISO Code)
```

## Common Information Codes

| Code | Type | Purpose |
|------|------|---------|
| 010A | Descriptive | Function and interface descriptions |
| 040A | Descriptive | General description and architecture |
| 520A | Procedural | Inspection/check/operation |
| 721A | Procedural | Installation/removal |
| 941A | IPD | Illustrated parts data |

## Adding New Data Modules

To add a new data module to this directory:

1. **Create XML file** following DMC naming convention
2. **Include required sections:**
   - identAndStatusSection with dmAddress and dmStatus
   - content section appropriate for the information type
3. **Reference BREX** in dmStatus section
4. **Link graphics** to files in ../GFX/ directory
5. **Update DMRL** in ../PUB/ to include the new DM

## Validation

Validate data modules against S1000D schemas:

```bash
# Descriptive DMs
xmllint --noout --schema s1000d/descript.xsd DMC-*-040A-D-*.xml

# Procedural DMs
xmllint --noout --schema s1000d/proced.xsd DMC-*-520A-D-*.xml

# IPD DMs
xmllint --noout --schema s1000d/ipd.xsd DMC-*-941A-D-*.xml

# Validate against BREX
schematron ../BREX/DMC-*.xml DMC-*.xml
```

## Cross-References

Data modules can reference:
- **Other DMs:** Using `<dmRef>` elements
- **Graphics:** Using `<graphic xlink:href="../GFX/filename.svg">`
- **External schemas:** Using `<externalPubRef>`
- **Common information:** Using `<infoEntityRef>`

Example:
```xml
<dmRef>
  <dmRefIdent>
    <dmCode modelIdentCode="BWQ1" ... />
  </dmRefIdent>
</dmRef>
```

## Best Practices

- ✅ Use meaningful techName and infoName in dmTitle
- ✅ Keep data modules focused on single topics
- ✅ Reference BREX in all data modules
- ✅ Use appropriate information codes
- ✅ Include security classification
- ✅ Link to graphics using relative paths
- ✅ Validate before committing

## Standards Compliance

- S1000D Issue 6.0
- XML 1.0
- UTF-8 encoding
- XLink 1.0 for references

## Related Documentation

- [CSDB README](../README.md) - Parent directory
- [BREX Directory](../BREX/) - Validation rules
- [GFX Directory](../GFX/) - Graphics referenced by DMs
- [PUB Directory](../PUB/) - DMRL listing all DMs

---

**Tip:** Use existing data modules as templates. Copy, rename according to DMC convention, and update content for your specific system or component.
