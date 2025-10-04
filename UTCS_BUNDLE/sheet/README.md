# Sheet

This directory contains build scripts, CI jobs, and reproducibility recipes for the UTCS v5.0 bundle.

## Purpose

The **Sheet** section of the UiX Threading model stores:
- Build automation (Makefile)
- CI/CD scripts
- Validation tooling
- Reproducibility recipes
- Test execution scripts

## Contents

### Makefile

**File:** `Makefile`

Build automation with the following targets:

```bash
# Show available targets
make help

# Validate manifest and bundle structure
make validate

# Full validation including crosswalk checks
make validate-full

# Run all checks (validation + schema verification)
make check

# Generate SBOM (requires syft or creates placeholder)
make sbom

# Create bundle archive
make bundle

# Clean generated files
make clean
```

**Usage from UTCS_BUNDLE root:**

```bash
cd UTCS_BUNDLE/sheet
make check
```

### CI Directory

**Directory:** `ci/`

Contains continuous integration scripts and validation tooling.

See [ci/README.md](ci/README.md) for details.

## UiX Threading Model

The **Sheet** is part of the **Binding** (output) layer in UTCS v5.0:

```
Threading (Input):
  - Context  — narrative documents
  - Content  — schemas, code
  - Cache    — examples, test data

Binding (Output):
  - Structure — grammar, mappings
  - Style     — formatting, legal
  - Sheet     — build, CI          ← YOU ARE HERE
```

## Build Reproducibility

Per Master Whitepaper #3 §3.2, builds must be:

1. **Deterministic** — Same inputs → same outputs
2. **Reproducible** — Documented dependencies and toolchain
3. **Auditable** — Build logs and evidence captured

### Requirements

- Python 3.8+
- jsonschema, PyYAML
- jq (for schema validation)
- Optional: syft (for SBOM generation), cosign (for signatures)

Install Python dependencies:

```bash
pip install jsonschema PyYAML
```

## Integration

The Sheet integrates with:

- **GitHub Actions** — `.github/workflows/utcs-validate.yml`
- **Manifest** — Referenced in `uix.sheet` section
- **Evidence** — Build artifacts tracked in attestations

## References

- [Master Whitepaper #3](../context/MASTER_WHITEPAPER_3_UTCS.md) — §3 Evidence Plane & Lifecycle
- [Bundle README](../README.md) — Quick start guide
- [Manifest](../manifest.utcs.yaml) — See `uix.sheet` section
- [CI Directory](ci/README.md) — Validation scripts
