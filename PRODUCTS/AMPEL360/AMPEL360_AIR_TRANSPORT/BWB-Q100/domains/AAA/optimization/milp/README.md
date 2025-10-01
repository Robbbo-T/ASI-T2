---
id: ASIT-BWQ1-AAA-OPTIMIZATION-MILP-0001
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/optimization/milp/README.md
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: 2025-10-01
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# AQUA MILP Optimization System

## Overview

This directory contains the AQUA (Advanced Quantum-classical Unified Avionics) MILP (Mixed-Integer Linear Programming) optimization system. The system implements a hybrid classical-quantum resource allocation planner with strict separation between model structure and data for UTCS-MI traceability and certification.

## Purpose

The AQUA MILP system optimizes multi-criteria resource allocation for:
- **Classical subsystems** (electric motors, H2 propulsion)
- **Quantum subsystems** (QNS links, QKD communication)
- **Synchronization constraints** (classical-quantum phase alignment)
- **Environmental constraints** (CO2 emissions budgets)
- **Reliability requirements** (mission-critical availability)

## Architecture

### Data-Model Separation (UTCS-MI Compliant)

The system follows the principle of separating:
1. **Model Logic** (`aqua_milp_model.py`) - Mathematical structure, constraints, objectives
2. **Mission Data** (`aqua_milp.dat`) - Parameters, sets, mission-specific values

This separation enables:
- Independent versioning and certification of model vs. data
- Cryptographic hashing for traceability (SHA-256)
- Solver-independent problem formulation
- Easy validation with different parameter sets

## Files

### `aqua_milp_model.py`
**Model Structure (Data-Free)**

Contains the Pyomo model structure including:
- Sets (S, Q, T) - Classical systems, Quantum systems, Time horizon
- Parameters - Costs, emissions, reliability, quality metrics
- Variables - Resource allocation decisions (continuous and binary)
- Objective function - Multi-criteria optimization
- Constraints - Demand, emissions, quality, synchronization, reliability

**Key Features:**
- No embedded data - all parameters loaded from .dat file
- AMPL/Pyomo compatible formulation
- Binary variables for quantum system activation
- Big-M linearization for synchronization constraints
- UTCS placeholder for external validation hooks

### `aqua_milp_data_generator.py`
**Data File Generator**

Generates `.dat` files in Pyomo/AMPL format from Python dictionaries:
- Example data for 2 classical subsystems, 2 quantum subsystems
- 6-step time horizon
- Configurable thresholds and weights
- Two-index parameter formatting for quantum metrics

**Usage:**
```bash
python aqua_milp_data_generator.py
```

Output: `aqua_milp.dat` in current directory

### `aqua_milp.dat`
**Mission Parameters (AMPL/Pyomo Format)**

Contains all model parameters in standard AMPL data format:
- Scalar parameters (thresholds, weights, bounds)
- One-dimensional parameters (per subsystem)
- Two-dimensional parameters (per subsystem per timestep)

**Format Compatibility:**
- Pyomo `create_instance()`
- AMPL `data;` section
- Export to `.lp` or `.mps` for Gurobi/CPLEX

### `aqua_milp_solve.py`
**Solver and UTCS Tracer**

Loads model and data, solves optimization, generates UTCS evidence:
- Automatic solver detection (Gurobi, CBC, GLPK, CPLEX)
- Result extraction and formatting
- UTCS-MI snapshot generation with:
  - Unique UTCS ID with timestamp
  - SHA-256 content hash
  - Provenance metadata
  - Optimization results summary

**Usage:**
```bash
python aqua_milp_solve.py
```

Output: `aqua_pyomo_solve_utcs.json` with traceability snapshot

## Execution Workflow

### 1. Generate Data
```bash
cd PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/optimization/milp
python3 aqua_milp_data_generator.py
```

### 2. Solve Model
```bash
python3 aqua_milp_solve.py
```

### 3. Review Results
- Console: Objective value, emissions, UTCS ID
- File: `aqua_pyomo_solve_utcs.json` - Full traceability snapshot

## Dependencies

**Required:**
- Python 3.8+
- Pyomo >= 6.0

**Solver (one of):**
- CBC (open-source, recommended for testing)
- GLPK (open-source)
- Gurobi (commercial, high-performance)
- CPLEX (commercial, high-performance)

**Installation:**
```bash
pip install pyomo
# For CBC solver
conda install -c conda-forge coincbc
# OR for GLPK
apt-get install glpk-utils
```

## UTCS-MI Traceability

### Versioning Strategy
- **Model code** (`aqua_milp_model.py`) - Algorithm version, git hash
- **Data files** (`*.dat`) - Mission/scenario identifier, parameter hash
- **Results** (`*.json`) - Links to model version + data hash + solver version

### Certification Evidence
1. **Model SHA-256** - Hash of `aqua_milp_model.py` source
2. **Data SHA-256** - Hash of `aqua_milp.dat` content
3. **Result SHA-256** - Hash of optimization output JSON
4. **Solver fingerprint** - Solver name, version, license info

### Validation Workflow
```python
# Verify result corresponds to specific model + data
import hashlib
with open('aqua_milp_model.py', 'rb') as f:
    model_hash = hashlib.sha256(f.read()).hexdigest()
with open('aqua_milp.dat', 'rb') as f:
    data_hash = hashlib.sha256(f.read()).hexdigest()
# Compare with UTCS snapshot provenance
```

## Model Formulation

### Objective Function
Multi-criteria minimization:
- **Cost** - Weighted sum of classical and quantum resource costs
- **Emissions** - Environmental impact (CO2)
- **Reliability** - Negative term (maximize reliability)
- **Synchronization penalty** - Classical-quantum phase deviation
- **UTCS violation penalty** - External validation hook

### Decision Variables
- `x[s,t]` - Continuous allocation of classical subsystem s at time t
- `qact[q,t]` - Binary activation of quantum subsystem q at time t
- `delta[t]` - Total synchronization deviation at time t
- `delta_q[q,t]` - Per-quantum-system sync deviation (linearized)
- `u[q,t], v[q,t]` - Auxiliary variables for absolute value linearization

### Constraints
1. **Demand Coverage** - Sum of allocations meets demand at each timestep
2. **Emission Budget** - Total emissions below global limit
3. **Quality Gates** - Quantum fidelity/latency thresholds
4. **Synchronization** - Classical-quantum phase alignment (linearized)
5. **Reliability** - Minimum system reliability at each timestep

## Integration Points

### Upstream
- Mission planning system → Data parameters
- Quantum backend monitors → Quality metrics (F, L)
- Classical system monitors → Performance data

### Downstream
- AQUA-OS scheduler → Resource allocation plan
- UTCS-MI evidence chain → Certification artifacts
- Gurobi/CPLEX → Performance profiling and tuning

## Performance Considerations

### Problem Scale
- **Current example:** 2 classical + 2 quantum systems, 6 timesteps
- **Variables:** ~80 (including auxiliary)
- **Constraints:** ~60
- **Expected solve time:** < 1 second (CBC), < 0.1 second (Gurobi)

### Scalability
- Linear scaling with time horizon (T)
- Linear scaling with subsystem count (|S|, |Q|)
- Quadratic growth in synchronization constraints (|Q| × |T|)

### Solver Selection
- **Development/CI:** CBC or GLPK (open-source, sufficient for small problems)
- **Production:** Gurobi or CPLEX (10-100x faster for large problems)
- **Certification:** Commercial solvers with formal verification support

## Future Enhancements

### Planned Features
1. **Dynamic data loading** - JSON/YAML parameter files
2. **Multi-scenario optimization** - Batch processing of parameter sets
3. **Sensitivity analysis** - Automated parameter perturbation
4. **Warm-start integration** - Reuse previous solutions
5. **Model export** - `.lp` and `.mps` file generation

### Certification Roadmap
1. **DO-178C compliance** - Formal model verification
2. **DO-333 integration** - Formal methods evidence
3. **UTCS-MI v5.0 full compliance** - Extended provenance chain
4. **Solver certification** - Validated solver configurations

## References

### Standards
- **ARINC 653** - Partitioned avionics architecture
- **DO-178C** - Software considerations in airborne systems
- **DO-333** - Formal methods supplement
- **UTCS-MI v5.0** - Universal Trust and Certification System

### Related Documentation
- [AQUA-OS Overview](../../IIS/ata/ATA-42/os/descriptive/os_overview.md)
- [QOx QUBO Standard](../qox/qubo/README.md)
- [UTCS Evidence Package](../../LCC/utcs/README.md)

## License

Proprietary - ASI-T Architecture Team
Classification: INTERNAL–EVIDENCE-REQUIRED

## Changelog

### v0.1.0 (2025-10-01)
- Initial implementation with data-model separation
- Example parameter set for 2+2 systems, 6 timesteps
- UTCS-MI snapshot generation
- Multi-solver support (CBC, GLPK, Gurobi, CPLEX)
