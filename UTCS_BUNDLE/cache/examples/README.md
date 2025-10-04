# Cache Examples

This directory contains example data, test vectors, and demonstration scenarios for the UTCS v5.0 bundle.

## Purpose

The **Cache** section of the UiX Threading model stores:
- Example configurations and use cases
- Test vectors for validation
- Demonstration scenarios (FCR-1, FCR-2 gates)
- Synthetic data for reproducibility
- Recorded telemetry samples

## Contents

### FCR-1 Demonstration

**File:** `fcr1-demo.json`

Minimal UTCS v5.0 bundle example demonstrating First Capability Review (FCR-1) gate requirements:

- Complete bundle structure showcase
- All six UiX sections present (context, content, cache, structure, style, sheet)
- Evidence references (manifest, SBOM, schemas, crosswalks)
- Validation results showing all checks passing
- Ethics guards enabled (MAL-EEM, MAP-EEM)

**Usage:**

```bash
# View example structure
cat cache/examples/fcr1-demo.json | jq '.'

# Validate example references
python sheet/ci/validate_utcs.py --manifest manifest.utcs.yaml
```

## Adding New Examples

When adding new examples:

1. **Name Convention:** Use descriptive kebab-case names (e.g., `fcr2-integration.json`, `h1-encryption-demo.json`)
2. **Structure:** Follow the pattern in `fcr1-demo.json`:
   - `example_id`: Unique identifier
   - `description`: Brief description of the scenario
   - `scenario`: Gate or use case name
   - `program`: Program identifier (BWB-Q100, GAIA-SAT, etc.)
   - `domain`: Three-letter domain code
   - `layer`: TFA bridge layer
   - `evidence`: References to bundle artifacts
   - `validation_results`: Expected outcomes
   - `notes`: Additional context

3. **Validation:** Ensure examples can be validated:
   ```bash
   jq '.' cache/examples/your-example.json > /dev/null
   ```

4. **Documentation:** Add entry to this README describing the example

## UiX Threading Model

The **Cache** is part of the **Threading** (input) layer in UTCS v5.0:

```
Threading (Input):
  - Context  — narrative documents
  - Content  — schemas, code
  - Cache    — examples, test data  ← YOU ARE HERE

Binding (Output):
  - Structure — grammar, mappings
  - Style     — formatting, legal
  - Sheet     — build, CI
```

## References

- [Master Whitepaper #3](../context/MASTER_WHITEPAPER_3_UTCS.md) — §1 Conceptual Model
- [Bundle README](../README.md) — Quick start guide
- [Manifest](../manifest.utcs.yaml) — See `uix.cache` section
