# Finance - Teknia Token System

This directory contains the Teknia Token (TT) configuration and ledger files.

## Files

- **teknia.tokenomics.json** - Token economics configuration (committed to git)
- **ledger.json** - Current token ledger with all accounts and transactions (not committed)
- **token_badge.json** - Generated badge for shields.io (not committed)

## Quick Start

### Initialize the Ledger (First Time Only)

```bash
python tools/tek_tokens.py init
```

This will create `ledger.json` with:
- Treasury account: 2,000,000,000 TT (720,000,000,000 deg)
- Genesis mint transaction

### Check Balances

```bash
# Show all accounts
python tools/tek_tokens.py balance

# Show specific account
python tools/tek_tokens.py balance treasury
```

### Make Transfers

```bash
# Transfer in TT (with --tokens flag)
python tools/tek_tokens.py tx --type transfer --amount 10 --tokens --from treasury --to user/alice

# Transfer in deg directly
python tools/tek_tokens.py tx --type transfer --amount 3600 --from treasury --to user/bob
```

### Generate Badge

```bash
python tools/tek_tokens.py verify
```

## Token Specifications

- **Genesis Supply**: 2,000,000,000 TT
- **Divisibility**: 360 degrees (deg) per TT
- **Minimum Unit**: 1 deg (integer only)
- **Total Supply**: 720,000,000,000 deg

## Documentation

See [docs/TOKENS.md](../docs/TOKENS.md) for complete documentation.

## Notes

- `ledger.json` and `token_badge.json` are excluded from git via `.gitignore`
- All amounts in the ledger are stored as integer deg values
- The CLI handles conversion between TT and deg automatically
