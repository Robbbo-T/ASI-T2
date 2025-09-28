---
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/20/20-40_Electrical_Bonding/SPM-20-40-0001_PlasmaShieldingBonding.md
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: TBD
classification: INTERNAL–EVIDENCE-REQUIRED
configuration: baseline
ethics_guard: MAL-EEM
id: SPM-20-40-0001
licenses:
  docs: CC-BY-4.0
llc: SYSTEMS
maintainer: Electrical Systems Team
project: PRODUCTS/AMPEL360/BWB-Q100
provenance:
  data_manifest_hash: sha256:TBD
  model_sha: sha256:TBD
  operator_id: UTCS:OP:copilot-gen
  policy_hash: sha256:TBD
release_date: 2025-09-24
title: 'SPM-20-40-0001: Standard Practice Manual — Plasma/EMI Shielding & Structural
  Bonding'
utcs_mi: v5.0
version: 0.1.0
---

# SPM-20-40-0001: Standard Practice Manual — Plasma/EMI Shielding & Structural Bonding

## 1) Purpose & Scope

This Standard Practice Manual (SPM) defines the procedures for electrical bonding, electromagnetic interference (EMI) shielding, and plasma protection systems for the BWB-Q100 airframe, including:

- Structural grounding and bonding networks
- EMI/RFI shielding installation and termination
- Lightning protection and static discharge systems
- Plasma protection during atmospheric entry
- Electrical continuity verification and testing

## 2) Materials & Components

### 2.1 Bonding Materials
- Bonding straps: Copper braid per MIL-B-5087
- Conductive gaskets: Fluorosilicone with silver fill
- Conductive sealants: EC-2216 per MIL-A-46146
- Grounding hardware: Stainless steel per MS20470

### 2.2 Shielding Materials
- EMI mesh: Woven copper per MIL-STD-1377
- Conductive coatings: Nickel-loaded per MIL-C-83231
- Plasma barriers: Refractory metal mesh systems
- Shield terminations: Environmental seal connectors

## 3) Installation Procedures

### 3.1 Surface Preparation
1. **Cleaning:** Remove paint, corrosion, contamination
2. **Abrasion:** Create conductive surface contact
3. **Primer:** Conductive primer if specified
4. **Torque:** Fastener torque per specification

### 3.2 Bonding Strap Installation
1. **Routing:** Follow approved wiring diagram
2. **Length:** Minimize strap length, avoid sharp bends
3. **Connection:** Clean metal-to-metal contact
4. **Hardware:** Use specified washers and fasteners
5. **Protection:** Shield from mechanical damage

### 3.3 EMI Shielding Installation
1. **Fit-up:** Verify shield coverage and overlap
2. **Termination:** 360° termination for effectiveness
3. **Grounding:** Bond shield to structure at multiple points
4. **Sealing:** Environmental sealing as required

## 4) Testing & Verification

### 4.1 Bond Resistance Testing
- **Equipment:** Micro-ohmmeter, 4-wire measurement
- **Current:** 10 amperes DC test current
- **Limits:** <2.5 milliohms for Class A bonds
- **Frequency:** 100% inspection of critical bonds

### 4.2 EMI Effectiveness Testing
- **Method:** Shielding effectiveness per MIL-STD-285
- **Frequency range:** 10 kHz to 10 GHz
- **Acceptance:** >40 dB attenuation minimum
- **Documentation:** Test reports with frequency plots

### 4.3 Lightning Protection Verification
- **Continuity:** End-to-end resistance <1 ohm
- **Current capacity:** Designed for 200,000 ampere peak
- **Inspection:** Visual and dimensional checks
- **Records:** Complete as-built documentation

## 5) Plasma Protection Systems

### 5.1 Entry Interface Design
- Refractory metal mesh barriers
- Thermal expansion joint accommodation
- Electrical isolation where required
- Integration with TPS tile systems

### 5.2 Installation Requirements
- High-temperature fastening systems
- Thermal barrier coatings
- Plasma-resistant materials only
- Ground test verification capability

## 6) Quality Control

### 6.1 Inspection Requirements
- Visual: 100% of all bonds and shields
- Electrical: Bond resistance per sampling plan
- Dimensional: Clearances and routing verification
- Environmental: Seal integrity and protection

### 6.2 Acceptance Criteria
- Bond resistance: Per location class requirements
- Shield effectiveness: >40 dB minimum
- Visual: No damage, corrosion, or contamination
- Installation: Per approved drawings and procedures

## 7) Documentation & Records

### 7.1 Required Forms
- `FORM-QA-20-40-01`: Bonding/EMI Continuity Record
- Bond resistance test data sheets
- EMI effectiveness test reports
- Lightning protection inspection records

### 7.2 Traceability Requirements
- Bonding strap serial numbers and lots
- Test equipment calibration records
- Installation photographs
- As-built wiring diagrams

## 8) Safety & Environmental

### 8.1 Electrical Safety
- Lock-out/tag-out procedures for powered systems
- ESD protection for sensitive components
- High-voltage safety for test equipment
- Arc flash protection during testing

### 8.2 Material Safety
- Conductive coating ventilation requirements
- Metal dust collection and disposal
- Chemical handling per material SDS
- Personal protective equipment requirements

## 9) Routing & System Integration

This SPM integrates with:
- **Electrical design:** Grounding schemes and shield requirements
- **Manufacturing:** Installation procedures and quality control
- **Test:** Lightning simulation and EMI test facilities
- **Configuration management:** As-built record maintenance

All evidence and test data flow through PDM-PLM for configuration control and QS certification.

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*