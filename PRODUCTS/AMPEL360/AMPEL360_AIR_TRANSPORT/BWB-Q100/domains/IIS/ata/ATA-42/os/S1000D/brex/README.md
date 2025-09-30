# BREX (Business Rules Exchange)

This directory contains Business Rules Exchange (BREX) files for S1000D data modules in the ATA-42 OS package.

## Purpose

BREX files define business rules and validation constraints that S1000D data modules must follow. These rules ensure consistency and compliance across all technical documentation.

## Files

- **BREX-ATA42-OS.xml**: Business rules for ATA-42 OS data modules

## BREX Rules

The BREX file defines context rules including:

1. **CR-001**: All DMs must reference this BREX
2. **CR-002**: Security classification required for all modules
3. **CR-003**: Responsible party company must be specified

## Usage

BREX validation is performed during the S1000D data module validation process:

```bash
# Validate BREX compliance
schematron BREX-ATA42-OS.xml ../dmodule/*.xml
```

## Related Documents

- [S1000D Data Modules](../dmodule/)
- [Main README](../../README.md)
