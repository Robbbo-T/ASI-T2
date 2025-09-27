# CAD Geometry Metadata

This directory contains metadata files for CAD geometry artifacts in the AMPEL360 PLUS space vehicle design.

## Purpose

Stores structured metadata for CAD geometry files following the CAD manifest schema, providing traceability, versioning, and integration information for all geometry assets.

## File Types

- **`*.cad.json`** - CAD manifest files following the `cad_manifest.schema.json` schema
- Each manifest describes exports, references, geometry properties, and UTCS provenance for a specific CAD artifact

## Naming Convention

```
PLUS-<TYPE>-<REV>.cad.json
```

Where:
- `<TYPE>` = Geometry type (OML, INTERFACE, etc.)
- `<REV>` = Revision identifier ([A-Z][0-9]{2})

Examples:
- `PLUS-OML-A02.cad.json` - Outer mold line revision A02
- `PLUS-INTERFACE-B03.cad.json` - Interface geometry revision B03

## Schema Validation

All manifest files are validated against:
- **Schema**: `../../schemas/cad_manifest.schema.json`
- **Validation**: Run `python ../../scripts/validate_json.py ../../schemas/ ../`

## Content Structure

Each manifest includes:
- **Identity**: ID, vehicle, kind, revision, status
- **Exports**: Paths to STEP/IGES/X_T files with format and purpose
- **References**: Links to ATA practices and S1000D data modules
- **Geometry**: Bounding box, coordinate system, material properties
- **UTCS**: Canonical hash and provenance for quality assurance

## Integration

- **Exports** reference files in `../exports/` directory
- **ATA References** link to `../../../../ata/ATA-20/` and `../../../../ata/ATA-57/`
- **Evidence** stored in `../../evidence/` directory structure