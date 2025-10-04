# Template Substitution Guide

This file lists all placeholders used in the S1000D template and their recommended replacements for creating a new data module package.

## Quick Reference Table

| Current Value | Element/Attribute | Where to Replace | Your Value |
|--------------|-------------------|------------------|------------|
| `BWQ1` | modelIdentCode | All DMC files, BREX, DMRL, filenames | ____________ |
| `57` | systemCode | All DMC files, BREX, DMRL, filenames | ____________ |
| `90` | subSystemCode | All DMC files, BREX, DMRL, filenames | ____________ |
| `00` | subSubSystemCode | All DMC files, BREX, DMRL, filenames | ____________ |
| `IDEALE.eu` | enterpriseCode | responsiblePartnerCompany, originator | ____________ |
| `57-90-00` | Text content | Titles, descriptions, figure labels | ____________ |
| `2025-10-04` | issueDate | All files | ____________ |
| `001` | issueNumber | All files | ____________ |

## Detailed Substitution Instructions

### 1. Model Identification Code (MIC)

**Current:** `BWQ1`  
**Description:** 4-character code identifying the aircraft model  
**Your Value:** `____________`

**Files to Update:**
- All XML files in `DMC/`
- BREX file in `BREX/`
- DMRL file in `PUB/`
- All XML filenames

**Locations in XML:**
```xml
<dmCode modelIdentCode="BWQ1" .../>
```

**Filename pattern:**
```
DMC-BWQ1-A-... → DMC-XXXX-A-...
```

### 2. System Code (ATA Chapter)

**Current:** `57`  
**Description:** ATA chapter number (2 digits)  
**Your Value:** `____________`

**Common ATA Chapters:**
- 04 = Airworthiness Limitations
- 20 = Standard Practices
- 27 = Flight Controls
- 28 = Fuel
- 32 = Landing Gear
- 51 = Structures - General
- 52 = Doors
- 53 = Fuselage
- 54 = Nacelles/Pylons
- 55 = Stabilizers
- 56 = Windows
- 57 = Wings

**Files to Update:**
- All XML files
- All filenames
- Graphics references

**Locations in XML:**
```xml
<dmCode ... systemCode="57" .../>
```

### 3. Sub System Code

**Current:** `90`  
**Description:** Sub-system within the ATA chapter (2 digits)  
**Your Value:** `____________`

**Example for ATA 57 (Wings):**
- 10 = Wing Primary Structure
- 20 = Control Surfaces
- 30 = Joints/Fasteners
- 40 = Access Panels
- 50 = System Provisions
- 90 = Miscellaneous (Template example)

**Files to Update:**
- All XML files
- All filenames

**Locations in XML:**
```xml
<dmCode ... subSystemCode="90" .../>
```

### 4. Sub-Sub System Code

**Current:** `00`  
**Description:** Further subdivision (2 digits)  
**Your Value:** `____________`

**Files to Update:**
- All XML files
- All filenames

**Locations in XML:**
```xml
<dmCode ... subSubSystemCode="00" .../>
```

### 5. Enterprise Code

**Current:** `IDEALE.eu`  
**Description:** Organization identifier  
**Your Value:** `____________`

**Common Formats:**
- Company domain (e.g., IDEALE.eu)
- CAGE code (5 alphanumeric)
- Custom project code

**Files to Update:**
- All XML files in `DMC/`, `BREX/`, `PUB/`

**Locations in XML:**
```xml
<responsiblePartnerCompany enterpriseCode="IDEALE.eu">
  <enterpriseName>IDEALE.eu</enterpriseName>
</responsiblePartnerCompany>
<originator enterpriseCode="IDEALE.eu">
  <enterpriseName>IDEALE.eu</enterpriseName>
</originator>
```

### 6. Language and Country Codes

**Current:** `en` / `US`  
**Description:** ISO language and country codes  
**Your Values:** `______` / `______`

**Common Combinations:**
- en-US (English - United States)
- en-GB (English - United Kingdom)
- fr-FR (French - France)
- de-DE (German - Germany)
- es-ES (Spanish - Spain)

**Files to Update:**
- All XML files
- All filenames

**Locations in XML:**
```xml
<language languageIsoCode="en" countryIsoCode="US"/>
```

**Filename pattern:**
```
...-EN-US.xml → ...-XX-YY.xml
```

### 7. Issue Date and Number

**Current:** `2025-10-04` / `001`  
**Description:** Publication date and issue number  
**Your Values:** `__________` / `______`

**Files to Update:**
- All XML files

**Locations in XML:**
```xml
<issueInfo issueNumber="001" inWork="00">
  <issueDate year="2025" month="10" day="04"/>
</issueInfo>
```

### 8. Descriptive Text Content

**Current:** `57-90-00 Template Example`  
**Description:** Human-readable titles and descriptions  
**Your Value:** `________________________________`

**Files to Update:**
- All XML files in `DMC/`
- README files
- Graphics

**Locations in XML:**
```xml
<dmTitle>
  <techName>57-90-00 Template Example</techName>
  <infoName>General Description &amp; Architecture</infoName>
</dmTitle>
```

### 9. Graphics References

**Current:** 
- `fig_overview.svg`
- `ipd_exploded.svg`
- `ICN-BWQ1-57-90-00-001`

**Your Values:**
- `________________________.svg`
- `________________________.svg`
- `ICN-____-__-__-__-___`

**Files to Update:**
- Graphics in `GFX/`
- References in XML files

**Locations in XML:**
```xml
<graphic infoEntityIdent="ICN-BWQ1-57-90-00-001" 
         xlink:href="../GFX/fig_overview.svg" 
         xlink:title="Overview Diagram"/>
```

## Automated Substitution Script

Save this as `substitute.sh` and run it in your new CSDB directory:

```bash
#!/bin/bash

# Configuration - EDIT THESE VALUES
NEW_MIC="XXXX"           # Your model code (4 chars)
NEW_SYS="XX"             # Your system code (2 digits)
NEW_SUBSYS="YY"          # Your sub-system code (2 digits)
NEW_SUBSUBSYS="ZZ"       # Your sub-sub-system code (2 digits)
NEW_ENTERPRISE="YOUR_ORG" # Your enterprise code
NEW_LANG="en"            # Language code
NEW_COUNTRY="US"         # Country code
NEW_DATE_Y="2025"        # Issue year
NEW_DATE_M="10"          # Issue month
NEW_DATE_D="04"          # Issue day
NEW_TITLE="Your Component Name"  # Technical name

# Perform substitutions
echo "Performing substitutions..."

# Replace codes in XML files
find . -type f -name "*.xml" -exec sed -i \
  -e "s/BWQ1/${NEW_MIC}/g" \
  -e "s/systemCode=\"57\"/systemCode=\"${NEW_SYS}\"/g" \
  -e "s/subSystemCode=\"90\"/subSystemCode=\"${NEW_SUBSYS}\"/g" \
  -e "s/subSubSystemCode=\"00\"/subSubSystemCode=\"${NEW_SUBSUBSYS}\"/g" \
  -e "s/IDEALE\\.eu/${NEW_ENTERPRISE}/g" \
  -e "s/57-90-00/${NEW_SYS}-${NEW_SUBSYS}-${NEW_SUBSUBSYS}/g" \
  -e "s/year=\"2025\"/year=\"${NEW_DATE_Y}\"/g" \
  -e "s/month=\"10\"/month=\"${NEW_DATE_M}\"/g" \
  -e "s/day=\"04\"/day=\"${NEW_DATE_D}\"/g" \
  {} +

# Rename files
cd DMC
for f in *BWQ1-A-57-90-0*.xml; do
  new_name=$(echo "$f" | sed "s/BWQ1/${NEW_MIC}/g" | sed "s/57-90-0/${NEW_SYS}-${NEW_SUBSYS}-${NEW_SUBSUBSYS}/g")
  mv "$f" "$new_name"
  echo "Renamed: $f -> $new_name"
done
cd ..

cd BREX
for f in *BWQ1-A-57-90-0*.xml; do
  new_name=$(echo "$f" | sed "s/BWQ1/${NEW_MIC}/g" | sed "s/57-90-0/${NEW_SYS}-${NEW_SUBSYS}-${NEW_SUBSUBSYS}/g")
  mv "$f" "$new_name"
  echo "Renamed: $f -> $new_name"
done
cd ..

cd PUB
for f in *BWQ1-A-57-90-00*.xml; do
  new_name=$(echo "$f" | sed "s/BWQ1/${NEW_MIC}/g" | sed "s/57-90-00/${NEW_SYS}-${NEW_SUBSYS}-${NEW_SUBSUBSYS}/g")
  mv "$f" "$new_name"
  echo "Renamed: $f -> $new_name"
done
cd ..

echo "✅ Substitution complete!"
echo "⚠️  Remember to:"
echo "   1. Update techName in dmTitle elements"
echo "   2. Replace placeholder content"
echo "   3. Update/replace graphics"
echo "   4. Validate XML files"
```

## Validation Checklist

After substitution, verify:

- [ ] All DMC codes updated in XML content
- [ ] All filenames updated
- [ ] Enterprise code consistent across all files
- [ ] Language/country codes updated
- [ ] Issue date updated
- [ ] techName and infoName updated
- [ ] Graphics references point to correct files
- [ ] BREX dmRef codes match
- [ ] DMRL references are correct
- [ ] XML files are still well-formed
- [ ] External schema references updated (if used)

## Testing Your Changes

```bash
# Test XML syntax
python3 -c "
import xml.etree.ElementTree as ET
import glob
for f in glob.glob('**/*.xml', recursive=True):
    try:
        ET.parse(f)
        print(f'✓ {f}')
    except Exception as e:
        print(f'✗ {f}: {e}')
"

# Check for remaining placeholders
grep -r "BWQ1" . --include="*.xml" || echo "✓ No BWQ1 found"
grep -r "57-90-00" . --include="*.xml" || echo "✓ No 57-90-00 found"
grep -r "IDEALE.eu" . --include="*.xml" || echo "✓ No IDEALE.eu found (if changed)"
```

---

**Questions or Issues?**  
Refer to the main [README.md](./README.md) or [QUICKSTART.md](./QUICKSTART.md) for more details.
