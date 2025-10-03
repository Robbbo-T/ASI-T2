# ICD-AAA-ATA-57-10: Wing Primary Structure Data Exchange Interface

**Document ID:** ICD-AAA-ATA-57-10  
**Domain:** AAA (Advanced Aerospace Architecture)  
**Revision:** 0.1.0  
**Date:** 2025-01-01  
**Status:** Baseline

---

## Purpose

This Interface Control Document (ICD) defines the data exchange interfaces for ATA-57-10 Wing Primary Structure between the ATA domain (knowledge repository) and other domains including CAX (Computer-Aided Engineering), QOX (Quantum Optimization), and PAX (Package & Deployment).

---

## Scope

This ICD covers:
- Data schemas for structural definitions
- Input/output manifests for compute workflows
- Traceability and provenance requirements (UTCS/QS)
- Package specifications for deployment

---

## Data Schemas

### JSON Schemas

All data exchange artifacts must conform to JSON Schema 2020-12 standard and the following schema files:

1. **joint.schema.json** — Joint definitions (mechanical, adhesive, hybrid)
2. **laminate.stack.schema.json** — Composite laminate layup specifications
3. **fastener.set.schema.json** — Fastener specifications and installation parameters
4. **attachment.fitting.schema.json** — Attachment fitting definitions
5. **acceptance.metric.schema.json** — Acceptance criteria and inspection metrics

All schemas are located in: `contracts/schemas/`

### Schema Versioning

- Schemas follow Semantic Versioning (semver)
- Version field is required in all schemas: `"version": "^\\d+\\.\\d+\\.\\d+$"`
- Breaking changes require major version increment
- Backward-compatible additions use minor version increment

---

## Data Exchange Patterns

### ATA → CAX (Design Input)

**Purpose:** Provide design requirements and constraints to CAD/FEA tools

**Inputs (from ATA-57-10):**
- Geometry definitions (reference surfaces, envelope)
- Material specifications (codes, properties)
- Load cases and boundary conditions
- Design constraints (clearances, manufacturing)

**Format:** JSON manifests referencing geometry files
**Location:** `io/routing.manifest.yaml` (sources section)

### CAX → ATA (Design Output)

**Purpose:** Capture design artifacts and analysis results

**Outputs (to ATA-57-10):**
- Part definitions (panels, spars, ribs, fittings)
- Assembly definitions (joints, fastener patterns)
- Analysis results (stresses, margins, buckling)
- Manufacturing data (ply books, drill patterns)

**Format:** JSON manifests + STEP/IGES geometry
**Location:** Referenced in `io/routing.manifest.yaml` (inputs section)

### ATA → QOX (Optimization Problems)

**Purpose:** Define optimization problems for quantum/classical solvers

**Inputs (from ATA-57-10):**
- Design variables (fastener locations, ply orientations)
- Objective functions (mass, cost, performance)
- Constraints (stress, buckling, manufacturing)
- Problem formulation (QUBO, BQM, MILP)

**Format:** JSON per qox_problem.schema.json
**Location:** Referenced via `io/routing.manifest.yaml` (qox section)

### QOX → ATA (Optimization Results)

**Purpose:** Return optimized configurations

**Outputs (to ATA-57-10):**
- Optimal design variables
- Solution quality metrics
- Solver performance data
- Trace/provenance (UTCS anchors)

**Format:** JSON results + solver metadata
**Location:** Logged in `evidence/` and referenced in manifest

### ATA → PAX (Package Definition)

**Purpose:** Specify deployment packages for on-board or off-board use

**Inputs (from ATA-57-10):**
- Bill of materials (BOM)
- Configuration baseline (versions, hashes)
- Evidence bundle (test reports, certs)
- Deployment constraints (target platform)

**Format:** JSON per package.schema.json
**Location:** `io/routing.manifest.yaml` (pax section)

### PAX → ATA (Package Artifacts)

**Purpose:** Return signed/sealed deployment packages

**Outputs (to ATA-57-10):**
- SBOM (Software/Structure Bill of Materials)
- Container images (OCI format for OFF)
- Digital signatures (QS/UTCS seals)
- Deployment manifests

**Format:** YAML/JSON + binary artifacts
**Location:** Referenced via `io/routing.manifest.yaml` (outputs section)

---

## Routing Manifest

The file `io/routing.manifest.yaml` is the single source of truth for all data flows. It defines:

- **Sources:** Where data originates (upstream ATA chapters, CAX tools)
- **Inputs:** Data consumed by ATA-57-10 processes
- **Outputs:** Data produced by ATA-57-10 processes
- **Evidence:** Traceability links to test results, approvals
- **UTCS/QS Anchors:** Cryptographic seals and provenance

### Manifest Schema

```yaml
id: <unique identifier>
version: <semver>
sources:
  - name: <source name>
    type: <ATA|CAX|QOX|PAX>
    uri: <path or URL>
    hash: <sha256>
inputs:
  - artifact: <artifact name>
    schema: <schema reference>
    uri: <path or URL>
    hash: <sha256>
outputs:
  - artifact: <artifact name>
    schema: <schema reference>
    uri: <path or URL>
    hash: <sha256>
evidence:
  - type: <test|analysis|approval>
    uri: <path or URL>
    hash: <sha256>
utcs:
  canonical_hash: <hash>
  sbom_uri: <path or URL>
  signer: <identity>
  timestamp: <ISO 8601>
```

---

## Quality & Traceability

### UTCS/QS Requirements

All data exchange artifacts must:
1. Include SHA-256 hash for integrity verification
2. Reference source provenance (who/when/what)
3. Link to evidence bundles (tests, analyses, approvals)
4. Carry UTCS anchor for quantum-safe sealing
5. Include version information (schema, data, tool)

### Validation

- All JSON artifacts must validate against referenced schema
- Validation tools: `jsonschema` (Python), `ajv` (JavaScript)
- Validation script: `scripts/validate_json.py` (if available)

### Approval

Data exchange interfaces require approval by:
- Domain architect (ATA-57-10 owner)
- Compute team lead (CAX/QOX)
- Systems integration lead (PAX)
- Configuration management (version control)

---

## Change Control

### Interface Changes

Changes to this ICD require:
1. Proposed change description
2. Impact assessment (who/what affected)
3. Multi-discipline review
4. Approval by all affected parties
5. Version increment (per semver)

### Schema Evolution

Schema changes follow these rules:
- **Additive changes** (new optional fields): Minor version increment
- **Breaking changes** (removed/renamed fields): Major version increment
- **Documentation only**: Patch version increment

---

## References

- UTCS/QS Framework: `PRODUCTS/INFRANET/AOA/core/evidence.py`
- JSON Schema Standard: https://json-schema.org/draft/2020-12/
- Package Schema: `../pax/schemas/package.schema.json`
- CAD Manifest Schema: `../cax/CAD/schemas/cad_manifest.schema.json` (if exists)
- QOX Problem Schema: `../qox/schemas/qox_problem.schema.json` (if exists)

---

## Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 0.1.0 | 2025-01-01 | Initial baseline | TBD |

---
*This ICD is configuration-controlled and subject to multi-domain approval.*
