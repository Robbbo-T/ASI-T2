# ASI-T2 Schematron Validation Rules

This directory contains Schematron rules for validating S1000D Data Modules against ASI-T2 business rules.

## Files

### asi-t2-dmfile.sch

S1000D DMC filename policy and ATA path alignment rules.

**Purpose:**
- Enforce S1000D Issue 5.0/6.0 filename conventions
- Validate ATA chapter structure (especially Chapter 57 - Wings)
- Ensure folder paths align with dmCode metadata
- Verify Model Identification Code (MIC) consistency

**Patterns Validated:**

1. **DMC Filename Convention**
   ```
   DMC-<MIC>-<SDC>-<SC>-<SSC>-<SSSC>-<AC><DAC>-<IC><ICV>-<ILC>-<LANG>-<COUNTRY>.xml
   ```

2. **ATA Path Alignment**
   - Folder path must contain: `<SC>-<SSC>-<SSSC>`
   - Example: `.../57-10-10/DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml`

3. **Chapter 57 Validation**
   - System Code: 57
   - Sub-System Code: 00-99 (e.g., 10 = Wing Structure)
   - Sub-Sub-System Code: 00-99

4. **MIC Consistency**
   - Filename MIC must match `dmCode/@modelIdentCode`

## Integration

### BREX Integration

Wire this Schematron into your BREX (Business Rules Exchange) data module:

```xml
<brex>
  <contexts>
    <context>
      <name>ASI-T2 Filename Policy</name>
      <schematronRef>
        <schematronURI>asi-t2-dmfile.sch</schematronURI>
      </schematronRef>
    </context>
  </contexts>
</brex>
```

### CSDB Validation

Most CSDB systems can validate against Schematron rules during:
- Data module check-in
- Publication assembly
- IETP generation

**Prerequisites:**
- CSDB must support `document-uri()` function
- Or bind physical filename to meta element on ingest

### Command-Line Validation

Using Schematron tools:

```bash
# Using Saxon with Schematron (ISO Schematron)
java -jar saxon.jar -xsl:iso_svrl_for_xslt2.xsl -s:asi-t2-dmfile.sch -o:asi-t2-dmfile.xsl
java -jar saxon.jar -xsl:asi-t2-dmfile.xsl -s:DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml

# Using xmllint (if Schematron support enabled)
xmllint --schematron asi-t2-dmfile.sch DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml
```

## Rule Details

### Pattern: dmc-filename-policy

Validates DMC filename matches S1000D pattern.

**Context:** `/dmodule` or `/s1000d:dmodule`

**Assertion:**
```xpath
matches(document-uri(/),
  'DMC-[A-Z0-9]{3,4}-[A-Z]-\d{2}-\d{2}-\d{2}-\d{2}[A-Z]-\d{3}[A-Z]-[A-Z]-[A-Z]{2}-[A-Z]{2}\.xml$')
```

**Error Message:**
> DMC filename not compliant with S1000D pattern.

### Pattern: dmc-ata-path-alignment

Validates folder path contains ATA structure from dmCode.

**Context:** `dmCode` element

**Variables:**
- `$sc` = `@systemCode`
- `$ssc` = `@subSystemCode`
- `$sssc` = `@subSubSystemCode`

**Assertion:**
```xpath
matches(document-uri(/),
  concat('.*/', $sc, '-', $ssc, '-', $sssc, '/'))
```

**Error Message:**
> Folder ATA path and dmCode mismatch.  
> Expected: 57-10-10

### Pattern: dmc-ata-chapter-57

Validates Chapter 57 (Wings) structure.

**Context:** `dmCode[@systemCode='57']`

**Assertion:**
```xpath
@subSystemCode castable as xs:integer and 
number(@subSystemCode) >= 0 and 
number(@subSystemCode) <= 99
```

**Error Message:**
> ATA Chapter 57 subSystemCode must be a valid 2-digit number (00-99).

### Pattern: dmc-mic-consistency

Validates MIC in filename matches dmCode.

**Context:** `dmCode` element

**Variables:**
- `$mic` = `@modelIdentCode`

**Assertion:**
```xpath
matches(document-uri(/), 
  concat('^.*/DMC-', $mic, '-'))
```

**Error Message:**
> MIC in filename does not match dmCode/@modelIdentCode.

## Customization

### Adding Custom Rules

To add project-specific rules:

1. Create new `<pattern>` in the Schematron file
2. Define `<rule>` with appropriate context
3. Add `<assert>` or `<report>` tests
4. Update this README with rule documentation

Example:
```xml
<pattern id="custom-security-check">
  <title>Ensure classification marking present</title>
  <rule context="/dmodule/identAndStatusSection/dmAddress/dmIdent">
    <assert test="security/@securityClassification">
      Security classification is mandatory for ASI-T2.
    </assert>
  </rule>
</pattern>
```

### Adapting for document-uri() Alternatives

If your CSDB doesn't support `document-uri()`, bind filename to metadata:

```xml
<!-- In your CSDB ingest pipeline, add: -->
<dmAddress>
  <dmIdent>
    <dmCode .../>
    <!-- Add custom meta element -->
    <physicalFilename>DMC-BWQ1-A-57-10-10-00A-040A-D-EN-US.xml</physicalFilename>
  </dmIdent>
</dmAddress>
```

Then adapt the Schematron:
```xml
<assert test="matches(//physicalFilename,
  'DMC-[A-Z0-9]{3,4}-[A-Z]-\d{2}-\d{2}-\d{2}-\d{2}[A-Z]-\d{3}[A-Z]-[A-Z]-[A-Z]{2}-[A-Z]{2}\.xml$')">
  ...
</assert>
```

## Testing

Test your Schematron rules:

```bash
# 1. Create test DM with known violations
# 2. Run Schematron validation
# 3. Verify expected errors appear
```

Example test DMs:
- `DMC-WRONG-A-57-10-10-00A-040A-D-EN-US.xml` (wrong MIC)
- `DMC-BWQ1-A-99-10-10-00A-040A-D-EN-US.xml` (invalid ATA chapter)
- File in wrong folder path

## Related Tools

- [../tools/lint_names.py](../tools/lint_names.py) - Python linter for pre-commit/CI
- [../.github/workflows/filename-policy.yml](../.github/workflows/filename-policy.yml) - GitHub Actions workflow
- [../scripts/migrate_ata_shortcode.py](../scripts/migrate_ata_shortcode.py) - Migration tool

## References

- [ISO/IEC 19757-3:2020](https://www.iso.org/standard/74515.html) - Schematron
- [S1000D Issue 5.0/6.0](http://www.s1000d.org/) - Business Rules Exchange (BREX)
- [Schematron Tutorials](http://schematron.com/)

---

**Version:** 1.0.0  
**Maintainer:** ASI-T Architecture Team  
**Last Updated:** 2025-10-04
