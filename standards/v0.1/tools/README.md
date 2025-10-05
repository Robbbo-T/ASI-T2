# IEF v0.1 Tools

Command-line tools for validating manifests and generating checksums.

## Tools

### validate_manifest.py

Validates IEF context manifests against the JSON Schema and checks file references.

**Usage:**

```bash
python validate_manifest.py <path/to/context.manifest.json>
```

**What it checks:**

1. **JSON parsing** - File is valid JSON
2. **Schema validation** - Conforms to `../schemas/context.schema.json`
   - Required fields present
   - Valid types and enum values
   - No additional properties (strict mode)
3. **Path resolution** - Files referenced in `exports.*` exist
   - `exports.sbom` path resolves and file exists
   - `exports.docs` path resolves (if present)
   - `exports.evidence` path resolves (if present)

**Exit codes:**

- `0` - Manifest is valid and all referenced files exist
- `1` - Schema validation failed or referenced files missing
- `2` - Usage error (file not found, wrong arguments)

**Example output:**

```bash
# Success
$ python validate_manifest.py ../../IDEALE/context.manifest.json
OK: manifest valid and export paths exist

# Schema error
$ python validate_manifest.py invalid.json
Schema error at $: 'ief_version' is a required property

# Missing file
$ python validate_manifest.py manifest.json
Missing export path sbom: sbom/missing.spdx.json
```

### generate_checksums.sh

Creates reproducible SHA-256 checksums for files and directories.

**Usage:**

```bash
./generate_checksums.sh <path> [<path>...]
```

**Features:**

- Accepts files and directories as arguments
- Recursively processes directories
- Sorts paths deterministically (`LC_ALL=C`)
- Creates `checksums.sha256` in current directory
- Compatible with `sha256sum -c checksums.sha256`

**Example:**

```bash
# Generate checksums for manifest and SBOM directory
$ ./generate_checksums.sh context.manifest.json sbom/
Wrote checksums.sha256

# Verify checksums
$ sha256sum -c checksums.sha256
context.manifest.json: OK
sbom/component.spdx.json: OK
```

**Reproducibility:**

The script ensures checksums are reproducible by:
- Using `LC_ALL=C` for consistent sorting
- Processing files in lexicographic order
- Creating stable output format

## CI Integration

Both tools integrate with GitHub Actions:

```yaml
- name: Validate manifest
  run: |
    python standards/v0.1/tools/validate_manifest.py IDEALE/context.manifest.json
```

## Requirements

**validate_manifest.py:**
- Python 3.7+
- `jsonschema` package: `pip install jsonschema`

**generate_checksums.sh:**
- Bash
- `sha256sum` (standard on Linux)
- `find`, `sort`, `xargs` (POSIX utilities)

## References

- [IEF Specification](../README.md)
- [JSON Schema](../schemas/context.schema.json)
- [Verify Spec](../specs/VERIFY-SPEC.md)
