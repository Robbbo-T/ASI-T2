#!/usr/bin/env python3
"""
Structure verification script for ASI-T2 repository.
Ensures the ENVIRONMENTS structure remains consistent and prevents regressions.
"""
import os
import sys
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def fail(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)

def main():
    print("🔍 Verifying ASI-T2 repository structure...")
    
    # 1) Check for merge conflicts
    print("  Checking for merge conflict markers...")
    for dp, _, files in os.walk(ROOT):
        for f in files:
            p = os.path.join(dp, f)
            try:
                with open(p, 'r', errors='ignore') as fh:
                    content = fh.read()
                if re.search(r'^(<<<<<<< |======= |>>>>>>> )', content, re.MULTILINE):
                    fail(f"Merge conflict markers found in {p}")
            except Exception:
                continue

    # 2) Check ENVIRONMENTS structure
    print("  Verifying ENVIRONMENTS structure...")
    env_dir = os.path.join(ROOT, "ENVIRONMENTS")
    if not os.path.exists(env_dir):
        fail("ENVIRONMENTS directory missing")

    env_contents = set(os.listdir(env_dir))
    
    # Required top-level directories
    required_dirs = {"DIGITAL", "PHYSICAL"}
    
    for req in required_dirs:
        if req not in env_contents:
            fail(f"Missing required ENVIRONMENTS/{req} directory")

    # Check for case collision issues
    print("  Checking for case collision issues...")
    forbidden_dirs = {"Air", "Cross", "Digital", "Ground", "Sea", "Space"}
    for forbidden in forbidden_dirs:
        if forbidden in env_contents:
            fail(f"Found forbidden directory ENVIRONMENTS/{forbidden} - should be LEGACY_{forbidden}")

    # 3) Check DIGITAL/CONTEXT structure
    print("  Verifying DIGITAL/CONTEXT structure...")
    digital_context = os.path.join(env_dir, "DIGITAL", "CONTEXT")
    if not os.path.exists(digital_context):
        fail("ENVIRONMENTS/DIGITAL/CONTEXT directory missing")

    required_digital_contexts = {
        "VIRTUAL", "QUANTUM", "AUGMENTATION", "EXTENSION", 
        "PROJECTION", "MIX", "CROSS"
    }
    
    digital_contents = set(os.listdir(digital_context))
    for ctx in required_digital_contexts:
        if ctx not in digital_contents:
            fail(f"Missing ENVIRONMENTS/DIGITAL/CONTEXT/{ctx}")
        
        readme_path = os.path.join(digital_context, ctx, "README.md")
        if not os.path.exists(readme_path):
            fail(f"Missing README.md in ENVIRONMENTS/DIGITAL/CONTEXT/{ctx}")

    # 4) Check PHYSICAL/CONTEXT structure
    print("  Verifying PHYSICAL/CONTEXT structure...")
    physical_context = os.path.join(env_dir, "PHYSICAL", "CONTEXT")
    if not os.path.exists(physical_context):
        fail("ENVIRONMENTS/PHYSICAL/CONTEXT directory missing")

    required_physical_contexts = {
        "AIR", "SEA", "DEEP_SEA", "GROUND", "SPACE", "DEEP_SPACE", "CYBER"
    }
    
    physical_contents = set(os.listdir(physical_context))
    for ctx in required_physical_contexts:
        if ctx not in physical_contents:
            fail(f"Missing ENVIRONMENTS/PHYSICAL/CONTEXT/{ctx}")
        
        readme_path = os.path.join(physical_context, ctx, "README.md")
        if not os.path.exists(readme_path):
            fail(f"Missing README.md in ENVIRONMENTS/PHYSICAL/CONTEXT/{ctx}")

    # 5) Verify legacy directories follow correct naming
    print("  Verifying legacy directory naming...")
    legacy_dirs = [d for d in env_contents if d.startswith("LEGACY_")]
    expected_legacy = {"LEGACY_Air", "LEGACY_Cross", "LEGACY_Digital", "LEGACY_Ground", "LEGACY_Sea", "LEGACY_Space"}
    
    for legacy in expected_legacy:
        if legacy in env_contents:
            readme_path = os.path.join(env_dir, legacy, "README.md")
            if not os.path.exists(readme_path):
                fail(f"Missing README.md in ENVIRONMENTS/{legacy}")

    print("✅ All structure checks passed!")
    print(f"   Found {len(required_digital_contexts)} digital contexts")
    print(f"   Found {len(required_physical_contexts)} physical contexts")
    print(f"   Found {len([d for d in env_contents if d.startswith('LEGACY_')])} legacy directories")

if __name__ == "__main__":
    main()