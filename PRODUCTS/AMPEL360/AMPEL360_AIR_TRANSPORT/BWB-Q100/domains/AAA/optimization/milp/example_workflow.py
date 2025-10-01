#!/usr/bin/env python3
"""
example_workflow.py
Demonstrates the complete AQUA MILP optimization workflow
"""

import sys
import subprocess
from pathlib import Path

def run_command(cmd, description):
    """Run a command and display results"""
    print(f"\n{'='*60}")
    print(f"📋 {description}")
    print(f"{'='*60}")
    print(f"$ {cmd}")
    print()
    
    result = subprocess.run(cmd, shell=False, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    if result.returncode != 0:
        print(f"❌ Command failed with exit code {result.returncode}")
        return False
    
    return True

def main():
    """Run the complete AQUA MILP workflow"""
    
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║    AQUA MILP Optimization System - Example Workflow       ║
    ║    Hybrid Classical-Quantum Resource Allocation           ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    # Check we're in the right directory
    if not Path("aqua_milp_model.py").exists():
        print("❌ Error: Must run from the AQUA MILP directory")
        print("   Navigate to: PRODUCTS/AMPEL360/.../AAA/optimization/milp/")
        return 1
    
    # Step 1: Generate data
    if not run_command(
        "python3 aqua_milp_data_generator.py",
        "Step 1: Generate Mission Data (aqua_milp.dat)"
    ):
        return 1
    
    # Step 2: Solve model
    if not run_command(
        "python3 aqua_milp_solve.py",
        "Step 2: Solve MILP Optimization Model"
    ):
        return 1
    
    # Step 3: Validate
    if not run_command(
        "python3 validate_aqua_milp.py",
        "Step 3: Validate UTCS-MI Compliance"
    ):
        return 1
    
    print("""
    
    ╔════════════════════════════════════════════════════════════╗
    ║                    ✅ Workflow Complete                    ║
    ╚════════════════════════════════════════════════════════════╝
    
    📁 Generated Files:
       • aqua_milp.dat              - Mission parameters (AMPL format)
       • aqua_pyomo_solve_utcs.json - UTCS traceability snapshot
    
    🔍 Key Results:
       • Optimal resource allocation computed
       • Classical-quantum synchronization verified
       • Emission constraints satisfied
       • UTCS-MI traceability validated
    
    📚 Next Steps:
       1. Review aqua_pyomo_solve_utcs.json for optimization results
       2. Modify aqua_milp_data_generator.py to test different scenarios
       3. Export model to .lp format for external solvers:
          model.write('aqua_milp.lp')
       4. Integrate with AQUA-OS scheduler
    
    🔗 Integration Points:
       • Mission Planning → aqua_milp.dat
       • AQUA-OS Scheduler → aqua_pyomo_solve_utcs.json
       • Certification → UTCS snapshot hashes
    """)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
