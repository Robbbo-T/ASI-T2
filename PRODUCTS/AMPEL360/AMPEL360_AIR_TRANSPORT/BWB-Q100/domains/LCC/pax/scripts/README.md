---
id: LCC-PAX-SCRIPTS-OV-0001
project: AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/LCC/pax/scripts/README.md
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: "2025-01-22"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# LCC PAx Validation Scripts

This directory contains validation scripts for PAx (Packaging & Applications) manifests in the LCC domain, with BWB-Q100 autopilot-specific validations and evidence requirements.

## Purpose

Provides LCC domain-specific validation tools for:

- **BWB autopilot compliance** - 35-surface coordination and control law validation
- **ARINC-653 requirements** - DAL A partition and timing constraint verification
- **Evidence validation** - MC/DC coverage, HIL testing, and QB advisory metrics
- **CI/CD integration** - Automated gate enforcement with structured error reporting

## Scripts

### `validate_pax.py`
**LCC Domain PAx Validator**

Enhanced validation for LCC domain manifests with BWB-Q100 autopilot-specific checks.

#### Features
- **Schema Validation**: JSON Schema Draft 2020-12 with LCC extensions
- **BWB Validation**: 35-surface count, QAFbW control law, DAL A requirements
- **Evidence Checking**: UTCS canonical hash, MC/DC coverage, HIL run counts
- **Health Monitoring**: ATA22HealthMonitor integration with autopilot-specific KPIs
- **Safety Compliance**: Cross-axis coupling, deadline misses, and QB advisory validation

#### BWB-Specific Validations
- Surface count validation (must be 35 for BWB-Q100)
- QAFbW control law verification
- DAL A partition compliance
- MC/DC coverage = 1.0 enforcement
- Deadline misses = 0 requirement
- Cross-axis coupling ≤ 0.15 limit

#### ATA22HealthMonitor Class
Integrated AQUA OS validator for autopilot health monitoring:
```python
checks = {
    'control_surface_sync': max_skew_ms() <= 5,
    'sensor_redundancy': voter_ok(),
    'actuator_response': lag_ok_us(),
    'span_load_distribution': span_load_err() <= 0.05,
    'elevon_coupling': cross_coupling_ratio() <= 0.15
}
```

#### Usage
```bash
# Validate single manifest
python validate_pax.py manifest.json

# Validate directory tree
python validate_pax.py --root domains/LCC/pax

# With schema validation
python validate_pax.py --schema package.schema.json manifest.yaml
```

#### Environment Variables
- `PAX_STRICT_FILES=1` - Fail on missing file references (CI mode)

## Integration

Scripts integrate with:
- **CI/CD Pipeline** - `.github/workflows/lcc_qafbw_gate.yml`
- **AQUA OS** - ATA22HealthMonitor class for health aggregation
- **TFA Gates** - Evidence validation for CB→QB→UE→FE→FWD→QS bridge
- **Schedulability Validation** - Cross-validation with CAST-32A timing analysis

## Error Reporting

Provides structured output for:
- Schema validation failures with field-specific errors
- BWB-specific compliance violations
- Evidence chain validation issues
- File reference and dependency problems

---

*LCC domain PAx validation with BWB-Q100 autopilot compliance*