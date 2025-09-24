# Procedural Modules (2xx/5xx/6xx/7xx)

Procedural modules contain step-by-step maintenance, removal, installation, and servicing procedures.

## Information Code Categories

### IC 2xx - General Procedures
- 200: General servicing procedures
- 240: Periodic maintenance tasks
- 260: Special operational procedures

### IC 5xx - Removal Procedures
- 500: General removal procedures
- 510: Component removal from aircraft
- 520: Subassembly disassembly

### IC 6xx - Servicing/Repair
- 600: General servicing procedures
- 610: Cleaning and inspection
- 620: Repair procedures
- 630: Adjustment procedures

### IC 7xx - Installation/Rigging
- 700: General installation procedures
- 710: Component installation to aircraft
- 720: Subassembly assembly
- 730: Rigging and adjustment

## R&I Pairing Convention

Removal and Installation procedures must be paired:
- IC 5xx ↔ IC 7xx (e.g., 500 removal pairs with 700 installation)
- Each removal procedure should reference its corresponding installation
- Installation procedures should reference removal prerequisites

```xml
<!-- In removal module (IC 500) -->
<dmRef>
  <dmRefIdent>
    <dmCode infoCode="700" infoCodeVariant="A"/>
  </dmRefIdent>
  <dmRefAddressItems>
    <dmTitle><infoName>Installation Procedure</infoName></dmTitle>
  </dmRefAddressItems>
</dmRef>

<!-- In installation module (IC 700) -->
<dmRef>
  <dmRefIdent>
    <dmCode infoCode="500" infoCodeVariant="A"/>
  </dmRefIdent>
  <dmRefAddressItems>
    <dmTitle><infoName>Removal Procedure</infoName></dmTitle>
  </dmRefAddressItems>
</dmRef>
```

## Safety Requirements

### Safety Preface
All procedural modules must include appropriate safety warnings:

```xml
<preliminaryRqmts>
  <reqSupportEquips>
    <supportEquipDescr>
      <name>Standard hand tools</name>
    </supportEquipDescr>
  </reqSupportEquips>
  <reqSafety>
    <noSafety>0</noSafety>
    <warningAndCautionPara>
      <warning>
        <warningAndCautionPara>
          <para>Ensure aircraft is properly secured and grounded before beginning work.</para>
        </warningAndCautionPara>
      </warning>
      <caution>
        <warningAndCautionPara>
          <para>Handle components with care to prevent damage to sealing surfaces.</para>
        </warningAndCautionPara>
      </caution>
    </warningAndCautionPara>
  </reqSafety>
</preliminaryRqmts>
```

### H₂ Safety Considerations
For hydrogen fuel system procedures, include specific warnings:

```xml
<warning>
  <warningAndCautionPara>
    <para>HYDROGEN HAZARD: Ensure hydrogen systems are properly vented and purged before maintenance. Follow lock-out/tag-out procedures for hydrogen supply valves.</para>
  </warningAndCautionPara>
</warning>
```

## Tooling and Equipment

### Required Support Equipment
```xml
<reqSupportEquips>
  <supportEquipDescr>
    <name>Torque wrench (0-50 Nm)</name>
    <shortName>TW-50</shortName>
  </supportEquipDescr>
  <supportEquipDescr>
    <name>Hydrogen-compatible sealant</name>
    <shortName>SEAL-H2</shortName>
  </supportEquipDescr>
</reqSupportEquips>
```

### Consumables and Expendables
```xml
<reqSpares>
  <sparesDescr>
    <name>O-ring, fuel interface</name>
    <partNumber>BWQ1-57-2001-001</partNumber>
    <qty>2</qty>
  </sparesDescr>
</reqSpares>
```

## Procedure Structure

### Main Procedure Content
```xml
<mainProcedure>
  <preliminEfectry>
    <effectivity>
      <configuration>
        <configString>BWB-Q100 All configurations</configString>
      </configuration>
    </effectivity>
  </preliminEfectry>
  
  <procedure>
    <step1>
      <para>Position aircraft in maintenance hangar.</para>
      <step2>
        <para>Ensure aircraft is properly chocked and grounded.</para>
      </step2>
      <step2>
        <para>Disconnect ground power if connected.</para>
      </step2>
    </step1>
    
    <step1>
      <para>Access wing box service panel:</para>
      <step2>
        <para>Remove access panel fasteners (8 places).</para>
        <figure>
          <graphic infoEntityIdent="ICN-BWQ1-A-571010-A-001-01"/>
        </figure>
      </step2>
      <step2>
        <para>Carefully remove access panel.</para>
        <caution>
          <warningAndCautionPara>
            <para>Support panel weight to prevent damage to hinges.</para>
          </warningAndCautionPara>
        </caution>
      </step2>
    </step1>
  </procedure>
</mainProcedure>
```

## Torque Specifications

### Torque Tables
```xml
<step2>
  <para>Tighten fasteners to specified torque:</para>
  <table>
    <tgroup cols="3">
      <colspec colname="item"/>
      <colspec colname="size"/>
      <colspec colname="torque"/>
      <thead>
        <row>
          <entry>Item</entry>
          <entry>Size</entry>
          <entry>Torque (Nm)</entry>
        </row>
      </thead>
      <tbody>
        <row>
          <entry>Access panel bolts</entry>
          <entry>M6</entry>
          <entry>8-10</entry>
        </row>
        <row>
          <entry>Interface bolts</entry>
          <entry>M8</entry>
          <entry>15-18</entry>
        </row>
      </tbody>
    </tgroup>
  </table>
</step2>
```

## Acceptance Criteria

### Functional Tests
Include acceptance criteria for completed procedures:

```xml
<closeRqmts>
  <reqConditions>
    <noConditions>0</noConditions>
    <conditionDescr>
      <condition>
        <conditionIdent>COND-001</conditionIdent>
        <conditionType>functional</conditionType>
        <conditionTypeValue>test</conditionTypeValue>
        <conditionDescr>
          <para>Verify system pressure within limits (XX-YY psi).</para>
        </conditionDescr>
      </condition>
    </conditionDescr>
  </reqConditions>
</closeRqmts>
```

### System Checks
```xml
<condition>
  <conditionIdent>COND-002</conditionIdent>
  <conditionType>inspection</conditionType>
  <conditionDescr>
    <para>Inspect all connections for proper engagement and absence of leaks.</para>
  </conditionDescr>
</condition>
```

## Effectivity Management

```xml
<effectivity>
  <configuration>
    <configString>BWB-Q100 Serial Numbers 001-050</configString>
  </configuration>
  <configuration>
    <configString>Modification 57-MOD-001 incorporated</configString>
  </configuration>
</effectivity>
```

## Checklist

### Procedure Planning
- [ ] Identify required tools and equipment
- [ ] Review safety requirements and H₂ hazards
- [ ] Verify R&I pairing for removal/installation procedures
- [ ] Check effectivity and configuration requirements
- [ ] Review related descriptive modules for component details

### Content Creation
- [ ] Include comprehensive safety preface
- [ ] Structure procedure with logical step hierarchy
- [ ] Add appropriate warnings and cautions in-line
- [ ] Include torque specifications and acceptance criteria
- [ ] Reference multimedia objects for complex steps
- [ ] Specify required consumables and spares

### Quality Assurance
- [ ] Procedure technically accurate and complete
- [ ] Safety warnings appropriate for hydrogen systems
- [ ] Cross-references to paired procedures included
- [ ] Acceptance criteria clearly defined
- [ ] Effectivity properly specified

## Common Mistakes

❌ **Missing Safety Warnings**: Inadequate H₂ safety considerations  
✅ **Correct**: Include comprehensive hydrogen-specific warnings and lock-out procedures

❌ **Unpaired R&I**: Removal procedure without corresponding installation  
✅ **Correct**: Always create paired removal/installation procedures with cross-references

❌ **Vague Steps**: "Remove component carefully"  
✅ **Correct**: "Remove component using lifting fixture to prevent damage to sealing surfaces (see Figure X)"

❌ **Missing Acceptance**: No verification of completed work  
✅ **Correct**: Include functional tests and inspection criteria

❌ **Wrong Information Code**: Using IC 040 for step-by-step procedures  
✅ **Correct**: Use appropriate procedural IC (5xx/6xx/7xx) based on task type

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0