# TeknIA TOKENS (TT) · Rules

## Objectives
- Incentivize knowledge exchange (CXP) with a repo budget (TT).
- Track costs/rewards in a verifiable append-only ledger.

## Roles
- **treasury**: repository budget holder
- **user/<github-username>**: individual contributors
- **sink:<event>**: absorbs costs (e.g., sink:consume)
- **domain/<DDD>**: domain-specific accounts (future)

## Economics

### Events & Pricing
- **CXP Publish** → *reward* +`prices.cxp_publish_reward` TT to `user/<actor>` (from treasury) **if** `auto.reward_on_publish = true`.
- **CXP Consume** → *charge* −`prices.cxp_consume_cost` TT from `treasury` to `sink:consume` **if** `auto.charge_on_consume = true`.

### Current Configuration
See [finance/teknia.tokenomics.json](../finance/teknia.tokenomics.json):
- Initial mint: 10,000 TT to treasury
- Publish reward: 3 TT
- Consume cost: 2 TT
- Auto rewards/charges: Configurable via `auto.*` flags

## Decision Points

### 1. Reward on Publish?
**Question**: Should we reward contributors for publishing context?

**Options**:
- **Yes** → Set `auto.reward_on_publish=true` (default)
  - Incentivizes documentation and context sharing
  - Credits come from treasury
- **No** → Set to false
  - Preserves treasury for other uses
  - Reduces automatic transactions

### 2. Who pays for Consume?
**Question**: Who should bear the cost of consuming external context?

**Current (M0)**: Treasury pays (repo-level cost)

**Future Options**:
- **User-level**: Requester pays from personal account
- **Domain-level**: Consuming domain pays from domain budget
- **Mixed**: Treasury subsidizes, user/domain covers remainder

To implement: Modify `cmd_auto()` in `tek_tokens.py` to debit from specified account.

### 3. Domain allocation
**Question**: How to distribute TT across domains?

**Current (M0)**: Equal allocation declared, not yet initialized

**Implementation Options**:
1. **Equal split**: `10000 / 15 domains ≈ 667 TT` each
2. **Activity-based**: Allocate based on contribution history
3. **Project-based**: Allocate per active projects/priorities

To implement: Run manual `TRANSFER` transactions from treasury to `domain/<DDD>`.

## Operations

### Initialize Ledger
```bash
python tools/tek_tokens.py init
```

Creates genesis transaction: MINT 10,000 TT to treasury.

### Check Balance
```bash
python tools/tek_tokens.py balance
```

Shows current balances for all holders.

### Manual Transaction
```bash
python tools/tek_tokens.py tx \
  --type transfer \
  --amount 10 \
  --from treasury \
  --to user/amedeo.pelliccia \
  --memo "manual reward for documentation"
```

### Automatic CXP Events
Triggered by GitHub Actions workflows:
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

### Verify Ledger Integrity
```bash
python tools/tek_tokens.py verify
```

Validates:
- Chain continuity (prev links)
- Hash integrity
- Generates balance badge (if enabled)

## Ledger Structure

### Location
`finance/ledger/tt-ledger.jsonl` (JSON Lines format)

### Transaction Schema
```json
{
  "id": "ttx_000001",
  "ts": "2025-10-04T12:00:00Z",
  "prev": "genesis",
  "type": "MINT|BURN|DEBIT|CREDIT|TRANSFER",
  "from": "mint|treasury|user/<username>|domain/<DDD>",
  "to": "treasury|user/<username>|domain/<DDD>|sink:<event>",
  "amount": 10.000,
  "unit": "TT",
  "ref": {"event": "...", "run_id": 0, "pr": 0},
  "memo": "human-readable description",
  "hash": "sha256(...)"
}
```

### Append-Only Rules
- No in-place edits allowed
- Corrections via compensating transactions
- Every record includes `prev` (previous id) and content `hash`
- Forms verifiable chain from genesis

## Security

### Chain Integrity
- Each transaction references previous via `prev` field
- Content hash (`hash` field) prevents tampering
- `verify` command checks full chain

### Access Control
- Ledger modifications only via PR + code review
- CI automatically appends for CXP events
- Manual transactions require maintainer approval

### Audit Trail
- All transactions timestamped (UTC)
- Event references (run_id, PR number) provide context
- Git history provides additional provenance

## Badge

### Configuration
See `badges` section in [finance/teknia.tokenomics.json](../finance/teknia.tokenomics.json).

### Endpoint
`finance/badges/tt-balance.json` follows Shields.io endpoint schema:
```json
{
  "schemaVersion": 1,
  "label": "TeknIA TT",
  "message": "10000.000 TT",
  "color": "blue"
}
```

### Display
Add to README:
```markdown
![TeknIA TT](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Robbbo-T/ASI-T2/main/finance/badges/tt-balance.json)
```

## Future Enhancements

### Roadmap
1. **Label-driven rewards**: Workflow reading `tt:reward-<n>` labels on PRs
2. **Signatures**: Add `sig` field for GPG/OIDC job signatures
3. **Domain accounts**: Split treasury into domain budgets
4. **Folder-based tracking**: Auto-attribute costs based on changed files
5. **Exchange rates**: Convert TT to other metrics (lines of code, test coverage)

### Contributing
See [GOVERNANCE.md](../governance/GOVERNANCE.md) for tokenomics change proposals.

## See Also
- [INTERFACES.md](./INTERFACES.md) - CXP specifications
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [GOVERNANCE.md](../governance/GOVERNANCE.md) - Governance model
