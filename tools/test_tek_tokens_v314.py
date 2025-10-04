#!/usr/bin/env python3
"""
Test suite for Teknia Token CLI v3.14 with π-tier fees, policy hash,
and enhanced features.
"""

import re
import json
import sys
import os
from pathlib import Path
import tempfile
import shutil
import subprocess

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

REPO_ROOT = Path(__file__).parent.parent

class TestTokenLedgerV314:
    """Test suite for v3.14 token system."""
    
    def __init__(self):
        self.test_dir = None
        self.original_files = {}
        self.tests_passed = 0
        self.tests_failed = 0
    
    def setup(self):
        """Setup test environment with temporary files."""
        self.test_dir = tempfile.mkdtemp(prefix="tek_tokens_v314_test_")
        print(f"Test directory: {self.test_dir}")
        
        # Backup original files
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        txlog = REPO_ROOT / "finance" / "txlog.jsonl"
        txhead = REPO_ROOT / "finance" / "txhead.json"
        badge_dir = REPO_ROOT / "badges"
        
        for file_path in [ledger_file, txlog, txhead]:
            if file_path.exists():
                backup_path = Path(self.test_dir) / file_path.name
                shutil.copy(file_path, backup_path)
                self.original_files[file_path] = backup_path
                file_path.unlink()
        
        if badge_dir.exists():
            backup_path = Path(self.test_dir) / "badges"
            shutil.copytree(badge_dir, backup_path, dirs_exist_ok=True)
            self.original_files[badge_dir] = backup_path
    
    def teardown(self):
        """Restore original files and cleanup."""
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        txlog = REPO_ROOT / "finance" / "txlog.jsonl"
        txhead = REPO_ROOT / "finance" / "txhead.json"
        badge_dir = REPO_ROOT / "badges"
        
        for file_path in [ledger_file, txlog, txhead]:
            if file_path.exists():
                file_path.unlink()
        
        if badge_dir.exists():
            shutil.rmtree(badge_dir)
        
        for original_path, backup_path in self.original_files.items():
            if backup_path.exists():
                if backup_path.is_dir():
                    shutil.copytree(backup_path, original_path, dirs_exist_ok=True)
                else:
                    shutil.copy(backup_path, original_path)
        
        if self.test_dir and Path(self.test_dir).exists():
            shutil.rmtree(self.test_dir)
        
        print(f"\n{'='*60}")
        print(f"Tests Passed: {self.tests_passed}")
        print(f"Tests Failed: {self.tests_failed}")
        print(f"{'='*60}")
    
    def assert_true(self, condition, message):
        """Assert that condition is True."""
        if condition:
            print(f"  ✓ {message}")
            self.tests_passed += 1
        else:
            print(f"  ✗ {message}")
            self.tests_failed += 1
    
    # --- helpers for robust stdout checks ---
    @staticmethod
    def _has_number_with_unit(text: str, value: int, unit: str = "deg") -> bool:
        """
        True if 'text' contains the integer 'value' followed by 'unit', with or without
        thousands separators (e.g., '2,566 deg' or '2566 deg').
        """
        pattern = rf"(?:\b{value:,}\s*{unit}\b|\b{value}\s*{unit}\b)"
        return re.search(pattern, text) is not None
    
    def run_cli(self, *args):
        """Run CLI command and return result."""
        cmd = [sys.executable, str(REPO_ROOT / "tools" / "tek_tokens.py")] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result
    
    def test_initialization(self):
        """Test ledger initialization with v3.14."""
        print("\nTest 1: Ledger Initialization (v3.14)")
        result = self.run_cli("init")
        
        self.assert_true(result.returncode == 0, "Init command succeeded")
        self.assert_true("v3.14" in result.stdout or "3.14" in result.stdout, "Version 3.14 mentioned")
        self.assert_true("Policy hash:" in result.stdout, "Policy hash stored")
        
        # Check ledger file
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        self.assert_true(ledger_file.exists(), "Ledger file created")
        
        with ledger_file.open() as f:
            ledger = json.load(f)
        
        self.assert_true("policy_hash" in ledger, "Policy hash in ledger")
        self.assert_true("TREASURY" in ledger["accounts"], "TREASURY account exists")
        self.assert_true("FOUNDER" in ledger["accounts"], "FOUNDER account exists")
        self.assert_true("VAULT_SUSTAIN" in ledger["accounts"], "VAULT_SUSTAIN account exists")
        
        # Check founder allocation (5%)
        genesis_deg = 720_000_000_000
        founder_deg = (genesis_deg * 500) // 10000
        self.assert_true(
            ledger["accounts"]["FOUNDER"] == founder_deg,
            f"Founder has 5% allocation ({founder_deg:,} deg)"
        )
    
    def test_pi_tier_fees(self):
        """Test π-tier fee calculation for transfers."""
        print("\nTest 2: π-Tier Fee Calculation")
        
        # Initialize if not already done
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        if not ledger_file.exists():
            self.run_cli("init")
        
        # Test 72 TT transfer (should use 0.314% tier)
        result = self.run_cli("transfer", "--from", "TREASURY", "--to", "alice", "--tt", "72")
        self.assert_true(result.returncode == 0, "72 TT transfer succeeded")
        self.assert_true("81 deg" in result.stdout, "Fee is 81 deg (0.314% of 25920)")
        
        # Test 720 TT transfer (should use 0.99% tier)
        result = self.run_cli("transfer", "--from", "TREASURY", "--to", "bob", "--tt", "720")
        self.assert_true(result.returncode == 0, "720 TT transfer succeeded")
        self.assert_true(self._has_number_with_unit(result.stdout, 2566, "deg"),
                        "Fee is 2566 deg (0.99% of 259200)")
        
        # Test 7200 TT transfer (should use 3.14% tier)
        result = self.run_cli("transfer", "--from", "TREASURY", "--to", "charlie", "--tt", "7200")
        self.assert_true(result.returncode == 0, "7200 TT transfer succeeded")
        self.assert_true(self._has_number_with_unit(result.stdout, 81388, "deg"),
                        "Fee is 81388 deg (3.14% of 2592000)")
    
    def test_reward_base_fee(self):
        """Test that reward uses 0.5% base fee, not π-tiers."""
        print("\nTest 3: Reward Uses Base Fee (0.5%)")
        
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        if not ledger_file.exists():
            self.run_cli("init")
        
        # Test 72 TT reward (should use 0.5% = 129 deg fee, not 0.314% = 81 deg)
        result = self.run_cli("reward", "--to", "dave", "--tt", "72")
        self.assert_true(result.returncode == 0, "72 TT reward succeeded")
        self.assert_true("129 deg" in result.stdout, "Fee is 129 deg (0.5% of 25920)")
    
    def test_min_transfer_scope(self):
        """Test that min_transfer_deg only applies to transfers, not reward/consume."""
        print("\nTest 4: Min Transfer Scope")
        
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        if not ledger_file.exists():
            self.run_cli("init")
        
        # Transfer of 7 TT should fail (not multiple of 7.2)
        result = self.run_cli("transfer", "--from", "TREASURY", "--to", "test", "--tt", "7")
        self.assert_true(result.returncode != 0, "7 TT transfer rejected (not multiple of 7.2)")
        
        # Reward of 1 TT should succeed (no min quantum for reward)
        result = self.run_cli("reward", "--to", "test2", "--tt", "1")
        self.assert_true(result.returncode == 0, "1 TT reward succeeded (no min quantum)")
    
    def test_quote_command(self):
        """Test quote command for fee estimation."""
        print("\nTest 5: Quote Command")
        
        # Quote for 720 TT transfer
        result = self.run_cli("quote", "--op", "transfer", "--tt", "720")
        self.assert_true(result.returncode == 0, "Quote command succeeded")
        self.assert_true(self._has_number_with_unit(result.stdout, 2566, "deg"),
                        "Quote shows correct fee (0.99% tier)")
        self.assert_true("Sender pays:" in result.stdout, "Quote shows sender cost")
        self.assert_true("Recipient gets:" in result.stdout, "Quote shows recipient amount")
        
        # Quote for reward should show 0.5% fee
        result = self.run_cli("quote", "--op", "reward", "--tt", "72")
        self.assert_true(result.returncode == 0, "Quote reward succeeded")
        self.assert_true("129 deg" in result.stdout, "Quote shows 0.5% fee for reward")
    
    def test_verify_command(self):
        """Test verify command checks policy hash and invariants."""
        print("\nTest 6: Verify Command")
        
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        if not ledger_file.exists():
            self.run_cli("init")
        
        # Verify should pass
        result = self.run_cli("verify")
        self.assert_true(result.returncode == 0, "Verify succeeded")
        self.assert_true("PASSED" in result.stdout, "Verification passed")
        self.assert_true("Policy hash:" in result.stdout, "Policy hash checked")
        self.assert_true("Total supply:" in result.stdout, "Total supply checked")
    
    def test_badge_command(self):
        """Test badge generation."""
        print("\nTest 7: Badge Generation")
        
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        if not ledger_file.exists():
            self.run_cli("init")
        
        result = self.run_cli("badge")
        self.assert_true(result.returncode == 0, "Badge command succeeded")
        
        badge_file = REPO_ROOT / "badges" / "tt-verified.svg"
        self.assert_true(badge_file.exists(), "Badge SVG file created")
        
        with badge_file.open() as f:
            content = f.read()
        self.assert_true("<svg" in content, "Badge is valid SVG")
    
    def test_eur_valuation(self):
        """Test EUR valuation display."""
        print("\nTest 8: EUR Valuation")
        
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        if not ledger_file.exists():
            self.run_cli("init")
        
        result = self.run_cli("--eur-per-tt", "0.10", "quote", "--op", "transfer", "--tt", "720")
        self.assert_true(result.returncode == 0, "EUR valuation succeeded")
        self.assert_true("€" in result.stdout, "EUR symbol displayed")
    
    def test_balance_verification(self):
        """Test that total balance equals genesis supply after transfers."""
        print("\nTest 9: Balance Conservation")
        
        ledger_file = REPO_ROOT / "finance" / "ledger.json"
        if not ledger_file.exists():
            self.run_cli("init")
        
        # Do several transfers
        self.run_cli("transfer", "--from", "TREASURY", "--to", "user1", "--tt", "7.2")
        self.run_cli("transfer", "--from", "TREASURY", "--to", "user2", "--tt", "14.4")
        self.run_cli("reward", "--to", "user3", "--tt", "10")
        
        # Load ledger and verify total
        with ledger_file.open() as f:
            ledger = json.load(f)
        
        total = sum(ledger["accounts"].values())
        genesis_deg = 720_000_000_000
        self.assert_true(total == genesis_deg, f"Total balance equals genesis ({total:,} == {genesis_deg:,})")
    
    def run_all_tests(self):
        """Run all tests."""
        print("="*60)
        print("Teknia Token CLI Test Suite v3.14")
        print("Testing π-tier fees, policy hash, and enhanced features")
        print("="*60)
        
        try:
            self.setup()
            
            self.test_initialization()
            self.test_pi_tier_fees()
            self.test_reward_base_fee()
            self.test_min_transfer_scope()
            self.test_quote_command()
            self.test_verify_command()
            self.test_badge_command()
            self.test_eur_valuation()
            self.test_balance_verification()
            
        finally:
            self.teardown()
        
        return self.tests_failed == 0


def main():
    """Run test suite."""
    test_suite = TestTokenLedgerV314()
    success = test_suite.run_all_tests()
    
    if success:
        print("\n✓ All tests passed!")
        return 0
    else:
        print(f"\n✗ {test_suite.tests_failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
