# SCHEMA - External Schemas

**Parent:** [../](../)

## Purpose

This directory contains external validation schemas that are referenced by S1000D data modules. These schemas provide additional validation beyond S1000D's built-in schema validation, particularly for domain-specific data payloads and custom extensions.

## Contents

### external_schema.json (3.8 KB)

**Type:** JSON Schema (Draft 2020-12)  
**Purpose:** Validation schema for inspection event payloads  
**Schema ID:** `https://ideale.eu/schemas/inspection-event.json`

**Validates:**
- Inspection event data structure
- Event types (visual, NDT UT/EC/thermography, dimensional)
- Inspector information and certifications
- Finding severity levels
- Equipment tracking and calibration
- MPD task compliance

**Used by:** Procedural DM (520A) references this schema for validating inspection event data

## What Are External Schemas?

External schemas allow S1000D data modules to:
- **Validate custom data** - Beyond standard S1000D elements
- **Enforce structure** - For domain-specific payloads
- **Enable integration** - With external systems and APIs
- **Support extensions** - Without modifying S1000D schemas

## Schema Formats Supported

### JSON Schema (Recommended)

**Advantages:**
- ✅ Industry standard for JSON validation
- ✅ Rich validation capabilities
- ✅ Wide tool support
- ✅ Human-readable
- ✅ Self-documenting

**Use for:** API payloads, configuration data, event data, integration schemas

**Draft versions:**
- Draft 2020-12 (latest)
- Draft-07 (widely supported)
- Draft-06, Draft-04 (legacy)

### XML Schema (XSD)

**Use for:** XML data validation beyond S1000D

### Schematron

**Use for:** Rule-based validation, business logic

## Referencing External Schemas from Data Modules

External schemas are referenced using `<externalPubRef>` in the data module's `dmStatus` section:

```xml
<externalPubRef id="extSchema01" 
                xlink:href="../SCHEMA/external_schema.json" 
                xlink:show="new" 
                xlink:actuate="onRequest">
  <title>External JSON Schema</title>
</externalPubRef>
```

### Reference in Content

You can refer to the schema in the content:

```xml
<para>Event payloads created during this procedure must validate against the
  <xref xrefType="external" internalRefIdRef="extSchema01">
    Inspection Event Schema
  </xref>.
</para>
```

## JSON Schema Structure

The example inspection event schema defines:

### Required Properties
- `eventType` - Type of inspection (enum)
- `timestamp` - ISO 8601 date-time
- `inspector` - Inspector details (id, name, certification)
- `findings` - Array of finding objects

### Optional Properties
- `location` - Station, zone, ATA chapter reference
- `equipment` - Equipment used and calibration
- `compliance` - MPD task and interval tracking

### Validation Rules
- String patterns (e.g., ATA chapter: `^[0-9]{2}(-[0-9]{2}(-[0-9]{2})?)?$`)
- Enumerations (severity: none, minor, major, critical)
- Required fields within nested objects
- Array item validation

## Adding New Schemas

To add a new external schema:

1. **Create schema file** in this directory
   ```bash
   # JSON Schema
   external_myschema.json
   
   # XML Schema
   external_myschema.xsd
   ```

2. **Define schema** with appropriate validation rules

3. **Reference from DM** using `<externalPubRef>`

4. **Validate** your schema is well-formed

5. **Test** with sample data

## Validating JSON Schemas

### Validate Schema Itself

```bash
# Check JSON syntax
python3 -c "import json; json.load(open('external_schema.json'))"

# Validate against JSON Schema meta-schema
jsonschema --validator Draft202012 external_schema.json
```

### Validate Data Against Schema

```python
import json
import jsonschema

# Load schema
with open('external_schema.json') as f:
    schema = json.load(f)

# Load data
with open('data.json') as f:
    data = json.load(f)

# Validate
try:
    jsonschema.validate(data, schema)
    print("✓ Data is valid")
except jsonschema.ValidationError as e:
    print(f"✗ Validation error: {e.message}")
```

## Example: Inspection Event Data

Sample data that validates against the inspection event schema:

```json
{
  "eventType": "ndt_ut",
  "timestamp": "2025-10-04T14:30:00Z",
  "inspector": {
    "id": "12345",
    "name": "John Smith",
    "certification": ["NDT Level II"]
  },
  "location": {
    "station": "FS 450",
    "zone": "57-10",
    "ata_chapter": "57-10-10"
  },
  "findings": [
    {
      "finding_id": "F001",
      "severity": "minor",
      "description": "Small surface indication detected",
      "action_required": "Monitor on next inspection"
    }
  ],
  "equipment": [
    {
      "equipment_id": "UT-2024-001",
      "equipment_type": "Phased Array UT",
      "calibration_date": "2025-09-01"
    }
  ]
}
```

## Schema Versioning

When schemas evolve:

1. **Use `$id` field** to identify schema version
2. **Create new files** for breaking changes
3. **Update references** in affected data modules
4. **Document changes** in schema description
5. **Maintain backwards compatibility** when possible

Example versioning:
```
external_schema_v1.json
external_schema_v2.json
external_schema.json -> symlink to current version
```

## Best Practices

✅ **Clear `$id`** - Use meaningful schema identifier  
✅ **Descriptive titles** - Explain schema purpose  
✅ **Rich descriptions** - Document each property  
✅ **Examples** - Provide valid data examples  
✅ **Validation** - Test schemas thoroughly  
✅ **Versioning** - Track schema changes  
✅ **Documentation** - Explain complex patterns

## Schema Design Guidelines

### Keep it Simple
- Start with required fields only
- Add optional fields as needed
- Avoid deep nesting

### Be Specific
- Use enumerations for controlled values
- Add patterns for formatted strings
- Set minimum/maximum constraints

### Make it Maintainable
- Use clear, consistent naming
- Add descriptions for all properties
- Document validation rules

### Ensure Compatibility
- Consider backwards compatibility
- Plan for future extensions
- Version schema appropriately

## Tools for Schema Development

### JSON Schema
- **Online validator:** https://www.jsonschemavalidator.net/
- **Python library:** `jsonschema`
- **JavaScript library:** `ajv`
- **Schema generator:** https://jsonschema.net/

### XML Schema (XSD)
- **xmllint** - Command-line validator
- **Oxygen XML Editor** - Full-featured IDE
- **Visual Studio** - XSD designer

## Integration with S1000D Tools

Many S1000D authoring and publishing tools support:
- Loading external schemas
- Validating data against schemas
- Schema-aware editing
- Automated validation in publishing pipeline

Check your tool documentation for specific capabilities.

## Standards Compliance

- JSON Schema Draft 2020-12
- XML Schema 1.1 (XSD)
- ISO Schematron
- S1000D Issue 6.0 external schema referencing

## Related Documentation

- [CSDB README](../README.md) - Parent directory
- [DMC Directory](../DMC/) - Data modules that reference schemas
- [JSON Schema Specification](https://json-schema.org/)
- [S1000D Specification](http://www.s1000d.org) - External schema usage

---

**Important:** External schemas should be version-controlled along with data modules. When schemas change, ensure all referencing data modules are updated and validated against the new schema version.
