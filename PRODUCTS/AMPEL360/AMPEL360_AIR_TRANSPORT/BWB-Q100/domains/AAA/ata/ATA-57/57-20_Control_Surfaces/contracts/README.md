# Contracts

This directory contains JSON schemas, interface control documents (ICDs), and configuration management artifacts for ATA-57-20 Control Surfaces.

## Purpose

The contracts directory provides:
- JSON schema definitions for control surface artifacts
- Schema versioning and change management
- Example JSON instances demonstrating usage
- Interface specifications with other systems
- Contract validation and enforcement

## Contents

### schemas/
JSON Schema (Draft 2020-12) definitions:
- **acceptance.metric.schema.json** - Acceptance/inspection metrics
- **control_surface.schema.json** - Control surface structures
- **hinge.schema.json** - Hinge assemblies
- **actuator_attachment.schema.json** - Actuator interfaces
- **balance_weight.schema.json** - Mass balance weights

### examples/
Validated JSON instances organized by type:
- **control_surface/** - Elevon/flaperon/spoiler examples
- **hinge/** - Hinge assembly examples
- **actuator_attachment/** - Actuator interface examples
- **balance_weight/** - Balance weight examples

### ICD-AAA-ATA-57-20.md
Master contract document defining:
- Schema versioning (SemVer)
- Breaking vs. non-breaking changes
- Migration procedures
- UTCS/QS integration
- Quality sealing requirements

## Schema Versioning

All schemas follow semantic versioning:
- **Major** version: Breaking changes
- **Minor** version: Backward-compatible additions
- **Patch** version: Clarifications and fixes

Breaking changes require:
- MRB approval
- Migration guide
- Update of all dependent instances
- Coordination with downstream systems (PAX, UTCS, QS)

## Validation

### Schema Validation
```bash
# Validate schema syntax
python -m json.tool schema.json > /dev/null

# Validate instance against schema
jsonschema -i example.json schema.json
```

### CI/CD Integration
All JSON instances must validate before:
- Deployment to PAX
- Quality sealing (QS)
- Configuration baseline updates

## Usage

### Creating New Instances
1. Reference appropriate schema in `$schema` property
2. Follow naming conventions (ID prefix patterns)
3. Include `version` and `effectivity_expr`
4. Validate against schema
5. Add to version control

### Updating Schemas
1. Determine version bump type (major/minor/patch)
2. Update ICD-AAA-ATA-57-20.md
3. Create migration guide if breaking change
4. Update all dependent instances
5. Coordinate with stakeholders

## Related Directories

- **../evidence/** - Evidence references for acceptance metrics
- **../io/** - UTCS/QS routing manifest
- **../S1000D/** - S1000D data modules

---
*Part of ATA-57-20 Control Surfaces contract framework.*
