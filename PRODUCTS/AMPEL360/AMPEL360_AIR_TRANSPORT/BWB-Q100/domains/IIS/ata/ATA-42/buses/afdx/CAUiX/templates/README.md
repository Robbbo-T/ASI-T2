# CAUiX Templates

This directory contains CAUiX template files for automated processing of AFDX documentation and configuration.

## Purpose

Templates define the structure and logic for automated processing tasks including:
- Document indexing and cross-referencing
- Configuration validation
- Data transformation and formatting
- Refactoring and segregation operations

## Contents

| Template | Version | Purpose |
|----------|---------|---------|
| `index-s1000d@v1.0.0.yaml` | 1.0.0 | Index S1000D artifacts (data modules, figures, DMRL, BREX) |
| `validate-afdx@v1.0.0.yaml` | 1.0.0 | Validate AFDX configuration and documentation |
| `refactor-segregate@v1.0.0.yaml` | 1.0.0 | Support domain segregation refactoring |

## Template Structure

Each template includes:
- **name**: Template identifier
- **version**: Semantic version
- **description**: Template purpose
- **input**: Input file patterns and sources
- **output**: Output format and destination
- **template**: Processing logic (Handlebars syntax)

## Usage

Templates are invoked through their corresponding manifests:
```bash
# Example invocation (via CAUiX engine)
cauix process --template index-s1000d@v1.0.0 --manifest ../manifests/index-s1000d@v1.0.0.manifest.yaml
```

## Related Files

- Manifests: [../manifests/](../manifests/)
- Parent Documentation: [../../README.md](../../README.md)
