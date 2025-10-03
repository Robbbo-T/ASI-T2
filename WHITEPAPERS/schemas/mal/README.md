---
id: MAL-SCHEMAS-README
project: ASI-T2
artifact: MAL Contract Schemas
version: 1.0.0
release_date: "2025-10-03"
maintainer: "ASI-T Architecture Team"
bridge: "QS→FWD→UE→FE→CB→QB"
ethics_guard: MAL-EEM
utcs_mi: v5.0
---

# MAL Contract Schemas

This directory contains JSON Schema definitions for MAL (Master Application Layer) contracts. These schemas define the wire-level message formats for all MAL communication.

## Schema Files

### Core Contracts

- **`mal.control.v1.json`** - Control command contract
  - Purpose: Deterministic command execution with idempotency
  - Required fields: `cmd`, `target`, `idempKey`
  - Features: TTL, priority, metadata support

- **`mal.telemetry.v1.json`** - Telemetry data contract
  - Purpose: Time-series data points with tagging
  - Required fields: `points` (array of k-v pairs)
  - Features: Aggregation metadata, unit specification, flexible value types

- **`mal.health.v1.json`** - Health check contract
  - Purpose: Liveness and readiness monitoring
  - Required fields: `alive`, `ready`
  - Features: Dependency tracking, health metrics, version reporting

- **`mal.log.v1.json`** - Structured logging contract
  - Purpose: Structured log entries with flight-recorder support
  - Required fields: `level`, `message`
  - Features: Error details, distributed tracing, hash-chain segments

## Schema Compliance

All schemas follow:
- **JSON Schema Draft 2020-12** specification
- **Strict validation**: `additionalProperties: false` where appropriate
- **Required fields**: Minimal but sufficient for contract semantics
- **Extensibility**: Optional fields for advanced use cases

## Usage

### Validation Example (Python)

```python
import json
from jsonschema import Draft202012Validator

# Load schema
with open('mal.control.v1.json') as f:
    schema = json.load(f)

# Load message
message = {
    "cmd": "set_mode",
    "target": "BWB-Q100.flight_ctl",
    "args": {"mode": "AUTO"},
    "idempKey": "f1cf-a1b2-c3d4-b702",
    "ttlMs": 3000
}

# Validate
validator = Draft202012Validator(schema)
validator.validate(message)  # Raises exception if invalid
```

### Validation Example (JavaScript)

```javascript
const Ajv = require('ajv');
const ajv = new Ajv();

// Load schema
const schema = require('./mal.control.v1.json');
const validate = ajv.compile(schema);

// Validate message
const message = {
  cmd: "set_mode",
  target: "BWB-Q100.flight_ctl",
  args: { mode: "AUTO" },
  idempKey: "f1cf-a1b2-c3d4-b702",
  ttlMs: 3000
};

const valid = validate(message);
if (!valid) {
  console.error(validate.errors);
}
```

## Schema Evolution

### Versioning

Schemas follow semantic versioning aligned with MAL protocol:
- **Major version** (v1, v2): Breaking changes, requires migrators
- **Minor version** (v1.1, v1.2): Backward-compatible additions
- **Patch version**: Documentation or non-semantic updates

### Compatibility Rules

1. **Adding optional fields**: Minor version bump
2. **Adding enum values**: Minor version bump
3. **Changing field types**: Major version bump
4. **Removing fields**: Major version bump
5. **Making optional→required**: Major version bump

### Migration Process

When introducing breaking changes:
1. Create new schema file: `mal.control.v2.json`
2. Implement migrator: `migrate_control_v1_to_v2()`
3. Document in `MIGRATION_GUIDE.md`
4. Support both versions during transition period
5. Deprecate old version with sunset timeline

## Testing

### Schema Validation Tests

Run schema validation tests:
```bash
cd ../../mal/sheet
make validate-schemas
```

### Contract Tests

Example contracts are available in `../../mal/examples/`:
- `control_example.json`
- `telemetry_example.json`
- `health_example.json`
- `log_example.json`

## Integration

### Message Envelope

All contracts are wrapped in a standard MAL envelope:

```json
{
  "hdr": {
    "mid": "9d1b...f1",
    "ts": "2025-10-03T09:12:11.456Z",
    "seq": 102934,
    "src": "BWB-Q100.AAA.ATA-57",
    "contract": "MAL.v1.control",
    "schema-id": "asi-t2.org/mal/control/v1",
    "schema-rev": 1,
    "mal-version": "1.0.0",
    "compat-minor": 0,
    "sig": "base64(ed25519(...))",
    "key-id": "ed25519:QS:core:0001"
  },
  "body": { /* contract-specific payload */ }
}
```

### Schema Resolution

Clients resolve schemas using:
1. **`schema-id`**: Canonical schema identifier
2. **`schema-rev`**: Schema revision number
3. **Local cache**: Cached schema files
4. **Remote registry**: Schema registry service (optional)

## Documentation

- **Master Whitepaper #2**: Complete MAL specification
- **Topic Grammar**: `../docs/topic_grammar.md`
- **Security Model**: `../docs/security_model.md`
- **UTCS Manifest**: `../utcs/manifest.yaml`

## Contributing

When adding or modifying schemas:
1. Follow JSON Schema 2020-12 specification
2. Add validation tests
3. Update UTCS manifest
4. Document in whitepaper appendix
5. Create example messages
6. Update this README

## Standards Compliance

- **JSON Schema**: Draft 2020-12
- **RFC 8259**: JSON specification
- **ISO 8601**: Date/time formats
- **RFC 4122**: UUID formats (UUIDv7 for message IDs)
- **UTCS v5.0**: Evidence and bundling

## License

These schemas are part of the ASI-T2 MAL specification and follow the same licensing terms. See repository LICENSE file for details.

## References

- [JSON Schema Specification](https://json-schema.org/)
- [Master Whitepaper #1](../../MASTER_WHITEPAPER_1.md)
- [Master Whitepaper #2](../../MASTER_WHITEPAPER_2_MAL.md)
- [TFA-V2 Framework Documentation](https://asi-t2.org/docs/tfa-v2)
