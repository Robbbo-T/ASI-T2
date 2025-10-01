"""
Simple test for the AQUA MILP Optimization module.
Tests basic model construction and execution.
"""
import sys
import os
import json
from pathlib import Path

# Add the optimization directory to the path
sys.path.insert(0, str(Path(__file__).parent))

def test_import():
    """Test that the module can be imported"""
    try:
        import aqua_milp_pyomo
        print("✓ Module import successful")
        return True
    except Exception as e:
        print(f"✗ Module import failed: {e}")
        return False

def test_solver_detection():
    """Test that at least one solver is available"""
    try:
        from pyomo.environ import SolverFactory
        
        solvers = ['gurobi', 'cbc', 'glpk', 'cplex']
        found = None
        
        for s in solvers:
            try:
                solver = SolverFactory(s)
                if solver.available(exception_flag=False):
                    found = s
                    break
            except Exception:
                continue
        
        if found:
            print(f"✓ Solver detection successful: {found}")
            return True
        else:
            print("✗ No solver found")
            return False
    except Exception as e:
        print(f"✗ Solver detection failed: {e}")
        return False

def test_model_execution():
    """Test that the model can be executed"""
    try:
        # Run the model as a subprocess to avoid conflicts
        import subprocess
        result = subprocess.run(
            [sys.executable, "aqua_milp_pyomo.py"],
            cwd=Path(__file__).parent,
            capture_output=True,
            timeout=120
        )
        
        if result.returncode == 0:
            print("✓ Model execution successful")
            
            # Check if output file was created
            output_file = Path(__file__).parent / "aqua_pyomo_plan_utcs.json"
            if output_file.exists():
                # Validate JSON structure
                with open(output_file, 'r') as f:
                    data = json.load(f)
                    
                required_fields = [
                    "UTCS_ID", "Timestamp_UTC", "SystemDomain", 
                    "SubsystemID", "ConfigVersion", "Mode",
                    "QuantumLayerPresent", "Plan_Optimization_Horizon",
                    "Optimization_Results_Summary", "Content_Hash_SHA256"
                ]
                
                missing = [f for f in required_fields if f not in data]
                if missing:
                    print(f"✗ UTCS-MI output missing fields: {missing}")
                    return False
                
                print("✓ UTCS-MI output validation successful")
                
                # Clean up output file
                output_file.unlink()
                
            return True
        else:
            print(f"✗ Model execution failed with code {result.returncode}")
            print(f"STDOUT: {result.stdout.decode()}")
            print(f"STDERR: {result.stderr.decode()}")
            return False
    except Exception as e:
        print(f"✗ Model execution failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("AQUA MILP Optimization Module Tests")
    print("="*50 + "\n")
    
    tests = [
        ("Import Test", test_import),
        ("Solver Detection Test", test_solver_detection),
        ("Model Execution Test", test_model_execution),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\nRunning: {name}")
        print("-" * 30)
        results.append(test_func())
    
    print("\n" + "="*50)
    print("Test Summary")
    print("="*50)
    
    passed = sum(results)
    total = len(results)
    print(f"\nPassed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ All tests passed!")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
