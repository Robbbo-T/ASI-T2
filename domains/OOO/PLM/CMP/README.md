# CMP — CAMPost (Services Post Operations)

**Process**: Post-operation services (disassembly, recycling, treatment, ESG compliance).

## Purpose

This directory contains CAMPost (CMP) artifacts for end-of-life management, including disassembly procedures, recycling documentation, and ESG compliance records.

## Artifact Types

- **Inputs**: BOM/traceability data, regulatory requirements
- **Outputs**: EoL reports, recycling procedures, treatment documentation, material recovery certificates
- **DISC codes**: EPR (Extended Producer Responsibility), RECY (Recycling), TREAT (Treatment), DISP (Disposal), MATREC (Material Recovery), CERT (Certificate)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CMP5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
RECY-BWQ1-CMP5710-FWD-SPAR-MATREC-AL7050-98PCT-r003.csv
EPR-BWQ1-CMP5710-WING-EOL-DISASSEMBLY-r001.pdf
TREAT-BWQ1-CMP5710-COMPOSITE-DISPOSAL-r002.xml
```

## File Extensions

Typical extensions: `pdf`, `csv`, `xml`, `json`

## Note

CAS is for in-service operation; CMP is for post-operation (End-of-Life).

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
