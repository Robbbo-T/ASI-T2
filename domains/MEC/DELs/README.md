# DELs — Final Check & Deliveries

**Process**: Final verification and delivery packages.

## Purpose

This directory contains final delivery artifacts including release packages, manifests, checksums, signatures, and final check reports.

## Naming Convention

Files in this directory follow the DELs naming pattern:

```
<DISC>-<MIC>-REL5710-<SCOPE>-<TAG>-r<REV>.<EXT>
```

### DISC Types

- **DLV**: Deliverable package
- **FC**: Final Check report
- **REL**: Release artifact

### Tags

- **PKG**: Package file
- **MANIFEST**: Manifest document
- **CSUM**: Checksum file
- **SIG**: Digital signature
- **RPT**: Report document
- **NOTES**: Release notes

### Examples

```
DLV-BWQ1-REL5710-FWD-SPAR-PKG-r001.zip
FC-BWQ1-REL5710-FWD-SPAR-RPT-r002.pdf
REL-BWQ1-REL5710-FWD-SPAR-MANIFEST-r001.json
DLV-BWQ1-REL5710-WING-CSUM-r001.sha256
```

## File Extensions

Typical extensions: `zip`, `json`, `xml`, `pdf`, `txt`, `sha256`, `sig`

## Validation

Run the linter to validate file names:
```bash
python3 ../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../README.md](../README.md)
- DELs Naming Convention: [../README.md#dels-pattern](../README.md#dels-pattern)
