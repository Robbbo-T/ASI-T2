# ARINC 429 Bus Configuration — ATA-42 IMA

**Parent:** [../../README.md](../../README.md)  
**Related:** [../afdx/](../afdx/)

## Purpose

ARINC 429 channel definitions, label dictionaries, and interface specifications for the BWB-Q100 IMA system.

## Contents

- **`channel_map.csv`** — Channel assignments (RX/TX), speeds, labels, producer/consumer mappings
- **`label_dict.csv`** *(planned)* — Label definitions (octal notation, parameter descriptions, units)
- **`timing_spec.md`** *(planned)* — Refresh rates, latency requirements, priority

## Key Files

| File | Description | Status |
|------|-------------|--------|
| `channel_map.csv` | ARINC 429 channel configuration with octal labels | ✅ Active |

## Standards

- **ARINC 429** — Mark 33 Digital Information Transfer System (DITS)
- **Speed:** 12.5 kbps (low speed) or 100 kbps (high speed)
- **Word format:** 32-bit, self-clocking, bipolar return-to-zero
- **Labels:** Octal notation (e.g., 203o, 204o)

## Validation

ARINC 429 configuration validated by `../../tools/ci/validate_a429.py` (planned).

---

**Revision History**

| Rev | Date | Author | Notes |
|-----|------|--------|-------|
| 0.1.0 | 2025-09-29 | IIS | Initial ARINC 429 directory README |
