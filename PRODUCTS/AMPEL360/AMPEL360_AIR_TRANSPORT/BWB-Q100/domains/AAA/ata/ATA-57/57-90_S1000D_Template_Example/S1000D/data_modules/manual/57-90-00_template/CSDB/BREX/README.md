# BREX - Business Rules Exchange

**Parent:** [../](../)

## Purpose

This directory contains Business Rules Exchange (BREX) data modules that define project-specific validation rules for S1000D data modules. BREX provides validation beyond standard S1000D schema validation, enforcing organization-specific conventions and requirements.

## What is BREX?

BREX (Business Rules Exchange) is an S1000D mechanism for defining and sharing validation rules. It allows organizations to specify:
- Required elements beyond schema requirements
- Allowed values for specific attributes
- Context-dependent validation rules
- Project-specific naming conventions
- Enterprise code and language requirements

## Contents

### DMC-BWQ1-A-57-90-00-00-00A-022A-B-EN-US.xml

This is the BREX data module for the 57-90-00 template example package.

**Information Code:** 022A-B (BREX)

**Key Validation Rules:**
- **CR-001**: All DMs must reference BREX - Ensures every data module includes a brexDmRef element
- **CR-002**: Enterprise code must be IDEALE.eu - Enforces consistent enterprise code usage
- **CR-003**: Language must be en-US - Ensures language and country code consistency
- **CR-004**: Security classification required - Mandates security classification in every DM
- **CR-005**: Title style enforcement - Requires both techName and infoName elements
- **CR-006**: External schema reference policy - Validates external publication references

**Notation Rules:**
- **NR-001**: SVG graphics preferred - Recommends SVG format for scalable graphics

## Using BREX

### Referencing BREX in Data Modules

All data modules must include a BREX reference in their `dmStatus` section:

```xml
<brexDmRef>
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A"
              systemCode="57" subSystemCode="9" subSubSystemCode="0"
              assyCode="00" disassyCode="00" disassyCodeVariant="A"
              infoCode="022" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
  </dmRef>
</brexDmRef>
```

### Validation

BREX rules can be validated using Schematron processors:

```bash
# Validate data modules against BREX rules
schematron DMC-BWQ1-A-57-90-00-00-00A-022A-B-EN-US.xml ../DMC/*.xml
```

## Customizing BREX Rules

When adapting this template for your project:

1. **Update BREX DMC code** to match your project's codes
2. **Modify context rules** to reflect your organization's requirements
3. **Add new rules** as needed for project-specific validation
4. **Update references** in all data modules to point to your BREX

### Adding New Rules

To add a new context rule:

```xml
<contextRule>
  <contextRuleIdent>CR-XXX</contextRuleIdent>
  <contextRuleTitle>Your Rule Title</contextRuleTitle>
  <contextRuleContext>
    <context>/path/to/element</context>
  </contextRuleContext>
  <contextRuleConstraint>
    <assert test="condition">Error message</assert>
  </contextRuleConstraint>
</contextRule>
```

## BREX File Naming Convention

BREX files follow S1000D DMC naming with information code 022:

```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC>-<DC><DCV>-022<ICV>-<ILC>-<LIC>-<CIC>.xml

Where:
- IC: 022 (BREX information code)
- ICV: A or B (typically B for BREX)
```

## Standards

- S1000D Issue 6.0 BREX specification
- ISO Schematron validation language
- XPath 1.0/2.0 for rule expressions

## Related Documentation

- [CSDB README](../README.md) - Parent directory documentation
- [DMC Directory](../DMC/) - Data modules that reference this BREX
- [S1000D Specification](http://www.s1000d.org) - Official S1000D documentation

---

**Note:** BREX rules are enforced during data module validation and publication processes. Ensure all data modules in your project reference the appropriate BREX file.
