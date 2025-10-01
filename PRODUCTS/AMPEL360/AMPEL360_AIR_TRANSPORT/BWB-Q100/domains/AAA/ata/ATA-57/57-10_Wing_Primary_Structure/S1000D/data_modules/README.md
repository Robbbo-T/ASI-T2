# S1000D Data Modules - ATA-57-10 Wing Primary Structure

This directory contains all S1000D Issue 6.0 data modules for the BWB-Q100 Wing Primary Structure (ATA-57-10), organized for maximum maintainability and compliance with aerospace documentation standards.

## Quick Start

```bash
# Validate all data modules against BREX
python scripts/validate_s1000d.py --brex ../BREX/BREX.xml --dmrl ../DMRL/DMRL.xml

# Generate module statistics
python scripts/module_stats.py --directory . --output stats.json

# Check cross-references
python scripts/check_xrefs.py --directory . --report xref_report.html
```

## Organization

### 📁 Descriptive (`descriptive/`)
Technical descriptions, specifications, and design information for wing structural components. Each component follows a logical breakdown from general to specific.

- **57-10-10** Forward Spar - Primary load-bearing structure
- **57-10-20** Rear Spar - Secondary load-bearing structure  
- **57-10-30** Ribs - Structural support and load distribution
- **57-10-40** Skin Panels - Aerodynamic surface and fuel containment
- **57-10-50** Stringers - Longitudinal reinforcement
- **57-10-60** Attachments - Interface points and fittings

### 🔧 Procedural (`procedural/`)
Step-by-step procedures organized by maintenance task type, with clear prerequisites and completion criteria.

- **inspection/** - Visual and NDT inspection procedures with acceptance criteria
- **removal_installation/** - R/I procedures with torque sequences and safety precautions
- **repair/** - Standard repair procedures with allowable damage limits

### 📊 Illustrated Parts Data (`ipd/`)
Parts identification, illustrated breakdowns, and item-level data for all components, synchronized with 360IPCirq for reusability.

## Data Module Coding System

S1000D data module codes follow the standard pattern:
```
DMC-BWQ1-A-57-10-XX-YY-ZZA-IIIIA-D-EN-US.xml
```

### Code Breakdown
| Segment | Meaning | Example | Description |
|---------|---------|---------|-------------|
| **BWQ1** | Model Identifier | BWQ1 | BWB-Q100 Aircraft |
| **A** | System Difference Code | A | System variant |
| **57-10-XX** | ATA Chapter/Subchapter | 57-10-10 | Wing Primary Structure - Forward Spar |
| **YY-ZZA** | Assembly/Disassembly/Item | 00-00A | Top-level assembly |
| **IIIIA** | Information Code | 040A | Descriptive information |
| **D** | Content Type | D | Data module |
| **EN-US** | Language | EN-US | English (US) |

## Information Codes Reference

| Code | Type | Purpose | Example Usage |
|------|------|---------|---------------|
| **040A** | Descriptive | Technical descriptions, specifications | Component geometry, materials |
| **520A** | Inspection | Visual/NDT procedures, acceptance criteria | Crack detection, corrosion checks |
| **720A** | R/I | Removal/Installation procedures | Component replacement, maintenance |
| **941A** | IPD | Illustrated parts data | Part numbers, quantities, illustrations |

## Module Matrix

| Component | Descriptive | Inspection | R/I | IPD | Total |
|-----------|-------------|------------|-----|-----|-------|
| Forward Spar | 10 | 7 | 3 | 4 | 24 |
| Rear Spar | 10 | 5 | 2 | 4 | 21 |
| Ribs | 7 | 3 | 0 | 3 | 13 |
| Skin Panels | 13 | 3 | 1 | 2 | 19 |
| Stringers | 5 | 1 | 0 | 2 | 8 |
| Attachments | 5 | 2 | 0 | 1 | 8 |
| **TOTAL** | **50** | **21** | **6** | **16** | **93** |

## Data Module List (XML)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- S1000D Data Module List - ATA-57-10 Wing Primary Structure -->
<!-- BWB-Q100 Aircraft - Issue 6.0 -->
<dmList>
  <dmListIdent>
    <dmListIssue>
      <dmListIssueNumber>001</dmListIssueNumber>
      <dmListIssueInWork>00</dmListIssueInWork>
    </dmListIssue>
    <dmListType>frontmatter</dmListType>
  </dmListIdent>
  
  <!-- Forward Spar Modules -->
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemCode="0" assyCode="10" disassyCode="00" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar</techName>
        <infoName>General Description and Architecture</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemCode="0" assyCode="10" disassyCode="01" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Inboard Section LH</techName>
        <infoName>Material, Geometry, Fastener Pattern</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="02" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Inboard Section RH</techName>
        <infoName>Material, Geometry, Fastener Pattern</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="03" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Mid Section LH</techName>
        <infoName>Splice Joints, Load Transfer</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="04" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Mid Section RH</techName>
        <infoName>Splice Joints, Load Transfer</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="05" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Outboard Section LH</techName>
        <infoName>Taper, Tip Attachment</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="06" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Outboard Section RH</techName>
        <infoName>Taper, Tip Attachment</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="07" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Upper Cap</techName>
        <infoName>Composite Layup, Stringer Runouts</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="08" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Lower Cap</techName>
        <infoName>Composite Layup, Fuel Seal Interface</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="09" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Web</techName>
        <infoName>Shear Panel, Stiffeners, Lightening Holes</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <!-- Forward Spar Inspection Modules -->
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="00" disassyCodeVariant="A" infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar Inspection</techName>
        <infoName>Visual, NDT Methods, Intervals</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="01" disassyCodeVariant="A" infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Inboard Section LH Inspection</techName>
        <infoName>Critical Zones, Crack Initiation Sites</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="02" disassyCodeVariant="A" infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Inboard Section RH Inspection</techName>
        <infoName>Critical Zones, Crack Initiation Sites</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="03" disassyCodeVariant="A" infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Mid Section LH Inspection</techName>
        <infoName>Splice Joint Eddy Current</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="04" disassyCodeVariant="A" infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Mid Section RH Inspection</techName>
        <infoName>Splice Joint Eddy Current</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="05" disassyCodeVariant="A" infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Outboard Section LH Inspection</techName>
        <infoName>Tip Attachment Ultrasonic</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="06" disassyCodeVariant="A" infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Outboard Section RH Inspection</techName>
        <infoName>Tip Attachment Ultrasonic</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <!-- Forward Spar R/I Modules -->
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="00" disassyCodeVariant="A" infoCode="720" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar R/I</techName>
        <infoName>General Precautions, Tooling Requirements</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="01" disassyCodeVariant="A" infoCode="720" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Inboard Section LH R/I</techName>
        <infoName>Fuel Drain, Fastener Sequence</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="02" disassyCodeVariant="A" infoCode="720" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Inboard Section RH R/I</techName>
        <infoName>Fuel Drain, Fastener Sequence</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <!-- Forward Spar IPD Modules -->
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="00" disassyCodeVariant="A" infoCode="941" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Forward Spar IPD</techName>
        <infoName>Parts Catalog, Applicability</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="01" disassyCodeVariant="A" infoCode="941" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Inboard Sections IPD</techName>
        <infoName>Part Numbers, Quantities</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="02" disassyCodeVariant="A" infoCode="941" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Mid Sections IPD</techName>
        <infoName>Splice Kit Components</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="10" disassyCode="03" disassyCodeVariant="A" infoCode="941" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Outboard Sections IPD</techName>
        <infoName>Tip Attachments</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <!-- Rear Spar Modules -->
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="00" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar</techName>
        <infoName>General Description and Load Paths</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="01" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Inboard Section LH</techName>
        <infoName>Landing Gear Beam Interface</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="02" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Inboard Section RH</techName>
        <infoName>Landing Gear Beam Interface</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="03" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Mid Section LH</techName>
        <infoName>Control Surface Hinge Locations</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="04" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Mid Section RH</techName>
        <infoName>Control Surface Hinge Locations</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="05" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Outboard Section LH</techName>
        <infoName>Aileron Support Structure</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="06" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Outboard Section RH</techName>
        <infoName>Aileron Support Structure</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="07" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Upper Cap</techName>
        <infoName>Tension Loads, Splice Design</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="08" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Lower Cap</techName>
        <infoName>Compression Loads, Anti-Buckling</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="1" subSubSystemName="0" assyCode="20" disassyCode="09" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
    </dmRefIdent>
    <dmRefAddress>
      <dmTitle>
        <techName>Rear Spar Web</techName>
        <infoName>Shear Transfer, Actuator Cutouts</infoName>
      </dmTitle>
    </dmRefAddress>
    <dmRefStatus>
      <dmRefStatusType>in-work</dmRefStatusType>
    </dmRefStatus>
  </dmRef>
  
  <!-- Additional modules would continue for Ribs, Skin Panels, Stringers, and Attachments -->
  <!-- This is a representative sample showing the structure and format -->
  
</dmList>
```

## Workflows & Best Practices

### 🔄 Module Creation Workflow

1. **Check DMRL** - Verify module is listed in requirements
2. **Use Template** - Start from approved template
3. **Create Content** - Follow S1000D authoring rules
4. **Validate BREX** - Run validation against BREX rules
5. **Check XRefs** - Verify all cross-references are valid
6. **Peer Review** - Technical review by subject matter expert
7. **Configuration Approval** - CM approval for release
8. **QS Seal** - Apply quality seal and register in UTCS

### 📋 Module Template Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dmodule xmlns:xlink="http://www.w3.org/1999/xlink">
  <identAndStatusSection>
    <dmAddress>
      <dmIdent>
        <dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" 
               subSystemCode="1" subSubSystemCode="0" assyCode="XX" 
               disassyCode="YY" disassyCodeVariant="A" infoCode="ZZZ" 
               infoCodeVariant="A" itemLocationCode="D"/>
        <dmAddressItems>
          <issueInfo issueNumber="001" inWork="00"/>
          <dmTitle>
            <techName>[Component Name]</techName>
            <infoName>[Specific Information]</infoName>
          </dmTitle>
        </dmAddressItems>
      </dmIdent>
    </dmAddress>
    <dmStatus>
      <dmStatusType>in-work</dmStatusType>
    </dmStatus>
  </identAndStatusSection>
  
  <content>
    <!-- Module content goes here -->
  </content>
</dmodule>
```

### 🔍 Validation Checklist

- [ ] Module exists in DMRL
- [ ] BREX validation passes
- [ ] All cross-references resolve
- [ ] ATA-20 forms referenced correctly
- [ ] Evidence links are valid
- [ ] Acceptance criteria defined
- [ ] Effectivity rules applied
- [ ] Language and terminology consistent
- [ ] Graphics and illustrations referenced
- [ ] Change control information complete

## Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| BREX validation fails | Missing required elements | Add required elements per BREX rules |
| Cross-reference broken | Target module not found | Verify target exists and update reference |
| Invalid information code | Wrong code for content type | Use correct information code (040A, 520A, etc.) |
| Missing ATA-20 reference | Procedure not linked to standard | Add reference to appropriate ATA-20 form |
| Effectivity not applied | Module not assigned to aircraft | Add effectivity rules in applicability section |

## Support & Resources

- **S1000D Specification**: Issue 6.0 documentation
- **BREX Rules**: `../BREX/BREX.xml`
- **DMRL Requirements**: `../DMRL/DMRL.xml`
- **ATA Standards**: `../../ATA-20/` directory
- **Validation Scripts**: `../../scripts/` directory
- **Templates**: `../../templates/` directory

---

*Part of ATA-57-10 Wing Primary Structure — Configuration controlled under UTCS/QS v5.0*  
*Last updated: 2025-10-01 | Version: 1.0.0*
