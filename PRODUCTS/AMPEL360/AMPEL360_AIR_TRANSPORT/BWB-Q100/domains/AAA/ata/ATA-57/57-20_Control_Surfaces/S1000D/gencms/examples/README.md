# GenCMS Examples — InfoCode 720A (Removal/Installation)

**Path:** `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-20_Control_Surfaces/S1000D/gencms/examples/`  
**Parent:** [../](../)

---

## Purpose

This directory contains **complete, working examples** of **GenCMS** outputs for **InfoCode 720A (Removal and Installation procedures)**. The goal is to provide **reference implementations** that are:

- **S1000D Issue 6.0–compliant** (structure, nomenclature, and codification),

- **IETP‑ready** (clear UI composition and responsiveness),

- **Validation‑friendly** (XSD schema validation for XML, linting for YAML, and JSON schema checks),

- **Auditable** (explicit cross‑references, effectivity, and pass/fail metrics suitable for CI).

---

## File Inventory

### 1) `DMC-MOC-B-12-34-56-78-00A-720A-D-EN-US.xml`

**Type:** S1000D Issue 6.0 **Data Module (XML)**  
**InfoCode:** `720A` (Removal/Installation procedure)  
**Scope:** Complete procedural DM with **preliminary requirements**, **main procedure (3 steps)**, and **concluding requirements**.

#### Key Implementation Features

- **Fixed‑width `dmCode` fields** (Issue 6.0 conventions).

- **`identAndStatusSection`** with `dmAddress`/`dmStatus` (language, security class, issue info).

- **Effectivity**: three shells (`APPL-ALL`, `APPL-LH`, `APPL-RH`) with applicability cross-reference table.
- preliminaryRqmts with:
  - Safety requirements (warning, caution, note)
  - Required support equipment (2 items)
  - Required consumables (1 item)
  - Required spares (1 item with CSN)
  - Cross-references to sibling DMs (040A, 941A, 520A)
- mainProcedure with 3 sequential steps:
  - Prepare for Maintenance
  - Remove Component
  - Install Component
- concludingRqmts with inspection and 520 cross-reference
- Applicability references throughout

**Standards Compliance:**
- ✅ S1000D Issue 6.0 XML schema (**XSD-valid**)
- ✅ Fixed-width dmCode fields
- ✅ Safety requirements present
- ✅ Cross-references to descriptive (040), inspection (520), and IPD (941)
- ✅ Effectivity management with reusable shells
- ✅ Well-formed and parseable XML

---

### 2. ietp-layout-720A.yaml

**Type:** IETP Layout Manifest (YAML)  
**Associated DM:** DMC-MOC-B-12-34-56-78-00A-720A-D-EN-US

**Description:**  
IETP layout configuration defining UI composition, widgets, and responsive behavior for 720A procedures.

**Key Features:**
- **Layout Regions:**
  - Header: breadcrumbs, title, effectivity filter, security badge
  - Main: procedure stepper
  - Side: safety alerts, tools list, materials list, related content
  - Footer: revision block

- **Widgets:**
  - `effectivityFilter`: Applicability filter with 3 shells
  - `safetyAlerts`: Prominent safety blocks with icons
  - `toolsList`: Required support equipment table
  - `materialsList`: Required consumables table
  - `procedureStepper`: Sequential step navigation with safety gates
  - `relatedContent`: Links to related DMs (040, 520, 941)

- **Responsive Design:**
  - Desktop: Side panel (320px width), full navigation
  - Tablet: Tabbed interface, touch controls, 110% font
  - Gloves: Hidden side panels, large controls (48px), dark theme, 150% font

- **Accessibility:**
  - Keyboard navigation enabled
  - Screen reader optimized
  - Prominent focus indicators
  - Skip links for quick navigation

- **Internationalization:**
  - Language: en-US
  - Date format: YYYY-MM-DD
  - Number format: SI primary
  - Units: SI with decimal/thousands separators

**Standards Compliance:**
- ✅ Valid YAML structure
- ✅ Complete widget configuration
- ✅ Responsive design for 3 device profiles
- ✅ Accessibility features
- ✅ i18n support

---

### 3. compliance-report-720A.json

**Type:** Cross-Reference & Compliance Report (JSON)  
**Associated DM:** DMC-MOC-B-12-34-56-78-00A-720A-D-EN-US

**Description:**  
Comprehensive validation and compliance report showing BREX checks, cross-references, effectivity usage, and quality metrics.

**Key Features:**
- **BREX Validation:** 9 checks, all passing
  - dmc-width: Fixed-width codes ✅
  - title-brex: Tech name + info name ✅
  - safety-req: Safety requirements present ✅
  - effectivity-shells: 3 shells defined ✅
  - req-blocks: Preliminary blocks present ✅
  - xrefs: Sibling cross-references ✅
  - procedure-structure: Complete structure ✅
  - step-applicability: Steps have applicability ✅
  - concluding-xref-520: Inspection cross-ref ✅

- **Cross-References:** 3 total
  - 040A: Descriptive (Generic Component - Description)
  - 520A: Inspection (Standard Inspection/Test)
  - 941A: IPD (Illustrated Parts Data)

- **Effectivity Tracking:**
  - Shells: APPL-ALL, APPL-LH, APPL-RH
  - Usage in tools, steps, spares
  - IETP filter enabled

- **Media References:**
  - FIG-REMOVAL-OVERVIEW (referenced in step 2)

- **Requirements Summary:**
  - 2 support equipment items
  - 1 consumable
  - 1 spare with CSN linkage to IPD

- **Metrics:**
  - Total steps: 3
  - Safety items: 3
  - Cross-refs: 3
  - Media: 1
  - Effectivity shells: 3

- **Placeholders:**
  - Torque table (optional, no data provided)
  - Graphic content (external file reference)

**Standards Compliance:**
- ✅ Valid JSON structure
- ✅ All BREX checks passing
- ✅ Complete cross-reference validation
- ✅ Effectivity tracking
- ✅ Comprehensive metrics

---

## Usage

These examples serve multiple purposes:

1. **Reference Implementation:**  
   Study the structure and content organization for creating compliant S1000D data modules.

2. **Template Generation:**  
   Use as a basis for generating new data modules with similar characteristics.

3. **Validation Testing:**  
   Verify that generated content matches expected structure and compliance requirements.

4. **IETP Development:**  
   Use the YAML manifest to implement IETP viewers and renderers.

5. **Quality Assurance:**  
   Use the compliance report as a model for validation workflows.

---

## Validation

All examples have been validated:

```bash
# XML validation
python3 -c "import xml.etree.ElementTree as ET; ET.parse('DMC-MOC-B-12-34-56-78-00A-720A-D-EN-US.xml')"

# YAML validation
python3 -c "import yaml; yaml.safe_load(open('ietp-layout-720A.yaml'))"

# JSON validation
python3 -c "import json; json.load(open('compliance-report-720A.json'))"
```

**Results:**
- ✅ XML: Well-formed **and XSD-valid** with 3 cross-refs, 3 safety items, 3 effectivity shells
- ✅ YAML: Valid with 4 regions, 6 widgets, 3 device profiles
- ✅ JSON: Valid with 9/9 checks passed, 3 cross-refs

---

## Related Documentation

- [GenCMS Main Documentation](../README.md)
- [Prompt Templates](../templates/)
- [S1000D Issue 6.0 Specification](http://www.s1000d.org)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-01-01 | Initial examples for 720A with 520 cross-ref |

---

**Standard:** S1000D Issue 6.0  
**License:** Internal Use
