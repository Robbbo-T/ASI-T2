# Documentation

This directory contains comprehensive documentation for the ASI-T2 ecosystem.

## Contents

### Token System v3.1

- **[TOKENS.md](TOKENS.md)** - Complete documentation for the Teknia Token (TT) system v3.1
  - Token specifications (2B TT genesis supply, 360-degree divisibility)
  - **v3.1 Features:**
    - Quantum transfer enforcement (2592 deg = 7.2 TT minimum)
    - Founder allocation (5% at genesis = 100M TT)
    - Sustain fee (0.5% per operation)
    - Three-account structure (TREASURY, FOUNDER, VAULT_SUSTAIN)
    - Transaction logging with SHA-256 hashing
    - Landauer@CMB physics integration
  - CLI tool usage and examples
  - Ledger structure and validation rules
  - CXP (Content Exchange Protocol) operations
  - Conversion tables and workflows

## Quick Links

### Token System
- Configuration: [finance/teknia.tokenomics.json](../finance/teknia.tokenomics.json)
- CLI Tool: [tools/tek_tokens.py](../tools/tek_tokens.py)
- Quick Start: [finance/README.md](../finance/README.md)
- CLI Reference: [tools/README.md](../tools/README.md)

### Other Documentation
- Master Whitepapers: [WHITEPAPERS/](../WHITEPAPERS/)
- UTCS Bundle: [UTCS_BUNDLE/README.md](../UTCS_BUNDLE/README.md)
- Finance Framework: [FINANCE/README.md](../FINANCE/README.md)
- Federation Quick Start: [FEDERATION_QUICKSTART.md](../FEDERATION_QUICKSTART.md)

## Contributing to Documentation

When adding new documentation to this directory:

1. Update this README.md to list the new document
2. Follow the existing documentation style and structure
3. Include practical examples and usage patterns
4. Cross-reference related documentation
5. Update [README-PAGES.md](../README-PAGES.md) if adding a new major topic

## Documentation Standards

- Use clear, concise language
- Include code examples with expected outputs
- Provide troubleshooting sections where appropriate
- Keep documentation synchronized with code changes
- Use consistent formatting and terminology
