# Sheet CI

This directory contains continuous integration scripts and validation tooling for the UTCS v5.0 bundle.

## Purpose

Automated validation scripts that ensure:
- Manifest schema compliance
- File integrity (hash validation)
- Structure correctness
- Ethics guard configuration
- Crosswalk completeness

## Contents

### UTCS Validator

**File:** `validate_utcs.py`

**Language:** Python 3.8+

Comprehensive validation script with 7 check types:

1. **Basic Structure** — Bundle ID, schema version, semver, bridge format
2. **JSON Schema** — Full Draft 2020-12 compliance
3. **UiX Sections** — All six sections present (context, content, cache, structure, style, sheet)
4. **File References** — All manifest references exist
5. **File Hashes** — SHA-256 validation
6. **Ethics Guard** — MAL-EEM and MAP-EEM configured
7. **Crosswalk Completeness** — TFA grammar and topic hierarchy present

**Usage:**

```bash
# Basic validation
python validate_utcs.py --manifest ../manifest.utcs.yaml

# Full validation with crosswalk checks
python validate_utcs.py --manifest ../manifest.utcs.yaml --check-crosswalk

# From Makefile
cd ..
make validate       # Basic
make validate-full  # With crosswalk
make check         # All checks
```

**Exit Codes:**
- `0` — Validation passed
- `1` — Validation failed

**Output:**

```
======================================================================
UTCS v5.0 Bundle Validation
======================================================================
Manifest: ../manifest.utcs.yaml

Basic Structure................................... ✓ PASS
JSON Schema....................................... ✓ PASS
UiX Sections...................................... ✓ PASS
File References................................... ✓ PASS
File Hashes....................................... ✓ PASS
Ethics Guard...................................... ✓ PASS

✓ SUCCESS: UTCS bundle validated successfully
```

## Dependencies

```bash
pip install jsonschema PyYAML
```

Or use repository requirements:

```bash
pip install -r /path/to/ASI-T2/requirements.txt
```

## CI/CD Integration

This script is called by:

**GitHub Actions Workflow:** `.github/workflows/utcs-validate.yml`

```yaml
- name: Validate UTCS manifest
  run: |
    cd UTCS_BUNDLE
    python sheet/ci/validate_utcs.py --manifest manifest.utcs.yaml
```

**Makefile Targets:**
- `make validate` → Basic validation
- `make validate-full` → With crosswalk checks
- `make check` → All validations + schema checks

## Validation Rules

### Schema Validation

Uses JSON Schema Draft 2020-12 validator against `content/schemas/utcs.manifest.v5.json`.

### Hash Validation

- Algorithm: SHA-256
- Skips hashes marked as "pending"
- Compares computed hash with manifest entry
- Reports mismatches with first 8 chars of each hash

### Ethics Guard Validation

Ensures `ethics_guard` contains valid entries:
- MAL-EEM (Main Application Layer Ethics & Ethics Management)
- MAP-EEM (Master Application Platform Ethics & Ethics Management)

### Crosswalk Validation

Checks for required structure files:
- `structure/tfa_grammar.md` — Path grammar definition
- `structure/topic_hierarchy.md` — Topic mappings

Validates content includes key patterns:
- TFA grammar: `domains/<DOMAIN_CODE>/ATA-`
- Topic hierarchy: `MAP Topic` column header

## Development

### Adding New Validation Checks

1. Add validation function following pattern:
   ```python
   def validate_new_check(manifest: Dict[str, Any]) -> Tuple[bool, List[str]]:
       """Validate new aspect."""
       issues = []
       # validation logic
       return len(issues) == 0, issues
   ```

2. Add to validators list in `validate_bundle()`:
   ```python
   validators = [
       # ... existing validators
       ("New Check", lambda: validate_new_check(manifest)),
   ]
   ```

3. Test thoroughly before committing

## References

- [Master Whitepaper #3](../../context/MASTER_WHITEPAPER_3_UTCS.md) — §7 Validation & CI
- [Bundle README](../../README.md) — Quick start guide
- [Manifest Schema](../../content/schemas/utcs.manifest.v5.json) — Validation schema
- [GitHub Workflow](/.github/workflows/utcs-validate.yml) — CI integration
