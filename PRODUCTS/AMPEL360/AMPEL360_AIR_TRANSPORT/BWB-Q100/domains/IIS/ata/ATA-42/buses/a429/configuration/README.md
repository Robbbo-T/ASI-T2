# ARINC 429 Configuration Files

**Parent:** [../](../)

## Purpose

Contains machine-readable configuration files defining ARINC 429 bus parameters and settings.

## Files

| File | Format | Description |
|------|--------|-------------|
| label_definitions.yaml | YAML | ARINC 429 label definitions with encodings |
| bus_configuration.json | JSON | Bus parameters and channel configurations |
| data_rates.conf | CONF | Data rate settings for channels |
| parity_settings.yaml | YAML | Error detection and handling configuration |

## Usage

```bash
# Validate YAML files
python -m pyyaml label_definitions.yaml parity_settings.yaml

# Validate JSON files
python -m json.tool bus_configuration.json
```

## Standards

- ARINC 429 Mark 33 specification
- Standard configuration file formats (YAML, JSON, CONF)
