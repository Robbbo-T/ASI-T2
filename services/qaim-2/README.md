# QAIM-2 — Quantum-Classical Optimization via AI Bridges

**Version:** 0.1.0  
**Bridge:** QS→FWD→UE→FE→CB→QB  
**Ethics:** MAP-EEM · MAL-EEM  
**UTCS:** v5.0

## Overview

QAIM-2 orchestrates **classical (CB)**, **cubic-bit (QB)**, and optional **quantum (QC)** resources through **AI bridges** for optimization problems across ASI-T2 products.

**Key Features:**
- AI-assisted solver selection with reinforcement learning
- Multi-solver portfolio (Gurobi, CBC, OR-Tools, GLPK, QB tensor, QC QAOA/VQE)
- UTCS v5.0 evidence generation and provenance
- S1000D/ATA-aware problem canonicalization
- Edge, site, and hub deployment configurations

**Critical Note:** **QB ≠ qubit**. QB is non-quantum 3D lifting (CB×CB×CB).

## Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# For development
pip install -e .[dev]
```

### Basic Usage

```python
from qaim_2.core import QAIM2Orchestrator

# Load configuration
config = yaml.safe_load(open('config/deployment-edge.yaml'))

# Create orchestrator
orchestrator = QAIM2Orchestrator(config)

# Define optimization problem
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
print(f"Solver: {result['solver']}")
print(f"Solution: {result['solution']}")
```

## Architecture

```
Inputs → PCAN → SM → SP → ARB → XFR → [CB/QB/QC] → UTCS Evidence
         ↓       ↓    ↓    ↓     ↓
      Policies  Data  RL  MAB  Translation
```

### Components

#### AI Bridges

- **PCAN** (Problem Canonicalization): Transform domain problems to standard format
- **SM** (Surrogate Models): GNN/GP/Transformer feature extraction
- **SP** (Strategy Policy): RL-based solver selection
- **ARB** (Arbitration): Multi-armed bandit runtime adjustment
- **XFR** (Cross-Framework): CB↔QB↔QC translation

#### Solver Pools

- **CB Pool**: Gurobi, CBC, OR-Tools, GLPK
- **QB Pool**: Tensor decomposition, lifted relaxation
- **QC Gateway**: IBM Quantum, D-Wave, IonQ (optional)

## Directory Structure

```
services/qaim-2/
├── core/
│   ├── __init__.py
│   └── qaim_orchestrator.py          # Main orchestrator
├── bridges/
│   ├── __init__.py
│   ├── pcan.py                        # Problem canonicalization
│   ├── surrogate_models.py           # GNN/GP/Transformer
│   ├── strategy_policy.py            # RL solver selection
│   ├── arbitration.py                # Multi-armed bandits
│   └── cross_framework.py            # CB↔QB↔QC translation
├── solvers/
│   ├── __init__.py
│   ├── cb_pool.py                    # Classical solvers
│   ├── qb_pool.py                    # Cubic-bit approximations
│   └── qc_gateway.py                 # Quantum computing interface
├── schemas/
│   ├── optimize_qb.v1.json           # Input schema
│   └── qaim_result.v1.json           # Output schema
├── config/
│   ├── deployment-edge.yaml          # Edge deployment
│   ├── deployment-site.yaml          # Site deployment
│   └── deployment-hub.yaml           # Hub deployment
└── README.md                          # This file
```

## Deployment Configurations

### Edge Deployment

Lightweight configuration for UAVs, edge devices, and real-time applications.

**Characteristics:**
- Classical solvers only (CBC, GLPK)
- No ML models
- Minimal resource usage
- < 512MB memory

**Use cases:** UAV mission planning, on-board optimization

```bash
python -m qaim_2.server --config config/deployment-edge.yaml
```

### Site Deployment

Regional deployment with mixed solver portfolio.

**Characteristics:**
- Classical + QB solvers
- Basic ML models (GP)
- Moderate resources
- 4GB memory, 16 CPUs

**Use cases:** Factory scheduling, regional logistics

```bash
python -m qaim_2.server --config config/deployment-site.yaml
```

### Hub Deployment

Full-featured deployment with all solvers including quantum.

**Characteristics:**
- CB + QB + QC solvers
- Full ML suite (GNN, GP, Transformer)
- High-performance computing
- 64GB memory, 64 CPUs, 2 GPUs

**Use cases:** Aircraft design, large-scale optimization, R&D

```bash
python -m qaim_2.server --config config/deployment-hub.yaml
```

## TFA V2 Bridge Mapping

| Layer | Role       | MAL Service | MAP Topics                       |
|-------|------------|-------------|----------------------------------|
| QS    | Provenance | MAL-QS      | map/1/log, map/1/telemetry       |
| FWD   | Nowcast    | MAL-FWD     | map/1/control, map/1/telemetry   |
| UE    | Collapse   | MAL-UE      | map/1/control, map/1/telemetry   |
| FE    | Federation | MAL-FE      | map/1/control, map/1/telemetry   |
| CB    | Classical  | MAL-CB      | map/1/control, map/1/telemetry   |
| QB    | Cubic-bit  | MAL-QB      | map/1/control, map/1/telemetry   |

## ASI-T2 Product Integration

### AMPEL360 BWB-Q100
- Aerodynamic optimization (AAA)
- Flight control tuning (LCC)
- Manufacturing planning (PPP)

### GAIA-SPACE
- Constellation scheduling
- Orbit optimization
- Ground station allocation

### GAIA-AIR
- Swarm coordination
- Multi-agent task assignment
- Energy-efficient routing

### H₂-AIRPORT
- Hydrogen storage optimization
- Fueling schedule coordination
- Safety zone layout

### BITFINANCE
- Portfolio optimization
- Risk management
- Transaction routing

## Evidence & Compliance

### UTCS v5.0 Evidence

Every optimization generates UTCS v5.0 evidence including:
- Input hash (SHA-256)
- Solver provenance
- Execution trace
- Solution verification
- Cryptographic signatures

### Standards Compliance

- **S1000D**: Data module integration
- **ATA**: Chapter mapping
- **DO-178C**: Software level TBD
- **ECSS**: Space standards

### Ethics

- **MAP-EEM**: Ethical evaluation matrix
- **MAL-EEM**: Master ethics module

## API Reference

See [MASTER_WHITEPAPER_4.md](../../WHITEPAPERS/MASTER_WHITEPAPER_4.md) for complete API documentation.

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/test_orchestrator.py
pytest tests/test_bridges.py
pytest tests/test_solvers.py
```

## Contributing

Follow ASI-T2 contribution guidelines. All changes must:
- Pass MAP-EEM/MAL-EEM review
- Include UTCS evidence
- Align with TFA V2 architecture
- Include tests

## License

MIT with responsible use. MAP-EEM/MAL-EEM required.

## References

- [MASTER_WHITEPAPER_4.md](../../WHITEPAPERS/MASTER_WHITEPAPER_4.md) - Complete specification
- [QAIM README](../../PRODUCTS/INFRANET/QAIM/README.md) - QAIM product overview
- [QAIM-2 Matrix](../../FIELDS/cross/process_engineering/QAIM-2/README.md) - CAx→QOx mapping

---

*Part of ASI-T2 INFRANET Product Suite*  
*Version: 0.1.0*  
*Last Updated: 2025-10-03*
