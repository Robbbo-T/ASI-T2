# S1000D Schema Files

This directory contains S1000D Issue 6.0 schema files for validation.

## Schemas

- **descript.xsd** - Schema for descriptive data modules
- **proced.xsd** - Schema for procedural data modules
- **brex.sch** - Schematron rules for BREX validation

## Usage

These schemas are used by validation tools to ensure S1000D compliance.

```bash
# Validate descriptive DMs
xmllint --noout --schema descript.xsd ../dmodule/*-D-EN-US.xml

# Validate procedural DMs
xmllint --noout --schema proced.xsd ../dmodule/*-P-EN-US.xml
```

## Note

Full S1000D Issue 6.0 schemas should be obtained from the official S1000D specification.
These are placeholder references for the validation structure.
