# QAIM-2 Core

This directory contains the core orchestration engine for the QAIM-2 optimization service.

## Overview

The core module implements the main `QAIM2Orchestrator` class that coordinates all AI bridges and solver pools to execute optimization requests following the TFA V2 bridge pattern.

## Components

### `qaim_orchestrator.py`

**Main Orchestrator Class**

The `QAIM2Orchestrator` is the central component that:
- Coordinates AI bridges (PCAN, SM, SP, ARB, XFR)
- Manages solver pools (CB, QB, QC)
- Generates UTCS v5.0 evidence
- Implements TFA V2 bridge pattern
- Provides async optimization interface

**Key Methods:**

#### `optimize(problem, constraints, metadata) → Dict`

Main entry point for optimization requests.

```python
orchestrator = QAIM2Orchestrator(config)

result = await orchestrator.optimize(
    problem={
        'problem_type': 'vehicle_routing',
        'variables': [...],
        'constraints': [...],
        'objectives': [...]
    },
    constraints={
        'time_limit': 60,
        'gap_tolerance': 0.01
    },
    metadata={
        'domain': 'logistics',
        'ata_chapter': 'ATA-34'
    }
)
```

**Returns:**
```python
{
    'request_id': 'uuid',
    'solver': 'cb_gurobi',
    'solution': {...},
    'metrics': {
        'objective_value': 10.5,
        'gap': 0.01,
        'solve_time': 5.2,
        'feasible': True
    },
    'evidence': {
        'version': 'utcs-v5.0',
        'provenance': {...}
    },
    'status': 'optimal'
}
```

## Architecture

### TFA V2 Bridge Flow

The orchestrator implements the complete bridge pattern:

```
Input
  ↓
[QS] Provenance Logging
  ↓
[FWD] PCAN: Problem Canonicalization
  ↓
[UE] SM: Feature Extraction
  ↓
[FE] SP: Solver Selection
  ↓
[FE] ARB: Runtime Arbitration
  ↓
[CB/QB] XFR: Framework Translation
  ↓
[CB/QB/QC] Solver Execution
  ↓
[QS] Evidence Generation
  ↓
Output + UTCS Evidence
```

### Component Initialization

The orchestrator initializes all components on construction:

```python
self.pcan = ProblemCanonicalizer(config['pcan'])
self.surrogate = SurrogateModels(config['surrogate'])
self.strategy = StrategyPolicy(config['strategy'])
self.arbitration = Arbitration(config['arbitration'])
self.translator = CrossFrameworkTranslator(config['translator'])
self.cb_pool = ClassicalSolverPool(config['cb_solvers'])
self.qb_pool = CubicBitSolverPool(config['qb_solvers'])
self.qc_gateway = QuantumGateway(config['qc_gateway'])
```

## UTCS v5.0 Evidence

Every optimization generates verifiable evidence:

```python
{
    'version': 'utcs-v5.0',
    'request_id': 'uuid',
    'timestamp': '2025-10-03T12:00:00Z',
    'duration_ms': 5200,
    'input_hash': 'sha256...',
    'solver': {
        'name': 'cb_gurobi',
        'version': '10.0.0',
        'config': {...}
    },
    'solution': {
        'status': 'optimal',
        'objective_value': 10.5,
        'gap': 0.01,
        'feasible': True
    },
    'provenance': {
        'bridge': 'QS→FWD→UE→FE→CB→QB',
        'ethics': 'MAP-EEM · MAL-EEM',
        'utcs_version': 'v5.0',
        'framework': 'TFA-V2'
    }
}
```

## Error Handling

The orchestrator provides comprehensive error handling:

```python
try:
    result = await orchestrator.optimize(problem, constraints)
except ValueError as e:
    # Invalid input or configuration
    print(f"Configuration error: {e}")
except TimeoutError as e:
    # Solver timeout
    print(f"Optimization timeout: {e}")
except Exception as e:
    # Unexpected error
    print(f"Error: {e}")
```

All errors generate error evidence for audit trails.

## Configuration

The orchestrator requires a configuration dictionary:

```python
config = {
    'pcan': {
        'enabled': True,
        'cache_size': 1000
    },
    'surrogate': {
        'enabled': True,
        'models': [...]
    },
    'strategy': {
        'algorithm': 'epsilon_greedy',
        'exploration_rate': 0.1
    },
    'arbitration': {
        'algorithm': 'ucb1',
        'window_size': 1000
    },
    'translator': {
        'formats': ['mip', 'qubo']
    },
    'cb_solvers': [...],
    'qb_solvers': {...},
    'qc_gateway': {...}
}
```

## Usage Example

Complete example:

```python
import asyncio
import yaml
from core.qaim_orchestrator import QAIM2Orchestrator

async def main():
    # Load configuration
    with open('config/deployment-site.yaml') as f:
        config = yaml.safe_load(f)
    
    # Create orchestrator
    orchestrator = QAIM2Orchestrator(config)
    
    # Define problem
    problem = {
        'problem_type': 'vehicle_routing',
        'variables': [
            {'name': 'route_1', 'type': 'binary'},
            {'name': 'route_2', 'type': 'binary'}
        ],
        'constraints': [
            {'type': 'capacity', 'value': 100}
        ],
        'objectives': [
            {'name': 'minimize_distance', 'sense': 'minimize'}
        ]
    }
    
    # Optimize
    result = await orchestrator.optimize(
        problem=problem,
        constraints={'time_limit': 60},
        metadata={'domain': 'logistics'}
    )
    
    print(f"Status: {result['status']}")
    print(f"Solver: {result['solver']}")
    print(f"Solution: {result['solution']}")

if __name__ == '__main__':
    asyncio.run(main())
```

## Performance Considerations

### Memory Usage
- Edge: ~100MB per orchestrator instance
- Site: ~500MB with ML models
- Hub: ~2GB with full ML suite

### Concurrency
- Each orchestrator handles one optimization at a time
- Deploy multiple instances for concurrent requests
- Use async/await for efficient I/O

### Caching
- PCAN caches canonical problems
- SM caches feature predictions
- ARB maintains solver statistics

## Testing

```bash
# Run core tests
pytest tests/test_orchestrator.py -v

# Test specific functionality
pytest tests/test_orchestrator.py::test_basic_optimization -v

# Run with coverage
pytest tests/test_orchestrator.py --cov=core --cov-report=html
```

## Monitoring

The orchestrator emits to MAP topics:

- `map/1/control` - Control messages
- `map/1/telemetry` - Performance metrics
- `map/1/log` - Audit logs

Enable monitoring in configuration:

```yaml
map:
  enabled: true
  broker: 'broker:1883'
  topics:
    - 'map/1/control'
    - 'map/1/telemetry'
    - 'map/1/log'
```

## References

- [MASTER_WHITEPAPER_4.md](../../WHITEPAPERS/MASTER_WHITEPAPER_4.md) - Architecture specification
- [API.md](../docs/API.md) - API documentation
- [example.py](../example.py) - Working example

---

*QAIM-2 Core Orchestration Engine*  
*TFA V2: QS→FWD→UE→FE→CB→QB*  
*UTCS: v5.0*
