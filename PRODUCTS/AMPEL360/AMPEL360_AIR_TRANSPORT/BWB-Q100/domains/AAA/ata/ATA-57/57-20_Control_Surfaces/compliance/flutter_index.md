# Flutter Evidence Index

List controlled references to flutter analysis & test results (URIs + sha256). No large files in-repo.

## Flutter Analysis

Document references to:
- Flutter analysis reports for control surfaces
- Wind tunnel test results
- Ground vibration test (GVT) data for control surfaces
- Flutter clearance documentation
- Modal analysis results

## Evidence References

All evidence files are stored externally with references here including:
- File URI or PDM location
- SHA256 hash for integrity verification
- Effectivity information (MSN ranges, blocks)
- Associated acceptance metrics (CO-3.13)
- QS/UTCS anchors

## Format

```yaml
evidence_entry:
  id: FLUTTER-CS-001
  type: flutter_analysis
  description: "Elevon flutter analysis, cruise configuration"
  uri: "pdm://BWB-Q100/analysis/flutter/elevon_cruise_v1.2.pdf"
  sha256: "abc123..."
  effectivity: "MSN001-999"
  acceptance_metric_ref: "ACPT-FLUTTER-001"
  utcs_anchor: "sha256:xyz789..."
  timestamp: "2025-01-15T10:30:00Z"
```
