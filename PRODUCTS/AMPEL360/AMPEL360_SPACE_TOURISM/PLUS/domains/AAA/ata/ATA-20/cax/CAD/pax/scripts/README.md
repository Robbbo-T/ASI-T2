# PAx Validation Scripts

This directory contains validation scripts for PAx (Packaging & Applications) manifests in the CAD domain, ensuring compliance with schemas, naming conventions, and evidence requirements.

## Purpose

Provides automated validation tools for CAD domain packaging manifests, supporting both development workflows and CI/CD pipelines with comprehensive error reporting and compliance checking.

## Scripts

### `validate_pax.py`
**PAx Manifest Validator (CAD Domain)**

Validates JSON/YAML packaging manifests against the PAx schema with CAD-specific rules and evidence checking.

#### Features
- **Schema Validation**: JSON Schema Draft 2020-12 with format checking
- **CAD Pattern Validation**: PLUS naming conventions and domain-specific rules
- **Evidence Verification**: SBOM, signatures, and file reference validation
- **Backward Compatibility**: Works with current and v1.1 schema formats
- **CI Integration**: Exit codes and structured error reporting

#### Usage
```bash
# Validate single manifest
python validate_pax.py manifest.json

# Validate multiple manifests
python validate_pax.py manifest1.json manifest2.yaml

# Schema-aware validation with custom schema
python validate_pax.py --schema ../schemas/package.schema.json manifest.json

# Directory scanning mode
python validate_pax.py --schema ../schemas/package.schema.json --root ../

# Strict file checking (CI mode)
PAX_STRICT_FILES=1 python validate_pax.py manifest.json
```

#### Validation Layers

1. **Schema Compliance**
   - JSON Schema validation with format checking
   - Required field verification
   - Type and pattern validation

2. **CAD-Specific Patterns**
   - Package names: `PLUS-CAD-[A-Z0-9-]+`
   - Canonical hash: `TBD|sha256:[a-f0-9]{64}`
   - Version format: Semantic versioning
   - Package kinds: OB-CAD-TOOL, OFF-CAD-EXPORTER, OFF-CAD-VALIDATOR

3. **Evidence Validation**
   - SBOM file presence and hash verification
   - Signature file validation (cosign, in-toto, x509)
   - Security policy compliance
   - CAD validation rules checking

4. **File Reference Validation**
   - SBOM file existence
   - Signature file presence
   - CAD export references (if specified)
   - Evidence path validation

#### Error Reporting
```
🔍 PAx Validation (CAD Domain)
Schema: /path/to/package.schema.json
==================================================

🔍 Validating: manifest.json
  ✅ Schema validation passed
  ✅ CAD patterns valid
  ✅ Evidence fields present
  ✅ Evidence patterns valid
  ⚠️  File reference validation failed: Missing files: ['sbom.json']
  ✅ MANIFEST.JSON - ALL VALIDATIONS PASSED

✅ SUCCESS: All PAx manifests validated successfully
```

#### Environment Variables
- **`PAX_STRICT_FILES`**: Set to `1` to fail on missing file references (CI mode)

#### Integration Points
- **Pre-commit Hooks**: Automatic validation on commit
- **CI/CD Pipelines**: Exit code compliance for automated workflows
- **Development**: Local validation before submission
- **Release Gates**: Quality assurance before deployment

## Development Guidelines

### Adding New Validations
1. **Schema Updates**: Modify `../schemas/package.schema.json`
2. **Pattern Validation**: Update CAD-specific validation functions
3. **Error Messages**: Ensure clear, actionable error descriptions
4. **Testing**: Validate against both valid and invalid manifests

### Error Handling
- **Graceful Degradation**: Continue validation on non-critical errors
- **Clear Messages**: Specific error locations and descriptions
- **CI-Friendly**: Structured output and appropriate exit codes
- **Debugging**: Verbose mode for troubleshooting

### Performance
- **Schema Caching**: Reuse parsed schemas across validations
- **File System**: Efficient file existence checking
- **Memory**: Streaming validation for large manifests
- **Parallelization**: Concurrent validation of multiple files

## Testing

### Test Manifests
Create test cases for:
- **Valid Manifests**: All validation layers pass
- **Schema Violations**: Missing fields, wrong types, invalid patterns
- **CAD Violations**: Invalid package names, wrong formats
- **Evidence Issues**: Missing SBOM, invalid signatures
- **File References**: Missing files, broken paths

### Validation Testing
```bash
# Test with valid manifest
python validate_pax.py test_valid.json

# Test with invalid manifest (should fail)
python validate_pax.py test_invalid.json && echo "ERROR: Should have failed"

# Test strict mode
PAX_STRICT_FILES=1 python validate_pax.py test_missing_files.json
```

## Dependencies

- **Python 3.8+**: Modern Python with type hints
- **jsonschema**: JSON Schema validation library
- **PyYAML**: YAML parsing for manifest files
- **pathlib**: Modern path handling
- **typing**: Type annotations for maintainability

## Integration

### CI/CD Pipeline
```yaml
- name: Validate PAx Manifests
  run: |
    python CAD/pax/scripts/validate_pax.py \
      --schema CAD/pax/schemas/package.schema.json \
      --root CAD/pax/
  env:
    PAX_STRICT_FILES: 1
```

### Pre-commit Hook
```yaml
- id: cad-pax-validation
  name: CAD PAx Package Validation
  entry: python CAD/pax/scripts/validate_pax.py
  language: system
  files: 'CAD/pax/.*\.(json|yaml|yml)$'
```

### Development Workflow
1. **Create Manifest**: Define package structure
2. **Local Validation**: `python validate_pax.py manifest.json`
3. **Fix Issues**: Address validation errors
4. **Evidence Generation**: Create SBOM and signatures
5. **Final Validation**: Ensure all checks pass
6. **Commit**: Automatic validation via pre-commit hooks