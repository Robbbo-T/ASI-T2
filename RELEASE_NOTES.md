# Release Notes

## Version 1.0.0 - CXP Starter Kit

### Release Date
2025-01-XX

### Overview
Initial release of CXP (Context eXchange Points) infrastructure for ASI-T2, enabling structured context exchange between repositories.

### New Features

#### CXP Infrastructure
- **UTCS Manifest System**: Machine-readable context exposure via `UTCS/context.manifest.json`
- **Links Map**: Inbound/outbound relationship tracking in `UTCS/links.map.json`
- **Schema Validation**: JSON Schema for manifest validation

#### Documentation
- **GENESIS.md**: Canon reference and SSoT definition
- **ARCHITECTURE.md**: LLC/MAL architecture documentation
- **INTERFACES.md**: CXP interface specifications

#### Governance
- **CODEOWNERS**: Repository ownership definitions
- **SECURITY.md**: Security policy and vulnerability disclosure
- **GOVERNANCE.md**: Technical review and release management processes

#### Automation
- **cxp-publish.yml**: Automated manifest publishing and SBOM generation
- **cxp-consume.yml**: Remote manifest consumption workflow
- **tek-tokens-verify.yml**: TeknIA Tokens ledger verification

#### TeknIA TOKENS (TT)
- **Tokenomics**: Budget system for knowledge exchange
- **Append-only Ledger**: Verifiable transaction history
- **CLI Tool**: `tek_tokens.py` for ledger management
- **Automatic Charging**: CXP events trigger TT rewards/costs

### Components

#### Machine-Readable Context (UTCS/)
- `context.manifest.json` - Repository metadata and interfaces
- `context.schema.json` - Validation schema
- `links.map.json` - Relationship mappings

#### Human-Readable Context (docs/)
- `GENESIS.md` - Canon reference
- `ARCHITECTURE.md` - System architecture
- `INTERFACES.md` - CXP specifications
- `TOKENS.md` - TT rules and decision points

#### Evidence (sbom/)
- `spdx.sbom.json` - SPDX 2.3 Software Bill of Materials

#### Finance (finance/)
- `teknia.tokenomics.json` - TT configuration
- `ledger/tt-ledger.jsonl` - Transaction log
- `badges/tt-balance.json` - Balance badge endpoint

#### Tools (tools/)
- `tek_tokens.py` - CLI for TT management

### GitHub Actions
- **CXP Publish**: Validates and publishes context manifests
- **CXP Consume**: Fetches and validates remote manifests
- **TT Verify**: Validates ledger integrity and updates badge

### Templates
- **Issue Template**: `cxp_request.yml` for context requests
- **PR Template**: Updated with CXP checklist

### Configuration
- **Badges**: Added CXP status badges to README

### Breaking Changes
None (initial release)

### Migration Guide
Not applicable (initial release)

### Known Issues
- SBOM generation requires `syft` tool (optional at H0 phase)
- TT badge endpoint requires external hosting setup

### Future Enhancements
- Label-driven TT rewards
- Domain-specific TT accounts
- Signature verification with GPG/OIDC
- CLI extensions for bundle operations

### Contributors
- @amedeo.pelliccia
- ASI-T Architecture Team

### See Also
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [GOVERNANCE.md](governance/GOVERNANCE.md) - Governance model
- [UTCS v5.0](UTCS_BUNDLE/) - Evidence framework
