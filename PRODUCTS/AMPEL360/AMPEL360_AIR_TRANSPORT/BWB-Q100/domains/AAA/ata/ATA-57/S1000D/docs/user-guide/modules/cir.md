# Common Information Repository (CIR)

The Common Information Repository provides standardized terminology, references, procedures, and configuration data shared across all S1000D data modules.

## CIR Purpose and Structure

### What is CIR?
Common Information Repository modules contain reusable information that appears in multiple data modules, ensuring consistency and reducing duplication across the technical publication.

### CIR Benefits
- **Consistency**: Standardized terminology and definitions
- **Efficiency**: Single-source maintenance of common content
- **Compliance**: Centralized management of regulatory references
- **Quality**: Reduced errors through centralized updates

## CIR Module Categories

### Terminology (CIR-BWQ1-00001)
**Location**: `common_information/terminology/CIR-BWQ1-00001.xml`

```xml
<commonInfoRepository>
  <cirIdent>
    <commonInfoDesignator>
      <commonInfoDesignatorIdent>CIR-BWQ1-00001</commonInfoDesignatorIdent>
    </commonInfoDesignator>
    <language languageIsoCode="en" countryIsoCode="US"/>
    <issueInfo issueNumber="001" inWork="01"/>
  </cirIdent>
  
  <cirContent>
    <commonInfoDescrPara>
      <title>BWQ1 Terminology Repository</title>
      <para>Standardized terminology for BWB-Q100 technical documentation.</para>
    </commonInfoDescrPara>
    
    <definitionList>
      <definitionListItem>
        <listItemTerm>BWB-Q100</listItemTerm>
        <listItemDefinition>
          <para>Blended Wing Body aircraft configuration with hydrogen propulsion system, 100-passenger capacity.</para>
        </listItemDefinition>
      </definitionListItem>
      
      <definitionListItem>
        <listItemTerm>Wing Box</listItemTerm>
        <listItemDefinition>
          <para>Primary structural component consisting of forward spar, aft spar, upper skin, lower skin, and intermediate ribs.</para>
        </listItemDefinition>
      </definitionListItem>
      
      <definitionListItem>
        <listItemTerm>H₂ System</listItemTerm>
        <listItemDefinition>
          <para>Hydrogen fuel storage, distribution, and management system including tanks, valves, regulators, and monitoring equipment.</para>
        </listItemDefinition>
      </definitionListItem>
    </definitionList>
  </cirContent>
</commonInfoRepository>
```

### References (CIR-BWQ1-00002)
**Location**: `common_information/references/CIR-BWQ1-00002.xml`

```xml
<cirContent>
  <commonInfoDescrPara>
    <title>Standard References</title>
    <para>Regulatory and industry standard references for BWQ1 documentation.</para>
  </commonInfoDescrPara>
  
  <definitionList>
    <definitionListItem>
      <listItemTerm>EASA CS-25</listItemTerm>
      <listItemDefinition>
        <para>European Union Aviation Safety Agency Certification Specifications for Large Aeroplanes.</para>
        <externalPubRef>
          <externalPubRefIdent>
            <externalPubCode>EASA-CS-25</externalPubCode>
          </externalPubRefIdent>
          <externalPubRefAddressItems>
            <externalPubTitle>Certification Specifications and Acceptable Means of Compliance for Large Aeroplanes</externalPubTitle>
          </externalPubRefAddressItems>
        </externalPubRef>
      </listItemDefinition>
    </definitionListItem>
    
    <definitionListItem>
      <listItemTerm>S1000D Issue 6.0</listItemTerm>
      <listItemDefinition>
        <para>International specification for technical publications using a common source database.</para>
        <externalPubRef>
          <externalPubRefIdent>
            <externalPubCode>S1000D-6.0</externalPubCode>
          </externalPubRefIdent>
        </externalPubRef>
      </listItemDefinition>
    </definitionListItem>
  </definitionList>
</cirContent>
```

### Safety Procedures (CIR-BWQ1-00003)
**Location**: `common_information/procedures/CIR-BWQ1-00003.xml`

```xml
<cirContent>
  <commonInfoDescrPara>
    <title>Standard Safety Procedures</title>
    <para>Common safety procedures referenced across multiple maintenance procedures.</para>
  </commonInfoDescrPara>
  
  <levelledPara>
    <title>Hydrogen Safety Protocol</title>
    <para>Standard safety protocol for all hydrogen system maintenance:</para>
    <sequentialList>
      <listItem>
        <para>Verify adequate ventilation in work area</para>
      </listItem>
      <listItem>
        <para>Eliminate all ignition sources within 10-meter radius</para>
      </listItem>
      <listItem>
        <para>Install hydrogen detection equipment</para>
      </listItem>
      <listItem>
        <para>Implement lock-out/tag-out procedures on all hydrogen supply valves</para>
      </listItem>
      <listItem>
        <para>Don hydrogen-rated personal protective equipment</para>
      </listItem>
    </sequentialList>
  </levelledPara>
  
  <levelledPara>
    <title>Lock-Out/Tag-Out Procedure</title>
    <para>Standard energy isolation procedure:</para>
    <sequentialList>
      <listItem>
        <para>Identify all energy sources (electrical, hydraulic, pneumatic, chemical)</para>
      </listItem>
      <listItem>
        <para>Notify affected personnel of impending lockout</para>
      </listItem>
      <listItem>
        <para>Shutdown equipment using normal operating procedures</para>
      </listItem>
      <listItem>
        <para>Isolate energy sources using lockout devices</para>
      </listItem>
      <listItem>
        <para>Apply personal locks and tags to isolation devices</para>
      </listItem>
      <listItem>
        <para>Verify isolation by attempting normal startup (controls only)</para>
      </listItem>
    </sequentialList>
  </levelledPara>
</cirContent>
```

### Configuration Data (CIR-BWQ1-00007)
**Location**: `common_information/configuration/CIR-BWQ1-00007.xml`

```xml
<cirContent>
  <commonInfoDescrPara>
    <title>BWQ1 Configuration Data</title>
    <para>Standard configuration parameters and limits for BWB-Q100 aircraft.</para>
  </commonInfoDescrPara>
  
  <levelledPara>
    <title>Fuel System Specifications</title>
    <table>
      <tgroup cols="3">
        <colspec colname="parameter"/>
        <colspec colname="value"/>
        <colspec colname="unit"/>
        <thead>
          <row>
            <entry>Parameter</entry>
            <entry>Value</entry>
            <entry>Unit</entry>
          </row>
        </thead>
        <tbody>
          <row>
            <entry>Hydrogen Tank Pressure (Operating)</entry>
            <entry>350</entry>
            <entry>bar</entry>
          </row>
          <row>
            <entry>Hydrogen Tank Pressure (Maximum)</entry>
            <entry>700</entry>
            <entry>bar</entry>
          </row>
          <row>
            <entry>Fuel Flow Rate (Maximum)</entry>
            <entry>2.5</entry>
            <entry>kg/min</entry>
          </row>
          <row>
            <entry>Tank Temperature (Operating)</entry>
            <entry>-40 to +65</entry>
            <entry>°C</entry>
          </row>
        </tbody>
      </tgroup>
    </table>
  </levelledPara>
  
  <levelledPara>
    <title>Structural Limits</title>
    <table>
      <tgroup cols="3">
        <thead>
          <row>
            <entry>Component</entry>
            <entry>Load Limit</entry>
            <entry>Unit</entry>
          </row>
        </thead>
        <tbody>
          <row>
            <entry>Wing Box (Ultimate)</entry>
            <entry>+3.75 / -1.5</entry>
            <entry>g</entry>
          </row>
          <row>
            <entry>Control Surface (Maximum)</entry>
            <entry>±25</entry>
            <entry>degrees</entry>
          </row>
          <row>
            <entry>Landing Gear (Maximum)</entry>
            <entry>65,000</entry>
            <entry>kg</entry>
          </row>
        </tbody>
      </tgroup>
    </table>
  </levelledPara>
</cirContent>
```

## CIR Integration in Data Modules

### Referencing CIR Content
Data modules reference CIR content using internal references:

```xml
<!-- In a descriptive module -->
<para>
  The 
  <internalRef internalRefId="CIR-BWQ1-00001" internalRefTargetType="irtt05">
    <internalRefText>wing box</internalRefText>
  </internalRef>
  primary structure consists of...
</para>

<!-- Referencing safety procedures -->
<preliminaryRqmts>
  <reqSafety>
    <internalRef internalRefId="CIR-BWQ1-00003" internalRefTargetType="irtt09">
      <internalRefText>Hydrogen Safety Protocol</internalRefText>
    </internalRef>
  </reqSafety>
</preliminaryRqmts>
```

### Cross-Reference Types
| Type | Code | Usage |
|------|------|-------|
| Definition | irtt05 | Terminology references |
| Procedure | irtt09 | Safety and procedural references |
| Table | irtt06 | Configuration data tables |
| External Publication | irtt07 | Regulatory references |

## CIR Maintenance

### Update Process
1. **Identify Changes**: Determine which CIR content needs updates
2. **Impact Analysis**: Identify affected data modules
3. **Update CIR**: Modify appropriate CIR module
4. **Validate References**: Ensure all internal references still resolve
5. **Update Data Modules**: Modify affected modules if necessary
6. **Regenerate Indices**: Update cross-reference indices

### Version Control
```xml
<cirIdent>
  <commonInfoDesignator>
    <commonInfoDesignatorIdent>CIR-BWQ1-00001</commonInfoDesignatorIdent>
  </commonInfoDesignator>
  <language languageIsoCode="en" countryIsoCode="US"/>
  <issueInfo issueNumber="002" inWork="00"/>  <!-- Version increment -->
</cirIdent>

<cirStatus issueType="changed">
  <reasonForUpdate>
    <simplePara>Updated hydrogen safety requirements per EASA advisory.</simplePara>
  </reasonForUpdate>
</cirStatus>
```

## CIR Categories Best Practices

### Terminology Management
- **Consistent Definitions**: Ensure all technical terms have single, authoritative definitions
- **Acronym Expansion**: Always provide full expansion for acronyms on first use
- **Units and Measurements**: Standardize measurement units (metric preferred)
- **Brand Names**: Use consistent product and component naming

### Reference Management
- **Current Standards**: Ensure all regulatory references are current
- **Accessibility**: Verify external publication references are accessible
- **Citation Format**: Use consistent citation formatting
- **Update Tracking**: Maintain record of reference version updates

### Safety Content
- **Regulatory Compliance**: Align with applicable safety regulations
- **Hazard Classification**: Use consistent hazard warning levels
- **Personal Protective Equipment**: Standard PPE requirements
- **Emergency Procedures**: Standardized emergency response procedures

### Configuration Data
- **Engineering Authority**: Verify all data with engineering authority
- **Units Consistency**: Use consistent measurement units throughout
- **Tolerance Specifications**: Include appropriate tolerance ranges
- **Effectivity**: Mark configuration-specific data appropriately

## GenCMS Integration

### CIR in Content Generation
GenCMS automatically incorporates CIR content during generation:

```javascript
// CIR integration in GenCMS
1. Load applicable CIR modules based on subsystem and IC
2. Extract relevant terminology and procedures
3. Include CIR references in generation prompt
4. Generate content with proper CIR cross-references
5. Validate generated references against CIR content
```

### Terminology Consistency
GenCMS ensures generated content uses CIR-defined terminology:
- Automatic terminology substitution
- Consistency checking against CIR definitions
- Warning for undefined terms not in CIR
- Suggestion of appropriate CIR references

## Checklist

### CIR Development
- [ ] All technical terms defined in terminology CIR
- [ ] Current regulatory references included in references CIR
- [ ] Standard safety procedures documented in procedures CIR
- [ ] Configuration data verified with engineering authority
- [ ] Cross-reference integrity maintained across all CIR modules

### CIR Usage in Data Modules
- [ ] Appropriate CIR references included for technical terms
- [ ] Safety procedures referenced where applicable
- [ ] Configuration data referenced rather than duplicated
- [ ] External publication references use CIR entries
- [ ] Internal reference types correctly specified

### CIR Maintenance
- [ ] Regular review schedule established for CIR content
- [ ] Change impact analysis performed before updates
- [ ] Version control properly maintained
- [ ] Cross-reference validation performed after changes
- [ ] GenCMS integration updated for CIR changes

## Common Mistakes

❌ **Inconsistent Terminology**: Using different terms for same concept across modules  
✅ **Correct**: Define terms once in CIR and reference consistently

❌ **Outdated References**: Using superseded regulatory or standard references  
✅ **Correct**: Regular review and update of all external publication references

❌ **Duplicate Safety Content**: Copying safety procedures into multiple modules  
✅ **Correct**: Define common safety procedures in CIR and reference them

❌ **Missing Cross-References**: Using CIR terminology without proper internal references  
✅ **Correct**: Always include appropriate internal references to CIR content

❌ **Configuration Data Duplication**: Repeating configuration data in multiple modules  
✅ **Correct**: Centralize configuration data in CIR and reference as needed

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0