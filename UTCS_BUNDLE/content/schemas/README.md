# Content Schemas

This directory contains JSON Schema definitions for the UTCS v5.0 bundle and ASI-T2 MAP contracts.

## Purpose

The **Content** section of the UiX Threading model stores:
- JSON Schema definitions
- Code and specifications
- Contract definitions
- API specifications

## Schemas

### 1. UTCS Manifest Schema v5.0

**File:** `utcs.manifest.v5.json`

**JSON Schema Draft:** 2020-12

Canonical schema for UTCS v5.0 bundle manifests. Validates:

- Bundle metadata (ID, program, version, bridge)
- UiX sections (context, content, cache, structure, style, sheet)
- Attestations (SBOM, signatures, DOI)
- File hashes (SHA-256)
- Ethics guards (MAL-EEM, MAP-EEM)
- Bridge services mapping
- Compatibility information

**Schema ID:** `https://asi-t2.org/schemas/utcs.manifest.v5.json`

**Usage:**

```bash
# Validate manifest against schema
python sheet/ci/validate_utcs.py --manifest manifest.utcs.yaml
```

### 2. MAP Control Contract v1

**File:** `map.control.v1.json`

**JSON Schema Draft:** 2020-12

Schema for ASI-T2 MAP.v1.control contracts. Defines:

- Command types (set_mode, update_param, trigger_action, etc.)
- Idempotency keys for deterministic execution
- Rate limiting configuration
- Acknowledgment requirements
- Evidence hooks for UTCS integration

**Schema ID:** `https://asi-t2.org/schemas/map.control.v1.json`

**Example Usage:**

```json
{
  "contract": "MAP.v1.control",
  "version": "1.0.0",
  "program": "BWB-Q100",
  "domain": "AAA",
  "command": {
    "type": "set_mode",
    "target": "flight_control",
    "params": { "mode": "auto" },
    "idempotency_key": "fc-auto-20251003-001"
  }
}
```

### 3. MAP Telemetry Contract v1

**File:** `map.telemetry.v1.json`

**JSON Schema Draft:** 2020-12

Schema for ASI-T2 MAP.v1.telemetry contracts. Defines:

- Topic path format (map/1/telemetry/...)
- Telemetry payload structure
- Timestamp and sequence numbers
- Optional Ed25519 signatures
- Quality indicators
- Evidence metadata (model ID, solver ID, seed)

**Schema ID:** `https://asi-t2.org/schemas/map.telemetry.v1.json`

**Example Usage:**

```json
{
  "contract": "MAP.v1.telemetry",
  "version": "1.0.0",
  "program": "BWB-Q100",
  "domain": "AAA",
  "telemetry": {
    "topic": "map/1/telemetry/BWB-Q100/AAA/WAVES/FWD/FWD",
    "data": { "pressure": 101325, "temperature": 288.15 },
    "timestamp_utc": "2025-10-03T09:30:00Z",
    "seq": 42
  }
}
```

## Validation

All schemas are validated automatically:

```bash
# Validate schema syntax
jq '.' content/schemas/*.json > /dev/null

# Run comprehensive validation
cd UTCS_BUNDLE/sheet
make check
```

## Schema Development

When adding or modifying schemas:

1. **Follow JSON Schema Draft 2020-12 standard**
2. **Use meaningful $id URIs** (https://asi-t2.org/schemas/...)
3. **Include descriptions** for all fields
4. **Define required fields** explicitly
5. **Use patterns** for validation (regex, enums)
6. **Test with examples** before committing

## UiX Threading Model

The **Content** is part of the **Threading** (input) layer in UTCS v5.0:

```
Threading (Input):
  - Context  — narrative documents
  - Content  — schemas, code      ← YOU ARE HERE
  - Cache    — examples, test data

Binding (Output):
  - Structure — grammar, mappings
  - Style     — formatting, legal
  - Sheet     — build, CI
```

## References

- [Master Whitepaper #3](../context/MASTER_WHITEPAPER_3_UTCS.md) — §2 Bundle Layout & Manifest
- [JSON Schema](https://json-schema.org/draft/2020-12/json-schema-core.html) — Standard specification
- [Manifest](../manifest.utcs.yaml) — See `uix.content` section
