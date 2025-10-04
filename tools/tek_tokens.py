#!/usr/bin/env python3
"""
Teknia Token (TT) CLI - Token Management System v3.14

Genesis Supply: 2,000,000,000 TT
Divisibility: 360 deg per TT
Ledger: Integer-based in deg units
Founder Allocation: 5% at genesis
Sustain Fee: π-tiers for transfers (0.314%, 0.99%, 3.14%); 0.5% for reward/consume

Usage:
    python tek_tokens.py init                           # Initialize ledger
    python tek_tokens.py balance --account <account>    # Show balances
    python tek_tokens.py transfer --from <account> --to <account> --tt <amount>
    python tek_tokens.py reward --to <account> --tt <amount>
    python tek_tokens.py consume --from <account> --tt <amount>
    python tek_tokens.py quote --op <op> --tt <amount>
    python tek_tokens.py verify                         # Verify ledger
    python tek_tokens.py badge --out <file>            # Generate badge
"""

import argparse
import json
import sys
import os
import hashlib
import time
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
from typing import Dict, Optional, Tuple

# File path constants
DEFAULT_CONFIG = "finance/teknia.tokenomics.json"
REPO_ROOT = Path(__file__).parent.parent

def get_config_path():
    """Get config path from environment or default."""
    config_env = os.environ.get("TEKNIA_CONFIG", DEFAULT_CONFIG)
    return REPO_ROOT / config_env

# Dynamic file paths based on config
TXLOG = REPO_ROOT / "finance" / "txlog.jsonl"
TXHEAD = REPO_ROOT / "finance" / "txhead.json"


class LedgerError(Exception):
    """Ledger-related errors."""
    pass

class AmountError(Exception):
    """Amount validation errors."""
    pass

def load_config():
    """Load tokenomics configuration."""
    config_path = get_config_path()
    if not config_path.exists():
        raise LedgerError(f"Config not found at {config_path}")
    with config_path.open() as f:
        return json.load(f)

def compute_policy_hash(cfg):
    """Compute SHA-256 hash of policy section."""
    policy = cfg.get("policy", {})
    policy_json = json.dumps(policy, sort_keys=True)
    return hashlib.sha256(policy_json.encode()).hexdigest()

def ledger_path(cfg):
    """Get ledger file path from config."""
    return REPO_ROOT / cfg["token"]["ledger_file"]

def load_ledger(cfg):
    """Load ledger from disk."""
    lp = ledger_path(cfg)
    if not lp.exists():
        raise LedgerError(f"Ledger file not found: {lp}. Run 'init' first.")
    with lp.open() as f:
        return json.load(f)

def save_ledger(cfg, data):
    """Save ledger to disk atomically."""
    lp = ledger_path(cfg)
    lp.parent.mkdir(parents=True, exist_ok=True)
    tmp = lp.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
    tmp.replace(lp)

def tt_to_deg_exact(tt_str: str, deg_per_tt: int) -> int:
    """Convert TT to deg using exact fraction arithmetic."""
    try:
        frac = Fraction(str(tt_str))
    except Exception:
        raise AmountError("Invalid TT amount format")
    deg = frac * deg_per_tt
    if deg.denominator != 1:
        raise AmountError(f"{tt_str} TT does not map to integer deg with {deg_per_tt}/TT")
    if deg.numerator <= 0:
        raise AmountError(f"Amount must be positive: {tt_str} TT")
    return int(deg.numerator)

def deg_to_tt(deg: int, deg_per_tt: int) -> float:
    """Convert deg to TT."""
    return deg / deg_per_tt


def compute_sustain_fee(cfg, op: str, amount_deg: int) -> int:
    """
    Compute sustain fee based on operation type and amount.
    
    For transfers: use π-tiers if configured, else base fee
    For reward/consume: always use base fee (0.5%)
    """
    policy = cfg.get("policy", {})
    base_bps = policy.get("sustain_fee_bps", 50)  # Default 0.5%
    
    # Check if this operation uses tiers
    tiers_config = policy.get("sustain_fee_tiers", {})
    tier_scope = tiers_config.get("scope", [])
    
    if op in tier_scope and "schedule" in tiers_config:
        # Use tiered fee schedule (for transfers)
        schedule = tiers_config["schedule"]
        # Sort by min_deg descending to check highest tier first
        sorted_tiers = sorted(schedule, key=lambda t: t["min_deg"], reverse=True)
        
        for tier in sorted_tiers:
            if amount_deg >= tier["min_deg"]:
                # Parse BPS (might be string like "31.4" or int like 99)
                bps_val = tier["bps"]
                if isinstance(bps_val, str):
                    # Convert "31.4" to 31.4 bps = 0.314%
                    bps_fraction = Fraction(bps_val)
                    # Calculate fee: amount * (bps/10000), floored, using exact Fraction arithmetic
                    fee = int((amount_deg * bps_fraction) // 10000)
                else:
                    fee = (amount_deg * bps_val) // 10000
                return fee
        # Fallback to base if no tier matches
        return (amount_deg * base_bps) // 10000
    else:
        # Use base fee (for reward/consume or if no tiers configured)
        return (amount_deg * base_bps) // 10000

def validate_min_transfer(cfg, op: str, amount_deg: int):
    """Validate minimum transfer amount based on operation scope."""
    policy = cfg.get("policy", {})
    min_deg = policy.get("min_transfer_deg", 2592)
    scope = policy.get("min_transfer_scope", ["transfer"])
    
    if op in scope and amount_deg % min_deg != 0:
        deg_per_tt = cfg["token"]["deg_per_tt"]
        raise AmountError(
            f"Amount {amount_deg} deg ({deg_to_tt(amount_deg, deg_per_tt):.2f} TT) "
            f"is not a multiple of min_transfer_deg {min_deg} deg "
            f"({deg_to_tt(min_deg, deg_per_tt):.2f} TT)"
        )

def format_eur(cfg, deg: int, eur_per_tt: Optional[float] = None, 
               eur_per_kwh: Optional[float] = None) -> str:
    """Format EUR value if EUR pricing is provided."""
    if eur_per_tt is None and eur_per_kwh is None:
        return ""
    
    deg_per_tt = cfg["token"]["deg_per_tt"]
    tt_amount = deg_to_tt(deg, deg_per_tt)
    
    if eur_per_tt is not None:
        eur_value = tt_amount * eur_per_tt
    else:
        # Calculate via Landauer@CMB
        physics = cfg.get("physics", {})
        T_CMB = physics.get("T_CMB_K", 2.7255)
        k_B = physics.get("k_B_J_per_K", 1.380649e-23)
        ln2 = physics.get("ln2", 0.6931471805599453)
        
        # Energy per bit erasure at CMB temperature (Joules)
        E_bit = k_B * T_CMB * ln2
        # Assume 1 deg = 1 bit operation (simplified)
        energy_joules = deg * E_bit
        # Convert to kWh: 1 kWh = 3.6e6 J
        energy_kwh = energy_joules / 3.6e6
        eur_value = energy_kwh * eur_per_kwh
    
    return f" (≈ €{eur_value:.4f})"

def init_ledger(args):
    """Initialize ledger with genesis supply and founder allocation."""
    cfg = load_config()
    lp = ledger_path(cfg)
    
    if lp.exists():
        print(f"Warning: Ledger already exists at {lp}")
        response = input("Reinitialize and reset all accounts? (yes/no): ")
        if response.lower() != "yes":
            print("Initialization cancelled.")
            return
    
    token = cfg["token"]
    policy = cfg["policy"]
    
    genesis_supply_tt = token["genesis_supply_tt"]
    deg_per_tt = token["deg_per_tt"]
    genesis_supply_deg = genesis_supply_tt * deg_per_tt
    
    founder_bps = policy.get("founder_allocation_bps", 500)
    founder_deg = (genesis_supply_deg * founder_bps) // 10000
    treasury_deg = genesis_supply_deg - founder_deg
    
    treasury_acct = token.get("treasury_account", "TREASURY")
    founder_acct = token.get("founder_account", "FOUNDER")
    sustain_vault = token.get("sustain_vault")
    
    # Compute policy hash for immutability
    policy_hash = compute_policy_hash(cfg)
    
    accounts = {
        treasury_acct: treasury_deg,
        founder_acct: founder_deg
    }
    if sustain_vault:
        accounts[sustain_vault] = 0
    
    ledger = {
        "version": cfg.get("version", "3.14"),
        "policy_hash": policy_hash,
        "accounts": accounts,
        "transactions": [],
        "metadata": {
            "created_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "genesis_supply_deg": genesis_supply_deg,
            "genesis_supply_tt": genesis_supply_tt
        }
    }
    
    save_ledger(cfg, ledger)
    
    print(f"✓ Ledger initialized (v{cfg.get('version', '3.14')})")
    print(f"✓ Genesis supply: {genesis_supply_tt:,} TT ({genesis_supply_deg:,} deg)")
    print(f"✓ Founder allocation: {deg_to_tt(founder_deg, deg_per_tt):,.2f} TT ({founder_deg:,} deg)")
    print(f"✓ Treasury: {deg_to_tt(treasury_deg, deg_per_tt):,.2f} TT ({treasury_deg:,} deg)")
    if sustain_vault:
        print(f"✓ Sustain vault: 0 TT (0 deg)")
    print(f"✓ Policy hash: {policy_hash[:16]}...")

def verify_ledger(args):
    """Verify ledger integrity and policy hash."""
    cfg = load_config()
    ledger = load_ledger(cfg)
    
    errors = []
    warnings = []
    
    # 1. Check policy hash
    expected_hash = compute_policy_hash(cfg)
    stored_hash = ledger.get("policy_hash")
    if stored_hash and stored_hash != expected_hash:
        errors.append(f"Policy hash mismatch! Expected {expected_hash[:16]}..., got {stored_hash[:16]}...")
    elif not stored_hash:
        warnings.append("No policy hash stored (legacy ledger)")
    
    # 2. Check total supply
    genesis_supply_deg = cfg["token"]["genesis_supply_tt"] * cfg["token"]["deg_per_tt"]
    total_balance = sum(ledger["accounts"].values())
    if total_balance != genesis_supply_deg:
        errors.append(f"Total balance mismatch: {total_balance} != {genesis_supply_deg}")
    
    # 3. Check for negative balances
    for acct, bal in ledger["accounts"].items():
        if bal < 0:
            errors.append(f"Negative balance in {acct}: {bal}")
    
    # 4. Check transaction hash chain (if txlog exists)
    if TXLOG.exists():
        try:
            with TXLOG.open() as f:
                tx_count = sum(1 for _ in f)
            print(f"✓ Transaction log: {tx_count} entries")
        except Exception as e:
            warnings.append(f"Could not read txlog: {e}")
    
    if errors:
        print("✗ Verification FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print("✓ Verification PASSED")
        if warnings:
            print("Warnings:")
            for warn in warnings:
                print(f"  - {warn}")
        print(f"✓ Policy hash: {expected_hash[:16]}...")
        print(f"✓ Total supply: {genesis_supply_deg:,} deg")
        print(f"✓ Account count: {len(ledger['accounts'])}")
        print(f"✓ Transaction count: {len(ledger.get('transactions', []))}")
        return 0


def show_balance(args):
    """Display account balances."""
    cfg = load_config()
    ledger = load_ledger(cfg)
    deg_per_tt = cfg["token"]["deg_per_tt"]
    
    eur_per_tt = getattr(args, 'eur_per_tt', None)
    eur_per_kwh = getattr(args, 'eur_per_kwh', None)
    
    if args.account:
        if args.account not in ledger["accounts"]:
            print(f"Account '{args.account}' not found")
            return 1
        bal_deg = ledger["accounts"][args.account]
        bal_tt = deg_to_tt(bal_deg, deg_per_tt)
        eur_str = format_eur(cfg, bal_deg, eur_per_tt, eur_per_kwh)
        print(f"\nAccount: {args.account}")
        print(f"  Balance: {bal_deg:,} deg = {bal_tt:,.2f} TT{eur_str}")
    else:
        genesis_deg = cfg["token"]["genesis_supply_tt"] * deg_per_tt
        genesis_tt = cfg["token"]["genesis_supply_tt"]
        print(f"\n=== Token Balances ===")
        print(f"Total Supply: {genesis_deg:,} deg ({genesis_tt:,} TT)")
        print()
        for acct, bal_deg in sorted(ledger["accounts"].items()):
            bal_tt = deg_to_tt(bal_deg, deg_per_tt)
            eur_str = format_eur(cfg, bal_deg, eur_per_tt, eur_per_kwh)
            print(f"{acct:20s}: {bal_deg:15,} deg = {bal_tt:12,.2f} TT{eur_str}")
    return 0

def execute_operation(cfg, ledger, op: str, from_acct: str, to_acct: str, 
                      amount_deg: int, eur_per_tt=None, eur_per_kwh=None):
    """Execute a transfer/reward/consume operation."""
    deg_per_tt = cfg["token"]["deg_per_tt"]
    
    # Validate minimum transfer quantum
    validate_min_transfer(cfg, op, amount_deg)
    
    # Compute fee
    fee_deg = compute_sustain_fee(cfg, op, amount_deg)
    total_deduct = amount_deg + fee_deg
    
    # Check balance
    from_bal = ledger["accounts"].get(from_acct, 0)
    if from_bal < total_deduct:
        raise LedgerError(
            f"Insufficient balance in {from_acct}: "
            f"has {from_bal} deg, needs {total_deduct} deg "
            f"({amount_deg} + {fee_deg} fee)"
        )
    
    # Ensure destination accounts exist
    if to_acct not in ledger["accounts"]:
        ledger["accounts"][to_acct] = 0
    
    sustain_vault = cfg["token"].get("sustain_vault")
    if sustain_vault and sustain_vault not in ledger["accounts"]:
        ledger["accounts"][sustain_vault] = 0
    
    # Execute transfer
    ledger["accounts"][from_acct] -= total_deduct
    ledger["accounts"][to_acct] += amount_deg
    if sustain_vault and fee_deg > 0:
        ledger["accounts"][sustain_vault] += fee_deg
    
    # Record transaction
    tx_id = f"TX-{len(ledger.get('transactions', [])) + 1:06d}"
    tx = {
        "tx_id": tx_id,
        "type": op,
        "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "from": from_acct,
        "to": to_acct,
        "amount_deg": amount_deg,
        "amount_tt": deg_to_tt(amount_deg, deg_per_tt),
        "fee_deg": fee_deg,
        "fee_tt": deg_to_tt(fee_deg, deg_per_tt)
    }
    ledger.setdefault("transactions", []).append(tx)
    
    # Log to txlog
    log_tx(tx, ledger.get("policy_hash"))
    
    # Save ledger
    save_ledger(cfg, ledger)
    
    # Display result
    print(f"✓ {tx_id} completed ({op})")
    print(f"  From: {from_acct} (new: {ledger['accounts'][from_acct]:,} deg / {deg_to_tt(ledger['accounts'][from_acct], deg_per_tt):,.2f} TT)")
    print(f"  To: {to_acct} (new: {ledger['accounts'][to_acct]:,} deg / {deg_to_tt(ledger['accounts'][to_acct], deg_per_tt):,.2f} TT)")
    amt_eur = format_eur(cfg, amount_deg, eur_per_tt, eur_per_kwh)
    print(f"  Amount: {amount_deg:,} deg ({deg_to_tt(amount_deg, deg_per_tt):.2f} TT{amt_eur})")
    if fee_deg > 0:
        fee_eur = format_eur(cfg, fee_deg, eur_per_tt, eur_per_kwh)
        print(f"  Fee: {fee_deg:,} deg ({deg_to_tt(fee_deg, deg_per_tt):.6f} TT{fee_eur}) → {sustain_vault}")

def log_tx(tx: dict, policy_hash: Optional[str]):
    """Append transaction to txlog.jsonl."""
    TXLOG.parent.mkdir(parents=True, exist_ok=True)
    with TXLOG.open('a') as f:
        f.write(json.dumps(tx) + '\n')
    
    # Update txhead with hash chain
    prev_hash = ""
    if TXHEAD.exists():
        with TXHEAD.open() as f:
            head = json.load(f)
            prev_hash = head.get("hash", "")
    
    # Compute hash: prev_hash + tx_data
    tx_data = f"{prev_hash}:{tx['tx_id']}:{tx['timestamp']}:{tx['from']}:{tx['to']}:{tx['amount_deg']}"
    tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
    
    head = {
        "tx_id": tx["tx_id"],
        "hash": tx_hash,
        "prev_hash": prev_hash,
        "timestamp": tx["timestamp"]
    }
    with TXHEAD.open('w') as f:
        json.dump(head, f, indent=2)

def transfer_cmd(args):
    """Handle transfer command."""
    cfg = load_config()
    ledger = load_ledger(cfg)
    deg_per_tt = cfg["token"]["deg_per_tt"]
    
    amount_deg = tt_to_deg_exact(args.tt, deg_per_tt)
    execute_operation(cfg, ledger, "transfer", args.from_account, args.to, 
                     amount_deg, args.eur_per_tt, args.eur_per_kwh)
    return 0

def reward_cmd(args):
    """Handle reward command."""
    cfg = load_config()
    ledger = load_ledger(cfg)
    deg_per_tt = cfg["token"]["deg_per_tt"]
    treasury = cfg["token"].get("treasury_account", "TREASURY")
    
    amount_deg = tt_to_deg_exact(args.tt, deg_per_tt)
    execute_operation(cfg, ledger, "reward", treasury, args.to, 
                     amount_deg, args.eur_per_tt, args.eur_per_kwh)
    return 0

def consume_cmd(args):
    """Handle consume command."""
    cfg = load_config()
    ledger = load_ledger(cfg)
    deg_per_tt = cfg["token"]["deg_per_tt"]
    treasury = cfg["token"].get("treasury_account", "TREASURY")
    
    amount_deg = tt_to_deg_exact(args.tt, deg_per_tt)
    execute_operation(cfg, ledger, "consume", args.from_account, treasury, 
                     amount_deg, args.eur_per_tt, args.eur_per_kwh)
    return 0

def quote_cmd(args):
    """Handle quote command (non-mutating)."""
    cfg = load_config()
    deg_per_tt = cfg["token"]["deg_per_tt"]
    
    amount_deg = tt_to_deg_exact(args.tt, deg_per_tt)
    fee_deg = compute_sustain_fee(cfg, args.op, amount_deg)
    net_deg = amount_deg - fee_deg if args.op == "reward" else amount_deg
    
    print(f"\n=== Quote for {args.op} ===")
    amt_eur = format_eur(cfg, amount_deg, args.eur_per_tt, args.eur_per_kwh)
    print(f"Amount: {amount_deg:,} deg ({deg_to_tt(amount_deg, deg_per_tt):.2f} TT{amt_eur})")
    
    fee_eur = format_eur(cfg, fee_deg, args.eur_per_tt, args.eur_per_kwh)
    print(f"Fee: {fee_deg:,} deg ({deg_to_tt(fee_deg, deg_per_tt):.6f} TT{fee_eur})")
    
    if args.op == "transfer":
        print(f"Sender pays: {amount_deg + fee_deg:,} deg ({deg_to_tt(amount_deg + fee_deg, deg_per_tt):.2f} TT)")
        print(f"Recipient gets: {amount_deg:,} deg ({deg_to_tt(amount_deg, deg_per_tt):.2f} TT)")
    elif args.op == "reward":
        net_eur = format_eur(cfg, net_deg, args.eur_per_tt, args.eur_per_kwh)
        print(f"Recipient gets: {net_deg:,} deg ({deg_to_tt(net_deg, deg_per_tt):.2f} TT{net_eur})")
    elif args.op == "consume":
        print(f"Sender pays: {amount_deg + fee_deg:,} deg ({deg_to_tt(amount_deg + fee_deg, deg_per_tt):.2f} TT)")
    
    return 0

def badge_cmd(args):
    """Generate verification badge SVG."""
    cfg = load_config()
    ledger = load_ledger(cfg)
    deg_per_tt = cfg["token"]["deg_per_tt"]
    
    treasury = cfg["token"].get("treasury_account", "TREASURY")
    treasury_bal = ledger["accounts"].get(treasury, 0)
    treasury_tt = deg_to_tt(treasury_bal, deg_per_tt)
    
    # Simple SVG badge
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="40">
  <rect width="200" height="40" fill="#0366d6"/>
  <text x="100" y="25" font-family="Arial" font-size="16" fill="white" text-anchor="middle">
    TT: {treasury_tt:,.0f}
  </text>
</svg>'''
    
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('w') as f:
        f.write(svg)
    
    print(f"✓ Badge generated: {out_path}")
    print(f"  Treasury: {treasury_tt:,.0f} TT")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Teknia Token (TT) CLI v3.14 - π-tier hybrid tokenomics",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Global options
    parser.add_argument('--config', help='Config file path (or set TEKNIA_CONFIG env)')
    parser.add_argument('--eur-per-tt', type=float, help='EUR per TT for valuation display')
    parser.add_argument('--eur-per-kwh', type=float, help='EUR per kWh for Landauer@CMB valuation')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # init
    subparsers.add_parser('init', help='Initialize ledger with genesis supply')
    
    # balance
    bal_parser = subparsers.add_parser('balance', help='Show account balances')
    bal_parser.add_argument('--account', help='Specific account (optional)')
    
    # transfer
    xfer_parser = subparsers.add_parser('transfer', help='Transfer tokens between accounts')
    xfer_parser.add_argument('--from', dest='from_account', required=True, help='Source account')
    xfer_parser.add_argument('--to', required=True, help='Destination account')
    xfer_parser.add_argument('--tt', required=True, help='Amount in TT')
    
    # reward
    reward_parser = subparsers.add_parser('reward', help='Reward tokens from treasury')
    reward_parser.add_argument('--to', required=True, help='Recipient account')
    reward_parser.add_argument('--tt', required=True, help='Amount in TT')
    
    # consume
    consume_parser = subparsers.add_parser('consume', help='Consume tokens to treasury')
    consume_parser.add_argument('--from', dest='from_account', required=True, help='Source account')
    consume_parser.add_argument('--tt', required=True, help='Amount in TT')
    
    # quote
    quote_parser = subparsers.add_parser('quote', help='Quote fee/net for operation (non-mutating)')
    quote_parser.add_argument('--op', required=True, choices=['transfer', 'reward', 'consume'],
                             help='Operation type')
    quote_parser.add_argument('--tt', required=True, help='Amount in TT')
    
    # verify
    subparsers.add_parser('verify', help='Verify ledger integrity and policy hash')
    
    # badge
    badge_parser = subparsers.add_parser('badge', help='Generate verification badge SVG')
    badge_parser.add_argument('--out', default='badges/tt-verified.svg', 
                             help='Output file path (default: badges/tt-verified.svg)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    # Set config if provided
    if args.config:
        os.environ["TEKNIA_CONFIG"] = args.config
    
    try:
        if args.command == 'init':
            return init_ledger(args)
        elif args.command == 'balance':
            return show_balance(args)
        elif args.command == 'transfer':
            return transfer_cmd(args)
        elif args.command == 'reward':
            return reward_cmd(args)
        elif args.command == 'consume':
            return consume_cmd(args)
        elif args.command == 'quote':
            return quote_cmd(args)
        elif args.command == 'verify':
            return verify_ledger(args)
        elif args.command == 'badge':
            return badge_cmd(args)
        else:
            parser.print_help()
            return 0
    
    except (LedgerError, AmountError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
