---
id: PS-20-20-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-20/20-20_Sealing_and_Pressurization/PS-20-20-0001_AblativeSealantApplication.md
llc: SYSTEMS
title: "PS-20-20-0001: Process Spec — Ablative/Barrier Sealant Application"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "Environmental Systems Team"
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

# PS-20-20-0001: Process Spec — Ablative/Barrier Sealant Application

## 1) Purpose & Scope

This Process Specification (PS) defines the procedures for application of ablative and barrier sealants in the BWB-Q100 airframe, specifically for:

- High-temperature interface sealing
- Plasma protection during atmospheric entry
- Cabin pressurization barrier systems
- Environmental protection for avionics bays
- Fuel tank sealing and vapor barriers

## 2) Materials & Specifications

### 2.1 Ablative Sealants
- Primary: RTV-560 silicone ablative per MIL-A-46146
- Secondary: DC-93-500 per AMS-S-3348
- Primer: A-1100 silane coupling agent

### 2.2 Barrier Sealants
- Fuel tank: PR-1422 polysulfide per MIL-S-8802
- Cabin: EA-934NA polysulfide per MIL-S-81733
- Avionics: RTV-41 silicone per MIL-A-46106

## 3) Application Procedures

### 3.1 Surface Preparation
1. **Cleaning:** Degrease with MEK, final wipe with IPA
2. **Abrasion:** Light abrasion with 320-grit aluminum oxide
3. **Primer application:** Apply thin, uniform coat
4. **Cure:** Air dry 30 minutes minimum before sealant

### 3.2 Sealant Application
1. **Mixing:** Hand mix or mechanical per manufacturer
2. **Application:** Continuous bead, no gaps or voids  
3. **Tooling:** Shape profile within 15 minutes
4. **Cure:** Environment per specification (temperature/humidity)

### 3.3 Quality Verification
1. **Profile check:** Verify sealant geometry and coverage
2. **Adhesion test:** Probe cure adhesion after 24 hours
3. **Leak test:** Pressure decay or tracer gas as applicable

## 4) Environmental Controls

- **Temperature:** 68-85°F (20-29°C) during application
- **Humidity:** 25-55% RH for optimal cure
- **Ventilation:** 10 air changes/hour minimum
- **Work time:** Complete tooling within pot life

## 5) Quality Control & Inspection

### 5.1 In-Process Checks
- Verify surface prep per water-break test
- Check sealant mixing ratio and work time
- Monitor environmental conditions continuously

### 5.2 Final Inspection  
- Visual: Coverage, profile, surface finish
- Dimensional: Height, width per drawing
- Adhesion: Pull test per specification
- Leak test: As required by application

## 6) Documentation Requirements

Required evidence:
- Material certifications and lot numbers
- Environmental condition logs
- Application photographs
- Inspection records and test results
- `FORM-QA-20-20-01`: Sealant Application Record

## 7) Routing & Integration

This process specification integrates with:
- **Design:** Sealant joint geometry and requirements
- **Manufacturing:** Work instructions and application sequence
- **QA:** Inspection criteria and acceptance limits
- **Environmental:** Test procedures for pressure and leak testing

Evidence flows through PDM-PLM for configuration control and QS approval.

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*