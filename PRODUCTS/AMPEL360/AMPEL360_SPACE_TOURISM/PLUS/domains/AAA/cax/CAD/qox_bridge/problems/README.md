# QOx Problem Definitions

This directory contains quantum optimization problem definitions for the CAx→QOx bridge, encoding discrete CAD design choices as QUBO/BQM formulations for quantum and quantum-inspired solvers.

## Purpose

Transforms combinatorial CAD design problems into quantum-ready optimization formulations, enabling quantum advantage for complex design space exploration in AMPEL360 PLUS space vehicle development.

## File Types

- **`*.json`** - QUBO/BQM problem definitions following `qox_problem.schema.json`
- Each problem encodes discrete design variables, objectives, and constraints for quantum solvers

## Naming Convention

```
PLUS-<DOMAIN>-<PROBLEM>-QUBO-<ID>.json
```

Where:
- `<DOMAIN>` = Design domain (TPS, STRUCT, OML, etc.)
- `<PROBLEM>` = Specific optimization problem (TILING, TOPOLOGY, etc.)
- `<ID>` = Sequential number (001, 002, etc.)

Examples:
- `PLUS-TPS-TILING-QUBO-001.json` - TPS panel placement optimization
- `PLUS-STRUCT-TOPOLOGY-QUBO-002.json` - Structural topology optimization
- `PLUS-OML-SHAPE-QUBO-003.json` - Outer mold line shape optimization

## Problem Categories

### TPS (Thermal Protection System)
- **Panel Placement**: Optimal tile selection and arrangement
- **Seam Configuration**: Minimizing thermal bridging and maintenance
- **Material Selection**: Multi-criteria material assignment
- **Coverage Optimization**: Complete surface protection with minimal mass

### Structural Design
- **Topology Optimization**: Discrete element selection for optimal load paths
- **Joint Placement**: Fastener and connection point optimization
- **Material Layout**: Composite layup and metallic section optimization
- **Load Distribution**: Force flow optimization under multiple load cases

### Aerodynamic Surfaces
- **Control Surface Layout**: Optimal placement for attitude control
- **Surface Segmentation**: Panel division for manufacturing and maintenance
- **Shape Optimization**: Discrete geometric parameter selection
- **Integration Constraints**: Vehicle-level compatibility requirements

## Problem Structure

### Variables
```json
"variables": {
  "x_i": {"count": 480, "domain": "binary", "meaning": "tile selection"},
  "y_j": {"count": 120, "domain": "binary", "meaning": "seam configuration"}
}
```

### Objectives
```json
"objective": [
  {"term": "thermal_margin", "weight": -2.0, "description": "Maximize safety margin"},
  {"term": "mass", "weight": 1.0, "description": "Minimize total mass"},
  {"term": "maintainability", "weight": -0.3, "description": "Maximize accessibility"}
]
```

### Constraints
```json
"constraints": [
  {"type": "coverage", "weight": 8.0, "description": "Complete surface coverage"},
  {"type": "max_panel_size", "weight": 4.0, "description": "Manufacturing limits"},
  {"type": "thermal_gradient", "weight": 3.0, "description": "Temperature limits"}
]
```

## Quantum Bridge (QAIM-2)

### Classical-to-Quantum Encoding
1. **Problem Identification**: Discrete design choices in CAD workflows
2. **Variable Mapping**: Binary/integer variables to qubits
3. **Objective Encoding**: Multi-objective cost functions as QUBO matrices
4. **Constraint Handling**: Penalty methods for hard/soft constraints

### Solver Integration
- **QAOA**: Quantum Approximate Optimization Algorithm
- **VQE**: Variational Quantum Eigensolver
- **Quantum Annealing**: D-Wave and similar platforms
- **Hybrid Classical**: Classical refinement of quantum solutions

### Hardware Requirements
- **Qubit Count**: Problem size determines minimum qubits needed
- **Connectivity**: Graph structure affects embedding efficiency
- **Coherence**: Algorithm depth vs. decoherence limits
- **Classical Support**: Hybrid loop implementation

## Data Sources

### Geometry Data
```json
"data_sources": {
  "coverage_matrix": "../../geometry/exports/PLUS-OML-A02.step",
  "incidence_table": "../../tps/layout/panel_incidence_R1.csv",
  "thermal_loads": "../../mdo/thermal/reentry_R1_loads.json"
}
```

### Integration Points
- **CAD Exports**: STEP/IGES files from geometry/ directory
- **Analysis Results**: CFD/CAE/thermal simulation data
- **Manufacturing Data**: Process constraints and capabilities
- **Operations**: Maintenance and inspection requirements

## Algorithm Configuration

### QAOA Parameters
```json
"algorithm": {
  "type": "QAOA",
  "parameters": {
    "layers": 3,
    "optimizer": "COBYLA",
    "max_iterations": 200,
    "random_seed": 42,
    "warm_start": true
  }
}
```

### Scaling and Normalization
```json
"scaling": {
  "objective_weights_normalized": true,
  "constraint_penalties_big_m": [8.0, 4.0, 6.0, 3.0],
  "variable_scaling": "unit_interval"
}
```

## Validation and Roundtrip

### Solution Validation
```json
"roundtrip": {
  "exports": ["../../geometry/exports/PLUS-OML-A02.step"],
  "validation": ["CAE/thermal", "CFD/aero"],
  "tolerance": {"objective": 0.05, "constraints": 0.01}
}
```

### Quality Assurance
- **Feasibility**: All solutions satisfy hard constraints
- **Optimality**: Gap analysis vs. classical benchmarks
- **Reproducibility**: Deterministic results with fixed seeds
- **Convergence**: Solution quality vs. iteration count

## Current Problems

### `PLUS-TPS-TILING-QUBO-001.json`
**TPS Panel Placement for Reentry Segment R1**

- **Variables**: 600 binary (480 tiles + 120 seams)
- **Objectives**: Thermal margin, mass, seam length, maintainability
- **Constraints**: Coverage, panel size, conflicts, thermal gradients
- **Data**: Coverage matrix, incidence tables, thermal loads
- **Hardware**: 600-qubit requirement for full problem

## Usage

### Problem Definition
1. **Identify Discrete Choices**: CAD decisions amenable to binary encoding
2. **Define Variables**: Binary/integer variables with clear physical meaning
3. **Formulate Objectives**: Multi-criteria optimization with appropriate weights
4. **Add Constraints**: Hard requirements and soft preferences
5. **Specify Data Sources**: Link to concrete geometry and analysis files

### Solver Execution
```python
# Load problem definition
with open('PLUS-TPS-TILING-QUBO-001.json') as f:
    problem = json.load(f)

# Extract QUBO matrix from objectives and constraints
Q = build_qubo_matrix(problem)

# Solve using quantum algorithm
solution = qaoa_solve(Q, problem['algorithm']['parameters'])

# Validate solution against CAD constraints
validate_solution(solution, problem['roundtrip'])
```

### Integration Workflow
1. **CAD Problem** → QUBO Formulation
2. **Quantum Solve** → Candidate Solutions  
3. **Classical Refinement** → Optimized Design
4. **CAD Validation** → Geometry Verification
5. **Evidence Generation** → UTCS Documentation

## Schema Validation

All problem files validate against:
```bash
python ../../scripts/validate_json.py ../../schemas/ .
```

Required schema: `../../schemas/qox_problem.schema.json`

## UTCS Integration

Each problem includes:
- **Canonical Hash**: Unique identifier for reproducibility
- **Evidence Path**: Quality assurance documentation
- **Provenance**: Source document and process tracking
- **Metadata**: Creation date, author, version, tags

## Future Directions

### Problem Expansion
- **Multi-Vehicle**: Cross-platform optimization problems
- **Multi-Disciplinary**: Coupled aero-thermo-structural problems
- **Time-Dependent**: Dynamic optimization over flight profiles
- **Uncertainty**: Robust optimization under parameter uncertainty

### Algorithm Development
- **Noise-Resilient**: Algorithms adapted for NISQ devices
- **Hybrid Methods**: Classical-quantum decomposition strategies
- **Error Mitigation**: Quantum error correction integration
- **Scalability**: Larger problems via problem decomposition

### Hardware Evolution
- **Gate-Based**: IBM, Google, Rigetti quantum processors
- **Annealing**: D-Wave and quantum annealing platforms
- **Photonic**: Xanadu and PsiQuantum photonic systems
- **Neutral Atom**: QuEra and atom computing platforms