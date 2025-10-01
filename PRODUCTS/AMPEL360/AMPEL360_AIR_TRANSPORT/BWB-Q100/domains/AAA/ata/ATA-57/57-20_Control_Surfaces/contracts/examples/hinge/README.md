# Hinge Examples

This directory contains example JSON instances for hinge assembly specifications following the `hinge.schema.json` schema.

## Purpose

These examples demonstrate:
- Hinge type definitions
- Bearing specifications
- Performance limits (friction, free play)
- Fastener references
- Acceptance criteria

## Examples

### HNG-ELV-001.json
Inboard hinge for left elevon:
- **Type**: Center-type hinge
- **Bearing**: Ball bearing
- **Fitting**: Titanium with aluminum bronze bushing
- **Friction Limit**: ≤ 0.5 Nm
- **Free Play**: ≤ 0.1 mm
- **Deflection Range**: ±30°

### HNG-ELV-002.json
Mid-span hinge for left elevon:
- Similar specifications to HNG-ELV-001
- Mid-span location on elevon

## Schema Reference

All examples validate against:
```
../../schemas/hinge.schema.json
```

## Required Fields

- `version` - Schema version (SemVer)
- `hinge_id` - Unique ID (pattern: HNG-[A-Z0-9_-]{3,})
- `hinge_type` - "overhung", "underhung", "center", or "special"
- `bearing_type` - "ball", "roller", or "sleeve"

## Acceptance Metrics

Examples include typical acceptance metrics:
- **Friction torque**: ≤ 0.5 Nm (measured through full ROM)
- **Free play**: ≤ 0.1 mm (measured at bearing center)
- Calibrated torque wrench measurement
- Dial indicator measurement

## Validation

To validate examples:
```bash
jsonschema -i HNG-ELV-001.json ../../schemas/hinge.schema.json
```

## Usage

Use these examples as templates when:
- Specifying hinges for new control surfaces
- Documenting hinge replacements
- Recording hinge maintenance actions
- Verifying hinge performance criteria

## Related

- Schema: `../../schemas/hinge.schema.json`
- Evidence: `../../../evidence/hinge_tests_index.md`
- ICD: `../../../icd/ICD-57-20-57-10_Wing_Structure.md`
- Form: ATA-20-70-01 Hinge Installation & Adjustment

---
*Part of ATA-57-20 Control Surfaces contract examples.*
