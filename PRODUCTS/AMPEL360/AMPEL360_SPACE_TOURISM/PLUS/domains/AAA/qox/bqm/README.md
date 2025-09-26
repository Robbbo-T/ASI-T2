---
id: ASIT-PLUS-AAA-QOX-BQM-OV-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/qox/bqm/README.md
llc: SYSTEMS
title: "QOx/BQM — Binary Quadratic Models (AMPEL360 PLUS)"
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

# QOx/BQM — Binary Quadratic Models

Binary Quadratic Models (BQM) are the canonical form used to encode **discrete design and scheduling decisions** as an energy minimization problem. This artifact standardizes **how** AMPEL360 PLUS builds, calibrates, verifies, and accepts BQM optimizations that feed **CAD/CAE/CFD/VP** downstream analyses.

---

## 1) Scope & Applicability

**Applies to** discrete optimization where variables are *binary* (`{0,1}`) or *spin* (`{-1,+1}`) and objectives/constraints are (at most) quadratic.

**Typical PLUS use-cases**
- **TPS panel layout**: minimize seams/thermal risk while respecting maintenance access windows.  
- **Structural topology choices**: select stiffener/bay options under weight & margin constraints.  
- **Actuation mode sequencing** (gear doors, control surfaces): minimize energy/peaks, enforce safety interlocks.  
- **Sensor/antenna placement**: maximize coverage/observability with wiring/EMI constraints.  
- **Test campaign design (DoE)**: select runs to maximize information/minimize cost.

**Out-of-scope:** Continuous optimization (use CAE/CFD for physics), control-law synthesis (see LCC), certification basis.

---

## 2) Mathematical Form & Conventions

A BQM minimizes the **Ising energy**:
```
E(s) = Σᵢ hᵢsᵢ + Σᵢ<ⱼ Jᵢⱼsᵢsⱼ + offset
```
where `s ∈ {-1, +1}ⁿ` (spin variables), `h` = linear biases, `J` = quadratic couplings.

**Binary encoding:** `x ∈ {0,1}ⁿ` with `s = 2x - 1` transforms to QUBO form.

**Standard constraints:**
- **Hard constraints** (feasibility): penalty multiplier `λ ≥ 50× max|objective|`
- **Soft constraints** (preferences): penalty multiplier `λ ≤ 10× max|objective|`

---

## 3) Workflow & Quality Gates

### Input Preparation
1. **Problem Definition**: Engineering requirements → discrete variables + objectives/constraints
2. **BQM Construction**: Build `h`, `J` matrices; apply penalty methods for constraints
3. **Scaling & Normalization**: Ensure numerical stability (`|h|, |J| ∈ [10⁻³, 10³]`)
4. **Validation**: Verify constraint satisfaction, objective scaling, variable bounds

### Solution & Verification
1. **Backend Selection**: Quantum annealer / Digital annealer / Classical solver based on problem size
2. **Parameter Tuning**: Annealing schedule, chain strength, sampling parameters
3. **Solution Extraction**: Best samples, energy distribution, constraint violations
4. **Engineering Validation**: Back-map to physical design; verify feasibility in CAD/CAE

### Quality Assurance
- **Convergence Metrics**: Energy gap, sample diversity, constraint satisfaction rate
- **Reproducibility**: Seed control, configuration versioning, result hashing
- **Performance Tracking**: Solution quality vs. classical benchmarks, timing analysis

---

## 4) Integration Points

**Upstream Inputs**
- **CAD**: Geometry discretization, spatial constraints, adjacency matrices
- **CAE**: Load envelopes, stress/thermal limits, sizing constraints  
- **CFD**: Pressure distributions, heating maps for TPS optimization
- **Requirements**: Mission constraints, safety margins, operational limits

**Downstream Outputs**
- **Design Selections**: Binary choices for detailed CAD modeling
- **Configuration Tables**: Optimized parameters for CAE analysis
- **Test Matrices**: DoE selections for VP validation campaigns
- **Reports**: Optimization rationale, trade-study results, sensitivity analysis

---

## 5) Tools & Infrastructure

**BQM Construction**
- **Python Libraries**: D-Wave Ocean SDK, NetworkX for graph problems
- **Modeling Framework**: Constraint programming interfaces, penalty formulations
- **Validation Tools**: Constraint checking, objective verification

**Solution Backends**
- **Quantum Annealers**: D-Wave Advantage, Leap cloud access
- **Digital Annealers**: Fujitsu DA, Hitachi CMOS annealing
- **Classical Solvers**: Gurobi, CPLEX for benchmarking and small problems

**Configuration Management**
- **Version Control**: Problem definitions, parameter sets, solution archives
- **UTCS Integration**: Evidence packaging, provenance tracking, QS sealing
- **Performance Database**: Solution quality metrics, timing benchmarks

---

## 6) Standards & Compliance

**Mathematical Standards**
- **Variable Naming**: Standardized conventions for different problem types
- **Penalty Formulation**: Systematic approach to constraint handling
- **Solution Validation**: Required checks before acceptance

**Documentation Requirements**
- **Problem Specification**: Clear mapping from engineering to mathematical form
- **Solution Report**: Energy landscapes, constraint analysis, engineering interpretation
- **Verification Evidence**: Back-check results, performance comparisons

**Quality Standards**
- **Solution Acceptance**: Minimum energy gap, constraint satisfaction thresholds
- **Performance Benchmarks**: Required comparison with classical methods
- **Reproducibility**: Seed management, configuration archival

---

## 7) Cross-Domain Interfaces

**CAx Integration**
- **CAD**: Discrete design choices → geometry updates → downstream analysis
- **CAE**: Topology optimization → structural analysis → performance validation
- **CFD**: Configuration optimization → flow analysis → aerodynamic assessment
- **VP**: System optimization → integrated simulation → mission performance

**QOx Coordination**
- **QUBO**: Standard problem formulation for multi-backend solving
- **Annealing**: Primary solution method for large-scale discrete problems
- **QAOA**: Gate-model alternative for specific problem structures

**Documentation Flow**
- **Requirements Traceability**: Engineering needs → optimization objectives
- **Solution Justification**: Mathematical results → engineering decisions
- **Verification Evidence**: Performance validation → design acceptance

This BQM framework provides AMPEL360 PLUS with systematic, auditable discrete optimization capabilities essential for advanced space tourism vehicle development.
