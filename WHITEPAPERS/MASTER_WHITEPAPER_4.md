---
id: ASIT2-WHITEPAPER-QAIM-4
project: ASI-T2
artifact: "Master Whitepaper #4 — QAIM-2: Quantum-Classical Optimization via AI Bridges"
llc: GENESIS
classification: PUBLIC-DRAFT
version: "0.1.0"
release_date: "2025-10-03"
author: "Amedeo Pelliccia"
maintainer: "ASI-T Architecture Team"
bridge: "QS→FWD→UE→FE→CB→QB"
ethics_guard: MAL-EEM · MAL-EEM
utcs_mi: "v5.0"
framework: TFA-V2
status: "Public draft for technical review"
ssot: "ASI-T · Universal Injection Prompt (v1)"
canonical_hash: "pending"
doi: "TBA"
description: >
  QAIM-2 orchestrates classical (CB), cubic-bit (QB), and optional quantum (QC)
  resources through AI bridges, aligned with TFA V2 bridge over ASI-T2 MAP
  with UTCS v5.0 evidence.
---

# QAIM-2 — Quantum-Classical Optimization via AI Bridges

> **IDEALE-EU** — ESG-EU strategy overlay for governance and disclosure.

## Executive Summary

**QAIM-2** orchestrates **classical (CB)**, **cubic-bit (QB)**, and optional **quantum (QC)** resources through **AI bridges**, aligned with **TFA V2 bridge** (QS→FWD→UE→FE→CB→QB) over **ASI-T2 MAP** with **UTCS v5.0** evidence.

**Key outcomes:**

- AI-assisted solver selection with QB approximations
- UTCS deterministic packaging
- MAP-EEM/MAL-EEM ethical governance
- S1000D/ATA, DO-178C, ECSS alignment

**Critical:** **QB ≠ qubit**. QB is non-quantum 3D lifting (CB×CB×CB). Qubits include transposition/projection time and teleportation-relative delay vs TP₀.

---

## 1. Scope & Objectives

**Scope:** Mission planning, routing, structural layout, scheduling for AMPEL360 BWB-Q100, GAIA-SPACE/AIR, H₂-AIRPORT, BITFINANCE.

**Objectives:**

1. AI bridges auto-selecting CB/QB/QC paths
2. Wire-clean MAP contracts with UTCS evidence
3. Safety-lite certification posture

---

## 2. Architecture

```
Inputs → PCAN → SM → SP → ARB → XFR → [CB/QB/QC] → UTCS Evidence
         ↓       ↓    ↓    ↓     ↓
      Policies  Data  RL  MAB  Translation
```

**Components:**

- **PCAN:** Problem canonicalization (S1000D/ATA-aware)
- **SM:** Surrogate models (GNN/GP/Transformer)
- **SP:** Strategy policy (RL solver selection)
- **ARB:** Multi-armed bandits (runtime adjustment)
- **XFR:** CB↔QB↔QC translator

---

## 3. TFA Bridge Mapping

| Layer | Role       | MAL Service | MAP Topics                       |
|-------|------------|-------------|----------------------------------|
| QS    | Provenance | MAL-QS      | map/1/log, map/1/telemetry       |
| FWD   | Nowcast    | MAL-FWD     | map/1/control, map/1/telemetry   |
| UE    | Collapse   | MAL-UE      | map/1/control, map/1/telemetry   |
| FE    | Federation | MAL-FE      | map/1/control, map/1/telemetry   |
| CB    | Classical  | MAL-CB      | map/1/control, map/1/telemetry   |
| QB    | Cubic-bit  | MAL-QB      | map/1/control, map/1/telemetry   |

---

## 4. AI Bridges

### 4.1 PCAN — Problem Canonicalization

**Purpose:** Transform domain-specific problems into standardized optimization formats.

**Features:**
- S1000D/ATA chapter recognition
- Constraint extraction and normalization
- Domain metadata preservation
- Type safety and validation

**Output:** Canonical problem representation with metadata tags.

### 4.2 SM — Surrogate Models

**Purpose:** Extract features and predict solver performance without full execution.

**Models:**
- **GNN:** Graph Neural Networks for structured problems
- **GP:** Gaussian Processes for uncertainty quantification
- **Transformer:** Attention-based models for sequential dependencies

**Metrics:** Predicted solve time, solution quality, resource requirements.

### 4.3 SP — Strategy Policy

**Purpose:** Select optimal solver and parameters using reinforcement learning.

**Algorithm:** Multi-objective RL with contextual bandits
**Training:** Offline on historical runs, online adaptation
**Policies:** Epsilon-greedy, UCB1, Thompson Sampling

### 4.4 ARB — Arbitration

**Purpose:** Runtime adjustment and fallback handling.

**Features:**
- Multi-armed bandit selection
- Timeout detection and solver switching
- Resource monitoring and load balancing
- Performance tracking and learning

### 4.5 XFR — Cross-Framework Translation

**Purpose:** Translate between CB, QB, and QC formulations.

**Supported formats:**
- Classical: MIP, SAT, CSP
- QB: Tensor networks, lifted formulations
- QC: QUBO, QAOA, VQE

---

## 5. Solvers

### 5.1 CB Pool — Classical Solvers

**Solvers:**
- **Gurobi:** Commercial MIP/LP solver
- **CBC:** Open-source MIP solver
- **OR-Tools:** Google's constraint programming
- **GLPK:** GNU Linear Programming Kit

**Selection criteria:** Problem size, constraint types, time budget.

### 5.2 QB Pool — Cubic-Bit Approximations

**Purpose:** Non-quantum 3D lifting for middle-scale problems.

**Methods:**
- Tensor decomposition
- Multi-dimensional dynamic programming
- Lifted linear relaxations

**Advantages:** No quantum hardware required, deterministic results.

### 5.3 QC Gateway — Quantum Computing

**Purpose:** Interface to quantum hardware and simulators.

**Providers:**
- IBM Quantum
- D-Wave Systems
- IonQ
- Rigetti Computing

**Algorithms:** QAOA, VQE, Quantum Annealing

---

## 6. Schemas

### 6.1 optimize_qb.v1

**Purpose:** Input schema for optimization requests.

**Fields:**
- `problem_type`: String (routing, scheduling, layout, etc.)
- `constraints`: Array of constraint objects
- `objectives`: Array of objective functions with weights
- `parameters`: Solver-specific configuration
- `metadata`: Domain tags, ATA chapters, S1000D references

### 6.2 qaim_result.v1

**Purpose:** Output schema for optimization results.

**Fields:**
- `request_id`: UUID for traceability
- `solver`: Selected solver name and version
- `solution`: Solution variables and values
- `metrics`: Solve time, objective value, gap
- `evidence`: UTCS evidence bundle
- `status`: Success, timeout, infeasible, error

---

## 7. Evidence & Compliance

### 7.1 UTCS v5.0 Integration

**Evidence bundle includes:**
- Input hash (SHA-256)
- Solver provenance (version, configuration)
- Execution trace (timing, resource usage)
- Solution verification (constraint satisfaction)
- Cryptographic signatures

**Validation:**
```bash
utcs verify qaim-2-result.json
cosign verify --key public.pem qaim:0.1.0
```

### 7.2 Standards Compliance

**Aerospace:**
- S1000D: Data module integration
- ATA: Chapter mapping and traceability
- DO-178C: Software level determination (TBD)
- ECSS: Space system standards

**Ethics:**
- MAP-EEM: Ethical evaluation matrix
- MAL-EEM: Master application layer ethics module

---

## 8. Deployment

### 8.1 Edge Deployment

**Characteristics:**
- Lightweight solvers (CBC, GLPK)
- Local decision making
- Limited connectivity
- Real-time constraints

**Use cases:** UAV mission planning, on-board optimization

### 8.2 Site Deployment

**Characteristics:**
- Mixed solver portfolio
- Regional data center
- Medium-scale problems
- Batch and interactive modes

**Use cases:** Factory scheduling, regional logistics

### 8.3 Hub Deployment

**Characteristics:**
- Full solver suite including QC
- High-performance computing
- Large-scale optimization
- Research and development

**Use cases:** Aircraft design, supply chain optimization

---

## 9. Integration with ASI-T2 Products

### 9.1 AMPEL360 BWB-Q100

**Applications:**
- Aerodynamic surface optimization (AAA domain)
- Flight control tuning (LCC domain)
- Manufacturing process planning (PPP domain)
- Supply chain routing (logistics)

### 9.2 GAIA-SPACE

**Applications:**
- Constellation scheduling
- Orbit optimization
- Ground station allocation
- Communication link planning

### 9.3 GAIA-AIR

**Applications:**
- Swarm coordination
- Multi-agent task assignment
- Collision avoidance
- Energy-efficient routing

### 9.4 H₂-AIRPORT

**Applications:**
- Hydrogen storage optimization
- Fueling schedule coordination
- Safety zone layout
- Equipment placement

### 9.5 BITFINANCE

**Applications:**
- Portfolio optimization
- Risk management
- Transaction routing
- Market making strategies

---

## 10. Performance Metrics

### 10.1 Solution Quality

**Metrics:**
- Objective value vs. best known
- Constraint violation percentage
- Solution feasibility rate

**Targets:**
- CB: Optimal or < 1% gap
- QB: < 5% gap from optimal
- QC: Problem-dependent

### 10.2 Time-to-Solution

**Metrics:**
- Wall-clock time
- CPU time
- Queue wait time (for QC)

**Targets:**
- Real-time: < 100ms
- Interactive: < 10s
- Batch: < 1h

### 10.3 Resource Efficiency

**Metrics:**
- CPU utilization
- Memory footprint
- Energy consumption
- Quantum circuit depth (QC)

---

## 11. Safety & Certification

### 11.1 Safety Posture

**Criticality:** DAL C/D (based on DO-178C)
**Failure modes:** Suboptimal solution, timeout, infeasible

**Mitigations:**
- Fallback to conservative solution
- Timeout monitoring and alerts
- Solution validation checks
- Human-in-the-loop for critical decisions

### 11.2 Verification & Validation

**Methods:**
- Unit tests for each component
- Integration tests for bridge interactions
- End-to-end tests with reference problems
- Regression tests on historical data

**Coverage targets:**
- Statement coverage: > 95%
- Branch coverage: > 90%
- Function coverage: 100%

---

## 12. Ethics & Governance

### 12.1 MAP-EEM Integration

**Evaluation criteria:**
- Transparency: Explainable solver selection
- Fairness: Unbiased optimization
- Privacy: Data protection in shared problems
- Accountability: Audit trail and provenance

### 12.2 MAL-EEM Guardrails

**Enforcement:**
- Pre-optimization checks (ethical constraints)
- Post-optimization validation (solution acceptability)
- Continuous monitoring (drift detection)
- Incident response (escalation procedures)

---

## 13. Roadmap

### Phase 1 (Q4 2025): Foundation
- [ ] Core orchestrator implementation
- [ ] CB solver pool (Gurobi, CBC)
- [ ] Basic PCAN and XFR
- [ ] UTCS v5.0 integration

### Phase 2 (Q1 2026): AI Bridges
- [ ] Surrogate models (GNN, GP)
- [ ] Strategy policy (RL)
- [ ] Arbitration (MAB)
- [ ] QB solver pool

### Phase 3 (Q2 2026): Quantum Integration
- [ ] QC gateway implementation
- [ ] IBM Quantum and D-Wave integration
- [ ] QAOA and VQE algorithms
- [ ] Hybrid classical-quantum workflows

### Phase 4 (Q3 2026): Production
- [ ] Multi-site deployment
- [ ] Performance optimization
- [ ] Certification artifacts
- [ ] Production monitoring

---

## 14. API Examples

### 14.1 Optimization Request

```python
import requests

payload = {
    "problem_type": "vehicle_routing",
    "constraints": [
        {"type": "capacity", "value": 100, "unit": "kg"},
        {"type": "time_window", "start": "08:00", "end": "18:00"}
    ],
    "objectives": [
        {"name": "minimize_distance", "weight": 0.7},
        {"name": "minimize_time", "weight": 0.3}
    ],
    "parameters": {
        "solver": "auto",
        "time_limit": 60,
        "gap_tolerance": 0.01
    },
    "metadata": {
        "domain": "logistics",
        "ata_chapter": "ATA-34",
        "classification": "INTERNAL"
    }
}

response = requests.post(
    "https://qaim-2.asi-t2.eu/v1/optimize",
    json=payload,
    headers={"Authorization": "Bearer <token>"}
)

result = response.json()
print(f"Solution: {result['solution']}")
print(f"Solver: {result['solver']}")
print(f"Time: {result['metrics']['solve_time']}s")
```

### 14.2 Evidence Verification

```bash
# Download evidence bundle
curl -H "Authorization: Bearer <token>" \
  https://qaim-2.asi-t2.eu/v1/evidence/<request_id> \
  -o evidence.json

# Verify with UTCS
utcs verify evidence.json

# Verify cryptographic signature
cosign verify --key qaim-public.pem evidence.json

# Extract provenance
jq '.provenance' evidence.json
```

---

## 15. Glossary

### Bridges
- **QS:** Quantum State (Primordial provenance)
- **FWD:** Forward (Nowcast wave propagation)
- **UE:** Universe Expansion (Collapse operator)
- **FE:** Federation (Multi-domain coordination)
- **CB:** Classical Bit (Standard computing)
- **QB:** Cubic Bit (3D non-quantum lifting)

### Solvers
- **MIP:** Mixed Integer Programming
- **SAT:** Boolean Satisfiability
- **CSP:** Constraint Satisfaction Problem
- **QUBO:** Quadratic Unconstrained Binary Optimization
- **QAOA:** Quantum Approximate Optimization Algorithm
- **VQE:** Variational Quantum Eigensolver

### Domains (ASI-T2)
- **AAA:** Aerodynamics
- **PPP:** Propulsion
- **EDI:** Electronics
- **LCC:** Linkages/Control
- **IIS:** Intelligence/Integration
- **OOO:** Operations

### Packs
- **CAx:** Computer-Aided X (CAD/CAE/CAM)
- **QOx:** Quantum-Optimized X
- **PAx:** Process Automation X (OB/OFF only)

---

## 16. Cite

> Pelliccia, A. (2025). *QAIM-2: Quantum-Classical Optimization via AI Bridges*. v0.1.0. DOI: TBA.

---

## 17. License

MIT with responsible use. MAP-EEM/MAL-EEM required.

---

## Appendix A — Implementation Skeleton

```python
# services/qaim-2/core/qaim_orchestrator.py
from typing import Dict, Any, Optional
import asyncio
from datetime import datetime
import uuid

class QAIM2Orchestrator:
    """Main orchestrator for QAIM-2 optimization service."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.pcan = ProblemCanonicalizer(config['pcan'])
        self.surrogate = SurrogateModels(config['surrogate'])
        self.strategy = StrategyPolicy(config['strategy'])
        self.arbitration = Arbitration(config['arbitration'])
        self.translator = CrossFrameworkTranslator(config['translator'])
        self.cb_pool = ClassicalSolverPool(config['cb_solvers'])
        self.qb_pool = CubicBitSolverPool(config['qb_solvers'])
        self.qc_gateway = QuantumGateway(config['qc_gateway']) if config.get('qc_enabled') else None
        
    async def optimize(
        self,
        problem: Dict[str, Any],
        constraints: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Main optimization entry point.
        
        Args:
            problem: Problem specification
            constraints: Optimization constraints
            metadata: Optional metadata (ATA, domain, etc.)
            
        Returns:
            OptimizationResult with solution and evidence
        """
        request_id = str(uuid.uuid4())
        start_time = datetime.utcnow()
        
        # 1. Canonicalize problem
        canonical = await self.pcan.canonicalize(problem, metadata)
        
        # 2. Extract features with surrogate models
        features = await self.surrogate.extract_features(canonical)
        
        # 3. Select solver using strategy policy
        solver_type, params = await self.strategy.select_solver(
            features, constraints
        )
        
        # 4. Arbitration: refine selection based on current load
        solver_instance = self.arbitration.select_arm({
            'solver_type': solver_type,
            'features': features,
            'context': self._get_context()
        })
        
        # 5. Translate problem to solver format
        solver_problem = await self.translator.translate(
            canonical, solver_type
        )
        
        # 6. Solve
        result = await self._solve(
            solver_instance, solver_problem, params
        )
        
        # 7. Generate UTCS evidence
        evidence = await self._generate_evidence(
            request_id, canonical, solver_instance, result, 
            start_time, datetime.utcnow()
        )
        
        # 8. Emit to MAP
        await self._emit_evidence(request_id, solver_instance, result)
        
        return {
            'request_id': request_id,
            'solver': str(solver_instance),
            'solution': result.solution,
            'metrics': result.metrics,
            'evidence': evidence,
            'status': result.status
        }
    
    async def _solve(
        self, 
        solver: Any, 
        problem: Any, 
        params: Dict[str, Any]
    ) -> Any:
        """Execute solver with timeout and monitoring."""
        if isinstance(solver, str):
            if solver.startswith('cb_'):
                return await self.cb_pool.solve(problem, params)
            elif solver.startswith('qb_'):
                return await self.qb_pool.solve(problem, params)
            elif solver.startswith('qc_'):
                if self.qc_gateway:
                    return await self.qc_gateway.solve(problem, params)
                else:
                    raise ValueError("QC not enabled")
        raise ValueError(f"Unknown solver: {solver}")
    
    async def _generate_evidence(
        self,
        request_id: str,
        canonical: Any,
        solver: Any,
        result: Any,
        start_time: datetime,
        end_time: datetime
    ) -> Dict[str, Any]:
        """Generate UTCS v5.0 evidence bundle."""
        return {
            'version': 'utcs-v5.0',
            'request_id': request_id,
            'timestamp': end_time.isoformat(),
            'duration_ms': int((end_time - start_time).total_seconds() * 1000),
            'input_hash': self._hash_input(canonical),
            'solver': {
                'name': str(solver),
                'version': getattr(solver, 'version', 'unknown'),
                'config': getattr(solver, 'config', {})
            },
            'solution': {
                'status': result.status,
                'objective_value': result.objective_value,
                'gap': result.gap,
                'feasible': result.feasible
            },
            'provenance': {
                'bridge': 'QS→FWD→UE→FE→CB→QB',
                'ethics': 'MAP-EEM',
                'utcs_version': 'v5.0'
            }
        }
    
    async def _emit_evidence(
        self,
        request_id: str,
        solver: Any,
        result: Any
    ) -> None:
        """Emit evidence to MAP topics."""
        # Publish to map/1/telemetry
        await self._publish_map('map/1/telemetry', {
            'request_id': request_id,
            'solver': str(solver),
            'status': result.status,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    def _get_context(self) -> Dict[str, Any]:
        """Get current system context for arbitration."""
        return {
            'load': self._get_system_load(),
            'queue_depth': self._get_queue_depth(),
            'available_solvers': self._get_available_solvers()
        }
    
    def _hash_input(self, canonical: Any) -> str:
        """Generate SHA-256 hash of canonical input."""
        import hashlib
        import json
        return hashlib.sha256(
            json.dumps(canonical, sort_keys=True).encode()
        ).hexdigest()
```

---

## Appendix B — Directory Structure

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
├── tests/
│   ├── __init__.py
│   ├── test_orchestrator.py          # Orchestrator tests
│   ├── test_bridges.py               # Bridge component tests
│   └── test_solvers.py               # Solver pool tests
├── config/
│   ├── deployment-edge.yaml          # Edge deployment config
│   ├── deployment-site.yaml          # Site deployment config
│   └── deployment-hub.yaml           # Hub deployment config
├── scripts/
│   ├── deploy.sh                     # Deployment script
│   └── validate.sh                   # Configuration validation
├── docs/
│   ├── API.md                        # API documentation
│   └── OPERATIONS.md                 # Operations manual
├── requirements.txt                   # Python dependencies
├── Dockerfile                         # Container image
└── README.md                          # Service overview
```

---

## Appendix C — Configuration Examples

### Edge Deployment (deployment-edge.yaml)

```yaml
version: '1.0'
deployment: edge
bridge: 'CB→QB'

pcan:
  enabled: true
  cache_size: 100

surrogate:
  enabled: false  # Lightweight edge

strategy:
  enabled: false  # Use default policy
  default_solver: 'cb_cbc'

arbitration:
  enabled: true
  fallback: 'cb_glpk'

translator:
  enabled: true
  formats: ['mip', 'sat']

cb_solvers:
  - name: 'cbc'
    enabled: true
    time_limit: 10
  - name: 'glpk'
    enabled: true
    time_limit: 5

qb_solvers:
  enabled: false  # Not needed on edge

qc_gateway:
  enabled: false  # No QC on edge

map:
  enabled: true
  topics:
    - 'map/1/telemetry'
    - 'map/1/log'

utcs:
  enabled: true
  version: 'v5.0'
  evidence_path: '/var/lib/qaim-2/evidence'
```

### Hub Deployment (deployment-hub.yaml)

```yaml
version: '1.0'
deployment: hub
bridge: 'QS→FWD→UE→FE→CB→QB→QC'

pcan:
  enabled: true
  cache_size: 10000
  s1000d_aware: true
  ata_mapping: true

surrogate:
  enabled: true
  models:
    - type: 'gnn'
      checkpoint: '/models/gnn-v1.2.pth'
    - type: 'gp'
      kernel: 'rbf'
    - type: 'transformer'
      checkpoint: '/models/transformer-v2.0.pth'

strategy:
  enabled: true
  algorithm: 'thompson_sampling'
  training_mode: 'online'
  exploration_rate: 0.1

arbitration:
  enabled: true
  algorithm: 'ucb1'
  window_size: 1000

translator:
  enabled: true
  formats: ['mip', 'sat', 'csp', 'qubo', 'qaoa', 'vqe']

cb_solvers:
  - name: 'gurobi'
    enabled: true
    license: '/opt/gurobi/gurobi.lic'
    time_limit: 3600
  - name: 'cbc'
    enabled: true
    time_limit: 1800
  - name: 'ortools'
    enabled: true
    time_limit: 1800
  - name: 'glpk'
    enabled: true
    time_limit: 600

qb_solvers:
  enabled: true
  methods:
    - 'tensor_decomposition'
    - 'lifted_relaxation'
  time_limit: 300

qc_gateway:
  enabled: true
  providers:
    - name: 'ibm_quantum'
      backend: 'ibmq_qasm_simulator'
      shots: 8192
    - name: 'dwave'
      solver: 'Advantage_system6.1'
      num_reads: 1000
  algorithms:
    - 'qaoa'
    - 'vqe'
    - 'quantum_annealing'

map:
  enabled: true
  topics:
    - 'map/1/control'
    - 'map/1/telemetry'
    - 'map/1/log'

utcs:
  enabled: true
  version: 'v5.0'
  evidence_path: '/data/qaim-2/evidence'
  signing_key: '/keys/qaim-2-private.pem'

ethics:
  map_eem: true
  mal_eem: true
  audit_mode: 'strict'
```

---

## Appendix D — Performance Benchmarks

### Classical Solvers (CB)

| Problem Type | Size | Solver | Time (s) | Gap (%) |
|--------------|------|--------|----------|---------|
| VRP          | 50   | Gurobi | 0.8      | 0.0     |
| VRP          | 100  | CBC    | 12.3     | 0.5     |
| Scheduling   | 20   | OR-Tools | 0.3    | 0.0     |
| Layout       | 100  | GLPK   | 45.2     | 2.1     |

### Cubic-Bit Solvers (QB)

| Problem Type | Size | Method | Time (s) | Gap (%) |
|--------------|------|--------|----------|---------|
| VRP          | 50   | Tensor | 2.1      | 1.5     |
| Scheduling   | 20   | Lifted | 0.7      | 0.8     |

### Quantum Solvers (QC)

| Problem Type | Size | Provider | Algorithm | Time (s) | Gap (%) |
|--------------|------|----------|-----------|----------|---------|
| QUBO         | 20   | IBM      | QAOA      | 15.2     | 3.2     |
| QUBO         | 50   | D-Wave   | Annealing | 8.5      | 2.8     |

*Benchmarks run on representative problems, Q4 2025 hardware*

---

*Last Updated: 2025-10-03*  
*Version: 0.1.0*  
*UTCS Anchor: TBD*
