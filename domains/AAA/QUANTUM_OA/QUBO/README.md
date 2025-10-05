# Quadratic Unconstrained Binary Optimization

**Process**: Quantum optimization and approximation algorithms.

## Purpose

This directory contains Quadratic Unconstrained Binary Optimization optimization artifacts including problem formulations, solution runs, and validation results.

## Naming Convention

Files in this directory follow the QUANTUM_OA naming pattern:

```
<ALG>-<MIC>-QOA5710-<SCOPE>-<DATASET?>-<STAGE?>-r<REV>.<EXT>
```

Where `<ALG>` for this directory is: **QUBO**

### Examples

```
QUBO-BWQ1-QOA5710-FWD-SPAR-OPT-DEV-r001.py
QUBO-BWQ1-QOA5710-LAYOUT-ROUTING-DS-BENCH01-r003.json
QUBO-BWQ1-QOA5710-STRUCTURAL-OPT-PROD-r005.ipynb
```

## File Extensions

Typical extensions: `py`, `ipynb`, `qasm`, `json`, `yaml`, `yml`, `csv`, `lp`, `mps`, `qubo`, `dimacs`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- QUANTUM_OA Process: [../../README.md#quantum_oa](../../README.md#quantum_oa)
