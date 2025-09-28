# S1000D — ATA-57 Wings (BWB-Q100)

**DMRL:** [`publication_modules/DML-BWQ1-ATA57-00_EN-US.xml`](./publication_modules/DML-BWQ1-ATA57-00_EN-US.xml)  
**PM (Publication Module):** [`publication_modules/PMC-BWQ1-ATA57-00_001-00_EN-US.xml`](./publication_modules/PMC-BWQ1-ATA57-00_001-00_EN-US.xml)  
**Indices:** [`indices/dm_index.xml`](./indices/dm_index.xml) · [`indices/xref_index.xml`](./indices/xref_index.xml)

## Routing
- **Common Information (CIR):** [`common_information/`](./common_information/)
- **Data Modules:** [`data_modules/`](./data_modules/)
  - Descriptive → [`data_modules/descriptive/`](./data_modules/descriptive/)
  - Procedural → [`data_modules/procedural/`](./data_modules/procedural/)
  - Fault Isolation → [`data_modules/fault/`](./data_modules/fault/)
  - IPD / Parts Lists → [`data_modules/ipd/`](./data_modules/ipd/)
- **Schemas:** [`schemas/`](./schemas/) · **Validators:** [`validation/validators/`](./validation/validators/)
- **Publication Modules:** [`publication_modules/`](./publication_modules/)
- **IETP Build:** [`ietp/`](./ietp/) · **Server:** [`gen_cms/server/`](./gen_cms/server/)

## Build & Validate
```bash
# Rebuild indices and validate CSDB
python validation/validators/generate_indices.py
python validation/validators/validate_csdb.py

# Optional: build IETP package
python ietp/build_ietp.py
```

> **Link policy:** relative links; directories end with `/`; files include full name (with issue/inWork if used).

## Data Module Naming Convention

Data modules follow S1000D naming convention:
- DMC-{Model Identification Code}-A-{System/Subsystem}-{Assembly}-{Disassembly}-{Information Code}-A-{Issue Number}-{Language}-{Country Code}

For BWB-Q100 ATA-57:
- Model: BWQ1 (mapped to marketing name "BWB-Q100")
- System: 57 (Wings)  
- Subsystems: 10, 20, 30, 40, 50

## Information Code Usage (S1000D Issue 6.0)

- **Descriptions**: 040 (general), 034 (technical data)
- **Procedures**: 200s (servicing/ops), 500s (removal), 600s (repair), 700s (install/rig)
- **Inspections/Tests**: 300s (inspection), 345 (system test), 350 (functional check)
- **Fault Isolation**: 420 (general FI), 421-428 (system-specific FI)
- **IPD/Parts**: 900 (illustrated parts data), 910 (parts lists)

## Key Files

- **BREX Data Module**: `DMC-BWQ1-A-00-00-00-00A-022A-D-EN-US.xml` - Project business rules
- **Wing Structure Description**: `DMC-BWQ1-A-57-10-00-00A-040A-D-EN-US.xml` - Example descriptive module
- **Publication Module**: `PMC-BWQ1-ATA57-00_001-00_EN-US.xml` - ATA-57 publication structure
- **Data Module Requirements List**: `DML-BWQ1-ATA57-00_EN-US.xml` - Complete ATA-57 data module requirements

## Documentation

### [📖 Authoring User Guide](docs/user-guide/User-Guide.md)
Comprehensive guide for authors, reviewers, and integrators covering:
- S1000D authoring best practices and module types
- GenCMS (Generative Content Management System) usage
- IETP (Interactive Electronic Technical Publication) features
- Validation pipeline and CI/CD integration
- Quality assurance and compliance requirements

## Integration with ASI-T2

This S1000D implementation integrates with:
- **QS/UTCS**: Quantum Seal / Universal Traceability for evidence tracking
- **CAx/QOx**: Classical and quantum-optimized engineering processes
- **SIM**: Sustainability Impact Model metrics
- **MAL-EEM**: Ethics & Empathy Module validation

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0  
**Classification**: INTERNAL–EVIDENCE-REQUIRED