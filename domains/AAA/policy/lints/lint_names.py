#!/usr/bin/env python3
import re, sys, pathlib, os

ATA = "5710"
# Determine enforcement root
if os.getenv("ENFORCED_ROOT"):
    ENFORCED_ROOT = os.getenv("ENFORCED_ROOT")
else:
    # Default: domains/<DDD> (2 parents up from this script)
    ENFORCED_ROOT = str(pathlib.Path(__file__).resolve().parents[2])

DM = re.compile(r'^DMC-[A-Z0-9]{3,4}-[A-Z]-\d{2}-\d{2}-\d{2}-\d{2}-[0-9A-Z]{3}-\d{3}[A-Z]-[A-Z]-[A-Z]{2}-[A-Z]{2}\.xml$')

RE_CAX = re.compile(
  rf'^(ASSY|PRT|DRW|FEM|CFD|MBD|EMI|NC|APT|OPR|FIX|TOOL|SET|QIP|QIF|DMIS|MEAS|MSA|CERT|EPR|RECY|TREAT|DISP|MATREC|CON|REQ|SYS|INS|INT|FIT|AMM|SRM|IPD|EIS|PIPE|JOB|TESTSET|EVID|RPT)-'
  rf'([A-Z0-9]{{3,4}})-(CAO|CAD|CAE|CAM|CAV|CAI|CAS|CAP|CMP)({ATA})-([A-Z0-9-]+)'
  rf'(?:-(LH|RH|CEN))?(?:-([A-Z0-9]{{3,8}}-[A-Z0-9-]+))?(?:-(GA|STAT|UL|FAT|DTA|CERT|VNV|QC|EOL))?(?:-CAP(?:\.[A-Z0-9-]+){{0,2}})?-r(\d{{3}})'
  rf'\.(step|stp|sldprt|sldasm|ipt|iam|dwg|dxf|pdf|inp|cdb|cas|dat|fem|nas|apt|cl|cls|nc|eia|qif|dmis|csv|xml|json|docx|req|sgml|yml|yaml)$'
)

RE_QOA = re.compile(
  rf'^(QOX|QUBO|QAOA|MILP|LP|QP|MINLP|CP|SAT|SA|GA)-([A-Z0-9]{{3,4}})-QOA({ATA})-([A-Z0-9-]+)'
  rf'(?:-(DS|INST|CASE)-[A-Z0-9-]+)?(?:-(DEV|INT|STG|PROD))?-r(\d{{3}})'
  rf'\.(py|ipynb|qasm|json|yaml|yml|csv|lp|mps|qubo|dimacs)$'
)

RE_PAX = re.compile(
  rf'^PAX-([A-Z0-9]{{3,4}})-PKG({ATA})-([A-Z0-9-]+)-(SRC|BIN|DOCS|SBOM|MANIFEST|CHECKLIST|EVIDENCE)-r(\d{{3}})'
  rf'\.(zip|tgz|tar\.gz|json|xml|pdf|txt|csv|spdx\.json)$'
)

RE_DELS = re.compile(
  rf'^(DLV|FC|REL)-([A-Z0-9]{{3,4}})-REL({ATA})-([A-Z0-9-]+)-(PKG|MANIFEST|CSUM|SIG|RPT|NOTES)-r(\d{{3}})'
  rf'\.(zip|json|xml|pdf|txt|sha256|sig)$'
)

def fail(p, msg): print(f"::error file={p}::{msg}")

def ok(name): return print("OK")

def lint_file(p: pathlib.Path) -> bool:
    name = p.name
    # Location
    try:
        p.resolve().relative_to(pathlib.Path(ENFORCED_ROOT).resolve())
    except Exception:
        fail(p, f"Archivo fuera del árbol del dominio: {ENFORCED_ROOT}")
        return False

    # Directory detection
    s = str(p.as_posix())
    if "/PLM/" in s:
        if RE_CAX.match(name) or DM.match(name): return True
        fail(p, "PLM: nombre no conforme a CAx++ / DM"); return False
    if "/QUANTUM_OA/" in s:
        if RE_QOA.match(name): return True
        fail(p, "QUANTUM_OA: nombre no conforme a QOA"); return False
    if "/PAx/" in s:
        if RE_PAX.match(name): return True
        fail(p, "PAx: nombre no conforme a Packaging"); return False
    if "/DELs/" in s:
        if RE_DELS.match(name): return True
        fail(p, "DELs: nombre no conforme a Deliveries"); return False

    # Ignore policy/tests
    if "/policy/" in s or "/tests/" in s: return True

    fail(p, "Ruta no clasificada (esperado PLM/QUANTUM_OA/PAx/DELs)")
    return False

def main(target):
    root = pathlib.Path(target)
    files = [root] if root.is_file() else [f for f in root.rglob('*') if f.is_file()]
    ok_all = True
    for f in files:
        ok_all &= lint_file(f)
    print("OK" if ok_all else "ERR")
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    tgt = sys.argv[1] if len(sys.argv) > 1 else ENFORCED_ROOT
    main(tgt)
