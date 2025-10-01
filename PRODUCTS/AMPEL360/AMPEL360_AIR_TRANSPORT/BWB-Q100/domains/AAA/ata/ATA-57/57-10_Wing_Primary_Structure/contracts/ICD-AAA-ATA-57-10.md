# ICD-AAA-ATA-57-10: Wing Primary Structure Interface Control Document

**Version:** 0.1.0  
**Date:** 2025-09-24  
**Status:** Baseline  
**Classification:** INTERNAL–EVIDENCE-REQUIRED

---

## Overview

This Interface Control Document (ICD) defines the data exchange interfaces, schemas, and contracts for ATA-57-10 Wing Primary Structure within the BWB-Q100 AAA domain.

## Scope

### Covered Interfaces
- Structural design data (CAX/CAD → ATA-57-10)
- Analysis results (CAX/CAE → ATA-57-10)
- Manufacturing data (ATA-57-10 → PAx)
- S1000D data modules (ATA-57-10 → Documentation systems)
- Evidence and compliance data (ATA-57-10 → QS/UTCS)

### Related ICDs
- **ICD-57-10-53**: Wing-to-fuselage attachments
- **ICD-57-10-57-20**: Wing-to-control surfaces
- **ICD-57-10-57-50**: Wing systems provisions

## Data Schemas

All data exchange uses JSON Schema 2020-12 format with semantic versioning.

### Primary Schemas

#### joint.schema.json
Defines structural joint metadata including:
- Joint type (bolted, bonded, hybrid)
- Member references
- Attachment fitting linkage
- Fastener specifications
- Bondline parameters
- Design loads
- Acceptance metrics

#### laminate.stack.schema.json
Defines composite laminate layup including:
- Ply sequence and orientation
- Material system
- Thickness per ply
- Core properties
- Symmetry rules

#### fastener.set.schema.json
Defines fastener specifications including:
- Fastener type and material
- Diameter and grip length
- Torque specifications
- Quantity and installation requirements

#### attachment.fitting.schema.json
Defines primary attachment fittings including:
- Interface type (wing_box, fuselage, etc.)
- Material and process
- Fastener set references
- Allowables references

#### acceptance.metric.schema.json
Defines acceptance and inspection criteria including:
- Metric identification
- Target values and limits
- Measurement methods
- Evidence references

## Data Flow

```
CAD Model → wing_geometry.json (OML/IML definition)
            ↓
FEA Analysis → loads.json (Load cases and distributions)
            ↓
ATA-57-10 → joint_definitions/*.json (Joint designs)
         → laminate_stacks/*.json (Layup schedules)
         → manufacturing_plans/*.json (Build instructions)
            ↓
S1000D → DMC/*.xml (Technical publications)
PAx → packages/*.json (Deliverable packages)
QS → evidence/*.json (Certification evidence)
```

## Version Management

### Schema Versioning
All schemas include a `version` field following semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Incompatible changes
- **MINOR**: Backward-compatible additions
- **PATCH**: Backward-compatible fixes

### Compatibility Rules
- Producers must specify schema version in data files
- Consumers must validate against declared schema version
- Breaking changes require coordination across all affected systems

## Validation

### Schema Validation
All data files must validate against their declared schema before acceptance:
```bash
ajv validate -s joint.schema.json -r schemas/*.json -d data/joint_*.json
```

### Reference Validation
Cross-references between schemas must be validated:
- Fastener set references in joints must resolve
- Attachment fitting references must exist
- Evidence references must point to valid files

## Change Control

All schema changes require:
1. Pull request with impact analysis
2. Review by data architecture team
3. Coordination with affected system owners
4. Migration guide for breaking changes
5. MRB approval for major versions

## Quality Standards

### Required Fields
All data files must include:
- `version`: Schema version (SemVer)
- `id`: Unique identifier
- UTCS provenance information

### Evidence Requirements
For certification artifacts:
- Canonical hash (SHA-256)
- SBOM reference
- QS signature anchor
- Provenance chain

## Tools and Utilities

### Validation Scripts
- `scripts/validate_schemas.sh`: Schema self-validation
- `scripts/validate_data.sh`: Data validation against schemas
- `scripts/check_references.sh`: Cross-reference validation

### Conversion Tools
- `scripts/cad_to_json.py`: CAD model extraction
- `scripts/fea_to_json.py`: FEA results extraction
- `scripts/json_to_s1000d.py`: S1000D generation

## Support

### Documentation
- Schema reference: `contracts/schemas/README.md`
- Examples: `contracts/examples/`
- Migration guides: `contracts/migrations/`

### Contact
- **Data Architecture**: ASI-T Architecture Team
- **Schema Questions**: #ata-schemas Slack channel
- **Bug Reports**: GitHub Issues

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Data Architect | TBD | 2025-09-24 | TBD |
| Structural Engineering | TBD | 2025-09-24 | TBD |
| Quality Assurance | TBD | 2025-09-24 | TBD |

---

*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
