# -*- coding: utf-8 -*-
import subprocess, sys, pathlib, shutil

DOM_ROOT = pathlib.Path(__file__).resolve().parents[1]
LINTER = DOM_ROOT / "policy" / "lints" / "lint_names.py"

def run_linter(target):
    p = subprocess.run([sys.executable, str(LINTER), str(target)], capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr

def test_ok_plm():
    sb = DOM_ROOT / "tests" / "sandbox_ok_plm"; 
    if sb.exists(): shutil.rmtree(sb)
    (sb / "PLM" / "CAD").mkdir(parents=True)
    f = sb / "PLM" / "CAD" / "ASSY-BWQ1-CAD5710-FWD-SPAR-GA-r012.step"; f.write_text("")
    code, out, err = run_linter(sb); assert code == 0, (out, err)

def test_ok_qoa():
    sb = DOM_ROOT / "tests" / "sandbox_ok_qoa"; 
    if sb.exists(): shutil.rmtree(sb)
    (sb / "QUANTUM_OA" / "MILP").mkdir(parents=True)
    f = sb / "QUANTUM_OA" / "MILP" / "MILP-BWQ1-QOA5710-FWD-SPAR-OPT-DEV-r001.lp"; f.write_text("")
    code, out, err = run_linter(sb); assert code == 0, (out, err)

def test_ok_pax():
    sb = DOM_ROOT / "tests" / "sandbox_ok_pax"; 
    if sb.exists(): shutil.rmtree(sb)
    (sb / "PAx").mkdir(parents=True)
    f = sb / "PAx" / "PAX-BWQ1-PKG5710-FWD-SPAR-DOCS-r001.zip"; f.write_text("")
    code, out, err = run_linter(sb); assert code == 0, (out, err)

def test_fail_ata_long():
    sb = DOM_ROOT / "tests" / "sandbox_fail_ata"; 
    if sb.exists(): shutil.rmtree(sb)
    (sb / "PLM" / "CAD").mkdir(parents=True)
    f = sb / "PLM" / "CAD" / "ASSY-BWQ1-CAD571010-FWD-SPAR-GA-r012.step"; f.write_text("")
    code, out, err = run_linter(sb); assert code != 0
