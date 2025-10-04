# CAS — Services in Operation

**Process**: In-service support and Technical Publications (S1000D).

## Purpose

This directory contains Services in Operation (CAS) artifacts including maintenance manuals, service bulletins, and illustrated parts data following S1000D standards.

## Artifact Types

- **Inputs**: S1000D DMRL, service feedback, maintenance data
- **Outputs**: AMM, SRM, IPD, EIS publications and bulletins
- **DISC codes**: AMM (Aircraft Maintenance Manual), SRM (Structural Repair Manual), IPD (Illustrated Parts Data), EIS (Equipment Information System)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAS5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
IPD-BWQ1-CAS5710-FWD-SPAR-IPD-941A-r003.xml
AMM-BWQ1-CAS5710-WING-INSPECTION-32-10-00-r002.sgml
SRM-BWQ1-CAS5710-SPAR-REPAIR-51-20-05-r001.pdf
```

## File Extensions

Typical extensions: `xml`, `sgml`, `pdf`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
