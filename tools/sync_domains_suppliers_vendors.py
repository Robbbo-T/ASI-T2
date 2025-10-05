#!/usr/bin/env python3
"""
Scaffold Supplier/Services and Vendors/Components domain trees.

Discovers unique domain codes from PRODUCTS/**/domains/* (any depth 1-3)
and creates standard folder structure for supplier/vendor alignment.

Idempotent: safe to re-run; only adds missing folders and .gitkeep files.
"""
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]

# Where to discover domains from product roots
PRODUCT_DOMAIN_GLOBS = [
    "PRODUCTS/*/*/*/domains/*",
    "PRODUCTS/*/*/domains/*",
    "PRODUCTS/*/domains/*",
]

# Targets to scaffold
TARGETS = [
    REPO / "Supplier" / "Services" / "domains",
    REPO / "Vendors" / "Components" / "domains",
]

# Standard subtrees
PLM_SUB = ["CAO", "CAD", "CAE", "CAM", "CAV", "CAI", "CAS", "CAP", "CMP"]
QOA_SUB = ["QOX", "MILP", "LP", "QP", "QUBO", "QAOA", "SA", "GA"]
TOPS = ["DELs", "PAx", "PLM", "QUANTUM_OA", "policy", "tests"]

README_STUB = """# {code} — Domain

This directory mirrors the **{code}** domain for {scope} alignment.

- **Source of truth (product roots):** see `PRODUCTS/**/domains/{code}/`
- **Structure here:** DELs, PAx, PLM, QUANTUM_OA, policy, tests
- **IEF/UTCS:** evidence lives with artifacts; link SBOMs from `sbom/` when packaging
"""

def discover_domain_codes():
    """Discover unique domain codes from product roots."""
    codes = set()
    for pat in PRODUCT_DOMAIN_GLOBS:
        for p in REPO.glob(pat):
            if p.is_dir():
                codes.add(p.name)
    return sorted(codes)

def ensure_dir(d: Path):
    """Create directory and add .gitkeep file."""
    d.mkdir(parents=True, exist_ok=True)
    (d / ".gitkeep").write_text("", encoding="utf-8")

def scaffold_for_code(root: Path, code: str, scope_label: str):
    """Create standard structure for a single domain code."""
    base = root / code
    # top-level bins
    for t in TOPS:
        ensure_dir(base / t)
    # PLM detail
    for s in PLM_SUB:
        ensure_dir(base / "PLM" / s)
    # QUANTUM_OA detail
    for s in QOA_SUB:
        ensure_dir(base / "QUANTUM_OA" / s)
    # README stub once
    readme = base / "README.md"
    if not readme.exists():
        readme.write_text(README_STUB.format(code=code, scope=scope_label), encoding="utf-8")

def main():
    """Main entry point."""
    codes = discover_domain_codes()
    if not codes:
        print("No product domains found under PRODUCTS/**/domains/*", file=sys.stderr)
        return 1

    for tgt in TARGETS:
        tgt.mkdir(parents=True, exist_ok=True)
        scope_label = "Supplier/Services" if "Supplier" in tgt.parts else "Vendors/Components"
        for code in codes:
            scaffold_for_code(tgt, code, scope_label)
    print(f"✓ Scaffolded {len(codes)} domains into Supplier/Services and Vendors/Components.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
