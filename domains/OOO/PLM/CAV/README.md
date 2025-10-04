# CAV — Quality Verification & Validation

**Process**: V&V plans, execution, and certifications.

## Purpose

This directory contains Quality Verification & Validation (CAV) artifacts including inspection programs, measurement data, and certification documents.

## Artifact Types

- **Inputs**: CAD/CAE models, acceptance criteria, quality standards
- **Outputs**: QIF/DMIS programs, measurement results, certificates of conformance, MSA studies
- **DISC codes**: QIP (Quality Inspection Plan), QIF (Quality Information Framework), DMIS (Dimensional Measuring Interface Standard), MEAS (Measurement), MSA (Measurement System Analysis), CERT (Certificate)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAV5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
QIF-BWQ1-CAV5710-FWD-SPAR-GDTPMI-r003.qif
DMIS-BWQ1-CAV5710-FRAME-INSPECTION-r002.dmis
CERT-BWQ1-CAV5710-MATERIAL-COC-AL7050-r001.pdf
```

## File Extensions

Typical extensions: `qif`, `dmis`, `csv`, `xml`, `pdf`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
