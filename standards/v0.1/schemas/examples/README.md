# IEF v0.1 Manifest Examples

This directory contains reference examples of valid IEF context manifests.

## Examples

### minimal.json

The simplest valid IEF manifest with only required fields:

```json
{
  "ief_version": "0.1",
  "name": "widget-core",
  "type": "component",
  "exports": {
    "sbom": "sbom/widget-core.spdx.json"
  }
}
```

**Use when:**
- Starting with IEF adoption
- Simple component packaging
- Minimal compliance requirements

### full.json

A comprehensive manifest showing all optional fields:

```json
{
  "ief_version": "0.1",
  "name": "widget-suite",
  "type": "product",
  "exports": {
    "sbom": "sbom/widget-suite.spdx.json",
    "docs": "docs/",
    "evidence": "evidence/"
  },
  "context": {
    "who": { "org": "ACME", "team": "Core" },
    "what": { "tag": "v1.2.3" },
    "where": { "region": "EU" },
    "when": { "built": "2025-10-05T12:00:00Z" },
    "why": { "objective": "release" }
  }
}
```

**Use when:**
- Full traceability needed
- Multiple evidence types (docs, evidence packs)
- Rich metadata requirements
- Production releases

## Validation

Both examples pass schema validation:

```bash
cd ../../tests
python run_tests.py
# Output: ✓ tests/conformance/valid/minimal.json
#         ✓ tests/conformance/valid/full.json
```

## Creating Your Own

1. Copy `minimal.json` as a starting point
2. Update `name`, `type`, and `exports.sbom` for your component
3. Add optional fields as needed
4. Validate: `python ../../tools/validate_manifest.py your-manifest.json`

## References

- [Context Manifest Specification](../../README.md#1-context-manifest-baseline)
- [JSON Schema](../context.schema.json)
