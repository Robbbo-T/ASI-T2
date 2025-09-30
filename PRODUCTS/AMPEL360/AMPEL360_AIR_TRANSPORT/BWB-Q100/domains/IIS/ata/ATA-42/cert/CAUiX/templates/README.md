# CAUiX Templates

This directory contains CAUiX template files that define reusable workflows for certification activities.

## Purpose

Templates provide standardized workflow definitions for:
- Evidence indexing and cataloging
- Validation of certification data
- Evidence package generation
- Audit trail maintenance

## Available Templates

| Template | Version | Type | Description |
|----------|---------|------|-------------|
| `index-cert@v1.0.0.yaml` | v1.0.0 | indexing | Scans and indexes certification evidence |
| `validate-cert@v1.0.0.yaml` | v1.0.0 | validation | Validates evidence tree structure |
| `generate-evidence@v1.0.0.yaml` | v1.0.0 | generation | Generates formatted evidence packages |
| `audit-trail@v1.0.0.yaml` | v1.0.0 | auditing | Creates audit trail entries with signatures |

## Template Structure

Each template defines:
- **Metadata**: Name, version, description
- **Inputs**: Required and optional parameters
- **Operations**: Sequence of actions to perform
- **Outputs**: Expected results and artifacts

## Usage

Templates are referenced by manifest files in the `../manifests/` directory, which specify how and when to execute each template.

## See Also

- [CAUiX Manifests](../manifests/README.md) - Execution configurations
- [CAUiX Documentation](../../README.md) - Overview of CAUiX integration
