#!/usr/bin/env python3
from pathlib import Path
try:
    import defusedxml.etree.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import json

ROOT = Path(__file__).resolve().parents[2]
DMRL = ROOT/"publication_modules/DML-BWQ1-ATA57-00_EN-US.xml"
IDX_XML = ROOT/"indices/dm_index.xml"
XREF_XML = ROOT/"indices/xref_index.xml"
SEARCH_JSON = ROOT/"indices/search.json"

def main():
    ROOT.joinpath("indices").mkdir(exist_ok=True)
    dm_index = ET.Element("dmIndex")
    
    # Build from DMRL: source of truth
    if DMRL.exists():
        dmrl = defusedxml.etree.ElementTree.parse(DMRL).getroot()
        for req in dmrl.findall(".//dmRequirement"):
            dmCode = req.find("./dmRefIdent/dmCode")
            lang = req.find("./dmRefIdent/language")
            if dmCode is None or lang is None: 
                continue
            fn = f'DMC-{dmCode.get("modelIdentCode")}-{dmCode.get("systemDiffCode")}-' \
                 f'{dmCode.get("systemCode")}-{dmCode.get("subSystemCode")}-{dmCode.get("subSubSystemCode")}-' \
                 f'{dmCode.get("assyCode")}-{dmCode.get("disassyCode")}{dmCode.get("disassyCodeVariant")}-' \
                 f'{dmCode.get("infoCode")}{dmCode.get("infoCodeVariant")}-{dmCode.get("itemLocationCode")}-' \
                 f'{lang.get("languageIsoCode").upper()}-{lang.get("countryIsoCode").upper()}.xml'
            path = None
            for bucket in ("descriptive","procedural","fault","ipd"):
                p = ROOT/"data_modules"/bucket/fn
                if p.exists(): 
                    path = p
                    break
            e = ET.SubElement(dm_index,"dm", {
                "key": fn.replace(".xml",""),
                "path": str(path.relative_to(ROOT)) if path else "MISSING",
                "ic": dmCode.get("infoCode"),
                "bucket": ("unknown" if path is None else path.parts[-2])
            })
    
    ET.ElementTree(dm_index).write(IDX_XML, encoding="utf-8", xml_declaration=True)

    # skeleton xrefs & search (authors can enrich later)
    ET.ElementTree(ET.Element("xrefs")).write(XREF_XML, encoding="utf-8", xml_declaration=True)
    SEARCH_JSON.write_text(json.dumps({"tokens":{}}, indent=2))
    print("Generated dm_index.xml, xref_index.xml, search.json")

if __name__ == "__main__":
    main()