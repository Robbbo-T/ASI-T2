"""
Test QAIM-2 Orchestrator

Tests for main orchestration logic and end-to-end optimization flows.
"""

import pytest
import asyncio
from unittest.mock import Mock, AsyncMock
import yaml
from pathlib import Path


# Import orchestrator
from core.qaim_orchestrator import QAIM2Orchestrator


@pytest.fixture
def edge_config():
    """Load edge deployment configuration."""
    config_path = Path(__file__).parent.parent / 'config' / 'deployment-edge.yaml'
    with open(config_path) as f:
        return yaml.safe_load(f)


@pytest.fixture
def sample_problem():
    """Sample optimization problem."""
    return {
        'problem_type': 'vehicle_routing',
        'variables': [
            {'name': 'x1', 'type': 'binary'},
            {'name': 'x2', 'type': 'binary'},
            {'name': 'x3', 'type': 'binary'}
        ],
        'constraints': [
            {'type': 'capacity', 'value': 100, 'unit': 'kg', 'sense': '<='}
        ],
        'objectives': [
            {'name': 'minimize_distance', 'sense': 'minimize', 'weight': 1.0}
        ]
    }


@pytest.fixture
def sample_constraints():
    """Sample optimization constraints."""
    return {
        'time_limit': 60,
        'gap_tolerance': 0.01
    }


@pytest.mark.asyncio
async def test_orchestrator_initialization(edge_config):
    """Test orchestrator initialization with configuration."""
    orchestrator = QAIM2Orchestrator(edge_config)
    
    assert orchestrator.config == edge_config
    assert orchestrator.pcan is not None
    assert orchestrator.surrogate is not None
    assert orchestrator.strategy is not None
    assert orchestrator.arbitration is not None
    assert orchestrator.translator is not None
    assert orchestrator.cb_pool is not None
    assert orchestrator.qb_pool is not None


@pytest.mark.asyncio
async def test_basic_optimization(edge_config, sample_problem, sample_constraints):
    """Test basic optimization flow."""
    orchestrator = QAIM2Orchestrator(edge_config)
    
    result = await orchestrator.optimize(
        problem=sample_problem,
        constraints=sample_constraints,
        metadata={'domain': 'logistics', 'ata_chapter': 'ATA-34'}
    )
    
    # Check result structure
    assert 'request_id' in result
    assert 'solver' in result
    assert 'solution' in result
    assert 'metrics' in result
    assert 'evidence' in result
    assert 'status' in result
    
    # Check evidence UTCS v5.0
    evidence = result['evidence']
    assert evidence['version'] == 'utcs-v5.0'
    assert evidence['provenance']['bridge'] == 'QS→FWD→UE→FE→CB→QB'
    assert evidence['provenance']['ethics'] == 'MAP-EEM · MAL-EEM'
    assert evidence['provenance']['utcs_version'] == 'v5.0'


@pytest.mark.asyncio
async def test_solver_selection(edge_config, sample_problem, sample_constraints):
    """Test that appropriate solver is selected."""
    orchestrator = QAIM2Orchestrator(edge_config)
    
    result = await orchestrator.optimize(
        problem=sample_problem,
        constraints=sample_constraints
    )
    
    # Edge config should use classical solvers
    assert result['solver'].startswith('cb_')
    assert result['status'] in ['optimal', 'feasible', 'infeasible', 'timeout', 'error']


@pytest.mark.asyncio
async def test_error_handling(edge_config):
    """Test error handling with invalid problem."""
    orchestrator = QAIM2Orchestrator(edge_config)
    
    # Invalid problem (missing required fields)
    invalid_problem = {
        'problem_type': 'unknown_type'
    }
    
    result = await orchestrator.optimize(
        problem=invalid_problem,
        constraints={}
    )
    
    # Should return error status with evidence
    assert result['status'] == 'error'
    assert 'evidence' in result
    assert result['solution'] is None


@pytest.mark.asyncio
async def test_hash_input():
    """Test input hashing for evidence."""
    config = {'pcan': {}, 'surrogate': {}, 'strategy': {}, 'arbitration': {}, 
              'translator': {}, 'cb_solvers': {}, 'qb_solvers': {}}
    orchestrator = QAIM2Orchestrator(config)
    
    canonical = {
        'problem_type': 'test',
        'variables': [{'name': 'x1'}],
        'constraints': [],
        'objectives': []
    }
    
    hash1 = orchestrator._hash_input(canonical)
    hash2 = orchestrator._hash_input(canonical)
    
    # Hash should be deterministic
    assert hash1 == hash2
    assert len(hash1) == 64  # SHA-256 produces 64 hex characters


@pytest.mark.asyncio
async def test_multiple_objectives(edge_config):
    """Test multi-objective optimization."""
    orchestrator = QAIM2Orchestrator(edge_config)
    
    problem = {
        'problem_type': 'scheduling',
        'variables': [
            {'name': 't1', 'type': 'continuous'},
            {'name': 't2', 'type': 'continuous'}
        ],
        'constraints': [],
        'objectives': [
            {'name': 'minimize_time', 'sense': 'minimize', 'weight': 0.6},
            {'name': 'minimize_cost', 'sense': 'minimize', 'weight': 0.4}
        ]
    }
    
    result = await orchestrator.optimize(
        problem=problem,
        constraints={'time_limit': 30}
    )
    
    assert result['status'] in ['optimal', 'feasible', 'timeout']
    assert 'evidence' in result


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
