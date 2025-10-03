# Evidence

This directory contains test and measurement evidence indexes for ATA-57-20 Control Surfaces.

## Purpose

The evidence directory provides:
- Centralized indexing of test results
- References to measurement data
- Traceability to acceptance criteria
- QS/UTCS anchors for quality sealing
- Effectivity tracking

## Evidence Indexes

### hinge_tests_index.md
Hinge performance test references:
- Friction torque measurements
- Free play measurements
- Load capacity tests
- Wear tests
- Bearing performance data

### fatigue_tests_index.md
Fatigue life test references:
- Full-scale control surface fatigue tests
- Component fatigue tests (hinges, fittings)
- Crack growth monitoring
- Fatigue spectrum definitions
- Test-to-failure results

### surface_finish_index.md
Surface finish measurement references:
- Profilometer scan data
- Surface roughness measurements (Ra, Rz)
- Visual inspection reports
- Aerodynamic smoothness verification
- Repair area finish verification

## Evidence Format

All evidence entries include:
- Unique evidence ID
- Type classification
- Description
- Test article identification
- Test facility/equipment
- URI/PDM location
- SHA256 hash for integrity
- Effectivity information
- Acceptance metric references
- Result status (PASS/FAIL)
- QS/UTCS anchors
- Timestamp

## External Storage

Evidence files are stored in PDM/PLM systems:
- Raw test data and traces
- Calibration certificates
- Test setup photographs
- Data acquisition logs
- Analysis reports

Only metadata and references are stored in Git.

## Acceptance Criteria

Evidence is linked to acceptance metrics:
- Hinge friction: ≤ 0.5 Nm
- Free play: ≤ 0.1 mm
- Surface finish: Ra ≤ 1.6 µm (Class B)
- Fatigue life: Complete target cycles without critical damage

See `../contracts/schemas/acceptance.metric.schema.json`

## Validation

All evidence indexes must:
- Include SHA256 hashes for integrity
- Reference valid acceptance metrics
- Include proper effectivity expressions
- Link to QS/UTCS anchors
- Follow YAML format conventions

## Related Directories

- **../compliance/** - Compliance evidence (flutter, loads, balance)
- **../contracts/schemas/** - Acceptance metric schemas
- **../io/** - UTCS/QS routing manifest
- **../S1000D/DMC/PR/** - Test procedures

---
*Part of ATA-57-20 Control Surfaces evidence framework.*
