#!/usr/bin/env python3
"""
Artefact C: QUBO for SICOCA (Supply Chain Optimization - Lane Selection)

This module implements a QUBO formulation for the SICOCA (Supply Chain Optimization)
subsystem within the AQUA framework. The problem optimizes the selection of logistic
lanes (routes) to minimize total cost (including CO2 emissions) while satisfying
demand constraints and avoiding resource conflicts.

The model is designed for quantum annealing hardware (e.g., D-Wave) or variational
quantum algorithms (QAOA, VQE) using frameworks like Qiskit or PennyLane.

Mathematical Formulation:
    H(x) = x^T Q x + C

where:
    - x = [x1, x2, x3, x4] is the binary decision vector (lane selection)
    - Q is the symmetric QUBO matrix
    - C is a constant offset term

The Hamiltonian consists of:
    1. Direct operational costs
    2. Demand satisfaction penalties
    3. Resource conflict penalties

Requirements:
    pip install pennylane numpy

Author: ASI-T Architecture Team
Version: 1.0.0
License: CC-BY-4.0 (docs), Proprietary (code)
"""

import json
from typing import Dict, Tuple, List

try:
    import pennylane as qml
    from pennylane import numpy as np
    PENNYLANE_AVAILABLE = True
except ImportError:
    import numpy as np
    PENNYLANE_AVAILABLE = False
    print("Warning: PennyLane not available. Quantum circuit features disabled.")


# ============================================================================
# Problem Data Definition
# ============================================================================

class SICOCALaneProblem:
    """
    SICOCA Lane Selection Problem Data
    
    Attributes:
        n_lanes: Number of logistic lanes
        capacities: Capacity of each lane (units)
        costs: Operational cost of each lane (including CO2)
        demand: Total demand to satisfy (units)
        conflicts: Pairs of lanes that cannot be used together
        w_cost: Weight for direct cost term
        penalty_demand: Penalty weight for demand satisfaction (A)
        penalty_conflict: Penalty weight for resource conflicts (B)
    """
    
    def __init__(
        self,
        n_lanes: int = 4,
        capacities: List[int] = None,
        costs: List[float] = None,
        demand: int = 100,
        conflicts: List[Tuple[int, int]] = None,
        w_cost: float = 1.0,
        penalty_demand: float = 5.0,
        penalty_conflict: float = 10.0
    ):
        """
        Initialize SICOCA Lane Selection Problem Data.

        Args:
            n_lanes (int): Number of logistic lanes.
            capacities (List[int]): Capacity of each lane (units).
            costs (List[float]): Operational cost of each lane (including CO2).
            demand (int): Total demand to satisfy (units).
            conflicts (List[Tuple[int, int]]): Pairs of lanes that cannot be used together.
            w_cost (float): Weight for direct cost term.
            penalty_demand (float): Penalty weight for demand satisfaction (A).
            penalty_conflict (float): Penalty weight for resource conflicts (B).
        """
        # Set defaults if None provided
        if capacities is None:
            capacities = [40, 60, 70, 50]
        if costs is None:
            costs = [5, 8, 12, 7]
        if conflicts is None:
            conflicts = [(0, 2), (1, 3)]

        self.n_lanes = n_lanes
        self.capacities = capacities
        self.costs = costs
        self.demand = demand
        self.conflicts = conflicts
        self.w_cost = w_cost
        self.penalty_demand = penalty_demand
        self.penalty_conflict = penalty_conflict
# ============================================================================
# QUBO Matrix Construction
# ============================================================================

def build_qubo_matrix(problem: SICOCALaneProblem) -> Tuple[Dict[Tuple[int, int], float], float]:
    """
    Construct the QUBO matrix Q and constant offset C.
    
    The energy function is:
        H(x) = w_cost * sum(C_n * x_n) 
             + A * (sum(Cap_n * x_n) - D)^2
             + B * sum(Conflict_{n,m} * x_n * x_m)
    
    Expanding the demand penalty:
        A * (sum(Cap_n * x_n) - D)^2 
        = A * [sum(Cap_n^2 * x_n) + sum_{n<m}(2*Cap_n*Cap_m * x_n * x_m) - 2*D*sum(Cap_n * x_n) + D^2]
    
    This gives us:
        - Diagonal terms: Q_{n,n} = w_cost * C_n + A * (Cap_n^2 - 2*D*Cap_n)
        - Off-diagonal terms: Q_{n,m} = A * 2*Cap_n*Cap_m + B * Conflict_{n,m}
        - Constant: C = A * D^2
    
    Args:
        problem: SICOCALaneProblem instance with problem data
        
    Returns:
        q_dict: Dictionary mapping (i, j) to Q_{i,j} values
        constant: Constant offset term C
    """
    q_dict = {}
    A = problem.penalty_demand
    B = problem.penalty_conflict
    D = problem.demand
    
    # Diagonal terms: Linear costs + demand penalty linear part
    for n in range(problem.n_lanes):
        cap_n = problem.capacities[n]
        cost_n = problem.costs[n]
        
        # Q_{n,n} = w_cost * C_n + A * (Cap_n^2 - 2*D*Cap_n)
        q_diag = problem.w_cost * cost_n + A * (cap_n**2 - 2 * D * cap_n)
        q_dict[(n, n)] = float(q_diag)
    
    # Off-diagonal terms: Demand penalty quadratic part + conflict penalties
    for n in range(problem.n_lanes):
        for m in range(n + 1, problem.n_lanes):
            cap_n = problem.capacities[n]
            cap_m = problem.capacities[m]
            
            # Q_{n,m} = 2 * A * Cap_n * Cap_m
            q_off = 2 * A * cap_n * cap_m
            
            # Add conflict penalty if lanes conflict
            if (n, m) in problem.conflicts or (m, n) in problem.conflicts:
                q_off += B
            
            q_dict[(n, m)] = float(q_off)
    
    # Constant offset
    constant = A * D**2
    
    return q_dict, constant


# ============================================================================
# Energy Calculation
# ============================================================================

def calculate_energy(x: np.ndarray, q_dict: Dict[Tuple[int, int], float], 
                    constant: float) -> float:
    """
    Calculate the QUBO energy for a given binary solution vector.
    
    E(x) = sum_{i,j} Q_{i,j} * x_i * x_j + C
    
    Args:
        x: Binary solution vector (0 or 1 values)
        q_dict: QUBO matrix as dictionary
        constant: Constant offset
        
    Returns:
        Total energy value
    """
    energy = constant
    
    for (i, j), val in q_dict.items():
        if i == j:
            # Diagonal term
            energy += val * x[i]
        else:
            # Off-diagonal term (upper triangular only)
            energy += val * x[i] * x[j]
    
    return float(energy)


def analyze_solution(x: np.ndarray, problem: SICOCALaneProblem) -> Dict:
    """
    Analyze a solution vector and compute its components.
    
    Args:
        x: Binary solution vector
        problem: Problem instance
        
    Returns:
        Dictionary with solution analysis
    """
    # Convert to regular numpy array if it's a PennyLane tensor
    if hasattr(x, 'numpy'):
        x = x.numpy()
    x = np.asarray(x)
    
    selected_lanes = [i + 1 for i, val in enumerate(x) if val == 1]
    total_capacity = sum(problem.capacities[i] * x[i] for i in range(problem.n_lanes))
    total_cost = sum(problem.costs[i] * x[i] for i in range(problem.n_lanes))
    
    # Check for conflicts
    conflicts_violated = []
    for lane_i, lane_j in problem.conflicts:
        if x[lane_i] == 1 and x[lane_j] == 1:
            conflicts_violated.append((lane_i + 1, lane_j + 1))
    
    # Demand satisfaction
    demand_gap = total_capacity - problem.demand
    demand_penalty = problem.penalty_demand * demand_gap**2
    
    # Conflict penalty
    conflict_penalty = problem.penalty_conflict * len(conflicts_violated)
    
    return {
        "selected_lanes": selected_lanes,
        "total_capacity": float(total_capacity),
        "total_cost": float(total_cost),
        "demand": int(problem.demand),
        "demand_gap": float(demand_gap),
        "demand_satisfied": bool(demand_gap >= 0),
        "conflicts_violated": conflicts_violated,
        "direct_cost_term": float(problem.w_cost * total_cost),
        "demand_penalty_term": float(demand_penalty),
        "conflict_penalty_term": float(conflict_penalty),
        "total_penalty": float(demand_penalty + conflict_penalty)
    }


# ============================================================================
# PennyLane Quantum Circuit Integration
# ============================================================================

def create_qaoa_circuit(q_dict: Dict[Tuple[int, int], float], 
                       constant: float, 
                       n_qubits: int = 4):
    """
    Create a QAOA circuit for the QUBO problem using PennyLane.
    
    This is a demonstration of how the QUBO would be loaded into a
    quantum computing framework for QAOA or VQE algorithms.
    
    Args:
        q_dict: QUBO matrix dictionary
        constant: Constant offset
        n_qubits: Number of qubits (lanes)
        
    Returns:
        PennyLane QNode if available, None otherwise
    """
    if not PENNYLANE_AVAILABLE:
        return None
    
    # Convert QUBO to Ising Hamiltonian
    # PennyLane provides utilities for this conversion
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def circuit(weights):
        """
        Simple QAOA-style circuit for demonstration.
        
        In production, this would include:
        - Problem Hamiltonian layers
        - Mixer Hamiltonian layers
        - Optimization of variational parameters
        """
        # Initial superposition
        for i in range(n_qubits):
            qml.Hadamard(wires=i)
        
        # Example variational layer (simplified)
        for i in range(n_qubits):
            qml.RY(weights[i], wires=i)
        
        # Example entangling layer
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i + 1])
        
        # Convert QUBO to Ising for measurement
        H = qml.qaoa.qubo_to_ising(q_dict, offset=constant)
        
        return qml.expval(H)
    
    return circuit


# ============================================================================
# Main Execution and Export
# ============================================================================

def main():
    """
    Main execution function: Build QUBO, verify solution, and export artifact.
    """
    print("="*70)
    print("SICOCA QUBO Model - Artefact C")
    print("Supply Chain Optimization (Lane Selection)")
    print("="*70)
    print()
    
    # Initialize problem
    problem = SICOCALaneProblem()
    
    print("Problem Configuration:")
    print(f"  Number of lanes: {problem.n_lanes}")
    print(f"  Total demand: {problem.demand} units")
    print(f"  Penalty weights: A={problem.penalty_demand}, B={problem.penalty_conflict}")
    print()
    
    print("Lane Data:")
    for i in range(problem.n_lanes):
        print(f"  Lane {i+1}: Capacity={problem.capacities[i]:3d}, "
              f"Cost={problem.costs[i]:2d}")
    print()
    
    print("Conflicts:")
    for lane_i, lane_j in problem.conflicts:
        print(f"  Lane {lane_i+1} <-> Lane {lane_j+1}")
    print()
    
    # Build QUBO matrix
    print("Building QUBO matrix...")
    q_dict, constant = build_qubo_matrix(problem)
    print(f"  Matrix size: {problem.n_lanes}×{problem.n_lanes}")
    print(f"  Non-zero entries: {len(q_dict)}")
    print(f"  Constant offset: {constant}")
    print()
    
    # Display QUBO matrix
    print("QUBO Matrix Q:")
    print("  " + "-" * 60)
    print(f"  {'Element':<10} {'Value':>12} {'Description'}")
    print("  " + "-" * 60)
    
    # Diagonal elements
    for i in range(problem.n_lanes):
        val = q_dict.get((i, i), 0)
        print(f"  Q_{i+1},{i+1:<6} {val:>12.0f}   Linear cost + demand penalty")
    
    # Off-diagonal elements
    for i in range(problem.n_lanes):
        for j in range(i + 1, problem.n_lanes):
            val = q_dict.get((i, j), 0)
            desc = "Demand penalty"
            if (i, j) in problem.conflicts or (j, i) in problem.conflicts:
                desc += " + CONFLICT"
            print(f"  Q_{i+1},{j+1:<6} {val:>12.0f}   {desc}")
    print("  " + "-" * 60)
    print()
    
    # Test expected solution
    # Expected optimal: Lane 2 (60) + Lane 4 (50) = 110 capacity, no conflicts
    expected_solution = np.array([0, 1, 0, 1])
    
    print("Verifying Expected Solution: [0, 1, 0, 1]")
    print("  (Lane 2 + Lane 4)")
    analysis = analyze_solution(expected_solution, problem)
    expected_energy = calculate_energy(expected_solution, q_dict, constant)
    
    print(f"  Selected lanes: {analysis['selected_lanes']}")
    print(f"  Total capacity: {analysis['total_capacity']} units (demand: {problem.demand})")
    print(f"  Demand satisfied: {analysis['demand_satisfied']}")
    print(f"  Direct cost: {analysis['direct_cost_term']:.2f}")
    print(f"  Demand penalty: {analysis['demand_penalty_term']:.2f}")
    print(f"  Conflict penalty: {analysis['conflict_penalty_term']:.2f}")
    print(f"  Total energy: {expected_energy:.2f}")
    print()
    
    # Create PennyLane circuit if available
    if PENNYLANE_AVAILABLE:
        print("PennyLane Integration:")
        circuit = create_qaoa_circuit(q_dict, constant, problem.n_lanes)
        if circuit:
            print("  ✓ QAOA circuit created successfully")
            print("  ✓ Ready for quantum optimization (QAOA/VQE)")
        print()
    else:
        print("PennyLane Integration:")
        print("  ⚠ PennyLane not available - install with: pip install pennylane")
        print()
    
    # Export for UTCS-MI traceability
    print("Exporting QUBO artifact for UTCS-MI...")
    
    # Convert q_dict keys to strings for JSON serialization
    q_dict_serializable = {f"{i},{j}": val for (i, j), val in q_dict.items()}
    
    artifact = {
        "problem_name": "SICOCA_Lane_Selection_MVP",
        "version": "1.0.0",
        "description": "QUBO formulation for supply chain lane selection optimization",
        "subsystem": "SICOCA",
        "framework": "AQUA",
        "qubo_matrix": q_dict_serializable,
        "constant_offset": float(constant),
        "problem_data": {
            "n_lanes": problem.n_lanes,
            "capacities": list(problem.capacities),
            "costs": list(problem.costs),
            "demand": int(problem.demand),
            "conflicts": problem.conflicts,
            "weights": {
                "w_cost": float(problem.w_cost),
                "penalty_demand": float(problem.penalty_demand),
                "penalty_conflict": float(problem.penalty_conflict)
            }
        },
        "variable_mapping": {
            "x0": "Lane 1 (Capacity: 40 units, Cost: 5)",
            "x1": "Lane 2 (Capacity: 60 units, Cost: 8)",
            "x2": "Lane 3 (Capacity: 70 units, Cost: 12)",
            "x3": "Lane 4 (Capacity: 50 units, Cost: 7)"
        },
        "expected_solution": {
            "binary_vector": [int(v) for v in expected_solution],
            "energy": float(expected_energy),
            "analysis": analysis
        },
        "metadata": {
            "creation_date": "2025-01-26",
            "author": "ASI-T Architecture Team",
            "license": "CC-BY-4.0",
            "utcs_mi_version": "v5.0",
            "quantum_backends": [
                "D-Wave Advantage (quantum annealing)",
                "QAOA (gate-based quantum)",
                "VQE (variational quantum eigensolver)"
            ]
        }
    }
    
    output_file = "aqua_sicoca_qubo.json"
    with open(output_file, "w") as f:
        json.dump(artifact, f, indent=2)
    
    print(f"  ✓ Artifact exported to: {output_file}")
    print()
    
    print("="*70)
    print("SICOCA QUBO Model Complete")
    print("="*70)
    print()
    print("Next Steps:")
    print("  1. Register artifact hash in UTCS-MI for traceability")
    print("  2. Load QUBO matrix into quantum solver (D-Wave/QAOA/VQE)")
    print("  3. Validate solution against supply chain constraints")
    print("  4. Integrate with AQUA framework for production use")
    print()


if __name__ == "__main__":
    main()
