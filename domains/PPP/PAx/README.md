# PAx — Packaging

**Process**: Packaging artifacts for on-board (OB) and off-board (OFF) deployment.

## Purpose

This directory contains packaging artifacts including binaries, source packages, documentation bundles, SBOMs, and manifests.

## Naming Convention

Files in this directory follow the PAx naming pattern:

```
PAX-<MIC>-PKG5710-<SCOPE>-<TYPE>-r<REV>.<EXT>
```

### Types

- **SRC**: Source code packages
- **BIN**: Binary/executable packages
- **DOCS**: Documentation packages
- **SBOM**: Software Bill of Materials
- **MANIFEST**: Package manifests
- **CHECKLIST**: Verification checklists
- **EVIDENCE**: Evidence packages

### Examples

```
PAX-BWQ1-PKG5710-FWD-SPAR-DOCS-r001.zip
PAX-BWQ1-PKG5710-FS-BOX-SBOM-r002.spdx.json
PAX-BWQ1-PKG5710-WING-MANIFEST-r003.json
PAX-BWQ1-PKG5710-ASSEMBLY-BIN-r004.tgz
```

## File Extensions

Typical extensions: `zip`, `tgz`, `tar.gz`, `json`, `xml`, `pdf`, `txt`, `csv`, `spdx.json`

## Validation

Run the linter to validate file names:
```bash
python3 ../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../README.md](../README.md)
- PAx Naming Convention: [../README.md#pax-pattern](../README.md#pax-pattern)
