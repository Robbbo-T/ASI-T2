# Shared Templates

Reusable templates and schemas for standardizing content across the IDEALE-EU Federation.

## Overview

This directory contains **federation-wide templates** that ensure consistency, compliance, and interoperability across all products, domains, and working groups. These templates implement the standards and policies defined in the governance framework.

## Available Templates

### 1. Domain Manifest Schema

**File**: [index.extracted.schema.json](./index.extracted.schema.json)

JSON Schema (Draft 2020-12) for validating domain manifest files (`index.extracted.yaml`).

**Purpose**: Enforce required metadata, classification, export control, and licensing information for all domain artifacts.

**Required Fields**:
- `schema_version`: Semantic version (e.g., "1.0.0")
- `product`: Product identifier (e.g., "AMPEL360_AIR_TRANSPORT")
- `platform`: Platform identifier (e.g., "BWB-Q100")
- `domain`: Domain code (e.g., "AAA", "IIS", "PPP")
- `classification`: OPEN | SHARED | RESTRICTED | CONTROLLED
- `export_control`: ITAR/EAR/EU dual-use declarations
- `licenses`: Code, docs, hardware license declarations
- `contacts`: Maintainer contact information

**Usage**:
```bash
# Validate a manifest
jsonschema -i path/to/index.extracted.yaml index.extracted.schema.json

# Or use the CI workflow
# .github/workflows/validate-manifests.yml
```

**See Also**: [Example manifest](../../PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/index.extracted.EXAMPLE.yaml)

---

### 2. Product README Template

**File**: [README.product.md](./README.product.md)

Markdown template for product-level README files.

**Purpose**: Standardize product documentation with federation metadata, governance links, and compliance information.

**Sections Included**:
- Product overview and mission
- Architecture and components
- Governance and ownership (CODEOWNERS)
- Classification and export control status
- Standards and certifications
- Getting started guide
- Contribution guidelines
- Security and incident response
- License information
- Contact information

**Usage**:
```bash
# Copy template to your product directory
cp Shared/_templates/README.product.md PRODUCTS/YOUR_PRODUCT/README.md

# Fill in placeholders:
# - {{PRODUCT_NAME}}
# - {{PRODUCT_DESCRIPTION}}
# - {{CLASSIFICATION}}
# - {{MAINTAINER_CONTACTS}}
# etc.
```

---

### 3. Contribution Guide Template

**File**: [CONTRIBUTING.template.md](./CONTRIBUTING.template.md)

Markdown template for domain-specific contribution guidelines.

**Purpose**: Provide consistent contributor experience while allowing customization for domain-specific workflows.

**Sections Included**:
- Code of conduct reference
- Development setup and dependencies
- Coding standards and style guides
- Testing requirements (unit, integration, compliance)
- Documentation requirements
- Review and approval process
- CI/CD pipeline expectations
- Domain-specific workflows (CAx, QOx, PAx, ATA)

**Usage**:
```bash
# Copy to your domain
cp Shared/_templates/CONTRIBUTING.template.md \
   PRODUCTS/YOUR_PRODUCT/domains/YOUR_DOMAIN/CONTRIBUTING.md

# Customize for your domain:
# - Add CAD/CFD tool requirements for CAx domains
# - Add quantum solver requirements for QOx domains
# - Add SBOM/signing requirements for PAx domains
# - Add S1000D validation for ATA domains
```

---

### 4. S1000D BREX Template

**File**: [S1000D_BREX.placeholder.xml](./S1000D_BREX.placeholder.xml)

XML template for S1000D Business Rules Exchange (BREX).

**Purpose**: Define project-specific S1000D validation rules for technical publications.

**Features**:
- SNS (Simplified Notation System) rule definitions
- Context-sensitive validation rules
- Security classification enforcement
- Issue tracking and status management
- Data module identification rules

**Usage**:
```xml
<!-- Copy to your ATA chapter directory -->
cp Shared/_templates/S1000D_BREX.placeholder.xml \
   PRODUCTS/YOUR_PRODUCT/domains/YOUR_DOMAIN/ata/ATA-XX/BREX.xml

<!-- Update project-specific values: -->
<!-- - modelIdentCode: Your project code -->
<!-- - brexDmCode: Unique BREX identifier -->
<!-- - enterpriseCode: Organization code -->
<!-- - Add custom validation rules -->
```

**Validation**:
```bash
# Validate BREX file
xmllint --schema s1000d-5.0/brex.xsd BREX.xml

# Apply BREX rules to data modules
# (use S1000D validator tool)
```

---

## Template Versioning

Templates follow semantic versioning aligned with federation schema versions:

| Template | Current Version | Schema Version | Status |
|----------|----------------|----------------|--------|
| index.extracted.schema.json | 1.0.0 | 1.0.0 | ✅ Stable |
| README.product.md | 1.0.0 | N/A | ✅ Stable |
| CONTRIBUTING.template.md | 1.0.0 | N/A | ✅ Stable |
| S1000D_BREX.placeholder.xml | 1.0.0 | S1000D 5.0 | ✅ Stable |

**Breaking changes** require major version bump and migration guide.

---

## Creating New Templates

To add a federation-wide template:

1. **Propose via RFC**: Open issue with `[RFC]` prefix describing need and scope
2. **TSC Review**: Technical Steering Committee evaluates and approves
3. **Implement**: Create template with comprehensive documentation
4. **Validate**: Test with 2+ real-world use cases
5. **Publish**: Add to this directory with version 1.0.0
6. **Announce**: Update [ROADMAP.md](../../ROADMAP.md) and notify working groups

**Template Requirements**:
- Clear purpose and scope
- Inline documentation/comments
- Placeholder syntax: `{{VARIABLE_NAME}}`
- Example/reference implementation
- Validation method (if applicable)
- Maintainer assignment in [CODEOWNERS](../../CODEOWNERS)

---

## Template Maintenance

### Updating Templates

1. **Backward compatibility**: Maintain for at least one major version
2. **Deprecation notice**: 6 months minimum before removal
3. **Migration guide**: Required for breaking changes
4. **Changelog**: Update [ROADMAP.md](../../ROADMAP.md) with version history

### Validation

All templates are automatically validated by CI:

- **Schema**: JSON Schema validation via `ajv`
- **Markdown**: Linting via `markdownlint`
- **XML**: Well-formedness via `xmllint`
- **YAML**: Linting via `yamllint`

See [.github/workflows/validate-manifests.yml](../../.github/workflows/validate-manifests.yml)

---

## Best Practices

### For Template Users

✅ **DO**:
- Copy template to appropriate location before editing
- Preserve required sections and structure
- Update version numbers when schema changes
- Test validation before committing
- Document customizations in comments

❌ **DON'T**:
- Edit templates directly in `Shared/_templates/`
- Remove required fields or sections
- Use incompatible file formats
- Skip validation steps
- Mix template versions within a product

### For Template Maintainers

✅ **DO**:
- Use clear, self-documenting placeholders
- Provide inline usage examples
- Include validation instructions
- Keep templates focused (single responsibility)
- Version aggressively (avoid breaking changes)

❌ **DON'T**:
- Make assumptions about user environment
- Include product-specific logic
- Hardcode organizational details
- Skip testing with diverse use cases
- Change semantics without version bump

---

## Related Documentation

- [Governance](../../GOVERNANCE.md) - RFC and approval process
- [Contributing](../../CONTRIBUTING.md) - General contribution guidelines
- [Policies](../../policies/) - Classification, export control, privacy, security
- [Federation Quickstart](../../FEDERATION_QUICKSTART.md) - New contributor guide

---

## Support

### Questions or Issues

- **Template bugs**: Open issue with `template:` label
- **Feature requests**: Submit RFC via GitHub Issues
- **Usage questions**: GitHub Discussions or relevant TSC mailing list

### Contacts

- **Template Maintainers**: See [CODEOWNERS](../../CODEOWNERS)
- **Schema Issues**: schema-wg@ideale-eu.example
- **General Questions**: templates@ideale-eu.example

---

**Directory Version**: 1.0.0  
**Last Updated**: 2025-01-01  
**Maintained By**: IDEALE-EU Schema Working Group

For questions about templates, open a [GitHub Discussion](https://github.com/Robbbo-T/ASI-T2/discussions) or contact templates@ideale-eu.example.
