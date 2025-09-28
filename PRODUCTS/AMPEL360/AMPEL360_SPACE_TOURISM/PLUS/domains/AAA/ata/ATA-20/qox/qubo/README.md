---
id: ASIT-PLUS-AAA-QOX-QUBO-OV-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/ATA-20/qox/qubo/README.md
llc: SYSTEMS
title: "QOx — QUBO Standard (Quadratic Unconstrained Binary Optimization)"
configuration: baseline
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "0.1.0"
release_date: 2025-09-26
maintainer: "ASI-T Architecture Team"
licenses:
  docs: "CC-BY-4.0"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
provenance:
  policy_hash: "sha256:TBD"
  model_sha: "sha256:TBD"
  data_manifest_hash: "sha256:TBD"
  operator_id: "UTCS:OP:copilot-gen"
---

# QOx — QUBO Standard

## 1) Purpose & Scope
This specification standardizes how **discrete engineering decisions** in AMPEL360 PLUS are encoded as **QUBO** problems for quantum/classical optimization. It defines the canonical mathematical form, exchange formats, penalty policies, V&V, and acceptance criteria—ensuring **auditable, reproducible** optimization evidence across QOx backends (Annealing, Digital Annealing, SA, QAOA).

**In-scope examples:** TPS tiling & seam routing, hinge/actuator discrete placement, topology switches, one-hot choices, scheduling & mode sequencing.  
**Out-of-scope:** Continuous physics models (handled in CAx/VP/LCC), certification basis, and control-law tuning.

## 2) Canonical Form & Relationship to BQM
A QUBO minimizes:
```
min_{x∈{0,1}^n} f(x) = x^T Q x + c
```
where `Q ∈ ℝ^{n×n}` is upper-triangular (diagonal holds linear terms), and `c` is a constant offset.

- **Equivalence to BQM:**  
  BQM linear terms `hᵢ` map to `Qᵢᵢ=hᵢ`; quadratic terms `Jᵢⱼ` map to `Qᵢⱼ=Jᵢⱼ` for `i<j`.  
  BQM (spin) ↔ QUBO (binary) conversions must record the **scale** and **offset** used.

## 3) Standard Constraint Handling

**Hard Constraints** (feasibility-critical, safety):  
Penalty weight `λ_hard ≥ 50× max|objective terms|`

**Soft Constraints** (preferences, optimization targets):  
Penalty weight `λ_soft ≤ 10× max|objective terms|`

**Common constraint patterns:**
- **One-hot selection:** `Σᵢ xᵢ = 1` → penalty `λ(Σᵢ xᵢ - 1)²`
- **Cardinality bounds:** `k₁ ≤ Σᵢ xᵢ ≤ k₂` → penalty `λ max{0, k₁ - Σᵢ xᵢ}² + λ max{0, Σᵢ xᵢ - k₂}²`
- **Logical implications:** `xᵢ → xⱼ` → penalty `λ xᵢ(1-xⱼ)`
- **Spatial constraints:** adjacency, exclusion zones via penalty matrices

---

## 4) Variable Encoding Standards

**Binary Variables (`x ∈ {0,1}`):**
- **Design choices:** Component on/off, material selection (one-hot)
- **Placement decisions:** Location selection, routing choices
- **Operational modes:** System state, sequence selection

**Variable naming convention:**
```
x[system]_[component]_[attribute]_[index]
Examples:
- x_tps_tile_active_047: TPS tile 47 is active
- x_gear_actuator_type_2: Actuator type 2 selected for landing gear
- x_route_path_segment_15: Path segment 15 selected in routing
```

**Index Management:**
- **Global indexing:** Unique variable numbers across entire problem
- **Block structure:** Group related variables for efficient solving
- **Mapping tables:** Variable index ↔ engineering parameter relationships

---

## 5) Problem Construction Workflow

### Step 1: Engineering Model → Mathematical Variables
1. **Identify discrete decisions:** Component selections, topology choices, schedules
2. **Define variable domains:** Binary, one-hot, combinatorial structures
3. **Establish constraints:** Safety requirements, physical limitations, preferences
4. **Quantify objectives:** Performance metrics, cost functions, multi-objective weights

### Step 2: QUBO Matrix Construction
1. **Linear terms:** Direct costs/benefits → diagonal elements `Qᵢᵢ`
2. **Quadratic interactions:** Coupling effects → off-diagonal elements `Qᵢⱼ`
3. **Constraint penalties:** Add penalty terms with appropriate weights
4. **Normalization:** Scale problem to avoid numerical issues

### Step 3: Validation & Quality Control
1. **Constraint verification:** Test penalty formulations with known violations
2. **Objective scaling:** Ensure balanced influence of different terms
3. **Feasibility checking:** Verify that feasible solutions exist
4. **Sensitivity analysis:** Test robustness to parameter variations

---

## 6) Exchange Formats & Data Standards

**QUBO JSON Format:**
```json
{
  "version": "1.0",
  "problem_id": "PLUS-TPS-LAYOUT-001",
  "variables": {
    "count": 150,
    "names": ["x_tps_tile_001", "x_tps_tile_002", ...],
    "domains": ["{0,1}", "{0,1}", ...]
  },
  "objective": {
    "linear": {"0": -5.2, "1": 3.1, ...},
    "quadratic": {"0,1": 2.5, "0,5": -1.8, ...},
    "constant": 10.0
  },
  "constraints": {
    "hard": [{"type": "cardinality", "variables": [0,1,2], "bounds": [1,1]}],
    "soft": [{"type": "preference", "weight": 0.5, "expression": "..."}]
  },
  "metadata": {
    "creation_date": "2025-09-26",
    "author": "PLUS-optimization-team",
    "engineering_context": "TPS tile layout optimization for thermal protection"
  }
}
```

**Binary Solution Format:**
```json
{
  "solution_id": "PLUS-TPS-LAYOUT-001-SOL-001",
  "variables": [1, 0, 1, 0, 1, ...],
  "objective_value": -127.5,
  "constraint_violations": [],
  "energy": -127.5,
  "solving_time": 2.3,
  "backend": "D-Wave-Advantage",
  "validation_status": "PASSED"
}
```

---

## 7) Solution Validation & Acceptance

**Mathematical Validation:**
- **Constraint satisfaction:** All hard constraints must be satisfied
- **Objective verification:** Computed objective matches expected value
- **Feasibility check:** Solution lies within valid engineering domain

**Engineering Validation:**
- **Physical realizability:** Solution can be implemented in hardware
- **Performance verification:** Meets functional requirements
- **Safety assessment:** No safety-critical constraints violated

**Quality Metrics:**
- **Solution quality:** Objective value relative to known bounds
- **Robustness:** Stability under small perturbations
- **Reproducibility:** Consistent results across multiple runs

---

## 8) Integration with QOx Backends

**Annealing Integration:**
- **D-Wave Ocean SDK:** Direct QUBO submission to quantum annealers
- **Parameter tuning:** Chain strength, annealing schedule optimization
- **Post-processing:** Sample filtering, constraint checking

**QAOA Integration:**
- **Hamiltonian construction:** QUBO → Pauli-Z cost Hamiltonian
- **Circuit parameterization:** Optimization parameter initialization
- **Expectation evaluation:** Quantum circuit measurement processing

**Classical Solvers:**
- **Gurobi/CPLEX:** Mixed-integer programming formulations
- **Simulated annealing:** Classical optimization baselines
- **Tabu search:** Local optimization with memory structures

---

## 9) Performance Standards & Benchmarking

**Solution Quality Requirements:**
- **Hard constraint satisfaction:** 100% compliance required
- **Soft constraint performance:** Target satisfaction levels defined per problem
- **Objective improvement:** Minimum improvement over baseline solutions

**Computational Performance:**
- **Time-to-solution limits:** Problem-dependent maximum solving time
- **Resource utilization:** Quantum/classical resource consumption tracking
- **Scalability benchmarks:** Performance vs. problem size relationships

**Comparison Standards:**
- **Classical baselines:** Required comparison with state-of-the-art classical methods
- **Historical performance:** Tracking improvement over time
- **Cross-backend validation:** Consistent results across different solvers

---

## 10) Documentation & Traceability

**Problem Documentation:**
- **Engineering context:** Clear description of optimization objectives
- **Variable definitions:** Mapping between mathematical and physical variables
- **Constraint justification:** Engineering rationale for all constraints

**Solution Documentation:**
- **Optimization log:** Complete record of solution process
- **Validation results:** Mathematical and engineering verification
- **Performance metrics:** Solution quality and computational efficiency

**Configuration Management:**
- **Version control:** Problem definitions, solution archives
- **Change tracking:** Evolution of problem formulations
- **UTCS integration:** Evidence packaging and provenance tracking

This QUBO standard ensures that AMPEL360 PLUS discrete optimization problems are formulated, solved, and validated in a systematic, auditable manner, enabling confident use of quantum and classical optimization technologies in safety-critical space tourism applications.
