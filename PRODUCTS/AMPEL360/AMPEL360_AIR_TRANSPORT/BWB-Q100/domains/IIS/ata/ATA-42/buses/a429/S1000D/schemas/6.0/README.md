# S1000D Schemas (Issue 6.0)

**Parent:** [../../](../../)

## Purpose

Contains S1000D Issue 6.0 XML schemas and validation rules for data modules.

## Schemas

| File | Description |
|------|-------------|
| descript.xsd | Schema for descriptive data modules |
| proced.xsd | Schema for procedural data modules |
| brex.sch | Schematron rules for BREX validation |

## Usage

```bash
# Validate descriptive data modules
xmllint --noout --schema descript.xsd ../../dmodule/*-D-EN-US.xml

# Validate procedural data modules
xmllint --noout --schema proced.xsd ../../dmodule/*-P-EN-US.xml
```

## Standards

- S1000D Issue 6.0
- XML Schema Definition (XSD)
- ISO Schematron

## Note

These are placeholder schemas. Full S1000D schemas are available from http://www.s1000d.org
