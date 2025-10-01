# Surface Finish Evidence

Profilometer logs, visual inspection records, acceptance metrics (CO-3.13), QS signature refs.

## Surface Finish Requirements

Document references to:
- Surface roughness measurements (Ra, Rz)
- Aerodynamic smoothness verification
- Waviness and profile measurements
- Visual inspection reports
- Surface defect documentation
- Repair area finish verification

## Measurement Methods

Surface finish measurement techniques:
- Profilometer scans (contact/non-contact)
- Visual inspection (lighting requirements)
- Template/gauge measurements
- Photogrammetry for large areas
- Acceptance zone verification

## Evidence References

All evidence files are stored externally with references here including:
- Profilometer scan data and plots
- Visual inspection photographs
- Measurement locations and grid patterns
- Acceptance criteria and tolerances
- Inspection reports and sign-offs
- Effectivity information
- QS/UTCS anchors

## Format

```yaml
evidence_entry:
  id: FINISH-CS-001
  type: surface_finish
  description: "Left elevon upper surface finish measurement"
  control_surface_id: "CS-ELV-001"
  surface: "upper"
  measurement_date: "2025-03-20"
  inspector: "QA-Inspector-042"
  method: "non-contact_profilometer"
  equipment: "PROF-NC-001"
  calibration_cert: "CAL-2025-015"
  grid_pattern: "200mm_x_200mm"
  measurements_count: 48
  uri: "pdm://BWB-Q100/inspection/surface_finish/L_elevon_upper_finish.csv"
  sha256: "vwx234..."
  acceptance_metric_ref: "ACPT-FINISH-001"
  result: "PASS"
  max_Ra_measured_um: 1.4
  limit_Ra_um: 1.6
  smoothness_class: "B"
  utcs_anchor: "sha256:yza567..."
  timestamp: "2025-03-20T11:30:00Z"
```

## Acceptance Criteria

- Surface smoothness: Ra ≤ 1.6 µm (Class B typical)
- No visible waviness beyond tolerance
- No surface defects (scratches, dents) exceeding limits
- Aerodynamic template fit within tolerance
- Post-repair surfaces meet original finish requirements
