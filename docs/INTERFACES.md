# CXP Interfaces

## Overview
Context eXchange Points (CXP) define how ASI-T2 exposes and consumes context across repositories.

## Inputs (Inbound)
Required context and requirements from external sources:
- **Upstream Manifests**: UTCS context manifests from dependencies
- **SBOM**: Software Bill of Materials from external components
- **Architecture Documents**: System architecture from related projects
- **Requirements**: Traced requirements from stakeholders

### Expected Formats
- UTCS manifest: JSON conforming to `context.schema.json`
- SBOM: SPDX 2.3+ JSON format
- Documentation: Markdown with frontmatter
- Requirements: Structured YAML or JSON

## Outputs (Outbound)
Manifests, documentation, and evidence we export:

### Primary Exports
1. **CXP Manifest** (`UTCS/context.manifest.json`)
   - Repository metadata
   - Domain catalog
   - Interface contracts
   - Dependency graph

2. **Architecture** (`docs/ARCHITECTURE.md`)
   - LLC/MAL structure
   - Domain organization
   - Traceability flows

3. **SBOM** (`sbom/spdx.sbom.json`)
   - Software inventory
   - License information
   - Vulnerability tracking

### Secondary Exports
- Schema definitions
- Interface contracts
- Test vectors
- Example data

## Versioning
- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Compatibility Policy**:
  - MAJOR: Breaking changes to interfaces
  - MINOR: Backward-compatible additions
  - PATCH: Bug fixes and documentation updates

### Breaking Change Rules
Breaking changes require:
1. Advance notice (documented in CHANGELOG)
2. Migration guide
3. Deprecation period (minimum 1 minor version)
4. Clear error messages for incompatible usage

## Consumption Workflow
To consume context from ASI-T2:
1. Fetch `UTCS/context.manifest.json`
2. Validate against `UTCS/context.schema.json`
3. Retrieve referenced artifacts (SBOM, docs)
4. Update your `UTCS/links.map.json` with inbound reference

## Publishing Workflow
To publish context updates:
1. Update relevant files (manifest, docs, SBOM)
2. Run `cxp-publish` workflow
3. Manifest is stamped with commit hash and timestamp
4. Validated against schema
5. Artifacts uploaded for consumers
