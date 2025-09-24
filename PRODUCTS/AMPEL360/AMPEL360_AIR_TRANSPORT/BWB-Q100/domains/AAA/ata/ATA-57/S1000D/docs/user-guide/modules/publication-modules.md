# Publication Modules (PM/DML/DMRL)

Publication modules define the structure and requirements for technical publications, including Data Module Requirements Lists (DMRL) and publication organization.

## Publication Module Structure

### Publication Module (PM)
Publication Modules define how data modules are organized into complete technical publications.

```xml
<publicationModule>
  <pmIdent>
    <pmCode modelIdentCode="BWQ1" pmIssuer="AMPEL360" pmNumber="ATA57" pmVolume="00"/>
    <language languageIsoCode="en" countryIsoCode="US"/>
    <issueInfo issueNumber="001" inWork="01"/>
  </pmIdent>
  
  <pmAddressItems>
    <issueDate year="2025" month="01" day="21"/>
    <pmTitle>
      <shortPmTitle>ATA-57 Wings Technical Publication</shortPmTitle>
    </pmTitle>
  </pmAddressItems>
  
  <pmStatus issueType="new">
    <security securityClassification="01"/>
    <dataRestrictions>
      <restrictionInfo>
        <classificationString>INTERNAL–EVIDENCE-REQUIRED</classificationString>
      </restrictionInfo>
    </dataRestrictions>
    <responsiblePartnerCompany>
      <enterpriseName>AMPEL360</enterpriseName>
    </responsiblePartnerCompany>
  </pmStatus>
</publicationModule>
```

## Data Module Requirements List (DMRL)

### DMRL Location and Structure
The DMRL defines all required data modules for the ATA-57 publication:

**File Location**: `publication_modules/DML-BWQ1-ATA57-00_EN-US.xml`

### DMRL Entry Structure
```xml
<dmlContent>
  <dmlEntry>
    <dmRef>
      <dmRefIdent>
        <dmCode modelIdentCode="BWQ1" systemDiffCode="A" 
                systemCode="57" subSystemCode="10" subSubSystemCode="00" 
                assyCode="00" disassyCode="00" disassyCodeVariant="A" 
                infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
      </dmRefIdent>
      <dmRefAddressItems>
        <dmTitle>
          <techName>BWB-Q100</techName>
          <infoName>Wing Structure - General Description</infoName>
        </dmTitle>
      </dmRefAddressItems>
    </dmRef>
    <dmrlEntryType>required</dmrlEntryType>
    <security securityClassification="01"/>
  </dmlEntry>
</dmlContent>
```

### DMRL Entry Types
- **required**: Essential data modules that must be authored
- **optional**: Modules that may be created based on configuration
- **conditional**: Modules required only under specific conditions

## Coverage Verification

### DMRL→DM Coverage Check
The validation pipeline verifies that all required DMRL entries have corresponding data modules:

```bash
# Coverage verification process
1. Parse DMRL entries marked as "required"
2. Check for corresponding XML files in data_modules/
3. Report missing modules
4. Generate DM shells for missing required modules
5. Update indices to reflect current coverage
```

### Coverage Report Example
```
DMRL Coverage Report - ATA-57
=============================
Total DMRL Entries: 156
Required Entries: 134
Optional Entries: 22

Authored Modules: 89 (66.4%)
Missing Required: 45 (33.6%)
Optional Authored: 7 (31.8%)

Missing Required Modules:
- DMC-BWQ1-A-57-10-60-00-00A-040A-D-EN-US (Wing Equipment Mounting)
- DMC-BWQ1-A-57-20-70-00-00A-345A-D-EN-US (Fuel System Pressure Test)
- DMC-BWQ1-A-57-30-80-00-00A-700A-D-EN-US (Control Surface Installation)
```

## DM Shell Generation

### Automatic Shell Creation
The system can generate skeleton data modules for missing DMRL entries:

```xml
<!-- Generated shell structure -->
<dmodule>
  <dmIdent>
    <dmCode modelIdentCode="BWQ1" systemDiffCode="A" 
            systemCode="57" subSystemCode="10" subSubSystemCode="00" 
            assyCode="00" disassyCode="00" disassyCodeVariant="A" 
            infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    <language languageIsoCode="en" countryIsoCode="US"/>
    <issueInfo issueNumber="001" inWork="01"/>
  </dmIdent>
  
  <dmAddressItems>
    <issueDate year="2025" month="01" day="21"/>
    <dmTitle>
      <techName>BWB-Q100</techName>
      <infoName>TO BE COMPLETED - Wing Structure General Description</infoName>
    </dmTitle>
  </dmAddressItems>
  
  <content>
    <description>
      <para>PLACEHOLDER: Content to be authored for this data module.</para>
      <para>DMRL Entry: [Reference to DMRL requirement]</para>
      <para>Information Code: 040 (General Description)</para>
    </description>
  </content>
</dmodule>
```

### Shell Generation Process
```bash
# Generate shells for missing required modules
python3 scripts/generate_dm_shells.py \
  --dmrl publication_modules/DML-BWQ1-ATA57-00_EN-US.xml \
  --output data_modules/ \
  --required-only
```

## Publication Organization

### Hierarchical Structure
Publication modules organize content hierarchically:

```
ATA-57 Wings Publication
├── 57-00 General (Introduction, Limitations)
├── 57-10 Wing Structure
│   ├── 57-10-00 General Description
│   ├── 57-10-10 Wing Box
│   ├── 57-10-20 Wing Surfaces
│   └── 57-10-30 Wing-Body Interface
├── 57-20 Fuel Interfaces
├── 57-30 Control Surfaces
├── 57-40 High-Lift Systems
└── 57-50 Equipment Integration
```

### Content Buckets by Information Code
```
Descriptive Modules (data_modules/descriptive/)
├── IC 040: General descriptions
├── IC 042: Operation descriptions  
├── IC 034: Technical data
└── IC 050-056: Specialized descriptions

Procedural Modules (data_modules/procedural/)
├── IC 5xx: Removal procedures
├── IC 6xx: Servicing procedures
└── IC 7xx: Installation procedures

Test Modules (data_modules/descriptive/)
├── IC 310: Visual inspections
├── IC 345: System tests
└── IC 350: Functional checks

Fault Isolation (data_modules/fault/)
├── IC 420: General fault isolation
└── IC 421-428: System-specific FI

IPD Modules (data_modules/ipd/)
├── IC 900: Illustrated parts data
└── IC 910: Special tools/equipment
```

## Index Generation

### Automatic Index Updates
The system automatically generates indices when content changes:

#### DM Index Structure
```xml
<!-- indices/dm_index.xml -->
<dmIndex>
  <dmIndexEntry>
    <dmCode modelIdentCode="BWQ1" systemDiffCode="A" 
            systemCode="57" subSystemCode="10" subSubSystemCode="00" 
            assyCode="00" disassyCode="00" disassyCodeVariant="A" 
            infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    <dmTitle>
      <techName>BWB-Q100</techName>
      <infoName>Wing Structure - General Description</infoName>
    </dmTitle>
    <dmPath>data_modules/descriptive/DMC-BWQ1-A-57-10-00-00-00A-040A-D-EN-US.xml</dmPath>
    <issueInfo issueNumber="001" inWork="01"/>
    <issueDate year="2025" month="01" day="21"/>
  </dmIndexEntry>
</dmIndex>
```

#### Index Generation Command
```bash
# Regenerate all indices
python3 scripts/generate_indices.py \
  --source data_modules/ \
  --output indices/ \
  --validate
```

## DDN Packaging

### Delivery Data Number (DDN) Structure
DDN packages organize publication content for delivery:

```
DDN-BWQ1-ATA57-001-00_EN-US/
├── data_modules/
│   ├── descriptive/
│   ├── procedural/
│   ├── fault/
│   └── ipd/
├── publication_modules/
│   └── DML-BWQ1-ATA57-00_EN-US.xml
├── multimedia/
├── schemas/
├── indices/
└── metadata/
    ├── ddn_manifest.xml
    └── validation_report.xml
```

### DDN Manifest
```xml
<ddnManifest>
  <ddnIdent>
    <ddnCode>DDN-BWQ1-ATA57-001-00</ddnCode>
    <language languageIsoCode="en" countryIsoCode="US"/>
  </ddnIdent>
  
  <ddnContent>
    <totalDataModules>89</totalDataModules>
    <totalMultimediaObjects>156</totalMultimediaObjects>
    <packageSize>45.2 MB</packageSize>
    <validationStatus>PASSED</validationStatus>
  </ddnContent>
  
  <deliveryInfo>
    <creationDate>2025-01-21</creationDate>
    <creator>BWQ1 Authoring System</creator>
    <deliveryMethod>electronic</deliveryMethod>
  </deliveryInfo>
</ddnManifest>
```

## Validation Integration

### Publication-Level Validation
```bash
# Complete publication validation
python3 scripts/validate_publication.py \
  --dmrl publication_modules/DML-BWQ1-ATA57-00_EN-US.xml \
  --data data_modules/ \
  --schemas schemas/ \
  --report validation/publication_report.xml
```

### Validation Checklist
- [ ] All required DMRL entries have corresponding data modules
- [ ] Cross-references between modules resolve correctly
- [ ] Publication structure is logically organized
- [ ] Security classifications are consistent
- [ ] Multimedia objects are accessible and properly referenced

## Tools and Scripts

### Available Utilities
```bash
# DMRL management
scripts/dmrl_coverage.py          # Check DMRL coverage
scripts/generate_dm_shells.py     # Create missing module shells
scripts/update_dmrl.py             # Update DMRL from authored content

# Index management  
scripts/generate_indices.py       # Regenerate all indices
scripts/validate_indices.py       # Verify index consistency

# Publication management
scripts/build_publication.py      # Build complete publication package
scripts/validate_publication.py   # Comprehensive publication validation
scripts/create_ddn.py              # Generate DDN delivery package
```

## Checklist

### DMRL Management
- [ ] All required data modules identified in DMRL
- [ ] Optional modules properly marked
- [ ] Conditional requirements clearly specified
- [ ] DMRL entries use correct DMC structure
- [ ] Security classifications appropriate

### Publication Structure
- [ ] Logical organization by subsystem and information code
- [ ] Cross-references between related modules
- [ ] Consistent naming conventions throughout
- [ ] Proper effectivity management
- [ ] Complete multimedia object inventory

### Validation and Delivery
- [ ] All required modules authored or shells generated
- [ ] Index consistency verified
- [ ] Publication-level validation passes
- [ ] DDN package complete and validated
- [ ] Delivery manifest accurate

## Common Mistakes

❌ **Incomplete DMRL**: Missing required entries for complex subsystems  
✅ **Correct**: Comprehensive analysis of all required content before DMRL finalization

❌ **Inconsistent DMC Structure**: Variations in data module coding conventions  
✅ **Correct**: Strict adherence to BWQ1 DMC naming standards across all entries

❌ **Missing Cross-References**: DMRL entries without proper module relationships  
✅ **Correct**: Include appropriate cross-references between related modules in DMRL

❌ **Outdated Indices**: Indices not updated after content changes  
✅ **Correct**: Automatic index regeneration as part of content update process

❌ **Invalid DDN Packaging**: Incomplete or inconsistent delivery packages  
✅ **Correct**: Comprehensive validation before DDN creation and delivery

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0