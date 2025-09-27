---
id: SPM-20-10-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-20/20-10_Structural_Practices/SPM-20-10-0001_CompositeFastening.md
llc: SYSTEMS
title: "SPM-20-10-0001: Standard Practice Manual — Composite Fastening & Bonding"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "M&P Engineering Team"
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

# SPM-20-10-0001: Standard Practice Manual — Composite Fastening & Bonding

## 1) Purpose & Scope

This Standard Practice Manual (SPM) defines the procedures for mechanical fastening and adhesive bonding of composite structures in the BWB-Q100 airframe, including:

- Hole preparation and drilling procedures
- Fastener installation and torque specifications
- Adhesive bonding processes and controls
- Quality assurance and inspection requirements
- Repair procedures for fastening systems

## 2) Materials & Equipment

### 2.1 Approved Fasteners
- Titanium fasteners: Ti-6Al-4V per AMS-4967
- Steel fasteners: A286 per AMS-5737
- Fastener coatings: Electroless nickel per AMS-C-26074

### 2.2 Adhesives
- Structural adhesives: EA-9394 per HMS-20-83
- Sealant adhesives: PR-1440 per MIL-S-81733
- Surface primers: BR-127 per MIL-P-23377

### 2.3 Equipment
- Drill motors: Variable speed, 0-3000 RPM
- Torque wrenches: Digital, ±2% accuracy
- Depth gauges: 0.001" resolution
- Bond test equipment: Ultrasonic C-scan

## 3) Procedures

### 3.1 Hole Preparation
1. **Pilot hole:** Drill 1/8" pilot hole at marked location
2. **Step drilling:** Progressively increase to final diameter
3. **Reaming:** Final ream to +0.000/-0.002" tolerance
4. **Deburring:** Remove all burrs and edge radii
5. **Cleaning:** Solvent wipe with IPA, water-break test

### 3.2 Fastener Installation
1. **Dry fit:** Verify fastener fit and engagement
2. **Sealant application:** Apply wet sealant if specified
3. **Installation:** Install fastener with specified torque
4. **Inspection:** Verify head flushness and seal integrity

### 3.3 Adhesive Bonding
1. **Surface preparation:** Grit blast or chemical etch
2. **Primer application:** Apply and cure per specification
3. **Adhesive mixing:** Mix ratio per manufacturer data
4. **Bond assembly:** Apply adhesive, assemble, cure
5. **Quality control:** NDT inspection per acceptance criteria

## 4) Quality Control

### 4.1 Inspection Requirements
- Visual inspection: 100% of all fasteners
- Torque verification: 10% sample or per specification
- NDT inspection: Per drawing requirements
- Bond testing: Ultrasonic C-scan for critical joints

### 4.2 Acceptance Criteria
- Hole quality: No damage, proper diameter and finish
- Head flushness: 0.000 to +0.010" above surface
- Torque values: Within ±10% of specification
- Bond integrity: No voids >1 mm², total void area <0.5%

## 5) Documentation & Evidence

Required forms and documentation:
- `FORM-QA-20-10-01`: Composite Fastening Record
- `FORM-QA-20-10-02`: Adhesive Bonding Record
- Material certifications and lot traceability
- NDT inspection reports and C-scan images
- Torque wrench calibration records

## 6) Safety & Environmental

### 6.1 Personal Protective Equipment
- Safety glasses with side shields
- Hearing protection during drilling operations
- Nitrile gloves for adhesive handling
- Respirator for solvent and adhesive work

### 6.2 Environmental Controls
- Temperature: 68-78°F (20-25°C)
- Relative humidity: ≤45%
- Ventilation: Local exhaust for solvents and adhesives
- Contamination control: Clean room practices for critical bonds

## 7) Routing & Data Flow

This SPM integrates with:
- **CAD systems:** Fastener specifications and hole locations
- **Manufacturing:** Work instructions and torque specifications  
- **QA systems:** Inspection records and acceptance criteria
- **Materials:** Adhesive specifications and handling requirements

Evidence flows to PDM-PLM for configuration control and QS sealing.

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*