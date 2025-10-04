#!/usr/bin/env python3
"""
Test suite for Teknia Token CLI v3.1 with min_transfer_deg validation,
founder allocation, and sustain fees
"""

import json
import sys
import os
from pathlib import Path
import tempfile
import shutil

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Import the token ledger
from tek_tokens import TokenLedger, TT_TO_DEG, GENESIS_SUPPLY_DEG, GENESIS_SUPPLY_TT


class TestTokenLedger:
    """Test suite for TokenLedger with min_transfer_deg validation."""
    
    def __init__(self):
        self.test_dir = None
        self.original_files = {}
        self.tests_passed = 0
        self.tests_failed = 0
    
    def setup(self):
        """Setup test environment with temporary files."""
        # Create temporary directory
        self.test_dir = tempfile.mkdtemp(prefix="tek_tokens_test_")
        print(f"Test directory: {self.test_dir}")
        
        # Backup original files
        from tek_tokens import LEDGER_FILE, BADGE_FILE, LEDGER_LOG_FILE
        for file_path in [LEDGER_FILE, BADGE_FILE, LEDGER_LOG_FILE]:
            if file_path.exists():
                backup_path = Path(self.test_dir) / file_path.name
                shutil.copy(file_path, backup_path)
                self.original_files[file_path] = backup_path
                # Remove original for testing
                file_path.unlink()
    
    def teardown(self):
        """Restore original files and cleanup."""
        from tek_tokens import LEDGER_FILE, BADGE_FILE, LEDGER_LOG_FILE
        
        # Remove test files
        for file_path in [LEDGER_FILE, BADGE_FILE, LEDGER_LOG_FILE]:
            if file_path.exists():
                file_path.unlink()
        
        # Restore backups
        for original_path, backup_path in self.original_files.items():
            if backup_path.exists():
                shutil.copy(backup_path, original_path)
        
        # Clean up temp directory
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
    
    def assert_raises(self, exception_type, func, *args, **kwargs):
        """Assert that function raises expected exception."""
        try:
            func(*args, **kwargs)
            return False
        except exception_type:
            return True
        except Exception as e:
            print(f"    Unexpected exception: {type(e).__name__}: {e}")
            return False
    
    def test_initialization(self):
        """Test ledger initialization with founder allocation."""
        print("\nTest 1: Ledger Initialization (v3.1)")
        ledger = TokenLedger()
        ledger.initialize()
        
        # Calculate expected values
        founder_allocation = (GENESIS_SUPPLY_DEG * 500) // 10000  # 5%
        treasury_balance = GENESIS_SUPPLY_DEG - founder_allocation
        
        self.assert_true(
            ledger.get_balance("FOUNDER") == founder_allocation,
            f"Founder has correct allocation (5%): {founder_allocation} deg"
        )
        self.assert_true(
            ledger.get_balance("TREASURY") == treasury_balance,
            f"Treasury has correct balance (95%): {treasury_balance} deg"
        )
        self.assert_true(
            ledger.get_balance("VAULT_SUSTAIN") == 0,
            "Sustain vault initialized to 0"
        )
        self.assert_true(
            len(ledger.ledger["transactions"]) == 2,
            "Genesis mint and founder allocation transactions recorded"
        )
    
    def test_min_transfer_deg_loading(self):
        """Test that min_transfer_deg is loaded correctly."""
        print("\nTest 2: min_transfer_deg Loading")
        ledger = TokenLedger()
        
        self.assert_true(
            ledger.min_transfer_deg == 2592,
            f"min_transfer_deg is 2592 (got {ledger.min_transfer_deg})"
        )
        self.assert_true(
            ledger.deg_to_tt(2592) == 7.2,
            "min_transfer_deg equals 7.2 TT"
        )
    
    def test_valid_transfer_multiples(self):
        """Test valid transfers that are multiples of min_transfer_deg with sustain fee."""
        print("\nTest 3: Valid Transfer Multiples (with sustain fee)")
        ledger = TokenLedger()
        
        # Make sure ledger is initialized
        if not ledger.ledger["accounts"]:
            ledger.initialize()
        
        # Test 1x min_transfer_deg (2592 deg = 7.2 TT)
        try:
            initial_vault = ledger.get_balance("VAULT_SUSTAIN")
            ledger.transfer("TREASURY", "user/alice", 2592, "transfer")
            self.assert_true(True, "Transfer of 2592 deg (1x quantum) succeeded")
            # Verify sustain fee collected (0.5% of 2592 = 12.96, floor to 12)
            expected_fee = (2592 * 50) // 10000
            actual_vault = ledger.get_balance("VAULT_SUSTAIN")
            self.assert_true(
                actual_vault == initial_vault + expected_fee,
                f"Sustain fee collected: {expected_fee} deg"
            )
        except Exception as e:
            self.assert_true(False, f"Transfer of 2592 deg failed: {e}")
        
        # Test 2x min_transfer_deg (5184 deg = 14.4 TT)
        try:
            ledger.transfer("TREASURY", "user/bob", 5184, "transfer")
            self.assert_true(True, "Transfer of 5184 deg (2x quantum) succeeded")
        except Exception as e:
            self.assert_true(False, f"Transfer of 5184 deg failed: {e}")
        
        # Test 10x min_transfer_deg (25920 deg = 72 TT)
        try:
            ledger.transfer("TREASURY", "user/charlie", 25920, "transfer")
            self.assert_true(True, "Transfer of 25920 deg (10x quantum) succeeded")
        except Exception as e:
            self.assert_true(False, f"Transfer of 25920 deg failed: {e}")
    
    def test_invalid_transfer_non_multiples(self):
        """Test that transfers NOT multiples of min_transfer_deg are rejected."""
        print("\nTest 4: Invalid Transfer Non-Multiples (Should be rejected)")
        ledger = TokenLedger()
        
        # Make sure ledger is initialized
        if not ledger.ledger["accounts"]:
            ledger.initialize()
        
        # Test 1 deg (should fail)
        result = self.assert_raises(
            ValueError,
            ledger.transfer,
            "TREASURY", "user/alice", 1, "transfer"
        )
        self.assert_true(result, "Transfer of 1 deg rejected")
        
        # Test 360 deg = 1 TT (should fail as it's not multiple of 2592)
        result = self.assert_raises(
            ValueError,
            ledger.transfer,
            "TREASURY", "user/alice", 360, "transfer"
        )
        self.assert_true(result, "Transfer of 360 deg (1 TT) rejected")
        
        # Test 36 deg = 0.1 TT (should fail)
        result = self.assert_raises(
            ValueError,
            ledger.transfer,
            "TREASURY", "user/alice", 36, "transfer"
        )
        self.assert_true(result, "Transfer of 36 deg (0.1 TT) rejected")
        
        # Test 18 deg = 0.05 TT (should fail)
        result = self.assert_raises(
            ValueError,
            ledger.transfer,
            "TREASURY", "user/alice", 18, "transfer"
        )
        self.assert_true(result, "Transfer of 18 deg (0.05 TT) rejected")
        
        # Test 1080 deg = 3 TT (should fail as it's not multiple of 2592)
        result = self.assert_raises(
            ValueError,
            ledger.transfer,
            "TREASURY", "user/alice", 1080, "transfer"
        )
        self.assert_true(result, "Transfer of 1080 deg (3 TT) rejected")
    
    def test_transaction_logging(self):
        """Test that transactions are logged to ledger.log."""
        print("\nTest 5: Transaction Logging")
        from tek_tokens import LEDGER_LOG_FILE
        
        ledger = TokenLedger()
        
        # Make sure ledger is initialized
        if not ledger.ledger["accounts"]:
            ledger.initialize()
        
        # Perform a valid transfer
        ledger.transfer("TREASURY", "user/alice", 2592, "transfer")
        
        # Check log file exists
        self.assert_true(
            LEDGER_LOG_FILE.exists(),
            "ledger.log file created"
        )
        
        # Read and validate log entry
        if LEDGER_LOG_FILE.exists():
            with open(LEDGER_LOG_FILE, 'r') as f:
                lines = f.readlines()
                self.assert_true(len(lines) >= 1, "At least one log entry exists")
                
                if lines:
                    log_entry = json.loads(lines[-1])
                    self.assert_true("id" in log_entry, "Log entry has 'id' field")
                    self.assert_true("timestamp" in log_entry, "Log entry has 'timestamp' field")
                    self.assert_true("src" in log_entry, "Log entry has 'src' field")
                    self.assert_true("dst" in log_entry, "Log entry has 'dst' field")
                    self.assert_true("deg" in log_entry, "Log entry has 'deg' field")
                    self.assert_true("hash" in log_entry, "Log entry has 'hash' field")
                    self.assert_true(log_entry["deg"] == 2592, "Log entry has correct amount")
    
    def test_integer_deg_validation(self):
        """Test that non-integer deg amounts are still rejected."""
        print("\nTest 6: Integer deg Validation")
        ledger = TokenLedger()
        
        # Test that invalid TT amounts (non-integer deg) are rejected
        result = self.assert_raises(
            ValueError,
            ledger.tt_to_deg,
            0.01  # 0.01 TT = 3.6 deg (not integer)
        )
        self.assert_true(result, "0.01 TT (3.6 deg) rejected")
        
        result = self.assert_raises(
            ValueError,
            ledger.tt_to_deg,
            0.001  # 0.001 TT = 0.36 deg (not integer)
        )
        self.assert_true(result, "0.001 TT (0.36 deg) rejected")
    
    def test_balance_verification(self):
        """Test that total balance equals genesis supply."""
        print("\nTest 7: Balance Verification")
        ledger = TokenLedger()
        
        # Make sure ledger is initialized
        if not ledger.ledger["accounts"]:
            ledger.initialize()
        
        # Perform several transfers
        ledger.transfer("TREASURY", "user/alice", 2592, "transfer")
        ledger.transfer("TREASURY", "user/bob", 5184, "transfer")
        ledger.transfer("TREASURY", "user/charlie", 25920, "transfer")
        
        # Sum all balances
        total_balance = sum(ledger.ledger["accounts"].values())
        
        self.assert_true(
            total_balance == GENESIS_SUPPLY_DEG,
            f"Total balance equals genesis supply ({total_balance} == {GENESIS_SUPPLY_DEG})"
        )
    
    def test_transaction_type_variants(self):
        """Test different transaction types."""
        print("\nTest 8: Transaction Type Variants")
        ledger = TokenLedger()
        
        # Make sure ledger is initialized
        if not ledger.ledger["accounts"]:
            ledger.initialize()
        
        # Test transfer
        try:
            ledger.transfer("TREASURY", "user/alice", 2592, "transfer")
            self.assert_true(True, "Transfer transaction succeeded")
        except Exception as e:
            self.assert_true(False, f"Transfer transaction failed: {e}")
        
        # Test reward
        try:
            ledger.transfer("TREASURY", "user/bob", 2592, "cxp_publish_reward")
            self.assert_true(True, "Reward transaction succeeded")
        except Exception as e:
            self.assert_true(False, f"Reward transaction failed: {e}")
        
        # Test consume/charge
        try:
            ledger.transfer("user/alice", "TREASURY", 2592, "cxp_consume_charge")
            self.assert_true(True, "Consume/charge transaction succeeded")
        except Exception as e:
            self.assert_true(False, f"Consume/charge transaction failed: {e}")
    
    def run_all_tests(self):
        """Run all tests."""
        print("="*60)
        print("Teknia Token CLI Test Suite v3.1")
        print("Testing quantum validation, founder allocation, sustain fees")
        print("="*60)
        
        try:
            self.setup()
            
            self.test_initialization()
            self.test_min_transfer_deg_loading()
            self.test_valid_transfer_multiples()
            self.test_invalid_transfer_non_multiples()
            self.test_transaction_logging()
            self.test_integer_deg_validation()
            self.test_balance_verification()
            self.test_transaction_type_variants()
            
        finally:
            self.teardown()
        
        return self.tests_failed == 0


def main():
    """Run test suite."""
    test_suite = TestTokenLedger()
    success = test_suite.run_all_tests()
    
    if success:
        print("\n✓ All tests passed!")
        return 0
    else:
        print(f"\n✗ {test_suite.tests_failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
