# CSDB (Common Source Database)

**Parent:** [../](../)

## Purpose

This directory contains the Common Source Database (CSDB) structure for the 57-90-00 template example, following S1000D Issue 6.0 organization standards.

## Directory Structure

```
CSDB/
├─ BREX/      - Business Rules Exchange (validation rules)
├─ DMC/       - Data Module Content (XML data modules)
├─ GFX/       - Graphics (SVG, PNG, etc.)
├─ SCHEMA/    - External validation schemas (JSON Schema, XSD)
└─ PUB/       - Publications (DMRL, PM, etc.)
```

## Contents

### BREX/ - Business Rules Exchange
Contains BREX data modules that define project-specific validation rules beyond the standard S1000D schema validation.

**Files:**
- `DMC-BWQ1-A-57-90-00-00-00A-022A-B-EN-US.xml` - BREX rules for this package

### DMC/ - Data Module Content
Contains the actual S1000D data modules (descriptive, procedural, IPD, etc.).

**Files:**
- `DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml` - Descriptive DM
- `DMC-BWQ1-A-57-90-00-00-00A-520A-D-EN-US.xml` - Procedural DM
- `DMC-BWQ1-A-57-90-00-00-00A-941A-D-EN-US.xml` - IPD DM

### GFX/ - Graphics
Contains all graphics referenced by data modules. SVG format is preferred for scalability.

**Files:**
- `fig_overview.svg` - System overview diagram (ICN-BWQ1-57-90-00-001)
- `ipd_exploded.svg` - Exploded view for IPD (ICN-BWQ1-57-90-00-901)

### SCHEMA/ - External Schemas
Contains external validation schemas referenced by data modules via `externalPubRef`.

**Files:**
- `external_schema.json` - JSON Schema for inspection event validation

### PUB/ - Publications
Contains publication-level data modules like DMRL (Data Module Requirement List) and PM (Publication Module).

**Files:**
- `DMRL-BWQ1-57-90-00.xml` - Data Module Requirement List

## Naming Conventions

### Data Module Code (DMC) Structure
```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC>-<DC><DCV>-<IC><ICV>-<ILC>-<LIC>-<CIC>.xml
```

Example: `DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml`

- **MIC**: BWQ1 (Model Identification Code)
- **SDC**: A (System Difference Code)
- **SC**: 57 (System Code / ATA Chapter)
- **SSC**: 90 (Sub System Code)
- **SSSC**: 00 (Sub-Sub System Code)
- **AC**: 00 (Assembly Code)
- **DC**: 00 (Disassembly Code)
- **DCV**: A (Disassembly Code Variant)
- **IC**: 040/520/941 (Information Code)
- **ICV**: A (Information Code Variant)
- **ILC**: D (Item Location Code)
- **LIC**: EN (Language ISO Code)
- **CIC**: US (Country ISO Code)

### Graphic File Naming
Graphics should use descriptive names and can be referenced by Info Entity Ident (ICN):
```
ICN-<MIC>-<SC>-<SSC>-<SSSC>-<SeqNo>
```

Example: `ICN-BWQ1-57-90-00-001` → `fig_overview.svg`

## Usage

### Adding New Data Modules

1. Create the XML file in the `DMC/` directory
2. Follow the DMC naming convention
3. Reference the BREX in the `dmStatus` section
4. Link any graphics to files in `GFX/`
5. Update the DMRL in `PUB/` to include the new DM

### Adding Graphics

1. Place graphics in `GFX/` directory
2. Use SVG format when possible
3. Reference from data modules using `xlink:href="../GFX/filename.svg"`
4. Assign appropriate ICN for traceability

### Validation

```bash
# Validate all descriptive DMs
xmllint --noout --schema http://www.s1000d.org/S1000D_6/xml_schema_flat/descript.xsd DMC/*-040A-D-*.xml

# Validate all procedural DMs
xmllint --noout --schema http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd DMC/*-520A-D-*.xml

# Validate all IPD DMs
xmllint --noout --schema http://www.s1000d.org/S1000D_6/xml_schema_flat/ipd.xsd DMC/*-941A-D-*.xml

# Validate BREX
xmllint --noout --schema http://www.s1000d.org/S1000D_6/xml_schema_flat/brex.xsd BREX/*.xml
```

## Cross-References

Data modules can reference each other using:
- `dmRef` - Reference to another data module
- `externalPubRef` - Reference to external publications/schemas
- `figureRef` - Reference to figures within the same DM

## Standards

- S1000D Issue 6.0
- ATA iSpec 2200
- XML 1.0
- SVG 1.1
- JSON Schema Draft 2020-12

---

**See also:** [Parent README](../README.md) for complete template documentation
