#!/usr/bin/env python3
import subprocess, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # .../S1000D
SCHEMAS = ROOT/"schemas"
ERR = 0

def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def check_schema(xml, xsd, hard_fail=False):
    global ERR
    r = sh("xmllint","--noout","--schema", str(SCHEMAS/xsd), str(xml))
    if r.returncode != 0:
        level = "error" if hard_fail else "warning"
        print(f"::{level} file={xml}::Schema validation issue ({xsd})\n{r.stderr}")
        if hard_fail:
            ERR = 1

def walk_and_validate():
    # CSDB control (hard fail)
    for f,x in [(ROOT/"metadata/csdb_control.xml","csdb.xsd"),
                (ROOT/"metadata/csdb_rules.xml","csdb_rules.xsd"),
                (ROOT/"metadata/access_control.xml","access_control.xsd"),
                (ROOT/"metadata/versioning.xml","versioning.xsd")]:
        if f.exists():
            check_schema(f,x,hard_fail=True)
    
    # DMRL (warn)
    dmls = list(ROOT.glob("DML-BWQ1-*.xml")) + list((ROOT/"publication_modules").glob("DML-BWQ1-*.xml"))
    for dml in dmls:
        check_schema(dml, "dmrl.xsd", hard_fail=False)

    # CIR (warn)
    for cir in (ROOT/"common_information").rglob("CIR-BWQ1-*.xml"):
        check_schema(cir,"cir.xsd",hard_fail=False)

    # DMs (warn)
    for dm in (ROOT/"data_modules").rglob("DMC-BWQ1-*.xml"):
        filename = dm.name
        if "-022A-" in filename:  # BREX
            check_schema(dm,"brex.xsd",hard_fail=False)
        else:
            # Extract infoCode for bucket-specific validation
            import re
            match = re.search(r'-(\d+)A?-[A-Z]+-[A-Z]+-[A-Z]+\.xml$', filename)
            if match:
                ic = match.group(1)
                if ic in ["200", "210", "220", "230", "240", "250", "260", "270", "280", "290",
                         "500", "510", "520", "530", "540", "550", "560", "570", "580", "590",
                         "600", "610", "620", "630", "640", "650", "660", "670", "680", "690",
                         "700", "710", "720", "730", "740", "750", "760", "770", "780", "790"]:
                    check_schema(dm,"proced.xsd",hard_fail=False)
                elif ic in ["420", "421", "422", "423", "424", "425", "426", "427", "428"]:
                    check_schema(dm,"fault.xsd",hard_fail=False)
                else:
                    check_schema(dm,"descript.xsd",hard_fail=False)
            else:
                check_schema(dm,"descript.xsd",hard_fail=False)

def en_dash_check():
    global ERR
    bad = []
    for md in ROOT.rglob("*.md"):
        txt = md.read_text(errors="ignore")
        if "classification:" in txt:
            for line in txt.splitlines():
                if line.strip().startswith("classification:") and "INTERNAL–EVIDENCE-REQUIRED" not in line:
                    bad.append(str(md))
                    break
    if bad:
        print("::error::CI classification en-dash check failed:", bad)
        ERR = 1

def main():
    walk_and_validate()
    en_dash_check()
    sys.exit(ERR)

if __name__ == "__main__":
    main()