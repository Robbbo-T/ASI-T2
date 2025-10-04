# Teknia Token CLI (`tek_tokens.py`) — v3.14

CLI for an integer `deg` ledger with exact `TT ⇄ deg`, **founder 5% at genesis**, **sustain fee tiered for transfers (π)** with **0.5% for reward/consume**, optional **Δθmin = 2592 deg** on transfers, and a **tx hash‑chain** plus **policy pin**.

**Config selection:** pass `--config path/to/tokenomics.json` or set `TEKNIA_CONFIG` environment variable.

## Features

### π-Tier Fee Schedule (v3.14)

Transfers use dynamic fees based on amount:

| Amount (TT) | Amount (deg) | Fee % | BPS | Description |
|-------------|--------------|-------|-----|-------------|
| ≥ 7,200     | ≥ 2,592,000  | 3.14% | 314 | 1000× Δθmin |
| ≥ 720       | ≥ 259,200    | 0.99% | 99  | 100× Δθmin |
| ≥ 72        | ≥ 25,920     | 0.314%| 31.4| 10× Δθmin |
| < 72        | < 25,920     | 0.5%  | 50  | Base fee |

**Reward/Consume operations always use 0.5% base fee.**

### Policy Immutability

- SHA-256 hash of policy section computed at `init`
- Stored in `ledger.json` as `policy_hash`
- `verify` command checks hash matches config
- Prevents silent policy changes

### Scope-Based Validation

- **min_transfer_deg** (7.2 TT) enforced on `transfer` only
- `reward` and `consume` have no minimum quantum
- Configurable via `min_transfer_scope` in tokenomics config

### Transaction Hash Chain

- Each tx logged to `txlog.jsonl`
- Chain: `TX_N_hash = SHA256(TX_{N-1}_hash + tx_data)`
- Head stored in `txhead.json`
- Enables efficient verification

### EUR Valuation (Optional)

Display parallel EUR values:

```bash
# Direct EUR/TT peg
python tek_tokens.py --eur-per-tt 0.10 balance

# Landauer@CMB energy pricing (EUR/kWh)
python tek_tokens.py --eur-per-kwh 0.30 quote --op transfer --tt 720
```

## Commands

### `init`
Initialize ledger with genesis supply and founder allocation.

```bash
python tek_tokens.py init
```

Creates:
- TREASURY: 1,900,000,000 TT (95%)
- FOUNDER: 100,000,000 TT (5%)
- VAULT_SUSTAIN: 0 TT (accumulates fees)

Stores policy hash for verification.

### `balance`
Show account balances.

```bash
# All accounts
python tek_tokens.py balance

# Specific account
python tek_tokens.py balance --account TREASURY
python tek_tokens.py balance --account alice

# With EUR
python tek_tokens.py --eur-per-tt 0.10 balance
```

### `transfer`
Transfer tokens between accounts.

**Fee:** π-tier based on amount  
**Min quantum:** 7.2 TT (2592 deg)

```bash
# 72 TT → 0.314% fee (81 deg)
python tek_tokens.py transfer --from TREASURY --to alice --tt 72

# 720 TT → 0.99% fee (2,566 deg)
python tek_tokens.py transfer --from TREASURY --to bob --tt 720

# 7200 TT → 3.14% fee (81,388 deg)
python tek_tokens.py transfer --from TREASURY --to charlie --tt 7200
```

### `reward`
Reward tokens from TREASURY.

**Fee:** 0.5% (base)  
**Min quantum:** None

```bash
# 1 TT reward (allowed, no minimum)
python tek_tokens.py reward --to alice --tt 1

# 72 TT reward (uses 0.5% fee, not 0.314% π-tier)
python tek_tokens.py reward --to bob --tt 72
```

### `consume`
Consume tokens to TREASURY.

**Fee:** 0.5% (base)  
**Min quantum:** None

```bash
# 2 TT consume
python tek_tokens.py consume --from alice --tt 2

# 50 TT consume
python tek_tokens.py consume --from bob --tt 50
```

### `quote`
Non-mutating fee/net estimation.

```bash
# Quote transfer (shows π-tier fee)
python tek_tokens.py quote --op transfer --tt 720
# Output:
# Amount: 259,200 deg (720.00 TT)
# Fee: 2,566 deg (7.13 TT)
# Sender pays: 261,766 deg (727.13 TT)
# Recipient gets: 259,200 deg (720.00 TT)

# Quote reward (shows 0.5% base fee)
python tek_tokens.py quote --op reward --tt 72
# Fee: 129 deg (0.36 TT)

# With EUR
python tek_tokens.py --eur-per-tt 0.10 quote --op transfer --tt 720
```

### `verify`
Verify ledger integrity.

```bash
python tek_tokens.py verify
```

Checks:
- Policy hash matches config
- Total supply = 720B deg
- No negative balances
- Transaction log integrity

### `badge`
Generate verification badge SVG.

```bash
# Default output: badges/tt-verified.svg
python tek_tokens.py badge

# Custom output
python tek_tokens.py badge --out path/to/badge.svg
```

## Configuration

### Default (Hybrid)
`finance/teknia.tokenomics.json`
- π-tier fees for transfers
- 0.5% for reward/consume
- min_transfer_deg = 2592 (transfers only)
- VAULT_SUSTAIN collects fees

### No-Fee Variant
`finance/teknia.tokenomics.nofee.json`
- No sustain fees
- No VAULT_SUSTAIN
- min_transfer_deg still enforced for transfers
- Useful for testing/internal systems

Select config:

```bash
# Environment variable
export TEKNIA_CONFIG=finance/teknia.tokenomics.nofee.json
python tek_tokens.py init

# Or CLI flag
python tek_tokens.py --config finance/teknia.tokenomics.nofee.json init
```

## Files

### Committed (Git)
- `finance/teknia.tokenomics.json` - v3.14 config (π-tiers)
- `finance/teknia.tokenomics.nofee.json` - v3.14 no-fee variant

### Not Committed (.gitignore)
- `finance/ledger.json` - Account balances and metadata
- `finance/txlog.jsonl` - Transaction log (JSONL)
- `finance/txhead.json` - Hash chain head

## Examples

### Complete Workflow

```bash
# 1. Initialize
python tek_tokens.py init

# 2. Check initial balances
python tek_tokens.py balance

# 3. Transfer with π-tier fees
python tek_tokens.py transfer --from TREASURY --to alice --tt 72
python tek_tokens.py transfer --from TREASURY --to bob --tt 720

# 4. Reward (no min quantum, 0.5% fee)
python tek_tokens.py reward --to charlie --tt 10

# 5. Consume
python tek_tokens.py consume --from alice --tt 5

# 6. Quote before large transfer
python tek_tokens.py quote --op transfer --tt 7200

# 7. Verify integrity
python tek_tokens.py verify

# 8. Generate badge
python tek_tokens.py badge
```

### With EUR Valuation

```bash
# Direct peg: 1 TT = €0.10
python tek_tokens.py --eur-per-tt 0.10 balance
python tek_tokens.py --eur-per-tt 0.10 quote --op transfer --tt 720

# Landauer@CMB: €0.30 per kWh
python tek_tokens.py --eur-per-kwh 0.30 balance
python tek_tokens.py --eur-per-kwh 0.30 quote --op transfer --tt 7200
```

## Testing

### v3.14 Test Suite

```bash
python tools/test_tek_tokens_v314.py
```

Tests:
- Initialization with policy hash
- π-tier fee calculation (0.314%, 0.99%, 3.14%)
- Reward/consume use base 0.5% fee
- Min transfer scope (transfers only)
- Quote command
- Verify command
- Badge generation
- EUR valuation
- Balance conservation

### v3.1 Legacy Tests

```bash
python tools/test_tek_tokens.py
```

Note: v3.1 tests expect old CLI structure and flat 0.5% fees. Use v3.14 tests for current system.

## Changelog

### v3.14 (Current)
- **π-tier fees**: 0.314%, 0.99%, 3.14% for transfers
- **Scope-based validation**: min_transfer_deg on transfers only
- **Policy immutability**: SHA-256 hash verification
- **New CLI**: `transfer`, `reward`, `consume`, `quote`, `badge`
- **EUR valuation**: `--eur-per-tt` and `--eur-per-kwh`
- **Hash chain**: `txlog.jsonl` + `txhead.json`
- **No-fee config**: `teknia.tokenomics.nofee.json`

### v3.1 (Legacy)
- Flat 0.5% fee for all operations
- min_transfer_deg enforced on all operations
- Old CLI: `tx --type <type>`
- No policy hash
- `ledger.log` instead of `txlog.jsonl`

## Migration from v3.1 to v3.14

If you have an existing v3.1 ledger:

1. Backup current ledger:
   ```bash
   cp finance/ledger.json finance/ledger.v31.backup.json
   cp finance/ledger.log finance/ledger.v31.backup.log
   ```

2. Re-initialize with v3.14:
   ```bash
   python tek_tokens.py init
   ```

3. Policy hash will be computed and stored automatically

4. Old transaction log (`ledger.log`) is replaced by `txlog.jsonl` and `txhead.json`

**Note:** Account balances are NOT automatically migrated. You'll need to manually replay transactions if needed.

## Support

- **Documentation**: `docs/TOKENS.md`
- **Finance README**: `finance/README.md`
- **Config examples**: `finance/teknia.tokenomics.json`, `finance/teknia.tokenomics.nofee.json`
- **Tests**: `tools/test_tek_tokens_v314.py`

---

**Teknia Token v3.14** — *π-tier hybrid tokenomics with policy immutability*
