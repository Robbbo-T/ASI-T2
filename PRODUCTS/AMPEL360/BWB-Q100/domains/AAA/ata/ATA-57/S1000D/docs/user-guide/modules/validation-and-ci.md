# Validation and CI

Automated validation ensures S1000D compliance, BREX rule adherence, and content quality through continuous integration processes.

## Validation Pipeline Overview

### CI Workflow Structure
The validation pipeline runs automatically on every commit and pull request:

```yaml
# .github/workflows/qaim_validation.yml (example structure)
name: S1000D Quality Assurance and Integrity Management

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Schema Validation
      - name: BREX Compliance Check
      - name: CSDB Rules Validation
      - name: DMRL Coverage Check
      - name: Cross-Reference Validation
      - name: Index Generation
      - name: DDN Packaging
      - name: Build IETP
```

### Validation Stages
1. **Schema Validation**: XSD compliance for all XML files
2. **BREX Compliance**: Business rules enforcement
3. **CSDB Rules**: Naming conventions and structure validation
4. **Coverage Analysis**: DMRL→DM coverage verification
5. **Cross-Reference Validation**: Link integrity checking
6. **Index Generation**: Automated index updates
7. **Publication Assembly**: DDN package creation

## Schema Validation

### Supported Schemas
**Location**: `schemas/`

#### Core S1000D Schemas
- **descript.xsd**: Descriptive modules (IC 040/042/034/050–056)
- **proced.xsd**: Procedural modules (IC 5xx/6xx/7xx)
- **fault.xsd**: Fault isolation modules (IC 420/421–428)
- **ipd.xsd**: Illustrated parts data (IC 900/910)
- **pm.xsd**: Publication modules
- **brex.xsd**: Business rules exchange
- **cir.xsd**: Common information repository

#### BWQ1-Specific Schemas
- **csdb_bwq1.xsd**: BWQ1 CSDB extensions
- **versioning.xsd**: Version control metadata
- **ddn.xsd**: Delivery data number packaging

### Validation Process
```bash
# Schema validation command
xmllint --noout --schema schemas/descript.xsd \
  data_modules/descriptive/DMC-BWQ1-A-57-10-00-00-00A-040A-D-EN-US.xml

# Batch validation for all modules
find data_modules/ -name "*.xml" -exec \
  python3 scripts/validate_schema.py {} \;
```

### Schema Validation Errors
Common schema validation issues:

#### Missing Required Elements
```xml
<!-- ❌ Missing required issueInfo -->
<dmIdent>
  <dmCode modelIdentCode="BWQ1"/>
  <!-- issueInfo missing -->
</dmIdent>

<!-- ✅ Correct structure -->
<dmIdent>
  <dmCode modelIdentCode="BWQ1"/>
  <language languageIsoCode="en" countryIsoCode="US"/>
  <issueInfo issueNumber="001" inWork="01"/>
</dmIdent>
```

#### Invalid Element Order
```xml
<!-- ❌ Wrong element order -->
<dmAddressItems>
  <dmTitle>Title</dmTitle>
  <issueDate year="2025" month="01" day="21"/>  <!-- Should come first -->
</dmAddressItems>

<!-- ✅ Correct order -->
<dmAddressItems>
  <issueDate year="2025" month="01" day="21"/>
  <dmTitle>Title</dmTitle>
</dmAddressItems>
```

## BREX Compliance Checking

### BREX Rules Source
**File**: `data_modules/descriptive/DMC-BWQ1-*-022A-*-EN-US.xml`

### Enforced BREX Rules

#### Classification String Format
```python
# BREX validation rule
def validate_classification_string(classification):
    # Must use en-dash (–) not hyphen (-)
    if '–' not in classification:
        return False, "Classification must use en-dash (–) not hyphen (-)"
    
    # Must follow format: LEVEL–CATEGORY
    pattern = r'^[A-Z]+–[A-Z\-]+'
    if not re.match(pattern, classification):
        return False, "Invalid classification format"
    
    return True, "Valid"

# Example validation
valid: "INTERNAL–EVIDENCE-REQUIRED"
invalid: "INTERNAL-EVIDENCE-REQUIRED"  # hyphen instead of en-dash
```

#### Enterprise Name Consistency
```python
def validate_enterprise_name(enterprise_name):
    expected = "AMPEL360"
    if enterprise_name != expected:
        return False, f"Enterprise name must be '{expected}', found '{enterprise_name}'"
    return True, "Valid"
```

#### MIC Consistency
```python
def validate_mic(mic):
    expected = "BWQ1"
    if mic != expected:
        return False, f"Model Identification Code must be '{expected}', found '{mic}'"
    return True, "Valid"
```

### BREX Validation Command
```bash
python3 scripts/validate_brex.py \
  --brex data_modules/descriptive/DMC-BWQ1-*-022A-*-EN-US.xml \
  --target data_modules/ \
  --report validation/brex_report.xml
```

## CSDB Rules Validation

### Naming Convention Validation
```python
# DMC naming pattern for BWQ1
DMC_PATTERN = r'^DMC-BWQ1-A-(\d{2})-(\d{2})-(\d{2})-(\d{2})A-(\d{3})A-D-EN-US\.xml$'

def validate_dm_filename(filename, dm_content):
    # Extract DMC from filename
    match = re.match(DMC_PATTERN, filename)
    if not match:
        return False, "Filename doesn't match BWQ1 DMC pattern"
    
    # Validate against content
    content_dmc = extract_dmc_from_xml(dm_content)
    filename_dmc = construct_dmc_from_match(match)
    
    if content_dmc != filename_dmc:
        return False, "Filename DMC doesn't match content DMC"
    
    return True, "Valid"
```

### Directory Structure Validation
```python
def validate_directory_structure():
    expected_buckets = {
        'descriptive': ['040', '042', '034', '050', '051', '052', '053', '054', '055', '056'],
        'procedural': ['5xx', '6xx', '7xx'],  # Expanded to full ranges
        'fault': ['420', '421', '422', '423', '424', '425', '426', '427', '428'],
        'ipd': ['900', '910']
    }
    
    for bucket, valid_ics in expected_buckets.items():
        bucket_path = f"data_modules/{bucket}/"
        for file in os.listdir(bucket_path):
            ic = extract_ic_from_filename(file)
            if ic not in valid_ics:
                return False, f"IC {ic} not valid for bucket {bucket}"
    
    return True, "Valid structure"
```

### CSDB Lint Checks
```bash
# Run CSDB linting
python3 scripts/csdb_lint.py \
  --source data_modules/ \
  --rules metadata/csdb_rules.xml \
  --fix-auto \
  --report validation/csdb_report.xml
```

Common CSDB lint fixes:
- Automatic en-dash insertion in classification strings
- MIC normalization to BWQ1
- Enterprise name standardization
- File naming corrections

## DMRL Coverage Analysis

### Coverage Check Process
```python
def check_dmrl_coverage(dmrl_file, data_modules_dir):
    # Parse DMRL entries
    required_modules = parse_dmrl_required_entries(dmrl_file)
    
    # Scan existing modules
    existing_modules = scan_data_modules(data_modules_dir)
    
    # Generate coverage report
    missing = set(required_modules) - set(existing_modules)
    extra = set(existing_modules) - set(required_modules)
    
    coverage_pct = (len(existing_modules) / len(required_modules)) * 100
    
    return {
        'coverage_percentage': coverage_pct,
        'missing_required': list(missing),
        'extra_modules': list(extra),
        'total_required': len(required_modules),
        'total_existing': len(existing_modules)
    }
```

### Coverage Report Output
```
DMRL Coverage Analysis - ATA-57
===============================
Total Required Modules: 156
Authored Modules: 89
Coverage: 57.1%

Missing Required Modules (67):
  DMC-BWQ1-A-57-10-60-00-00A-040A-D-EN-US
  DMC-BWQ1-A-57-20-70-00-00A-345A-D-EN-US
  DMC-BWQ1-A-57-30-80-00-00A-700A-D-EN-US
  ...

Extra Modules Not in DMRL (3):
  DMC-BWQ1-A-57-99-00-00-00A-040A-D-EN-US (Experimental)
  ...

Recommendations:
- Generate shells for 67 missing required modules
- Review extra modules for DMRL inclusion
- Priority modules: 23 high-priority safety-related procedures
```

### DM Shell Generation
```bash
# Generate shells for missing required modules
python3 scripts/generate_dm_shells.py \
  --dmrl publication_modules/DML-BWQ1-ATA57-00_EN-US.xml \
  --output data_modules/ \
  --missing-only \
  --template-dir templates/
```

## Cross-Reference Validation

### Link Integrity Checking
```python
def validate_cross_references(data_modules_dir):
    broken_refs = []
    
    for dm_file in find_all_dm_files(data_modules_dir):
        dm_content = parse_xml(dm_file)
        
        # Check dmRef elements
        for dmref in dm_content.findall('.//dmRef'):
            target_dmc = extract_dmc_from_dmref(dmref)
            if not module_exists(target_dmc, data_modules_dir):
                broken_refs.append({
                    'source': dm_file,
                    'target': target_dmc,
                    'type': 'dmRef'
                })
        
        # Check internalRef elements (CIR references)
        for intref in dm_content.findall('.//internalRef'):
            target_cir = intref.get('internalRefId')
            if not cir_exists(target_cir):
                broken_refs.append({
                    'source': dm_file,
                    'target': target_cir,
                    'type': 'internalRef'
                })
    
    return broken_refs
```

### Cross-Reference Report
```
Cross-Reference Validation Report
=================================
Total References Checked: 1,247
Valid References: 1,198 (96.1%)
Broken References: 49 (3.9%)

Broken dmRef Links (31):
  Source: DMC-BWQ1-A-57-10-10-00-00A-034A-D-EN-US.xml
  Target: DMC-BWQ1-A-57-10-15-00-00A-500A-D-EN-US.xml (missing)
  
Broken internalRef Links (18):
  Source: DMC-BWQ1-A-57-20-10-00-00A-700A-D-EN-US.xml
  Target: CIR-BWQ1-00004 (missing CIR module)

Recommendations:
- Create missing target modules or remove invalid references
- Verify CIR modules are up to date
- Consider using conditional references for optional content
```

## Index Generation

### Automatic Index Updates
```python
def generate_dm_index(data_modules_dir, output_file):
    index_entries = []
    
    for dm_file in find_all_dm_files(data_modules_dir):
        dm_content = parse_xml(dm_file)
        
        entry = {
            'dmc': extract_dmc(dm_content),
            'title': extract_title(dm_content),
            'path': os.path.relpath(dm_file),
            'issue': extract_issue_info(dm_content),
            'date': extract_issue_date(dm_content),
            'security': extract_security_classification(dm_content)
        }
        index_entries.append(entry)
    
    # Sort by DMC
    index_entries.sort(key=lambda x: x['dmc'])
    
    # Generate XML index
    generate_xml_index(index_entries, output_file)
```

### Index Files Generated
- **dm_index.xml**: Complete data module index
- **multimedia_index.xml**: Multimedia object catalog
- **cir_index.xml**: Common information repository index
- **cross_ref_index.xml**: Cross-reference map

## DDN Packaging

### Delivery Package Creation
```python
def create_ddn_package(source_dir, output_dir, ddn_id):
    package_dir = os.path.join(output_dir, ddn_id)
    
    # Copy content
    copy_data_modules(source_dir, package_dir)
    copy_multimedia(source_dir, package_dir)
    copy_schemas(source_dir, package_dir)
    copy_indices(source_dir, package_dir)
    
    # Generate manifest
    manifest = create_ddn_manifest(package_dir, ddn_id)
    save_manifest(manifest, package_dir)
    
    # Validate package
    validation_report = validate_ddn_package(package_dir)
    save_validation_report(validation_report, package_dir)
    
    # Create archive
    create_ddn_archive(package_dir, f"{ddn_id}.zip")
```

### DDN Validation
```bash
# Validate complete DDN package
python3 scripts/validate_ddn.py \
  --package DDN-BWQ1-ATA57-001-00_EN-US/ \
  --schemas schemas/ \
  --report validation/ddn_validation_report.xml
```

## Performance Optimization

### Parallel Validation
```python
from concurrent.futures import ThreadPoolExecutor

def validate_modules_parallel(module_files, num_threads=4):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(validate_single_module, f) for f in module_files]
        results = [future.result() for future in futures]
    return results
```

### Incremental Validation
```python
def incremental_validation(changed_files):
    # Only validate changed files and their dependencies
    affected_modules = find_affected_modules(changed_files)
    validation_results = validate_modules(affected_modules)
    
    # Update indices only for affected content
    update_indices_incremental(affected_modules)
    
    return validation_results
```

### Caching Strategy
```python
# Cache validation results to avoid re-validation
VALIDATION_CACHE = {}

def cached_validation(module_file):
    file_hash = calculate_file_hash(module_file)
    
    if file_hash in VALIDATION_CACHE:
        return VALIDATION_CACHE[file_hash]
    
    result = perform_validation(module_file)
    VALIDATION_CACHE[file_hash] = result
    return result
```

## Checklist

### CI Pipeline Setup
- [ ] All validation scripts configured and tested
- [ ] Schema files current and accessible
- [ ] BREX rules properly defined and enforced
- [ ] CSDB rules comprehensive and up-to-date
- [ ] Performance optimization implemented

### Validation Quality
- [ ] Schema validation covers all XML content
- [ ] BREX compliance rules match project requirements
- [ ] Cross-reference validation comprehensive
- [ ] DMRL coverage tracking functional
- [ ] Error reporting clear and actionable

### Automation and Integration
- [ ] CI triggers configured for all relevant events
- [ ] Validation reports generated and stored
- [ ] Automatic fixes applied where appropriate
- [ ] Integration with development workflow
- [ ] Performance meets project requirements

## Common Mistakes

❌ **Ignoring Schema Validation**: Allowing invalid XML to pass through CI  
✅ **Correct**: Strict schema validation as first gate in pipeline

❌ **Inconsistent BREX Enforcement**: Rules applied inconsistently across modules  
✅ **Correct**: Automated BREX validation with clear error messages

❌ **Broken Cross-References**: Invalid links between modules  
✅ **Correct**: Comprehensive cross-reference validation and automated fixing

❌ **Outdated Indices**: Stale index files not reflecting current content  
✅ **Correct**: Automatic index regeneration on every content change

❌ **Slow Validation Pipeline**: Validation taking too long and blocking development  
✅ **Correct**: Optimized parallel validation with intelligent caching

---

**Last Updated**: 2025-01-21  
**S1000D Version**: 6.0