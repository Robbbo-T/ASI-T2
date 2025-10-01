---
id: ASIT2-AQUA-OS-AIRCRAFT-OPTIMIZATION-README
project: ASI-T2
artifact: AQUA OS Aircraft Optimization Module
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0.0
release_date: 2024-10-01
maintainer: "AQUA Optimization Team"
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# AQUA OS Aircraft Optimization Module

This module contains the **Mixed Integer Linear Programming (MILP)** optimization framework for the AQUA (Aircraft Quantum Underlaying Architecture) operating system. It implements hybrid classical-quantum resource planning with multi-criteria optimization and UTCS-MI traceability.

## Overview

The AQUA MILP optimizer solves resource allocation problems across hybrid classical-quantum avionics systems, balancing:

- **Cost**: Operational expenses across subsystems
- **Emissions**: Environmental impact (CO₂ budget compliance)
- **Reliability**: System-level dependability requirements
- **Synchronization**: Classical-quantum layer coherence (decoherence penalty)

## Files

### `aqua_milp_pyomo.py`

Complete MILP optimization model implemented using the **Pyomo** modeling framework.

**Key Features**:
- Multi-criteria objective function with weighted cost, emissions, reliability, and synchronization penalties
- Hybrid system modeling (classical propulsion + quantum navigation/communication)
- Linearized synchronization constraints using Big-M method
- Quantum subsystem quality certification (Fidelity/Latency thresholds)
- UTCS-MI v5.0 compliant traceability output with SHA-256 hashing
- Support for multiple solvers: CBC, GLPK, Gurobi, CPLEX

## Installation

### Requirements

Install Pyomo and a compatible solver:

```bash
# Install Pyomo
pip install pyomo

# Install a solver (choose one):
# Option 1: CBC (open source, recommended for testing)
conda install -c conda-forge coincbc

# Option 2: GLPK (open source, lightweight)
conda install -c conda-forge glpk

# Option 3: Gurobi (commercial, requires license)
pip install gurobipy

# Option 4: CPLEX (commercial, requires license)
pip install cplex
```

### Quick Start

Run the optimization model:

```bash
cd PRODUCTS/INFRANET/AQUA_OS_AIRCRAFT/optimization
python aqua_milp_pyomo.py
```

The script will:
1. Automatically detect available solvers
2. Build and solve the MILP model
3. Display the optimal resource allocation plan
4. Generate a UTCS-MI traceability snapshot (`aqua_pyomo_plan_utcs.json`)

## Model Structure

### Decision Variables

- **x[s,t]**: Classical subsystem usage (continuous, 0 to capacity)
  - `s ∈ S`: Subsystems (motor_electrico, motor_h2)
  - `t ∈ T`: Time steps (0-5, representing 6-hour flight horizon)

- **qact[q,t]**: Quantum subsystem activation (binary, 0 or 1)
  - `q ∈ Q`: Quantum links (qns_link, qkd_comm)

### Constraints

1. **Demand Coverage**: Classical + quantum performance ≥ operational demand
2. **Emissions Budget**: Total CO₂ emissions ≤ budget (10.0 units)
3. **Quality Certification**: Quantum links disabled if Fidelity < F_min or Latency > L_max
4. **Synchronization Bound**: Classical-quantum phase deviation ≤ DELTA_MAX (0.5)
5. **Reliability Minimum**: System reliability ≥ R_MIN (0.95) at each time step

### Objective Function

```
Minimize:
  w_c × (Cost_classical + Cost_quantum)
  + w_e × (Emissions_classical + Emissions_quantum)
  - w_r × (Reliability_classical + Reliability_quantum)
  + λ_sync × Total_Desynchronization
  + β_reg × UTCS_Violations
```

**Weights**:
- `w_c = 1.0` (Cost)
- `w_e = 10.0` (Emissions - high priority for sustainability)
- `w_r = 5.0` (Reliability)
- `λ_sync = 50.0` (Synchronization penalty)
- `β_reg = 1000.0` (Regulatory/UTCS penalty)

## Example Output

```
==================================================
PLAN DE RECURSOS HÍBRIDO (AQUA MILP)
==================================================

--- Instante t=0 (Demanda: 40.0 / Cubierta: 50.00) ---
  > Clásico (x): {'motor_electrico': 0.0, 'motor_h2': 0.0}
  > Cuántico (qact): {'qns_link': 1, 'qkd_comm': 0}
  > Desincronía (delta): 0.1000 (Max: 0.5)

...

--- Resumen General ---
Objetivo Total (Ponderado): 245.67
Emisiones Totales (Presupuesto 10.0): 1.234567
Sincronía Total Penalizada: 0.6000
==================================================

[UTCS-MI] Registro de configuración guardado en aqua_pyomo_plan_utcs.json
[UTCS-MI] ID de Trazabilidad: UTCS-Avionics-IntegratedFlightControl-MILP_Planner-v1.0-Operational-20241001T120000Z-a1b2c3d4
[UTCS-MI] Hash de Integridad: e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z4
```

## UTCS-MI Traceability

The optimization generates a JSON snapshot conforming to UTCS-MI v5.0:

```json
{
  "UTCS_ID": "UTCS-Avionics-IntegratedFlightControl-MILP_Planner-v1.0-Operational-20241001T120000Z-a1b2c3d4",
  "Timestamp_UTC": "20241001T120000Z",
  "SystemDomain": "Avionics",
  "SubsystemID": "IntegratedFlightControl",
  "ConfigVersion": "v1.0",
  "Mode": "Operational",
  "QuantumLayerPresent": true,
  "Plan_Optimization_Horizon": { ... },
  "Optimization_Results_Summary": { ... },
  "Content_Hash_SHA256": "e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z4"
}
```

## Customization

### Modifying Parameters

Edit the parameter section in `aqua_milp_pyomo.py`:

```python
# Subsystems
S = ['motor_electrico', 'motor_h2', 'your_system']
Q = ['qns_link', 'qkd_comm', 'your_quantum_link']

# Capacities and costs
cap_s = {'motor_electrico': 100.0, 'motor_h2': 80.0, 'your_system': 120.0}
c_s = {'motor_electrico': 2.0, 'motor_h2': 3.5, 'your_system': 2.5}

# Time horizon
T = list(range(12))  # 12-hour horizon
```

### Adding Constraints

Add new constraints using Pyomo constraint rules:

```python
def your_constraint_rule(m, t):
    # Your constraint logic
    return m.x['motor_electrico', t] + m.x['motor_h2', t] <= 150.0

model.your_cons = Constraint(model.T, rule=your_constraint_rule)
```

## Integration with AQUA OS

This optimization module is designed to integrate with:

- **QAFbW** (Quantum-Assisted Fly-by-Wire): Resource allocation for flight control
- **NAVSYS** (Navigation System): Quantum navigation link planning
- **SEC_KMS** (Security/Key Management): QKD resource scheduling
- **UTCS_QS** (Evidence & Trace): Traceability and audit trail integration

## References

- [AQUA OS Aircraft README](../README.md)
- [UTCS_QS Component Specification](../components/UTCS_QS/README.md)
- [QAIM Optimization Standards](../../QAIM/README.md)
- [Pyomo Documentation](https://pyomo.readthedocs.io/)

## Support

For issues or questions:
- Check solver installation: Run `python -c "from pyomo.environ import *; print(SolverFactory('glpk').available())"`
- Verify model feasibility: Review constraint violations in solver output
- Traceability issues: Validate JSON output against UTCS-MI v5.0 schema

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*
