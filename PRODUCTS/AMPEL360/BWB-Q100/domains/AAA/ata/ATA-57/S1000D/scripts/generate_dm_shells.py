#!/usr/bin/env python3
"""Generate Data Module shells from DMRL requirements."""
from pathlib import Path
try:
    import defusedxml.etree.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DMRL = ROOT/"publication_modules/DML-BWQ1-ATA57-00_EN-US.xml"

DM_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<dmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="../../schemas/{schema}">
  <identAndStatusSection>
    <dmAddress>
      <dmIdent>
        <dmCode modelIdentCode="{mic}" systemDiffCode="{sdc}"
                systemCode="{sc}" subSystemCode="{ssc}" subSubSystemCode="{sssc}"
                assyCode="{ac}" disassyCode="{dc}" disassyCodeVariant="{dcv}"
                infoCode="{ic}" infoCodeVariant="{icv}" itemLocationCode="{iloc}"/>
        <language languageIsoCode="{lang}" countryIsoCode="{country}"/>
        <issueInfo issueNumber="001" inWork="01"/>
      </dmIdent>
      <dmAddressItems>
        <issueDate year="2025" month="09" day="22"/>
        <dmTitle><techName>BWB-Q100</techName><infoName>{title}</infoName></dmTitle>
      </dmAddressItems>
    </dmAddress>
    <dmStatus issueType="new">
      <security securityClassification="01"/>
      <dataRestrictions>
        <restrictionInfo>
          <classificationString>INTERNAL–EVIDENCE-REQUIRED</classificationString>
        </restrictionInfo>
      </dataRestrictions>
      <responsiblePartnerCompany>
        <enterpriseName>AMPEL360</enterpriseName>
      </responsiblePartnerCompany>
    </dmStatus>
  </identAndStatusSection>

  <content>
    <description>
      <levelledPara>
        <title>{title}</title>
        <para>TODO: Add content for {comment}</para>
      </levelledPara>
    </description>
  </content>
</dmodule>'''

def main():
    if not DMRL.exists():
        print(f"DMRL not found: {DMRL}")
        return

    dmrl = ET.parse(DMRL).getroot()
    generated = 0

    for req in dmrl.findall(".//dmRequirement"):
        dmCode = req.find("./dmRefIdent/dmCode")
        lang = req.find("./dmRefIdent/language")
        comment = req.find("./reqComment")
        
        if dmCode is None or lang is None:
            continue
            
        # Build filename
        filename = f'DMC-{dmCode.get("modelIdentCode")}-{dmCode.get("systemDiffCode")}-' \
                  f'{dmCode.get("systemCode")}-{dmCode.get("subSystemCode")}-{dmCode.get("subSubSystemCode")}-' \
                  f'{dmCode.get("assyCode")}-{dmCode.get("disassyCode")}{dmCode.get("disassyCodeVariant")}-' \
                  f'{dmCode.get("infoCode")}{dmCode.get("infoCodeVariant")}-{dmCode.get("itemLocationCode")}-' \
                  f'{lang.get("languageIsoCode").upper()}-{lang.get("countryIsoCode").upper()}.xml'

        # Determine bucket and schema based on infoCode
        ic = dmCode.get("infoCode")
        if ic == "022":  # BREX
            bucket = "descriptive"
            schema = "brex.xsd"
        elif ic in ["200", "210", "220", "230", "240", "250", "260", "270", "280", "290"]:
            bucket = "procedural"
            schema = "proced.xsd"
        elif ic in ["500", "510", "520", "530", "540", "550", "560", "570", "580", "590"]:
            bucket = "procedural"
            schema = "proced.xsd"
        elif ic in ["600", "610", "620", "630", "640", "650", "660", "670", "680", "690"]:
            bucket = "procedural"
            schema = "proced.xsd"
        elif ic in ["700", "710", "720", "730", "740", "750", "760", "770", "780", "790"]:
            bucket = "procedural"
            schema = "proced.xsd"
        elif ic in ["420", "421", "422", "423", "424", "425", "426", "427", "428"]:
            bucket = "fault"
            schema = "fault.xsd"
        else:
            bucket = "descriptive"
            schema = "descript.xsd"

        target_dir = ROOT / "data_modules" / bucket
        target_file = target_dir / filename
        
        # Skip if file already exists
        if target_file.exists():
            continue
            
        # Create directory if needed
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate shell
        title = comment.text if comment is not None else f"Data Module {ic}"
        content = DM_TEMPLATE.format(
            schema=schema,
            mic=dmCode.get("modelIdentCode"),
            sdc=dmCode.get("systemDiffCode"),
            sc=dmCode.get("systemCode"),
            ssc=dmCode.get("subSystemCode"),
            sssc=dmCode.get("subSubSystemCode"),
            ac=dmCode.get("assyCode"),
            dc=dmCode.get("disassyCode"),
            dcv=dmCode.get("disassyCodeVariant"),
            ic=dmCode.get("infoCode"),
            icv=dmCode.get("infoCodeVariant"),
            iloc=dmCode.get("itemLocationCode"),
            lang=lang.get("languageIsoCode"),
            country=lang.get("countryIsoCode"),
            title=title,
            comment=comment.text if comment is not None else "No description"
        )
        
        target_file.write_text(content)
        generated += 1

    if generated > 0:
        print(f"Total generated: {generated} DM shells")
    else:
        print("No DM shells needed - all files exist")

if __name__ == "__main__":
    main()