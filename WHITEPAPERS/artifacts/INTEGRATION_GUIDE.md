# Using Integration Schemas and Validators

This guide explains how to use the ASI-T2 MAP ↔ TFA ecosystem integration schemas and validators from **Integration Whitepaper #2**.

## Overview

The integration architecture defines:

* **ASI-T2 MAP** (Platform) — Communication infrastructure with contracts
* **TFA MAP** (Programs) — Per-domain services (e.g., MAP-AAA, MAP-PPP)
* **TFA MAL** (Layers) — Per-bridge services (MAL-QS, MAL-FWD, MAL-UE, MAL-FE, MAL-CB, MAL-QB)

## Quick Start

### 1. Validate Topics

Check that your topic naming follows the hierarchy:

```bash
# Single topic validation
python scripts/validate_topic_hierarchy.py "map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB"

# Batch validation from file
echo "map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB" > topics.txt
echo "map/1/telemetry/BWB-Q100/AAA/SYSTEMS/SI/CB" >> topics.txt
echo "map/1/log/BWB-Q100/AAA/STATES/QS/QS" >> topics.txt
python scripts/validate_topic_hierarchy.py --batch topics.txt
```

### 2. Validate Bridge Flow

Check that your bridge flow configuration is correct:

```bash
python scripts/validate_bridge_flow.py WHITEPAPERS/artifacts/examples/mal-services/bridge-flow-example.yaml
```

### 3. Validate Service Configurations

Use JSON Schema validation to check MAL service configs:

```bash
pip install jsonschema pyyaml

python3 << 'EOF'
import jsonschema
import yaml
import json

# Load schema
with open('WHITEPAPERS/artifacts/schemas/integration/mal-qs.schema.json') as f:
    schema = json.load(f)

# Load config
with open('WHITEPAPERS/artifacts/examples/mal-services/mal-qs-example.yaml') as f:
    config = yaml.safe_load(f)

# Validate
try:
    jsonschema.validate(config, schema)
    print('✅ Configuration is valid')
except jsonschema.exceptions.ValidationError as e:
    print(f'❌ Validation error: {e.message}')
EOF
```

## Topic Hierarchy

### Format

```
map/<major>/<contract>/<program>/<domain>/<group>/<llc>/<layer>
```

### Examples

```
# Control topics
map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB
map/1/control/BWB-Q100/AAA/QUBITS/QB/QB
map/1/control/BWB-Q100/FLEET/ELEMENTS/FE/FE

# Telemetry topics
map/1/telemetry/BWB-Q100/AAA/SYSTEMS/SI/CB
map/1/telemetry/BWB-Q100/AAA/STATES/QS/QS

# Health topics (simplified)
map/1/health/BWB-Q100
map/1/health/BWB-Q100/AAA

# Log topics (simplified)
map/1/log/BWB-Q100/AAA/STATES/QS/QS
```

### Valid Values

* **Major version:** `1` (current)
* **Contract:** `control`, `telemetry`, `health`, `log`
* **Domain:** `AAA`, `AAP`, `CCC`, `CQH`, `DDD`, `EDI`, `EEE`, `EER`, `IIF`, `IIS`, `LCC`, `LIB`, `MEC`, `OOO`, `PPP`, `FLEET`
* **Layer:** `QS`, `FWD`, `UE`, `FE`, `CB`, `QB`

## Bridge Flow Semantics

### Layer Order (Canonical)

**QS → FWD → UE → FE → CB → QB**

* **QS (Primordial):** State origin/reference
* **FWD (Forward Wave Dynamics):** Prediction/probability
* **UE (Unit Element):** Atomic execution
* **FE (Federation Entanglement):** Coordination
* **CB (Classical Bit):** Deterministic computation
* **QB (Bit Cubic):** Advisory optimization (non-quantum)

### Valid Transitions

```yaml
QS → FWD, UE
FWD → UE, FE
UE → FE, CB
FE → CB, QB
CB → QB
QB → (terminal, advisory only)
```

### Bridge Flow Configuration

Create a `bridge-flow.yaml` file:

```yaml
layers:
  QS:
    description: Primordial state
    role: state_management
    properties: [immutable, versioned, signed]
  # ... other layers

flows:
  - from: QS
    to: FWD
    description: State feeds predictions
  # ... other flows

utcs:
  require_signature: true
  record_backend: true
  bundle_format: UTCS-v5.0
```

Then validate:

```bash
python scripts/validate_bridge_flow.py bridge-flow.yaml
```

## MAL Service Contracts

### Creating a MAL Service

1. Choose the appropriate layer (QS/FWD/UE/FE/CB/QB)
2. Create a configuration file following the schema
3. Validate against the schema

Example MAL-CB service configuration:

```yaml
service_id: MAL-CB-BWB-Q100-AAA
version: 0.1.0
layer: CB
description: Classical solver service

topics:
  subscribe:
    - map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB
  publish:
    - map/1/telemetry/BWB-Q100/AAA/SYSTEMS/SI/CB

computation:
  deterministic: true
  validation:
    enabled: true
    method: redundant-computation
  solvers:
    - solver_id: IPOPT-3.14.0
      type: nonlinear
      version: 3.14.0

utcs:
  require_signature: true
  record_backend: true
  bundle_format: UTCS-v5.0
```

Validate:

```bash
python3 << 'EOF'
import jsonschema, yaml, json

with open('WHITEPAPERS/artifacts/schemas/integration/mal-cb.schema.json') as f:
    schema = json.load(f)

with open('my-mal-cb-service.yaml') as f:
    config = yaml.safe_load(f)

jsonschema.validate(config, schema)
print('✅ Service configuration is valid')
EOF
```

### MAL Service Schema Reference

| Layer | Schema File | Purpose |
|-------|-------------|---------|
| QS | `mal-qs.schema.json` | Primordial state management |
| FWD | `mal-fwd.schema.json` | Forward wave dynamics/prediction |
| UE | `mal-ue.schema.json` | Atomic execution |
| FE | `mal-fe.schema.json` | Federation coordination |
| CB | `mal-cb.schema.json` | Classical computation |
| QB | `mal-qb.schema.json` | Advisory optimization |

## MAP Platform Contracts

### Message Formats

All MAP messages follow these contracts:

1. **Control** (`map-control.schema.json`) — Commands, acks
2. **Telemetry** (`map-telemetry.schema.json`) — Measurements, state
3. **Health** (`map-health.schema.json`) — Service health
4. **Log** (`map-log.schema.json`) — Audit logs

### Example Control Message

```json
{
  "message_id": "550e8400-e29b-41d4-a716-446655440000",
  "version": "1.0.0",
  "contract": "control",
  "timestamp": "2025-10-03T12:00:00Z",
  "sequence": 42,
  "topic": "map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB",
  "sender": {
    "id": "MAL-FE-001",
    "type": "service"
  },
  "payload": {
    "command": "solve_optimization",
    "parameters": {
      "problem_type": "aerodynamic",
      "tolerance": 1e-6
    },
    "priority": "normal",
    "timeout_ms": 30000
  },
  "security": {
    "signature": {
      "algorithm": "Ed25519",
      "value": "base64-encoded-signature",
      "key_id": "key-001"
    }
  }
}
```

Validate:

```bash
python3 << 'EOF'
import jsonschema, json

with open('WHITEPAPERS/artifacts/schemas/integration/map-control.schema.json') as f:
    schema = json.load(f)

with open('control-message.json') as f:
    message = json.load(f)

jsonschema.validate(message, schema)
print('✅ Control message is valid')
EOF
```

## Security & UTCS

### Signature Requirements

All critical messages MUST be signed:

```python
import ed25519
import json
import base64

# Sign message
signing_key = ed25519.SigningKey(b'...')  # Load your key
message_bytes = json.dumps(message['payload']).encode()
signature = signing_key.sign(message_bytes)

message['security'] = {
    'signature': {
        'algorithm': 'Ed25519',
        'value': base64.b64encode(signature).decode(),
        'key_id': 'key-001'
    }
}
```

### UTCS Evidence Bundles

Every service MUST include UTCS metadata:

```yaml
utcs:
  require_signature: true
  record_backend: true
  bundle_format: UTCS-v5.0
  evidence_fields:
    - timestamp
    - hash
    - signature
    - context
    - content
```

## QB Safety Constraints

QB (Bit Cubic) services are **advisory only** and MUST include safety constraints:

```yaml
optimization:
  role: advisory  # MUST be advisory
  safety:
    max_age_s: 30  # Solutions expire
    fallback: use_cb_solution  # Fallback required
    accept_predicates:  # Safety predicates
      - min_separation_nm >= 5
      - structural_margin >= 1.5
```

QB solutions MUST:
1. Pass all `accept_predicates`
2. Be validated by CB layer before use
3. Have a fallback mechanism
4. Expire after `max_age_s`

## Troubleshooting

### Topic Validation Errors

**Error:** `Invalid domain 'XYZ'`
- Use only valid domain codes: AAA, AAP, CCC, etc.

**Error:** `Invalid layer 'XX'`
- Use only valid layers: QS, FWD, UE, FE, CB, QB

**Error:** `Topic does not match expected pattern`
- Follow format: `map/1/<contract>/<PROGRAM>/<DOMAIN>/<GROUP>/<LLC>/<LAYER>`

### Bridge Flow Errors

**Error:** `Invalid transition X → Y`
- Check VALID_TRANSITIONS in bridge flow semantics

**Error:** `Flow graph contains cycles`
- Bridge flow must be acyclic (no circular dependencies)

**Error:** `QB must be terminal`
- QB cannot have outgoing flows (advisory only)

### Schema Validation Errors

**Error:** `Missing required field`
- Check schema for required fields and add them

**Error:** `Does not match pattern`
- Follow naming conventions (e.g., `MAL-CB-*` for CB services)

## Examples

See `WHITEPAPERS/artifacts/examples/mal-services/` for complete examples:

* `mal-qs-example.yaml` — QS state management
* `mal-cb-example.yaml` — CB classical solver
* `mal-qb-example.yaml` — QB optimization (advisory)
* `bridge-flow-example.yaml` — Complete bridge flow

## References

* [Integration Whitepaper #2](../MASTER_WHITEPAPER_2.md)
* [Master Whitepaper #1](../MASTER_WHITEPAPER_1.md)
* [Schema Directory](./schemas/integration/)
* [JSON Schema Specification](https://json-schema.org/)

## Support

* **Issues:** https://github.com/Robbbo-T/ASI-T2/issues
* **Maintainer:** ASI-T Architecture Team

---

*Part of ASI-T2 Integration Architecture*  
*Version: 0.1.0*  
*Last Updated: 2025-10-03*
