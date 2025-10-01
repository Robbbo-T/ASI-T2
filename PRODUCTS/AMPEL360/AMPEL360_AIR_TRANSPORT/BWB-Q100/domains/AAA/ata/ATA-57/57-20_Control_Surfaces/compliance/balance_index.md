# Balance Evidence Index

Mass & aerodynamic balance evidence; measurement reports, rig outputs, associated acceptance metrics.

## Balance Requirements

Document references to:
- Mass balance calculations and measurements
- Balance weight specifications
- Aerodynamic balance features (horn balance, set-back hinge)
- Balance rig test results
- Static and dynamic balance measurements
- Balance adjustment procedures

## Evidence References

All evidence files are stored externally with references here including:
- File URI or PDM location
- SHA256 hash for integrity verification
- Effectivity information (MSN ranges, blocks)
- Associated balance weight IDs (CO-3.5)
- Acceptance metrics (CO-3.13)
- QS/UTCS anchors

## Format

```yaml
evidence_entry:
  id: BALANCE-CS-001
  type: mass_balance
  description: "Left elevon mass balance measurement"
  uri: "pdm://BWB-Q100/balance/control_surfaces/L_elevon_balance_MSN045.pdf"
  sha256: "ghi789..."
  effectivity: "MSN045"
  balance_weight_ref: "BLW-ELV-001"
  acceptance_metric_ref: "ACPT-BALANCE-001"
  utcs_anchor: "sha256:rst456..."
  timestamp: "2025-02-01T09:15:00Z"
```
