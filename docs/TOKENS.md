# Teknia Token (TT) - Documentation v3.14

## Overview

**Teknia Token (TT)** is the native token of the ASI-T2 ecosystem with unique 360-degree divisibility, founder allocation, and π-tier sustainability mechanisms.

### Key Specifications

- **Token Name**: Teknia Token
- **Token Symbol**: TT
- **Version**: 3.14
- **Genesis Supply**: 2,000,000,000 TT (2 billion)
- **Divisibility**: 360 degrees (deg) per 1 TT
- **Total Genesis Supply**: 720,000,000,000 deg (720 billion)
- **Ledger Precision**: Integer deg units only
- **Founder Allocation**: 5% (100M TT / 36B deg) at genesis
- **Sustain Fee**: π-tier for transfers (0.314%, 0.99%, 3.14%); 0.5% for reward/consume

### Account Structure

- **TREASURY**: Main treasury (95% of genesis = 1.9B TT)
- **FOUNDER**: Founder allocation (5% of genesis = 100M TT)
- **VAULT_SUSTAIN**: Sustainability vault (accumulates fees)

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

### Minimum Transfer Quantum (Δθₘᵢn)

The token system enforces a **minimum transfer quantum** of **2592 deg (7.2 TT)** for **transfers only**:

- **min_transfer_deg**: 2592 deg = 7.2 TT
- **Scope**: Applies to `transfer` operations only (configurable)
- **Reward/Consume**: No minimum quantum restriction
- All transfers must be exact multiples of 2592 deg
- This quantum represents the minimum operational gradient for token flow
- Enforces the TFA (Thermodynamic Field Approach) correlation: Δθₘᵢn ↔ ΔTₘᵢn

**Valid Transfer Examples:**
- ✓ 2592 deg (7.2 TT) - 1x quantum
- ✓ 5184 deg (14.4 TT) - 2x quantum
- ✓ 25920 deg (72 TT) - 10x quantum

**Invalid Transfer Examples:**
- ✗ 1 deg - Not a multiple of 2592
- ✗ 360 deg (1 TT) - Not a multiple of 2592
- ✗ 36 deg (0.1 TT) - Not a multiple of 2592
- ✗ 1080 deg (3 TT) - Not a multiple of 2592

**Reward/Consume (No Restriction):**
- ✓ 360 deg (1 TT) - Any integer deg amount
- ✓ 1080 deg (3 TT) - Any integer deg amount

### Sustain Fee Mechanism (π-Tiers)

Token operations use a **tiered fee structure**:

#### For Transfers: π-Tier Schedule

| Amount (TT) | Amount (deg) | Tier BPS | Fee % | Description |
|-------------|--------------|----------|-------|-------------|
| ≥ 72        | ≥ 25,920     | 31.4     | 0.314% | 10× Δθmin |
| ≥ 720       | ≥ 259,200    | 99       | 0.99%  | 100× Δθmin |
| ≥ 7,200     | ≥ 2,592,000  | 314      | 3.14%  | 1000× Δθmin |
| < 72        | < 25,920     | 50       | 0.5%   | Base fee |

**Fee Calculation**: `(amount_deg × tier_bps) // 10000` (integer floor division)

**Examples:**
- Transfer 72 TT (25,920 deg): Fee = 81 deg (0.314%)
- Transfer 720 TT (259,200 deg): Fee = 2,566 deg (0.99%)
- Transfer 7,200 TT (2,592,000 deg): Fee = 81,388 deg (3.14%)

#### For Reward/Consume: Base Fee (0.5%)

- **Fee Rate**: 50 basis points (bps) = 0.5%
- **Fee Calculation**: `(amount_deg × 50) // 10000`
- **Example**: Reward 72 TT → Fee = 129 deg (0.5%)

**All fees go to `VAULT_SUSTAIN` account and are paid by the sender.**

### Founder Allocation

At genesis initialization:
- **5% allocation** (500 bps) to `FOUNDER` account
- Calculated as: `(720B deg × 500) ÷ 10000 = 36B deg` (100M TT)
- Remaining **95%** to `TREASURY` account: 684B deg (1.9B TT)
- Floor division ensures exact integer amounts

### Policy Immutability

v3.14 introduces **policy hash verification**:
- SHA-256 hash of policy section computed at initialization
- Stored in `ledger.json` as `policy_hash`
- `verify` command checks policy integrity
- Prevents silent policy changes

**Note**: The v3.1 pricing structure values (1080 deg, 720 deg) are **not** multiples of min_transfer_deg (2592). Use quantum-compliant amounts for actual transfers, or use `reward`/`consume` operations which don't have minimum quantum restrictions.

## CLI Tool: `tek_tokens.py` v3.14

The `tek_tokens.py` CLI tool manages the token ledger with integer deg precision, founder allocation, π-tier fees, and policy immutability.

### Installation

No installation required. The tool is located at `tools/tek_tokens.py` and uses Python 3.8+.

### Configuration

Select tokenomics configuration:

```bash
# Use default config (π-tier fees)
python tools/tek_tokens.py init

# Use no-fee config
export TEKNIA_CONFIG=finance/teknia.tokenomics.nofee.json
python tools/tek_tokens.py init

# Or use --config flag
python tools/tek_tokens.py --config finance/teknia.tokenomics.nofee.json init
```

### Commands

#### `init` - Initialize Ledger

Initialize the ledger with genesis supply and 5% founder allocation:

```bash
python tools/tek_tokens.py init
```

This creates:
- **TREASURY**: 684B deg (1.9B TT) - 95% of genesis
- **FOUNDER**: 36B deg (100M TT) - 5% allocation
- **VAULT_SUSTAIN**: 0 deg - Accumulates fees

#### `balance` - Check Balances

Show all account balances:

```bash
python tools/tek_tokens.py balance
```

Show specific account:

```bash
python tools/tek_tokens.py balance --account TREASURY
python tools/tek_tokens.py balance --account FOUNDER
python tools/tek_tokens.py balance --account alice
```

With EUR valuation:

```bash
# Direct EUR/TT peg
python tools/tek_tokens.py --eur-per-tt 0.10 balance

# Landauer@CMB energy pricing
python tools/tek_tokens.py --eur-per-kwh 0.30 balance
```

#### `transfer` - Transfer Tokens

Transfer tokens between accounts (uses π-tier fees, requires multiple of 7.2 TT):

```bash
# Transfer 7.2 TT (minimum quantum)
python tools/tek_tokens.py transfer --from TREASURY --to alice --tt 7.2

# Transfer 72 TT (0.314% fee tier)
python tools/tek_tokens.py transfer --from TREASURY --to bob --tt 72

# Transfer 720 TT (0.99% fee tier)
python tools/tek_tokens.py transfer --from TREASURY --to charlie --tt 720

# Transfer 7200 TT (3.14% fee tier)
python tools/tek_tokens.py transfer --from TREASURY --to dave --tt 7200
```

#### `reward` - Reward Tokens

Reward tokens from TREASURY (uses 0.5% base fee, no minimum quantum):

```bash
# Reward 1 TT (allowed, no minimum quantum)
python tools/tek_tokens.py reward --to alice --tt 1

# Reward 3 TT
python tools/tek_tokens.py reward --to bob --tt 3

# Reward 72 TT (uses 0.5% fee, not 0.314% π-tier)
python tools/tek_tokens.py reward --to charlie --tt 72
```

#### `consume` - Consume Tokens

Consume tokens to TREASURY (uses 0.5% base fee, no minimum quantum):

```bash
# Consume 2 TT from user
python tools/tek_tokens.py consume --from alice --tt 2

# Consume larger amount
python tools/tek_tokens.py consume --from bob --tt 50
```

#### `quote` - Fee Estimation

Get fee estimates without mutating ledger:

```bash
# Quote transfer (shows π-tier fee)
python tools/tek_tokens.py quote --op transfer --tt 720

# Quote reward (shows 0.5% base fee)
python tools/tek_tokens.py quote --op reward --tt 72

# Quote consume
python tools/tek_tokens.py quote --op consume --tt 50

# With EUR valuation
python tools/tek_tokens.py --eur-per-tt 0.10 quote --op transfer --tt 720
```

#### `verify` - Verify Ledger

Verify ledger integrity and policy hash:

```bash
python tools/tek_tokens.py verify
```

Checks:
- Policy hash matches config
- Total supply equals genesis (720B deg)
- No negative balances
- Transaction log consistency

#### `badge` - Generate Badge

Generate verification badge SVG:

```bash
# Default output: badges/tt-verified.svg
python tools/tek_tokens.py badge

# Custom output
python tools/tek_tokens.py badge --out custom/path/badge.svg
```

### Examples

```bash
# Complete workflow
python tools/tek_tokens.py init
python tools/tek_tokens.py balance
python tools/tek_tokens.py transfer --from TREASURY --to alice --tt 72
python tools/tek_tokens.py reward --to bob --tt 10
python tools/tek_tokens.py quote --op transfer --tt 7200
python tools/tek_tokens.py verify
python tools/tek_tokens.py badge
```

## Ledger Structure

The ledger is stored in `finance/ledger.json` with the following structure:

```json
{
  "version": "3.14",
  "policy_hash": "ea1a0c25ffcf7453...",
  "accounts": {
    "TREASURY": 684000000000,
    "FOUNDER": 36000000000,
    "VAULT_SUSTAIN": 12345,
    "alice": 25920,
    "bob": 3600
  },
  "transactions": [
    {
      "tx_id": "TX-000001",
      "type": "transfer",
      "timestamp": "2024-01-01T00:00:00Z",
      "from": "TREASURY",
      "to": "alice",
      "amount_deg": 25920,
      "amount_tt": 72.0,
      "fee_deg": 81,
      "fee_tt": 0.225
    }
  ],
  "metadata": {
    "created_at": "2024-01-01T00:00:00Z",
    "genesis_supply_deg": 720000000000,
    "genesis_supply_tt": 2000000000
  }
}
```

### Account Naming Convention

- `TREASURY` - Main treasury account
- `FOUNDER` - Founder allocation account
- `VAULT_SUSTAIN` - Sustainability vault
- `alice`, `bob`, `charlie` - User accounts
- `contract/<name>` - Smart contract accounts (if used)

## Validation Rules

### Valid Amounts

An amount is valid if it satisfies:
1. Results in an integer number of deg
2. For **transfers only**: Must be multiple of min_transfer_deg (2592 deg / 7.2 TT)
3. For **reward/consume**: Any positive integer deg amount

```python
def is_valid_tt_amount(tt: float) -> bool:
    deg = tt * 360
    # Must be integer deg
    if not deg.is_integer():
        return False
    # Must be multiple of min_transfer_deg
    return int(deg) % 2592 == 0
```

Examples:
- ✓ 7.2 TT → 2592 deg (1x quantum)
- ✓ 14.4 TT → 5184 deg (2x quantum)
- ✓ 72 TT → 25920 deg (10x quantum)
- ✗ 1.0 TT → 360 deg (not multiple of 2592)
- ✗ 0.5 TT → 180 deg (not multiple of 2592)
- ✗ 0.1 TT → 36 deg (not multiple of 2592)
- ✗ 0.33 TT → 118.8 deg (not integer)
- ✗ 1.001 TT → 360.36 deg (not integer)

### Transaction Validation

All transactions must satisfy:
1. Source account exists
2. Source account has sufficient balance
3. Amount is a positive integer (in deg)
4. Amount is ≤ source account balance
5. **Amount is an exact multiple of min_transfer_deg (2592 deg)**

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
- **Policy settings including min_transfer_deg (2592 deg)**
- Pricing structure for CXP operations
- Account definitions
- Validation rules

Key policy section:
```json
"policy": {
  "deg_per_tt": 360,
  "min_transfer_deg": 2592,
  "rounding": "reject-non-integer-deg",
  "validation": [
    "sum(balances) == total_supply_deg",
    "all amounts integer in deg",
    "no negative balances",
    "amount_deg % min_transfer_deg == 0"
  ]
}
```

### Ledger File

Location: `finance/ledger.json`

Contains:
- All account balances (in deg)
- Complete transaction history
- Metadata (timestamps, version, totals)

### Transaction Log File

Location: `finance/ledger.log`

Contains:
- Append-only log of all transactions
- Each line is a JSON object with transaction details
- Fields: id, timestamp, src, dst, deg, hash
- Used for auditing and traceability

Example log entry:
```json
{"id": "TX-000001", "timestamp": "2024-01-01T12:00:00Z", "src": "treasury", "dst": "user/alice", "deg": 2592, "hash": "a1b2c3d4e5f6g7h8"}
```

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
5. **Quantum Transfer Enforcement**: All transfers must be exact multiples of min_transfer_deg (2592 deg)
6. **Append-Only Logging**: Transaction log file provides cryptographic audit trail with hashes

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
