# ATA-57-20 — Control Surfaces (BWB-Q100)

**Control surfaces structure:** elevons, flaperons, spoilers, tabs, their attachment mechanisms, hinges, and structural provisions for actuation.  
**Golden rule:** knowledge lives here (ATA); compute lives in **CAX/QOX**; deployable packages live in **PAx**.

---

## Quick Nav

- [Scope & Applicability](#scope--applicability)
- [Pattern Compliance](#pattern-compliance)
- [Directory Breakdown](#directory-breakdown)
- [S1000D Data Modules (DMRL-driven)](#s1000d-data-modules-dmrl-driven)
- [BREX Validation Rules](#brex-validation-rules)
- [Seed Data Modules](#seed-data-modules)
- [CI Hooks](#ci-hooks)
- [Interfaces & Dependencies](#interfaces--dependencies)
- [Mandatory Forms (ATA-20)](#mandatory-forms-ata20--links)
- [Configuration Breakdown — CBS → CI → CO](#configuration-breakdown--cbs--ci--co)
- [360IPCirq (R/I → IPC Reusability Bridge)](#360ipcirq-ri--ipc-reusability-bridge)
- [Acceptance & Inspection](#acceptance--inspection)
- [Evidence & QS](#evidence--qs)
- [Validation & CI](#validation--ci)
- [Change Control](#change-control)

---

## Scope & Applicability

**Includes**
- Control surface structures: elevons, flaperons, spoilers, tabs
- Hinge mechanisms and fittings
- Actuator attachment provisions and load paths
- Control surface balance systems (mass, aerodynamic)
- Structural lightning protection provisions for control surfaces
- Surface finish and aerodynamic smoothness requirements
- Structural repairs baseline rules (link to chapter-specific repair DMs under S1000D)

**Excludes**
- Flight control functionality and signaling (ATA-27)
- Hydraulic/electric actuation systems (ATA-29/24)
- Control surface aerodynamic design (referenced via CAx/ICDs)

---

## Pattern Compliance

- **ATA pattern:** `ATA-57/57-20_<Subject>/` *(4-digit subchapter)*, with **S1000D folders placed below the 4-digit node**.  
- **Do not store** heavy CAx/QOx data here—reference via [`io/routing.manifest.yaml`](#ioroutingmanifestyaml) and S1000D cross-refs.
- **DMC pattern:** normalize to full 2-digit fields → `…-subSystemCode(20)-subSubSystemCode(xx)-assyCode(yy)-disassyCode(zz)-Variant(A)-infoCode(iii)-Variant(A)…`

---

## Directory Breakdown

> Canonical layout with S1000D content organized under the 4-digit subchapter.

```
57-20_Control_Surfaces/
├── [README.md](#readme)
├── S1000D/
│   ├── BREX/
│   │   ├── [BREX.xml](#s1000dbrexbrexxml)                           # Business Rules Exchange - S1000D validation rules
│   │   └── [README.md](#s1000dbrexreadmemd)
│   ├── DMRL/
│   │   ├── [DMRL.xml](#s1000dmrldmrlxml)                           # Data Module Requirements List
│   │   └── [README.md](#s1000dmrlreadmemd)
│   ├── data_modules/
│   │   ├── descriptive/
│   │   │   ├── [57-20-10_Elevons/](#s1000ddata_modulesdescriptive57-20-10_elevons)
│   │   │   ├── [57-20-20_Flaperons/](#s1000ddata_modulesdescriptive57-20-20_flaperons)
│   │   │   ├── [57-20-30_Spoilers/](#s1000ddata_modulesdescriptive57-20-30_spoilers)
│   │   │   ├── [57-20-40_Tabs/](#s1000ddata_modulesdescriptive57-20-40_tabs)
│   │   │   └── [README.md](#s1000ddata_modulesdescriptivereadmemd)
│   │   ├── procedural/
│   │   │   ├── inspection/
│   │   │   │   ├── [57-20-10_Elevons/](#s1000ddata_modulesproceduralinspection57-20-10_elevons)
│   │   │   │   ├── [57-20-20_Flaperons/](#s1000ddata_modulesproceduralinspection57-20-20_flaperons)
│   │   │   │   ├── [57-20-30_Spoilers/](#s1000ddata_modulesproceduralinspection57-20-30_spoilers)
│   │   │   │   └── [57-20-40_Tabs/](#s1000ddata_modulesproceduralinspection57-20-40_tabs)
│   │   │   ├── removal_installation/
│   │   │   │   ├── [57-20-10_Elevons/](#s1000ddata_modulesproceduralremoval_installation57-20-10_elevons)
│   │   │   │   ├── [57-20-20_Flaperons/](#s1000ddata_modulesproceduralremoval_installation57-20-20_flaperons)
│   │   │   │   ├── [57-20-30_Spoilers/](#s1000ddata_modulesproceduralremoval_installation57-20-30_spoilers)
│   │   │   │   └── [57-20-40_Tabs/](#s1000ddata_modulesproceduralremoval_installation57-20-40_tabs)
│   │   │   ├── repair/
│   │   │   │   ├── [57-20-10_Elevons/](#s1000ddata_modulesproceduralrepair57-20-10_elevons)
│   │   │   │   ├── [57-20-20_Flaperons/](#s1000ddata_modulesproceduralrepair57-20-20_flaperons)
│   │   │   │   ├── [57-20-30_Spoilers/](#s1000ddata_modulesproceduralrepair57-20-30_spoilers)
│   │   │   │   └── [57-20-40_Tabs/](#s1000ddata_modulesproceduralrepair57-20-40_tabs)
│   │   │   └── [README.md](#s1000ddata_modulesproceduralreadmemd)
│   │   └── [README.md](#s1000ddata_modulesreadmemd)
│   └── [README.md](#s1000dreadmemd)
├── compliance/
│   ├── [flutter_index.md](#complianceflutter_indexmd)
│   ├── [loads_index.md](#complianceloads_indexmd)
│   ├── [balance_index.md](#compliancebalance_indexmd)
│   └── [README.md](#compliancereadmemd)
├── contracts/
│   ├── schemas/
│   │   ├── [README.md](#contractsschemasreadmemd)
│   │   ├── [hinge.schema.json](#contractsschemashingeschemajson)
│   │   ├── [control_surface.schema.json](#contractsschemascontrol_surfaceschemajson)
│   │   ├── [actuator_attachment.schema.json](#contractsschemasactuator_attachmentschemajson)
│   │   ├── [balance_weight.schema.json](#contractsschemasbalance_weightschemajson)
│   │   ├── [acceptance.metric.schema.json](#contractsschemasacceptancemetricschemajson)
│   │   ├── [laminate.stack.schema.json](#contractsschemaslaminatestackschemajson)
│   │   ├── [joint.schema.json](#contractsschemasjointschemajson)
│   │   └── [fastener.set.schema.json](#contractsschemasfastenersetschemajson)
│   ├── [ICD-AAA-ATA-57-20.md](#contractsicd-aaa-ata-57-20md)
│   └── [README.md](#contractsreadmemd)
├── evidence/
│   ├── [hinge_tests_index.md](#evidencehinge_tests_indexmd)
│   ├── [fatigue_tests_index.md](#evidencefatigue_tests_indexmd)
│   ├── [surface_finish_index.md](#evidencesurface_finish_indexmd)
│   └── [README.md](#evidencereadmemd)
├── icd/
│   ├── [ICD-57-20-27_Flight_Control_System.md](#icdicd-57-20-27_flight_control_systemmd)
│   ├── [ICD-57-20-29_Hydraulic_System.md](#icdicd-57-20-29_hydraulic_systemmd)
│   ├── [ICD-57-20-57-10_Wing_Structure.md](#icdicd-57-20-57-10_wing_structuremd)
│   ├── [ICD-57-20-57-30_High_Lift.md](#icdicd-57-20-57-30_high_liftmd)
│   └── [README.md](#icdreadmemd)
├── io/
│   └── [routing.manifest.yaml](#ioroutingmanifestyaml)
└── [README.md](#readme)
```

---

## S1000D Data Modules (DMRL-driven)

The following is a representative, non-exhaustive list of S1000D Data Modules (DMs) managed within this ATA chapter. The definitive list is controlled by [`S1000D/DMRL/DMRL.xml`](#s1000dmrldmrlxml). Each DM is validated against the **BREX** rules.

**Information Codes Used:**
- **040A:** Descriptive Information
- **520A:** Procedural - Inspection/Repair Procedure
- **720A:** Procedural - Removal/Installation Procedure
- **941A:** Illustrated Parts Data (IPD)

### System Level (57-20-00)

| DMC | Information Code | Title |
|-----|------------------|-------|
| `DMC-BWQ1-A-57-20-00-00-00A-040A-D-EN-US` | 040A | Control Surfaces - System Description and Principles |
| `DMC-BWQ1-A-57-20-00-01-00A-520A-D-EN-US` | 520A | Control Surface Balance - General Adjustment and Inspection |
| `DMC-BWQ1-A-57-20-00-02-00A-520A-D-EN-US` | 520A | Control Surface Hinges - Common Inspection and Lubrication |
| `DMC-BWQ1-A-57-20-00-03-00A-520A-D-EN-US` | 520A | Control Surface Surface Finish - Inspection and Acceptance |
| `DMC-BWQ1-A-57-20-00-00-00A-941A-D-EN-US` | 941A | Control Surfaces - Common Hardware and Tools (Fasteners, Bearings) |

### 57-20-10: Elevons

| DMC | Information Code | Title |
|-----|------------------|-------|
| `DMC-BWQ1-A-57-20-10-00-00A-040A-D-EN-US` | 040A | Elevons - Description and Operation |
| `DMC-BWQ1-A-57-20-10-01-00A-520A-D-EN-US` | 520A | Elevon - General Inspection Procedure |
| `DMC-BWQ1-A-57-20-10-02-00A-520A-D-EN-US` | 520A | Elevon Structure - Detailed Repair (Skin, Core, Spar) |
| `DMC-BWQ1-A-57-20-10-03-00A-520A-D-EN-US` | 520A | Elevon Hinge and Fitting - Detailed Repair |
| `DMC-BWQ1-A-57-20-10-00-00A-720A-D-EN-US` | 720A | Elevon - Removal and Installation |
| `DMC-BWQ1-A-57-20-10-00-00A-941A-D-EN-US` | 941A | Elevon - Illustrated Parts Data |

### 57-20-20: Flaperons

| DMC | Information Code | Title |
|-----|------------------|-------|
| `DMC-BWQ1-A-57-20-20-00-00A-040A-D-EN-US` | 040A | Flaperons - Description and Operation |
| `DMC-BWQ1-A-57-20-20-01-00A-520A-D-EN-US` | 520A | Flaperon - General Inspection Procedure |
| `DMC-BWQ1-A-57-20-20-02-00A-520A-D-EN-US` | 520A | Flaperon Structure - Detailed Repair |
| `DMC-BWQ1-A-57-20-20-03-00A-520A-D-EN-US` | 520A | Flaperon Actuator Attachment - Inspection and Repair |
| `DMC-BWQ1-A-57-20-20-00-00A-720A-D-EN-US` | 720A | Flaperon - Removal and Installation |
| `DMC-BWQ1-A-57-20-20-00-00A-941A-D-EN-US` | 941A | Flaperon - Illustrated Parts Data |

### 57-20-30: Spoilers

| DMC | Information Code | Title |
|-----|------------------|-------|
| `DMC-BWQ1-A-57-20-30-00-00A-040A-D-EN-US` | 040A | Spoilers - Description and Operation |
| `DMC-BWQ1-A-57-20-30-01-00A-520A-D-EN-US` | 520A | Spoiler - General Inspection Procedure |
| `DMC-BWQ1-A-57-20-30-02-00A-520A-D-EN-US` | 520A | Spoiler Structure - Detailed Repair |
| `DMC-BWQ1-A-57-20-30-03-00A-520A-D-EN-US` | 520A | Spoiler Hinge and Fitting - Inspection and Repair |
| `DMC-BWQ1-A-57-20-30-00-00A-720A-D-EN-US` | 720A | Spoiler - Removal and Installation |
| `DMC-BWQ1-A-57-20-30-00-00A-941A-D-EN-US` | 941A | Spoiler - Illustrated Parts Data |

### 57-20-40: Tabs (Trim/Balance)

| DMC | Information Code | Title |
|-----|------------------|-------|
| `DMC-BWQ1-A-57-20-40-00-00A-040A-D-EN-US` | 040A | Tabs (Trim/Balance) - Description and Operation |
| `DMC-BWQ1-A-57-20-40-01-00A-520A-D-EN-US` | 520A | Tab - General Inspection Procedure |
| `DMC-BWQ1-A-57-20-40-02-00A-520A-D-EN-US` | 520A | Tab Structure - Detailed Repair |
| `DMC-BWQ1-A-57-20-40-03-00A-520A-D-EN-US` | 520A | Balance Weight Installation and Adjustment |
| `DMC-BWQ1-A-57-20-40-00-00A-720A-D-EN-US` | 720A | Tab - Removal and Installation |
| `DMC-BWQ1-A-57-20-40-00-00A-941A-D-EN-US` | 941A | Tab - Illustrated Parts Data |

> **Estimated total:** ~30 DMs listed above, with additional detailed procedural DMs for specific repair scenarios bringing the total to the estimated 45–50. All DMs are version-controlled within the PDM system.

---

## BREX Validation Rules

The following BREX rules are specific to ATA-57-20 and extend/compose with the 57-10 BREX:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <title>BREX — ATA-57-20 Control Surfaces</title>
  <ns prefix="xlink" uri="http://www.w3.org/1999/xlink"/>

  <!-- Fixed-width fields -->
  <pattern id="dmcode-widths">
    <rule context="//dmCode">
      <assert test="string-length(@systemCode)=2 and string-length(@subSystemCode)=2 and string-length(@subSubSystemCode)=2">System/SubSystem/SubSubSystem must be 2 digits.</assert>
      <assert test="string-length(@assyCode)=2 and string-length(@disassyCode)=2">Assy/Disassy must be 2 digits.</assert>
    </rule>
  </pattern>

  <!-- Allowed info codes in 57-20 -->
  <pattern id="allowed-info-codes-5720">
    <rule context="//dmCode[@systemCode='57' and @subSystemCode='20']">
      <assert test="@infoCode=('040','520','720','941')">Info code must be 040, 520, 720, or 941.</assert>
    </rule>
  </pattern>

  <!-- Forms must be externalPubRef; dmRef reserved for DMs -->
  <pattern id="forms-as-externalpub">
    <rule context="dmodule[.//dmCode/@infoCode=('520','720')]">
      <assert test="count(.//refs/externalPubRef[contains(@xlink:href,'FORM-QA-20')]) &gt; 0">Procedural DMs must link required ATA-20 form(s) via externalPubRef.</assert>
      <assert test="count(.//refs/dmRef[contains(@xlink:href,'FORM-QA-20')]) = 0">Do not use dmRef for forms; use externalPubRef.</assert>
    </rule>
  </pattern>

  <!-- 360IPCirq: 720A must reference at least one 941A DM and use csn/itemRef -->
  <pattern id="ri-ipd-bridge">
    <rule context="dmodule[dmAddress/dmIdent/dmCode/@infoCode='720']">
      <assert test="count(.//preliminaryRqmts/refs/dmRef[contains(@xlink:href,'-941')]) &gt;= 1">720A must reference at least one 941A DM.</assert>
      <assert test="count(.//preliminaryRqmts/reqSpares/reqSpare[@csn and @itemRef]) &gt; 0">720A must list reqSpares with csn + itemRef that exist in 941A.</assert>
    </rule>
  </pattern>

  <!-- Titles and issue info -->
  <pattern id="titles-issueinfo">
    <rule context="//dmTitle">
      <assert test="techName and normalize-space(techName)!=''">techName required.</assert>
      <assert test="infoName and normalize-space(infoName)!=''">infoName required.</assert>
    </rule>
    <rule context="//dmIdent">
      <assert test="issueInfo/issueNumber and matches(issueInfo/issueNumber,'\d{3}')">issueNumber must be 3 digits.</assert>
      <assert test="issueInfo/inWork and matches(issueInfo/inWork,'\d{2}')">inWork must be 2 digits.</assert>
    </rule>
  </pattern>

  <!-- Safety requirements for procedures -->
  <pattern id="proc-safety">
    <rule context="dmodule[dmAddress/dmIdent/dmCode/@infoCode=('520','720')]">
      <assert test="count(.//preliminaryRqmts/safetyRqmts/*) &gt; 0">Procedural DMs must include safety requirements.</assert>
    </rule>
  </pattern>

  <!-- Hinge/balance procedural guardrails -->
  <pattern id="hinge-balance-forms">
    <rule context="dmodule[.//dmTitle/techName=('Elevon','Flaperon','Spoiler','Tab')]">
      <assert test="not(contains(lower-case(string(.)),'hinge')) or count(.//externalPubRef[contains(@xlink:href,'20-70')]) &gt;= 1">Hinge tasks must reference Hinge Installation &amp; Adjustment form.</assert>
      <assert test="not(contains(lower-case(string(.)),'balance')) or count(.//externalPubRef[contains(@xlink:href,'20-60')]) &gt;= 1">Balance tasks must reference Balance Weight form.</assert>
    </rule>
  </pattern>
</schema>
```

---

## Seed Data Modules

The following are minimal, valid seed DMs for each information code that compile under a Schematron BREX:

### 040A — Elevons / Description

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:xlink="http://www.w3.org/1999/xlink">
  <dmAddress>
    <dmIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A"
              systemCode="57" subSystemCode="20" subSubSystemCode="10"
              assyCode="00" disassyCode="00" disassyCodeVariant="A"
              infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
      <language countryIsoCode="US" languageIsoCode="en"/>
      <issueInfo issueNumber="001" inWork="00"/>
    </dmIdent>
    <dmAddressItems>
      <dmTitle><techName>Elevons</techName><infoName>Description and Operation</infoName></dmTitle>
      <dmCreated>2025-09-24</dmCreated>
      <security securityClassification="01-unclassified"/>
    </dmAddressItems>
  </dmAddress>

  <content>
    <description>
      <para>Elevons provide combined pitch and roll control on the BWB-Q100. Structure includes skins, ribs, spars, hinges, actuator fittings and mass-balance provisions.</para>
      <para>Lightning protection features and bonding paths are integrated with the hinge fittings and trailing-edge seal interfaces.</para>
      <figure>
        <title>Elevon Overview</title>
        <graphic infoEntityIdent="GR-57-20-10-OVW"/>
      </figure>
      <para>For attachment to the primary wing structure, see <dmRef>
        <dmRefIdent><dmCode modelIdentCode="BWQ1" systemDiffCode="A" systemCode="57" subSystemCode="10" subSubSystemCode="60" assyCode="04" disassyCode="00" disassyCodeVariant="A" infoCode="040" infoCodeVariant="A" itemLocationCode="D"/></dmRefIdent>
        <dmRefAddress><dmTitle><techName>Control Surface Hinge Fittings</techName><infoName>Moment Transfer, Bushing Details</infoName></dmTitle></dmRefAddress>
      </dmRef>.</para>
    </description>
  </content>
</dmodule>
```

### 520A — Common hinge inspection/lube

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:xlink="http://www.w3.org/1999/xlink">
  <dmAddress>
    <dmIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A"
              systemCode="57" subSystemCode="20" subSubSystemCode="00"
              assyCode="02" disassyCode="00" disassyCodeVariant="A"
              infoCode="520" infoCodeVariant="A" itemLocationCode="D"/>
      <language countryIsoCode="US" languageIsoCode="en"/>
      <issueInfo issueNumber="001" inWork="00"/>
    </dmIdent>
    <dmAddressItems>
      <dmTitle><techName>Control Surface Hinges</techName><infoName>Common Inspection and Lubrication</infoName></dmTitle>
      <dmCreated>2025-09-24</dmCreated>
      <security securityClassification="01-unclassified"/>
    </dmAddressItems>
  </dmAddress>

  <content>
    <procedure>
      <preliminaryRqmts>
        <safetyRqmts>
          <warning><para>Install safety locks to prevent control surface movement.</para></warning>
        </safetyRqmts>
        <reqSupportEquips>
          <reqSupportEquip><name>Torque wrench (5 Nm range, class A)</name></reqSupportEquip>
          <reqSupportEquip><name>Dial indicator (0.01 mm)</name></reqSupportEquip>
        </reqSupportEquips>
        <reqConsumables>
          <reqConsumable><name>Approved lubricant per spec LUB-57-A</name></reqConsumable>
          <reqConsumable><name>Solvent cleaner (aerospace grade)</name></reqConsumable>
        </reqConsumables>

        <!-- Link to ATA-20 forms as external publications -->
        <refs>
          <externalPubRef xlink:href="../../20/20-70_Mechanical_Linkages/forms/FORM-QA-20-70-01_Hinge_Installation_Adjustment.md"/>
          <externalPubRef xlink:href="../../20/20-50_Surface_Finish/forms/FORM-QA-20-50-01_Surface_Finish_Aerodynamic_Smoothness.md"/>
        </refs>
      </preliminaryRqmts>

      <mainProcedure>
        <proceduralStep>
          <title>Free-play and friction check</title>
          <para>Measure free play at hinge axes; allowable ≤ 0.1 mm. Record torque to start motion; allowable ≤ 0.5 Nm unless otherwise specified.</para>
        </proceduralStep>
        <proceduralStep>
          <title>Lubrication</title>
          <para>Apply LUB-57-A to bearings per manufacturer spec. Wipe excess and verify no contamination remains.</para>
        </proceduralStep>
      </mainProcedure>

      <concludingRqmts>
        <closeRqmts>
          <inspection><para>Record results against acceptance metric CO-3.13 in CSDB evidence registry.</para></inspection>
        </closeRqmts>
      </concludingRqmts>
    </procedure>
  </content>
</dmodule>
```

### 720A — Elevon R/I (with 360IPCirq bridge)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:xlink="http://www.w3.org/1999/xlink">
  <dmAddress>
    <dmIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A"
              systemCode="57" subSystemCode="20" subSubSystemCode="10"
              assyCode="00" disassyCode="00" disassyCodeVariant="A"
              infoCode="720" infoCodeVariant="A" itemLocationCode="D"/>
      <language countryIsoCode="US" languageIsoCode="en"/>
      <issueInfo issueNumber="001" inWork="00"/>
    </dmIdent>
    <dmAddressItems>
      <dmTitle><techName>Elevon</techName><infoName>Removal and Installation</infoName></dmTitle>
      <dmCreated>2025-09-24</dmCreated>
      <security securityClassification="01-unclassified"/>
    </dmAddressItems>
  </dmAddress>

  <content>
    <procedure>
      <preliminaryRqmts>
        <safetyRqmts>
          <warning><para>Support the control surface to prevent hinge damage.</para></warning>
        </safetyRqmts>

        <!-- 360IPCirq: CSN/itemRef keys match 941A -->
        <reqSpares>
          <reqSpare csn="ELV-ASSY-00" itemRef="ELV-ASSY-00-ITEM-001"/>
          <reqSpare csn="ELV-HINGE-KIT-01" itemRef="KIT-HINGE-57-20-10-01"/>
          <reqSpare csn="ELV-BAL-KIT-01" itemRef="KIT-BAL-57-20-10-01"/>
        </reqSpares>

        <refs>
          <dmRef xlink:href="DMC-BWQ1-A-57-20-10-00-00A-941A-D-EN-US.xml"/>
          <externalPubRef xlink:href="../../20/20-60_Balance_and_Alignment/forms/FORM-QA-20-60-01_Balance_Weight_Installation.md"/>
          <externalPubRef xlink:href="../../20/20-70_Mechanical_Linkages/forms/FORM-QA-20-70-01_Hinge_Installation_Adjustment.md"/>
        </refs>
      </preliminaryRqmts>

      <mainProcedure>
        <proceduralStep id="ri-01"><title>Preparation</title>
          <para>Install gust locks. Remove actuator pins per ATA-27 task reference.</para>
        </proceduralStep>
        <proceduralStep id="ri-02"><title>Removal</title>
          <para>Remove hinge bolts following reverse torque sequence; tag hardware.</para>
        </proceduralStep>
        <proceduralStep id="ri-03"><title>Installation</title>
          <para>Align hinge bores; install bolts and torque per CO-3.20. Apply locking method per FORM-QA-20-70-01.</para>
        </proceduralStep>
        <proceduralStep id="ri-04"><title>Balance Check</title>
          <para>Verify static balance; adjust with KIT-BAL-57-20-10-01. Record on FORM-QA-20-60-01.</para>
        </proceduralStep>
      </mainProcedure>

      <concludingRqmts>
        <closeRqmts>
          <inspection><para>Perform free-play/friction checks and sign-off acceptance metric CO-3.13.</para></inspection>
        </closeRqmts>
      </concludingRqmts>
    </procedure>
  </content>
</dmodule>
```

### 941A — Elevon IPD (keys shared with 720A)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dmAddress>
    <dmIdent>
      <dmCode modelIdentCode="BWQ1" systemDiffCode="A"
              systemCode="57" subSystemCode="20" subSubSystemCode="10"
              assyCode="00" disassyCode="00" disassyCodeVariant="A"
              infoCode="941" infoCodeVariant="A" itemLocationCode="D"/>
      <language countryIsoCode="US" languageIsoCode="en"/>
      <issueInfo issueNumber="001" inWork="00"/>
    </dmIdent>
    <dmAddressItems>
      <dmTitle><techName>Elevon</techName><infoName>Illustrated Parts Data</infoName></dmTitle>
      <dmCreated>2025-09-24</dmCreated>
      <security securityClassification="01-unclassified"/>
    </dmAddressItems>
  </dmAddress>

  <content>
    <ipd>
      <catalogIntro><para>Assemblies, kits and hardware for 57-20-10 Elevons.</para></catalogIntro>

      <catalogSeqNumber csn="ELV-ASSY-00">
        <figure figureNumber="ELV-ASSY-00-FIG">
          <title>Elevon Assembly</title>
          <graphic infoEntityIdent="GR-57-20-10-IPD-OVW"/>
          <item itemRef="ELV-ASSY-00-ITEM-001">
            <descr>Elevon Assembly LH</descr>
            <partRef manufacturerCode="BWQ" partNumberValue="BWQ57-20-10-001"/>
            <qtyPerAssy value="1"/>
          </item>
          <item itemRef="ELV-ASSY-00-ITEM-002">
            <descr>Elevon Assembly RH</descr>
            <partRef manufacturerCode="BWQ" partNumberValue="BWQ57-20-10-002"/>
            <qtyPerAssy value="1"/>
          </item>
        </figure>
      </catalogSeqNumber>

      <catalogSeqNumber csn="ELV-HINGE-KIT-01">
        <figure figureNumber="ELV-HINGE-KIT-01-FIG">
          <title>Hinge Service Kit</title>
          <graphic infoEntityIdent="GR-57-20-10-HINGE-KIT"/>
          <item itemRef="KIT-HINGE-57-20-10-01">
            <descr>Hinge Kit, Elevon</descr>
            <partRef manufacturerCode="FAS" partNumberValue="FAS-K57-20-10-A"/>
            <qtyPerAssy value="1"/>
          </item>
        </figure>
      </catalogSeqNumber>

      <catalogSeqNumber csn="ELV-BAL-KIT-01">
        <figure figureNumber="ELV-BAL-KIT-01-FIG">
          <title>Balance Weight Kit</title>
          <graphic infoEntityIdent="GR-57-20-10-BAL-KIT"/>
          <item itemRef="KIT-BAL-57-20-10-01">
            <descr>Balance Weight Kit</descr>
            <partRef manufacturerCode="BAL" partNumberValue="BAL-K57-20-10-A"/>
            <qtyPerAssy value="1"/>
          </item>
        </figure>
      </catalogSeqNumber>
    </ipd>
  </content>
</dmodule>
```

---

## CI Hooks

The following CI hooks are recommended for validating the ATA-57-20 documentation:

### Folder hygiene check

```bash
# ci/check-tree.sh
set -e
dup=$(grep -Ril "README.md" S1000D/data_modules | sort | uniq -d || true)
if [ -n "$dup" ]; then echo "Duplicate/looped entries in data_modules tree"; echo "$dup"; exit 1; fi
```

### Schematron validation

```bash
# ci/validate.sh
xsltproc schematron/iso_svrl_for_xslt2.xsl S1000D/BREX/BREX.xml > brex.xsl
for dm in $(git ls-files "S1000D/data_modules/**/*.xml"); do
  xsltproc brex.xsl "$dm" | grep -q "<failed-assert" && { echo "BREX fail: $dm"; exit 2; } || true
done
```

### GitHub Actions

```yaml
name: s1000d-57-20
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: sudo apt-get update && sudo apt-get install -y xsltproc
      - run: bash ci/check-tree.sh
      - run: bash ci/validate.sh
```

---

## 360IPCirq (R/I → IPC Reusability Bridge)

- **Intent:** Every **720A** R/I DM enumerates removal kits, torque sequences, sealants, and fittings **with the same item keys** used by **941A** IPD figures/items to enable **"removal for repair → IPC 360 reusability"**.  
- **Where:** See [`S1000D/data_modules/procedural/removal_installation/`](#s1000ddata_modulesproceduralremoval_installation) and corresponding IPD directories.  
- **Contracts:** The mapping keys and effectivity rules are defined in [`contracts/ICD-AAA-ATA-57-20.md`](#contractsicd-aaa-ata-57-20md) and the JSON schemas under [`contracts/schemas/`](#contractsschemas).

---

## Interfaces & Dependencies

- **ATA-57-10 Wing Primary Structure:** attachment points, load transfer, tolerances.  
- **ATA-27 Flight Controls:** control surface kinematics, actuation requirements.  
- **ATA-29 Hydraulic Systems:** hydraulic actuation interfaces, pressure requirements.  
- **ATA-57-30 High-Lift Devices:** integration with flaps and slats.  
- **ATA-20 Standard Practices:** fastening, bonding, sealing, material handling, EMI/bonding.  
- **ATA-04 (IPD):** figures/items for spares; see 360IPCirq linkage for interchangeability/reusability.

---

## Mandatory Forms (ATA-20)

Use canonical forms—**do not duplicate** inside ATA-57-20. Link from DMs and acceptance records using **externalPubRef**:

- Composite Fastening — `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`
- Adhesive Bonding — `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`
- Surface Finish & Aerodynamic Smoothness — `../../20/20-50_Surface_Finish/forms/FORM-QA-20-50-01_Surface_Finish_Aerodynamic_Smoothness.md`
- Balance Weight Installation — `../../20/20-60_Balance_and_Alignment/FORM-QA-20-60-01_Balance_Weight_Installation.md`
- Hinge Installation & Adjustment — `../../20/20-70_Mechanical_Linkages/FORM-QA-20-70-01_Hinge_Installation_Adjustment.md`

---

## Configuration Breakdown — CBS → CI → CO

### L0 — Capability (System)
**CI-0.0** `57-20_Control_Surfaces` — Control surfaces structure for BWB-Q100 wing.

### L1 — Major Configuration Groups
**CI-1.1 Control Surface Structures** (elevons, flaperons, spoilers, tabs)
**CI-1.2 Hinge Mechanisms** (fittings, bearings, attachments)
**CI-1.3 Actuator Attachments** (fittings, load paths, provisions)
**CI-1.4 Balance Systems** (mass balance, aerodynamic balance)
**CI-1.5 Surface Finish & Aerodynamics** (smoothness, sealing)
**CI-1.6 Loads & Flutter** (design envelope, flutter characteristics)
**CI-1.7 Repairs** (standard structural repairs catalog)
**CI-1.8 Effectivity & Options** (block/variant rules)
**CI-1.9 Evidence & QA** (hinge tests, fatigue tests, surface finish)
**CI-1.10 Schemas & Interfaces** (contracts, manifests, ICDs)

### L2 — Subsystems & Containers

#### CI-1.1 Control Surface Structures
- **CI-2.1** Elevons — structure, skins, ribs, internal structure.
- **CI-2.2** Flaperons — structure, skins, ribs, internal structure.
- **CI-2.3** Spoilers — structure, skins, ribs, internal structure.
- **CI-2.4** Tabs — structure, attachment mechanisms.

#### CI-1.2 Hinge Mechanisms
- **CI-2.5** Hinge Fittings — lugs, bearings, attachment points.
- **CI-2.6** Hinge Bearings — types, materials, lubrication requirements.
- **CI-2.7** Hinge Attachments — to wing structure, load paths.

#### CI-1.3 Actuator Attachments
- **CI-2.8** Actuator Fittings — attachment points, load paths.
- **CI-2.9** Actuator Provisions — mounting interfaces, clearances.
- **CI-2.10** Load Path Reinforcements — local structure reinforcement.

#### CI-1.4 Balance Systems
- **CI-2.11** Mass Balance Weights — types, locations, attachment methods.
- **CI-2.12** Aerodynamic Balance Features — horn balance, set-back hinge.
- **CI-2.13** Balance Adjustment Mechanisms — adjustable weights, trim tabs.

#### CI-1.5 Surface Finish & Aerodynamics
- **CI-2.14** Surface Finish Requirements — smoothness, tolerances.
- **CI-2.15** Sealing Provisions — gap sealing, edge sealing.
- **CI-2.16** Aerodynamic Features — vortex generators, seals.

#### CI-1.6 Loads & Flutter
- **CI-2.17** Load Cases — limit/ultimate, fatigue spectra, gust/maneuver.
- **CI-2.18** Flutter Characteristics — natural frequencies, damping.
- **CI-2.19** Control Surface Hinge Moments — actuation requirements.

#### CI-1.7 Repairs
- **CI-2.20** Standard Repairs — scarf/patch/core replacement, insert repairs.
- **CI-2.21** Acceptance Limits — post-repair metrics (UT/thermography/margins).

#### CI-1.8 Effectivity & Options
- **CI-2.22** Effectivity Sets — MSN ranges, blocks.
- **CI-2.23** Options — variant flags (e.g., high-speed option, balance option).

#### CI-1.9 Evidence & QA
- **CI-2.24** Hinge Tests — wear, load capacity, friction measurements.
- **CI-2.25** Fatigue Tests — control surface fatigue test results.
- **CI-2.26** Surface Finish Measurements — profile measurements, visual inspection.
- **CI-2.27** QA Forms Linkage — ATA-20 mandatory forms.

#### CI-1.10 Schemas & Interfaces
- **CI-2.28** JSON Schemas — hinge, control surface, actuator attachment, balance weight, acceptance metric.
- **CI-2.29** ICDs — with ATA-27 / 29 / 57-10 / 57-30 / 57-50.
- **CI-2.30** Routing Manifest — inputs/outputs linkage, UTCS/QS anchors.

### L3 — Leaf Configurable Objects (CO)

> Atomic definition points for design/manufacturing/inspection; version-pinned & sealed.

1. **Control Surface Panel (CO-3.1)** → `surface_id`, `type(elevon/flaperon/spoileron)`, `geometry_ref`, `laminate_code`, `thickness_map`, `material_spec`, `effectivity_expr`
2. **Hinge Fitting (CO-3.2)** → `hinge_id`, `type(over/under/special)`, `material_spec`, `bearing_type`, `load_capacity`, `attachment_method`
3. **Hinge Bearing (CO-3.3)** → `bearing_id`, `type(ball/roller/sleeve)`, `material_spec`, `lubrication_req`, `service_interval`
4. **Actuator Attachment Fitting (CO-3.4)** → `fitting_id`, `actuator_type`, `load_capacity`, `attachment_method`, `material_spec`
5. **Mass Balance Weight (CO-3.5)** → `weight_id`, `mass_kg`, `location_ref`, `attachment_method`, `adjustment_range`
6. **Aerodynamic Balance Feature (CO-3.6)** → `balance_id`, `type(horn/setback)`, `geometry_ref`, `effectiveness_factor`
7. **Surface Finish Requirement (CO-3.7)** → `finish_id`, `area_ref`, `smoothness_class`, `measurement_method`, `acceptance_criteria`
8. **Sealing Provision (CO-3.8)** → `seal_id`, `type(gap/edge)`, `material_spec`, `application_method`, `service_requirements`
9. **Load Case (CO-3.9)** → `case_id`, `description`, `limit/ultimate`, `flight_condition`, `control_surface_deflection`
10. **Flutter Characteristic (CO-3.10)** → `flutter_id`, `mode_shape`, `frequency_hz`, `damping_ratio`, `margin`
11. **Hinge Moment (CO-3.11)** → `moment_id`, `flight_condition`, `deflection_deg`, `moment_Nm`, `actuation_power_req`
12. **Standard Repair (CO-3.12)** → `repair_id`, `type(scarf/patch/core/insert)`, `ply_schedule`, `adhesive_ref`, `acceptance_ref`, `effectivity_expr`
13. **Acceptance Metric (CO-3.13)** → `metric_id`, `feature(friction/finish/alignment)`, `threshold`, `method`, `evidence_ref`
14. **Effectivity Rule (CO-3.14)** → `expr`, `start`, `end`, `options[]`, `exclusions[]`
15. **Option Flag (CO-3.15)** → `option_code`, `name`, `dependencies[]`, `exclusions[]`
16. **Tool Ref (CO-3.16)** → `tool_code`, `description`, `alt_tool[]`, `calibration_due`
17. **Material Ref (CO-3.17)** → `mat_code`, `spec`, `batch_required{Y/N}`, `shelf_life`, `storage_class`
18. **Lubrication Parameter (CO-3.18)** → `lubricant_code`, `application_method`, `interval_hours`, `quantity`
19. **Balance Adjustment (CO-3.19)** → `adjustment_id`, `method`, `tool_required`, `measurement_required`, `tolerance`
20. **Hinge Installation Parameter (CO-3.20)** → `hinge_code`, `torque_Nm`, `alignment_tolerance`, `clearance_spec`
21. **Evidence File Ref (CO-3.21)** → `type(hinge_test/fatigue/finish)`, `uri`, `sha256`, `form_link`
22. **QA Form Link (CO-3.22)** → `form_id`, `rev`, `path`, `required_in_steps[]`
23. **QS/UTCS Anchor (CO-3.23)** → `canonical_hash`, `sbom_uri`, `signer`, `timestamp`

> **Schemas** for COs are pinned in [`contracts/schemas/*.schema.json`](#contractsschemas) and referenced from [`io/routing.manifest.yaml`](#ioroutingmanifestyaml).

---

## Acceptance & Inspection

| Feature / Metric                   | Minimum Requirement (unless drawing/spec overrides) | Method                          |
| ---                                | ---                                                 | ---                             |
| Hinge friction                     | ≤ 0.5 Nm (typical)                                | Torque measurement, test rig    |
| Hinge free play                    | ≤ 0.1 mm                                           | Dial indicator, feeler gauge    |
| Control surface alignment          | ±0.5 mm (typical)                                  | Laser alignment, tooling        |
| Surface smoothness                 | Ra ≤ 1.6 µm (Class B)                             | Profilometer, visual inspection |
| Gap uniformity                     | ±0.2 mm (typical)                                  | Gap gauges, visual inspection   |
| Balance weight accuracy            | ±5 g (typical)                                     | Weighing scale, balance rig     |
| Actuator attachment preload        | Per design specification                           | Load cell, torque wrench        |
| Post-repair NDT                    | No critical indications; per CO-3.13 acceptance    | UT/RT/thermography              |

> When generic limits conflict with model/drawing, the **model/drawing governs**.

---

## Evidence & QS

- **Forms (linked):**  
  - Composite Fastening → `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`
  - Adhesive Bonding → `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`
  - Surface Finish & Aerodynamic Smoothness → `../../20/20-50_Surface_Finish/forms/...`
  - Balance Weight Installation → `../../20/20-60_Balance_and_Alignment/FORM-QA-20-60-01_Balance_Weight_Installation.md`
  - Hinge Installation & Adjustment → `../../20/20-70_Mechanical_Linkages/FORM-QA-20-70-01_Hinge_Installation_Adjustment.md`

- **Traceability:** material lots, OOC timers, torque values, sealant batches, NDT results, test coupons → indexed under [`evidence/`](#evidence) and cross-referenced from DMs.  
- **QS seal:** applied only when *all* applicable ATA-20 practices and acceptance metrics (per [`contracts/schemas/acceptance.metric.schema.json`](#contractsschemasacceptancemetricschemajson)) are fully evidenced and referenced.

---

## Validation & CI

- **S1000D validation:** BREX rules ([`S1000D/BREX/BREX.xml`](#s1000dbrexbrexxml)) applied on each DM; DMRL conformance required.  
- **Schema validation:** JSON instances referenced by DMs must pass:
  - [`contracts/schemas/laminate.stack.schema.json`](#contractsschemaslaminatestackschemajson)
  - [`contracts/schemas/joint.schema.json`](#contractsschemasjointschemajson)
  - [`contracts/schemas/fastener.set.schema.json`](#contractsschemasfastenersetschemajson)
  - [`contracts/schemas/attachment.fitting.schema.json`](#contractsschemasactuator_attachmentschemajson)
  - [`contracts/schemas/acceptance.metric.schema.json`](#contractsschemasacceptancemetricschemajson)
- **Routing manifest:** [`io/routing.manifest.yaml`](#ioroutingmanifestyaml) records CAx/QOx/PAX inputs/outputs and UTCS/QS anchors. CI fails closed if any reference is missing or unverifiable.

---

## Change Control

Any deviation from ATA-20 or drawing/spec requires **M&P** and **MRB** approval and is recorded here. Releases follow **PDM-PLM** change notices; manifests and signatures are updated under [`io/`](#io) and [`evidence/`](#evidence).

---

*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
