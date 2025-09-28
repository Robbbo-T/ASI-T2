---
id: ASIT-PLUS-BWQ1-AAA-ATA57-S1000D-DMRL-OV-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/docs/S1000D/README-DMRL.md
llc: SYSTEMS
title: "DMRL — ATA-57 Wings (BWB-Q100, S1000D Issue 6.0)"
configuration: conf_000_baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-01-21
maintainer: "ASI-T Architecture Team"
licenses:
  docs: "CC-BY-4.0"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
provenance:
  policy_hash: "sha256:TBD"
  model_sha: "sha256:TBD"
  data_manifest_hash: "sha256:TBD"
  operator_id: "UTCS:OP:copilot-gen"
---

# Data Module Requirements List (DMRL) — ATA-57 Wings

**S1000D master list:** [`DML-BWQ1-ATA57-00.xml`](./DML-BWQ1-ATA57-00.xml)  
**ATA-57 landing:** [`../README.md`](../README.md)  
**AAA domain:** [`../../../`](../../../)  

> **Link policy:** relative links only. Directories end with `/`; files include full names.

---

## 1) Overview

The **DMRL** defines the complete set of **S1000D data modules** required to document **ATA-57 — Wings** for the **BWB-Q100** program. It drives scope, planning, and QA completeness for the wing structure, fuel interfaces, control surfaces, high-lift, and equipment integration.

- Format: **S1000D Issue 6.0**  
- Model Ident Code (MIC): **`BWQ1`**  
- Governing file: [`DML-BWQ1-ATA57-00.xml`](./DML-BWQ1-ATA57-00.xml)  
- BREX (business rules): *(placeholder, to be added)* `BREX-BWQ1-AAA.xml`

---

## 2) Purpose

- **Requirements traceability:** single source of truth for required DMs
- **Planning & progress tracking:** plan effort and mark completion vs. DMRL
- **Validation:** prevents documentation gaps; supports **QS/UTCS** evidence
- **Compliance:** aligns to **S1000D Issue 6.0** structure and code rules

---

## 3) Coverage Summary

The DMRL specifies **~55 data modules** across subsystems:

### 57-10 Wing Structure *(~9 DMs)*
- General description & maintenance planning  
- Wing box primary structure; skins, stringers, spars, ribs  
- BWB wing/center-body blended integration  
- Equipment attachment fittings; transition fairings

### 57-20 Wing Fuel System Interfaces *(~11 DMs)*
- General description; **H₂ fuel safety**  
- Integral tank integration; line routing and management  
- Ventilation & inerting; H₂ tank structural interfaces

### 57-30 Wing Control Surfaces *(~10 DMs)*
- Control-surface overview  
- Ailerons (remove/install/IPD)  
- Spoilers/speedbrakes  
- Trailing-edge actuation; load-alleviation

### 57-40 High-Lift Systems *(~9 DMs)*
- System overview  
- Slats & flaps (R/I, IPD)  
- Actuation & drive; control & indication

### 57-50 Wing Equipment Integration *(~10 DMs)*
- Antennas & sensors  
- Nav/comm integration; wing lighting  
- Ice detect/protect; smart/quantum wing features

> Final counts are managed in the XML DMRL; this README summarizes the scope.

---

## 4) Information Codes (Issue 6.0)

| Code | Meaning                         |
|:----:|---------------------------------|
| 040  | General descriptions            |
| 034  | Technical data / breakdowns     |
| 011  | Safety summaries                |
| 018  | Warnings & cautions             |
| 100  | Scheduled maintenance           |
| 052  | Routing/location diagrams       |
| 310  | Visual inspections              |
| 345  | System/structural tests         |
| 350  | Functional checks               |
| 420  | Fault isolation                 |
| 500  | Removal procedures              |
| 600  | Servicing procedures            |
| 700  | Installation/rigging            |
| 900  | Illustrated parts data (IPD)    |
| 910  | Parts lists (PL)                |

> Use **040/034** for descriptions/breakdowns, **500/700** for R/I, **900/910** for IPD/PL, **420** for FI.

---

## 5) DMRL XML Skeleton

```xml
<dmrl xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="schemas/dmrl.xsd">
  <identAndStatusSection>
    <dmrlAddress>
      <dmrlIdent dmrlCode="DML-BWQ1-ATA57-00"/>
      <issueInfo issueNumber="001" inWork="00"/>
      <dmrlTitle>DMRL — ATA-57 Wings (BWB-Q100, conf_000_baseline)</dmrlTitle>
    </dmrlAddress>
  </identAndStatusSection>

  <content>
    <!-- Repeat one dmRequirement per required DM -->
    <dmRequirement>
      <dmRefIdent>
        <dmCode modelIdentCode="BWQ1" systemCode="57" subsystemCode="10"
                infoCode="040" infoCodeVariant="A" itemLocationCode="A"/>
        <language languageIsoCode="en" countryIsoCode="US"/>
      </dmRefIdent>
      <reqComment>57-10 General Description</reqComment>
    </dmRequirement>

    <!-- … ~55 total dmRequirement elements … -->
  </content>
</dmrl>
````

**Schema path (relative):** `./schemas/dmrl.xsd` *(add if not present)*

---

## 6) Data Module Code (DMC) Pattern

**Minimal** S1000D DMC fields used by this project:

* `modelIdentCode` = **BWQ1**
* `systemCode` = **57** (ATA chapter)
* `subsystemCode` / `subsubsystemCode` = **10/20/30/40/50** as needed
* `infoCode` / `infoCodeVariant` = from table above
* `itemLocationCode` = e.g., `A` (aircraft-level), refine as needed

**Example (flap removal):**

```
BWQ1-57-40-500-A
  MIC  SYS SUB  IC   ICV ILC
```

---

## 7) Filenames & Foldering

* **DMRL file**: `DML-BWQ1-ATA57-00.xml` *(this folder)*
* **Data module XMLs**: place under `./DM/` or per your S1000D build layout

  * Suggested: `./DM/57-xx/<DMC>.xml`
* **BREX**: `./BREX/BREX-BWQ1-AAA.xml`
* **Schema**: `./schemas/dmrl.xsd`

> Keep filenames consistent with the DMC inside the file to simplify QA automation.

---

## 8) Validation

**Prereqs:** add `dmrl.xsd` under `./schemas/`

```bash
# XML well-formedness
xmllint --noout ./DML-BWQ1-ATA57-00.xml

# Schema validation
xmllint --noout --schema ./schemas/dmrl.xsd ./DML-BWQ1-ATA57-00.xml
```

**Checks performed:**

* Issue 6.0 structure and required elements
* Valid **MIC** (`BWQ1`) and **systemCode** (`57`)
* DMC formatting and language blocks

---

## 9) Use in the Documentation Project

1. **Scope** — derive all required DMs from the DMRL.
2. **Plan** — assign owners/effort per DM; track status.
3. **Author** — create DM XMLs matching DMRL entries.
4. **QA** — validate XML + cross-check against DMRL (no gaps).
5. **Publish** — assemble IETP/IETM per S1000D workflow.

**Progress Checklist (sample):**

| Subsystem       | DM Count | Authored | QA Pass | Notes |
| --------------- | -------: | -------: | ------: | ----- |
| 57-10 Structure |        9 |        0 |       0 |       |
| 57-20 Fuel IF   |       11 |        0 |       0 |       |
| 57-30 Ctrl Surf |       10 |        0 |       0 |       |
| 57-40 High-Lift |        9 |        0 |       0 |       |
| 57-50 Equip Int |       10 |        0 |       0 |       |
| **Total**       |  **~55** |        0 |       0 |       |

> Maintain a living checklist next to the DMRL; each DM shall link back to this DMRL.

---

## 10) Integration (ASI-T2)

* **QS/UTCS:** log DMRL hash and each DM’s canonical hash for traceable publication chains.
* **CAx/QOx:** reference engineering sources (CAD/CAE/CFD/QUBO) inside applicable DMs.
* **SIM:** prefer modular, reusable content; track update energy/cost (optional).
* **MAL-EEM:** ensure safety/ethics content (warnings, cautions) is present and consistent.

---

## 11) Cross-References

* ATA-57 root → [`../README.md`](../README.md)
* AAA domain index → [`../../../`](../../../)
* Sibling ATA (examples):

  * ATA-27 Flight Controls → [`../../27/README.md`](../../27/README.md)
  * ATA-20 Standard Practices → [`../../20/README.md`](../../20/README.md)

---

## 12) Revision History

| Rev | Date       | Description                   | QS/UTCS Ref |
| --- | ---------- | ----------------------------- | ----------- |
| 0   | 2025-01-21 | Initial DMRL README (Issue 6) | `TBD`       |

---

*Classification: INTERNAL–EVIDENCE-REQUIRED • S1000D v6.0 • BWB-Q100 / ATA-57*

```

