# Contract / ICD — ATA-57-20

JSON instance contracts, acceptance metrics, and routing to PAX/UTCS/QS. This ICD governs schema versions and breaking changes.

## Schema Versions

Current schema versions (SemVer):
- **acceptance.metric.schema.json**: 1.0.0
- **control_surface.schema.json**: 1.0.0
- **hinge.schema.json**: 1.0.0
- **actuator_attachment.schema.json**: 1.0.0
- **balance_weight.schema.json**: 1.0.0

## Schema Change Management

### Breaking Changes
Breaking changes (major version bump) require:
1. MRB approval
2. Update to all dependent JSON instances
3. Migration guide documentation
4. Coordination with downstream systems (PAX, UTCS, QS)

### Non-Breaking Changes
Non-breaking changes (minor/patch version bump):
- Additional optional fields
- Clarification of descriptions
- New enum values (with backward compatibility)
- Documentation improvements

## Contract Principles

### Version Pinning
All JSON instances must specify schema version:
```json
{
  "version": "1.0.0",
  "$schema": "../../schemas/control_surface.schema.json"
}
```

### Validation Requirements
- All instances must validate against their schema
- CI/CD pipelines must include schema validation
- Invalid instances block deployment to PAX

### Effectivity Management
- All configurable objects (CO) include effectivity expressions
- Effectivity tracked through MSN ranges, blocks, and option flags
- Changes to effectivity require configuration control

## UTCS/QS Integration

### Canonical Hashing
All finalized artifacts receive:
- SHA256 canonical hash
- SBOM reference
- Digital signature
- Timestamp

### Quality Sealing
QS anchors link:
- Design artifacts (JSON instances)
- Test evidence
- Inspection records
- Configuration status

## References

- Schema files: `./schemas/`
- Example instances: `./examples/`
- Routing manifest: `../io/routing.manifest.yaml`
- Evidence indexes: `../evidence/`

---
*Part of BWB-Q100 contract framework. Subject to configuration control.*
