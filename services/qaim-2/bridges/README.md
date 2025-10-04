# QAIM-2 AI Bridges

This directory contains the AI bridge components that orchestrate solver selection and problem transformation in the QAIM-2 optimization service.

## Overview

The bridges implement the TFA V2 pattern layers (FWD, UE, FE) for intelligent routing between classical (CB), cubic-bit (QB), and quantum computing (QC) solvers.

## Components

### 1. PCAN — Problem Canonicalization (`pcan.py`)

**TFA Layer:** FWD (Nowcast)

Transforms domain-specific problems into standardized optimization formats with S1000D/ATA awareness.

**Key Features:**
- Variable, constraint, and objective extraction
- S1000D data module integration
- ATA chapter mapping (ATA-21 through ATA-71)
- Metadata enrichment and normalization

**Usage:**
```python
from bridges.pcan import ProblemCanonicalizer

pcan = ProblemCanonicalizer(config)
canonical = await pcan.canonicalize(problem, metadata)
```

### 2. SM — Surrogate Models (`surrogate_models.py`)

**TFA Layer:** UE (Collapse)

ML-based feature extraction and solver performance prediction without full execution.

**Models:**
- **GNN (Graph Neural Networks):** Structured problem analysis
- **GP (Gaussian Processes):** Uncertainty quantification
- **Transformer:** Sequential dependency modeling

**Usage:**
```python
from bridges.surrogate_models import SurrogateModels

sm = SurrogateModels(config)
features = await sm.extract_features(canonical)
```

### 3. SP — Strategy Policy (`strategy_policy.py`)

**TFA Layer:** FE (Federation)

Reinforcement learning-based solver selection using contextual bandits.

**Algorithms:**
- Epsilon-greedy exploration
- UCB1 (Upper Confidence Bound)
- Thompson Sampling

**Usage:**
```python
from bridges.strategy_policy import StrategyPolicy

sp = StrategyPolicy(config)
solver, params = await sp.select_solver(features, constraints)
```

### 4. ARB — Arbitration (`arbitration.py`)

**TFA Layer:** FE (Federation)

Runtime adjustment and fallback handling using multi-armed bandits.

**Features:**
- Dynamic solver switching
- Load balancing
- Timeout detection
- Performance tracking

**Usage:**
```python
from bridges.arbitration import Arbitration

arb = Arbitration(config)
solver = arb.select_arm(context)
```

### 5. XFR — Cross-Framework Translation (`cross_framework.py`)

**TFA Layer:** CB/QB (Translation)

Translates canonical problems into solver-specific formats.

**Supported Formats:**
- **Classical:** MIP, SAT, CSP
- **Cubic-bit:** Tensor networks, lifted formulations
- **Quantum:** QUBO, QAOA, VQE

**Usage:**
```python
from bridges.cross_framework import CrossFrameworkTranslator

xfr = CrossFrameworkTranslator(config)
solver_problem = await xfr.translate(canonical, solver_type)
```

## Architecture Flow

```
Problem → PCAN → SM → SP/ARB → XFR → Solver
          (FWD)  (UE)  (FE)     (CB/QB)
```

## Configuration

Bridge components are configured via deployment YAML files:

```yaml
# Edge deployment (minimal)
pcan:
  enabled: true
  s1000d_aware: false
surrogate:
  enabled: false

# Hub deployment (full ML)
pcan:
  enabled: true
  s1000d_aware: true
  ata_mapping: true
surrogate:
  enabled: true
  models:
    - type: 'gnn'
    - type: 'gp'
    - type: 'transformer'
```

## Testing

```bash
# Run bridge tests
pytest tests/test_bridges.py -v

# Test specific bridge
pytest tests/test_bridges.py::test_pcan_canonicalization -v
```

## References

- [MASTER_WHITEPAPER_4.md](../../WHITEPAPERS/MASTER_WHITEPAPER_4.md) - Complete specification
- [API.md](../docs/API.md) - API documentation
- [OPERATIONS.md](../docs/OPERATIONS.md) - Operations guide

---

*Part of QAIM-2 Quantum-Classical Optimization Service*  
*TFA V2 Bridge: QS→FWD→UE→FE→CB→QB*
