# IEF v0.1 Schemas

This directory contains the JSON Schema definition and examples for IEF context manifests.

## Files

- **context.schema.json** - JSON Schema Draft 7 specification for IEF v0.1 context manifests
  - Defines required fields: `ief_version`, `name`, `type`, `exports`
  - Enforces strict validation with `additionalProperties: false`
  - Schema ID: `https://ideale.eu/ief/v0.1/context.schema.json`

- **examples/** - Reference implementations showing valid manifest formats
  - `minimal.json` - Minimal valid manifest with required fields only
  - `full.json` - Full-featured manifest with all optional fields

## Usage

Validate a manifest against the schema:

```bash
python ../tools/validate_manifest.py path/to/manifest.json
```

Or use directly with a JSON Schema validator:

```python
import json
from jsonschema import Draft7Validator

schema = json.load(open('context.schema.json'))
manifest = json.load(open('your-manifest.json'))
Draft7Validator(schema).validate(manifest)
```

## Schema Details

**Required Fields:**
- `ief_version` - Must be `"0.1"` (string constant)
- `name` - Component/product identifier (string, min length 1)
- `type` - One of: `component`, `product`, `service`
- `exports.sbom` - Relative path to SPDX 2.3 SBOM file (string, min length 1)

**Optional Fields:**
- `exports.docs` - Path to documentation directory
- `exports.evidence` - Path to evidence directory
- `context` - Metadata object with who/what/where/when/why

## References

- [Main IEF Specification](../README.md)
- [JSON Schema Draft 7](https://json-schema.org/draft-07/schema)
