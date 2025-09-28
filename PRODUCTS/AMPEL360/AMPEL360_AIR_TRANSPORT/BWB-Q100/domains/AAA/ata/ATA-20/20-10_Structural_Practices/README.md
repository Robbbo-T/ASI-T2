---
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/20/20-10_Structural_Practices/README.md
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: TBD
classification: INTERNAL–EVIDENCE-REQUIRED
configuration: baseline
ethics_guard: MAL-EEM
id: ATA-20-10-OV-0001
licenses:
  docs: CC-BY-4.0
llc: SYSTEMS
maintainer: M&P Engineering Team
project: PRODUCTS/AMPEL360/BWB-Q100
provenance:
  data_manifest_hash: sha256:TBD
  model_sha: sha256:TBD
  operator_id: UTCS:OP:copilot-gen
  policy_hash: sha256:TBD
release_date: 2025-09-24
title: 'ATA-20-10: Structural Practices (BWB-Q100)'
utcs_mi: v5.0
version: 0.1.0
---

# ATA-20-10 — Structural Practices

This module defines mechanical fastening, adhesive bonding, scarf/patch repairs, inserts & potting for sandwich structures in the BWB-Q100 airframe.

## 1) Scope & Purpose

Provides standard practices for:
- Mechanical fastening systems (bolted, riveted, bonded)
- Adhesive bonding processes and controls
- Composite repair techniques (scarf and patch repairs)
- Insert installation and core potting for sandwich structures
- Surface preparation and quality control

## 2) Contents & Index

- `./SPM-20-10-0001_CompositeFastening.md` — Standard Practice Manual for Composite Fastening & Bonding
- `./forms/` — QA forms and inspection records
- `./test-coupons/` — Test specimen data and acceptance criteria
- `./procedures/` — Detailed work instructions

Key artifacts:
- **[SPM-20-10-0001]** [Standard Practice Manual — Composite Fastening & Bonding](./SPM-20-10-0001_CompositeFastening.md)

## 3) Routing

### 3.1 Upstream (Inputs)
| Source (ID) | Transport | Path/Topic/Endpoint | Format/Schema | Cadence/Trigger | Owner |
|---|---|---|---|---|---|
| AAA/CAX/CAD (Fastener Specs) | PDM-PLM artifact | /pdm/cad/fasteners/specs/ | STEP/PDF v2.1 | on-design-release | CAD Team |
| M&P/Materials | PDM-PLM artifact | /pdm/mp/adhesives/specs/ | Material Specs v1.5 | on-material-approval | M&P Team |
| QA/Standards | PDM-PLM artifact | /pdm/qa/structural/standards/ | ASTM/ISO Standards | on-standard-update | QA Team |

### 3.2 Downstream (Outputs)
| Consumer (ID) | Transport | Path/Topic/Endpoint | Format/Schema | Contract/ICD | Owner |
|---|---|---|---|---|---|
| AAA/ATA/51 (Structures) | PDM-PLM artifact | /pdm/ata/51/practices/fastening/ | SPM v1.0 | ICD-AAA-ATA-51-020 | Structures Team |
| AAA/ATA/53 (Fuselage) | PDM-PLM artifact | /pdm/ata/53/practices/fastening/ | SPM v1.0 | ICD-AAA-ATA-53-020 | Fuselage Team |
| Manufacturing/Assembly | PDM-PLM artifact | /pdm/mfg/work-instructions/fastening/ | Work Instructions v1.0 | ICD-MFG-FASTENING | MFG Team |
| QA/Inspection | API | https://qa.api/structural/fastening | JSON v1.0 | ICD-QA-STRUCTURAL | QA Team |

### 3.3 Cadence & Environments
- **Dev:** file:///dev/ata/20/20-10/ (ad hoc on PR)
- **Stage:** file:///stage/ata/20/20-10/ (daily 01:00 UTC)
- **Prod:** /pdm/ata/20/20-10/ (post-baseline release)

### 3.4 Controls & Reliability
- **Classification:** INTERNAL–EVIDENCE-REQUIRED
- **Access:** PDM role: `AAA.structural` (read), `M&P.engineers` (write)
- **SLO:** publish ≤ 15 min after M&P approval; **Retries:** 3× exponential
- **Alerts:** #aaa-structural on failure; **Escalation:** M&P on-call within 10 min
- **Change route:** via M&P approval + CN; MRB for deviations

### 3.5 Artifacts
- **Schemas/ICDs:** `../contracts/structural/`
- **Manifests:** `../io/structural.manifest.yaml`

## 4) Interfaces

**Inputs:** CAD fastener specifications, material data sheets, quality standards
**Outputs:** Work instructions, inspection criteria, QA forms
**Contracts:** Links to ICD-AAA-STRUCTURAL-020, fastener acceptance checks

## 5) Evidence & QA

- QS forms: `FORM-QA-20-10-01` (Composite Fastening), `FORM-QA-20-10-02` (Adhesive Bonding)
- Hashes/manifests: `structural-fastening.manifest.json`, SHA256 checksums
- Test/validation reports: Coupon test data, pull-test results, bond-strength validation

## 6) Lifecycle & Ownership

**Status:** Baseline
**Maintainer:** M&P Engineering Team (primary), Structural Analysis Team (secondary)
**Change policy:** M&P approval required for all changes; link to CN-STRUCTURAL-001

## 7) Cross-References

- Parent module: [ATA-20 Standard Practices](../README.md)
- Related ATA chapters: ATA-51 (Structures), ATA-53 (Fuselage)
- Material specifications: MS-BWB-ADHESIVES-001, MS-BWB-FASTENERS-001

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*