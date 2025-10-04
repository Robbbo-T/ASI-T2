# CAD — Computer Aided Design

**Process**: 3D modeling, assemblies, and technical drawings.

## Purpose

This directory contains Computer Aided Design (CAD) artifacts including 3D models, assemblies, and 2D drawings for the domain.

## Artifact Types

- **Inputs**: CON/REQ/SYS specifications, geometric requirements
- **Outputs**: 3D parts, assemblies, technical drawings
- **DISC codes**: ASSY (Assembly), PRT (Part), DRW (Drawing)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAD5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step
PRT-BWQ1-CAD5710-RIB-STATION-200-LH-r008.sldprt
DRW-BWQ1-CAD5710-FRAME-DETAIL-A-r004.pdf
```

## File Extensions

Typical extensions: `step`, `stp`, `sldprt`, `sldasm`, `ipt`, `iam`, `dwg`, `dxf`, `pdf`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
