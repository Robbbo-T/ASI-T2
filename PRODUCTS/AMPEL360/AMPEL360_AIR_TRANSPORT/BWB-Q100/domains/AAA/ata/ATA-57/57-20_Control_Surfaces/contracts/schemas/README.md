# JSON Schemas

This directory contains JSON Schema (Draft 2020-12) definitions for ATA-57-20 Control Surfaces artifacts.

## Purpose

These schemas define:
- Data structures for control surface components
- Validation rules and constraints
- Required and optional fields
- Pattern matching for identifiers
- Cross-references between artifacts

## Schema Files

### acceptance.metric.schema.json
Generic acceptance and inspection metrics:
- Metric identification and naming
- Units of measurement
- Target values and limits
- Measurement methods
- Evidence references

### control_surface.schema.json
Control surface structural definitions:
- Surface types (elevon, flaperon, spoiler, tab)
- Geometry and laminate references
- Assembly component references (hinges, actuators, balance weights)
- Surface finish requirements
- Effectivity expressions

### hinge.schema.json
Hinge assembly specifications:
- Hinge types (overhung, underhung, center, special)
- Bearing specifications (ball, roller, sleeve)
- Performance limits (torque, free play)
- Fastener references
- Acceptance metrics

### actuator_attachment.schema.json
Actuator interface definitions:
- Actuator types (hydraulic, electromechanical)
- Load capacity and stroke
- Interface ICD references
- Preload requirements
- Acceptance metrics

### balance_weight.schema.json
Mass balance specifications:
- Mass and location
- Attachment methods
- Adjustment ranges
- Acceptance criteria

## Schema Versioning

All schemas follow semantic versioning (SemVer):
- **Major.Minor.Patch** format
- Documented in each schema's `version` property
- Governed by ICD-AAA-ATA-57-20.md

### Version Guidelines
- **Major**: Breaking changes (e.g., removing required fields)
- **Minor**: Backward-compatible additions (e.g., new optional fields)
- **Patch**: Clarifications, documentation improvements

## Validation

### Schema Syntax Validation
```bash
python -m json.tool acceptance.metric.schema.json > /dev/null
```

### Instance Validation
```bash
jsonschema -i ../examples/control_surface/CS-ELV-001.json control_surface.schema.json
```

### CI/CD Integration
Schemas are validated automatically in CI/CD pipelines before:
- Merging to main branch
- Creating releases
- Deployment to production

## Schema References

Schemas use `$ref` to reference other schemas:
- Relative file paths: `./acceptance.metric.schema.json`
- JSON Pointer syntax for nested definitions

Example:
```json
{
  "acceptance_metrics": {
    "type": "array",
    "items": {
      "$ref": "./acceptance.metric.schema.json"
    }
  }
}
```

## Usage Guidelines

### Creating New Artifacts
1. Reference appropriate schema in `$schema` property
2. Follow ID pattern requirements (e.g., CS-*, HNG-*, ACTF-*)
3. Include version matching schema version
4. Validate before committing

### Updating Schemas
1. Determine version bump type
2. Update schema file
3. Update ICD-AAA-ATA-57-20.md
4. Migrate existing instances if breaking change
5. Update documentation

## Related

- Examples: `../examples/`
- Contract ICD: `../ICD-AAA-ATA-57-20.md`
- Validation: CI/CD workflows
- Documentation: `../../README.md`

---
*Part of ATA-57-20 Control Surfaces contract framework.*
