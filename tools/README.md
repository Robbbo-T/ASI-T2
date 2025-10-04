# Tools - Teknia Token CLI v3.1

This directory contains command-line tools for managing the ASI-T2 ecosystem.

## Overview

### Teknia Token v3.1 Features

- **Quantum Transfer Enforcement**: Minimum 2592 deg (7.2 TT) per transfer
- **Founder Allocation**: 5% (100M TT) allocated at genesis to FOUNDER account
- **Sustain Fee**: 0.5% deducted from sender on all transfers
- **Three-Account System**: TREASURY, FOUNDER, VAULT_SUSTAIN
- **Transaction Logging**: SHA-256 hashed audit trail in `finance/ledger.log`
- **Integer Precision**: All amounts in exact integer deg values

## tek_tokens.py

The Teknia Token (TT) management CLI tool v3.1.

### Requirements

- Python 3.8+
- No additional dependencies

### Commands

#### Initialize Ledger (v3.1)

```bash
python tek_tokens.py init
```

**v3.1 Initialization:**
- Mints 2,000,000,000 TT (720B deg) total supply
- Allocates 5% (100M TT / 36B deg) to FOUNDER account
- Allocates 95% (1.9B TT / 684B deg) to TREASURY account
- Creates VAULT_SUSTAIN account (0 deg initially)

**Output:**
```
✓ Ledger initialized (v3.1)
✓ Genesis supply: 2,000,000,000 TT (720,000,000,000 deg)
✓ Founder allocation (5%): 100,000,000.00 TT (36,000,000,000 deg)
✓ Treasury balance: 1,900,000,000.00 TT (684,000,000,000 deg)
✓ Sustain vault: 0 TT (0 deg)
```

#### Check Balances

```bash
# All accounts
python tek_tokens.py balance

# Specific account
python tek_tokens.py balance <account_name>
```

**v3.1 Accounts:**
- `TREASURY` - Main operational treasury (95% of genesis)
- `FOUNDER` - Founder allocation (5% of genesis)
- `VAULT_SUSTAIN` - Accumulates 0.5% fees from all transfers
- `user/<username>` - User accounts (created on first transfer)

#### Perform Transaction (v3.1)

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

**⚠️ v3.1 Requirements:**
- Amount must be a multiple of 2592 deg (7.2 TT quantum)
- Sender must have sufficient balance for transfer + 0.5% sustain fee
- Fee is automatically deducted and sent to VAULT_SUSTAIN

**Valid Examples:**

```bash
# Transfer 7.2 TT (2592 deg = 1x quantum)
python tek_tokens.py tx --type transfer --amount 7.2 --tokens --from TREASURY --to user/alice
# Sender pays: 2604 deg (2592 + 12 fee)
# Recipient gets: 2592 deg
# Vault gets: 12 deg

# Transfer 14.4 TT (5184 deg = 2x quantum)
python tek_tokens.py tx --type transfer --amount 14.4 --tokens --from TREASURY --to user/bob

# Transfer 72 TT (25920 deg = 10x quantum)
python tek_tokens.py tx --type transfer --amount 72 --tokens --from TREASURY --to user/charlie
```

**Invalid Examples (will be rejected):**

```bash
# 1 TT = 360 deg (not multiple of 2592)
python tek_tokens.py tx --type transfer --amount 1 --tokens --from TREASURY --to user/alice
# ERROR: Not a multiple of min_transfer_deg

# 0.1 TT = 36 deg (not multiple of 2592)
python tek_tokens.py tx --type transfer --amount 0.1 --tokens --from TREASURY --to user/bob
# ERROR: Not a multiple of min_transfer_deg

# 3 TT = 1080 deg (not multiple of 2592)
python tek_tokens.py tx --type transfer --amount 3 --tokens --from TREASURY --to user/charlie
# ERROR: Not a multiple of min_transfer_deg
```

#### Generate Verification Badge

```bash
python tek_tokens.py verify
```

Creates `finance/token_badge.json` for shields.io badges.

### Transaction Types

- **transfer** - Generic token transfer
- **cxp_publish_reward** - Reward for publishing content
- **cxp_consume_charge** - Charge for consuming content

**Note:** All transaction types are subject to quantum validation (2592 deg minimum) and 0.5% sustain fee.

### Account Naming Conventions (v3.1)

**System Accounts (uppercase):**
- `TREASURY` - Main treasury account (95% of genesis)
- `FOUNDER` - Founder allocation (5% of genesis)
- `VAULT_SUSTAIN` - Sustainability vault (accumulates fees)

**User Accounts:**
- `user/<username>` - User accounts (e.g., `user/alice`)
- `contract/<name>` - Smart contract accounts
- `reserve/<purpose>` - Reserve accounts

### Sustain Fee Calculation

All transfers automatically deduct a 0.5% fee from the sender:

```
Fee = (amount_deg × 50) // 10000  (floor division)

Examples:
  2,592 deg → 12 deg fee
  5,184 deg → 25 deg fee
  25,920 deg → 129 deg fee
```

### Transaction Logging

All transactions are logged to `finance/ledger.log` with:
- Transaction ID
- Timestamp (ISO 8601 UTC)
- Source and destination accounts
- Amount in deg
- SHA-256 hash for audit trail

Example log entry:
```json
{"id": "TX-000002", "timestamp": "2025-10-04T12:55:44Z", "src": "TREASURY", "dst": "user/alice", "deg": 2592, "hash": "cc4085562bd175e7"}
```

## test_tek_tokens.py

Comprehensive test suite for Teknia Token v3.1.

### Running Tests

```bash
python test_tek_tokens.py
```

### Test Coverage

- ✓ Ledger initialization with founder allocation
- ✓ Quantum validation (2592 deg multiples)
- ✓ Sustain fee calculation and collection
- ✓ Balance integrity with fees
- ✓ Invalid transfer rejections (1 deg, 360 deg, 36 deg, 18 deg, 1080 deg)
- ✓ Transaction logging verification
- ✓ Three-account initialization

**Results:** 30 tests, 100% pass rate

## Documentation

- **Complete Guide**: [docs/TOKENS.md](../docs/TOKENS.md)
- **Finance README**: [finance/README.md](../finance/README.md)
- **Tokenomics Config**: [finance/teknia.tokenomics.json](../finance/teknia.tokenomics.json)

## Version History

- **v3.1.0** - Quantum validation, founder allocation, sustain fees, transaction logging
- **v1.0.0** - Initial release with 360-degree divisibility
