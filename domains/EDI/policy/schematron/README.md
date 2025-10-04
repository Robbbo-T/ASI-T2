# Schematron — S1000D Validation Rules

This directory contains Schematron validation rules for S1000D Data Modules (DMCs).

## Purpose

Validates that S1000D Data Module Codes (DMCs) are properly aligned with the directory structure and domain organization.

## Files

### dmc-ata-align.sch

Schematron rules that validate:
1. DMCs reside under the correct domain path (`/domains/EDI/`)
2. The directory structure reflects the ATA chapter from the dmCode (`<SC>-<SSC>-<SSSC>`)

**Key Rules:**
- DMC path must contain `/domains/EDI/`
- Directory path must match the ATA structure from dmCode attributes

## Usage

### With xmllint (if available)
```bash
xmllint --noout --schematron dmc-ata-align.sch <DMC-file.xml>
```

### With Saxon or other XSLT processors
```bash
# Convert Schematron to XSLT first, then apply
saxon -xsl:iso_svrl_for_xslt2.xsl -s:dmc-ata-align.sch -o:dmc-ata-align.xsl
saxon -xsl:dmc-ata-align.xsl -s:<DMC-file.xml>
```

## S1000D Compliance

This validation ensures compliance with:
- S1000D Issue 5.0 specification
- ATA iSpec 2200 chapter structure
- Domain-based organization requirements

## Related Documentation

- Domain README: [../../README.md](../../README.md)
- S1000D Standards: [../../README.md#cas--services-in-operation](../../README.md#cas--services-in-operation)
