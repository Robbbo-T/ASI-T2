#!/usr/bin/env python3
"""
Teknia Token (TT) CLI - Token Management System v3.14

- Integer-only ledger in 'deg' (1 TT = 360 deg)
- Founder allocation at genesis (bps)
- π-tier fees for transfers; 0.5% base for reward/consume
- Minimum transfer quantum: 2,592 deg (7.2 TT) for transfers
- Structured ledger JSON + append-only txlog + hash head
- CXP automation: auto reward on publish / charge on consume

Usage:
    python tools/tek_tokens.py init
    python tools/tek_tokens.py balance [--account <acct>] [--eur-per-tt X] [--eur-per-kwh Y]
    python tools/tek_tokens.py transfer --from <acct> --to <acct> --tt <amount>
    python tools/tek_tokens.py reward   --to <acct> --tt <amount>
    python tools/tek_tokens.py consume  --from <acct> --tt <amount>
    python tools/tek_tokens.py quote --op transfer|reward|consume --tt <amount>
    python tools/tek_tokens.py verify
    python tools/tek_tokens.py badge [--out badges/tt-verified.svg]
    python tools/tek_tokens.py auto --event cxp-publish|cxp-consume --actor <gh_user> [--run-id N] [--pr N]

Config:
    - Default: finance/teknia.tokenomics.json
    - Override with --config or TEKNIA_CONFIG env
"""

import argparse
import json
import os
import sys
import hashlib
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
from typing import Optional, Dict, Tuple

# ---------- Paths & Config ----------

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = "finance/teknia.tokenomics.json"
TXLOG = REPO_ROOT / "finance" / "txlog.jsonl"
TXHEAD = REPO_ROOT / "finance" / "txhead.json"

class LedgerError(Exception): ...
class AmountError(Exception): ...

def get_config_path():
    cfg_env = os.environ.get("TEKNIA_CONFIG", DEFAULT_CONFIG)
    return REPO_ROOT / cfg_env

def load_config() -> dict:
    cfg_path = get_config_path()
    if not cfg_path.exists():
        raise LedgerError(f"Config not found at {cfg_path}")
    with cfg_path.open(encoding="utf-8") as f:
        return json.load(f)

def ledger_path(cfg: dict) -> Path:
    return REPO_ROOT / cfg["token"]["ledger_file"]

def load_ledger(cfg: dict) -> dict:
    lp = ledger_path(cfg)
    if not lp.exists():
        raise LedgerError(f"Ledger not found: {lp}. Run 'init' first.")
    with lp.open(encoding="utf-8") as f:
        return json.load(f)

def save_ledger(cfg: dict, data: dict) -> None:
    lp = ledger_path(cfg)
    lp.parent.mkdir(parents=True, exist_ok=True)
    tmp = lp.with_suffix(".json.tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
    tmp.replace(lp)

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def compute_policy_hash(cfg: dict) -> str:
    policy = cfg.get("policy", {})
    policy_json = json.dumps(policy, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(policy_json.encode()).hexdigest()

# ---------- Unit Conversion & Fees ----------

def tt_to_deg_exact(tt_str: str, deg_per_tt: int) -> int:
    try:
        frac = Fraction(tt_str)
    except Exception as e:
        raise AmountError(f"Invalid TT amount: {tt_str}") from e
    deg = frac * deg_per_tt
    if deg.denominator != 1:
        raise AmountError(f"{tt_str} TT does not map to integer deg at {deg_per_tt}/TT")
    if deg.numerator <= 0:
        raise AmountError("Amount must be positive")
    return int(deg.numerator)

def deg_to_tt(deg: int, deg_per_tt: int) -> float:
    return deg / deg_per_tt

def compute_sustain_fee(cfg: dict, op: str, amount_deg: int) -> int:
    policy = cfg.get("policy", {})
    base_bps = policy.get("sustain_fee_bps", 50)  # 0.5%
    tiers = policy.get("sustain_fee_tiers", {})
    tier_scope = tiers.get("scope", [])
    schedule = tiers.get("schedule", [])

    if op in tier_scope and schedule:
        # Highest qualifying tier first
        sorted_sched = sorted(schedule, key=lambda t: t["min_deg"], reverse=True)
        for tier in sorted_sched:
            if amount_deg >= int(tier["min_deg"]):
                bps = Fraction(str(tier["bps"]))  # accept "31.4" style
                return int((amount_deg * bps) // 10000)
    # Fallback / reward / consume
    return (amount_deg * base_bps) // 10000

def validate_min_transfer(cfg: dict, op: str, amount_deg: int) -> None:
    policy = cfg.get("policy", {})
    min_deg = int(policy.get("min_transfer_deg", 2592))
    scope = policy.get("min_transfer_scope", ["transfer"])
    if op in scope and amount_deg % min_deg != 0:
        dpt = cfg["token"]["deg_per_tt"]
        raise AmountError(
            f"Amount {amount_deg} deg ({deg_to_tt(amount_deg, dpt):.2f} TT) "
            f"is not a multiple of min_transfer_deg {min_deg} deg "
            f"({deg_to_tt(min_deg, dpt):.2f} TT)"
        )

# ---------- EUR Valuation (optional) ----------

def format_eur(cfg: dict, deg: int, eur_per_tt: Optional[float], eur_per_kwh: Optional[float]) -> str:
    if eur_per_tt is None and eur_per_kwh is None:
        return ""
    dpt = cfg["token"]["deg_per_tt"]
    if eur_per_tt is not None:
        return f" (≈ €{deg_to_tt(deg, dpt) * eur_per_tt:.4f})"
    # Landauer@CMB model
    phys = cfg.get("physics", {})
    T = phys.get("T_CMB_K", 2.7255)
    kB = phys.get("k_B_J_per_K", 1.380649e-23)
    ln2 = phys.get("ln2", 0.6931471805599453)
    E_bit = kB * T * ln2
    energy_kwh = (deg * E_bit) / 3.6e6
    return f" (≈ €{energy_kwh * float(eur_per_kwh):.6f})"

# ---------- Transaction Recording ----------

def log_tx(tx: dict) -> None:
    TXLOG.parent.mkdir(parents=True, exist_ok=True)
    with TXLOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(tx, separators=(",", ":")) + "\n")

    prev_hash = ""
    if TXHEAD.exists():
        with TXHEAD.open(encoding="utf-8") as f:
            head = json.load(f)
            prev_hash = head.get("hash", "")
    data = f"{prev_hash}:{tx['tx_id']}:{tx['timestamp']}:{tx['from']}:{tx['to']}:{tx['amount_deg']}"
    tx_hash = hashlib.sha256(data.encode()).hexdigest()
    with TXHEAD.open("w", encoding="utf-8") as f:
        json.dump({"tx_id": tx["tx_id"], "hash": tx_hash, "prev_hash": prev_hash, "timestamp": tx["timestamp"]}, f, indent=2)

# ---------- Core Ops ----------

def ensure_account(ledger: dict, acct: str) -> None:
    if acct not in ledger["accounts"]:
        ledger["accounts"][acct] = 0

def execute_operation(cfg: dict, ledger: dict, op: str, from_acct: str, to_acct: str,
                      amount_deg: int, eur_per_tt=None, eur_per_kwh=None) -> None:
    dpt = cfg["token"]["deg_per_tt"]
    sustain_vault = cfg["token"].get("sustain_vault")

    validate_min_transfer(cfg, op, amount_deg)
    fee_deg = compute_sustain_fee(cfg, op, amount_deg)
    total_deduct = amount_deg + fee_deg

    if ledger["accounts"].get(from_acct, 0) < total_deduct:
        raise LedgerError(
            f"Insufficient balance in {from_acct}: has {ledger['accounts'].get(from_acct,0)} deg, "
            f"needs {total_deduct} deg ({amount_deg}+{fee_deg} fee)"
        )

    ensure_account(ledger, to_acct)
    if sustain_vault:
        ensure_account(ledger, sustain_vault)

    ledger["accounts"][from_acct] -= total_deduct
    ledger["accounts"][to_acct] += amount_deg
    if sustain_vault and fee_deg > 0:
        ledger["accounts"][sustain_vault] += fee_deg

    tx_id = f"TX-{len(ledger.get('transactions', [])) + 1:06d}"
    tx = {
        "tx_id": tx_id,
        "type": op,
        "timestamp": now_iso(),
        "from": from_acct,
        "to": to_acct,
        "amount_deg": amount_deg,
        "amount_tt": deg_to_tt(amount_deg, dpt),
        "fee_deg": fee_deg,
        "fee_tt": deg_to_tt(fee_deg, dpt)
    }
    ledger.setdefault("transactions", []).append(tx)
    log_tx(tx)
    save_ledger(cfg, ledger)

    print(f"✓ {tx_id} completed ({op})")
    print(f"  From: {from_acct:20s} → {ledger['accounts'][from_acct]:,} deg ({deg_to_tt(ledger['accounts'][from_acct], dpt):,.2f} TT)")
    print(f"  To:   {to_acct:20s} → {ledger['accounts'][to_acct]:,} deg ({deg_to_tt(ledger['accounts'][to_acct], dpt):,.2f} TT)")
    print(f"  Amount: {amount_deg:,} deg ({deg_to_tt(amount_deg, dpt):.2f} TT){format_eur(cfg, amount_deg, eur_per_tt, eur_per_kwh)}")
    if fee_deg:
        print(f"  Fee:    {fee_deg:,} deg ({deg_to_tt(fee_deg, dpt):.6f} TT){format_eur(cfg, fee_deg, eur_per_tt, eur_per_kwh)}"
              f"{' → ' + sustain_vault if sustain_vault else ''}")

# ---------- Commands ----------

def cmd_init(_args) -> int:
    cfg = load_config()
    lp = ledger_path(cfg)
    if lp.exists():
        print(f"Ledger already exists at {lp}")
        resp = input("Reinitialize and RESET all balances? (yes/no): ").strip().lower()
        if resp != "yes":
            print("Initialization cancelled.")
            return 1

    token = cfg["token"]
    policy = cfg["policy"]
    dpt = token["deg_per_tt"]
    genesis_tt = int(token["genesis_supply_tt"])
    genesis_deg = genesis_tt * dpt

    founder_bps = int(policy.get("founder_allocation_bps", 500))
    founder_deg = (genesis_deg * founder_bps) // 10000
    treasury_deg = genesis_deg - founder_deg

    treasury = token.get("treasury_account", "TREASURY")
    founder = token.get("founder_account", "FOUNDER")
    sustain = token.get("sustain_vault")

    accounts = {treasury: treasury_deg, founder: founder_deg}
    if sustain:
        accounts[sustain] = 0

    ledger = {
        "version": cfg.get("version", "3.14"),
        "policy_hash": compute_policy_hash(cfg),
        "accounts": accounts,
        "transactions": [],
        "metadata": {
            "created_at": now_iso(),
            "genesis_supply_deg": genesis_deg,
            "genesis_supply_tt": genesis_tt
        }
    }
    save_ledger(cfg, ledger)

    print(f"✓ Ledger initialized (v{ledger['version']})")
    print(f"✓ Genesis: {genesis_tt:,} TT ({genesis_deg:,} deg)")
    print(f"✓ Founder: {deg_to_tt(founder_deg, dpt):,.2f} TT ({founder_deg:,} deg)")
    print(f"✓ Treasury: {deg_to_tt(treasury_deg, dpt):,.2f} TT ({treasury_deg:,} deg)")
    if sustain:
        print("✓ Sustain vault: 0 TT (0 deg)")
    print(f"✓ Policy hash: {ledger['policy_hash'][:16]}...")
    return 0

def cmd_verify(_args) -> int:
    cfg = load_config()
    ledger = load_ledger(cfg)
    errors, warns = [], []

    # Policy immutability
    expect = compute_policy_hash(cfg)
    stored = ledger.get("policy_hash")
    if not stored:
        warns.append("No stored policy hash (legacy ledger)")
    elif stored != expect:
        errors.append(f"Policy hash mismatch: expected {expect[:16]}..., got {stored[:16]}...")

    # Supply invariant
    total_bal = sum(ledger["accounts"].values())
    genesis_deg = int(cfg["token"]["genesis_supply_tt"]) * int(cfg["token"]["deg_per_tt"])
    if total_bal != genesis_deg:
        errors.append(f"Total balance mismatch: {total_bal} != {genesis_deg}")

    # Negative balances
    for acct, bal in ledger["accounts"].items():
        if bal < 0:
            errors.append(f"Negative balance in {acct}: {bal}")

    # txlog presence
    if TXLOG.exists():
        with TXLOG.open(encoding="utf-8") as f:
            tx_count = sum(1 for _ in f)
        print(f"✓ Transaction log: {tx_count} entries")

    if errors:
        print("✗ Verification FAILED")
        for e in errors: print("  -", e)
        return 1

    print("✓ Verification PASSED")
    if warns:
        print("Warnings:")
        for w in warns: print("  -", w)
    print(f"✓ Policy hash: {expect[:16]}...")
    print(f"✓ Total supply: {genesis_deg:,} deg")
    print(f"✓ Accounts: {len(ledger['accounts'])}")
    print(f"✓ Transactions: {len(ledger.get('transactions', []))}")
    return 0

def cmd_balance(args) -> int:
    cfg = load_config()
    ledger = load_ledger(cfg)
    dpt = cfg["token"]["deg_per_tt"]

    if args.account:
        acct = args.account
        if acct not in ledger["accounts"]:
            print(f"Account '{acct}' not found")
            return 1
        bal_deg = ledger["accounts"][acct]
        print(f"\nAccount: {acct}")
        print(f"  Balance: {bal_deg:,} deg = {deg_to_tt(bal_deg, dpt):,.2f} TT{format_eur(cfg, bal_deg, args.eur_per_tt, args.eur_per_kwh)}")
    else:
        print("\n=== Token Balances ===")
        total_deg = int(cfg["token"]["genesis_supply_tt"]) * dpt
        print(f"Total Supply: {total_deg:,} deg ({int(cfg['token']['genesis_supply_tt']):,} TT)\n")
        for acct, bal_deg in sorted(ledger["accounts"].items()):
            print(f"{acct:20s}: {bal_deg:15,} deg = {deg_to_tt(bal_deg, dpt):12,.2f} TT"
                  f"{format_eur(cfg, bal_deg, args.eur_per_tt, args.eur_per_kwh)}")
    return 0

def cmd_transfer(args) -> int:
    cfg = load_config()
    ledger = load_ledger(cfg)
    dpt = cfg["token"]["deg_per_tt"]
    amt_deg = tt_to_deg_exact(args.tt, dpt)
    execute_operation(cfg, ledger, "transfer", args.from_account, args.to, amt_deg, args.eur_per_tt, args.eur_per_kwh)
    return 0

def cmd_reward(args) -> int:
    cfg = load_config()
    ledger = load_ledger(cfg)
    dpt = cfg["token"]["deg_per_tt"]
    treasury = cfg["token"].get("treasury_account", "TREASURY")
    amt_deg = tt_to_deg_exact(args.tt, dpt)
    execute_operation(cfg, ledger, "reward", treasury, args.to, amt_deg, args.eur_per_tt, args.eur_per_kwh)
    return 0

def cmd_consume(args) -> int:
    cfg = load_config()
    ledger = load_ledger(cfg)
    dpt = cfg["token"]["deg_per_tt"]
    treasury = cfg["token"].get("treasury_account", "TREASURY")
    amt_deg = tt_to_deg_exact(args.tt, dpt)
    execute_operation(cfg, ledger, "consume", args.from_account, treasury, amt_deg, args.eur_per_tt, args.eur_per_kwh)
    return 0

def cmd_quote(args) -> int:
    cfg = load_config()
    dpt = cfg["token"]["deg_per_tt"]
    amt_deg = tt_to_deg_exact(args.tt, dpt)
    fee_deg = compute_sustain_fee(cfg, args.op, amt_deg)
    net_deg = amt_deg - fee_deg if args.op == "reward" else amt_deg

    print(f"\n=== Quote for {args.op} ===")
    print(f"Amount: {amt_deg:,} deg ({deg_to_tt(amt_deg, dpt):.2f} TT){format_eur(cfg, amt_deg, args.eur_per_tt, args.eur_per_kwh)}")
    print(f"Fee:    {fee_deg:,} deg ({deg_to_tt(fee_deg, dpt):.6f} TT){format_eur(cfg, fee_deg, args.eur_per_tt, args.eur_per_kwh)}")
    if args.op == "transfer":
        print(f"Sender pays:   {amt_deg + fee_deg:,} deg ({deg_to_tt(amt_deg + fee_deg, dpt):.2f} TT)")
        print(f"Recipient gets:{amt_deg:,} deg ({deg_to_tt(amt_deg, dpt):.2f} TT)")
    elif args.op == "reward":
        print(f"Recipient gets:{net_deg:,} deg ({deg_to_tt(net_deg, dpt):.2f} TT){format_eur(cfg, net_deg, args.eur_per_tt, args.eur_per_kwh)}")
    elif args.op == "consume":
        print(f"Sender pays:   {amt_deg + fee_deg:,} deg ({deg_to_tt(amt_deg + fee_deg, dpt):.2f} TT)")
    return 0

def cmd_badge(args) -> int:
    cfg = load_config()
    ledger = load_ledger(cfg)
    dpt = cfg["token"]["deg_per_tt"]
    treasury = cfg["token"].get("treasury_account", "TREASURY")
    tre_deg = ledger["accounts"].get(treasury, 0)
    tre_tt = deg_to_tt(tre_deg, dpt)

    # SVG badge
    out_svg = Path(args.out)
    out_svg.parent.mkdir(parents=True, exist_ok=True)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="40">
  <rect width="220" height="40" fill="#0366d6"/>
  <text x="110" y="25" font-family="Arial" font-size="16" fill="white" text-anchor="middle">
    TT Treasury: {tre_tt:,.0f}
  </text>
</svg>'''
    out_svg.write_text(svg, encoding="utf-8")
    print(f"✓ Badge SVG: {out_svg}")

    # Optional Shields endpoint JSON
    badges_cfg = cfg.get("badges", {})
    endpoint_path = badges_cfg.get("path")
    if badges_cfg.get("enabled") and endpoint_path:
        ep = REPO_ROOT / endpoint_path
        ep.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schemaVersion": 1,
            "label": badges_cfg.get("label", "Teknia TT"),
            "message": f"{tre_tt:,.0f} TT",
            "color": badges_cfg.get("color", "blue")
        }
        ep.write_text(json.dumps(payload), encoding="utf-8")
        print(f"✓ Shields endpoint: {ep}")

    return 0

def cmd_auto(args) -> int:
    """
    Automation hooks for CXP events using config:
      - prices.cxp_publish_reward_tt
      - prices.cxp_consume_cost_tt
      - auto.reward_on_publish
      - auto.charge_on_consume
    """
    cfg = load_config()
    ledger = load_ledger(cfg)
    dpt = cfg["token"]["deg_per_tt"]
    treasury = cfg["token"].get("treasury_account", "TREASURY")
    actor = args.actor or "unknown"

    if args.event == "cxp-publish" and cfg.get("auto", {}).get("reward_on_publish", True):
        tt_amt = cfg.get("prices", {}).get("cxp_publish_reward_tt", 3)
        amt_deg = tt_to_deg_exact(str(tt_amt), dpt)
        execute_operation(cfg, ledger, "reward", treasury, f"user/{actor}", amt_deg, args.eur_per_tt, args.eur_per_kwh)
        return 0

    if args.event == "cxp-consume" and cfg.get("auto", {}).get("charge_on_consume", True):
        tt_amt = cfg.get("prices", {}).get("cxp_consume_cost_tt", 2)
        amt_deg = tt_to_deg_exact(str(tt_amt), dpt)
        # For a repo-level charge, send from TREASURY to sink
        execute_operation(cfg, ledger, "consume", treasury, "sink:consume", amt_deg, args.eur_per_tt, args.eur_per_kwh)
        return 0

    print("No auto action taken (disabled or unknown event).")
    return 0

# ---------- Main ----------

def main() -> int:
    p = argparse.ArgumentParser(description="Teknia Token (TT) CLI v3.14 — π-tier hybrid tokenomics",
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--config", help="Config file path (or set TEKNIA_CONFIG)")
    p.add_argument("--eur-per-tt", type=float, help="EUR per TT for valuation display")
    p.add_argument("--eur-per-kwh", type=float, help="EUR per kWh (Landauer@CMB valuation)")

    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("init", help="Initialize ledger with genesis supply")

    b = sub.add_parser("balance", help="Show balances")
    b.add_argument("--account", help="Specific account")

    x = sub.add_parser("transfer", help="Transfer tokens between accounts")
    x.add_argument("--from", dest="from_account", required=True)
    x.add_argument("--to", required=True)
    x.add_argument("--tt", required=True)

    r = sub.add_parser("reward", help="Reward tokens from treasury")
    r.add_argument("--to", required=True)
    r.add_argument("--tt", required=True)

    c = sub.add_parser("consume", help="Consume tokens to treasury")
    c.add_argument("--from", dest="from_account", required=True)
    c.add_argument("--tt", required=True)

    q = sub.add_parser("quote", help="Quote fees and net amounts (no mutation)")
    q.add_argument("--op", required=True, choices=["transfer", "reward", "consume"])
    q.add_argument("--tt", required=True)

    sub.add_parser("verify", help="Verify ledger integrity and policy hash")

    badge = sub.add_parser("badge", help="Generate badge SVG (+ Shields endpoint if configured)")
    badge.add_argument("--out", default="badges/tt-verified.svg")

    auto = sub.add_parser("auto", help="Automation hooks for CXP events")
    auto.add_argument("--event", required=True, choices=["cxp-publish", "cxp-consume"])
    auto.add_argument("--actor")
    auto.add_argument("--run-id")
    auto.add_argument("--pr")

    args = p.parse_args()
    if not args.cmd:
        p.print_help()
        return 0

    # Propagate --config to env for loaders
    if args.config:
        os.environ["TEKNIA_CONFIG"] = args.config

    try:
        if args.cmd == "init":    return cmd_init(args)
        if args.cmd == "balance": return cmd_balance(args)
        if args.cmd == "transfer": return cmd_transfer(args)
        if args.cmd == "reward":  return cmd_reward(args)
        if args.cmd == "consume": return cmd_consume(args)
        if args.cmd == "quote":   return cmd_quote(args)
        if args.cmd == "verify":  return cmd_verify(args)
        if args.cmd == "badge":   return cmd_badge(args)
        if args.cmd == "auto":    return cmd_auto(args)
        p.print_help(); return 0
    except (LedgerError, AmountError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        return 1

if __name__ == "__main__":
    sys.exit(main())

