---
id: ASIT2-FINANCE-README
project: ASI-T2
artifact: Sustainable Finance Framework
llc: GOVERNANCE
classification: PUBLIC-DRAFT
version: 0.1.0
release_date: "2025-10-01"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
canonical_hash: pending
---

# ASI-T2 Finance — Sustainable Economics & Teknia Token

**Status:** Draft for technical review  
**Whitepaper Reference:** [Master Whitepaper #1, Section 4.7](../WHITEPAPERS/MASTER_WHITEPAPER_1.md#47-sustainable-anti-speculative-finance)

This directory contains both the **high-level sustainable finance framework** and the **technical implementation of Teknia Token (TT) v3.14**.

---

## Quick Links

- [Sustainable Finance Framework](#sustainable-finance-framework)
- [Teknia Token (TT) v3.14 Implementation](#teknia-token-tt-v314-implementation)
- [Related Documentation](#related-documentation-1)

---

## Sustainable Finance Framework

The ASI-T2 Sustainable Finance framework aligns economic incentives with service delivery, ethical governance, and verifiable impact, emphasizing **service-objective outcomes (SLOs)**, **operational credits**, and **quadratic funding**.

### Core Principles

#### 1. Service-Aligned Economics
* **Service Level Objectives (SLOs):** Financial rewards tied to measurable service delivery.
* **Performance-Based Allocation:** Resources flow to systems and teams meeting or exceeding SLOs.
* **Verifiable Impact:** All claims must be backed by UTCS-anchored evidence.

#### 2. Anti-Speculation Mechanisms
* **Demurrage:** Holding costs applied to idle balances to discourage hoarding.
* **Lock-ups:** Time-locked commitments for long-term stability.
* **Reserve Requirements:** Mandatory reserves to ensure system solvency.

#### 3. Operational Credits (Non-Transferable)
* Cannot be traded on secondary markets
* Expire after a defined period
* Tied to specific products/services (AMPEL360 flights, GAIA data access, etc.)

#### 4. Quadratic Funding for Public Goods
* Matching funds favor projects with broad-based community support
* Target: Public-interest R&D, safety improvements, open-source contributions
* Governance: Transparent allocation via multisig treasury and MAL-EEM policies

#### 5. Slashing for SLO Breaches
* Trigger: Failure to meet committed SLOs or violation of MAL-EEM policies
* Mechanism: Automated reduction of allocated resources
* Appeals: Dispute resolution process with evidence review

For detailed principles, see [PRINCIPLES.md](./PRINCIPLES.md).  
For sponsorship policies, see [SPONSORSHIP.md](./SPONSORSHIP.md).

---

## Teknia Token (TT) v3.14 Implementation

**Technical implementation of the token system with π-tier hybrid tokenomics.**

### Key Parameters

- **Unit of account:** `deg` (integer only)
- **Conversion:** `1 TT = 360 deg`
- **Genesis supply:** `2,000,000,000 TT = 720,000,000,000 deg`
- **Founder allocation (genesis):** **5%** to `FOUNDER` (floor in `deg`)
- **Sustain fee:** **Transfers use π‑tiers** (0.314% ≥ 72 TT; 0.99% ≥ 720 TT; 3.14% ≥ 7,200 TT).  
  `reward`/`consume` remain at **0.5%**. Sender pays; fees go to `VAULT_SUSTAIN` (floor in `deg`).
- **Δθmin (policy):** `min_transfer_deg = 2592` (7.2 TT) — applies to **transfers** only (scope configurable).
- **Treasury:** `TREASURY`

### Quick Start
```bash
# 0) (Optional) Choose config
#    - Hybrid (fees + Δθmin): default at finance/teknia.tokenomics.json
#    - No-fee variant: set TEKNIA_CONFIG=finance/teknia.tokenomics.nofee.json or use --config
#    - (Optional) EUR display: add --eur-per-tt 0.10  or  --eur-per-kwh 0.30

# 1) Initialize the ledger (creates finance/ledger.json) with 5% founder allocation
python3 tools/tek_tokens.py init

# 2) Check balances (TT/deg and optional EUR)
python3 tools/tek_tokens.py balance --account TREASURY
python3 tools/tek_tokens.py balance --account FOUNDER
python3 tools/tek_tokens.py balance --account VAULT_SUSTAIN

# 3) Transfer 7.2 TT (2592 deg) from treasury to Alice
# Fee (base tier for < 72 TT) = floor(2592 * 0.005) = 12 deg → VAULT_SUSTAIN
# Alice receives net = 2592 - 12 = 2580 deg
python3 tools/tek_tokens.py transfer --from TREASURY --to alice --tt 7.2

# 4) Reward: 3 TT to creator (sustain fee applies to TREASURY at 0.5%)
python3 tools/tek_tokens.py reward --to creator --tt 3

# 5) Consume: charge 2 TT from creator (sustain fee applies to creator at 0.5%)
python3 tools/tek_tokens.py consume --from creator --tt 2

# 6) Verify ledger invariants + policy hash + tx hash-chain
python3 tools/tek_tokens.py verify

# 7) Quote (no mutation): fee/net (TT/deg and optional EUR)
python3 tools/tek_tokens.py quote --op transfer --tt 72

# 8) Generate verification badge SVG
python3 tools/tek_tokens.py badge --out badges/tt-verified.svg
```

## π-Tier Fee Schedule (Transfers Only)

| Amount (TT) | Amount (deg) | Tier BPS | Fee % | Description |
|-------------|--------------|----------|-------|-------------|
| ≥ 72        | ≥ 25,920     | 31.4     | 0.314% | 10× Δθmin |
| ≥ 720       | ≥ 259,200    | 99       | 0.99%  | 100× Δθmin |
| ≥ 7,200     | ≥ 2,592,000  | 314      | 3.14%  | 1000× Δθmin |
| < 72        | < 25,920     | 50       | 0.5%   | Base fee |

**Note:** `reward` and `consume` operations always use the base 0.5% fee, regardless of amount.

## Commands

### `init`
Initialize ledger with genesis supply and 5% founder allocation. Stores policy hash for immutability verification.

### `balance [--account <name>]`
Show account balances. Omit `--account` to show all accounts.

### `transfer --from <source> --to <dest> --tt <amount>`
Transfer tokens between accounts. Uses π-tier fees. Requires amount to be multiple of 7.2 TT (2592 deg).

### `reward --to <recipient> --tt <amount>`
Reward tokens from TREASURY. Uses 0.5% base fee. No minimum quantum restriction.

### `consume --from <source> --tt <amount>`
Consume tokens to TREASURY. Uses 0.5% base fee. No minimum quantum restriction.

### `quote --op <transfer|reward|consume> --tt <amount>`
Non-mutating estimate of fees and net amounts. Useful for planning transactions.

### `verify`
Verify ledger integrity:
- Policy hash matches config
- Total supply equals genesis (720B deg)
- No negative balances
- Transaction log consistency

### `badge [--out <file>]`
Generate verification badge SVG showing treasury balance.

## Configuration

### Default Config (finance/teknia.tokenomics.json)
- π-tier fees for transfers
- 0.5% fee for reward/consume
- Δθmin = 2592 deg (7.2 TT) for transfers
- VAULT_SUSTAIN collects fees

### No-Fee Config (finance/teknia.tokenomics.nofee.json)
- No sustain fees
- No VAULT_SUSTAIN
- Δθmin still enforced for transfers
- Useful for testing or internal systems

Select config via:
```bash
# Environment variable
export TEKNIA_CONFIG=finance/teknia.tokenomics.nofee.json
python3 tools/tek_tokens.py init

# Or CLI flag
python3 tools/tek_tokens.py --config finance/teknia.tokenomics.nofee.json init
```

## EUR Valuation (Optional)

Display parallel EUR values in output:

```bash
# Direct EUR per TT peg
python3 tools/tek_tokens.py --eur-per-tt 0.10 balance

# Landauer@CMB energy pricing (EUR per kWh)
python3 tools/tek_tokens.py --eur-per-kwh 0.30 quote --op transfer --tt 720
```

## Files

- **teknia.tokenomics.json** - v3.14 config with π-tiers (committed)
- **teknia.tokenomics.nofee.json** - v3.14 no-fee variant (committed)
- **ledger.json** - Current account balances and metadata (not committed)
- **txlog.jsonl** - Append-only transaction log with hash chain (not committed)
- **txhead.json** - Latest transaction hash for chain verification (not committed)

## Policy Immutability

At initialization, a SHA-256 hash of the policy section is computed and stored in `ledger.json`. The `verify` command checks that the current config policy hash matches the stored hash, preventing silent policy changes.

## Transaction Hash Chain

Each transaction is logged to `txlog.jsonl` and linked via hash chain:
```
TX_N_hash = SHA256(TX_{N-1}_hash + tx_id + timestamp + from + to + amount)
```

The chain head is stored in `txhead.json` for efficient verification.

---

**Version:** 3.14 (π-tier hybrid tokenomics)  
**Previous:** 3.1 (flat 0.5% fee)

---

## Related Documentation

### Within This Directory
* [PRINCIPLES.md](./PRINCIPLES.md) - Detailed economic principles and mechanisms
* [SPONSORSHIP.md](./SPONSORSHIP.md) - Sponsorship and funding policy (IDEALE-EU, MAL-EEM)
* [teknia.tokenomics.json](./teknia.tokenomics.json) - v3.14 config with π-tiers
* [teknia.tokenomics.nofee.json](./teknia.tokenomics.nofee.json) - v3.14 no-fee variant

### External References
* [Master Whitepaper #1](../WHITEPAPERS/MASTER_WHITEPAPER_1.md) - Architecture overview
* [Token Documentation](../docs/TOKENS.md) - Comprehensive token guide
* [Token CLI Tool](../tools/tek_tokens.py) - Command-line interface
* [Token Tests](../tools/test_tek_tokens_v314.py) - Test suite

---

## Files in This Directory

- **README.md** - This file (framework + implementation overview)
- **PRINCIPLES.md** - Detailed economic principles (demurrage, lock-ups, slashing, treasury governance)
- **SPONSORSHIP.md** - Sponsorship and funding policy
- **teknia.tokenomics.json** - v3.14 config with π-tiers (committed)
- **teknia.tokenomics.nofee.json** - v3.14 no-fee variant (committed)
- **ledger.json** - Current account balances and metadata (generated, not committed)
- **txlog.jsonl** - Append-only transaction log with hash chain (generated, not committed)
- **txhead.json** - Latest transaction hash for chain verification (generated, not committed)

---

*Last Updated: 2025-10-01*  
*Version: 0.1.0*  
*Framework Status: Draft for technical review*  
*Implementation: v3.14 (π-tier hybrid tokenomics)*

