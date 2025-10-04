# Lints — Naming Convention Validators

This directory contains automated linters that enforce naming conventions for the domain.

## Purpose

The linter validates filenames according to their location in the domain tree:
- **PLM/**: CAx++ naming pattern validation
- **QUANTUM_OA/**: QOA naming pattern validation
- **PAx/**: Packaging naming pattern validation
- **DELs/**: Deliveries naming pattern validation

## Files

### lint_names.py

The main linter script that validates filenames based on tree location.

**Usage:**
```bash
# Validate entire domain
python3 lint_names.py ../../

# Validate specific subdirectory
python3 lint_names.py ../../PLM/CAD/
```

**Environment Variables:**
- `ENFORCED_ROOT`: Override the root directory for validation (useful for CI/CD)

**Exit Codes:**
- `0`: All files pass validation
- `1`: One or more files fail validation

## Validation Rules

The linter uses regex patterns to validate filenames:

1. **PLM (CAx++)**: `<DISC>-<MIC>-<DOMAIN><ATA>-<SCOPE>-...-r<REV>.<EXT>`
2. **QUANTUM_OA**: `<ALG>-<MIC>-QOA<ATA>-<SCOPE>-...-r<REV>.<EXT>`
3. **PAx**: `PAX-<MIC>-PKG<ATA>-<SCOPE>-<TYPE>-r<REV>.<EXT>`
4. **DELs**: `<DISC>-<MIC>-REL<ATA>-<SCOPE>-<TAG>-r<REV>.<EXT>`

Files in `policy/` and `tests/` directories are ignored.

## CI Integration

This linter is automatically run by the CI workflow:
`.github/workflows/domains-filename-policy.yml`

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- Naming Conventions: [../../README.md#naming-conventions](../../README.md#naming-conventions)
