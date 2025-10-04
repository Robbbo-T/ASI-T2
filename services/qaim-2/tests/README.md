# QAIM-2 Tests

This directory contains the test suite for the QAIM-2 optimization service.

## Overview

Comprehensive tests covering the orchestrator, AI bridges, solver pools, and end-to-end optimization flows.

## Test Files

### `test_orchestrator.py`

**Core orchestrator tests**

Tests the main `QAIM2Orchestrator` class functionality including:

- Orchestrator initialization with configuration
- Basic optimization workflow
- Solver selection logic
- Error handling
- Input hashing for evidence
- Multi-objective optimization
- UTCS v5.0 evidence generation
- TFA V2 bridge pattern verification

**Key Tests:**

#### `test_orchestrator_initialization`
Verifies all components initialize correctly from configuration.

#### `test_basic_optimization`
Tests end-to-end optimization with sample vehicle routing problem.

#### `test_solver_selection`
Validates appropriate solver selection based on configuration and problem.

#### `test_error_handling`
Ensures robust error handling with invalid inputs.

#### `test_hash_input`
Validates deterministic SHA-256 hashing of canonical inputs.

#### `test_multiple_objectives`
Tests multi-objective optimization with weighted objectives.

**Running Tests:**
```bash
# All orchestrator tests
pytest tests/test_orchestrator.py -v

# Specific test
pytest tests/test_orchestrator.py::test_basic_optimization -v

# With coverage
pytest tests/test_orchestrator.py --cov=core --cov-report=html
```

## Test Structure

### Fixtures

**Configuration Fixtures:**
```python
@pytest.fixture
def edge_config():
    """Load edge deployment configuration."""
    config_path = Path(__file__).parent.parent / 'config' / 'deployment-edge.yaml'
    with open(config_path) as f:
        return yaml.safe_load(f)
```

**Problem Fixtures:**
```python
@pytest.fixture
def sample_problem():
    """Sample optimization problem."""
    return {
        'problem_type': 'vehicle_routing',
        'variables': [...],
        'constraints': [...],
        'objectives': [...]
    }
```

### Test Patterns

**Async Tests:**
```python
@pytest.mark.asyncio
async def test_basic_optimization(edge_config, sample_problem):
    orchestrator = QAIM2Orchestrator(edge_config)
    result = await orchestrator.optimize(sample_problem, constraints)
    assert result['status'] in ['optimal', 'feasible']
```

**Error Tests:**
```python
@pytest.mark.asyncio
async def test_error_handling(edge_config):
    orchestrator = QAIM2Orchestrator(edge_config)
    result = await orchestrator.optimize(invalid_problem, {})
    assert result['status'] == 'error'
    assert 'evidence' in result
```

## Running Tests

### All Tests

```bash
# Run all tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=. --cov-report=html

# Parallel execution
pytest tests/ -n auto
```

### Specific Tests

```bash
# Orchestrator only
pytest tests/test_orchestrator.py -v

# Specific test function
pytest tests/test_orchestrator.py::test_basic_optimization -v

# Tests matching pattern
pytest tests/ -k "optimization" -v
```

### Test Markers

```bash
# Run only fast tests
pytest tests/ -m "not slow" -v

# Run integration tests
pytest tests/ -m integration -v

# Skip certain tests
pytest tests/ -m "not expensive" -v
```

## Test Coverage

### Current Coverage

Target coverage levels:
- **Core orchestrator:** > 95%
- **AI bridges:** > 90%
- **Solver pools:** > 85%
- **Overall:** > 90%

### Generate Coverage Report

```bash
# HTML report
pytest tests/ --cov=. --cov-report=html
open htmlcov/index.html

# Terminal report
pytest tests/ --cov=. --cov-report=term

# XML report (for CI)
pytest tests/ --cov=. --cov-report=xml
```

## Test Configuration

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
asyncio_mode = auto
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    expensive: marks tests that use paid resources
```

### conftest.py

Common fixtures and configuration:

```python
# conftest.py
import pytest
import yaml
from pathlib import Path

@pytest.fixture(scope="session")
def config_dir():
    return Path(__file__).parent.parent / 'config'

@pytest.fixture
def edge_config(config_dir):
    with open(config_dir / 'deployment-edge.yaml') as f:
        return yaml.safe_load(f)
```

## Test Data

### Sample Problems

Test data in `tests/data/`:
- `vehicle_routing.json` - VRP problem
- `scheduling.json` - Job shop problem
- `portfolio.json` - Portfolio optimization

### Expected Results

Golden outputs in `tests/expected/`:
- `vehicle_routing_result.json` - Expected VRP result
- `evidence_structure.json` - Expected evidence format

## Continuous Integration

### GitHub Actions

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: pytest tests/ --cov=. --cov-report=xml
      - uses: codecov/codecov-action@v2
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pytest-check
        name: pytest
        entry: pytest
        args: [tests/, -v]
        language: system
        pass_filenames: false
```

## Test Development

### Adding New Tests

1. Create test file: `test_<module>.py`
2. Import necessary fixtures
3. Write test functions with `test_` prefix
4. Use async for async code
5. Add assertions
6. Document test purpose

**Example:**
```python
@pytest.mark.asyncio
async def test_new_feature(edge_config):
    """Test description here."""
    orchestrator = QAIM2Orchestrator(edge_config)
    # Test logic
    assert expected_condition
```

### Test Best Practices

1. **One assertion per test** (when possible)
2. **Clear test names** describing what is tested
3. **Arrange-Act-Assert** pattern
4. **Use fixtures** for common setup
5. **Mock external dependencies** (quantum providers, etc.)
6. **Test edge cases** and error conditions

## Mocking

### Mock Solvers

```python
from unittest.mock import Mock, AsyncMock

@pytest.fixture
def mock_cb_pool():
    pool = Mock()
    pool.solve = AsyncMock(return_value=SolverResult(...))
    return pool
```

### Mock Quantum Providers

```python
@pytest.fixture
def mock_ibm_quantum():
    provider = Mock()
    provider.execute = AsyncMock(return_value={...})
    return provider
```

## Performance Tests

### Benchmark Tests

```python
@pytest.mark.benchmark
def test_optimization_performance(benchmark, edge_config):
    result = benchmark(run_optimization, edge_config)
    assert result['solve_time'] < 1.0  # Should complete in < 1s
```

### Load Tests

```python
@pytest.mark.slow
@pytest.mark.asyncio
async def test_concurrent_requests():
    """Test handling multiple concurrent optimizations."""
    tasks = [orchestrator.optimize(problem, {}) for _ in range(10)]
    results = await asyncio.gather(*tasks)
    assert all(r['status'] == 'optimal' for r in results)
```

## Debugging Tests

### Verbose Output

```bash
# Show print statements
pytest tests/ -v -s

# Show local variables on failure
pytest tests/ -v -l

# Drop into debugger on failure
pytest tests/ --pdb
```

### Test Profiling

```bash
# Profile test execution
pytest tests/ --profile

# Profile with cProfile
python -m cProfile -o profile.stats -m pytest tests/
```

## References

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [example.py](../example.py) - Working example for reference

---

*QAIM-2 Test Suite*  
*Framework: pytest + pytest-asyncio*  
*Target Coverage: > 90%*  
*Last Updated: 2025-10-03*
