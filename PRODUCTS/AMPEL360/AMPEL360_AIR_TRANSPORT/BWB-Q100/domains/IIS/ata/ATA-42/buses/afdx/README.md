# AFDX Bus Configuration — ATA-42 IMA

**Parent:** [../../README.md](../../README.md)  
**Related:** [../a429/](../a429/)

## Purpose

AFDX (ARINC 664 Part 7) Virtual Link definitions, bandwidth allocation, and network configuration for the BWB-Q100 IMA system.

## Contents

- **`vl_table.csv`** — Virtual Link table with complete configuration
- **`network_topology.md`** *(planned)* — Physical network layout, switch configuration, redundancy
- **`policing_rules.md`** *(planned)* — BAG enforcement, bandwidth allocation group details

## Key Files

| File | Description | Status |
|------|-------------|--------|
| `vl_table.csv` | AFDX VL configuration (13 columns: VL_ID, Source, Sinks, TrafficClass, BAG, etc.) | ✅ Active |

## Virtual Link Summary

Current VL allocations (see `vl_table.csv` for complete details):

- **VL-FBW-CMD** (P-FBW → Actuation_GW): 2ms BAG, 1024 kbps, Class A, Dual redundancy
- **VL-NAV-ATT** (P-NAV → P-FBW/P-DISP): 8ms BAG, 512 kbps, Class A, Dual redundancy  
- **VL-MAINT-LOG** (P-MAINT → Recorder): 128ms BAG, 94 kbps, Class B, Single network

**Total bandwidth:** ~1.6 kbps per network (1.6% utilization of 100 Mbps link)

## Standards

- **ARINC 664 Part 7** — Aircraft Data Network, Full Duplex Switched Ethernet (AFDX)
- **Link speed:** 100 Mbps (full duplex)
- **BAG values:** {1, 2, 4, 8, 16, 32, 64, 128} ms
- **Traffic classes:** A (1-8ms), B (16-128ms)
- **Frame size:** 64-1518 bytes (L2 including headers/FCS)

## Validation

AFDX configuration validated by `../../tools/ci/validate_afdx.py`:
- BAG compliance
- Bandwidth calculations
- Link utilization (warning at 75%, error at 100%)

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial AFDX directory README |
