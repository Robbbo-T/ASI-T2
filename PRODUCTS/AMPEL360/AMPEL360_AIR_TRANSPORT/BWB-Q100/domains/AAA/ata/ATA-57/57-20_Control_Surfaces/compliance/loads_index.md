# Loads Evidence Index

Controlled references to aero/structural loads (limit/ultimate, fatigue spectra), with effectivity.

## Load Cases

Document references to:
- Control surface aerodynamic loads
- Limit and ultimate load cases
- Fatigue load spectra
- Gust and maneuver loads
- Hinge moment envelopes
- Actuation force requirements

## Evidence References

All evidence files are stored externally with references here including:
- File URI or PDM location
- SHA256 hash for integrity verification
- Effectivity information (MSN ranges, blocks, options)
- Associated load case IDs (CO-3.9)
- QS/UTCS anchors

## Format

```yaml
evidence_entry:
  id: LOADS-CS-001
  type: structural_loads
  description: "Elevon limit loads, symmetric flight"
  uri: "pdm://BWB-Q100/loads/control_surfaces/elevon_limit_v2.1.xlsx"
  sha256: "def456..."
  effectivity: "MSN001-999, OPT-HIGH-SPEED"
  load_case_ref: "LC-CS-001"
  utcs_anchor: "sha256:uvw123..."
  timestamp: "2025-01-20T14:45:00Z"
```
