# Control Surface Examples

This directory contains example JSON instances for control surface specifications following the `control_surface.schema.json` schema.

## Purpose

These examples demonstrate:
- Complete control surface definitions
- Assembly references (hinges, actuators, balance weights)
- Surface finish requirements
- Acceptance metrics
- Effectivity expressions

## Examples

### CS-ELV-001.json
Left elevon control surface for BWB-Q100:
- **Type**: Elevon
- **Construction**: Carbon fiber/epoxy composite laminate
- **Hinges**: 3 ball bearing hinges (HNG-ELV-001, -002, -003)
- **Actuator**: 1 electromechanical actuator (ACTF-ELV-001)
- **Balance**: 1 leading edge mass balance weight (BLW-ELV-001)
- **Surface Finish**: Class B (Ra ≤ 1.6 µm)
- **Effectivity**: MSN001-999

## Schema Reference

All examples validate against:
```
../../schemas/control_surface.schema.json
```

## Required Fields

- `version` - Schema version (SemVer)
- `surface_id` - Unique ID (pattern: CS-[A-Z0-9_-]{3,})
- `type` - "elevon", "flaperon", "spoiler", or "tab"
- `effectivity_expr` - MSN/block/options expression

## Acceptance Metrics

Examples include typical acceptance metrics:
- **Alignment**: ±0.5 mm positional accuracy
- **Surface finish**: Ra ≤ 1.6 µm (Class B)
- Laser alignment measurement
- Profilometer surface scanning

## Assembly References

Control surfaces reference:
- **Hinges**: Array of hinge IDs (HNG-*)
- **Actuator attachments**: Array of actuator fitting IDs (ACTF-*)
- **Balance weights**: Array of balance weight IDs (BLW-*)

## Validation

To validate examples:
```bash
jsonschema -i CS-ELV-001.json ../../schemas/control_surface.schema.json
```

## Usage

Use these examples as templates for:
- New control surface specifications
- Configuration baseline documentation
- Maintenance record references
- Engineering change proposals

## Related

- Schema: `../../schemas/control_surface.schema.json`
- Hinges: `../hinge/`
- Actuators: `../actuator_attachment/`
- Balance: `../balance_weight/`
- ICDs: `../../../icd/`

---
*Part of ATA-57-20 Control Surfaces contract examples.*
