# Documentation

This directory contains comprehensive documentation for the ASI-T2 ecosystem.

## Contents

### Token System v3.14

- **[TOKENS.md](TOKENS.md)** - Complete documentation for the Teknia Token (TT) system v3.14
  - Token specifications (2B TT genesis supply, 360-degree divisibility)
  - **v3.14 Features:**
    - **π-tier fee schedule** for transfers (0.314%, 0.99%, 3.14%)
    - Reward/consume operations use base 0.5% fee
    - Scope-based validation (min quantum on transfers only)
    - Policy immutability via SHA-256 hash verification
    - EUR valuation support (`--eur-per-tt` or `--eur-per-kwh`)
    - Transaction hash chain (`txlog.jsonl` + `txhead.json`)
    - Dual configs (hybrid with fees + no-fee variant)
  - **Enhanced CLI:** `transfer`, `reward`, `consume`, `quote`, `verify`, `badge` commands
  - Ledger structure and validation rules
  - Conversion tables and workflows
  - Migration guide from v3.1

## Quick Links

### Token System v3.14
- **Configuration:** 
  - Hybrid: [finance/teknia.tokenomics.json](../finance/teknia.tokenomics.json)
  - No-fee: [finance/teknia.tokenomics.nofee.json](../finance/teknia.tokenomics.nofee.json)
- **CLI Tool:** [tools/tek_tokens.py](../tools/tek_tokens.py)
- **Tests:** [tools/test_tek_tokens_v314.py](../tools/test_tek_tokens_v314.py)
- **Quick Start:** [finance/README.md](../finance/README.md)
- **CLI Reference:** [tools/README.md](../tools/README.md)

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

## Token System v3.14 Overview

The Teknia Token system v3.14 introduces **π-tier hybrid tokenomics**:

### Fee Structure
- **Transfers:** Dynamic π-tier fees based on amount
  - ≥ 7,200 TT → 3.14% (1000× Δθmin)
  - ≥ 720 TT → 0.99% (100× Δθmin)
  - ≥ 72 TT → 0.314% (10× Δθmin)
  - < 72 TT → 0.5% (base)
- **Reward/Consume:** Always 0.5% (predictable, not tiered)

### Policy Immutability
A SHA-256 hash of the policy section is computed at initialization and stored in `ledger.json`. The `verify` command ensures the policy hasn't been silently modified.

### Transaction Hash Chain
Each transaction is logged to `txlog.jsonl` with a cryptographic hash chain:
```
TX_N_hash = SHA256(TX_{N-1}_hash + tx_data)
```
The chain head is stored in `txhead.json` for efficient verification.

### Example Usage
```bash
# Initialize with v3.14
python tools/tek_tokens.py init

# Transfer 720 TT (uses 0.99% π-tier fee)
python tools/tek_tokens.py transfer --from TREASURY --to alice --tt 720
# → Fee: 2566 deg (0.99%)

# Reward 72 TT (uses 0.5% base fee, not 0.314% π-tier)
python tools/tek_tokens.py reward --to bob --tt 72

# Quote with EUR valuation
python tools/tek_tokens.py --eur-per-tt 0.10 quote --op transfer --tt 7200

# Verify integrity & generate badge
python tools/tek_tokens.py verify
python tools/tek_tokens.py badge --out badges/tt-verified.svg
```

See [TOKENS.md](TOKENS.md) for complete documentation.
