# CAD Domain Usage Guide

This guide explains how to use the comprehensive CAD domain structure and validation tools implemented for AMPEL360 PLUS space vehicle design.

## 🚀 Quick Start

### Prerequisites
```bash
# Install required Python packages
pip install jsonschema pyyaml

# Install pre-commit (optional, for CI)
pip install pre-commit
pre-commit install
```

### Directory Structure Overview
```
CAD/
├── geometry/             # Parametric OML, fairings, windows, etc.
├── structure/            # Frames, ribs, spars, joints
├── tps/                  # Thermal protection systems
├── interfaces/           # Seats, restraints, hatches, landing gear
├── mdo/                  # Multi-disciplinary optimization configs
├── qox_bridge/           # Quantum optimization problems
├── pax/                  # Packaging (OB/OFF)
├── schemas/              # JSON schemas for validation
└── scripts/              # Validation tools
```

## 📋 JSON Schemas

### CAD Manifest Schema
Used for: `geometry/metadata/*.cad.json`, `structure/metadata/*.json`
```bash
# Validate CAD manifests
python3 scripts/validate_json.py schemas/ geometry/ structure/
```

### QOx Problem Schema
Used for: `qox_bridge/problems/*.json`
```bash
# Validate quantum optimization problems
python3 scripts/validate_json.py schemas/ qox_bridge/
```

### PAx Package Schema
Used for: `pax/**/*.json`
```bash
# Validate packaging manifests
python3 pax/scripts/validate_pax.py pax/OB/manifests/*.json
```

## 🔧 Validation Tools

### 1. JSON Schema Validation
```bash
# Validate all JSON files against appropriate schemas
python3 scripts/validate_json.py schemas/ geometry/ qox_bridge/ structure/ tps/
```

### 2. Link Validation
```bash
# Check all relative paths and references
python3 scripts/link_check.py .
```

### 3. Naming Convention Guard
```bash
# Enforce PLUS naming conventions
python3 scripts/naming_guard.py .
```

### 4. PAx Package Validation  
```bash
# Validate packaging manifests
python3 pax/scripts/validate_pax.py --schema pax/schemas/package.schema.json --root pax/
```

## 📝 File Naming Conventions

### CAD Exports
```
PLUS-<MODULE>-<FEATURE>-<REV>.<ext>
Examples:
- PLUS-OML-window-A02.step
- PLUS-TPS-tiling-v05.iges
- PLUS-STRUCT-topoRibs-2025Q3.x_t
```

### CAD Manifests
```
PLUS-<TYPE>-<ID>.cad.json
Examples:
- PLUS-OML-A02.cad.json
- PLUS-STRUCT-B03.cad.json
```

### QOx Problems
```
PLUS-<DOMAIN>-<PROBLEM>-QUBO-<ID>.json
Examples:
- PLUS-TPS-TILING-QUBO-001.json
- PLUS-STRUCT-TOPOLOGY-QUBO-002.json
```

### Package Manifests
```
PLUS-CAD-<TYPE>-<ID>.json
Examples:
- PLUS-CAD-EXPORTER-001.json
- PLUS-CAD-VALIDATOR-A02.json
```

## 🎯 Example Workflows

### Adding a New CAD Design

1. **Create CAD Model** (using CATIA/NX/Fusion360)
2. **Export Geometry**
   ```bash
   # Place exports in geometry/exports/
   PLUS-OML-cockpit-A03.step
   PLUS-OML-cockpit-A03.iges
   ```

3. **Create Manifest**
   ```bash
   # Create geometry/metadata/PLUS-OML-A03.cad.json
   {
     "$schema": "../../schemas/cad_manifest.schema.json",
     "id": "PLUS-OML-A03",
     "vehicle": "AMPEL360_PLUS",
     "kind": "OML",
     "rev": "A03",
     "exports": [...]
   }
   ```

4. **Validate**
   ```bash
   python3 scripts/validate_json.py schemas/ geometry/
   python3 scripts/naming_guard.py .
   python3 scripts/link_check.py .
   ```

### Creating a Quantum Optimization Problem

1. **Define Problem**
   ```bash
   # Create qox_bridge/problems/PLUS-OML-SHAPE-QUBO-001.json
   {
     "$schema": "../../schemas/qox_problem.schema.json",
     "id": "PLUS-OML-SHAPE-QUBO-001",
     "goal": "Optimize outer mold line for aerodynamic efficiency",
     "variables": {...},
     "objective": [...],
     "constraints": [...]
   }
   ```

2. **Validate**
   ```bash
   python3 scripts/validate_json.py schemas/ qox_bridge/
   ```

### Packaging for Deployment

1. **Create Package Manifest**
   ```bash
   # Create pax/OFF/manifests/PLUS-CAD-VIEWER-001.json
   {
     "package_name": "PLUS-CAD-VIEWER-001",
     "package": {
       "kind": "OFF-CAD-EXPORTER",
       "cad_specific": {
         "supported_formats": ["STEP", "IGES"],
         "geometry_types": ["OML", "STRUCTURE"]
       }
     }
   }
   ```

2. **Validate**
   ```bash
   python3 pax/scripts/validate_pax.py pax/OFF/manifests/PLUS-CAD-VIEWER-001.json
   ```

## 🔄 CI/CD Integration

The pre-commit hooks automatically run validation on changed files:

```yaml
# .pre-commit-config.yaml includes:
- id: cad-json-validation        # Validates JSON schemas
- id: cad-link-check            # Validates file references  
- id: cad-naming-guard          # Enforces naming conventions
- id: cad-pax-validation        # Validates package manifests
```

## 🆘 Troubleshooting

### Schema Validation Errors
```bash
# Check schema syntax
python3 -m json.tool schemas/cad_manifest.schema.json

# Validate specific file
python3 scripts/validate_json.py schemas/ geometry/metadata/problem-file.json
```

### Naming Convention Violations
```bash
# See detailed naming requirements
python3 scripts/naming_guard.py . 2>&1 | grep "Examples:"
```

### Missing File References
```bash
# Check what files are expected
python3 scripts/link_check.py . 2>&1 | grep "Broken link:"
```

## 📖 Further Reading

- [README.md](README.md) - Complete CAD domain documentation
- [schemas/](schemas/) - JSON schema definitions
- [PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/pax/](../../../AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/pax/) - Reference PAx implementation
- [Root README](../../../../../README.md) - ASI-T2 overview and PAx structure