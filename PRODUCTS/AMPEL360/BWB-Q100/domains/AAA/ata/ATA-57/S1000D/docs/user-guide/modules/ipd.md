# IPD/Parts Modules (900/910)

Illustrated Parts Data (IPD) modules provide interactive part catalogs with visual identification, part numbers, and hierarchical assembly structures.

## Information Code Categories

### IC 900 - Illustrated Parts Data
- Complete parts breakdown with illustrations
- Part number cross-references
- Assembly/subassembly hierarchy
- Effectivity and configuration management

### IC 910 - Special Tools and Equipment
- Specialized tooling requirements
- Ground support equipment
- Test equipment specifications
- Tool part numbers and suppliers

## IPD Module Structure

### Basic IPD Framework
```xml
<content>
  <illustratedPartsCatalog>
    <figure>
      <graphic infoEntityIdent="ICN-BWQ1-A-571010-A-001-01">
        <symbol infoEntityIdent="ICN-BWQ1-A-571010-A-001-01"/>
      </graphic>
      <legend>
        <crewDrillDownRef>
          <callout calloutNumber="1">
            <para>Wing box assembly</para>
          </callout>
          <callout calloutNumber="2">
            <para>Forward spar</para>
          </callout>
          <callout calloutNumber="3">
            <para>Aft spar</para>
          </callout>
        </crewDrillDownRef>
      </legend>
    </figure>
    
    <catalogSeqNumber>
      <catalogSeqNumberValue>57-10-10</catalogSeqNumberValue>
      <partsList>
        <partEntry>
          <calloutNumber calloutNumber="1"/>
          <partAndPartExtension>
            <partNumber>BWQ1-57-1001-001</partNumber>
            <partTitle>Wing box assembly, center section</partTitle>
          </partAndPartExtension>
          <quantityPerNextHigherAssy>1</quantityPerNextHigherAssy>
          <partLocationList>
            <partLocation>
              <partLocationIdent>57-10-10-00</partLocationIdent>
            </partLocation>
          </partLocationList>
        </partEntry>
      </partsList>
    </catalogSeqNumber>
  </illustratedPartsCatalog>
</content>
```

## IPC Viewer Integration

### Interactive Features
The IETP includes an integrated IPC (Illustrated Parts Catalog) viewer that provides:

- **Visual Part Identification**: Click-to-identify parts on illustrations
- **Part Number Lookup**: Search by part number or description
- **Assembly Navigation**: Drill-down from assemblies to components
- **Effectivity Filtering**: Show only parts applicable to specific configurations

### IPC Viewer Behavior
```javascript
// IPC viewer functionality in IETP
1. Load IPD module with illustration and parts list
2. Display interactive illustration with clickable callouts
3. Highlight selected parts in both illustration and parts list
4. Provide part detail popup with:
   - Part number and title
   - Quantity per assembly
   - Effectivity information
   - Cross-reference to descriptive modules
```

### Generate Illustration Feature
The IPC viewer includes an AI-powered "Generate Illustration" button:

#### How It Works
1. **Parts List Analysis**: Extracts part descriptions and relationships from IPD module
2. **AI Prompt Generation**: Creates detailed prompt for illustration generation
3. **Image Generation**: Uses AI to create technical illustration showing part relationships
4. **File Management**: Saves generated illustration with proper ICN naming
5. **Module Update**: Updates `<graphic href>` reference in IPD module

#### Generated Illustration Naming
```
multimedia/graphics/generated/
├── ICN-BWQ1-A-571010-A-001-01.svg    # Wing box assembly
├── ICN-BWQ1-A-571010-A-002-01.svg    # Forward spar detail
└── ICN-BWQ1-A-571010-A-003-01.svg    # Aft spar detail
```

## Part Hierarchy and Relationships

### Parent-Child Relationships
```xml
<partEntry>
  <calloutNumber calloutNumber="1"/>
  <partAndPartExtension>
    <partNumber>BWQ1-57-1001-001</partNumber>
    <partTitle>Wing box assembly</partTitle>
  </partAndPartExtension>
  <quantityPerNextHigherAssy>1</quantityPerNextHigherAssy>
  
  <!-- Child components -->
  <partEntry>
    <calloutNumber calloutNumber="1A"/>
    <partAndPartExtension>
      <partNumber>BWQ1-57-1001-101</partNumber>
      <partTitle>Forward spar</partTitle>
    </partAndPartExtension>
    <quantityPerNextHigherAssy>1</quantityPerNextHigherAssy>
  </partEntry>
  
  <partEntry>
    <calloutNumber calloutNumber="1B"/>
    <partAndPartExtension>
      <partNumber>BWQ1-57-1001-201</partNumber>
      <partTitle>Aft spar</partTitle>
    </partAndPartExtension>
    <quantityPerNextHigherAssy>1</quantityPerNextHigherAssy>
  </partEntry>
</partEntry>
```

### Assembly Cross-References
```xml
<partEntry>
  <partAndPartExtension>
    <partNumber>BWQ1-57-1001-301</partNumber>
    <partTitle>Wing skin panel</partTitle>
  </partAndPartExtension>
  <partRef>
    <dmRef>
      <dmRefIdent>
        <dmCode modelIdentCode="BWQ1" systemDiffCode="A" 
                systemCode="57" subSystemCode="10" subSubSystemCode="20" 
                assyCode="00" disassyCode="00" disassyCodeVariant="A" 
                infoCode="900" infoCodeVariant="A" itemLocationCode="D"/>
      </dmRefIdent>
      <dmRefAddressItems>
        <dmTitle><infoName>Wing Skin Panel Assembly</infoName></dmTitle>
      </dmRefAddressItems>
    </dmRef>
  </partRef>
</partEntry>
```

## Effectivity Management

### Configuration-Specific Parts
```xml
<partEntry>
  <calloutNumber calloutNumber="5"/>
  <partAndPartExtension>
    <partNumber>BWQ1-57-2001-001</partNumber>
    <partTitle>Fuel interface coupling</partTitle>
  </partAndPartExtension>
  <quantityPerNextHigherAssy>2</quantityPerNextHigherAssy>
  <effectivity>
    <configuration>
      <configString>BWB-Q100 with hydrogen fuel system</configString>
    </configuration>
  </effectivity>
</partEntry>

<partEntry>
  <calloutNumber calloutNumber="5"/>
  <partAndPartExtension>
    <partNumber>BWQ1-57-2001-002</partNumber>
    <partTitle>Conventional fuel coupling</partTitle>
  </partAndPartExtension>
  <quantityPerNextHigherAssy>2</quantityPerNextHigherAssy>
  <effectivity>
    <configuration>
      <configString>BWB-Q100 conventional fuel configuration</configString>
    </configuration>
  </effectivity>
</partEntry>
```

### Serial Number Effectivity
```xml
<partEntry>
  <effectivity>
    <serialNumber>
      <serialNumberRange>
        <serialNumberFrom>BWQ1-001</serialNumberFrom>
        <serialNumberTo>BWQ1-050</serialNumberTo>
      </serialNumberRange>
    </serialNumber>
  </effectivity>
</partEntry>
```

## Multimedia Object Integration

### ICN File Naming Convention
```
ICN-{MIC}-{SysDiff}-{System}{SubSys}{SubSubSys}-{Variant}-{Seq}-{Issue}

Examples:
ICN-BWQ1-A-571010-A-001-01.svg    # Wing box overview
ICN-BWQ1-A-571010-A-002-01.svg    # Detail view A
ICN-BWQ1-A-571010-A-003-01.svg    # Detail view B
```

### Graphic References
```xml
<graphic infoEntityIdent="ICN-BWQ1-A-571010-A-001-01">
  <symbol infoEntityIdent="ICN-BWQ1-A-571010-A-001-01"/>
</graphic>
```

### File Storage Structure
```
multimedia/graphics/
├── technical/
│   ├── ICN-BWQ1-A-571010-A-001-01.svg
│   └── ICN-BWQ1-A-571010-A-002-01.svg
└── generated/
    ├── ICN-BWQ1-A-571010-A-003-01.svg
    └── ICN-BWQ1-A-571010-A-004-01.svg
```

## Special Tooling (IC 910)

### Tool Specifications
```xml
<catalogSeqNumber>
  <catalogSeqNumberValue>57-10-TOOLS</catalogSeqNumberValue>
  <partsList>
    <partEntry>
      <calloutNumber calloutNumber="T1"/>
      <partAndPartExtension>
        <partNumber>BWQ1-TOOL-57-001</partNumber>
        <partTitle>Wing box lifting fixture</partTitle>
      </partAndPartExtension>
      <quantityPerNextHigherAssy>1</quantityPerNextHigherAssy>
      <partLocationList>
        <partLocation>
          <partLocationIdent>GROUND-SUPPORT</partLocationIdent>
        </partLocation>
      </partLocationList>
      <partRef>
        <externalPubRef>
          <externalPubRefIdent>
            <externalPubCode>GSE-MANUAL-001</externalPubCode>
          </externalPubRefIdent>
          <externalPubRefAddressItems>
            <externalPubTitle>Ground Support Equipment Manual</externalPubTitle>
          </externalPubRefAddressItems>
        </externalPubRef>
      </partRef>
    </partEntry>
  </partsList>
</catalogSeqNumber>
```

### Test Equipment References
```xml
<partEntry>
  <partAndPartExtension>
    <partNumber>BWQ1-TEST-57-001</partNumber>
    <partTitle>Wing load test fixture</partTitle>
  </partAndPartExtension>
  <partRef>
    <dmRef>
      <dmRefIdent>
        <dmCode infoCode="345" infoCodeVariant="A"/>
      </dmRefIdent>
      <dmRefAddressItems>
        <dmTitle><infoName>Wing Load Test Procedure</infoName></dmTitle>
      </dmRefAddressItems>
    </dmRef>
  </partRef>
</partEntry>
```

## Quality Standards

### Illustration Requirements
- **Technical Accuracy**: All parts must be correctly positioned and proportioned
- **Callout Clarity**: Callout numbers must be clearly visible and unambiguous
- **Detail Level**: Sufficient detail for part identification without over-complexity
- **Consistency**: Illustration style consistent across all IPD modules

### Part Data Accuracy
- **Part Numbers**: Verified against engineering parts database
- **Quantities**: Accurate count per next higher assembly
- **Effectivity**: Current configuration and serial number applicability
- **Cross-References**: Valid links to related modules and external publications

## Checklist

### IPD Development
- [ ] All parts in assembly identified and numbered
- [ ] Illustration created or generated showing all callout items
- [ ] Part numbers verified against engineering database
- [ ] Quantities per assembly confirmed
- [ ] Effectivity properly specified for all configurations
- [ ] Cross-references to related modules validated

### IPC Viewer Compatibility
- [ ] Illustration uses proper ICN naming convention
- [ ] Callout numbers match between illustration and parts list
- [ ] Interactive elements function correctly in IETP
- [ ] Part detail information complete and accurate
- [ ] Search functionality works for part numbers and descriptions

### Quality Assurance
- [ ] Technical review by engineering confirms accuracy
- [ ] All multimedia objects exist and render properly
- [ ] Cross-reference links resolve correctly
- [ ] Effectivity filters work correctly in IPC viewer
- [ ] Generated illustrations meet quality standards

## Common Mistakes

❌ **Mismatched Callouts**: Callout numbers in illustration don't match parts list  
✅ **Correct**: Ensure exact correspondence between illustration callouts and parts list entries

❌ **Missing Effectivity**: Parts applicable to specific configurations not marked  
✅ **Correct**: Include proper effectivity tags for configuration-specific parts

❌ **Incorrect ICN Naming**: Graphics not following standard naming convention  
✅ **Correct**: Use proper ICN format: ICN-BWQ1-A-{system}-{variant}-{seq}-{issue}

❌ **Broken Cross-References**: Links to non-existent assembly or descriptive modules  
✅ **Correct**: Validate all cross-references during development and updates

❌ **Poor Illustration Quality**: Generated illustrations lack sufficient detail  
✅ **Correct**: Review and enhance AI-generated illustrations for technical accuracy

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0