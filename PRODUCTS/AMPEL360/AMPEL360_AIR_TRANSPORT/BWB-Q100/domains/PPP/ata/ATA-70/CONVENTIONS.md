---
id: ATA-XX-CONVENTIONS
project: ASI-T2
artifact: ATA-XX Documentation Conventions
classification: INTERNAL
version: 0.1.0
release_date: 2025-09-30
maintainer: IIS (Integrated Information Systems)
language_default: en-US
enterprise_code: IIS
canonical_hash: pending
ethics_guard: MAL-EEM
---

# ATA-XX Documentation Conventions

## Overview

This document defines the conventions used throughout the ATA-XX documentation structure, including naming conventions, version control practices, front-matter YAML structure, and hashing/signing procedures.

## File Naming Conventions

### General Files
- Use lowercase with underscores (snake_case)
- Be descriptive but concise
- Include version or date when appropriate
- Examples: `system_requirements.yaml`, `test_report_20250930.md`

### S1000D Files
- Follow S1000D naming conventions for DMs and ICNs
- Use the format `DMC-[ModelIdentCode]-[SystemDiffCode]-[SystemCode]-[SubSystemCode]-[SubSubSystemCode]-[AssyCode]-[DisassyCode]-[DisassyCodeVariant]-[InfoCode]-[InfoCodeVariant]-[ItemLocationCode].xml`

### Configuration Files
- Use `.yaml` extension for configuration files
- Use `.json` for schema definitions

### Test Files
- Prefix test cases with `tc_`
- Prefix test data with `td_`

## Version Control

### Branching Strategy
- `main`: Protected branch for released versions
- `develop`: Integration branch for ongoing work
- `feature/*`: Feature branches for new development
- `hotfix/*`: Emergency fixes

### Commit Messages
- Use the imperative mood
- Include issue number when applicable
- Format: `type(scope): description`

### Tagging
- Use semantic versioning (SemVer)
- Format: `v[MAJOR].[MINOR].[PATCH]`

## Front-Matter YAML

### Required Fields
All documentation files must include YAML front-matter with required fields:

```yaml
---
id: [unique identifier]
project: ASI-T2
artifact: [artifact name]
classification: [classification level]
version: [version number]
release_date: [YYYY-MM-DD]
maintainer: [maintainer name]
language_default: [language code]
enterprise_code: [enterprise code]
canonical_hash: [hash value]
ethics_guard: MAL-EEM
---
```

## Hashing and Signing

### File Hashing
- Use SHA-256 for all file hashes
- Store hashes in manifest files
- Update hashes when files change

### Manifest Files
- Use YAML format for manifest files
- Include file paths, hashes, and metadata

## Quality Assurance

### Validation
- Use schema validation for YAML and JSON files
- Use linting tools for Markdown files
- Use XML validation for S1000D files

### Reviews
- All documentation must be reviewed before release
- Use pull requests for changes
- Track review status in project management tools

## Security Considerations

### Access Control
- Restrict access to sensitive information
- Use role-based access control
- Audit access logs regularly

### Ethics Guard
- Apply MAL-EEM ethics guard to all AI-generated content
- Review AI-generated content for accuracy and appropriateness
