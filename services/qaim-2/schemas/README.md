# QAIM-2 JSON Schemas

This directory contains JSON Schema definitions for validating QAIM-2 optimization requests and results.

## Overview

JSON schemas ensure type safety, validation, and documentation of the QAIM-2 API surface. All requests and responses conform to these schemas for consistency and reliability.

## Schema Files

### 1. Input Schema (`optimize_qb.v1.json`)

**Purpose:** Validate optimization request inputs

**Schema Version:** Draft-07  
**API Version:** v1  
**URL:** `https://asi-t2.eu/schemas/qaim-2/optimize_qb.v1.json`

**Structure:**

```json
{
  "problem_type": "vehicle_routing",
  "variables": [...],
  "constraints": [...],
  "objectives": [...],
  "parameters": {...},
  "metadata": {...}
}
```

**Required Fields:**
- `problem_type` - Type of optimization problem
- `objectives` - At least one objective function

**Optional Fields:**
- `variables` - Decision variables (auto-inferred if omitted)
- `constraints` - Problem constraints
- `parameters` - Solver-specific parameters
- `metadata` - Traceability information

**Supported Problem Types:**
- `vehicle_routing` - VRP variants
- `scheduling` - Job shop, flow shop
- `layout` - Facility layout problems
- `assignment` - Resource assignment
- `portfolio` - Portfolio optimization
- `resource_allocation` - Resource allocation
- `path_planning` - Path planning
- `bin_packing` - Bin packing
- `knapsack` - Knapsack variants
- `tsp` - Traveling Salesman Problem
- `vrp` - Vehicle Routing Problem
- `job_shop` - Job shop scheduling
- `flow_shop` - Flow shop scheduling
- `general_mip` - General MIP
- `general_qubo` - General QUBO

**Variable Types:**
- `binary` - Binary (0 or 1)
- `integer` - Integer values
- `continuous` - Continuous values

**Constraint Types:**
- `capacity` - Capacity constraints
- `time_window` - Time window constraints
- `precedence` - Precedence constraints
- `resource` - Resource constraints
- `linear` - Linear constraints
- `quadratic` - Quadratic constraints
- `logical` - Logical constraints
- `custom` - Custom constraints

### 2. Output Schema (`qaim_result.v1.json`)

**Purpose:** Validate optimization results and UTCS v5.0 evidence

**Schema Version:** Draft-07  
**API Version:** v1  
**URL:** `https://asi-t2.eu/schemas/qaim-2/qaim_result.v1.json`

**Structure:**

```json
{
  "request_id": "uuid",
  "solver": "cb_gurobi",
  "solution": {...},
  "metrics": {...},
  "evidence": {...},
  "status": "optimal"
}
```

**Required Fields:**
- `request_id` - UUID for traceability
- `solver` - Solver used
- `status` - Solution status
- `evidence` - UTCS v5.0 evidence bundle

**Status Values:**
- `optimal` - Optimal solution found
- `feasible` - Feasible solution found
- `infeasible` - Problem is infeasible
- `timeout` - Solver timed out
- `error` - Error occurred
- `unknown` - Unknown status

**Evidence Structure:**
- `version` - Always "utcs-v5.0"
- `request_id` - Matches parent request_id
- `timestamp` - ISO 8601 timestamp
- `duration_ms` - Execution duration
- `input_hash` - SHA-256 of input
- `solver` - Solver provenance
- `solution` - Solution evidence
- `provenance` - TFA V2 bridge info

**Provenance Fields:**
- `bridge` - "QS→FWD→UE→FE→CB→QB"
- `ethics` - "MAP-EEM · MAL-EEM"
- `utcs_version` - "v5.0"
- `framework` - "TFA-V2"

## Usage

### Python Validation

```python
import json
import jsonschema

# Load schemas
with open('schemas/optimize_qb.v1.json') as f:
    input_schema = json.load(f)

with open('schemas/qaim_result.v1.json') as f:
    output_schema = json.load(f)

# Validate input
request = {
    'problem_type': 'vehicle_routing',
    'objectives': [
        {'name': 'minimize_distance', 'sense': 'minimize'}
    ]
}

jsonschema.validate(request, input_schema)

# Validate output
result = {
    'request_id': 'uuid',
    'solver': 'cb_cbc',
    'status': 'optimal',
    'evidence': {
        'version': 'utcs-v5.0',
        'provenance': {
            'bridge': 'QS→FWD→UE→FE→CB→QB',
            'ethics': 'MAP-EEM · MAL-EEM',
            'utcs_version': 'v5.0',
            'framework': 'TFA-V2'
        }
    }
}

jsonschema.validate(result, output_schema)
```

### Command Line Validation

```bash
# Using jsonschema CLI
pip install jsonschema[cli]

# Validate input
jsonschema -i request.json schemas/optimize_qb.v1.json

# Validate output
jsonschema -i result.json schemas/qaim_result.v1.json
```

### API Integration

The QAIM-2 service automatically validates:
- All incoming requests against `optimize_qb.v1.json`
- All outgoing results against `qaim_result.v1.json`

Validation errors return HTTP 400 with detailed error messages.

## Schema Versioning

### Version Format

Schemas follow semantic versioning in filenames:
- `optimize_qb.v1.json` - Version 1.0
- `optimize_qb.v2.json` - Version 2.0 (breaking changes)
- `optimize_qb.v1.1.json` - Version 1.1 (compatible additions)

### Version Compatibility

- **v1.x** - Backward compatible within v1
- **v2.x** - Breaking changes from v1

### Migration Guide

When upgrading schema versions:

1. Review changelog for breaking changes
2. Update client code for new fields
3. Test with new schema
4. Deploy updated clients
5. Migrate service to new schema

## Extending Schemas

### Adding New Problem Types

To add a new problem type:

1. Update `problem_type` enum in `optimize_qb.v1.json`
2. Document problem-specific constraints
3. Add test cases
4. Update API documentation

### Adding New Constraint Types

To add a new constraint type:

1. Update `constraints.type` enum
2. Document constraint format
3. Update XFR translator
4. Add solver support

### Adding New Metadata Fields

Metadata extensions are backward compatible:

```json
{
  "metadata": {
    "domain": "AAA",
    "ata_chapter": "ATA-57",
    "custom_field": "value"  // Extensions allowed
  }
}
```

## Schema Tools

### Validation Tools

- **jsonschema** - Python validator
- **ajv** - JavaScript validator (Node.js)
- **JSON Schema Validator** - Online tool

### Schema Generation

Generate client code from schemas:

```bash
# Python dataclasses
datamodel-codegen --input schemas/ --output models/

# TypeScript interfaces
json-schema-to-typescript schemas/*.json --output types/
```

### Schema Documentation

Generate HTML documentation:

```bash
# Using json-schema-for-humans
generate-schema-doc schemas/ docs/schema-html/
```

## Testing

```bash
# Validate all example files
for f in examples/*.json; do
  jsonschema -i "$f" schemas/optimize_qb.v1.json
done

# Run schema tests
pytest tests/test_schemas.py -v
```

## References

- [JSON Schema Specification](https://json-schema.org/)
- [API.md](../docs/API.md) - API documentation
- [MASTER_WHITEPAPER_4.md](../../WHITEPAPERS/MASTER_WHITEPAPER_4.md) - Schema design rationale

---

*QAIM-2 JSON Schema Definitions*  
*Schema Version: Draft-07*  
*API Version: v1*  
*Last Updated: 2025-10-03*
