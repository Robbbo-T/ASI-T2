# Validation Schemas

This directory contains validation schemas and rules for certification artifacts.

## Purpose

Provides automated validation for:
- Certification plan structure and content
- Evidence tree organization
- Data consistency and completeness

## Available Schemas

| Schema | Type | Purpose |
|--------|------|---------|
| `cert_plan.schema.json` | JSON Schema | Validates certification plan YAML files |
| `evidence_rules.yaml` | YAML Rules | Defines required evidence directory structure |

## Certification Plan Schema

The `cert_plan.schema.json` file:
- Validates certification plan structure
- Ensures required fields are present
- Checks data types and formats
- Validates Design Assurance Levels (DAL A-E)
- Verifies authority names (FAA, EASA, etc.)
- Validates date formats and version numbers

### Usage

```bash
# Validate certification plan against schema
python3 -m jsonschema -i plans/certification_plan.yaml schemas/cert_plan.schema.json
```

## Evidence Rules

The `evidence_rules.yaml` file:
- Defines required top-level directories
- Specifies standard-specific subdirectories
- Lists required file patterns
- Identifies deprecated directories

### Usage

```bash
# Validate evidence tree structure
python3 scripts/validate_evidence_tree.py --root evidence --rules schemas/evidence_rules.yaml
```

## Validation Framework

Schemas are used by:
- Makefile validation targets (`make validate-plans`)
- Pre-commit hooks (`.pre-commit-config.yaml`)
- CI/CD pipelines
- Manual validation scripts

## See Also

- [Scripts](../scripts/README.md) - Validation scripts
- [Makefile](../Makefile) - Validation targets
- [Plans](../plans/README.md) - Plans validated by these schemas
