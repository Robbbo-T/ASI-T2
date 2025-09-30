# CAUiX Manifests

This directory contains CAUiX manifest files that define automated execution configurations for certification workflows.

## Purpose

Manifests specify how CAUiX templates should be executed, including:
- Execution triggers (schedule, on_commit, manual)
- Input parameters
- Output specifications
- Retention policies

## Available Manifests

| Manifest | Version | Template | Purpose |
|----------|---------|----------|---------|
| `index-cert@v1.0.0.manifest.yaml` | v1.0.0 | index-cert@v1.0.0 | Automated evidence indexing |
| `validate-cert@v1.0.0.manifest.yaml` | v1.0.0 | validate-cert@v1.0.0 | Evidence validation on commit |
| `generate-evidence@v1.0.0.manifest.yaml` | v1.0.0 | generate-evidence@v1.0.0 | Evidence package generation |

## Usage

Manifests are used by the CAUiX automation system to execute certification workflows. They reference templates from the `../templates/` directory and define specific execution parameters for each workflow.

## See Also

- [CAUiX Templates](../templates/README.md) - Template definitions
- [CAUiX Documentation](../../README.md) - Overview of CAUiX integration
