# CAE — Computer Aided Engineering

**Process**: Analysis and simulation (structures, fluids, multibody, EMC/EMI).

## Purpose

This directory contains Computer Aided Engineering (CAE) artifacts including FEM, CFD, multibody dynamics, and EMI simulation models and results.

## Artifact Types

- **Inputs**: CAD models, loads, boundary conditions
- **Outputs**: Solver models, simulation results, analysis reports
- **DISC codes**: FEM (Finite Element), CFD (Computational Fluid Dynamics), MBD (Multibody Dynamics), EMI (Electromagnetic Interference)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAE5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
FEM-BWQ1-CAE5710-FS-BOX-STAT-r006.inp
CFD-BWQ1-CAE5710-WING-CRUISE-MACH085-r012.cas
MBD-BWQ1-CAE5710-LANDING-GEAR-KINEMATICS-r003.dat
```

## File Extensions

Typical extensions: `inp`, `cdb`, `cas`, `dat`, `fem`, `nas`, `pdf`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
