---
id: ASIT-PLUS-AAA-SPM-20-40-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/20/20-40_Electrical_Bonding/SPM-20-40-0001_PlasmaShieldingBonding.md
llc: PROCESS
title: "Standard Practice Manual: Plasma Shielding & Structural Bonding"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "Electrical Systems Team"
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

# Standard Practice Manual: Plasma Shielding & Structural Bonding

## 1. Purpose
This manual establishes **mandatory practices** for electrical bonding, electromagnetic interference (EMI) protection, and plasma shielding of the **AMPEL360 PLUS** space tourism vehicle. It ensures electrical continuity, lightning protection, static discharge prevention, and protection against reentry plasma effects during space tourism operations.

## 2. Scope
Applies to all electrical bonding and shielding systems including:
- **Structural bonding** between metallic and composite components
- **Lightning protection** systems and strike attachment points
- **Static discharge** prevention and dissipation systems
- **EMI/RFI shielding** for electronic systems and wiring
- **Plasma protection** during reentry phase
- **Grounding systems** for electrical safety and functionality

**Exclusions:** Power system grounding (see EEE/ATA-24), avionics shielding design (see IIS/ATA-42), communications antenna systems (see LCC/ATA-23).

## 3. Normative References
- **ATA-20:** Standard Practices – Airframe (this chapter)
- **SPM-20-10-0001:** *Composite Fastening & Bonding* (structural interfaces)
- **EEE/ATA-24:** Electrical Power (power system grounding)
- **IIS/ATA-42:** Integrated Modular Avionics (EMI requirements)
- **MIL-B-5087:** *Bonding, Electrical, for Aircraft*
- **DO-160:** *Environmental Conditions and Test Procedures for Airborne Equipment*

## 4. Electrical Bonding Requirements

### 4.1. Bonding Resistance Limits
- **Structure-to-structure bonds:** ≤2.5 milliohms DC resistance
- **Equipment grounding:** ≤2.5 milliohms to structure
- **Lightning protection:** ≤1.0 milliohm for primary current paths
- **Static discharge:** ≤10 megohms surface resistivity maximum

### 4.2. Bond Permanence Classifications
- **Class R (Removable):** Demountable equipment, access panels, removable fairings
- **Class S (Semi-permanent):** Major assemblies, engine mounts, wing attachments
- **Class P (Permanent):** Welded or bonded joints not intended for disassembly

### 4.3. Environmental Requirements
- **Temperature range:** -65°F to +200°F (-54°C to +93°C) operational
- **Humidity:** 95% RH at 160°F (71°C) for 240 hours
- **Salt spray:** 5% NaCl solution, 35°C, 48 hours exposure
- **Vibration:** Per vehicle flight load spectrum without degradation

## 5. Materials & Hardware

### 5.1. Bonding Straps & Jumpers
- **Flexible copper braid:** Tin-plated, per MIL-B-5087
- **Solid conductors:** Copper or aluminum per application requirements
- **Stainless steel straps:** For high-temperature applications (>200°F)
- **Conductive gaskets:** Beryllium-copper, silver-plated per EMI requirements

### 5.2. Fasteners & Hardware
- **Bonding screws:** Cadmium-plated steel or stainless steel with star washers
- **Bonding nuts:** Self-locking with integral star washer or spring contact
- **Conductive compounds:** Silver-filled grease for aluminum-to-aluminum bonds
- **Sealants:** Conductive sealants for EMI gasketing applications

### 5.3. Surface Treatments
- **Aluminum surfaces:** Alodine 1200S or chromate conversion coating
- **Steel surfaces:** Cadmium or zinc plating with chromate topcoat
- **Composite surfaces:** Conductive primer or metallic mesh integration
- **Dissimilar metal protection:** Barrier coatings to prevent galvanic corrosion

## 6. Installation Procedures

### 6.1. Surface Preparation
1. **Cleaning:** Remove all paint, primer, oxide, and contamination from bond area
2. **Surface finish:** 250 μin RMS maximum, 63 μin RMS preferred
3. **Chemical treatment:** Apply appropriate conversion coating per material
4. **Masking:** Protect adjacent areas from surface treatment chemicals

### 6.2. Bonding Strap Installation
1. **Strap selection:** Size conductors for maximum fault current plus 25% margin
2. **Routing:** Minimize length, avoid sharp bends, protect from mechanical damage
3. **Termination:** Use appropriate lugs, apply anti-oxidant compound
4. **Hardware:** Install with specified torque, use star washers for permanent contact

### 6.3. Composite Structure Bonding
1. **Conductive elements:** Install metallic mesh or conductive primer during layup
2. **Attachment points:** Use metallic inserts or bonded fittings for bond attachment
3. **Continuity:** Verify electrical path through composite structure joints
4. **Protection:** Seal bond points to prevent moisture ingress and corrosion

### 6.4. EMI Shielding Installation
1. **Gasket selection:** Choose appropriate material for frequency range and environment
2. **Compression:** Achieve 25-50% gasket compression for effective shielding
3. **Continuity:** Ensure 360-degree electrical continuity around shielded enclosures
4. **Maintenance access:** Design for gasket replacement without structure modification

## 7. Lightning Protection System

### 7.1. Strike Attachment Points
- **Location:** Wing tips, nose cone, tail surfaces, antenna mounts
- **Design:** Low impedance path to structure with surge protection
- **Materials:** Copper or aluminum conductors, stainless steel attachment hardware
- **Spacing:** Maximum 10-foot spacing along extremities for attachment probability

### 7.2. Current Path Design
- **Primary paths:** Heavy conductors (minimum #4 AWG) for lightning current
- **Secondary paths:** Bonding jumpers across joints in primary current path
- **Protection:** Surge suppressors at sensitive equipment interfaces
- **Testing:** High-current injection testing to verify path integrity

### 7.3. Composite Structure Protection
- **Expanded foil:** Embedded metallic mesh for current distribution
- **Edge protection:** Metallic strips at composite panel edges
- **Fastener protection:** Isolation or surge protection at critical fasteners
- **Resin system:** Lightning-resistant resin systems in high-risk areas

## 8. Plasma Environment Protection

### 8.1. Reentry Plasma Effects
- **Electrical isolation:** Plasma sheath can isolate vehicle from ground potential
- **Communication blackout:** Plasma interferes with RF communications
- **Static buildup:** Charge accumulation on vehicle surfaces during reentry
- **Arc protection:** Prevention of destructive arcing between isolated components

### 8.2. Plasma Mitigation Measures
- **Conductive surfaces:** Maintain electrical continuity across all external surfaces
- **Static dissipation:** Provide controlled discharge paths to prevent arc-over
- **Material selection:** Use materials resistant to plasma erosion and electrical effects
- **System design:** Design electronics to operate in high electrical noise environment

### 8.3. Special Considerations
- **TPS integration:** Maintain electrical continuity through thermal protection system
- **Window treatments:** Conductive coatings on windows for electrical continuity
- **Antenna systems:** Plasma-resistant antenna designs and materials
- **Monitoring systems:** Real-time plasma environment monitoring during reentry

## 9. Testing & Verification

### 9.1. Resistance Measurements
- **Equipment:** Calibrated microhmmeter or bond tester
- **Test current:** 10 amperes DC minimum for structural bonds
- **Frequency:** Initial installation, after maintenance, annual verification
- **Documentation:** Test results recorded in UTCS/QS system

### 9.2. High-Current Testing
- **Lightning simulation:** High-current pulse testing of protection systems
- **Current levels:** Up to 200,000 amperes peak for lightning simulation
- **Waveform:** 8/20 microsecond double exponential per IEC standards
- **Safety:** Remote operation with proper safety procedures and equipment

### 9.3. EMI Effectiveness Testing
- **Shielding effectiveness:** Per MIL-STD-285 or IEEE-299 standards
- **Frequency range:** DC to 18 GHz for space vehicle applications
- **Acceptance criteria:** Minimum 40 dB shielding effectiveness
- **Test setup:** Controlled electromagnetic environment with calibrated instrumentation

## 10. Quality Control & Acceptance

### 10.1. Inspection Requirements
- **Visual inspection:** 100% of all bonds for proper installation and hardware
- **Resistance testing:** All structural bonds and equipment grounding points
- **Continuity verification:** End-to-end continuity checks on current paths
- **Documentation review:** Verify all test data and acceptance criteria met

### 10.2. Acceptance Criteria
- **Bond resistance:** Must meet specified limits for each bond classification
- **Visual standards:** No corrosion, proper hardware installation, adequate clearances
- **Current path integrity:** Continuous path with no high-resistance joints
- **EMI effectiveness:** Measured shielding meets or exceeds design requirements

### 10.3. Rejection & Corrective Action
- **High resistance:** Clean and remake bond connections, verify surface preparation
- **Corrosion:** Remove corrosion, apply proper protective treatment, remake bond
- **Hardware defects:** Replace defective hardware, verify proper installation
- **Continuity failure:** Locate and repair open circuits, verify repair effectiveness

## 11. Maintenance & Monitoring

### 11.1. Periodic Inspection
- **Frequency:** Annual inspection of all accessible bonds and connections
- **Post-flight:** Inspection after lightning strike or suspected electrical anomaly
- **Environmental:** Additional inspection after severe weather exposure
- **Trending:** Monitor resistance values for degradation trends

### 11.2. Preventive Maintenance
- **Cleaning:** Remove corrosion and contamination from bond areas
- **Re-torque:** Verify fastener torque on removable bond connections
- **Replacement:** Replace degraded gaskets, corroded hardware, damaged straps
- **Protection:** Apply protective treatments and sealants as required

### 11.3. Condition Monitoring
- **Resistance monitoring:** Automated monitoring systems where practical
- **Environmental sensors:** Monitor temperature, humidity, contamination levels
- **Performance tracking:** Monitor EMI performance and lightning protection effectiveness
- **Data analysis:** Trend analysis for predictive maintenance scheduling

## 12. Safety Requirements

### 12.1. Personnel Safety
- **Electrical hazards:** Lock-out/tag-out procedures for high-voltage systems
- **Chemical exposure:** Proper ventilation and PPE for surface treatment chemicals
- **High-current testing:** Safety procedures for lightning simulation testing
- **Training:** Certified technicians only for critical bonding operations

### 12.2. System Safety
- **Ground loops:** Avoid ground loops that could cause electrical interference
- **Isolation:** Proper isolation of sensitive equipment from high-current paths
- **Protection:** Surge protection for critical electronic systems
- **Fail-safe design:** Bonding system failures should not compromise vehicle safety

## 13. Documentation & Configuration Control

### 13.1. Technical Documentation
- **Installation drawings:** Detailed drawings showing bond locations and requirements
- **Test procedures:** Specific procedures for all required testing
- **Material specifications:** Approved materials list with application notes
- **Inspection criteria:** Clear acceptance/rejection criteria with examples

### 13.2. Quality Records
- **Installation records:** Documentation of all bond installations with signatures
- **Test data:** All resistance measurements and test results
- **Maintenance history:** Complete history of inspections, repairs, and modifications
- **Configuration control:** Changes controlled through engineering change process

This standard practice manual ensures the electrical integrity and protection of the AMPEL360 PLUS space tourism vehicle throughout all phases of flight operations.