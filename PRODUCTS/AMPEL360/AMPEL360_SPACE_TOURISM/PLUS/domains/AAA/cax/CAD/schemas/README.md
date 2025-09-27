# CAD Domain JSON Schemas

This directory contains JSON schemas for validating CAD domain artifacts, ensuring consistent structure, compliance, and quality across all CAD-related files in the AMPEL360 PLUS space vehicle development.

## Purpose

Provides comprehensive validation schemas for CAD manifests and quantum optimization problems, enforcing PLUS naming conventions, UTCS compliance, and integration requirements across the entire CAD workflow.

## Schema Files

### `cad_manifest.schema.json`
**CAD Manifest Schema (v1.1)**

Validates CAD artifact metadata files with strict compliance requirements.

#### Key Features
- **Strict Validation**: `additionalProperties: false` prevents schema drift
- **PLUS Naming**: Enforces `PLUS-[A-Z0-9-]+` identifier patterns
- **Export Validation**: Path patterns for STEP/IGES/X_T files
- **ATA Integration**: Reference patterns for ATA-20/ATA-57 documents
- **UTCS Compliance**: Canonical hash and provenance tracking

#### Structure Overview
```json
{
  "id": "PLUS-OML-A02",
  "vehicle": "AMPEL360_PLUS", 
  "kind": "OML|STRUCTURE|TPS|INTERFACE|ASSEMBLY",
  "rev": "[A-Z][0-9]{2}",
  "status": "in-work|baseline|superseded",
  "exports": [{"path": "...", "format": "STEP|IGES|...", "purpose": "CFD|CAE|..."}],
  "refs": {"ata_practices": [...], "s1000d_dms": [...]},
  "geometry": {"bounding_box": {...}, "coordinate_system": "..."},
  "utcs": {"canonical_hash": "TBD|sha256:...", "provenance": "..."}
}
```

### `qox_problem.schema.json`
**QOx Problem Specification Schema (v1.1)**

Validates quantum optimization problem definitions for the CAx→QOx bridge.

#### Key Features
- **Variable Definitions**: Binary/integer/continuous variable pools
- **Multi-Objective**: Weighted objective function specification
- **Constraint Handling**: Penalty-based constraint encoding
- **Algorithm Config**: QAOA/VQE/Annealing parameter specification
- **Data Integration**: Links to geometry and analysis data sources
- **Hardware Specification**: Qubit requirements and backend selection

#### Structure Overview
```json
{
  "id": "PLUS-TPS-TILING-QUBO-001",
  "goal": "Problem description",
  "variables": {"x_i": {"count": 480, "domain": "binary", "meaning": "..."}},
  "objective": [{"term": "...", "weight": -2.0, "description": "..."}],
  "constraints": [{"type": "...", "weight": 8.0, "parameters": {...}}],
  "algorithm": {"type": "QAOA", "parameters": {...}, "hardware": {...}},
  "data_sources": {"coverage_matrix": "...", "thermal_loads": "..."},
  "utcs": {"canonical_hash": "TBD|sha256:...", "evidence_path": "..."}
}
```

## Validation Features

### Pattern Enforcement
- **IDs**: `^PLUS-[A-Z0-9-]+$` for all artifacts
- **Revisions**: `^[A-Z][0-9]{2}$` (e.g., A02, B15) 
- **File Paths**: Relative path validation with extension checking
- **Hash Values**: `^(TBD|sha256:[a-f0-9]{64})$` pattern
- **Versions**: Semantic versioning `^\d+\.\d+\.\d+$`

### Format Validation
- **Date/Time**: ISO 8601 format checking
- **Enums**: Controlled vocabularies for critical fields
- **Required Fields**: Mandatory properties for completeness
- **Type Safety**: Strict type checking (string, number, array, object)

### Domain-Specific Rules
- **CAD Formats**: STEP, IGES, Parasolid, STL, X_T support
- **Export Purposes**: CFD, CAE, Manufacturing, Visualization, Archive
- **Geometry Types**: OML, STRUCTURE, TPS, INTERFACE, ASSEMBLY
- **Algorithm Types**: QAOA, VQE, Annealing, QUBO
- **Hardware Backends**: simulator, ibm_quantum, dwave, rigetti, ionq, quantinuum, oqc

## Usage

### Validation Commands
```bash
# Validate CAD manifests
python ../scripts/validate_json.py . ../geometry/ ../structure/ ../tps/

# Validate QOx problems  
python ../scripts/validate_json.py . ../qox_bridge/

# Schema syntax validation
python -m json.tool cad_manifest.schema.json > /dev/null
python -m json.tool qox_problem.schema.json > /dev/null
```

### Integration with CI/CD
```yaml
# Pre-commit hook example
- id: cad-json-validation
  name: CAD JSON Schema Validation
  entry: python CAD/scripts/validate_json.py CAD/schemas CAD/geometry CAD/qox_bridge
  language: system
  files: 'CAD/.*\.json$'
```

### Development Workflow
1. **Create Artifact**: CAD manifest or QOx problem definition
2. **Schema Reference**: Include `$schema` property pointing to appropriate schema
3. **Local Validation**: Run validation scripts before commit
4. **Fix Issues**: Address any schema violations
5. **Commit**: Automatic validation via pre-commit hooks

## Schema Development

### Version Management
- **Semantic Versioning**: Schema versions follow semver (v1.0, v1.1, v2.0)
- **Backward Compatibility**: Additive changes in minor versions
- **Breaking Changes**: Major version increments for incompatible changes
- **Migration Guides**: Documentation for schema upgrades

### Extension Guidelines
- **Additive Changes**: New optional properties preferred
- **Controlled Evolution**: Schema changes via pull request review
- **Testing**: Validate against existing artifacts before merging
- **Documentation**: Update examples and usage guides

### Best Practices
- **Minimal Schemas**: Only define necessary constraints
- **Clear Descriptions**: Descriptive property documentation
- **Example Values**: Include examples in descriptions
- **Error Messages**: Schema violations should provide clear guidance

## Quality Assurance

### Schema Testing
```bash
# Test valid examples
jsonschema -i ../geometry/metadata/PLUS-OML-A02.cad.json cad_manifest.schema.json
jsonschema -i ../qox_bridge/problems/PLUS-TPS-TILING-QUBO-001.json qox_problem.schema.json

# Test invalid examples (should fail)
jsonschema -i test_invalid_manifest.json cad_manifest.schema.json
```

### Continuous Validation
- **Pre-commit**: Validate schema files on every commit
- **CI Pipeline**: Comprehensive validation in GitHub Actions
- **Release Gates**: Schema compliance required for releases
- **Monitoring**: Track schema violation rates and patterns

## Integration Points

### CAD Workflow
- **Design Phase**: CAD manifests for geometry tracking
- **Optimization**: QOx problems for quantum-enhanced design
- **Manufacturing**: Export validation for production readiness
- **Quality**: UTCS compliance for certification

### External Systems
- **PLM Integration**: Product lifecycle management systems
- **CAE/CFD Tools**: Analysis software integration
- **Manufacturing**: CAM and tooling systems
- **Documentation**: S1000D and ATA compliance

### Evidence Chain
- **Provenance**: Source document tracking
- **Canonical Hash**: Unique content identification
- **Evidence Path**: Quality assurance documentation
- **Audit Trail**: Complete change history

## Reference Implementation

### JSON Schema Validators
- **Python**: `jsonschema` library with Draft 2020-12 support
- **JavaScript**: `ajv` validator with full feature support  
- **Java**: `everit-org/json-schema` with format validation
- **Go**: `xeipuuv/gojsonschema` with custom formats

### Editor Integration
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "properties": {
    "$schema": {
      "enum": [
        "../../schemas/cad_manifest.schema.json",
        "../../schemas/qox_problem.schema.json"
      ]
    }
  }
}
```

### API Validation
```python
import jsonschema

# Load schemas
with open('schemas/cad_manifest.schema.json') as f:
    cad_schema = json.load(f)

# Validate manifest
validator = jsonschema.Draft202012Validator(cad_schema)
errors = list(validator.iter_errors(manifest_data))

if errors:
    for error in errors:
        print(f"Validation error: {error.message}")
```

## Future Enhancements

### Advanced Validation
- **Cross-Reference**: Validate file references and dependencies
- **Semantic Constraints**: Domain-specific business rules
- **Version Compatibility**: Multi-version schema support
- **Dynamic Validation**: Runtime constraint checking

### Tooling Integration
- **IDE Support**: Real-time validation in development environments
- **API Gateway**: Schema validation for REST endpoints
- **Database**: Schema-aware data storage and retrieval
- **Documentation**: Auto-generated docs from schemas

### Standards Alignment
- **OpenAPI**: Integration with API specification standards
- **JSON-LD**: Semantic web compatibility
- **SHACL**: RDF constraint language alignment
- **ISO Standards**: Alignment with CAD/CAM standards