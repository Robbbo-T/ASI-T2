# Quick Reference Guide - CSDB S1000D Issue 6.0 Modules

## Document Quick Reference

| DMC | Type | Info Code | Title | Use When |
|-----|------|-----------|-------|----------|
| DMC-BWBQ100-A-57-10-10-00-00A-040A-D-EN-US | Descriptive | 040A | General Description — Sensor-Integrated (QSS) | Understanding forward spar structure and QSS deployment |
| DMC-BWBQ100-A-57-10-10-00-00A-520A-D-EN-US | Procedural | 520A | Inspection — Access, QSS Methods, Intervals | Performing forward spar inspections with QSS diagnostics |
| DMC-BWBQ100-A-57-10-10-00-01A-720A-D-EN-US | Procedural | 720A | Removal/Installation — Access Panel with QSS Disconnect | Removing or installing access panels with QSS connectors |
| DMC-BWBQ100-A-57-10-10-00-00A-941A-D-EN-US | IPD | 941A | Illustrated Parts — QSS Sensor Patch Kit | Ordering QSS sensor patches and related parts |

## Module Relationships

```
┌─────────────────────────────────────────────────────────────┐
│  DMC-BWBQ100-A-57-10-10-00-00A-040A-D-EN-US                │
│  (General Description)                                       │
│  • Forward spar structure                                    │
│  • QSS sensor locations and specs                           │
│  • Materials and layup overview                             │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ├── Referenced by ──────────────────────────┐
                  │                                            │
                  ▼                                            ▼
┌─────────────────────────────────────────┐  ┌────────────────────────────────────┐
│  DMC-BWBQ100-A-57-10-10-00-00A-520A-D   │  │  DMC-BWBQ100-A-57-10-10-00-01A-720A │
│  (Inspection Procedure)                  │  │  (R/I Procedure)                   │
│  • Access and QSS connection            │  │  • Panel removal sequence          │
│  • Visual inspection                     │  │  • QSS disconnect procedures       │
│  • QSS health check                     │  │  • Installation and torque specs   │
│  • NDT escalation                       │  │                                    │
└──────────────┬──────────────────────────┘  └─────────────────┬──────────────────┘
               │                                                │
               │                                                │
               └─────────────── References ────────────────────┘
                                    │
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  DMC-BWBQ100-A-57-10-10-00-00A-941A-D   │
                  │  (IPD - Parts Catalog)                  │
                  │  • QSS-FS-INB-01 (Inboard patch)       │
                  │  • QSS-FS-MID-01 (Mid patch)           │
                  │  • QSS-FS-OUTB-01 (Outboard patch)     │
                  │  • QSS-ADH-KIT-A (Adhesive kit)        │
                  └─────────────────────────────────────────┘
```

## QSS Sensor Specifications

| Station | Part Number | Monitoring | Frequency | Temperature |
|---------|-------------|------------|-----------|-------------|
| Inboard | QSS-FS-INB-01 | Strain + Acoustic | 500 Hz (2 kHz burst) | Yes |
| Mid | QSS-FS-MID-01 | Strain + Acoustic | 500 Hz | No |
| Outboard | QSS-FS-OUTB-01 | Strain only | 200 Hz | No |

## TFA Topic Structure

```
tfa/bwbq100/qs/strain/
├── FS-INB    # Inboard station strain data
├── FS-MID    # Mid station strain data
└── FS-OUTB   # Outboard station strain data

tfa/bwbq100/qs/acoustic/
├── FS-INB    # Inboard station acoustic data
└── FS-MID    # Mid station acoustic data
```

## Common Tasks

### Performing an Inspection

1. Review **DMC-BWBQ100-A-57-10-10-00-00A-040A-D-EN-US** for QSS location reference
2. Follow **DMC-BWBQ100-A-57-10-10-00-00A-520A-D-EN-US** inspection procedure:
   - Open access using R/I procedure if needed
   - Connect QSS diagnostics to TFA topics
   - Perform visual inspection
   - Execute QSS health check
   - Document results with UTCS signature

### Replacing a QSS Sensor

1. Order parts from **DMC-BWBQ100-A-57-10-10-00-00A-941A-D-EN-US** IPD catalog
2. Use **DMC-BWBQ100-A-57-10-10-00-01A-720A-D-EN-US** to access the sensor:
   - Remove access panel
   - Disconnect QSS connector
3. Follow removal/installation procedures (sensor-specific SRM)
4. Reconnect and verify using inspection procedure
5. Close panel using R/I procedure

### Troubleshooting QSS Anomalies

1. Consult **DMC-BWBQ100-A-57-10-10-00-00A-520A-D-EN-US** for:
   - QSS health check procedure
   - Baseline signature verification
   - Threshold definitions
2. If anomaly confirmed:
   - Perform detailed NDT per inspection DM
   - Document findings
   - Escalate per maintenance program

## External References

### Always Required
- **STD-STRUCT-INSPECT** - Structural Inspection Standard Practices
- **STD-STRUCT-TORQUE** - Fastener Torque and Re-use Standards
- **LAYUP-FS-V1** - Forward Spar Layup Schema v1

### QSS-Specific Documentation
- QSS sensor technical manuals (QSS-FS-INB-01, QSS-FS-MID-01, QSS-FS-OUTB-01)
- TFA bus interface specifications
- UTCS signature requirements

## Graphics Reference

| Figure ID | Title | Used In | Status |
|-----------|-------|---------|--------|
| FIG-57-10-720-REMOVAL | Access Panel Removal Sequence | R/I Procedure | ⚠️ TBD |
| FIG-57-10-720-INSTALL | Access Panel Installation Sequence | R/I Procedure | ⚠️ TBD |
| FIG-57-10-10-QSS-PATCHES | QSS Patch Locations | IPD Catalog | ⚠️ TBD |

## Applicability

- **Product:** BWB Q100 (Blended Wing Body)
- **Model Code:** BWBQ100
- **MSN Range:** 0001-9999
- **Applicability ID:** APPL-BWBQ100-BASE-0001-9999
- **Configuration:** Baseline with QSS integration

## Responsible Organization

- **Name:** IDEALE.eu
- **Enterprise Code:** IDLEU
- **Contact:** [per organization contact procedures]

## Revision Information

- **Issue:** S1000D Issue 6.0
- **Module Issue:** 001-00 (Initial release)
- **Status:** New

## Notes

- All procedures require qualified personnel
- QSS interfaces must be de-energized before access
- Data persistence requires UTCS signature and SHA-256 hash
- Sensor anomalies are maintenance triggers in addition to scheduled intervals

---

*Quick Reference Guide for CSDB S1000D Issue 6.0 Forward Spar QSS Modules*
