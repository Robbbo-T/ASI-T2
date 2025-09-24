#!/usr/bin/env python3
"""
Meta-OS Test Framework
Comprehensive testing suite for aerospace system validation
"""

import argparse
import json
import yaml
import subprocess
import tempfile
import os
import time
from pathlib import Path
from typing import Dict, List, Any
import unittest

class MetaOSTestFramework:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.test_results = []
        self.temp_dir = None
    
    def setup(self):
        """Initialize test environment"""
        self.temp_dir = tempfile.mkdtemp(prefix="metaos_test_")
        print(f"[TEST] Created temporary directory: {self.temp_dir}")
    
    def teardown(self):
        """Clean up test environment"""
        if self.temp_dir and os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)
            print(f"[TEST] Cleaned up temporary directory")
    
    def test_yaml_artifacts(self) -> bool:
        """Test all YAML files for syntax validity"""
        print("[TEST] Validating YAML artifacts...")
        yaml_files = [
            "orchestrator/manifests/mission/uav_sat_demo.yaml",
            "middleware/dds/qos_policies.yaml",
            "security/fdir/rules/uav_fdir.yaml",
            "security/attestation/tpm_evidence.yaml"
        ]
        
        success = True
        for yaml_file in yaml_files:
            file_path = self.base_path / yaml_file
            try:
                with open(file_path, 'r') as f:
                    yaml.safe_load(f)
                print(f"  ✓ {yaml_file}")
            except Exception as e:
                print(f"  ✗ {yaml_file}: {e}")
                success = False
        
        self.test_results.append(("YAML Validation", success))
        return success
    
    def test_json_artifacts(self) -> bool:
        """Test all JSON files for syntax validity"""
        print("[TEST] Validating JSON artifacts...")
        json_files = [
            "security/ota/update-manifests/uav01_2025-09-24.json"
        ]
        
        success = True
        for json_file in json_files:
            file_path = self.base_path / json_file
            try:
                with open(file_path, 'r') as f:
                    json.load(f)
                print(f"  ✓ {json_file}")
            except Exception as e:
                print(f"  ✗ {json_file}: {e}")
                success = False
        
        self.test_results.append(("JSON Validation", success))
        return success
    
    def test_cli_tools(self) -> bool:
        """Test CLI tools functionality"""
        print("[TEST] Testing CLI tools...")
        
        success = True
        
        # Test metaosctl deploy
        try:
            result = subprocess.run([
                "python3", str(self.base_path / "tooling/cli/metaosctl.py"),
                "deploy", str(self.base_path / "orchestrator/manifests/mission/uav_sat_demo.yaml"),
                "--require-attestation"
            ], capture_output=True, text=True, cwd=self.base_path)
            
            if result.returncode == 0 and "DONE (stub)" in result.stdout:
                print("  ✓ metaosctl deploy")
            else:
                print(f"  ✗ metaosctl deploy: {result.stderr}")
                success = False
        except Exception as e:
            print(f"  ✗ metaosctl deploy: {e}")
            success = False
        
        # Test metaosctl qos audit
        try:
            result = subprocess.run([
                "python3", str(self.base_path / "tooling/cli/metaosctl.py"),
                "qos", "audit", "--profile", "crit-telemetry", "--asset", "UAV-01"
            ], capture_output=True, text=True, cwd=self.base_path)
            
            if result.returncode == 0 and "Profile: crit-telemetry" in result.stdout:
                print("  ✓ metaosctl qos audit")
            else:
                print(f"  ✗ metaosctl qos audit: {result.stderr}")
                success = False
        except Exception as e:
            print(f"  ✗ metaosctl qos audit: {e}")
            success = False
        
        # Test metaosctl fdir test
        try:
            result = subprocess.run([
                "python3", str(self.base_path / "tooling/cli/metaosctl.py"),
                "fdir", "test", str(self.base_path / "security/fdir/rules/uav_fdir.yaml"),
                "--inject", "LOST_GNSS"
            ], capture_output=True, text=True, cwd=self.base_path)
            
            if result.returncode == 0 and "plan_rtl" in result.stdout:
                print("  ✓ metaosctl fdir test")
            else:
                print(f"  ✗ metaosctl fdir test: {result.stderr}")
                success = False
        except Exception as e:
            print(f"  ✗ metaosctl fdir test: {e}")
            success = False
        
        self.test_results.append(("CLI Tools", success))
        return success
    
    def test_simulator(self) -> bool:
        """Test the system simulator"""
        print("[TEST] Testing system simulator...")
        
        try:
            # Run a short simulation
            result = subprocess.run([
                "python3", str(self.base_path / "tooling/cli/metaos_simulator.py"),
                "--duration", "5",
                "--export", os.path.join(self.temp_dir, "test_telemetry.json")
            ], capture_output=True, text=True, cwd=self.base_path, timeout=30)
            
            if result.returncode == 0 and "Mission simulation completed" in result.stdout:
                # Check if telemetry file was created
                telemetry_file = os.path.join(self.temp_dir, "test_telemetry.json")
                if os.path.exists(telemetry_file):
                    with open(telemetry_file, 'r') as f:
                        telemetry_data = json.load(f)
                    
                    if len(telemetry_data) > 0:
                        print(f"  ✓ Simulator ran successfully, generated {len(telemetry_data)} telemetry messages")
                        success = True
                    else:
                        print("  ✗ Simulator ran but generated no telemetry")
                        success = False
                else:
                    print("  ✗ Simulator ran but telemetry export failed")
                    success = False
            else:
                print(f"  ✗ Simulator failed: {result.stderr}")
                success = False
        except subprocess.TimeoutExpired:
            print("  ✗ Simulator test timed out")
            success = False
        except Exception as e:
            print(f"  ✗ Simulator test error: {e}")
            success = False
        
        self.test_results.append(("Simulator", success))
        return success
    
    def test_mission_schema_validation(self) -> bool:
        """Test mission manifest schema validation"""
        print("[TEST] Testing mission schema validation...")
        
        mission_file = self.base_path / "orchestrator/manifests/mission/uav_sat_demo.yaml"
        
        try:
            with open(mission_file, 'r') as f:
                mission_data = yaml.safe_load(f)
            
            required_fields = ["missionId", "assets", "placement", "telemetry"]
            success = True
            
            for field in required_fields:
                if field not in mission_data:
                    print(f"  ✗ Missing required field: {field}")
                    success = False
                else:
                    print(f"  ✓ Required field present: {field}")
            
            # Validate asset structure
            if "assets" in mission_data and isinstance(mission_data["assets"], list):
                for i, asset in enumerate(mission_data["assets"]):
                    asset_required = ["id", "nodeClass", "roles"]
                    for field in asset_required:
                        if field not in asset:
                            print(f"  ✗ Asset {i} missing field: {field}")
                            success = False
            
            self.test_results.append(("Mission Schema", success))
            return success
            
        except Exception as e:
            print(f"  ✗ Mission schema validation failed: {e}")
            self.test_results.append(("Mission Schema", False))
            return False
    
    def test_qos_policy_validation(self) -> bool:
        """Test QoS policy validation"""
        print("[TEST] Testing QoS policy validation...")
        
        qos_file = self.base_path / "middleware/dds/qos_policies.yaml"
        
        try:
            with open(qos_file, 'r') as f:
                qos_data = yaml.safe_load(f)
            
            success = True
            
            if "profiles" not in qos_data:
                print("  ✗ Missing 'profiles' section")
                success = False
            else:
                profiles = qos_data["profiles"]
                
                # Check critical telemetry profile
                if "crit-telemetry" in profiles:
                    profile = profiles["crit-telemetry"]
                    required_fields = ["reliability", "history", "deadline"]
                    
                    for field in required_fields:
                        if field in profile:
                            print(f"  ✓ crit-telemetry has {field}")
                        else:
                            print(f"  ✗ crit-telemetry missing {field}")
                            success = False
                    
                    # Check priority value
                    if "transport_priority" in profile:
                        priority = profile["transport_priority"]
                        if isinstance(priority, int) and 0 <= priority <= 15:
                            print(f"  ✓ Valid transport_priority: {priority}")
                        else:
                            print(f"  ✗ Invalid transport_priority: {priority}")
                            success = False
                else:
                    print("  ✗ Missing crit-telemetry profile")
                    success = False
            
            self.test_results.append(("QoS Validation", success))
            return success
            
        except Exception as e:
            print(f"  ✗ QoS validation failed: {e}")
            self.test_results.append(("QoS Validation", False))
            return False
    
    def run_all_tests(self) -> bool:
        """Run all test suites"""
        print("=" * 60)
        print("Meta-OS Test Framework - Running All Tests")
        print("=" * 60)
        
        self.setup()
        
        all_success = True
        all_success &= self.test_yaml_artifacts()
        all_success &= self.test_json_artifacts()
        all_success &= self.test_cli_tools()
        all_success &= self.test_simulator()
        all_success &= self.test_mission_schema_validation()
        all_success &= self.test_qos_policy_validation()
        
        self.teardown()
        
        print("\n" + "=" * 60)
        print("Test Results Summary:")
        print("=" * 60)
        
        for test_name, success in self.test_results:
            status = "PASS" if success else "FAIL"
            print(f"{test_name:30} {status}")
        
        overall_status = "PASS" if all_success else "FAIL"
        print(f"{'Overall Status':30} {overall_status}")
        
        return all_success

def main():
    parser = argparse.ArgumentParser(description="Meta-OS Test Framework")
    parser.add_argument("--base-path", type=str, default=".", help="Base path to Meta-OS directory")
    parser.add_argument("--test", choices=["yaml", "json", "cli", "simulator", "schema", "all"], 
                       default="all", help="Specific test to run")
    
    args = parser.parse_args()
    
    base_path = Path(args.base_path).resolve()
    if not base_path.exists():
        print(f"Error: Base path {base_path} does not exist")
        return 1
    
    framework = MetaOSTestFramework(base_path)
    
    if args.test == "all":
        success = framework.run_all_tests()
    elif args.test == "yaml":
        framework.setup()
        success = framework.test_yaml_artifacts()
        framework.teardown()
    elif args.test == "json":
        framework.setup()
        success = framework.test_json_artifacts()
        framework.teardown()
    elif args.test == "cli":
        framework.setup()
        success = framework.test_cli_tools()
        framework.teardown()
    elif args.test == "simulator":
        framework.setup()
        success = framework.test_simulator()
        framework.teardown()
    elif args.test == "schema":
        framework.setup()
        success = framework.test_mission_schema_validation() and framework.test_qos_policy_validation()
        framework.teardown()
    else:
        print(f"Unknown test: {args.test}")
        return 1
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())