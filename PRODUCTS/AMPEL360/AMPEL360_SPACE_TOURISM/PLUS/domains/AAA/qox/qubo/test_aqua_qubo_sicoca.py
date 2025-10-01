#!/usr/bin/env python3
"""
Test suite for SICOCA QUBO implementation.

This script validates the QUBO matrix construction, energy calculations,
and JSON artifact generation for the SICOCA lane selection problem.
"""

import sys
import json
from pathlib import Path

# Add the parent directory to the path to import the module
sys.path.insert(0, str(Path(__file__).parent))

from aqua_qubo_sicoca import (
    SICOCALaneProblem,
    build_qubo_matrix,
    calculate_energy,
    analyze_solution
)

try:
    import numpy as np
except ImportError:
    print("Error: NumPy is required for testing")
    sys.exit(1)


def test_qubo_matrix_values():
    """Test that QUBO matrix values match the problem specification."""
    print("Testing QUBO matrix construction...")
    
    problem = SICOCALaneProblem()
    q_dict, constant = build_qubo_matrix(problem)
    
    # Expected values from problem statement
    expected_diagonal = {
        (0, 0): -31995,
        (1, 1): -41992,
        (2, 2): -45488,
        (3, 3): -37493
    }
    
    expected_off_diagonal = {
        (0, 1): 24000,
        (0, 2): 28010,  # Includes conflict penalty
        (0, 3): 20000,
        (1, 2): 42000,
        (1, 3): 30010,  # Includes conflict penalty
        (2, 3): 35000
    }
    
    expected_constant = 50000
    
    # Check diagonal elements
    for key, expected_val in expected_diagonal.items():
        actual_val = q_dict[key]
        assert abs(actual_val - expected_val) < 1e-6, \
            f"Diagonal Q{key} mismatch: expected {expected_val}, got {actual_val}"
    
    # Check off-diagonal elements
    for key, expected_val in expected_off_diagonal.items():
        actual_val = q_dict[key]
        assert abs(actual_val - expected_val) < 1e-6, \
            f"Off-diagonal Q{key} mismatch: expected {expected_val}, got {actual_val}"
    
    # Check constant
    assert abs(constant - expected_constant) < 1e-6, \
        f"Constant mismatch: expected {expected_constant}, got {constant}"
    
    print("  ✓ All QUBO matrix values correct")


def test_expected_solution():
    """Test that the expected solution produces the correct energy."""
    print("Testing expected solution energy...")
    
    problem = SICOCALaneProblem()
    q_dict, constant = build_qubo_matrix(problem)
    
    # Expected optimal solution: Lane 2 + Lane 4
    solution = np.array([0, 1, 0, 1])
    
    # Calculate energy
    energy = calculate_energy(solution, q_dict, constant)
    
    # Expected energy from problem statement:
    # C + Q22 + Q44 + Q24 = 50000 + (-41992) + (-37493) + 30010 = 525
    expected_energy = 525.0
    
    assert abs(energy - expected_energy) < 1e-6, \
        f"Energy mismatch: expected {expected_energy}, got {energy}"
    
    print(f"  ✓ Expected solution energy correct: {energy}")


def test_solution_analysis():
    """Test solution analysis components."""
    print("Testing solution analysis...")
    
    problem = SICOCALaneProblem()
    solution = np.array([0, 1, 0, 1])
    
    analysis = analyze_solution(solution, problem)
    
    # Verify components
    assert analysis['selected_lanes'] == [2, 4], \
        f"Selected lanes mismatch: {analysis['selected_lanes']}"
    
    assert analysis['total_capacity'] == 110.0, \
        f"Total capacity mismatch: {analysis['total_capacity']}"
    
    assert analysis['total_cost'] == 15.0, \
        f"Total cost mismatch: {analysis['total_cost']}"
    
    assert analysis['demand_satisfied'] == True, \
        f"Demand satisfaction incorrect: {analysis['demand_satisfied']}"
    
    assert len(analysis['conflicts_violated']) == 1, \
        f"Conflict count incorrect: {len(analysis['conflicts_violated'])}"
    
    assert analysis['direct_cost_term'] == 15.0, \
        f"Direct cost term mismatch: {analysis['direct_cost_term']}"
    
    assert abs(analysis['demand_penalty_term'] - 500.0) < 1e-6, \
        f"Demand penalty mismatch: {analysis['demand_penalty_term']}"
    
    assert abs(analysis['conflict_penalty_term'] - 10.0) < 1e-6, \
        f"Conflict penalty mismatch: {analysis['conflict_penalty_term']}"
    
    print("  ✓ Solution analysis components correct")


def test_json_artifact():
    """Test that JSON artifact exists and is valid."""
    print("Testing JSON artifact...")
    
    artifact_path = Path(__file__).parent / "aqua_sicoca_qubo.json"
    
    assert artifact_path.exists(), \
        f"JSON artifact not found at {artifact_path}"
    
    with open(artifact_path, 'r') as f:
        artifact = json.load(f)
    
    # Verify required fields
    required_fields = [
        'problem_name',
        'version',
        'qubo_matrix',
        'constant_offset',
        'problem_data',
        'variable_mapping',
        'expected_solution',
        'metadata'
    ]
    
    for field in required_fields:
        assert field in artifact, f"Missing required field: {field}"
    
    # Verify QUBO matrix has 10 elements (4 diagonal + 6 off-diagonal)
    assert len(artifact['qubo_matrix']) == 10, \
        f"QUBO matrix should have 10 elements, got {len(artifact['qubo_matrix'])}"
    
    # Verify expected solution
    expected_vector = artifact['expected_solution']['binary_vector']
    assert expected_vector == [0, 1, 0, 1], \
        f"Expected solution vector mismatch: {expected_vector}"
    
    expected_energy = artifact['expected_solution']['energy']
    assert abs(expected_energy - 525.0) < 1e-6, \
        f"Expected solution energy mismatch: {expected_energy}"
    
    print("  ✓ JSON artifact valid and complete")


def test_alternative_solutions():
    """Test energy calculation for other solution configurations."""
    print("Testing alternative solutions...")
    
    problem = SICOCALaneProblem()
    q_dict, constant = build_qubo_matrix(problem)
    
    # Test a few other solutions
    test_cases = [
        ([1, 0, 0, 0], "Lane 1 only"),
        ([0, 1, 0, 0], "Lane 2 only"),
        ([1, 1, 0, 0], "Lane 1 + 2"),
        ([0, 0, 1, 1], "Lane 3 + 4")
    ]
    
    for solution, description in test_cases:
        solution_array = np.array(solution)
        energy = calculate_energy(solution_array, q_dict, constant)
        analysis = analyze_solution(solution_array, problem)
        
        # Just verify calculation completes without errors
        print(f"  ✓ {description}: energy = {energy:.1f}")
    
    print("  ✓ Alternative solutions calculated successfully")


def main():
    """Run all tests."""
    print("="*70)
    print("SICOCA QUBO Test Suite")
    print("="*70)
    print()
    
    tests = [
        test_qubo_matrix_values,
        test_expected_solution,
        test_solution_analysis,
        test_json_artifact,
        test_alternative_solutions
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
            print()
        except AssertionError as e:
            print(f"  ✗ FAILED: {e}")
            failed += 1
            print()
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            failed += 1
            print()
    
    print("="*70)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*70)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
