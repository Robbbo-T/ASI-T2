# CAUiX Manifests

This directory contains CAUiX manifest files that define execution parameters and dependencies for automated processing templates.

## Purpose

Manifests specify how CAUiX templates should be executed, including:
- Input file patterns and locations
- Output destinations and formats
- Validation rules and checks
- Traceability requirements
- Execution triggers and dependencies

## Contents

| File | Template | Purpose |
|------|----------|---------|
| `index-s1000d@v1.0.0.manifest.yaml` | index-s1000d@v1.0.0 | S1000D artifact indexing execution config |
| `validate-afdx@v1.0.0.manifest.yaml` | validate-afdx@v1.0.0 | AFDX validation execution config |

## Usage

Manifests are consumed by the CAUiX execution engine to:
1. Locate and validate input files
2. Apply templates to generate outputs
3. Validate results against schemas and rules
4. Record traceability and evidence

## Related Files

- Templates: [../templates/](../templates/)
- Parent Documentation: [../../README.md](../../README.md)
