# GenCMS — Generative Content Management System

**Version:** 1.0.0  
**Standard:** S1000D Issue 6.0 (**XSD-first validation**)  
**Path:** `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-20_Control_Surfaces/S1000D/gencms/`  
**Parent:** [../](../)  
**License:** Internal   
**Maintainer:** Technical Publications Team

---

## 1) Purpose & Scope

**GenCMS** is a generative, interactive system that produces **IETP-ready** technical publications—combining **S1000D 6.0 XML Data Modules**, **IETP Layout Manifests (YAML)**, and **Compliance Summaries (JSON)**. It automatically selects the correct **layout archetype** by **infoCode family** (040/5xx/7xx/9xx), assembles cross-references, applies effectivity, and enforces **BREX** rules—while guaranteeing **XSD validation** against the official S1000D 6.0 schemas.

**Core guarantees**

- **Standards-based** S1000D 6.0 structure (namespaces, fixed-width codes, required sections).
- **XSD-valid** XML (**mandatory**).
- **Schematron/BREX** checks (**recommended**, project-specific).
- **Consistent tri-artifact** emission: XML ↔ YAML ↔ JSON (self-consistent identifiers and metrics).
- **IETP-ready UI** with accessibility and device profiles (desktop/tablet/gloves).

---

## 2) Directory Structure

```
gencms/
├── README.md                             # This document
├── templates/
│   └── GENCMS_PROMPT_IETP_LAYOUT.md      # Prompt template: rules, layout patterns, XSD requirements
└── examples/
    ├── DMC-MOC-B-12-34-56-78-00A-720A-D-EN-US.xml   # 720A R/I example (XSD-valid)
    ├── ietp-layout-720A.yaml                         # IETP manifest for 720A
    └── compliance-report-720A.json                   # Validation report (9 checks)
```

---

## 3) Key Features

### 1. XSD-First Validation

- **Mandatory XSD validation** against official S1000D Issue 6.0 schemas
- XML must be well-formed **and** schema-valid before emission
- Optional Schematron/BREX checks (project-specific rules)
- Fail-safe: if validation fails, emit placeholders and error reports

### 2. Standards-Based

- **S1000D Issue 6.0** compliant structure and nomenclature
- **BREX** (Business Rules Exchange) aware
- **DMRL** (Data Module Requirements List) integration
- Fixed-width dmCode fields (2 digits)
- Proper effectivity shell management

### 3. Layout Patterns by InfoCode

GenCMS automatically selects the appropriate IETP layout based on the infoCode:

| InfoCode | Layout Pattern | Key Widgets |
|----------|---------------|-------------|
| **040** (Descriptive) | Article + Figure rail | Content viewer, figure rail, related DMs |
| **5xx** (Inspection/Repair) | Stepper + Acceptance | Safety alerts, tools, acceptance criteria |
| **7xx** (Removal/Installation) | Stepper + Kits | Safety alerts, tools, kits, torque table |
| **9xx** (IPD) | Figure viewer + Callouts | Interactive figures, CSN groups, effectivity filter |

### 4. Dynamic Effectivity Management

- Reusable effectivity shells (e.g., APPL-ALL, APPL-LH, APPL-RH)
- Applicability cross-reference tables
- IETP filter widgets for user-driven effectivity selection
- Effectivity applied to steps, tools, consumables, and spares

### 5. Cross-Reference Intelligence

- Automatic linking between descriptive (040), procedural (5xx/7xx), and IPD (9xx) modules
- Standards and specification references
- Media and figure references
- IPD linkage for required spares

### 6. Quality Assurance

- BREX validation with detailed compliance reports
- Schema validation (S1000D 6.0)
- Missing content detection
- Placeholder tracking for incomplete data

---

## Usage

### Using the Prompt Template

The main prompt template is located at:
```
templates/GENCMS_PROMPT_IETP_LAYOUT.md
```

This template can be used with AI systems or content management tools to generate S1000D-compliant data modules and IETP layouts.

**Input Parameters:**
```json
{
  "modelIdentCode": "MOC",
  "dmCode": {
    "systemCode": "12",
    "subSystemCode": "34",
    "subSubSystemCode": "56",
    "assyCode": "78",
    "disassyCode": "00",
    "infoCode": "720",
    "infoCodeVariant": "A",
    "itemLocationCode": "D"
  },
  "language": "en-US",
  "security": "01-unclassified",
  "effectivity": ["ALL", "LH", "RH"]
}
```

**Expected Outputs:**
1. S1000D XML data module
2. IETP layout manifest (YAML)
3. Cross-reference and compliance report (JSON)

### Example Output for 720A (Removal/Installation)

See the `examples/` directory for a complete implementation:

1. **S1000D XML**: `DMC-MOC-B-12-34-56-78-00A-720A-D-EN-US.xml`
   - Complete procedural structure
   - Safety requirements (warnings, cautions, notes)
   - Required tools and consumables
   - Procedural steps with effectivity
   - Cross-references to descriptive and IPD modules

2. **IETP Layout**: `ietp-layout-720A.yaml`
   - Responsive design (desktop/tablet/gloves)
   - Procedure stepper widget
   - Safety alerts panel
   - Tools and materials lists
   - Related content links
   - Accessibility features

3. **Compliance Report**: `compliance-report-720A.json`
   - BREX validation results
   - Cross-reference validation
   - Effectivity usage tracking
   - Media references
   - Requirements summary
   - Placeholder tracking

---

## InfoCode Patterns

### 040 — Descriptive Data Modules

**Purpose**: Component descriptions, system overviews, theory of operation

**Key Sections**:
- Description content
- Figures and illustrations
- Related procedures and IPD references

**IETP Widgets**:
- Article content viewer
- Figure rail (inline or sidebar)
- Related content panel

---

### 5xx — Inspection/Repair Procedures

**Purpose**: Inspection methods, repair procedures, acceptance criteria

**Key Sections**:
- Safety requirements
- Required tools and equipment
- Procedural steps
- Acceptance criteria tables
- Concluding requirements

**IETP Widgets**:
- Procedure stepper
- Safety alerts (prominent)
- Tools list
- Acceptance criteria table
- Related content

---

### 7xx — Removal/Installation Procedures

**Purpose**: Component removal and installation procedures

**Key Sections**:
- Safety requirements
- Required tools, consumables, and spares
- Removal steps
- Installation steps
- Torque specifications
- Concluding requirements

**IETP Widgets**:
- Procedure stepper (sequential with safety gates)
- Safety alerts
- Tools list
- Kits panel (spares with CSN)
- Torque table
- Related content

**Example**: See `examples/DMC-MOC-B-12-34-56-78-00A-720A-D-EN-US.xml`

---

### 9xx — Illustrated Parts Data (IPD)

**Purpose**: Parts breakdown, catalog sequence numbers, illustrations

**Key Sections**:
- Interactive figures
- Item callouts
- CSN groups with effectivity
- Part descriptions

**IETP Widgets**:
- Figure viewer (interactive with zoom/pan)
- Callout list
- CSN groups with effectivity filter
- Part details panel

---

## BREX Validation Rules

GenCMS enforces the following BREX rules:

### General Rules (all infoCodes)

| Rule ID | Description | Requirement |
|---------|-------------|-------------|
| `dmc-width` | Fixed-width codes | All dmCode fields must be 2 digits where applicable |
| `title-brex` | Title structure | dmTitle must include both techName and infoName |
| `effectivity-present` | Effectivity shells | At least one effectivity shell must be defined |
| `security-class` | Security classification | Security classification must be specified |

### Procedural Rules (5xx, 7xx)

| Rule ID | Description | Requirement |
|---------|-------------|-------------|
| `procedure-safety-block` | Safety requirements | Must include safetyRqmts with warning/caution/note |
| `prelim-blocks` | Preliminary requirements | Must have preliminaryRqmts section |
| `main-procedure` | Main procedure | Must have mainProcedure with proceduralSteps |
| `concluding-rqmts` | Concluding requirements | Should have concludingRqmts (recommended) |

### Cross-reference Rules

| Rule ID | Description | Requirement |
|---------|-------------|-------------|
| `xrefs-resolvable` | Valid references | All dmRef entries must point to valid DMCs |
| `ipd-linkage` | IPD cross-reference | If reqSpare elements exist, should cross-ref to 9xx DM |
| `descriptive-link` | Descriptive cross-reference | Procedures should cross-ref to sibling 040 DM |

---

## Responsive Design

GenCMS supports three device profiles:

### Desktop
- Side panels (320px width)
- Full navigation
- Standard font sizes
- Mouse/keyboard interaction

### Tablet
- Tabbed interface
- Touch-optimized controls
- 110% font size
- Swipe gestures

### Gloves
- Hidden side panels (modal access)
- Large controls (48px minimum)
- Dark theme by default
- 150% font size
- High contrast

---

## Accessibility Features

- **Keyboard navigation**: Full keyboard support for all interactions
- **Screen reader optimization**: Proper ARIA labels and semantic HTML
- **Contrast modes**: Auto, light, dark, high-contrast
- **Focus indicators**: Prominent visual focus indicators
- **Skip links**: Quick navigation to main content
- **Alt text**: All figures include descriptive alt text

---

## Internationalization (i18n)

- **Language support**: Based on dmCode language specification
- **Date formats**: ISO 8601 by default, locale-specific optional
- **Number formats**: Configurable decimal and thousands separators
- **Units**: SI units primary, with optional imperial conversion
- **UI labels**: Translatable strings in IETP manifests

---

## Integration with S1000D Ecosystem

### DMRL Integration

GenCMS reads the DMRL to:
- Discover required data modules
- Apply effectivity shells
- Validate requirement status (required/optional)
- Generate cross-references

Example DMRL reference: `../DMRL/DMRL.xml`

### BREX Integration

GenCMS reads BREX files to:
- Apply business rules
- Validate content structure
- Enforce project-specific constraints
- Generate compliance reports

Example BREX reference: `../BREX/`

### Data Module Cross-References

GenCMS automatically creates cross-references between:
- **Descriptive (040)** ↔ **Procedures (5xx/7xx)** ↔ **IPD (9xx)**
- Procedures ↔ Standard practices
- Components ↔ IPD catalog items

---

## Workflow

### 1. Preparation

- Define DMRL with required data modules and effectivity shells
- Create or reference BREX for project-specific validation rules
- Gather input parameters (dmCode, effectivity, security, etc.)

### 2. Generation

- Invoke GenCMS with prompt template and parameters
- GenCMS selects layout pattern based on infoCode
- GenCMS generates S1000D XML skeleton
- GenCMS creates IETP layout manifest
- GenCMS produces compliance report

### 3. Enrichment

- Populate content placeholders with detailed technical information
- Add actual figures and media files
- Refine procedural steps with specific instructions
- Add torque tables, tool specifications, etc.

### 4. Validation

- Validate XML against S1000D 6.0 schema
- Run BREX validation
- Review compliance report
- Address warnings and errors

### 5. Publication

- Package data module for IETP delivery
- Include media files and graphics
- Generate publication metadata
- Archive with version control

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-01-01 | Initial release with 720A example |

---

## References

- [S1000D Official Site](http://www.s1000d.org)
- [DMRL Documentation](../DMRL/)
- [BREX Documentation](../BREX/)
- [Data Modules](../DMC/)

---

## License

Internal Use

---

## Maintainer

Technical Publications Team  
Contact: See main repository README
