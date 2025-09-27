# PAx Package Schemas

This directory contains JSON schemas for validating PAx (Packaging & Applications) manifests in the CAD domain, ensuring consistent structure and compliance for both on-board and off-board package definitions.

## Purpose

Provides strict schema validation for CAD domain packaging manifests, enforcing UTCS/QS evidence requirements, ARINC compliance for on-board systems, and OCI standards for off-board containers.

## Schema Files

### `package.schema.json`
**CAD Domain Package Manifest Schema (v1.1)**

Validates packaging manifests for CAD tools and services with:
- **UTCS Header**: Canonical identification and provenance
- **Package Definition**: CAD-specific capabilities and interfaces
- **Security Policies**: Signing, constraints, and sanitization
- **Evidence Chain**: SBOM, signatures, and attestations

## Schema Structure

### UTCS Header
```json
"utcs_header": {
  "id": "ASIT-PLUS-CAD-...",
  "project": "PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM",
  "version": "semver format",
  "canonical_hash": "TBD|sha256:...",
  "bridge": "CB→QB→UE→FE→FWD→QS"
}
```

### Package Types
- **`OB-CAD-TOOL`**: On-board CAD visualization/processing
- **`OFF-CAD-EXPORTER`**: Off-board export and conversion
- **`OFF-CAD-VALIDATOR`**: Validation and compliance checking

### CAD-Specific Properties
```json
"cad_specific": {
  "supported_formats": ["STEP", "IGES", "X_T", "STL"],
  "geometry_types": ["OML", "STRUCTURE", "TPS", "INTERFACE"],
  "validation_rules": [...],
  "export_presets": {...}
}
```

### Evidence Requirements
```json
"evidence": {
  "canonical_hash": "sha256:...",
  "sbom": {"path": "...", "hash": "...", "format": "SPDX|CycloneDX"},
  "signatures": [{"type": "cosign|in-toto|x509", "path": "..."}],
  "cad_validation": {
    "geometry_checks": [...],
    "naming_compliance": true,
    "schema_validation": true
  }
}
```

## Validation Features

### Strict Validation
- **`additionalProperties: false`** - Prevents schema drift
- **Pattern Matching**: PLUS naming conventions, semantic versioning
- **Format Checking**: Dates, URIs, hash values
- **Enum Constraints**: Controlled vocabularies for critical fields

### CAD Domain Rules
- **Package Names**: `^PLUS-CAD-[A-Z0-9-]+$` pattern
- **CAD Systems**: CATIA, NX, Fusion360, SolidWorks, Generic
- **File Formats**: Standardized CAD export formats
- **Geometry Types**: OML, STRUCTURE, TPS, INTERFACE, ASSEMBLY

### UTCS/QS Integration
- **Canonical Hash**: `TBD|sha256:[a-f0-9]{64}` pattern
- **Bridge Specification**: `CB→QB→UE→FE→FWD→QS` exact match
- **Ethics Guard**: MAL-EEM compliance
- **LLC Classification**: SYSTEMS, COMPONENTS, QUBITS, etc.

## Usage

### Validation Command
```bash
# Validate specific manifest
python ../scripts/validate_pax.py --schema package.schema.json manifest.json

# Validate all manifests in directory
python ../scripts/validate_pax.py --schema package.schema.json --root ../
```

### Schema Development
```bash
# Validate schema syntax
python -m json.tool package.schema.json > /dev/null

# Test against example manifests
jsonschema -i ../OB/manifests/example.json package.schema.json
```

## Integration

### CI/CD Validation
- **Pre-commit Hooks**: Automatic validation on commit
- **GitHub Actions**: Continuous validation in pull requests
- **Release Gates**: Schema compliance required for releases

### Development Workflow
1. **Create Manifest**: Define package using schema structure
2. **Validate**: Run schema validation locally
3. **Evidence**: Generate SBOM and signatures
4. **Quality**: UTCS canonical hash assignment
5. **Deploy**: Package ready for distribution

## Schema Evolution

### Version Management
- **Semantic Versioning**: Schema versions follow semver
- **Backward Compatibility**: Additive changes preferred
- **Breaking Changes**: Major version increments with migration guide

### Extension Points
- **Custom Properties**: Domain-specific additions in controlled namespaces
- **Validation Rules**: Additional constraints via JSON Schema extensions
- **Format Support**: New CAD formats via enum updates

## References

- **JSON Schema**: [Draft 2020-12](https://json-schema.org/draft/2020-12/schema)
- **UTCS Standards**: Unified Traceability and Compliance System
- **PAx Framework**: Packaging & Applications methodology
- **CAD Standards**: STEP (ISO 10303), IGES, Parasolid specifications