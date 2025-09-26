---
id: ASIT-PLUS-AAA-MS-20-30-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/20/20-30_Material_Handling/MS-20-30-0001_TPS_TileHandling.md
llc: MATERIAL
title: "Material Specification: TPS Tile Handling & Inspection"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "Materials Engineering Team"
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

# Material Specification: TPS Tile Handling & Inspection

## 1. Purpose
This specification defines **mandatory requirements** for the handling, storage, inspection, installation, and maintenance of **Thermal Protection System (TPS) tiles** used on the **AMPEL360 PLUS** space tourism vehicle. It ensures tile integrity, proper installation, and operational safety for reentry thermal protection.

## 2. Scope
Applies to all TPS tile materials and systems including:
- **HRSI tiles** (High-temperature Reusable Surface Insulation)
- **LRSI tiles** (Low-temperature Reusable Surface Insulation)  
- **AFRSI blankets** (Advanced Flexible Reusable Surface Insulation)
- **RCC panels** (Reinforced Carbon-Carbon for leading edges)
- **Adhesive and attachment systems** for TPS installation
- **Gap fillers and seals** between TPS elements

**Exclusions:** TPS design requirements and certification basis (see ATA-57/ATA-53), structural attachment design (see ATA-51).

## 3. Normative References
- **ATA-20:** Standard Practices – Airframe (this chapter)
- **PS-20-20-0001:** *Ablative Sealant Application* (gap sealing)
- **ATA-57:** Wings (TPS integration on lifting surfaces)
- **ATA-53:** Fuselage (TPS integration on body)
- **NASA-STD-5020:** *Requirements for Thermal Protection System Materials*

## 4. Material Classifications & Properties

### 4.1. HRSI Tiles (High-Temperature Areas)
- **Material:** Silica fiber with borosilicate glass coating
- **Service temperature:** Up to 2300°F (1260°C)
- **Density:** 9-22 lb/ft³ depending on application
- **Applications:** Wing leading edge, nose cone, high-heating areas during reentry

### 4.2. LRSI Tiles (Moderate-Temperature Areas)
- **Material:** Silica fiber with aluminoborosilicate coating
- **Service temperature:** Up to 1200°F (650°C)
- **Density:** 9-15 lb/ft³
- **Applications:** Fuselage sides, upper surfaces, moderate heating zones

### 4.3. AFRSI Blankets (Low-Temperature Areas)
- **Material:** Silica fiber batting with outer fabric
- **Service temperature:** Up to 700°F (370°C)
- **Weight:** 0.5-1.5 lb/ft²
- **Applications:** Cargo bay, internal surfaces, low-heating areas

### 4.4. RCC Panels (Extreme High-Temperature)
- **Material:** Carbon-carbon composite with silicon carbide coating
- **Service temperature:** Up to 3000°F (1650°C)
- **Applications:** Wing leading edges, nose cap, highest heating areas

## 5. Handling Requirements

### 5.1. General Handling Precautions
- **Personnel training:** Only certified technicians handle TPS materials
- **Clean environment:** Class 100,000 cleanroom or equivalent for critical operations
- **Protective equipment:** Lint-free gloves, coveralls, safety glasses mandatory
- **Lifting restrictions:** No lifting by edges, use proper lifting fixtures only

### 5.2. Tile-Specific Handling
1. **HRSI/LRSI tiles:**
   - Support entire tile during handling, never by corners or edges
   - Use padded lifting fixtures designed for specific tile geometry
   - Maximum handling force: 5 lbs distributed load
   - Avoid impact or shock loading >2G acceleration

2. **AFRSI blankets:**
   - Roll for transport, do not fold or crease
   - Store flat when not in use, avoid compression
   - Handle with clean, dry gloves to prevent contamination

3. **RCC panels:**
   - Use specialized lifting equipment due to weight and brittleness
   - Inspect for coating damage after each handling operation
   - Store in protective containers with cushioned supports

### 5.3. Transportation
- **Packaging:** Custom foam-lined containers for each tile configuration
- **Environment:** Temperature controlled 65-75°F, humidity <50% RH
- **Shock protection:** Maximum 1G shock during transport
- **Documentation:** Chain of custody log for all tile movements

## 6. Storage Requirements

### 6.1. Environmental Controls
- **Temperature:** 70±10°F (21±6°C) with <5°F/hour change rate
- **Humidity:** 45±10% RH with continuous monitoring
- **Cleanliness:** Positive pressure, HEPA filtration, <Class 100,000
- **Contamination control:** No hydrocarbons, silicones, or organic solvents in storage area

### 6.2. Storage Configuration
- **Tile racks:** Padded supports every 6 inches, no point loading
- **Blanket storage:** Flat storage on clean surfaces, rolls if necessary
- **RCC storage:** Individual protective containers with desiccant
- **Inventory tracking:** RFID tags and database tracking for each item

### 6.3. Shelf Life Management
- **HRSI/LRSI tiles:** Indefinite if stored properly, inspect annually
- **AFRSI blankets:** 10-year shelf life from manufacture date
- **RCC panels:** Indefinite, inspect coating integrity every 2 years
- **Adhesives:** 6-month shelf life refrigerated, 30 days at room temperature

## 7. Inspection Procedures

### 7.1. Incoming Inspection
1. **Visual examination:**
   - Surface coating integrity (no cracks, chips, or delamination)
   - Dimensional verification within drawing tolerances
   - Edge condition (no cracking or spalling)
   - Cleanliness (no contamination, foreign materials)

2. **Documentation review:**
   - Material certification and test data
   - Manufacturing traveler and quality records
   - Storage and handling history since manufacture

### 7.2. In-Service Inspection
1. **Pre-installation inspection:**
   - Repeat incoming inspection criteria
   - Verify tile identification and configuration match
   - Check adhesive shelf life and storage conditions

2. **Post-flight inspection:**
   - Photographic documentation of all TPS surfaces
   - Close visual inspection for damage, erosion, or degradation
   - Dimensional checks on critical tiles using templates
   - Coating thickness measurement (RCC panels)

### 7.3. Repair/Replacement Criteria
- **HRSI/LRSI tiles:**
  - Cracks >0.25" in any direction: replace
  - Coating loss >10% of surface area: replace
  - Edge damage >0.125" deep: repair or replace per engineering disposition

- **AFRSI blankets:**
  - Tears or holes >1" diameter: replace
  - Contamination not removable by approved cleaning: replace
  - Compression set >25% of original thickness: replace

- **RCC panels:**
  - Any crack in substrate: replace immediately
  - Coating loss >5% of area: evaluate for repair or replacement
  - Impact damage visible to naked eye: engineering evaluation required

## 8. Installation Requirements

### 8.1. Surface Preparation
- **Substrate cleanliness:** Solvent clean per SPM-20-10-0001
- **Surface roughness:** 125-250 μin RMS for optimal adhesive bond
- **Primer application:** Apply per adhesive manufacturer specifications
- **Cure verification:** Verify primer cure before tile installation

### 8.2. Adhesive Application
- **Room temperature vulcanizing (RTV):** For removable installations
- **Structural adhesives:** For permanent installations per PS-20-20-0001
- **Gap management:** 0.030"-0.060" nominal gap between tiles
- **Sealant application:** Apply gap sealant per PS-20-20-0001 procedures

### 8.3. Installation Verification
- **Bond strength:** Verification per manufacturer test procedures
- **Gap uniformity:** Laser measurement of gap dimensions
- **Surface smoothness:** Step height <0.050" between adjacent tiles
- **Installation documentation:** Photographic record and dimensional report

## 9. Quality Control & Acceptance

### 9.1. Acceptance Criteria
- **Visual standards:** No cracks, chips, contamination, or installation damage
- **Dimensional tolerance:** All critical dimensions within drawing limits
- **Bond integrity:** No disbonds detectable by tap test or thermography
- **Surface finish:** Coating intact with no exposed substrate

### 9.2. Rejection Criteria
- **Structural damage:** Any cracks, delamination, or substrate exposure
- **Contamination:** Any foreign material not removable by approved cleaning
- **Out-of-tolerance:** Dimensions outside drawing specifications
- **Installation defects:** Poor adhesive bonds, excessive gaps, misalignment

### 9.3. Non-Conformance Disposition
- **Minor defects:** Local repair if approved by engineering
- **Major defects:** Tile replacement and investigation of root cause
- **Installation errors:** Remove and reinstall with new adhesive/sealant
- **Documentation:** NCR in UTCS/QS system with corrective action

## 10. Safety & Environmental Requirements

### 10.1. Personnel Safety
- **Respiratory protection:** N95 minimum for fiber exposure, P100 for RCC
- **Skin protection:** Nitrile gloves and coveralls, no direct skin contact
- **Eye protection:** Safety glasses with side shields minimum
- **Medical surveillance:** Annual pulmonary function testing for exposed personnel

### 10.2. Environmental Protection
- **Waste disposal:** All TPS waste as hazardous material per local regulations
- **Air filtration:** HEPA filtration of all work area exhaust
- **Contamination control:** Prevent release of fibers to environment
- **Spill response:** Immediate cleanup and containment procedures

## 11. Documentation & Traceability

### 11.1. Required Records
- **Material pedigree:** Manufacturing source, lot numbers, test data
- **Handling log:** All handling operations with date, time, personnel
- **Storage history:** Environmental conditions, duration, any anomalies
- **Installation record:** Location, orientation, adhesive lot, installation date
- **Inspection results:** All inspection data with accept/reject disposition

### 11.2. QS Integration
- **Digital records:** All data in UTCS/QS system with blockchain verification
- **Configuration management:** Link to vehicle configuration and change control
- **Trend analysis:** Statistical process control on inspection and performance data
- **Audit trail:** Complete traceability from raw material to end-of-life disposal

## 12. Training & Certification

### 12.1. Personnel Requirements
- **Basic certification:** 40-hour TPS handling course with written and practical exam
- **Advanced certification:** Additional 20 hours for RCC and critical operations
- **Recertification:** Annual recertification with competency demonstration
- **Record keeping:** Training records in personnel qualification database

### 12.2. Facility Certification
- **Environmental qualification:** Verify cleanroom and storage capabilities
- **Equipment calibration:** All handling and inspection equipment current
- **Procedure compliance:** Audit conformance to this specification annually
- **Continuous improvement:** Feedback system for procedure updates

This material specification ensures the integrity and proper handling of TPS materials critical to passenger safety during AMPEL360 PLUS space tourism missions.