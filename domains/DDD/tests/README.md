# Tests — Domain Validation Test Suite

This directory contains automated tests for the domain's naming conventions and validation rules.

## Purpose

Validates that the linter correctly enforces naming conventions for all process trees (PLM, QUANTUM_OA, PAx, DELs).

## Files

### test_lint_names.py

pytest test suite with 4 test cases:

1. **test_ok_plm**: Validates correct PLM (CAx++) filenames pass
2. **test_ok_qoa**: Validates correct QUANTUM_OA filenames pass
3. **test_ok_pax**: Validates correct PAx filenames pass
4. **test_fail_ata_long**: Validates incorrect ATA codes are rejected

## Running Tests

### Run all tests in this domain
```bash
python3 -m pytest test_lint_names.py -v
```

### Run specific test
```bash
python3 -m pytest test_lint_names.py::test_ok_plm -v
```

### Run with coverage
```bash
python3 -m pytest test_lint_names.py --cov=../policy/lints --cov-report=term
```

## Test Structure

Tests create temporary sandbox directories to validate the linter:
- `sandbox_ok_plm/`: Valid PLM files
- `sandbox_ok_qoa/`: Valid QUANTUM_OA files
- `sandbox_ok_pax/`: Valid PAx files
- `sandbox_fail_ata/`: Invalid ATA code files

These sandbox directories are:
- Automatically created during test execution
- Automatically cleaned up after tests
- Excluded from version control via `.gitignore`

## CI Integration

These tests are run automatically by the CI workflow as part of the domain validation pipeline.

## Related Documentation

- Domain README: [../README.md](../README.md)
- Linter: [../policy/lints/lint_names.py](../policy/lints/lint_names.py)
- CI Workflow: [/.github/workflows/domains-filename-policy.yml](/.github/workflows/domains-filename-policy.yml)
