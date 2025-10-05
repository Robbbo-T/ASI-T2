# CAO — Computer Aided Kick-Off

**Process**: Pre-design and program start-up: concept, requirements, architecture, baselines.

## Purpose

This directory contains Computer Aided Kick-Off (CAO) artifacts for the domain. CAO represents the initial phase of engineering development where concepts are defined, requirements are established, and system architectures are created.

## Artifact Types

- **Inputs**: Stakeholder needs, constraints, trade-off studies
- **Outputs**: Concept documents, specifications, system architecture definitions
- **DISC codes**: CON (Concept), REQ (Requirements), SYS (System Architecture)

## Naming Convention

Files in this directory follow the CAx++ naming pattern:

```
<DISC>-<MIC>-CAO5710-<SCOPE>-<HAND?>-<EFFT?>-<LIFE?>-<CAP?>-r<REV>.<EXT>
```

### Examples

```
CON-BWQ1-CAO5710-FWD-SPAR-CONFIG-GA-r001.pdf
REQ-BWQ1-CAO5710-WING-ROOT-REQUIREMENTS-r005.docx
SYS-BWQ1-CAO5710-HYDRAULIC-SYSTEM-ARCH-r003.xml
```

## File Extensions

Typical extensions: `pdf`, `docx`, `req`, `xml`, `json`

## Validation

Run the linter to validate file names:
```bash
python3 ../../policy/lints/lint_names.py .
```

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- CAx Process Definitions: [../../README.md#cax-process-definitions](../../README.md#cax-process-definitions)
