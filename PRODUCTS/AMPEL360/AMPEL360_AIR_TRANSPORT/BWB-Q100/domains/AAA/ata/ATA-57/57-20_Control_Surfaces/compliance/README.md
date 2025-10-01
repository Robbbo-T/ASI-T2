# Compliance Evidence Indexes

This directory contains evidence indexes for compliance substantiation and regulatory certification of ATA-57-20 Control Surfaces.

## Purpose

The compliance directory provides:
- Centralized indexing of substantiation evidence
- References to analysis and test results
- Effectivity tracking for compliance data
- Traceability to regulatory requirements
- QS/UTCS anchors for quality sealing

## Evidence Indexes

### flutter_index.md
References to flutter analysis and test results:
- Wind tunnel test data
- Ground vibration test (GVT) results
- Flutter clearance documentation
- Modal analysis reports
- Natural frequency measurements

### loads_index.md
References to structural and aerodynamic loads:
- Limit and ultimate load cases
- Fatigue load spectra
- Gust and maneuver loads
- Hinge moment envelopes
- Load transfer analysis

### balance_index.md
References to mass and aerodynamic balance evidence:
- Mass balance calculations
- Balance weight specifications
- Static and dynamic balance measurements
- Balance rig test results
- Center of gravity measurements

## Evidence Format

All evidence entries include:
- Unique evidence ID
- Type classification
- Description
- URI/PDM location
- SHA256 hash for integrity
- Effectivity information (MSN, blocks, options)
- Associated acceptance metrics
- QS/UTCS anchors
- Timestamp

## External Storage

Evidence files are stored in PDM/PLM systems:
- Large data files (analysis results, test data)
- CAD models and FEA results
- Test videos and photographs
- Certification documents

Only metadata and references are stored in Git.

## Validation

All evidence indexes must:
- Include SHA256 hashes for integrity verification
- Reference valid acceptance metrics (CO-3.13)
- Include proper effectivity expressions
- Link to QS/UTCS anchors

## Related Directories

- **../evidence/** - Test evidence indexes (hinge, fatigue, finish)
- **../contracts/schemas/** - Acceptance metric schemas
- **../io/** - UTCS/QS routing manifest

---
*Part of ATA-57-20 Control Surfaces compliance framework.*
