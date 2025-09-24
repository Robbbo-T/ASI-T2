# S1000D Templates

This directory contains template files for creating S1000D data modules and publication modules.

## Available Templates

- `data_module_template.xml` - Base template for all data module types with corrected S1000D Issue 6.0 compliance
- `dmrl_template.xml` - Data Module Requirements List template for system-level requirements definition

## Template Features

The data module template includes:
- **XSD-based validation** (no DTD references)
- **Valid Model Identification Code** (BWQ1 instead of BWB-Q100)
- **Proper BREX reference** to project business rules
- **Correct information code guidance**:
  - Descriptions: 040 (general), 034 (technical data)
  - Procedures: 200s (servicing/ops), 500s (removal), 600s (repair), 700s (install/rig)
  - Inspections/Tests: 300s (inspection), 345 (system test), 350 (functional check)
  - Fault Isolation: 420 (general FI), 421-428 (system-specific FI)

The DMRL template includes:
- **Requirements list structure** for complete system documentation planning
- **Standard DMRL identification** (DML-BWQ1-{ATA}-{SEQ} format)
- **Data module reference format** with proper S1000D code structure
- **Human-readable requirement comments** for traceability

## Usage

1. Copy the appropriate template file
2. Rename with proper S1000D data module code (DMC-BWQ1-...) or DMRL code (DML-BWQ1-...)
3. Replace placeholder values with actual content
4. Update schema reference to match content type (descript.xsd, dmrl.xsd, proced.xsd, etc.)
5. Validate against S1000D Issue 6.0 schemas
6. Review for ASI-T2 integration compliance

## Information Code Mapping for ATA-57

### 57-10 Wing Structure
- General/overviews: **040** (Description)
- Physical breakdowns: **034** (Technical data, physical)
- Tests (proof load, stiffness): **350**/**345** (structure/test)

### 57-20 Fuel Interfaces
- Description: **040**; functional check: **350**; leak test: **345**

### 57-30 Control Surfaces
- Removal: **5xx**; Installation/Rigging: **7xx**; Operational checks: **345** (system test)

### 57-40 High-Lift
- Install/adjust: **7xx**; Asymmetry test: **345**; Description/logic: **042** (function)

### 57-50 Equipment Integration
- Descriptions: **040/050–056** as needed

### Fault Isolation (All Subsystems)
- General FI framework: **420**; system-specific FI trees: **421–428**