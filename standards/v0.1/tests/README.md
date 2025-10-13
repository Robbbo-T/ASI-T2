# IEF v0.1 Conformance Tests

Automated test suite for validating IEF v0.1 schema compliance.

## Test Runner

**run_tests.py** - Validates test manifests against the JSON Schema and reports results.

```bash
python run_tests.py
```

Expected output:

```
✓ tests/conformance/valid/minimal.json
✓ tests/conformance/valid/full.json
✗ tests/conformance/invalid/bad-type.json  [EXPECTED FAIL]
✗ tests/conformance/invalid/no-version.json  [EXPECTED FAIL]
PASS: 2 valid, 2 invalid caught
```

Exit codes:
- `0` - All tests pass (valid accepted, invalid rejected)
- `1` - Test failures detected

## Test Structure

```
tests/
├── run_tests.py              # Test runner
└── conformance/
    ├── valid/                # Should pass schema validation
    │   ├── minimal.json      # Minimal required fields
    │   └── full.json         # All optional fields
    └── invalid/              # Should fail schema validation
        ├── no-version.json   # Missing required field
        └── bad-type.json     # Invalid enum value
```

## Test Cases

### Valid Manifests

Tests that **should pass** validation:

- **minimal.json** - Only required fields (`ief_version`, `name`, `type`, `exports.sbom`)
- **full.json** - All fields including optional `context` metadata

### Invalid Manifests

Tests that **should fail** validation:

- **no-version.json** - Missing required `ief_version` field
- **bad-type.json** - Invalid `type` value (not in enum)

## Running in CI

The test suite integrates with GitHub Actions via `.github/workflows/ief-verify.yml`:

```yaml
- name: Run IEF conformance tests
  run: |
    cd standards/v0.1/tests
    python run_tests.py
```

## Adding Tests

To add new test cases:

1. **Valid tests:** Add JSON to `conformance/valid/`
2. **Invalid tests:** Add JSON to `conformance/invalid/`
3. Run `python run_tests.py` to verify

The test runner automatically discovers all `*.json` files in these directories.

## References

- [JSON Schema](../schemas/context.schema.json)
- [IEF Specification](../README.md)
- [Validation Tool](../tools/validate_manifest.py)
