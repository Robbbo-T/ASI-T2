# Balance Weight Examples

This directory contains example JSON instances for balance weight specifications following the `balance_weight.schema.json` schema.

## Purpose

These examples demonstrate:
- Mass balance weight definitions
- Center of gravity specifications
- Attachment method documentation
- Adjustment range parameters
- Acceptance criteria

## Examples

### BLW-ELV-001.json
Leading edge mass balance weight for left elevon:
- **Mass**: 2.850 kg
- **Material**: Tungsten alloy
- **Location**: Station 325, leading edge horn balance cavity
- **Attachment**: Bolted with adjustable shims, lock-wired
- **Adjustment Range**: ±25g (50g total)
- **CG Location**: -125 mm from hinge line (forward)

## Schema Reference

All examples validate against:
```
../../schemas/balance_weight.schema.json
```

## Required Fields

- `version` - Schema version (SemVer)
- `weight_id` - Unique ID (pattern: BLW-[A-Z0-9_-]{3,})
- `mass_kg` - Mass in kilograms
- `attachment_method` - Attachment description

## Acceptance Metrics

Examples include typical acceptance metrics:
- **Mass accuracy**: ±5g tolerance
- **CG location**: ±2mm tolerance from design position
- Weighing on calibrated scales
- Balance rig measurements

## Validation

To validate examples:
```bash
jsonschema -i BLW-ELV-001.json ../../schemas/balance_weight.schema.json
```

## Usage

Use these examples as templates when:
- Specifying balance weights for new control surfaces
- Documenting balance weight replacements
- Recording balance adjustments during rigging
- Verifying flutter margin compliance

## Related

- Schema: `../../schemas/balance_weight.schema.json`
- Compliance: `../../../compliance/balance_index.md`
- Evidence: `../../../evidence/hinge_tests_index.md`
- Form: ATA-20-60-01 Balance Weight Installation

---
*Part of ATA-57-20 Control Surfaces contract examples.*
