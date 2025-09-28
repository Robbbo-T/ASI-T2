# BWB-Q100 Assembly Management Scripts

## Overview

Automation and validation scripts for BWB-Q100 airframe assembly management.

## Scripts

### `validate_assembly_links.py`

**Purpose**: Comprehensive validation of assembly structure, metadata, and cross-references.

**Features**:
- Assembly directory structure validation
- ATA chapter scope compliance (airframes only: ATA-51/52/53/54/55/56/57)
- Control surface mapping consistency checks
- Broken link detection
- Metadata consistency validation
- JSON output for CI integration

**Usage**:
```bash
# Standard validation
python validate_assembly_links.py --base domains/AAA/cax/CAD

# JSON output for CI
python validate_assembly_links.py --base domains/AAA/cax/CAD --json
```

### `create_assembly_folders.sh`

**Purpose**: Automated creation of assembly folder structure with proper templates.

**Features**:
- Creates all 20 specified ASM folders
- Applies metadata templates with correct assembly IDs
- Generates required subdirectories (models/, drawings/, icd/)
- Cross-platform compatibility (macOS/Linux)
- Idempotent operation (safe to run multiple times)

**Usage**:
```bash
# Run from BWB-Q100 root directory
bash domains/AAA/cax/CAD/scripts/create_assembly_folders.sh
```

## CI Integration

These scripts are integrated into GitHub Actions workflow:
- `.github/workflows/airframes_validate.yml`
- Automatic validation on CAD changes
- Prevents invalid assembly configurations

## Assembly Scope

Scripts enforce **airframes-only** scope:
- ATA-51: Structure - General
- ATA-52: Doors  
- ATA-53: Fuselage
- ATA-54: Nacelles/Pylons
- ATA-55: Stabilizers
- ATA-56: Windows
- ATA-57: Wings

Non-airframe components (avionics, systems, etc.) are excluded from validation.