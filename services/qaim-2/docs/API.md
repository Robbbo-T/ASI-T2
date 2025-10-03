# QAIM-2 API Documentation

## Overview

QAIM-2 provides a REST API (future) and Python SDK for quantum-classical optimization across ASI-T2 products.

## Python SDK

### Installation

```python
# From the services directory
import sys
sys.path.append('/path/to/services')
from qaim_2.core import QAIM2Orchestrator
```

### Basic Usage

```python
import asyncio
import yaml
from qaim_2.core import QAIM2Orchestrator

# Load configuration
with open('config/deployment-edge.yaml') as f:
    config = yaml.safe_load(f)

# Create orchestrator
orchestrator = QAIM2Orchestrator(config)

# Define problem
problem = {
    'problem_type': 'vehicle_routing',
    'variables': [
        {'name': 'x1', 'type': 'binary'},
        {'name': 'x2', 'type': 'binary'}
    ],
    'constraints': [
        {'type': 'capacity', 'value': 100, 'unit': 'kg'}
    ],
    'objectives': [
        {'name': 'minimize_distance', 'sense': 'minimize'}
    ]
}

# Solve
result = await orchestrator.optimize(
    problem=problem,
    constraints={'time_limit': 60}
)

print(f"Status: {result['status']}")
print(f"Solution: {result['solution']}")
```

## REST API (Planned)

### POST /v1/optimize

Submit optimization request.

**Request:**
```json
{
  "problem_type": "vehicle_routing",
  "variables": [...],
  "constraints": [...],
  "objectives": [...],
  "parameters": {
    "solver": "auto",
    "time_limit": 60
  },
  "metadata": {
    "domain": "logistics",
    "ata_chapter": "ATA-34"
  }
}
```

**Response:**
```json
{
  "request_id": "uuid",
  "solver": "cb_gurobi",
  "solution": {...},
  "metrics": {
    "objective_value": 10.5,
    "gap": 0.01,
    "solve_time": 5.2,
    "feasible": true
  },
  "evidence": {
    "version": "utcs-v5.0",
    "provenance": {
      "bridge": "QS→FWD→UE→FE→CB→QB",
      "ethics": "MAP-EEM · MAL-EEM"
    }
  },
  "status": "optimal"
}
```

### GET /v1/evidence/{request_id}

Retrieve UTCS evidence for a request.

**Response:**
```json
{
  "version": "utcs-v5.0",
  "request_id": "uuid",
  "timestamp": "2025-10-03T12:00:00Z",
  "input_hash": "sha256...",
  "solver": {...},
  "solution": {...},
  "provenance": {...}
}
```

## Problem Types

### Supported Problem Types

- `vehicle_routing` - Vehicle Routing Problem (VRP)
- `scheduling` - Job shop, flow shop scheduling
- `layout` - Facility layout, placement problems
- `assignment` - Resource assignment
- `portfolio` - Portfolio optimization
- `resource_allocation` - Resource allocation
- `path_planning` - Path planning, routing
- `bin_packing` - Bin packing
- `knapsack` - Knapsack variants
- `tsp` - Traveling Salesman Problem
- `general_mip` - General Mixed Integer Programming
- `general_qubo` - General QUBO problems

## Solver Selection

### Automatic Selection

When `parameters.solver = "auto"`, the AI bridges select the optimal solver:

1. **PCAN** canonicalizes the problem
2. **SM** extracts features using ML models
3. **SP** uses RL to select solver
4. **ARB** refines selection based on load
5. **XFR** translates to solver format

### Manual Selection

Specify solver explicitly:

```python
parameters = {
    'solver': 'cb_gurobi',  # or cb_cbc, qb_tensor, qc_qaoa, etc.
    'time_limit': 60,
    'gap_tolerance': 0.01
}
```

### Available Solvers

#### Classical (CB)
- `cb_gurobi` - Commercial MIP solver (license required)
- `cb_cbc` - Open-source MIP solver
- `cb_ortools` - Google OR-Tools
- `cb_glpk` - GNU Linear Programming Kit

#### Cubic-Bit (QB)
- `qb_tensor` - Tensor decomposition method
- `qb_lifted` - Lifted linear relaxation

#### Quantum (QC)
- `qc_qaoa` - Quantum Approximate Optimization Algorithm
- `qc_vqe` - Variational Quantum Eigensolver
- `qc_annealing` - Quantum Annealing (D-Wave)

## Configuration

### Edge Configuration

Minimal resources, classical solvers only:

```yaml
deployment: edge
cb_solvers:
  - name: 'cbc'
    enabled: true
    time_limit: 10
```

### Site Configuration

Mixed portfolio with QB:

```yaml
deployment: site
cb_solvers:
  - name: 'cbc'
  - name: 'ortools'
qb_solvers:
  enabled: true
  methods: ['tensor_decomposition']
```

### Hub Configuration

Full suite including quantum:

```yaml
deployment: hub
cb_solvers: [gurobi, cbc, ortools, glpk]
qb_solvers:
  enabled: true
qc_gateway:
  enabled: true
  providers: [ibm_quantum, dwave]
```

## Evidence & Provenance

Every optimization generates UTCS v5.0 evidence:

```python
evidence = result['evidence']
print(evidence['version'])  # 'utcs-v5.0'
print(evidence['input_hash'])  # SHA-256 hash
print(evidence['provenance']['bridge'])  # 'QS→FWD→UE→FE→CB→QB'
```

### Verification

```bash
# Verify evidence integrity
utcs verify evidence.json

# Verify cryptographic signature
cosign verify --key public.pem evidence.json
```

## Metadata & Traceability

### ATA Chapter Mapping

```python
metadata = {
    'ata_chapter': 'ATA-34',  # Navigation
    'domain': 'IIS'  # Integration/Intelligence
}
```

### S1000D References

```python
metadata = {
    's1000d_refs': [
        'DMC-BWB-A-34-00-00-00A-040A-A',
        'DMC-BWB-A-34-10-00-00A-040A-A'
    ]
}
```

## Error Handling

```python
result = await orchestrator.optimize(problem, constraints)

if result['status'] == 'error':
    print(f"Error: {result['metrics']['error']}")
elif result['status'] == 'timeout':
    print("Solver timed out")
elif result['status'] == 'infeasible':
    print("Problem is infeasible")
else:
    print(f"Solution: {result['solution']}")
```

## Performance Tuning

### Time Limits

```python
constraints = {
    'time_limit': 60,  # seconds
    'gap_tolerance': 0.01  # 1% gap
}
```

### Thread Control

```python
parameters = {
    'threads': 8  # For classical solvers
}
```

### Quantum Parameters

```python
parameters = {
    'shots': 8192,  # Number of quantum measurements
    'optimizer': 'COBYLA'  # Classical optimizer for hybrid
}
```

## Monitoring & Telemetry

### MAP Topics

QAIM-2 publishes to:
- `map/1/control` - Control messages
- `map/1/telemetry` - Performance metrics
- `map/1/log` - Audit logs

### Metrics Collection

Enable in configuration:

```yaml
logging:
  metrics_enabled: true
monitoring:
  prometheus_enabled: true
```

---

*For complete examples, see [example.py](../example.py)*  
*For schema details, see [schemas/](../schemas/)*
