# QAIM-2 Solver Pools

This directory contains solver pool implementations for Classical (CB), Cubic-bit (QB), and Quantum Computing (QC) execution layers.

## Overview

Solver pools manage and execute optimization problems using different computational paradigms:
- **CB (Classical Bit):** Traditional optimization solvers
- **QB (Cubic Bit):** Non-quantum 3D tensor lifting
- **QC (Quantum Computing):** Full quantum algorithms

## Components

### 1. CB Pool — Classical Solvers (`cb_pool.py`)

**TFA Layer:** CB (Classical Bit)

Manages classical optimization solvers for MIP, LP, and other standard problems.

**Supported Solvers:**

| Solver | Type | License | Best For |
|--------|------|---------|----------|
| Gurobi | Commercial MIP | Proprietary | Large-scale MIP, best performance |
| CBC | Open-source MIP | EPL | Medium-scale MIP, free |
| OR-Tools | Google CP/MIP | Apache 2.0 | Constraint programming, routing |
| GLPK | GNU LP/MIP | GPL | Small problems, lightweight |

**Usage:**
```python
from solvers.cb_pool import ClassicalSolverPool

cb_pool = ClassicalSolverPool(config)
result = await cb_pool.solve(problem, params)

print(f"Status: {result.status}")
print(f"Objective: {result.objective_value}")
print(f"Gap: {result.gap}")
```

**Configuration:**
```yaml
cb_solvers:
  - name: 'gurobi'
    enabled: true
    license: '/opt/gurobi/gurobi.lic'
    time_limit: 3600
    threads: 32
  - name: 'cbc'
    enabled: true
    time_limit: 1800
    threads: 16
```

**Performance Characteristics:**
- **Time:** Milliseconds to hours (problem-dependent)
- **Optimality:** Guaranteed optimal (within gap tolerance)
- **Scalability:** Up to millions of variables (Gurobi)

### 2. QB Pool — Cubic-Bit Solvers (`qb_pool.py`)

**TFA Layer:** QB (Cubic Bit)

**IMPORTANT:** QB ≠ qubit. QB is non-quantum 3D lifting (CB×CB×CB).

Implements tensor-based approximation methods for middle-scale problems.

**Methods:**

| Method | Description | Best For |
|--------|-------------|----------|
| Tensor Decomposition | Tucker/CP decomposition | Structured problems |
| Lifted Relaxation | Multi-dimensional lifting | Non-convex problems |

**Usage:**
```python
from solvers.qb_pool import CubicBitSolverPool

qb_pool = CubicBitSolverPool(config)
result = await qb_pool.solve(problem, params)

print(f"Iterations: {result.iterations}")
print(f"Objective: {result.objective_value}")
```

**Configuration:**
```yaml
qb_solvers:
  enabled: true
  methods:
    - 'tensor_decomposition'
    - 'lifted_relaxation'
  time_limit: 300
  gpu_enabled: true
```

**Performance Characteristics:**
- **Time:** Seconds to minutes
- **Optimality:** Near-optimal (typically < 5% gap)
- **Scalability:** Hundreds to thousands of variables
- **Hardware:** CPU or GPU acceleration

### 3. QC Gateway — Quantum Computing (`qc_gateway.py`)

**TFA Layer:** QC (Quantum Computing)

Full quantum computing interface with transposition/projection time.

**Providers:**

| Provider | Hardware | Algorithms | Access |
|----------|----------|------------|--------|
| IBM Quantum | Superconducting | QAOA, VQE | Cloud API |
| D-Wave | Quantum Annealing | Annealing | Cloud API |
| IonQ | Trapped Ion | QAOA, VQE | Cloud API |
| Rigetti | Superconducting | QAOA, VQE | Cloud API |

**Algorithms:**

| Algorithm | Type | Best For |
|-----------|------|----------|
| QAOA | Hybrid | Combinatorial optimization |
| VQE | Hybrid | Ground state problems |
| Quantum Annealing | Adiabatic | QUBO problems |

**Usage:**
```python
from solvers.qc_gateway import QuantumGateway

qc_gateway = QuantumGateway(config)
result = await qc_gateway.solve(problem, params)

print(f"Quantum time: {result.quantum_time}s")
print(f"Classical time: {result.classical_time}s")
print(f"Shots: {result.shots}")
```

**Configuration:**
```yaml
qc_gateway:
  enabled: true
  providers:
    - name: 'ibm_quantum'
      backend: 'ibmq_qasm_simulator'
      shots: 8192
      token_file: '/keys/ibm_token'
    - name: 'dwave'
      solver: 'Advantage_system6.1'
      num_reads: 1000
      token_file: '/keys/dwave_token'
  algorithms:
    - 'qaoa'
    - 'vqe'
    - 'quantum_annealing'
```

**Performance Characteristics:**
- **Time:** Seconds to minutes (queue + execution)
- **Optimality:** Approximate (gap varies)
- **Scalability:** Limited by qubit count (< 100 qubits typically)
- **Cost:** Pay-per-use (shots/minutes)

## Solver Selection

### Automatic Selection

The orchestrator selects solvers using AI bridges:

1. **PCAN** canonicalizes problem
2. **SM** extracts features
3. **SP** recommends solver
4. **ARB** refines selection
5. **XFR** translates to solver format

### Manual Selection

Specify solver in parameters:

```python
parameters = {
    'solver': 'cb_gurobi',  # Force specific solver
    'time_limit': 60
}
```

### Selection Criteria

| Problem Size | Complexity | Time Budget | Recommended |
|--------------|-----------|-------------|-------------|
| Small (< 50 vars) | Any | Any | CB (Gurobi/CBC) |
| Medium (50-500) | High | Minutes | QB (Tensor) |
| Large (> 500) | Low | Hours | CB (Gurobi) |
| Large (> 500) | High | Minutes | QB (Lifted) |
| Any | QUBO-compatible | Research | QC (QAOA) |

## Result Objects

### SolverResult (CB)

```python
{
    'status': 'optimal',
    'solution': {'x1': 1.0, 'x2': 2.0},
    'objective_value': 10.5,
    'gap': 0.0,
    'solve_time': 2.3,
    'feasible': True
}
```

### QBResult (QB)

```python
{
    'status': 'optimal',
    'solution': {'x1': 1.0, 'x2': 2.0},
    'objective_value': 10.8,
    'gap': 0.02,
    'solve_time': 1.5,
    'feasible': True,
    'iterations': 42
}
```

### QCResult (QC)

```python
{
    'status': 'optimal',
    'solution': {'x1': 1, 'x2': 0},
    'objective_value': 9.8,
    'gap': 0.05,
    'solve_time': 15.2,
    'feasible': True,
    'shots': 8192,
    'quantum_time': 2.1,
    'classical_time': 13.1
}
```

## Error Handling

All solver pools handle:
- **Timeout:** Return best solution found
- **Infeasibility:** Report infeasible status
- **Solver unavailable:** Fallback to alternative
- **License errors:** Clear error messages

```python
try:
    result = await cb_pool.solve(problem, params)
except ValueError as e:
    print(f"Configuration error: {e}")
except TimeoutError as e:
    print(f"Solver timeout: {e}")
```

## Testing

```bash
# Run solver pool tests
pytest tests/test_solvers.py -v

# Test specific solver
pytest tests/test_solvers.py::test_cb_gurobi -v

# Test QB methods
pytest tests/test_solvers.py::test_qb_tensor -v

# Test QC gateway
pytest tests/test_solvers.py::test_qc_qaoa -v
```

## Performance Benchmarks

See `IMPLEMENTATION_SUMMARY.md` Appendix D for detailed benchmarks.

**Quick Reference:**

| Solver | Problem Size | Time | Gap |
|--------|-------------|------|-----|
| Gurobi | 100 vars | 0.8s | 0.0% |
| CBC | 100 vars | 12.3s | 0.5% |
| QB Tensor | 50 vars | 2.1s | 1.5% |
| QAOA | 20 vars | 15.2s | 3.2% |

## Extending Solver Pools

### Adding New Classical Solver

1. Add solver to `cb_pool.py`
2. Implement `_solve_<solver>` method
3. Update configuration schema
4. Add tests

### Adding New QB Method

1. Add method to `qb_pool.py`
2. Implement solver logic
3. Update configuration
4. Add tests

### Adding New QC Provider

1. Add provider to `qc_gateway.py`
2. Implement provider connection
3. Add authentication
4. Add tests

## References

- [MASTER_WHITEPAPER_4.md](../../WHITEPAPERS/MASTER_WHITEPAPER_4.md) - Solver specifications
- [API.md](../docs/API.md) - Solver selection API
- [OPERATIONS.md](../docs/OPERATIONS.md) - Solver pool management

---

*QAIM-2 Solver Pools*  
*CB: Classical | QB: Cubic-bit (non-quantum) | QC: Quantum*  
*Version: 0.1.0*
