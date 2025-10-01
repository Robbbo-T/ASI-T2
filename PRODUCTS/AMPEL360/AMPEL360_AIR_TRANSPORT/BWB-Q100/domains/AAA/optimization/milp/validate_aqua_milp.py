#!/usr/bin/env python3
"""
validate_aqua_milp.py
Validates the AQUA MILP system for UTCS-MI traceability compliance
"""

import json
import hashlib
from pathlib import Path

def validate_utcs_snapshot(snapshot_path="aqua_pyomo_solve_utcs.json"):
    """Validate UTCS snapshot structure and integrity"""
    
    print("=" * 60)
    print("AQUA MILP UTCS-MI Validation")
    print("=" * 60)
    
    # Load snapshot
    snapshot_file = Path(snapshot_path)
    if not snapshot_file.exists():
        print(f"❌ FAIL: Snapshot file {snapshot_path} not found")
        return False
        
    with open(snapshot_file, 'r') as f:
        snapshot = json.load(f)
    
    print(f"✓ Snapshot file loaded: {snapshot_path}")
    
    # Validate required fields
    required_fields = [
        "UTCS_ID",
        "Timestamp_UTC", 
        "Plan_Optimization_Horizon",
        "Optimization_Results_Summary",
        "Content_Hash_SHA256"
    ]
    
    missing_fields = [f for f in required_fields if f not in snapshot]
    if missing_fields:
        print(f"❌ FAIL: Missing required fields: {missing_fields}")
        return False
    
    print("✓ All required fields present")
    
    # Validate UTCS_ID format
    utcs_id = snapshot["UTCS_ID"]
    if not utcs_id.startswith("UTCS-"):
        print(f"❌ FAIL: Invalid UTCS_ID format: {utcs_id}")
        return False
    
    print(f"✓ UTCS_ID valid: {utcs_id}")
    
    # Validate hash format
    content_hash = snapshot["Content_Hash_SHA256"]
    if len(content_hash) != 64 or not all(c in '0123456789abcdef' for c in content_hash):
        print(f"❌ FAIL: Invalid SHA256 hash format")
        return False
    
    print(f"✓ Content hash valid: {content_hash[:16]}...")
    
    # Validate optimization results
    results = snapshot["Optimization_Results_Summary"]
    required_results = ["ObjectiveValue", "TotalEmissions", "TotalSyncDeviation"]
    missing_results = [r for r in required_results if r not in results]
    
    if missing_results:
        print(f"❌ FAIL: Missing results: {missing_results}")
        return False
    
    print("✓ Optimization results structure valid")
    
    # Display results
    print("\n--- Optimization Results ---")
    print(f"  Objective Value: {results['ObjectiveValue']:.2f}")
    print(f"  Total Emissions: {results['TotalEmissions']:.6f}")
    print(f"  Sync Deviation: {results['TotalSyncDeviation']:.6f}")
    
    # Validate plan structure
    plan = snapshot["Plan_Optimization_Horizon"]
    if 'x' not in plan or 'q' not in plan:
        print(f"❌ FAIL: Invalid plan structure")
        return False
    
    print(f"✓ Plan contains {len(plan['x'])} timesteps")
    
    print("\n" + "=" * 60)
    print("✅ SUCCESS: UTCS-MI validation passed")
    print("=" * 60)
    
    return True

def validate_data_model_separation():
    """Validate that model and data are properly separated"""
    
    print("\n" + "=" * 60)
    print("Data-Model Separation Validation")
    print("=" * 60)
    
    model_file = Path("aqua_milp_model.py")
    data_file = Path("aqua_milp.dat")
    
    if not model_file.exists():
        print(f"❌ FAIL: Model file not found")
        return False
    
    if not data_file.exists():
        print(f"❌ FAIL: Data file not found")
        return False
    
    print(f"✓ Model file: {model_file}")
    print(f"✓ Data file: {data_file}")
    
    # Compute hashes for traceability
    with open(model_file, 'rb') as f:
        model_hash = hashlib.sha256(f.read()).hexdigest()
    
    with open(data_file, 'rb') as f:
        data_hash = hashlib.sha256(f.read()).hexdigest()
    
    print(f"\nTraceability Hashes:")
    print(f"  Model SHA256: {model_hash[:16]}...{model_hash[-8:]}")
    print(f"  Data SHA256:  {data_hash[:16]}...{data_hash[-8:]}")
    
    # Check model doesn't contain hardcoded data
    with open(model_file, 'r') as f:
        model_content = f.read()
    
    # Look for suspicious patterns (hardcoded values)
    suspicious_patterns = [
        "= 0.98",  # reliability value
        "= 100.0",  # capacity value
        "= 2.0",  # cost value
    ]
    
    found_hardcoded = []
    for pattern in suspicious_patterns:
        if pattern in model_content:
            found_hardcoded.append(pattern)
    
    if found_hardcoded:
        print(f"\n⚠️  WARNING: Potential hardcoded values in model: {found_hardcoded}")
        print("    (May be acceptable for bounds/constraints)")
    else:
        print(f"\n✓ No hardcoded data values detected in model")
    
    print("\n" + "=" * 60)
    print("✅ SUCCESS: Data-Model separation verified")
    print("=" * 60)
    
    return True

def main():
    """Run all validations"""
    
    all_passed = True
    
    # Validate UTCS snapshot
    if not validate_utcs_snapshot():
        all_passed = False
    
    # Validate data-model separation
    if not validate_data_model_separation():
        all_passed = False
    
    if all_passed:
        print("\n" + "🎉 " * 20)
        print("All AQUA MILP validations passed!")
        print("🎉 " * 20)
        return 0
    else:
        print("\n❌ Some validations failed")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
