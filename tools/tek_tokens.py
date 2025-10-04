#!/usr/bin/env python3
"""
Teknia Token (TT) CLI - Token Management System v3.1

Genesis Supply: 2,000,000,000 TT
Divisibility: 360 deg per TT
Ledger: Integer-based in deg units
Founder Allocation: 5% at genesis
Sustain Fee: 0.5% per operation (from sender)

Usage:
    python tek_tokens.py init                           # Initialize ledger
    python tek_tokens.py balance [account]              # Show balances
    python tek_tokens.py tx --type <type> --amount <n> [--tokens] --from <account> --to <account>
    python tek_tokens.py verify                         # Generate verification badge
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Optional

# Constants
TT_TO_DEG = 360
GENESIS_SUPPLY_TT = 2_000_000_000
GENESIS_SUPPLY_DEG = GENESIS_SUPPLY_TT * TT_TO_DEG

# File paths
REPO_ROOT = Path(__file__).parent.parent
TOKENOMICS_FILE = REPO_ROOT / "finance" / "teknia.tokenomics.json"
LEDGER_FILE = REPO_ROOT / "finance" / "ledger.json"
BADGE_FILE = REPO_ROOT / "finance" / "token_badge.json"
LEDGER_LOG_FILE = REPO_ROOT / "finance" / "ledger.log"


class TokenLedger:
    """Manages the token ledger with integer deg precision."""
    
    def __init__(self):
        self.ledger = self._load_ledger()
        self.tokenomics = self._load_tokenomics()
        
        # Load policy settings
        policy = self.tokenomics.get("policy", {})
        self.min_transfer_deg = policy.get("min_transfer_deg", 2592)
        self.founder_allocation_bps = policy.get("founder_allocation_bps", 500)  # 5%
        self.sustain_fee_bps = policy.get("sustain_fee_bps", 50)  # 0.5%
        
        # Load account names
        token_config = self.tokenomics.get("token", {})
        self.treasury_account = token_config.get("treasury_account", "TREASURY")
        self.founder_account = token_config.get("founder_account", "FOUNDER")
        self.sustain_vault = token_config.get("sustain_vault", "VAULT_SUSTAIN")
    
    def _load_tokenomics(self) -> Dict:
        """Load tokenomics configuration."""
        if not TOKENOMICS_FILE.exists():
            print(f"Error: Tokenomics file not found at {TOKENOMICS_FILE}")
            sys.exit(1)
        
        with open(TOKENOMICS_FILE, 'r') as f:
            return json.load(f)
    
    def _load_ledger(self) -> Dict:
        """Load ledger from disk or return empty ledger."""
        if LEDGER_FILE.exists():
            with open(LEDGER_FILE, 'r') as f:
                return json.load(f)
        return {
            "accounts": {},
            "transactions": [],
            "metadata": {
                "created_at": None,
                "last_updated": None,
                "version": "1.0"
            }
        }
    
    def _save_ledger(self):
        """Save ledger to disk."""
        self.ledger["metadata"]["last_updated"] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LEDGER_FILE, 'w') as f:
            json.dump(self.ledger, f, indent=2)
        print(f"Ledger saved to {LEDGER_FILE}")
    
    def _log_transaction(self, tx_id: str, tx_type: str, from_account: str, to_account: str, 
                        amount_deg: int, tx_hash: str = None):
        """Append transaction to ledger.log for auditing."""
        timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        if tx_hash is None:
            # Generate simple hash from transaction data
            import hashlib
            tx_data = f"{tx_id}:{timestamp}:{from_account}:{to_account}:{amount_deg}"
            tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()[:16]
        
        log_entry = {
            "id": tx_id,
            "timestamp": timestamp,
            "src": from_account,
            "dst": to_account,
            "deg": amount_deg,
            "hash": tx_hash
        }
        
        # Append to log file
        LEDGER_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LEDGER_LOG_FILE, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    
    def tt_to_deg(self, tt: float) -> int:
        """Convert TT to deg. Must result in integer deg."""
        deg = tt * TT_TO_DEG
        if abs(deg - round(deg)) >= 1e-10:
            raise ValueError(f"Invalid TT amount: {tt} TT does not convert to integer deg")
        return int(round(deg))
    
    def deg_to_tt(self, deg: int) -> float:
        """Convert deg to TT."""
        return deg / TT_TO_DEG
    
    def get_balance(self, account: str) -> int:
        """Get balance in deg."""
        return self.ledger["accounts"].get(account, 0)
    
    def get_balance_tt(self, account: str) -> float:
        """Get balance in TT."""
        return self.deg_to_tt(self.get_balance(account))
    
    def initialize(self):
        """Initialize the ledger with genesis supply, founder allocation, and treasury."""
        if self.ledger["accounts"]:
            print("Warning: Ledger already initialized. Accounts exist:")
            for account, balance in self.ledger["accounts"].items():
                print(f"  {account}: {balance} deg ({self.deg_to_tt(balance):.2f} TT)")
            response = input("Reinitialize and reset all accounts? (yes/no): ")
            if response.lower() != "yes":
                print("Initialization cancelled.")
                return
        
        # Calculate founder allocation (5% = 500 bps, floor)
        founder_allocation_deg = (GENESIS_SUPPLY_DEG * self.founder_allocation_bps) // 10000
        treasury_initial_deg = GENESIS_SUPPLY_DEG - founder_allocation_deg
        
        # Reset ledger with three accounts
        self.ledger = {
            "accounts": {
                self.treasury_account: treasury_initial_deg,
                self.founder_account: founder_allocation_deg,
                self.sustain_vault: 0
            },
            "transactions": [
                {
                    "tx_id": "GENESIS-MINT",
                    "type": "mint",
                    "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                    "from": "genesis",
                    "to": self.treasury_account,
                    "amount_deg": GENESIS_SUPPLY_DEG,
                    "amount_tt": GENESIS_SUPPLY_TT,
                    "description": "Initial mint of genesis supply"
                },
                {
                    "tx_id": "GENESIS-FOUNDER",
                    "type": "founder_allocation",
                    "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                    "from": self.treasury_account,
                    "to": self.founder_account,
                    "amount_deg": founder_allocation_deg,
                    "amount_tt": self.deg_to_tt(founder_allocation_deg),
                    "description": f"Founder allocation: {self.founder_allocation_bps} bps of genesis supply"
                }
            ],
            "metadata": {
                "created_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "last_updated": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "version": "1.0",
                "total_supply_deg": GENESIS_SUPPLY_DEG,
                "total_supply_tt": GENESIS_SUPPLY_TT
            }
        }
        
        self._save_ledger()
        print(f"✓ Ledger initialized (v3.1)")
        print(f"✓ Genesis supply: {GENESIS_SUPPLY_TT:,} TT ({GENESIS_SUPPLY_DEG:,} deg)")
        print(f"✓ Founder allocation (5%): {self.deg_to_tt(founder_allocation_deg):,.2f} TT ({founder_allocation_deg:,} deg)")
        print(f"✓ Treasury balance: {self.deg_to_tt(treasury_initial_deg):,.2f} TT ({treasury_initial_deg:,} deg)")
        print(f"✓ Sustain vault: 0 TT (0 deg)")
    
    def transfer(self, from_account: str, to_account: str, amount_deg: int, tx_type: str = "transfer"):
        """Transfer tokens between accounts with 0.5% sustain fee."""
        # Validate min_transfer_deg quantum
        if amount_deg % self.min_transfer_deg != 0:
            raise ValueError(
                f"Invalid transfer amount: {amount_deg} deg is not a multiple of "
                f"min_transfer_deg ({self.min_transfer_deg} deg = {self.deg_to_tt(self.min_transfer_deg):.2f} TT). "
                f"Transfer amount must be a multiple of the minimum quantum."
            )
        
        # Calculate sustain fee (0.5% = 50 bps, floor)
        sustain_fee_deg = (amount_deg * self.sustain_fee_bps) // 10000
        total_deduction_deg = amount_deg + sustain_fee_deg
        
        # Validate from account exists and has sufficient balance
        if from_account not in self.ledger["accounts"]:
            raise ValueError(f"Account '{from_account}' does not exist")
        
        from_balance = self.ledger["accounts"][from_account]
        if from_balance < total_deduction_deg:
            raise ValueError(
                f"Insufficient balance in '{from_account}': "
                f"has {from_balance} deg ({self.deg_to_tt(from_balance):.2f} TT), "
                f"needs {total_deduction_deg} deg ({self.deg_to_tt(total_deduction_deg):.2f} TT) "
                f"[{amount_deg} transfer + {sustain_fee_deg} sustain fee]"
            )
        
        # Ensure to_account and sustain_vault exist
        if to_account not in self.ledger["accounts"]:
            self.ledger["accounts"][to_account] = 0
        if self.sustain_vault not in self.ledger["accounts"]:
            self.ledger["accounts"][self.sustain_vault] = 0
        
        # Perform transfer and fee collection
        self.ledger["accounts"][from_account] -= total_deduction_deg
        self.ledger["accounts"][to_account] += amount_deg
        self.ledger["accounts"][self.sustain_vault] += sustain_fee_deg
        
        # Record transaction
        tx_id = f"TX-{len(self.ledger['transactions']) + 1:06d}"
        transaction = {
            "tx_id": tx_id,
            "type": tx_type,
            "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "from": from_account,
            "to": to_account,
            "amount_deg": amount_deg,
            "amount_tt": self.deg_to_tt(amount_deg),
            "sustain_fee_deg": sustain_fee_deg,
            "sustain_fee_tt": self.deg_to_tt(sustain_fee_deg) if sustain_fee_deg > 0 else 0
        }
        self.ledger["transactions"].append(transaction)
        
        # Log transaction to ledger.log
        self._log_transaction(tx_id, tx_type, from_account, to_account, amount_deg)
        
        self._save_ledger()
        print(f"✓ Transaction {tx_id} completed")
        print(f"  Type: {tx_type}")
        print(f"  From: {from_account} (new balance: {self.ledger['accounts'][from_account]} deg / {self.get_balance_tt(from_account):.2f} TT)")
        print(f"  To: {to_account} (new balance: {self.ledger['accounts'][to_account]} deg / {self.get_balance_tt(to_account):.2f} TT)")
        print(f"  Amount: {amount_deg} deg ({self.deg_to_tt(amount_deg):.2f} TT)")
        if sustain_fee_deg > 0:
            print(f"  Sustain Fee: {sustain_fee_deg} deg ({self.deg_to_tt(sustain_fee_deg):.6f} TT) → {self.sustain_vault}")
    
    def show_balance(self, account: Optional[str] = None):
        """Display account balances."""
        if account:
            if account not in self.ledger["accounts"]:
                print(f"Account '{account}' not found")
                return
            balance_deg = self.ledger["accounts"][account]
            balance_tt = self.deg_to_tt(balance_deg)
            print(f"\nAccount: {account}")
            print(f"  Balance: {balance_deg:,} deg")
            print(f"  Balance: {balance_tt:,.2f} TT")
        else:
            print("\n=== Token Balances ===")
            print(f"Total Supply: {GENESIS_SUPPLY_DEG:,} deg ({GENESIS_SUPPLY_TT:,} TT)")
            print()
            total_distributed = 0
            for acc, balance in sorted(self.ledger["accounts"].items()):
                total_distributed += balance
                balance_tt = self.deg_to_tt(balance)
                print(f"{acc:20s}: {balance:15,} deg = {balance_tt:15,.2f} TT")
            print(f"{'-'*60}")
            print(f"{'Total Distributed':20s}: {total_distributed:15,} deg = {self.deg_to_tt(total_distributed):15,.2f} TT")
    
    def generate_badge(self):
        """Generate a verification badge JSON."""
        total_distributed = sum(self.ledger["accounts"].values())
        if "treasury" in self.ledger["accounts"]:
            treasury_balance = self.get_balance("treasury")
        else:
            print("Warning: 'treasury' account not found in ledger. Setting treasury balance to 0.")
            treasury_balance = 0
        
        badge = {
            "schemaVersion": 1,
            "label": "TT Balance",
            "message": f"{self.deg_to_tt(treasury_balance):,.0f} TT",
            "color": "blue",
            "namedLogo": "ethereum",
            "style": "for-the-badge",
            "metadata": {
                "treasury_balance_deg": treasury_balance,
                "treasury_balance_tt": self.deg_to_tt(treasury_balance),
                "total_supply_deg": GENESIS_SUPPLY_DEG,
                "total_supply_tt": GENESIS_SUPPLY_TT,
                "total_distributed_deg": total_distributed,
                "total_distributed_tt": self.deg_to_tt(total_distributed),
                "num_accounts": len(self.ledger["accounts"]),
                "num_transactions": len(self.ledger["transactions"]),
                "last_updated": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
            }
        }
        
        with open(BADGE_FILE, 'w') as f:
            json.dump(badge, f, indent=2)
        
        print(f"✓ Badge generated at {BADGE_FILE}")
        print(f"  Treasury: {self.deg_to_tt(treasury_balance):,.0f} TT")
        print(f"  Total Distributed: {self.deg_to_tt(total_distributed):,.0f} TT")


def main():
    parser = argparse.ArgumentParser(
        description="Teknia Token (TT) CLI - Token Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Initialize ledger (first time only)
  python tek_tokens.py init
  
  # Show all balances
  python tek_tokens.py balance
  
  # Show specific account balance
  python tek_tokens.py balance treasury
  
  # Transfer 1 TT (360 deg)
  python tek_tokens.py tx --type transfer --amount 1 --tokens --from treasury --to user/alice
  
  # Transfer 0.5 TT (180 deg) - valid because 0.5*360=180 is integer
  python tek_tokens.py tx --type transfer --amount 0.5 --tokens --from treasury --to user/bob
  
  # Transfer in deg directly (7.2 TT = 2592 deg)
  python tek_tokens.py tx --type transfer --amount 2592 --from treasury --to user/charlie
  
  # Reward for CXP publish (3 TT = 1080 deg)
  python tek_tokens.py tx --type cxp_publish_reward --amount 3 --tokens --from treasury --to user/alice
  
  # Charge for CXP consume (2 TT = 720 deg)
  python tek_tokens.py tx --type cxp_consume_charge --amount 2 --tokens --from user/alice --to treasury
  
  # Generate verification badge
  python tek_tokens.py verify
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Init command
    subparsers.add_parser('init', help='Initialize ledger with genesis supply')
    
    # Balance command
    balance_parser = subparsers.add_parser('balance', help='Show account balances')
    balance_parser.add_argument('account', nargs='?', help='Specific account to show (optional)')
    
    # Transaction command
    tx_parser = subparsers.add_parser('tx', help='Perform a transaction')
    tx_parser.add_argument('--type', required=True, 
                          choices=['transfer', 'cxp_publish_reward', 'cxp_consume_charge'],
                          help='Transaction type')
    tx_parser.add_argument('--amount', required=True, type=float,
                          help='Amount to transfer')
    tx_parser.add_argument('--tokens', action='store_true',
                          help='Amount is in TT (convert to deg). Default is deg.')
    tx_parser.add_argument('--from', dest='from_account', required=True,
                          help='Source account')
    tx_parser.add_argument('--to', dest='to_account', required=True,
                          help='Destination account')
    
    # Verify command
    subparsers.add_parser('verify', help='Generate verification badge')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        ledger = TokenLedger()
        
        if args.command == 'init':
            ledger.initialize()
        
        elif args.command == 'balance':
            ledger.show_balance(args.account)
        
        elif args.command == 'tx':
            # Convert amount to deg if --tokens flag is used
            if args.tokens:
                amount_deg = ledger.tt_to_deg(args.amount)
            else:
                # Amount is already in deg, must be integer
                if not args.amount.is_integer():
                    print(f"Error: Amount must be integer when specified in deg")
                    return 1
                amount_deg = int(args.amount)
            
            ledger.transfer(args.from_account, args.to_account, amount_deg, args.type)
        
        elif args.command == 'verify':
            ledger.generate_badge()
        
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
