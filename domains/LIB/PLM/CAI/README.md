# CAI — Computer Aided Installation & Integration

**Process**: Assembly installation and integration into higher-level systems.

## Purpose

This directory contains Computer Aided Installation & Integration (CAI) artifacts including installation procedures, interface definitions, and fit-check documentation.

## Artifact Types

- **Inputs**: CAD/CAE/CAM models, tooling, interface specifications
- **Outputs**: Installation instructions, fit-check reports, integration models
- **DISC codes**: INS (Installation), INT (Integration), FIT (Fit Check)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAI5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
INS-BWQ1-CAI5710-FWD-SPAR-INSTALL-GA-r001.pdf
INT-BWQ1-CAI5710-WING-FUSELAGE-INTERFACE-r003.step
FIT-BWQ1-CAI5710-SHIMMING-PROCEDURE-r002.docx
```

## File Extensions

Typical extensions: `pdf`, `step`, `dwg`, `json`, `docx`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
