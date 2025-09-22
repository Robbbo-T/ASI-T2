# S1000D Schemas

S1000D Version 6 XML schemas and validation files for ATA-57 Wings documentation.

## Contents

This directory contains:

### Core Schema Files
- **`descript.xsd`** - Descriptive data module schema (Info Code 040)
- **`brex.xsd`** - Business Rules Exchange schema (Info Code 022)  
- **`pm.xsd`** - Publication Module schema
- **`catalog.xml`** - XML catalog for schema resolution

### Schema Files Structure
```
schemas/
├── brex.xsd        # BREX data module validation
├── descript.xsd    # Descriptive data module validation  
├── pm.xsd          # Publication module validation
└── catalog.xml     # XML catalog for editor integration
```

### Validation Standards
- **S1000D Issue 6.0** compliant schemas
- **XSD-based validation** (not DTD)
- **Model Identification Code** validation (BWQ1 format)
- **Business rule compliance** via BREX schema

## Editor Integration

Configure your XML editor to use the catalog:
1. Point editor to `catalog.xml` for schema resolution
2. Enable XSD validation for S1000D files
3. Use schema hints in data modules: `xsi:noNamespaceSchemaLocation="../../schemas/[type].xsd"`

## Schema Validation Workflow

1. **Author** data modules with proper schema references
2. **Validate** against appropriate XSD schema
3. **Apply** BREX business rules via BREX schema
4. **Verify** BWQ1 MIC compliance
5. **Generate** publications via PM schema

## Integration Extensions

Custom schema validation for:
- **QS/UTCS** quantum traceability elements
- **SIM** sustainability metrics elements
- **CAx/QOx** engineering process references
- **MAL-EEM** ethics validation markers

## Usage

All ATA-57 data modules validate against these schemas:
- Descriptive modules → `descript.xsd`
- BREX modules → `brex.xsd`  
- Publication modules → `pm.xsd`

Validation ensures:
- Proper S1000D Issue 6.0 structure
- Valid MIC format (BWQ1)
- Business rule compliance
- Schema-driven content validation