# Validation Scripts

This directory contains Python scripts for validating certification artifacts.

## Purpose

Provides automated validation tools for:
- Evidence tree structure verification
- Compliance checking
- Data integrity validation

## Available Scripts

| Script | Language | Purpose |
|--------|----------|---------|
| `validate_evidence_tree.py` | Python 3 | Validates evidence directory structure against rules |

## Evidence Tree Validation Script

The `validate_evidence_tree.py` script:
- Validates evidence directory structure
- Checks for required subdirectories per standard
- Identifies missing evidence directories
- Detects deprecated directories
- Supports JSON and human-readable output

### Usage

```bash
# Basic validation with human-readable output
python3 scripts/validate_evidence_tree.py --root evidence --rules schemas/evidence_rules.yaml

# JSON output for automation
python3 scripts/validate_evidence_tree.py --root evidence --rules schemas/evidence_rules.yaml --json

# Help information
python3 scripts/validate_evidence_tree.py --help
```

### Output

The script provides:
- **Info**: Successfully validated items
- **Warnings**: Non-critical issues (e.g., empty directories)
- **Errors**: Critical issues (e.g., missing required directories)
- **Status**: Overall validation pass/fail

### Exit Codes

- `0`: Validation passed
- `1`: Validation failed (errors found)

## Integration

Scripts are integrated with:
- Makefile validation targets (`make validate-evidence`)
- Pre-commit hooks (`.pre-commit-config.yaml`)
- CI/CD pipelines
- Manual validation workflows

## Dependencies

Scripts require:
- Python 3.8 or later
- PyYAML (for YAML parsing)
- Standard library modules only

## See Also

- [Schemas](../schemas/README.md) - Validation rules and schemas
- [Makefile](../Makefile) - Validation targets
- [Evidence](../evidence/README.md) - Evidence structure being validated
