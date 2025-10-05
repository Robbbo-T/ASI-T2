# Invalid Test Cases

IEF manifests that **should fail** schema validation.

## Test Files

### no-version.json

Missing required `ief_version` field:

```json
{
  "name": "bad",
  "type": "component",
  "exports": { "sbom": "sbom/x.spdx.json" }
}
```

**Expected error:**
- ❌ `'ief_version' is a required property`

### bad-type.json

Invalid `type` enum value:

```json
{
  "ief_version": "0.1",
  "name": "bad",
  "type": "library",
  "exports": { "sbom": "sbom/x.spdx.json" }
}
```

**Expected error:**
- ❌ `'library' is not one of ['component', 'product', 'service']`

## Expected Behavior

When running the test suite:

```bash
cd ../..
python run_tests.py
```

Both files should show:

```
✗ tests/conformance/invalid/bad-type.json  [EXPECTED FAIL]
✗ tests/conformance/invalid/no-version.json  [EXPECTED FAIL]
```

The test runner expects these to fail and counts them as passing tests.

## Adding Invalid Tests

To add a new invalid test case:

1. Create a JSON file that violates the schema
2. Add it to this directory
3. Run `python ../../run_tests.py` to verify it's caught
4. Document the expected error in this README

## Common Schema Violations

Test cases should cover:

- ✅ Missing required fields (`ief_version`, `name`, `type`, `exports`)
- ✅ Invalid enum values (e.g., `type: "library"`)
- ⚠️ Wrong value types (e.g., `ief_version: 0.1` as number)
- ⚠️ Additional properties at root level
- ⚠️ Invalid nested structure

## References

- [JSON Schema](../../../schemas/context.schema.json)
- [Valid Test Cases](../valid/README.md)
