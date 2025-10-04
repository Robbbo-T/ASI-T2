# PUB - Publications

**Parent:** [../](../)

## Purpose

This directory contains publication-level data modules and lists that organize and manage collections of data modules. These files define which data modules are included in a publication and how they are structured.

## Contents

### DMRL-BWQ1-57-90-00.xml (2.3 KB)

**Type:** Data Module Requirement List  
**Purpose:** Lists all data modules required for the 57-90-00 documentation package

**Function:**
- Specifies all data modules that make up the publication
- Defines the scope of the documentation package
- Used by publishing systems to collect and organize DMs
- Serves as a manifest for the documentation set

**Contains references to:**
1. DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml (Descriptive)
2. DMC-BWQ1-A-57-90-00-00-00A-520A-D-EN-US.xml (Procedural)
3. DMC-BWQ1-A-57-90-00-00-00A-941A-D-EN-US.xml (IPD)

## What is DMRL?

The Data Module Requirement List (DMRL) is an S1000D mechanism for:
- **Scoping** - Defining which DMs belong to a publication
- **Organization** - Structuring DMs into logical groups
- **Management** - Tracking DM requirements for projects
- **Publishing** - Providing input to publication generation tools

## DMRL Structure

```xml
<dmrl>
  <identAndStatusSection>
    <dmrlAddress>
      <dmrlIdent>...</dmrlIdent>
      <dmrlAddressItems>...</dmrlAddressItems>
    </dmrlAddress>
    <dmrlStatus>...</dmrlStatus>
  </identAndStatusSection>
  
  <requirementList>
    <requiredDm>
      <dmRefIdent>...</dmRefIdent>
    </requiredDm>
    <!-- Additional DMs -->
  </requirementList>
</dmrl>
```

## DMRL Naming Convention

DMRL files use a simplified naming pattern:

```
DMRL-<MIC>-<SC>-<SSC>-<SSSC>.xml

Example: DMRL-BWQ1-57-90-00.xml

Where:
- MIC: BWQ1 (Model Identification Code)
- SC: 57 (System Code)
- SSC: 90 (Sub System Code)
- SSSC: 00 (Sub-Sub System Code)
```

## Adding Data Modules to DMRL

When you add a new data module to the DMC/ directory, update the DMRL:

```xml
<requiredDm>
  <dmRefIdent>
    <dmCode modelIdentCode="BWQ1" systemDiffCode="A"
            systemCode="57" subSystemCode="9" subSubSystemCode="0"
            assyCode="00" disassyCode="00" disassyCodeVariant="A"
            infoCode="XXX" infoCodeVariant="A" itemLocationCode="D"/>
    <language languageIsoCode="en" countryIsoCode="US"/>
  </dmRefIdent>
</requiredDm>
```

## Using DMRL

### Publication Generation

DMRL is used by publishing tools to:
1. Collect all required data modules
2. Resolve cross-references between DMs
3. Generate table of contents
4. Create complete publications (PDF, HTML, etc.)
5. Validate completeness of documentation set

### Example Publishing Command

```bash
# Generate publication from DMRL
s1000d-publish --dmrl DMRL-BWQ1-57-90-00.xml --output manual.pdf

# Validate DMRL and referenced DMs
s1000d-validate --dmrl DMRL-BWQ1-57-90-00.xml
```

## Other Publication Files

This directory can also contain:

### PM (Publication Module)

**File pattern:** `PMC-*.xml`  
**Purpose:** Defines publication structure, front matter, table of contents

Publication Modules provide:
- Title page information
- Table of contents structure
- Front matter (preface, introduction)
- Applicability statements
- Grouping and ordering of data modules

### DML (Data Module List)

**File pattern:** `DML-*.xml`  
**Purpose:** Lists data modules for exchange or delivery

Data Module Lists are used for:
- Delivery packages
- Update distributions
- Configuration management
- Data exchange between organizations

## Validation

Validate DMRL structure:

```bash
# Validate DMRL XML
xmllint --noout --schema s1000d/dmrl.xsd DMRL-*.xml

# Check referenced DMs exist
for dm in $(grep -oP 'DMC-[A-Z0-9-]+\.xml' DMRL-*.xml); do
  if [ ! -f "../DMC/$dm" ]; then
    echo "Missing: $dm"
  fi
done
```

## Maintaining DMRL

### When to Update

Update DMRL when you:
- ✅ Add new data modules
- ✅ Remove obsolete data modules
- ✅ Change DM codes (major revisions)
- ✅ Split or merge documentation sets

### What to Update

When updating DMRL:
1. **Add/remove `<requiredDm>` entries** as needed
2. **Update issue date** in dmrlAddressItems
3. **Increment issue number** if significant changes
4. **Update title** if scope changes
5. **Validate** against schema

## Best Practices

✅ **Keep DMRL current** - Update whenever DMs are added/removed  
✅ **Validate regularly** - Ensure all referenced DMs exist  
✅ **Use consistent ordering** - Group related DMs logically  
✅ **Document scope** - Use clear title describing coverage  
✅ **Version control** - Track changes to DMRL over time

## Advanced: Grouping Data Modules

DMRL can include grouping for better organization:

```xml
<requirementList>
  <reqGroup>
    <reqGroupTitle>Descriptive Information</reqGroupTitle>
    <requiredDm>...</requiredDm>
    <requiredDm>...</requiredDm>
  </reqGroup>
  
  <reqGroup>
    <reqGroupTitle>Procedures</reqGroupTitle>
    <requiredDm>...</requiredDm>
  </reqGroup>
</requirementList>
```

## Integration with CSMS

DMRL can be managed within Content Management Systems:
- **Check-in/check-out** - Version control for DMRL
- **Workflow** - Review and approval processes
- **Publishing** - Automated publication generation
- **Distribution** - Controlled release of documentation

## Standards Compliance

- S1000D Issue 6.0 DMRL specification
- XML 1.0
- UTF-8 encoding

## Related Documentation

- [CSDB README](../README.md) - Parent directory
- [DMC Directory](../DMC/) - Data modules referenced by DMRL
- [S1000D Specification](http://www.s1000d.org) - DMRL requirements

---

**Tip:** Start with a simple DMRL listing all DMs. As your documentation grows, add grouping and structure to organize DMs logically for better usability.
