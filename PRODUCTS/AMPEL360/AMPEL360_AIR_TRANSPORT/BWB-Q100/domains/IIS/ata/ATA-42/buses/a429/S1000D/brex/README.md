# S1000D BREX (Business Rules Exchange)

**Parent:** [../](../)

## Purpose

Contains Business Rules Exchange (BREX) files that define project-specific validation rules for S1000D data modules.

## Files

- **BREX-ATA42-A429.xml** — Business rules for BWB-Q100 ARINC 429 implementation

## Usage

BREX files are referenced by data modules to ensure compliance with project-specific requirements beyond standard S1000D validation.

```bash
# Validate data modules against BREX rules
schematron BREX-ATA42-A429.xml ../dmodule/*.xml
```

## Standards

- S1000D Issue 6.0 BREX specification
- BWB-Q100 project business rules
