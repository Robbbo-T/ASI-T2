---
id: ASIT2-APLUS-AAA-ATA20-INDEX
project: ASI-T2
artifact: ATA-20 Standard Practices — Airframe (PLUS)
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: 2025-09-27
maintainer: AAA (Airframes) · PLUS Line
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
canonical_hash: pending
---

# ATA-20 — Standard Practices (Airframe) · AMPEL360 PLUS

Authoritative practices for the airframe: fasteners & torque, sealants/adhesives, corrosion control, bonding/grounding.  
This index maps the **S1000D** structure and links to each Data Module (DM).

## Structure
- [`S1000D/brex/`](./S1000D/brex/) — Project BREX (rules)
- [`S1000D/dmrl/`](./S1000D/dmrl/) — DMRL (requirements)
- [`S1000D/data_modules/descriptive/`](./S1000D/data_modules/descriptive/) — Descriptive DMs

## Data Modules (DMs)
- **Overview** — [`DMC-PLS1-A-20-00-00-00A-040A-D-EN-US.xml`](./S1000D/data_modules/descriptive/DMC-PLS1-A-20-00-00-00A-040A-D-EN-US.xml)
- **Fasteners & Torque Standards** — [`DMC-PLS1-A-20-10-00-00A-040A-D-EN-US.xml`](./S1000D/data_modules/descriptive/DMC-PLS1-A-20-10-00-00A-040A-D-EN-US.xml)
- **Sealants & Adhesives Practices** — [`DMC-PLS1-A-20-20-00-00A-040A-D-EN-US.xml`](./S1000D/data_modules/descriptive/DMC-PLS1-A-20-20-00-00A-040A-D-EN-US.xml)
- **Corrosion Prevention & Control** — [`DMC-PLS1-A-20-30-00-00A-040A-D-EN-US.xml`](./S1000D/data_modules/descriptive/DMC-PLS1-A-20-30-00-00A-040A-D-EN-US.xml)
- **Bonding & Grounding Essentials** — [`DMC-PLS1-A-20-40-00-00A-040A-D-EN-US.xml`](./S1000D/data_modules/descriptive/DMC-PLS1-A-20-40-00-00A-040A-D-EN-US.xml)

## Cross-Reference Policy
*ATA-20 is practices-only.* When practices apply to specific systems (e.g., flight controls ATA-27), reference the target DM—do **not** duplicate content here.

## Quality & Evidence
- UTCS/QS: every DM must carry `canonical_hash` on release.
- SBOM & signatures: if any binaries/scripts are attached, include CycloneDX/SPDX and cosign attestations.