---
id: SPM-20-20-0002
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/20/20-20_Sealing_and_Pressurization/SPM-20-20-0002_CabinIntegrityChecks.md
llc: SYSTEMS
title: "SPM-20-20-0002: Standard Practice Manual — Pre-Flight/Pre-Close Cabin Integrity Checks"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "Ground Operations Team"
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

# SPM-20-20-0002: Standard Practice Manual — Pre-Flight/Pre-Close Cabin Integrity Checks

## 1) Purpose & Scope

This Standard Practice Manual (SPM) defines the pre-flight and pre-close inspection procedures for cabin integrity verification in the BWB-Q100 vehicle, including:

- Pressure decay testing procedures
- Leak detection and acceptance criteria
- Visual inspection requirements for seals and barriers
- Documentation and evidence requirements
- Go/no-go decision criteria for flight operations

## 2) Test Equipment & Setup

### 2.1 Pressure Test Equipment
- Pressure source: 0-50 psia, regulated to ±0.1 psi
- Pressure transducers: ±0.05% accuracy, 0.1 psi resolution
- Data acquisition: 1 Hz sampling minimum
- Environmental monitoring: Temperature, humidity, barometric pressure

### 2.2 Leak Detection Equipment
- Helium mass spectrometer: 10⁻⁹ std cc/sec sensitivity
- Ultrasonic leak detector: 40 kHz frequency
- Bubble test solution: Approved leak detection fluid
- Access equipment: Platforms, lighting, inspection tools

## 3) Pre-Test Inspection

### 3.1 Visual Inspection
1. **Seal condition:** Check for cuts, tears, displacement
2. **Hardware:** Verify fastener torque and engagement
3. **Access panels:** Confirm proper closure and sealing
4. **Penetrations:** Inspect wire/tube feed-throughs
5. **Structural integrity:** Check for cracks or damage

### 3.2 Environmental Conditions
- Ambient temperature: 65-85°F (18-29°C)
- Barometric pressure: 29.0-31.0 in Hg
- Wind velocity: <20 mph for outdoor testing
- Precipitation: None during test period

## 4) Pressure Decay Test Procedure

### 4.1 Initial Pressurization
1. **Setup:** Connect pressure source and instrumentation
2. **Baseline:** Record ambient conditions
3. **Pressurize:** Slowly increase to test pressure (8.6 psia typical)
4. **Stabilize:** Allow 15-minute stabilization period
5. **Seal:** Isolate cabin from pressure source

### 4.2 Decay Measurement
1. **Duration:** Monitor pressure for 30 minutes minimum
2. **Data collection:** Record pressure every 30 seconds
3. **Temperature compensation:** Account for thermal effects
4. **Calculation:** Determine leak rate in scfm or scih

### 4.3 Acceptance Criteria
| Cabin Volume | Maximum Leak Rate | Test Pressure |
|---|---|---|
| Main cabin | 0.05 scfm | 8.6 psia |
| Avionics bay | 0.02 scfm | 5.0 psia |
| Equipment bay | 0.03 scfm | 5.0 psia |

## 5) Leak Detection & Localization

### 5.1 Helium Tracer Gas Method
1. **Preparation:** Evacuate cabin to 1 torr or less
2. **Tracer application:** Apply helium to suspect areas
3. **Detection:** Use mass spectrometer with probe
4. **Quantification:** Measure leak rate in std cc/sec
5. **Documentation:** Mark and photograph leak locations

### 5.2 Bubble Test Method
1. **Pressurization:** Maintain 2-5 psi positive pressure
2. **Solution application:** Apply leak detection fluid
3. **Observation:** Look for bubble formation
4. **Size assessment:** Measure bubble formation rate
5. **Repair:** Mark for immediate attention if required

## 6) Documentation Requirements

### 6.1 Test Records
- Environmental conditions log
- Pressure decay data sheets
- Leak detection results
- Photographic evidence
- Inspector signatures and certifications

### 6.2 Corrective Actions
- Non-conformance reports for failures
- Repair procedures and re-test requirements
- Engineering disposition for marginal results
- Final acceptance signatures

## 7) Decision Criteria

### 7.1 Accept for Flight
- All leak rates within acceptance limits
- No visual defects requiring immediate attention
- Complete documentation package
- All corrective actions closed

### 7.2 Reject/Repair Required
- Any leak rate exceeding acceptance criteria
- Visual evidence of seal damage or deterioration
- Missing or incomplete documentation
- Environmental test conditions not met

## 8) Quality Forms

Required documentation:
- `FORM-QA-20-20-01`: Cabin Integrity Test Record
- `FORM-QA-20-20-02`: Leak Detection Results
- `FORM-QA-20-20-03`: Pre-Flight Inspection Checklist
- Environmental conditions log
- Calibration records for test equipment

## 9) Routing & Integration

This SPM integrates with:
- **Ground operations:** Pre-flight inspection procedures
- **Engineering:** Leak rate acceptance criteria and analysis
- **Quality:** Inspection records and flight readiness certification
- **Configuration management:** As-built seal and barrier configurations

All test data and evidence flow through PDM-PLM for flight readiness determination and QS certification.

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*