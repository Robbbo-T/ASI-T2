# Assembly Template

## Overview

Template files and structure for creating new BWB-Q100 airframe assemblies.

## Contents

- **metadata.yaml**: Template metadata file with airframes-scoped configuration
- Standard assembly structure template

## Usage

This template is used by the `create_assembly_folders.sh` script to generate new assembly folders with consistent structure and metadata.

### Template Structure

Each assembly created from this template includes:

- `models/`: 3D CAD models and geometry files
- `drawings/`: 2D technical drawings and documentation
- `icd/`: Interface Control Documents
- `metadata.yaml`: Assembly metadata and configuration

### Metadata Template Features

- **Airframes scope**: Limited to ATA chapters 51, 52, 53, 54, 55, 56, 57
- **QOx integration**: Quantum optimization variables section
- **Manufacturing**: Material family and method specifications
- **Validation**: FEA/CFD requirements and certification tests
- **Revision tracking**: Version history and change management

## Customization

When creating new assemblies:

1. Copy the template structure
2. Update `assembly_id` to match folder name (ASM-XXX)
3. Customize `name`, `ata_chapter`, and other metadata
4. Define QOx optimization variables as needed
5. Specify linked components and interfaces

## Related Files

- `../scripts/create_assembly_folders.sh`: Uses this template
- `../assemblies.manifest.yaml`: Assembly registry and mapping