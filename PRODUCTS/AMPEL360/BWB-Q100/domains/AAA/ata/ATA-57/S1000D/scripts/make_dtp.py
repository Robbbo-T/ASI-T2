#!/usr/bin/env python3
import zipfile, datetime
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT/"exchange/packages"

def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    name = f"BWQ1_ATA57_{ts}.zip"
    pkg = OUTDIR/name

    # Collect: PM, DMRL, all DMs present in dm_index.xml
    dm_index_path = ROOT/"indices/dm_index.xml" 
    items = []
    
    # Add DMRL - check multiple possible locations
    dmrl_candidates = [ROOT/"DML-BWQ1-ATA57-00.xml", ROOT/"publication_modules/DML-BWQ1-ATA57-00_EN-US.xml"]
    for dmrl in dmrl_candidates:
        if dmrl.exists():
            items.append(dmrl)
            break
    
    # Add PMs from publication_modules
    for pm in (ROOT/"publication_modules").glob("PMC-*.xml"):
        items.append(pm)
    
    # Add DMs if index exists
    if dm_index_path.exists():
        dm_index = ET.parse(dm_index_path).getroot()
        for dm in dm_index.findall("./dm"):
            p = dm.get("path")
            if p and p != "MISSING":
                items.append(ROOT/p)

    # Write DDN
    ddn = ET.Element("ddn")
    ET.SubElement(ddn,"packageId").text = name
    ET.SubElement(ddn,"sender").text = "AMPEL360/AAA/ATA-57"
    ET.SubElement(ddn,"recipient").text = "External-Consumer"
    ET.SubElement(ddn,"created").text = ts
    items_e = ET.SubElement(ddn,"items")
    for i in items:
        if i.exists():
            ET.SubElement(items_e,"item", {"path": str(i.relative_to(ROOT))})
    ddn_xml = ROOT/"exchange/outgoing/DDN.xml"
    ddn_xml.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(ddn).write(ddn_xml, encoding="utf-8", xml_declaration=True)

    # Zip
    with zipfile.ZipFile(pkg, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(ddn_xml, arcname="DDN.xml")
        for i in items:
            if i.exists():
                z.write(i, arcname=str(i.relative_to(ROOT)))
    print(f"Package created: {pkg}")

if __name__ == "__main__":
    main()