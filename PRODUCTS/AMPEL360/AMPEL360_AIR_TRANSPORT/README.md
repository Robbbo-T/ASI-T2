---
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/README.md
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: TBD
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: AMPEL360-AIR-TRANSPORT-OV-0001
llc: GENESIS
maintainer: Robbbo-T / ASI-T Architecture Team
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/README.md
release_date: 2025-09-24
utcs_mi: v5.0
version: 0.1.0
---

# AMPEL360_AIR_TRANSPORT — Air Transport Products

This subfolder contains all AMPEL360 products designed for air transport operations, including civil aviation aircraft with passenger transport capabilities.

---

## Product Family

- **BWB-Q100** — Blended Wing Body 100-passenger aircraft *(active)*
  Path: `./BWB-Q100/`

---

## Directory Structure

```
AMPEL360_AIR_TRANSPORT/
├── README.md                    # This file (UTCS-headed)
└── BWB-Q100/                    # Baseline passenger configuration
    ├── domains/                 # Engineering domains
    ├── QS/                      # Evidence, signatures, KPIs
    └── ata/                     # S1000D/ATA seeds
```

---

## Scope & Objectives

**Scope:** Air transport AMPEL360 products including commercial passenger aircraft, cargo aircraft, and related air transport systems.

**Objectives:**
- Verifiable sustainability (SIM KPIs) with circularity-by-design
- Certifiable safety & compliance (CS-25 family, ARP4754A/4761)
- Reproducible data flows across **CB→QB→UE→FE→FWD→QS** with UTCS/DET provenance

---

## Quick Navigation

- **BWB-Q100 (Transport Civil × Air)** → `./BWB-Q100/`
  - CAD Wing Baseline (AAA→cax→CAD) → `./BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model/`
  - Master Params → `./BWB-Q100/domains/AAA/cax/CAD/wing_baseline_model/master_model/params.yaml`
  - (Optional) ATA-57 S1000D → `./BWB-Q100/ata/57/`

---

## Changelog

- **0.1.0 — 2025-09-24**  
  Initial AMPEL360_AIR_TRANSPORT subfolder with BWB-Q100 product moved from parent directory.