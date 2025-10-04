# GenCMS Templates — Prompt Templates for Dynamic IETP Generation

**Parent:** [../](../)

---

## Purpose

This directory contains prompt templates for the GenCMS (Generative Content Management System). These templates provide standardized instructions for generating S1000D Issue 6.0 compliant data modules with dynamic IETP layouts.

The templates are **vendor-neutral** and **project-agnostic**, designed to work with any S1000D-compliant system without requiring modification for specific projects or organizations.

---

## Files

### GENCMS_PROMPT_IETP_LAYOUT.md

**Type:** GenCMS Prompt Template  
**Version:** 1.0.0  
**Standard:** S1000D Issue 6.0

**Description:**  
Comprehensive prompt template for generating IETP-ready outputs that conform to S1000D Issue 6.0 standards. This template dynamically resolves the correct IETP layout pattern from context and parameters, then generates compliant S1000D XML, IETP layout manifests, and cross-reference/compliance summaries.

---

## Template Features

### 1. Role Definition

The template defines GenCMS as a generative, interactive agent with specific responsibilities:
- Produce IETP-ready outputs (layout + content)
- Conform to S1000D Issue 6.0
- Integrate with BREX (Business Rules Exchange)
- Integrate with DMRL (Data Module Requirements List)
- Generate three synchronized artifacts: XML, YAML, JSON

### 2. Input Discovery

The template instructs GenCMS to automatically discover:
- DMRL (required/optional DMs + effectivity shells)
- BREX (constraints and Schematron rules)
- Neighbor DMs in the same functional area
- Applicable standards and specifications
- Figures and media references

### 3. Parameter Structure

JSON-based parameter schema for:
- Model identification codes
- DMC fields (system, subsystem, assembly, disassembly, infoCode)
- Language and localization
- Security classification
- Effectivity expressions
- Device profiles (desktop/tablet/gloves)
- Theme preferences
- Navigation depth
- Figure inclusion flags

### 4. Dynamic Layout Selection

Automatic layout pattern selection based on infoCode family:

| InfoCode | Layout Type | Components |
|----------|-------------|------------|
| **040** | Descriptive | Article + Figure rail + Related DMs panel |
| **5xx** | Inspection/Repair | Stepper + Safety + Tools + Acceptance table |
| **7xx** | Removal/Installation | Stepper + Kits + Torque + Tools |
| **9xx** | IPD | Figure viewer + Callouts + CSN groups |

### 5. Standards Compliance

Built-in rules for S1000D 6.0 + BREX compliance:
- Fixed-width dmCode fields (2 digits)
- Complete dmAddress population
- Safety blocks for procedural content
- Cross-reference integrity checking
- Effectivity presence validation
- Non-blocking placeholder generation

### 6. Effectivity Management

Instructions for handling applicability:
- Build effectivity expressions from shells
- Expose effectivity filter widgets in IETP
- Apply effectivity to steps, tools, consumables, spares
- Support complex effectivity logic (AND/OR/NOT)

### 7. Cross-Reference Intelligence

Automated cross-referencing between:
- Descriptive (040) ↔ Procedures (5xx/7xx) ↔ IPD (9xx)
- Procedures ↔ Standard practices and specs
- Components ↔ IPD catalog items (via CSN)

### 8. Quality Gates

Built-in validation and reporting:
- BREX rule checking with pass/fail status
- Missing input detection and reporting
- Placeholder tracking
- Compliance checklist generation

### 9. Responsive Design

Instructions for device-aware layouts:
- **Desktop:** Full layout with side panels, mouse/keyboard
- **Tablet:** Tabbed interface, touch controls, larger fonts
- **Gloves:** Simplified layout, large controls (48px), high contrast

### 10. Accessibility

Requirements for accessible outputs:
- Keyboard navigation support
- Screen reader optimization
- Figure alt text
- Skip links
- Contrast modes
- Focus indicators

### 11. Internationalization

Support for localization:
- Language-specific labels
- Date format by locale
- Number format by locale
- Unit system (SI primary)

---

## Usage

### For AI Systems

Use this template as a system prompt or instruction set when invoking AI models to generate S1000D content:

```python
with open('GENCMS_PROMPT_IETP_LAYOUT.md', 'r') as f:
    prompt_template = f.read()

# Combine with user parameters
parameters = {
    "modelIdentCode": "MOC",
    "dmCode": {
        "systemCode": "12",
        "infoCode": "720",
        # ... other fields
    }
}

# Send to AI model
response = ai_model.generate(prompt_template, parameters)
```

### For Content Management Systems

Integrate the template logic into your CMS workflow:

1. **Input Phase:** Collect parameters from content authors
2. **Discovery Phase:** Auto-discover DMRL, BREX, neighbor DMs
3. **Generation Phase:** Apply template rules to generate artifacts
4. **Validation Phase:** Run BREX checks and quality gates
5. **Output Phase:** Deliver XML + YAML + JSON

### For Manual Authoring

Use the template as a checklist and structure guide:

- Follow the infoCode layout patterns
- Ensure all mandatory sections are present
- Apply effectivity shells consistently
- Include proper cross-references
- Validate against BREX rules

---

## Template Structure

The template follows a logical flow:

1. **Role & Goal** — Define the agent's purpose and objectives
2. **Inputs** — What information to discover automatically
3. **Parameters** — What the user must provide
4. **Required Behavior** — Core generation rules (5 categories)
5. **Outputs** — Three required artifacts (XML, YAML, JSON)
6. **Style & UX** — User experience requirements
7. **Generation Steps** — 8-step workflow for consistent results
8. **Layout Patterns** — Detailed descriptions for each infoCode
9. **Validation Rules** — BREX checks by category
10. **Example Usage** — Concrete example for 720A

---

## Customization

While the template is designed to be vendor-neutral, organizations may customize:

### Project-Specific Fields
- Model identification codes
- Security classification schemes
- Effectivity shell naming conventions

### BREX Extensions
- Add organization-specific BREX rules
- Customize validation severity levels
- Define custom quality gates

### Layout Variations
- Modify widget configurations
- Add custom UI components
- Adjust responsive breakpoints

### Language Support
- Add additional locale codes
- Define custom date/number formats
- Provide translated UI labels

**Important:** When customizing, maintain the core S1000D 6.0 compliance requirements and avoid introducing project-specific dependencies into the base template.

---

## Integration with GenCMS Ecosystem

This template integrates with other GenCMS components:

- **[Examples](../examples/)** — Reference implementations demonstrating template outputs
- **[Main Documentation](../README.md)** — Overall GenCMS system documentation
- **DMRL** — Data Module Requirements Lists define required DMs
- **BREX** — Business Rules Exchange files define validation rules
- **DMC** — Generated Data Modules stored in repository

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-01-01 | Initial release with vendor-neutral design |

---

## Standards & References

- [S1000D Official Site](http://www.s1000d.org)
- [S1000D Issue 6.0 Specification](http://www.s1000d.org/S1000D_6-0/)
- [BREX Documentation](http://www.s1000d.org/brex)
- [IETP Viewer Guidelines](http://www.s1000d.org/ietp)

---

**Standard:** S1000D Issue 6.0  
**License:** Internal Use  
**Maintainer:** Technical Publications Team
