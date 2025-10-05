# S1000D Template Quick Start Guide

## 🚀 Quick Copy-Paste Commands

### 1. Copy Template to New Location

```bash
# Copy entire CSDB structure to your target ATA chapter
cp -r PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-90_S1000D_Template_Example/S1000D/data_modules/manual/57-90-00_template/CSDB \
     /path/to/your/ata/chapter/XX-YY-ZZ_description/
```

### 2. Batch Replace Placeholders

```bash
# Navigate to your new CSDB directory
cd /path/to/your/ata/chapter/XX-YY-ZZ_description/CSDB

# Replace Model Identification Code (MIC)
find . -type f -name "*.xml" -exec sed -i 's/BWQ1/YOUR_MIC/g' {} +

# Replace ATA codes
find . -type f -name "*.xml" -exec sed -i 's/systemCode="57"/systemCode="XX"/g' {} +
find . -type f -name "*.xml" -exec sed -i 's/subSystemCode="9"/subSystemCode="YY"/g' {} +
find . -type f -name "*.xml" -exec sed -i 's/subSubSystemCode="0"/subSubSystemCode="ZZ"/g' {} +

# Replace in filenames
for f in DMC/*BWQ1-A-57-90-00*.xml; do
  mv "$f" "${f//BWQ1/YOUR_MIC}"
done
for f in DMC/*YOUR_MIC-A-57-*.xml; do
  mv "$f" "${f//57-90-00/XX-YY-ZZ}"
done

# Update graphics references
find . -type f -name "*.xml" -exec sed -i 's/57-90-00/XX-YY-ZZ/g' {} +

# Update enterprise code if needed
find . -type f -name "*.xml" -exec sed -i 's/IDEALE\.eu/YOUR_ENTERPRISE/g' {} +
```

## 📋 Placeholder Reference

| Placeholder | Description | Example | Your Value |
|------------|-------------|---------|------------|
| `BWQ1` | Model Identification Code (4 chars) | BWQ1 | _________ |
| `57` | ATA Chapter / System Code | 57 (Wings) | _________ |
| `90` | Sub System Code | 90 (Template) | _________ |
| `00` | Sub-Sub System Code | 00 | _________ |
| `IDEALE.eu` | Enterprise Code | IDEALE.eu | _________ |
| `en` | Language ISO Code | en (English) | _________ |
| `US` | Country ISO Code | US (United States) | _________ |

## 🔧 Customization Checklist

- [ ] Copy CSDB structure to target location
- [ ] Replace MIC (BWQ1) with your model code
- [ ] Replace ATA codes (57-90-00) with your chapter
- [ ] Update enterprise code if needed
- [ ] Rename all files to match new codes
- [ ] Update techName in dmTitle elements
- [ ] Update infoName in dmTitle elements
- [ ] Replace placeholder content with actual technical data
- [ ] Create/replace graphics in GFX/ directory
- [ ] Update figure references (xlink:href)
- [ ] Customize BREX rules if needed
- [ ] Update DMRL with correct DM references
- [ ] Update external schema if used
- [ ] Validate all XML files

## 🎯 Information Code Reference

Common S1000D Information Codes:

| Code | Type | Purpose |
|------|------|---------|
| 010A | Descriptive | Function, interface descriptions |
| 022A | BREX | Business rules exchange |
| 040A | Descriptive | General description |
| 520A | Procedural | Inspection/check/operation |
| 721A | Procedural | Installation/removal |
| 941A | IPD | Illustrated parts data |

## 📝 DMC Naming Pattern

```
DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC>-<DC><DCV>-<IC><ICV>-<ILC>-<LIC>-<CIC>.xml

Example:
DMC-BWQ1-A-57-90-00-00-00A-040A-D-EN-US.xml
    │    │  │  │  │  │  │   │    │  │  │
    │    │  │  │  │  │  │   │    │  │  └─ Country: US
    │    │  │  │  │  │  │   │    │  └──── Language: EN
    │    │  │  │  │  │  │   │    └─────── Item Location: D
    │    │  │  │  │  │  │   └──────────── Info Code: 040A
    │    │  │  │  │  │  └──────────────── Disassembly: 00A
    │    │  │  │  │  └─────────────────── Assembly: 00
    │    │  │  │  └────────────────────── Sub-Sub System: 00
    │    │  │  └───────────────────────── Sub System: 90
    │    │  └──────────────────────────── System: 57
    │    └─────────────────────────────── System Diff: A
    └──────────────────────────────────── Model ID: BWQ1
```

## ✅ Validation Commands

```bash
# Validate XML well-formedness (if xmllint available)
xmllint --noout DMC/*.xml
xmllint --noout BREX/*.xml
xmllint --noout PUB/*.xml

# Python validation alternative
python3 -c "
import xml.etree.ElementTree as ET
import glob
for f in glob.glob('DMC/*.xml'):
    try:
        ET.parse(f)
        print(f'✓ {f}')
    except Exception as e:
        print(f'✗ {f}: {e}')
"

# Validate against S1000D schemas (if available)
xmllint --schema s1000d/descript.xsd --noout DMC/*-040A-*.xml
xmllint --schema s1000d/proced.xsd --noout DMC/*-520A-*.xml
xmllint --schema s1000d/ipd.xsd --noout DMC/*-941A-*.xml
```

## 🔗 Cross-References

### Internal DM References
```xml
<dmRef>
  <dmRefIdent>
    <dmCode modelIdentCode="BWQ1" systemDiffCode="A"
            systemCode="57" subSystemCode="90" subSubSystemCode="0"
            assyCode="00" disassyCode="00" disassyCodeVariant="A"
            infoCode="040" infoCodeVariant="A" itemLocationCode="D"/>
  </dmRefIdent>
</dmRef>
```

### External Schema References
```xml
<externalPubRef id="extSchema01" 
                xlink:href="../SCHEMA/external_schema.json">
  <title>External JSON Schema</title>
</externalPubRef>
```

### Graphic References
```xml
<graphic infoEntityIdent="ICN-BWQ1-57-90-00-001" 
         xlink:href="../GFX/fig_overview.svg" 
         xlink:title="Overview Diagram"/>
```

## 🎨 Graphics Guidelines

1. **Format**: Use SVG for scalability
2. **Location**: Place in GFX/ directory
3. **Naming**: Descriptive names (e.g., `fig_overview.svg`)
4. **ICN**: Assign Info Entity Ident for traceability
   - Format: `ICN-<MIC>-<SC>-<SSC>-<SSSC>-<SeqNo>`
   - Example: `ICN-BWQ1-57-90-00-001`

## 📚 Additional Resources

- **Full README**: See [README.md](./README.md) for complete documentation
- **CSDB README**: See [CSDB/README.md](./S1000D/data_modules/manual/57-90-00_template/CSDB/README.md)
- **S1000D Spec**: http://www.s1000d.org
- **ATA iSpec 2200**: https://www.ata.org/resources/specifications

## 💡 Tips

1. **Start Small**: Begin with the descriptive DM (040A)
2. **Incremental**: Add procedural and IPD DMs as content develops
3. **Validate Often**: Check XML syntax after each change
4. **Version Control**: Use git to track changes
5. **BREX Rules**: Customize validation rules for your project
6. **Graphics**: Create placeholder graphics early, refine later
7. **Cross-refs**: Maintain consistent references between DMs

## ⚠️ Common Pitfalls

- ❌ Forgetting to update DMC codes in filenames AND file content
- ❌ Inconsistent enterprise codes across files
- ❌ Breaking XML well-formedness during manual edits
- ❌ Incorrect xlink:href paths to graphics
- ❌ Missing BREX reference in dmStatus section
- ❌ Inconsistent ATA codes between DMC and content

---

**Need Help?**
Refer to the main [README.md](./README.md) for detailed explanations of each component.
