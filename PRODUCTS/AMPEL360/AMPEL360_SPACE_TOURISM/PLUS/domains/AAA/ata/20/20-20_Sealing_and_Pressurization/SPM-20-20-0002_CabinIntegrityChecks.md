---
id: ASIT-PLUS-AAA-SPM-20-20-0002
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/20/20-20_Sealing_and_Pressurization/SPM-20-20-0002_CabinIntegrityChecks.md
llc: PROCESS
title: "Standard Practice Manual: Pre-Flight Cabin Integrity Checks"
configuration: baseline
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "1.0.0"
release_date: 2025-09-26
maintainer: "Flight Operations Team"
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

# Standard Practice Manual: Pre-Flight Cabin Integrity Checks

## 1. Purpose
Establish **mandatory pre-flight inspection and test procedures** to verify the hermetic integrity of the **passenger cabin**, **avionics compartments**, and related pressurized volumes of the **AMPEL360 PLUS** vehicle. This SPM ensures leak-tightness, correct operation of relief/over-pressure protections, and proper documentation in UTCS/QS prior to passenger boarding.

## 2. Scope
Applies to:
- **Cabin primary pressure vessel** and interfaces (doors, windows, hatches, penetrations).
- **Service & avionics bays** that are pressure-managed for environmental control.
- **Seal systems** (perimeter door seals, window/frame seals, feed-throughs).
- **Relief, dump, and isolation valves** function checks (non-intrusive).

Excludes: design allowables and certification basis (see ATA-51/53/56/57), life-support performance testing (CCC domain), and software control logic validation (LCC/ATA-27).

## 3. Normative References
- **ATA-20**: Standard Practices – Airframe.  
- **PS-20-20-0001**: *Ablative Sealant Application* (thermal gap sealing at TPS interfaces).  
- **ATA-32/ATA-57**: Gear-door & lifting-surface TPS interfaces (adjacent sealing).
- **ATA-53**: Fuselage (primary pressure vessel).
- **ATA-56**: Windows (transparency pressure retention).
- **CCC/ATA-35**: Life Support (cabin pressurization system performance).

## 4. Equipment & Materials

### 4.1. Pressure Test Equipment
- **Pressure source**: Regulated air/nitrogen, 0-20 psig capability, ±0.1 psi accuracy
- **Pressure instrumentation**: Digital manometers, calibrated within 30 days
- **Flow meters**: Mass flow measurement for leak quantification (SCFM resolution)
- **Temperature sensors**: Ambient temperature compensation for test accuracy

### 4.2. Leak Detection Equipment
- **Soap solution**: Snoop or equivalent, food-grade for passenger areas
- **Ultrasonic leak detector**: Portable unit for high-pressure gas leaks
- **Helium leak detector**: For precision leak location (if specified by engineering)
- **Pressure decay instrumentation**: Data logging capability for automated tests

### 4.3. Safety Equipment
- **Pressure relief**: Portable relief valves for over-pressure protection during test
- **Personal protective equipment**: Safety glasses, hearing protection for pneumatic equipment
- **Emergency procedures**: Posted procedures for pressure system emergencies

## 5. Pre-Flight Inspection Procedures

### 5.1. Visual Inspection
1. **Cabin interior**: Inspect all visible seals, gaskets, windows, door frames for:
   - Cracks, cuts, permanent deformation in sealing surfaces
   - Foreign object debris (FOD) in seal grooves or contact surfaces
   - Proper seal installation and retention (no missing clips, retainers)
   - Door and hatch alignment, proper engagement of latching mechanisms

2. **External inspection**: Verify:
   - Door and hatch external seals for damage, contamination
   - Vent and relief port clear of obstructions
   - TPS-to-structure seal continuity at cabin interfaces (visual only)

### 5.2. Functional Checks
1. **Door operations**: Cycle all cabin doors/hatches through full operation:
   - Proper latching engagement and release
   - Door seal compression (tactile check during closing)
   - Warning lights and position indication (if installed)
   - Emergency release operation (ground safety engaged)

2. **Window integrity**: Check window installations:
   - Frame-to-fuselage seal integrity
   - Window-to-frame seal condition
   - No stress cracks in transparency material
   - Proper installation torque on retaining hardware (if accessible)

## 6. Pressure Testing Procedures

### 6.1. Test Setup
1. **Cabin preparation**:
   - Remove or secure all loose objects from cabin
   - Close and latch all doors, hatches, vents per normal flight configuration
   - Install pressure test connections at designated service ports
   - Verify all pressure relief systems are operational and set correctly

2. **Instrumentation**:
   - Connect calibrated pressure gauges at multiple cabin locations
   - Install temperature sensors for ambient correction
   - Verify data logging system operation and time synchronization

### 6.2. Pressure Decay Test
1. **Initial pressurization**:
   - Slowly pressurize cabin to **3.0 psig** (±0.1 psi)
   - Allow 15-minute stabilization period for thermal equilibrium
   - Record initial pressure, temperature, and time

2. **Decay measurement**:
   - Isolate pressure source and monitor for **30 minutes**
   - Record pressure at 5-minute intervals (automated preferred)
   - Calculate leak rate: L = (ΔP × V) / (Δt × P_atm) where:
     - L = leak rate (SCFM)
     - ΔP = pressure drop (psi)
     - V = cabin volume (ft³)
     - Δt = test duration (minutes)
     - P_atm = atmospheric pressure (psia)

3. **Acceptance criteria**:
   - **Maximum allowable leak rate**: 0.5 SCFM at 3.0 psig
   - **Pressure drop limit**: <0.2 psi in 30 minutes at constant temperature
   - **Test validity**: Temperature variation <±5°F during test period

### 6.3. Leak Location (if required)
1. **Pressurize to test pressure** (3.0 psig) and maintain
2. **Soap solution application**: Apply to all suspected leak areas:
   - Door and window perimeter seals
   - Penetrations and feed-throughs
   - Structural joints with pressure boundary function
3. **Ultrasonic detection**: Use for inaccessible or hard-to-see areas
4. **Document leak locations**: Photography and written description for repair action

## 7. Acceptance Criteria & Disposition

### 7.1. Pass Criteria
- **Leak rate**: ≤0.5 SCFM at 3.0 psig test pressure
- **Visual inspection**: No damage, FOD, or improper installation noted
- **Functional checks**: All doors, latches, and seals operate normally
- **Relief system**: Proper operation of pressure relief and dump valves

### 7.2. Failure Modes & Actions
- **Excessive leak rate**: Locate and repair leaks, re-test after repair
- **Visual defects**: Replace damaged seals, clean FOD, adjust door alignment
- **Functional failures**: Repair or replace latching mechanisms, adjust door rigging
- **Relief system malfunction**: Repair or replace valves, re-calibrate settings

### 7.3. Documentation Requirements
- **Test data sheet**: Pressures, temperatures, leak rates, test duration
- **Discrepancy log**: Description of any anomalies found and corrective actions
- **Photographic record**: Document any damage or repairs performed
- **Sign-off**: Authorized inspector signature and date/time of completion

## 8. Safety Considerations

### 8.1. Pressure System Safety
- **Maximum test pressure**: Never exceed 3.5 psig (safety limit)
- **Relief protection**: Ensure relief valves are functional before pressurizing
- **Personnel evacuation**: Clear cabin during pressure testing (automated systems only)
- **Emergency depressurization**: Immediate manual dump capability readily available

### 8.2. Confined Space Safety
- **Ventilation**: Ensure adequate air exchange before personnel entry
- **Communication**: Maintain radio contact with test personnel
- **Emergency egress**: Multiple exit routes available and unobstructed
- **Gas detection**: Monitor for hazardous gas accumulation (nitrogen, etc.)

## 9. Quality Assurance & Traceability

### 9.1. Personnel Qualifications
- **Inspector certification**: Current qualification on AMPEL360 PLUS systems
- **Pressure test training**: Specific training on these procedures within 12 months
- **Safety training**: Confined space and pressure system safety current

### 9.2. Equipment Calibration
- **Pressure gauges**: Calibration within 30 days of use
- **Flow meters**: Annual calibration with NIST-traceable standards
- **Temperature sensors**: Calibration within 6 months
- **Calibration records**: Maintained in UTCS/QS system

### 9.3. Record Retention
- **Test records**: Permanent retention in aircraft logbook and UTCS/QS
- **Trend analysis**: Leak rate trends monitored for predictive maintenance
- **Configuration control**: Test procedure revisions controlled and distributed
- **Audit trail**: Complete traceability of all test data and corrective actions

## 10. Revision Control

This SPM is subject to configuration control through the UTCS/QS system. Changes require approval by Flight Operations and Quality Assurance. Personnel must be trained on current revision before performing these procedures. Revision status is maintained electronically with automatic notification of updates.