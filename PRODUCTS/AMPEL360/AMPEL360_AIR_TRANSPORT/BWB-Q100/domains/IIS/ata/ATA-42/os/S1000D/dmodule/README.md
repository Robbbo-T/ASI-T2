# S1000D Data Modules

This directory contains S1000D Issue 6.0 data modules (DMs) for the ATA-42 Operating System package.

## Data Modules

| DM Code | Type | Info Code | Description |
|---------|------|-----------|-------------|
| DMC-Q100-A-42-00-00-00A-010A-D-EN-US.xml | Descriptive | 010 | General OS description |
| DMC-Q100-A-42-10-00-00A-010A-D-EN-US.xml | Descriptive | 010 | OS design overview |
| DMC-Q100-A-42-11-00-00A-010A-D-EN-US.xml | Descriptive | 010 | Architecture specification |
| DMC-Q100-A-42-12-00-00A-012A-D-EN-US.xml | Descriptive | 012 | Configuration management |
| DMC-Q100-A-42-20-00-00A-030A-D-EN-US.xml | Descriptive | 030 | Security architecture |
| DMC-Q100-A-42-30-00-00A-020A-P-EN-US.xml | Procedural | 020 | Integration procedures |
| DMC-Q100-A-42-40-00-00A-020A-P-EN-US.xml | Procedural | 020 | Test procedures |
| DMC-Q100-A-42-90-00-00A-022A-D-EN-US.xml | Descriptive | 022 | Compliance documentation |

## Data Module Types

- **Descriptive (D)**: Technical descriptions, specifications, and architecture
- **Procedural (P)**: Step-by-step procedures for integration and testing

## Validation

```bash
# Validate descriptive modules
xmllint --noout --schema ../schemas/6.0/descript.xsd *-D-EN-US.xml

# Validate procedural modules
xmllint --noout --schema ../schemas/6.0/proced.xsd *-P-EN-US.xml
```

## Related Documents

- [BREX Rules](../brex/)
- [DMRL](../dmrl/)
- [Publications](../publications/)
- [Main README](../../README.md)
