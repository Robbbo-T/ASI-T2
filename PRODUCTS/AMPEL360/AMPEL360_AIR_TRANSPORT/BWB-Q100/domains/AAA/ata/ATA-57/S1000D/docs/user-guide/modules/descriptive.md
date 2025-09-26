# Descriptive Modules (040/042/034/050–056)

Descriptive modules provide technical descriptions, system overviews, and component specifications.

## Information Code Usage

### IC 040 - General Description
- System overviews and functional descriptions
- High-level architecture and configuration
- Interface descriptions between systems

### IC 042 - Description/Operation
- Detailed operational descriptions
- Control logic and system behavior
- Performance characteristics

### IC 034 - Technical Data
- Physical component specifications
- Material properties and dimensions
- Engineering data and tolerances

### IC 050–056 - Specific Descriptions
- Specialized descriptive content
- Component-specific technical data
- Interface specifications

## Required Metadata

```xml
<dmIdent>
  <dmCode modelIdentCode="BWQ1" systemDiffCode="A" 
          systemCode="57" subSystemCode="10" subSubSystemCode="00" 
          assyCode="00" disassyCode="00" disassyCodeVariant="A" 
          infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
  <language languageIsoCode="en" countryIsoCode="US"/>
  <issueInfo issueNumber="001" inWork="01"/>
</dmIdent>
```

## Content Structure

### Typical Descriptive Module Structure
```xml
<content>
  <description>
    <para>System overview paragraph...</para>
    <levelledPara>
      <title>Configuration</title>
      <para>Configuration details...</para>
    </levelledPara>
    <levelledPara>
      <title>Components</title>
      <para>Component descriptions...</para>
      <randomList>
        <listItem><para>Component A - function and location</para></listItem>
        <listItem><para>Component B - function and location</para></listItem>
      </randomList>
    </levelledPara>
  </description>
</content>
```

## Cross-References

### Referencing CIR Content
```xml
<internalRef internalRefId="CIR-BWQ1-00001" internalRefTargetType="irtt05">
  <para>As defined in the terminology CIR</para>
</internalRef>
```

### Referencing Other Data Modules
```xml
<dmRef>
  <dmRefIdent>
    <dmCode modelIdentCode="BWQ1" systemDiffCode="A" 
            systemCode="57" subSystemCode="10" subSubSystemCode="10" 
            assyCode="00" disassyCode="00" disassyCodeVariant="A" 
            infoCode="500" infoCodeVariant="A" itemLocationCode="D"/>
  </dmRefIdent>
  <dmRefAddressItems>
    <dmTitle><techName>BWB-Q100</techName><infoName>Wing Box Removal</infoName></dmTitle>
  </dmRefAddressItems>
</dmRef>
```

## BREX Integration

Descriptive modules must comply with BWQ1 BREX rules:
- Classification string must use en-dash: `INTERNAL–EVIDENCE-REQUIRED`
- Enterprise name must be consistent: `AMPEL360`
- Responsible partner company must be specified
- Security classification must be appropriate for content sensitivity

## Multimedia Integration

### Referencing Graphics
```xml
<graphic infoEntityIdent="ICN-BWQ1-A-571000-A-001-01">
  <symbol infoEntityIdent="ICN-BWQ1-A-571000-A-001-01"/>
</graphic>
```

### Multimedia Objects
- Place multimedia files in `multimedia/graphics/` for technical diagrams
- Use descriptive file names: `wing-box-assembly-overview.svg`
- Ensure high resolution for technical accuracy

## Quality Standards

### Content Requirements
- Technical accuracy verified against engineering data
- Consistent terminology per CIR definitions
- Clear, concise language appropriate for maintenance personnel
- Proper use of S1000D markup elements

### Common Elements
- Use `<para>` for standard paragraphs
- Use `<levelledPara>` for hierarchical content
- Use `<randomList>` for unordered lists
- Use `<sequentialList>` for ordered procedures

## Checklist

### Before Writing
- [ ] Verify information code (040/042/034/050–056) matches content type
- [ ] Check DMRL for required content scope
- [ ] Review related modules for cross-reference opportunities
- [ ] Identify multimedia objects needed

### Content Creation
- [ ] Include system overview in opening paragraph
- [ ] Structure content with appropriate levelled paragraphs
- [ ] Use consistent terminology from CIR
- [ ] Include proper cross-references to related modules
- [ ] Add multimedia references where appropriate

### Review and Validation
- [ ] Schema validation passes
- [ ] BREX compliance verified
- [ ] Technical accuracy confirmed
- [ ] Cross-references resolve correctly
- [ ] Multimedia objects exist and are properly referenced

## Common Mistakes

❌ **Wrong Information Code**: Using IC 500 (removal) for descriptive content  
✅ **Correct**: Use IC 040 for general descriptions, IC 034 for technical data

❌ **Inconsistent Terminology**: Using different terms for the same component  
✅ **Correct**: Reference CIR terminology and use consistently

❌ **Missing Cross-References**: Not linking to related procedures or specifications  
✅ **Correct**: Include appropriate `<dmRef>` elements to related modules

❌ **Poor Structure**: Long paragraphs without logical organization  
✅ **Correct**: Use `<levelledPara>` to create clear hierarchical structure

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0