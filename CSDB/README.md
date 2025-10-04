# Common Source Database (CSDB)

This directory contains S1000D Issue 6.0 compliant data modules for the BWB-Q100 aircraft.

## Directory Structure

```
CSDB/
└── DMC/                    # Data Module Code files
```

## Data Modules

### Forward Spar (57-10-10) with QSS Integration

The following modules document the Forward Spar with integrated Quantum Sensorial Skin (QSS):

#### DMC-BWBQ100-A-57-10-10-00-00A-040A-D-EN-US.xml
**Type:** Descriptive (040A)  
**Title:** Forward Spar (57-10-10) — General Description — Sensor-Integrated (QSS)  
**Scope:** Overall configuration, QSS sensor deployment, materials and layup

Key Features:
- QSS patches at inboard, mid, and outboard stations
- Strain/acoustic/temperature monitoring
- TFA bus integration
- Continuous structural health monitoring

#### DMC-BWBQ100-A-57-10-10-00-00A-520A-D-EN-US.xml
**Type:** Procedural (520A)  
**Title:** Forward Spar (57-10-10) — Inspection — Access, QSS Methods, Intervals  
**Scope:** Inspection procedures incorporating QSS health checks

Key Features:
- QSS diagnostics procedures
- TFA topic connectivity
- General visual inspection
- NDT escalation procedures
- Data persistence with UTCS signatures

#### DMC-BWBQ100-A-57-10-10-00-01A-720A-D-EN-US.xml
**Type:** Procedural (720A)  
**Title:** Forward Spar (57-10-10) — Removal/Installation — Access Panel with QSS Disconnect  
**Scope:** Access panel removal/installation with QSS connector handling

Key Features:
- Panel removal sequence
- QSS connector disconnect/reconnect procedures
- Sealant application
- Fastener torque requirements

#### DMC-BWBQ100-A-57-10-10-00-00A-941A-D-EN-US.xml
**Type:** IPD (941A)  
**Title:** Forward Spar (57-10-10) — Illustrated Parts — QSS Sensor Patch Kit  
**Scope:** Parts catalog for QSS sensor patches and associated materials

Parts Included:
- QSS-FS-INB-01: QSS Patch — Inboard Station
- QSS-FS-MID-01: QSS Patch — Mid Station
- QSS-FS-OUTB-01: QSS Patch — Outboard Station
- QSS-ADH-KIT-A: Adhesive/Primer Set (QSS bonding)

## Model Identification

- **Model Code:** BWBQ100 (Blended Wing Body Q100)
- **Applicability:** APPL-BWBQ100-BASE-0001-9999 (MSN 0001–9999)
- **Organization:** IDEALE.eu (Enterprise Code: IDLEU)

## S1000D Compliance

All modules conform to:
- **Issue:** S1000D Issue 6.0
- **Schema:** XSD (not DTD)
- **Validation:** Against official S1000D 6.0 schemas

## QSS Technology

**QSS (Quantum Sensorial Skin)** is a proprietary structural health monitoring technology developed by IDEALE.eu.

### Features:
- Real-time strain, acoustic, and temperature monitoring
- TFA (Topic-based Field Addressing) bus integration
- UTCS-signature-v2 data provenance per flight
- SHA-256 hash verification
- Multi-station deployment (inboard, mid, outboard)

### TFA Topics:
```
tfa/bwbq100/qs/strain/{FS-INB|FS-MID|FS-OUTB}
tfa/bwbq100/qs/acoustic/{FS-INB|FS-MID|FS-OUTB}
```

## References

- **Layup Schema:** LAYUP-FS-V1 (Forward Spar Layup Schema v1)
- **Standard Practices:** STD-STRUCT-INSPECT, STD-STRUCT-TORQUE
- **Graphics:** FIG-57-10-720-REMOVAL, FIG-57-10-720-INSTALL, FIG-57-10-10-QSS-PATCHES

## Validation

To validate these modules against S1000D 6.0 schemas:

```bash
# Descriptive modules
xmllint --noout --schema http://www.s1000d.org/S1000D_6-0/xml_schema_flat/descriptive.xsd \
  DMC-BWBQ100-A-57-10-10-00-00A-040A-D-EN-US.xml

# Procedural modules
xmllint --noout --schema http://www.s1000d.org/S1000D_6-0/xml_schema_flat/procedural.xsd \
  DMC-BWBQ100-A-57-10-10-00-00A-520A-D-EN-US.xml \
  DMC-BWBQ100-A-57-10-10-00-01A-720A-D-EN-US.xml

# IPD modules
xmllint --noout --schema http://www.s1000d.org/S1000D_6-0/xml_schema_flat/ipd.xsd \
  DMC-BWBQ100-A-57-10-10-00-00A-941A-D-EN-US.xml
```

## Issue

Created for **Issue 6.0** — Integration of QSS technology with Forward Spar documentation

---

*Maintained by IDEALE.eu — Part of ASI-T2 Advanced Systems Integration*
