# Valid Test Cases

IEF manifests that **should pass** schema validation.

## Test Files

### minimal.json

Minimal valid manifest with only required fields:

```json
{
  "ief_version": "0.1",
  "name": "ok",
  "type": "component",
  "exports": {
    "sbom": "sbom/component.spdx.json"
  }
}
```

**Tests:**
- ✅ Required `ief_version` field present
- ✅ Valid `type` enum value (`component`)
- ✅ Required `exports.sbom` field present
- ✅ No additional properties at root level

### full.json

Comprehensive manifest with all optional fields:

```json
{
  "ief_version": "0.1",
  "name": "ok-full",
  "type": "product",
  "exports": {
    "sbom": "sbom/widget.spdx.json",
    "docs": "docs/",
    "evidence": "evidence/"
  },
  "context": {
    "who": {"org": "ACME"}
  }
}
```

**Tests:**
- ✅ All required fields present
- ✅ Valid `type` enum value (`product`)
- ✅ Optional `exports.docs` and `exports.evidence` fields
- ✅ Optional `context` metadata object

## Expected Behavior

When running the test suite:

```bash
cd ../..
python run_tests.py
```

Both files should show:

```
✓ tests/conformance/valid/minimal.json
✓ tests/conformance/valid/full.json
```

## Adding Valid Tests

To add a new valid test case:

1. Create a JSON file in this directory
2. Ensure it conforms to `../../../schemas/context.schema.json`
3. Run `python ../../run_tests.py` to verify
4. The test runner auto-discovers new files

## References

- [Schema Examples](../../../schemas/examples/)
- [JSON Schema](../../../schemas/context.schema.json)
