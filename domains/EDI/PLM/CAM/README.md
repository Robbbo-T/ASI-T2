# CAM — Computer Aided Manufacturing

**Process**: Manufacturing planning and programming.

## Purpose

This directory contains Computer Aided Manufacturing (CAM) artifacts including NC programs, tooling definitions, and manufacturing process plans.

## Artifact Types

- **Inputs**: CAD models, manufacturing routes, tooling specifications
- **Outputs**: NC code, APT programs, process sheets, tooling designs
- **DISC codes**: NC (Numerical Control), APT (Automatically Programmed Tools), OPR (Operation), FIX (Fixture), TOOL (Tooling), SET (Setup)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAM5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
NC-BWQ1-CAM5710-FWD-SPAR-OP30-DRILL-r002.nc
APT-BWQ1-CAM5710-RIB-MACHINING-PATH-r005.apt
OPR-BWQ1-CAM5710-ASSEMBLY-SEQUENCE-r001.pdf
```

## File Extensions

Typical extensions: `nc`, `eia`, `apt`, `cl`, `cls`, `csv`, `pdf`, `step`, `stp`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
