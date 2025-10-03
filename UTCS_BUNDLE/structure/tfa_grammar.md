# TFA Grammar & Path Validation

## Path Grammar (TFA V2)

The TFA bridge is grounded in an **ATA/S1000D-anchored path** enriched with **CAx + QOx + PAx** packages:

```
domains/<DOMAIN_CODE>/ATA-XX/<XX-XX>_<DESCRIPTION>/S1000D/<LAYER>/<PACK>/<SUBPACK>
```

### Components

* `<DOMAIN_CODE>` ∈ {AAA, AAP, AAQ, ..., PPP}
* `ATA-XX` = relevant ATA chapter (e.g., ATA-57 Airframes, ATA-22 Auto Flight)
* `<XX-XX>_<DESCRIPTION>` = ATA work-breakdown subpattern (e.g., `57-10_WING_PRIMARY_STRUCTURE`)
* `S1000D` = DMC metadata + structured content
* `<LAYER>` ∈ {QS, FWD, UE, FE, CB, QB}
* `<PACK>` ∈ {**CAx**, **QOx**, **PAx**}
* `<SUBPACK>` = repo leaf (e.g., `CAD`, `CAE`, `OPT`, `ANNEAL`, `OB`, `OFF`, `TESTS`, `INSPECTION`)

### Pack Definitions (Canonical)

#### CAx — Computer-Aided *X*
Computer-aided design, engineering, manufacturing, testing, and CFD.

Examples:
- `CAD` — Computer-Aided Design
- `CAE` — Computer-Aided Engineering
- `CAM` — Computer-Aided Manufacturing
- `CAT` — Computer-Aided Testing
- `CFD` — Computational Fluid Dynamics

#### QOx — Quantum Optimizations
Variational/annealing/quantum-inspired optimization; scheduling/routing/packing.

Examples:
- `OPT` — General optimization
- `ANNEAL` — Annealing-based optimization
- `QAOA` — Quantum Approximate Optimization Algorithm
- `VQE` — Variational Quantum Eigensolver
- `QUBO` — Quadratic Unconstrained Binary Optimization

#### PAx — Packaging & Assemblies
**Orientation markers ONLY: OB (Onboard), OFF (Outboard)**

Examples:
- `OB` — Onboard packaging and assemblies
- `OFF` — Outboard (off-board) packaging and assemblies

**IMPORTANT:** PAx uses ONLY the orientation markers `OB` and `OFF`. All other subpackages should be classified under CAx or QOx.

### Example Paths

```
# CAx examples
domains/AAA/ATA-57/57-10_WING/S1000D/CB/CAx/CAD/
domains/AAA/ATA-57/57-10_WING/S1000D/FWD/CAx/CFD/

# QOx examples
domains/AAA/ATA-71/71-00_POWERPLANT/S1000D/QB/QOx/ANNEAL/
domains/AAA/ATA-22/22-10_AUTOPILOT/S1000D/CB/QOx/OPT/

# PAx examples (orientation markers only)
domains/AAA/ATA-57/57-10_WING/S1000D/CB/PAx/OB/
domains/AAA/ATA-53/53-00_FUSELAGE/S1000D/CB/PAx/OFF/
```

## TFA Bridge Layers

### QS — Primordial
- **Description:** Canonical anchor and ordering of state
- **Purpose:** Evidence origin, state logging, decision records
- **Typical components:** State machines, decision logs, audit trails

### FWD — Forward Wave Dynamics
- **Description:** Prediction/Probability, nowcast
- **Purpose:** Forward simulation, wave propagation, probabilistic forecasting
- **Typical components:** Predictive models, simulation engines, forecasters

### UE — Unit Element / Collapse
- **Description:** Unit element collapse and measurement
- **Purpose:** State resolution, measurement, discrete event handling
- **Typical components:** Sensors, measurement systems, event handlers

### FE — Federation Entanglement / Contracting
- **Description:** Federation and contracting mechanisms
- **Purpose:** Multi-agent coordination, contract enforcement, federated learning
- **Typical components:** Contract managers, federation protocols, consensus algorithms

### CB — Classical Bit / Companion Binary
- **Description:** Classical computing and binary operations
- **Purpose:** Traditional computation, control systems, classical solvers
- **Typical components:** Flight control, navigation, classical optimization

### QB — Bit Cubic (non-quantum)
- **Description:** Cubic bit representation (non-quantumised)
- **Purpose:** Advisory systems, decision support, risk assessment
- **Typical components:** Advisory engines, recommender systems, risk analyzers

## Validation Rules

### CI Gate Enforcement

Non-conforming paths **FAIL** FCR-1/FCR-2 per the SSoT (**ASI-T · Universal Injection Prompt v1**).

### Path Pattern Validation

```regex
^domains/[A-Z]{3}/ATA-\d{2}/\d{2}-\d{2}_[A-Z0-9_]+/S1000D/(QS|FWD|UE|FE|CB|QB)/(CAx|QOx|PAx)/(CAD|CAE|CAM|CAT|CFD|OPT|ANNEAL|QAOA|VQE|QUBO|OB|OFF|TESTS|INSPECTION)/.*$
```

### Subpackage Constraints

1. **CAx subpackages:** {CAD, CAE, CAM, CAT, CFD, TESTS, INSPECTION}
2. **QOx subpackages:** {OPT, ANNEAL, QAOA, VQE, QUBO, TESTS}
3. **PAx subpackages:** {OB, OFF} **ONLY**

### ATA Chapter Alignment

Ensure ATA chapter codes align with domain content:
- **ATA-22:** Auto Flight
- **ATA-53:** Fuselage
- **ATA-57:** Wings
- **ATA-71:** Power Plant
- **ATA-73:** Engine Fuel and Control
- **ATA-78:** Engine Exhaust

## Integration with UTCS

All TFA paths **MUST** be registered in UTCS bundles via:
1. **structure/tfa_grammar.md** (this file)
2. **structure/topic_hierarchy.md** (topic ↔ path ↔ DMC crosswalk)

Path validation is enforced by:
- `utcs validate` — manifest schema, hashes, crosswalk completeness
- `tfa path.check` — ATA/S1000D grammar and OB/OFF usage
