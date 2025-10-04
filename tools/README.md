# Tools - Teknia Token CLI

This directory contains command-line tools for managing the ASI-T2 ecosystem.

## tek_tokens.py

The Teknia Token (TT) management CLI tool.

### Requirements

- Python 3.8+
- No additional dependencies

### Commands

#### Initialize Ledger

```bash
python tek_tokens.py init
```

Mints 2,000,000,000 TT to the treasury account (first time only).

#### Check Balances

```bash
# All accounts
python tek_tokens.py balance

# Specific account
python tek_tokens.py balance <account_name>
```

#### Perform Transaction

```bash
python tek_tokens.py tx \
  --type <transfer|cxp_publish_reward|cxp_consume_charge> \
  --amount <amount> \
  [--tokens] \
  --from <source_account> \
  --to <destination_account>
```

**Flags:**
- `--tokens`: Amount is in TT (converts to deg). Without this flag, amount is in deg.

**Examples:**

```bash
# Transfer 1 TT
python tek_tokens.py tx --type transfer --amount 1 --tokens --from treasury --to user/alice

# Transfer 180 deg (0.5 TT)
python tek_tokens.py tx --type transfer --amount 180 --from treasury --to user/bob

# Reward for publishing (3 TT = 1080 deg)
python tek_tokens.py tx --type cxp_publish_reward --amount 3 --tokens --from treasury --to user/alice

# Charge for consuming (2 TT = 720 deg)
python tek_tokens.py tx --type cxp_consume_charge --amount 2 --tokens --from user/alice --to treasury
```

#### Generate Verification Badge

```bash
python tek_tokens.py verify
```

Creates `finance/token_badge.json` for shields.io badges.

### Transaction Types

- **transfer** - Generic token transfer
- **cxp_publish_reward** - Reward for publishing content (default: 3 TT)
- **cxp_consume_charge** - Charge for consuming content (default: 2 TT)

### Account Naming Conventions

- `treasury` - Main treasury account
- `user/<username>` - User accounts (e.g., `user/alice`)
- `contract/<name>` - Smart contract accounts
- `reserve/<purpose>` - Reserve accounts

## Documentation

See [docs/TOKENS.md](../docs/TOKENS.md) for complete documentation.
