# Actuator Attachment Examples

This directory contains example JSON instances for actuator attachment specifications following the `actuator_attachment.schema.json` schema.

## Purpose

These examples demonstrate:
- Proper schema usage and validation
- Realistic parameter values
- Acceptance metric definitions
- Effectivity expression format
- Interface ICD references

## Examples

### ACTF-ELV-001.json
Electromechanical actuator attachment for left elevon:
- **Type**: Electromechanical linear actuator
- **Capacity**: 45 kN
- **Stroke**: 150 mm
- **Preload**: 60 kN (80% of proof load)
- **Acceptance Metrics**: Preload verification, angular alignment

## Schema Reference

All examples validate against:
```
../../schemas/actuator_attachment.schema.json
```

## Required Fields

- `version` - Schema version (SemVer)
- `attachment_id` - Unique ID (pattern: ACTF-[A-Z0-9_-]{3,})
- `actuator_type` - "hydraulic" or "electromechanical"
- `load_capacity_kN` - Load capacity in kilonewtons

## Validation

To validate examples:
```bash
jsonschema -i ACTF-ELV-001.json ../../schemas/actuator_attachment.schema.json
```

## Usage

Use these examples as templates when creating:
- New actuator attachment specifications
- Actuator upgrade configurations
- Maintenance documentation references
- Interface verification data

## Related

- Schema: `../../schemas/actuator_attachment.schema.json`
- ICD: `../../../icd/ICD-57-20-27_Flight_Control_System.md`
- ICD: `../../../icd/ICD-57-20-29_Hydraulic_System.md`

---
*Part of ATA-57-20 Control Surfaces contract examples.*
