# S1000D Issue 6.0 Template Example

**Parent:** [../](../)

## Purpose

This directory provides a **complete S1000D Issue 6.0 compliant scaffold** with sample Data Modules (DMs) that can be used as a template for creating new S1000D documentation packages. The structure follows aerospace industry best practices and the S1000D specification Issue 6.0.

## Key Features

- ✅ **S1000D Issue 6.0 compliant** data modules
- ✅ **IDEALE.eu enterprise code** convention
- ✅ **Complete CSDB structure** (DMC, BREX, GFX, SCHEMA, PUB)
- ✅ **Three sample DMs**: Descriptive (040A), Procedural (520A), and IPD (941A)
- ✅ **BREX validation rules** for Issue 6.0
- ✅ **DMRL** (Data Module Requirement List)
- ✅ **Placeholder graphics** (SVG format)
- ✅ **External schema example** (JSON Schema)

## Structure

```
57-90_S1000D_Template_Example/
└─ S1000D/
   └─ data_modules/
      └─ manual/
         └─ 57-90-00_template/
            └─ CSDB/
               ├─ BREX/      - Business Rules Exchange (validation rules)
               ├─ DMC/       - Data Module Content (the actual DMs)
               ├─ GFX/       - Graphics (SVG illustrations)
               ├─ SCHEMA/    - External schemas (JSON Schema, etc.)
               └─ PUB/       - Publications (DMRL)
```

## Data Modules Included

### 1. Descriptive DM (040A)
**File:** `DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml`

General description and architecture data module including:
- Overall configuration and function
- Load paths and structural philosophy
- Materials and specifications
- Section breakdown and stations
- Interface definitions

### 2. Procedural DM (520A)
**File:** `DMC-BWQ1-A-57-90-00-00-00A-520A-D-EN-US.xml`

Inspection and operation procedures including:
- Preliminary requirements (tools, personnel, safety)
- General inspection philosophy
- Inspection zones and access procedures
- NDT method selection
- MPD-derived intervals
- Close-out requirements

### 3. IPD DM (941A)
**File:** `DMC-BWQ1-A-57-90-00-00-00A-941A-D-EN-US.xml`

Illustrated Parts Data including:
- Catalog sequence numbering
- Exploded view figures
- Part identification (part numbers, manufacturers)
- Quantities per assembly
- Figure callouts and references

## Additional Files

### BREX (Business Rules Exchange)
**File:** `BREX/DMC-BWQ1-A-57-90-00-00-00A-022A-B-EN-US.xml`

Defines project-specific validation rules:
- BREX reference enforcement
- Enterprise code validation (IDEALE.eu)
- Language validation (en-US)
- Security classification requirements
- Title style enforcement
- External schema reference policies

### DMRL (Data Module Requirement List)
**File:** `PUB/DMRL-BWQ1-57-90-00.xml`

Lists all required data modules for the 57-90-00 package.

### Graphics
**Directory:** `GFX/`

Contains placeholder SVG graphics:
- `fig_overview.svg` - System overview diagram
- `ipd_exploded.svg` - Exploded view for IPD

### External Schema
**File:** `SCHEMA/external_schema.json`

Example JSON Schema for inspection event payload validation, demonstrating how to reference external schemas from S1000D data modules.

## Using This Template

### Quick Start

1. **Copy the entire CSDB structure** to your target location:
   ```bash
   cp -r CSDB /path/to/your/ata/chapter/
   ```

2. **Search and replace placeholders**:
   - `BWQ1` → Your model identification code (4 chars)
   - `57` → Your ATA chapter (2 digits)
   - `90` → Your sub-system code (2 digits)
   - `00` → Your sub-sub-system code (2 digits)
   - `IDEALE.eu` → Your enterprise code (if different)

3. **Update content**:
   - Edit XML files to reflect your actual system/component
   - Replace graphics with actual technical illustrations
   - Update BREX rules as needed for your project
   - Modify external schema if using different validation

### Detailed Customization Guide

#### Data Module Codes (DMC)

S1000D DMC naming follows this pattern:
```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC>-<DC><DCV>-<IC><ICV>-<ILC>-<LIC>-<CIC>.xml

Where:
- MIC  = Model Identification Code (e.g., BWQ1)
- SDC  = System Difference Code (e.g., A)
- SC   = System Code / ATA Chapter (e.g., 57)
- SSC  = Sub System Code (e.g., 90)
- SSSC = Sub-Sub System Code (e.g., 00)
- AC   = Assembly Code (e.g., 00)
- DC   = Disassembly Code (e.g., 00)
- DCV  = Disassembly Code Variant (e.g., A)
- IC   = Information Code (e.g., 040, 520, 941)
- ICV  = Information Code Variant (e.g., A)
- ILC  = Item Location Code (e.g., D)
- LIC  = Language ISO Code (e.g., EN)
- CIC  = Country ISO Code (e.g., US)
```

#### Information Codes

Common S1000D information codes:
- **010A** - Description
- **022A** - BREX
- **040A** - Descriptive (General)
- **520A** - Procedural (Inspection/Operation)
- **941A** - Illustrated Parts Data (IPD)

#### Enterprise Codes

This template uses `IDEALE.eu` as the enterprise code. Update this in:
- All `responsiblePartnerCompany` elements
- All `originator` elements
- BREX validation rules

## Validation

### XML Schema Validation

Validate against S1000D Issue 6.0 schemas:

```bash
# Descriptive DM
xmllint --noout --schema http://www.s1000d.org/S1000D_6/xml_schema_flat/descript.xsd \
  DMC/DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml

# Procedural DM
xmllint --noout --schema http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd \
  DMC/DMC-BWQ1-A-57-90-00-00-00A-520A-D-EN-US.xml

# IPD DM
xmllint --noout --schema http://www.s1000d.org/S1000D_6/xml_schema_flat/ipd.xsd \
  DMC/DMC-BWQ1-A-57-90-00-00-00A-941A-D-EN-US.xml
```

### BREX Validation

Apply BREX rules using Schematron:

```bash
schematron BREX/DMC-BWQ1-A-57-90-00-00-00A-022A-B-EN-US.xml DMC/*.xml
```

## Key Differences from Issue 5.0

This template follows S1000D Issue 6.0, which includes:

1. **Updated schema locations** - Using Issue 6.0 XSD schemas
2. **Enhanced BREX** - More sophisticated context rules
3. **External schema support** - Better integration with JSON Schema
4. **Improved referencing** - Updated cross-reference mechanisms
5. **Quality assurance** - Updated QA elements

## References

- [S1000D Specification](http://www.s1000d.org)
- [ATA iSpec 2200](https://www.ata.org/resources/specifications)
- [BWB-Q100 Project Documentation](../../../../../../)

## Standards Compliance

- ✅ S1000D Issue 6.0
- ✅ ATA iSpec 2200
- ✅ XML 1.0
- ✅ SVG 1.1
- ✅ JSON Schema Draft 2020-12

## Notes

- **Placeholder Content**: All content in these data modules is placeholder/example content. Replace with actual technical data for your system.
- **Graphics**: SVG graphics are simple placeholders. Replace with actual technical illustrations created in your authoring tool.
- **Schema**: The external JSON schema is an example. Customize or remove based on your validation needs.
- **BREX Rules**: The BREX rules provided are examples. Add project-specific rules as needed.

## License

Follows the licensing terms of the ASI-T2 project.

---

**Version:** 1.0  
**Last Updated:** 2025-10-04  
**Maintained by:** IDEALE.eu
