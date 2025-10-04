# JSON Schemas

This directory contains JSON Schema (Draft 2020-12) files that define data contracts for wing primary structure artifacts.

## Purpose

Provides formal schemas for:
- Structural component definitions
- Joint and fastener specifications
- Acceptance criteria and metrics
- Data validation and interchange

## Schemas

### acceptance.metric.schema.json
Defines inspection acceptance criteria and metrics including:
- Measurement methods and equipment
- Acceptance limits (upper/lower)
- Inspection frequency and sampling
- Evidence requirements

### attachment.fitting.schema.json
Defines wing attachment fittings including:
- Fitting geometry and materials
- Load capabilities (tension, compression, shear, moment)
- Bushing specifications
- Interface references

### fastener.set.schema.json
Defines fastener specifications including:
- Fastener codes and dimensions
- Material and finish specifications
- Installation parameters (torque, hole preparation)
- Acceptance criteria (flushness, visual inspection)

### joint.schema.json
Defines structural joints including:
- Joint types (mechanical, adhesive, hybrid)
- Member configurations
- Load capabilities and environmental classes
- Acceptance requirements and NDT

### laminate.stack.schema.json
Defines composite laminate layups including:
- Material system (resin, fiber, prepreg)
- Ply sequences and orientations
- Cure profiles and quality requirements
- Allowables and applications

### crack_event.schema.json
Defines crack detection and characterization events from structural health monitoring including:
- Event identification and timestamp
- Location and component identification
- Detection method and sensor characteristics
- Crack characteristics (length, depth, growth rate)
- Severity classification and recommended actions
- Validation status and provenance

## Schema Features

All schemas include:
- **Version field** — Semantic versioning (e.g., "1.0.0")
- **Detailed descriptions** — Clear property documentation
- **Required fields** — Explicit required property lists
- **Validation rules** — Pattern matching, ranges, enums
- **Cross-references** — Links to related schemas

## Usage

### Validation
```bash
# Python
jsonschema -i artifact.json schema.schema.json

# JavaScript
ajv validate -s schema.schema.json -d artifact.json
```

### Integration
Reference schemas in artifacts using `$schema` property:
```json
{
  "$schema": "../../contracts/schemas/joint.schema.json",
  "version": "1.0.0",
  ...
}
```

## Standards Compliance

- JSON Schema Draft 2020-12
- Semantic versioning for schema evolution
- RESTful API compatibility

---

*Part of ATA-57-10 Wing Primary Structure — Configuration controlled under UTCS/QS v5.0*
