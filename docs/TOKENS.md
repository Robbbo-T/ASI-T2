# Teknia Token (TT) — Rules & Spec v3.14

**Teknia Token (TT)** is the native accounting unit for IDEALE/ASI-T2 interactions.  
It supports verifiable incentives for knowledge exchange and a deterministic, integer-only ledger.

---

## Objectives

- Incentivize **Context eXchange Profile (CXP)** publishing and consumption with a repo-scoped budget (TT).
- Track costs/rewards in a verifiable **append-only** ledger with cryptographic integrity.

---

## Roles & Accounts

**Human & org roles**
- `treasury` — repository budget holder
- `user/<github-username>` — individual contributors
- `domain/<DDD>` — domain budgets (e.g., `domain/AAA`) *(future/optional)*
- `sink:<event>` — cost sinks (e.g., `sink:consume`)

**System accounts**
- `TREASURY` — main treasury (receives genesis minus founder allocation)
- `FOUNDER` — founder allocation
- `VAULT_SUSTAIN` — accumulates sustainability fees

> You can use either the lowercase “Rules” style (e.g., `treasury`) in docs or the uppercase system accounts in the CLI; both map cleanly in the tooling.

---

## Token Specifications (v3.14)

- **Symbol**: TT  
- **Genesis Supply**: **2,000,000,000 TT**  
- **Divisibility**: `1 TT = 360 deg` (integer **deg** only; no fractions)  
- **Founder Allocation**: **5%** (100M TT / 36B deg) at genesis  
- **Treasury at Genesis**: **95%** (1.9B TT / 684B deg)  
- **Minimum Transfer Quantum**: **2,592 deg** (**7.2 TT**) — **transfers only**  
- **Sustain Fees**: π-tier schedule on transfers; base 0.5% on reward/consume  
- **Policy Immutability**: SHA-256 of policy stored in ledger and checked by `verify`

### Divisibility & Precision

All arithmetic uses **integer deg**:
```

1 TT = 360 deg
0.5 TT = 180 deg  ✓
0.25 TT = 90 deg  ✓
0.01 TT = 3.6 deg ✗ (not integer → invalid)

````

### Minimum Transfer Quantum (Δθmin)

- **min_transfer_deg** = **2,592 deg** = **7.2 TT**  
- Applies to **transfer** only (configurable).  
- **reward/consume** have **no quantum restriction** (still integer deg).

Valid transfer examples:
- ✓ 2,592 deg (7.2 TT)
- ✓ 25,920 deg (72 TT)
- ✗ 360 deg (1 TT) — not a multiple of 2,592

### Sustain Fee Mechanism (π-tiers for transfers)

| Amount (TT) | Amount (deg) | Tier BPS | Fee %  | Notes                |
|-------------|---------------|----------|--------|----------------------|
| ≥ 7,200     | ≥ 2,592,000   | 314      | 3.14%  | 1000× Δθmin          |
| ≥ 720       | ≥ 259,200     | 99       | 0.99%  | 100× Δθmin           |
| ≥ 72        | ≥ 25,920      | 31.4     | 0.314% | 10× Δθmin            |
| < 72        | < 25,920      | 50       | 0.5%   | Base transfer tier   |

**Fee calculation**: `(amount_deg × tier_bps) // 10000` (integer floor division)  
**Reward/Consume fee**: fixed **0.5%** (`50 bps`) → `(amount_deg × 50) // 10000`  
**Fee sink**: all fees credit **`VAULT_SUSTAIN`** and are **paid by sender**.

---

## Economics: Events & Pricing (CXP)

Automatable pricing hooks aligned to repo workflows:

- **CXP Publish** → *reward* `+ prices.cxp_publish_reward` TT to `user/<actor>` (from `treasury`) **iff** `auto.reward_on_publish = true`.
- **CXP Consume** → *charge* `− prices.cxp_consume_cost` TT from `treasury` to `sink:consume` **iff** `auto.charge_on_consume = true`.

See configuration in `finance/teknia.tokenomics.json` (or `teknia.tokenomics.nofee.json`).

---

## Configuration Files

- **Tokenomics**: `finance/teknia.tokenomics.json`  
  - `deg_per_tt: 360`
  - `min_transfer_deg: 2592`
  - `sustain_fee_tiers` as above
  - policy hashing & validation rules

- **Ledger (balances + tx + policy hash)**: `finance/ledger.json`
- **Transaction log (append-only)**: `finance/txlog.jsonl`
- **Head pointer**: `finance/txhead.json`
- **Badge output (example)**: `badges/tt-verified.svg` *(via CLI)*

---

## CLI — `tools/tek_tokens.py` (v3.14)

> Python 3.8+. Integer-only arithmetic in **deg**, policy hashing, π-tier fees, min transfer quantum.

### Init

```bash
# default config (π-tier fees)
python tools/tek_tokens.py init

# use alternate config (no-fee)
python tools/tek_tokens.py --config finance/teknia.tokenomics.nofee.json init
````

Creates:

* `TREASURY`: 684,000,000,000 deg (1.9B TT)
* `FOUNDER`: 36,000,000,000 deg (100M TT)
* `VAULT_SUSTAIN`: 0 deg

### Balances

```bash
python tools/tek_tokens.py balance
python tools/tek_tokens.py balance --account TREASURY
python tools/tek_tokens.py --eur-per-tt 0.10 balance
```

### Transfers (π-tiers, **must** be multiple of 7.2 TT)

```bash
python tools/tek_tokens.py transfer --from TREASURY --to alice --tt 7.2
python tools/tek_tokens.py transfer --from TREASURY --to bob   --tt 72
```

### Rewards & Consume (base 0.5% fee, **no** min quantum)

```bash
python tools/tek_tokens.py reward  --to alice       --tt 3
python tools/tek_tokens.py consume --from user/bob  --tt 2
```

### Quotes (no mutation)

```bash
python tools/tek_tokens.py quote --op transfer --tt 720
python tools/tek_tokens.py quote --op reward   --tt 72
```

### Verify & Badge

```bash
python tools/tek_tokens.py verify
python tools/tek_tokens.py badge --out badges/tt-verified.svg
```

---

## Automation Hooks (CXP)

Typical GitHub Actions integration:

```bash
# On CXP Publish
python tools/tek_tokens.py auto \
  --event cxp-publish \
  --actor github_username \
  --run-id 12345

# On CXP Consume
python tools/tek_tokens.py auto \
  --event cxp-consume \
  --actor github_username \
  --run-id 12346
```

Toggle behavior via `auto.*` flags in tokenomics config.

---

## Validation Rules

1. Amounts must resolve to **integer deg**.
2. **Transfer** amounts must be **multiples of 2,592 deg** (7.2 TT).
3. Source account must exist and have sufficient balance.
4. No negative balances; sum of balances equals **genesis supply deg**.
5. `verify` checks policy hash, chain consistency, and supply invariants.

Example check function (conceptual):

```python
def is_valid_transfer_deg(amount_deg: int) -> bool:
    return amount_deg > 0 and (amount_deg % 2592 == 0)
```

---

## Ledger Model

* **Format**: `finance/ledger.json` (balances + policy + metadata), `finance/txlog.jsonl` (append-only tx), `finance/txhead.json` (chain head).
* **Immutability**: each tx links prior hash; `verify` recomputes and checks chain & policy hash.
* **Corrections**: via compensating transactions only (no in-place edits).

**Illustrative transaction entry**:

```json
{
  "tx_id": "TX-000123",
  "type": "transfer",
  "timestamp": "2025-10-04T12:00:00Z",
  "from": "TREASURY",
  "to": "alice",
  "amount_deg": 25920,
  "fee_deg": 81,
  "policy_hash": "sha256:...",
  "prev": "TX-000122",
  "hash": "sha256:..."
}
```

---

## Domain Allocation (Optional)

Initial ideas for distributing TT from treasury:

1. **Equal split** across domains (`AAA..PPP`)
2. **Activity-based** by contribution metrics
3. **Project-based** by portfolio priorities

> Implement with `TRANSFER` transactions from `TREASURY` to `domain/<DDD>`.

---

## Security & Governance

* **Append-only** ledger with hash chaining
* **Policy immutability** via stored SHA-256
* **PR-gated** changes; CI verifies `balance` + `verify`
* **Exportable** badges and reports for transparency

---

## Badge Endpoint (Shields)

(Optional) Shields endpoint JSON:

```json
{
  "schemaVersion": 1,
  "label": "Teknia TT",
  "message": "10000 TT",
  "color": "blue"
}
```

Embed in README:

```markdown
![Teknia TT](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<org>/<repo>/main/finance/badges/tt-balance.json)
```

---

## Roadmap

1. **Label-driven rewards** (`tt:reward-<n>` on PRs)
2. **Signatures** for tx (GPG/OIDC job claims)
3. **Domain budgets** with scheduled top-ups
4. **Folder-based attribution** of costs/rewards
5. **Quoting in EUR** via energy/price models

---

## See Also

* Tokenomics config — `finance/teknia.tokenomics.json`
* Optional no-fee config — `finance/teknia.tokenomics.nofee.json`
* CLI — `tools/tek_tokens.py`
* Repo README — `README.md`

```

