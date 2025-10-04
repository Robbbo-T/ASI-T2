# Teknia Token (TT) - Documentation

## Overview

**Teknia Token (TT)** is the native token of the ASI-T2 ecosystem with unique 360-degree divisibility.

### Key Specifications

- **Token Name**: Teknia Token
- **Token Symbol**: TT
- **Genesis Supply**: 2,000,000,000 TT (2 billion)
- **Divisibility**: 360 degrees (deg) per 1 TT
- **Total Genesis Supply**: 720,000,000,000 deg (720 billion)
- **Ledger Precision**: Integer deg units only

## Token Economics

### Divisibility Model

Unlike traditional cryptocurrencies that use decimal divisibility, TT uses a **360-degree division model**:

```
1 TT = 360 deg
```

This means:
- **0.5 TT** = 180 deg ✓ (valid)
- **0.25 TT** = 90 deg ✓ (valid)
- **0.1 TT** = 36 deg ✓ (valid)
- **0.01 TT** = 3.6 deg ✗ (invalid - not an integer)

### Precision Rules

All ledger entries are stored as **integer deg values**. No fractional deg units are allowed. This ensures:
- Exact arithmetic without floating-point errors
- Deterministic transaction outcomes
- Simple verification and auditing

### Pricing Structure

The tokenomics configuration defines standard pricing for CXP (Content Exchange Protocol) operations:

| Operation | Cost/Reward (TT) | Cost/Reward (deg) |
|-----------|------------------|-------------------|
| CXP Publish Reward | 3 TT | 1,080 deg |
| CXP Consume Cost | 2 TT | 720 deg |

## CLI Tool: `tek_tokens.py`

The `tek_tokens.py` CLI tool manages the token ledger with integer deg precision.

### Installation

No installation required. The tool is located at `tools/tek_tokens.py` and uses Python 3.8+.

### Initialization

Initialize the ledger (first time only):

```bash
python tools/tek_tokens.py init
```

This mints the genesis supply of 2,000,000,000 TT (720,000,000,000 deg) to the `treasury` account.

### Balance Checking

Show all account balances:

```bash
python tools/tek_tokens.py balance
```

Show a specific account balance:

```bash
python tools/tek_tokens.py balance treasury
python tools/tek_tokens.py balance user/alice
```

### Transactions

#### Transfer Tokens

Transfer using TT (with automatic conversion to deg):

```bash
# Transfer 1 TT (360 deg)
python tools/tek_tokens.py tx --type transfer --amount 1 --tokens --from treasury --to user/alice

# Transfer 0.5 TT (180 deg)
python tools/tek_tokens.py tx --type transfer --amount 0.5 --tokens --from treasury --to user/bob

# Transfer 7.2 TT (2592 deg)
python tools/tek_tokens.py tx --type transfer --amount 7.2 --tokens --from treasury --to user/charlie
```

Transfer using deg directly:

```bash
# Transfer 2592 deg (7.2 TT)
python tools/tek_tokens.py tx --type transfer --amount 2592 --from treasury --to user/charlie

# Transfer 1080 deg (3 TT)
python tools/tek_tokens.py tx --type transfer --amount 1080 --from treasury --to user/alice
```

#### CXP Operations

Reward for publishing content:

```bash
python tools/tek_tokens.py tx --type cxp_publish_reward --amount 3 --tokens --from treasury --to user/alice
```

Charge for consuming content:

```bash
python tools/tek_tokens.py tx --type cxp_consume_charge --amount 2 --tokens --from user/alice --to treasury
```

### Verification Badge

Generate a verification badge (JSON format for Shields.io):

```bash
python tools/tek_tokens.py verify
```

This creates `finance/token_badge.json` with current treasury balance and system statistics.

## Ledger Structure

The ledger is stored in `finance/ledger.json` with the following structure:

```json
{
  "accounts": {
    "treasury": 720000000000,
    "user/alice": 1080,
    "user/bob": 180
  },
  "transactions": [
    {
      "tx_id": "GENESIS-MINT",
      "type": "mint",
      "timestamp": "2024-01-01T00:00:00Z",
      "from": "genesis",
      "to": "treasury",
      "amount_deg": 720000000000,
      "amount_tt": 2000000000,
      "description": "Initial mint of genesis supply"
    }
  ],
  "metadata": {
    "created_at": "2024-01-01T00:00:00Z",
    "last_updated": "2024-01-01T00:00:00Z",
    "version": "1.0",
    "total_supply_deg": 720000000000,
    "total_supply_tt": 2000000000
  }
}
```

### Account Naming Convention

- `treasury` - Main treasury account
- `user/<username>` - User accounts (e.g., `user/alice`)
- `contract/<name>` - Smart contract accounts
- `reserve/<purpose>` - Reserve accounts

## Validation Rules

### Valid Amounts

An amount is valid if it results in an integer number of deg:

```python
def is_valid_tt_amount(tt: float) -> bool:
    deg = tt * 360
    return deg.is_integer()
```

Examples:
- ✓ 1.0 TT → 360 deg
- ✓ 0.5 TT → 180 deg
- ✓ 0.25 TT → 90 deg
- ✓ 7.2 TT → 2592 deg
- ✗ 0.33 TT → 118.8 deg (not integer)
- ✗ 1.001 TT → 360.36 deg (not integer)

### Transaction Validation

All transactions must satisfy:
1. Source account exists
2. Source account has sufficient balance
3. Amount is a positive integer (in deg)
4. Amount is ≤ source account balance

## Examples

### Complete Workflow

```bash
# 1. Initialize ledger
python tools/tek_tokens.py init
# Output: ✓ Minted 2,000,000,000 TT (720,000,000,000 deg) to treasury

# 2. Check initial balance
python tools/tek_tokens.py balance
# Output: treasury: 720,000,000,000 deg = 2,000,000,000.00 TT

# 3. Transfer to user
python tools/tek_tokens.py tx --type transfer --amount 10 --tokens --from treasury --to user/alice
# Output: ✓ Transaction TX-000002 completed

# 4. Reward user for publishing
python tools/tek_tokens.py tx --type cxp_publish_reward --amount 3 --tokens --from treasury --to user/alice
# Output: ✓ Transaction TX-000003 completed

# 5. User consumes content
python tools/tek_tokens.py tx --type cxp_consume_charge --amount 2 --tokens --from user/alice --to treasury
# Output: ✓ Transaction TX-000004 completed

# 6. Check final balances
python tools/tek_tokens.py balance
# Shows updated balances for treasury and user/alice

# 7. Generate verification badge
python tools/tek_tokens.py verify
# Output: ✓ Badge generated at finance/token_badge.json
```

### Treasury Badge in README

Add to your README.md:

```markdown
![TT Balance](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Robbbo-T/ASI-T2/main/finance/token_badge.json)
```

## Configuration Files

### Tokenomics Configuration

Location: `finance/teknia.tokenomics.json`

Contains:
- Token specifications (name, symbol, supply)
- Divisibility rules (360 deg per TT)
- Pricing structure for CXP operations
- Account definitions
- Validation rules

### Ledger File

Location: `finance/ledger.json`

Contains:
- All account balances (in deg)
- Complete transaction history
- Metadata (timestamps, version, totals)

### Badge File

Location: `finance/token_badge.json`

Contains:
- Shields.io compatible badge definition
- Treasury balance
- System statistics

## Security Considerations

1. **Integer Arithmetic**: All calculations use integer deg values to avoid floating-point errors
2. **Balance Verification**: Total distributed tokens always equals genesis supply
3. **Transaction History**: Immutable transaction log for auditing
4. **Account Validation**: All transfers validate source account existence and balance

## CI/CD Integration

Optional GitHub Actions workflow for automated verification:

```yaml
# .github/workflows/tek-tokens-verify.yml
name: TT Token Verification
on: [push, pull_request]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Verify token ledger
        run: |
          python tools/tek_tokens.py balance
          python tools/tek_tokens.py verify
```

## FAQs

### Why 360 degrees?

The 360-degree system provides:
- Intuitive fractional divisions (1/2, 1/3, 1/4, 1/6, 1/8, etc.)
- Cultural significance (circle, degrees)
- Alignment with geometric and astronomical concepts

### Can I transfer fractional TT amounts?

Yes, as long as the fractional amount converts to an integer number of deg. For example:
- 0.5 TT = 180 deg ✓
- 0.25 TT = 90 deg ✓
- 0.1 TT = 36 deg ✓

### What happens if I try to transfer an invalid amount?

The CLI will reject the transaction with an error message indicating that the amount does not convert to integer deg.

### How do I add a new account?

Accounts are created automatically when they receive their first transfer. Simply send tokens to the new account name:

```bash
python tools/tek_tokens.py tx --type transfer --amount 1 --tokens --from treasury --to user/newuser
```

## Version History

- **v1.0** - Initial release
  - Genesis supply: 2B TT
  - 360-degree divisibility
  - Integer deg ledger
  - CLI tool with init, balance, tx, verify commands

## References

- [Tokenomics Configuration](../finance/teknia.tokenomics.json)
- [CLI Tool Source](../tools/tek_tokens.py)
- Main README: [README.md](../README.md)

---

*Teknia Token (TT) - 360° of Precision*
