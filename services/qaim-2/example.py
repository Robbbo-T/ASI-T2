#!/usr/bin/env python3
"""
QAIM-2 Example: Simple Optimization

Demonstrates basic usage of QAIM-2 orchestrator with edge configuration.
"""

import asyncio
import sys
from pathlib import Path
import yaml
import json

# Add services directory to path
services_dir = Path(__file__).parent.parent
sys.path.insert(0, str(services_dir))

# Import from qaim-2 package (using underscore for Python import)
import importlib.util
spec = importlib.util.spec_from_file_location(
    "qaim_2",
    Path(__file__).parent / "core" / "qaim_orchestrator.py"
)
qaim_2 = importlib.util.module_from_spec(spec)

# For simplicity, directly import the classes we need
sys.path.insert(0, str(Path(__file__).parent))
from bridges.pcan import ProblemCanonicalizer
from bridges.surrogate_models import SurrogateModels
from bridges.strategy_policy import StrategyPolicy
from bridges.arbitration import Arbitration
from bridges.cross_framework import CrossFrameworkTranslator
from solvers.cb_pool import ClassicalSolverPool
from solvers.qb_pool import CubicBitSolverPool
from solvers.qc_gateway import QuantumGateway
from core.qaim_orchestrator import QAIM2Orchestrator


async def main():
    """Run simple optimization example."""
    
    print("=" * 60)
    print("QAIM-2 Optimization Example")
    print("=" * 60)
    print()
    
    # Load edge configuration
    config_path = Path(__file__).parent / 'config' / 'deployment-edge.yaml'
    print(f"Loading configuration: {config_path}")
    with open(config_path) as f:
        config = yaml.safe_load(f)
    print("✓ Configuration loaded")
    print()
    
    # Create orchestrator
    print("Creating QAIM-2 Orchestrator...")
    orchestrator = QAIM2Orchestrator(config)
    print("✓ Orchestrator initialized")
    print()
    
    # Define optimization problem
    print("Defining optimization problem...")
    problem = {
        'problem_type': 'vehicle_routing',
        'variables': [
            {'name': 'route_1', 'type': 'binary'},
            {'name': 'route_2', 'type': 'binary'},
            {'name': 'route_3', 'type': 'binary'}
        ],
        'constraints': [
            {
                'type': 'capacity',
                'value': 100,
                'unit': 'kg',
                'sense': '<='
            }
        ],
        'objectives': [
            {
                'name': 'minimize_distance',
                'sense': 'minimize',
                'weight': 1.0
            }
        ]
    }
    
    constraints = {
        'time_limit': 60,
        'gap_tolerance': 0.01
    }
    
    metadata = {
        'domain': 'logistics',
        'ata_chapter': 'ATA-34',
        'classification': 'INTERNAL',
        'requester': 'example_user'
    }
    
    print("Problem type:", problem['problem_type'])
    print("Variables:", len(problem['variables']))
    print("Constraints:", len(problem['constraints']))
    print("Objectives:", len(problem['objectives']))
    print()
    
    # Solve
    print("Solving optimization problem...")
    print("-" * 60)
    result = await orchestrator.optimize(
        problem=problem,
        constraints=constraints,
        metadata=metadata
    )
    print("-" * 60)
    print()
    
    # Display results
    print("RESULTS:")
    print("=" * 60)
    print(f"Request ID:      {result['request_id']}")
    print(f"Status:          {result['status']}")
    print(f"Solver:          {result['solver']}")
    print(f"Solution:        {json.dumps(result['solution'], indent=2)}")
    print()
    
    print("METRICS:")
    print("-" * 60)
    metrics = result['metrics']
    print(f"Objective Value: {metrics.get('objective_value', 'N/A')}")
    print(f"Gap:             {metrics.get('gap', 'N/A')}")
    print(f"Solve Time:      {metrics.get('solve_time', 'N/A')}s")
    print(f"Feasible:        {metrics.get('feasible', 'N/A')}")
    print()
    
    print("EVIDENCE (UTCS v5.0):")
    print("-" * 60)
    evidence = result['evidence']
    print(f"Version:         {evidence['version']}")
    print(f"Timestamp:       {evidence['timestamp']}")
    print(f"Duration:        {evidence['duration_ms']}ms")
    print(f"Input Hash:      {evidence.get('input_hash', 'N/A')[:16]}...")
    print()
    
    provenance = evidence['provenance']
    print("PROVENANCE:")
    print(f"  Bridge:        {provenance['bridge']}")
    print(f"  Ethics:        {provenance['ethics']}")
    print(f"  UTCS:          {provenance['utcs_version']}")
    print(f"  Framework:     {provenance['framework']}")
    print()
    
    print("=" * 60)
    print("✓ Example completed successfully")
    print("=" * 60)


if __name__ == '__main__':
    asyncio.run(main())
