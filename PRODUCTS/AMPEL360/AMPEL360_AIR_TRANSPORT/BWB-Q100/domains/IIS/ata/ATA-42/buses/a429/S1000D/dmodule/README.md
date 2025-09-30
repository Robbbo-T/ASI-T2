# S1000D Data Modules

**Parent:** [../](../)

## Purpose

Contains S1000D data modules (XML) documenting the ARINC 429 bus implementation.

## Data Modules

| File | Type | Description |
|------|------|-------------|
| DMC-Q100-A-42-60-00-00A-010A-D-EN-US.xml | Descriptive | General A429 description |
| DMC-Q100-A-42-61-00-00A-010A-D-EN-US.xml | Descriptive | A429 bus architecture |
| DMC-Q100-A-42-62-00-00A-012A-D-EN-US.xml | Descriptive | Label definitions & configuration |
| DMC-Q100-A-42-63-00-00A-030A-D-EN-US.xml | Descriptive | A429 security implementation |
| DMC-Q100-A-42-64-00-00A-020A-P-EN-US.xml | Procedural | A429 integration procedures |
| DMC-Q100-A-42-65-00-00A-020A-P-EN-US.xml | Procedural | A429 test procedures |
| DMC-Q100-A-42-69-00-00A-022A-D-EN-US.xml | Descriptive | A429 compliance documentation |

## Validation

```bash
# Validate descriptive data modules
xmllint --noout --schema ../schemas/6.0/descript.xsd *-D-EN-US.xml

# Validate procedural data modules
xmllint --noout --schema ../schemas/6.0/proced.xsd *-P-EN-US.xml
```

## Standards

- S1000D Issue 6.0
- DMC (Data Module Code) naming convention
