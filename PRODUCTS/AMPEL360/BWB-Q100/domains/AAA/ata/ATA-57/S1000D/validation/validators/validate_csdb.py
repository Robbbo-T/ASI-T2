#!/usr/bin/env python3
import subprocess, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # .../S1000D
SCHEMAS = ROOT/"schemas"
ERR = 0

def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def check_schema(xml, xsd):
    global ERR
    r = sh("xmllint","--noout","--schema", str(SCHEMAS/xsd), str(xml))
    if r.returncode != 0:
        print(f"::warning file={xml}::Schema validation issue: {xsd}\n{r.stderr}")
        # Only error on CSDB control files, warn on others
        if xml.name.startswith(('csdb_', 'access_control', 'versioning')):
            ERR = 1

def walk_and_validate():
    # CSDB control
    for f,x in [(ROOT/"metadata/csdb_control.xml","csdb.xsd"),
                (ROOT/"metadata/csdb_rules.xml","csdb_rules.xsd"),
                (ROOT/"metadata/access_control.xml","access_control.xsd"),
                (ROOT/"metadata/versioning.xml","versioning.xsd")]:
        if f.exists():
            check_schema(f,x)
    
    # Check for DML file (might be in root or publication_modules)
    dml_files = list(ROOT.glob("DML-BWQ1-*.xml")) + list((ROOT/"publication_modules").glob("DML-BWQ1-*.xml"))
    for dml in dml_files:
        check_schema(dml,"dmrl.xsd")

    # CIR
    for cir in (ROOT/"common_information").rglob("CIR-BWQ1-*.xml"):
        check_schema(cir,"cir.xsd")

    # DMs - use appropriate schema based on infoCode
    for dm in (ROOT/"data_modules").rglob("DMC-BWQ1-*.xml"):
        # Extract infoCode from filename to determine schema
        filename = dm.name
        if "-022A-" in filename:  # BREX
            check_schema(dm,"brex.xsd")
        else:
            # lenient: validate all others against descript.xsd (project stubs)
            check_schema(dm,"descript.xsd")

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