# Integration Schemas & Examples

This directory contains JSON schemas and example configurations for ASI-T2 MAP ↔ TFA ecosystem integration, as specified in **Integration Whitepaper #2**.

## Directory Structure

```
integration/
├── mal-*.schema.json      # MAL service contract schemas
├── map-*.schema.json      # ASI-T2 MAP platform contract schemas
└── README.md              # This file
```

## MAL Service Contract Schemas

MAL (Main Application Layer) services provide bridge-aligned horizontal services:

* **`mal-qs.schema.json`** — MAL-QS (Primordial State) service contract
* **`mal-fwd.schema.json`** — MAL-FWD (Forward Wave Dynamics) service contract
* **`mal-ue.schema.json`** — MAL-UE (Unit Element) service contract
* **`mal-fe.schema.json`** — MAL-FE (Federation Entanglement) service contract
* **`mal-cb.schema.json`** — MAL-CB (Classical Bit) service contract
* **`mal-qb.schema.json`** — MAL-QB (Bit Cubic) service contract

## ASI-T2 MAP Platform Contract Schemas

MAP (Master Application Platform) contracts define wire-level message formats:

* **`map-control.schema.json`** — Control messages (commands, acks)
* **`map-telemetry.schema.json`** — Telemetry messages (measurements, state updates)
* **`map-health.schema.json`** — Health monitoring messages
* **`map-log.schema.json`** — Audit log messages

## Bridge Semantics (Canonical)

**QS → FWD → UE → FE → CB → QB**

* **QS (Primordial):** Origin/reference state
* **FWD (Prediction/Probability):** Forward wave dynamics
* **UE (Unit Element):** Atomic state decision and collapse
* **FE (Federation Entanglement):** Inter-system coordination
* **CB (Classical Bit):** Deterministic computation
* **QB (Bit Cubic):** Discrete 3D optimization (non-quantum, advisory only)

## Validation

### Schema Validation

Validate MAL service configurations against schemas:

```bash
# Using Python jsonschema
pip install jsonschema
python -c "
import jsonschema
import yaml
import json

# Load schema
with open('WHITEPAPERS/schemas/integration/mal-qs.schema.json') as f:
    schema = json.load(f)

# Load config
with open('WHITEPAPERS/examples/mal-services/mal-qs-example.yaml') as f:
    config = yaml.safe_load(f)

# Validate
jsonschema.validate(config, schema)
print('✅ Valid')
"
```

### Topic Hierarchy Validation

Validate topic naming and hierarchy:

```bash
python scripts/validate_topic_hierarchy.py "map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB"
python scripts/validate_topic_hierarchy.py --batch topics.txt
```

### Bridge Flow Validation

Validate bridge flow semantics:

```bash
python scripts/validate_bridge_flow.py WHITEPAPERS/examples/mal-services/bridge-flow-example.yaml
```

## Usage Examples

See `WHITEPAPERS/examples/mal-services/` for complete service configuration examples:

* `mal-qs-example.yaml` — QS state management service
* `mal-cb-example.yaml` — CB classical solver service
* `mal-qb-example.yaml` — QB optimization service (advisory)
* `bridge-flow-example.yaml` — Complete bridge flow configuration

## Schema Standards

All schemas follow:

* **JSON Schema Draft 2020-12**
* **Semantic versioning** for schema versions
* **Required fields** clearly marked
* **Enum constraints** for controlled vocabularies
* **Pattern validation** for identifiers and topics
* **Description fields** for documentation

## UTCS Integration

All schemas include UTCS (UiX Threading Context/Content/Cache & Structure/Style/Sheet) v5.0 integration:

* **Signature requirements** (Ed25519)
* **Backend recording** for audit trails
* **Bundle format** specification
* **Evidence fields** (timestamp, hash, signature, context, content)

## Security & Ethics

* **MAP-EEM** (platform) enforces authorization policies
* **MAL-EEM** (layers) enforces peaceful-use restrictions
* **QB advisory role** strictly enforced with safety predicates
* **Signature verification** required on all critical messages

## Compliance

Schemas align with:

* **S1000D/ATA** path grammar
* **DO-178C/DO-330** (where applicable)
* **IEC 62443** security requirements
* **ISO/IEC 27001** information security
* **UTCS v5.0** evidence bundling

## Contributing

When modifying schemas:

1. Update schema version (semantic versioning)
2. Ensure backward compatibility for MINOR changes
3. Update examples to match schema changes
4. Run validation tests
5. Update this README if structure changes

## References

* [Integration Whitepaper #2](../INTEGRATION_WHITEPAPER_2.md)
* [Master Whitepaper #1](../MASTER_WHITEPAPER_1.md)
* [JSON Schema Specification](https://json-schema.org/)
* [UTCS v5.0 Documentation](../../README.md)

---

*Part of ASI-T2 Integration Architecture*  
*Version: 0.1.0*  
*UTCS Anchor: TBD*
