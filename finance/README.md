# Finance - Teknia Token System v3.1

**Enterprise-Grade Token System with Mathematical Precision**

This directory contains the Teknia Token (TT) configuration and ledger files with founder allocation, sustain fees, and quantum transfer enforcement.

## Core Specifications

- **Genesis Supply**: 2,000,000,000 TT (720,000,000,000 deg)
- **Divisibility**: 360 degrees (deg) per TT
- **Founder Allocation**: 5% (100M TT) to `FOUNDER` at genesis
- **Sustain Fee**: 0.5% per operation to `VAULT_SUSTAIN` (from sender)
- **Minimum Quantum**: 2592 deg (7.2 TT) per transfer
- **Ledger Precision**: Integer deg units only

## Files

- **teknia.tokenomics.json** - Token economics configuration v3.1 (committed to git)
- **ledger.json** - Current token ledger with all accounts and transactions (not committed)
- **ledger.log** - Append-only transaction log with cryptographic hashes (not committed)
- **token_badge.json** - Generated badge for shields.io (not committed)

## Quick Start

### Initialize the Ledger (First Time Only)

```bash
python tools/tek_tokens.py init
```

This creates `ledger.json` with three accounts:
- **TREASURY**: 1,900,000,000 TT (684B deg) - 95% of genesis
- **FOUNDER**: 100,000,000 TT (36B deg) - 5% founder allocation
- **VAULT_SUSTAIN**: 0 TT (0 deg) - Accumulates 0.5% fees

### Check Balances

```bash
# Show all accounts
python tools/tek_tokens.py balance

# Show specific account
python tools/tek_tokens.py balance TREASURY
python tools/tek_tokens.py balance FOUNDER
```

### Make Transfers

**Important**: All transfers must be multiples of 2592 deg (7.2 TT) and include a 0.5% sustain fee.

```bash
# Valid: 7.2 TT = 2592 deg (1x quantum)
python tools/tek_tokens.py tx --type transfer --amount 7.2 --tokens \
  --from TREASURY --to user/alice
# Sender pays: 2604 deg (2592 + 12 fee)
# Recipient gets: 2592 deg
# Vault gets: 12 deg

# Valid: 14.4 TT = 5184 deg (2x quantum)
python tools/tek_tokens.py tx --type transfer --amount 14.4 --tokens \
  --from TREASURY --to user/bob

# Invalid: 1 TT = 360 deg (not a multiple of 2592)
python tools/tek_tokens.py tx --type transfer --amount 1 --tokens \
  --from TREASURY --to user/charlie
# ERROR: Not a multiple of min_transfer_deg
```

### View Transaction Log

```bash
cat finance/ledger.log
# One JSON object per line with full transaction details
```

### Generate Badge

```bash
python tools/tek_tokens.py verify
```

## Account Structure

### Genesis Accounts (Created at Init)

1. **TREASURY** - 684,000,000,000 deg (1,900,000,000 TT)
   - Main operational treasury
   - 95% of genesis supply
   - Source for most transfers

2. **FOUNDER** - 36,000,000,000 deg (100,000,000 TT)
   - Founder allocation (5% of genesis)
   - Fixed at initialization
   - No vesting schedule

3. **VAULT_SUSTAIN** - 0 deg initially
   - Sustainability vault
   - Accumulates 0.5% of all transfer amounts
   - Grows with system usage

### User Accounts (Created on First Transfer)

- **user/\<username\>** - Individual user accounts
- **contract/\<name\>** - Smart contract accounts
- **reserve/\<purpose\>** - Reserve accounts

## Enhanced Features v3.1

### 1. Founder Allocation (5%)

Automatically allocated during initialization:
- **Amount**: 36,000,000,000 deg (100,000,000 TT)
- **Calculation**: `(720B × 500) // 10000`
- **Account**: `FOUNDER`
- **Purpose**: Long-term alignment and sustainability

### 2. Sustain Fee (0.5%)

Applied to every transfer operation:
- **Rate**: 50 basis points = 0.5%
- **Calculation**: `(amount_deg × 50) // 10000` (floored)
- **Paid by**: Sender (additional to transfer amount)
- **Destination**: `VAULT_SUSTAIN` account

**Examples:**
```
Transfer 2,592 deg → Fee: 12 deg
Transfer 5,184 deg → Fee: 25 deg
Transfer 25,920 deg → Fee: 129 deg
```

### 3. Quantum Transfer (Δθₘᵢn)

All transfers must be multiples of the minimum quantum:
- **Quantum**: 2592 deg = 7.2 TT
- **Valid**: 2592, 5184, 7776, 10368, ... deg
- **Invalid**: 1, 360, 1080, 1800, ... deg
- **Physical basis**: Landauer@CMB thermodynamic framework

### 4. Transaction Logging

Complete audit trail in `ledger.log`:
- **Format**: JSON lines (one per transaction)
- **Fields**: `{id, timestamp, src, dst, deg, hash}`
- **Hash**: SHA-256 (16 chars)
- **Append-only**: Immutable history

### 5. Physics Integration

Aligned with TFA V2 Landauer@CMB model:
- **T_CMB**: 2.7255 K
- **k_B**: 1.380649 × 10⁻²³ J/K
- **Energy mapping**: Discrete quantum correlation
- **ΔTₘᵢn ↔ Δθₘᵢn**: Thermodynamic-informational duality

## Validation Rules

All operations validate:
1. ✓ Integer arithmetic (no floating-point)
2. ✓ Quantum compliance (`amount % 2592 == 0`)
3. ✓ Balance sufficiency (including fee)
4. ✓ Total supply conservation (720B deg)
5. ✓ Non-negative balances
6. ✓ Account existence
7. ✓ Fee calculation correctness

## Testing

Run comprehensive test suite:
```bash
python tools/test_tek_tokens.py
# 30+ tests, 100% pass rate
```

## Documentation

- **Complete Guide**: [docs/TOKENS.md](../docs/TOKENS.md)
- **CLI Tool**: `tools/tek_tokens.py`
- **Test Suite**: `tools/test_tek_tokens.py`

## Version History

- **v3.1.0** - Founder allocation, sustain fees, enhanced validation
- **v1.0.0** - Initial release with quantum validation

## Notes

- `ledger.json`, `ledger.log`, and `token_badge.json` are excluded from git via `.gitignore`
- All amounts are stored as integer deg values
- The CLI handles TT ↔ deg conversion automatically
- Sustain fees are always floored (integer division)
- Use `TREASURY` (uppercase) for the treasury account in v3.1

---

**Teknia Token v3.1** - *Mathematical Precision Meets Physical Reality*

