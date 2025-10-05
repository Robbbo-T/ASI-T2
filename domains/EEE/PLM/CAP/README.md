# CAP — Computer Aided Processes

**Process**: Cross-functional processes (DevOps, CI/CD, QA/Testing, observability).

## Purpose

This directory contains Computer Aided Processes (CAP) artifacts including CI/CD pipelines, test evidence, and process automation scripts. CAP can also be used as an overlay on other CAx files.

## Artifact Types

- **Outputs**: Pipeline definitions, test reports, evidence packages, automation scripts
- **DISC codes**: PIPE (Pipeline), JOB (Job Definition), TESTSET (Test Suite), EVID (Evidence), RPT (Report)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAP5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
PIPE-BWQ1-CAP5710-FWD-SPAR-CI-PIPELINE-r001.yaml
EVID-BWQ1-CAP5710-WING-QA-TEST-REPORT-r004.pdf
JOB-BWQ1-CAP5710-NIGHTLY-BUILD-r002.yml
```

## CAP as Overlay

CAP can also be used as an optional overlay on other CAx files to indicate process stage:

```
-CAP.[CI|CD|QA|TEST|UNIT|E2E|PERF|HIL|SIL|LINT|SCHEMA|BREX|SEC|TRACE|LOG|MON].[DEV|INT|STG|PROD]
```

Example: `FEM-BWQ1-CAE5710-FS-BOX-STAT-CAP.TEST.STG-r006.inp`

## File Extensions

Typical extensions: `yml`, `yaml`, `json`, `xml`, `csv`, `pdf`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
