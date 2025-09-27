---
id: ATA-20-40-OV-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-20/20-40_Electrical_Bonding/README.md
llc: SYSTEMS
title: "ATA-20-40: Electrical Bonding / EMI (BWB-Q100)"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "Electrical Systems Team"
licenses:
  docs: "CC-BY-4.0"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
provenance:
  policy_hash: "sha256:TBD"
  model_sha: "sha256:TBD"
  data_manifest_hash: "sha256:TBD"
  operator_id: "UTCS:OP:copilot-gen"
---

# ATA-20-40 — Electrical Bonding / EMI

This module defines structural bonding to ground, lightning/ESD controls, shield terminations, and electromagnetic interference (EMI) protection for the BWB-Q100 airframe.

## 1) Scope & Purpose

Provides standard practices for:
- Structural electrical bonding and grounding systems
- Lightning protection and static discharge controls
- EMI/RFI shielding and shield terminations
- Plasma protection during atmospheric entry
- ESD-safe handling procedures for sensitive components

## 2) Contents & Index

- `./SPM-20-40-0001_PlasmaShieldingBonding.md` — Standard Practice Manual for Plasma/EMI Shielding & Structural Bonding
- `./bonding-maps/` — Electrical bonding diagrams and resistance maps
- `./lightning-protection/` — Lightning strike protection zones and test procedures
- `./emi-testing/` — EMI/RFI test procedures and acceptance criteria

Key artifacts:
- **[SPM-20-40-0001]** [Standard Practice Manual — Plasma/EMI Shielding & Structural Bonding](./SPM-20-40-0001_PlasmaShieldingBonding.md)

## 3) Routing

### 3.1 Upstream (Inputs)
| Source (ID) | Transport | Path/Topic/Endpoint | Format/Schema | Cadence/Trigger | Owner |
|---|---|---|---|---|---|
| AAA/CAX/CAD (Electrical Layout) | PDM-PLM artifact | /pdm/cad/electrical/bonding/ | Wiring Diagrams v1.5 | on-electrical-design | Electrical CAD Team |
| EEE/Systems | PDM-PLM artifact | /pdm/eee/grounding/requirements/ | Grounding Specs v2.0 | on-requirements-update | EEE Team |
| Test/EMI Lab | PDM-PLM artifact | /pdm/test/emi/standards/ | Test Standards v1.2 | on-standard-update | EMI Test Team |

### 3.2 Downstream (Outputs)
| Consumer (ID) | Transport | Path/Topic/Endpoint | Format/Schema | Contract/ICD | Owner |
|---|---|---|---|---|---|
| AAA/ATA/24 (Electrical Power) | PDM-PLM artifact | /pdm/ata/24/bonding/practices/ | Bonding Procedures v1.0 | ICD-AAA-ATA-24-020 | Power Systems Team |
| Manufacturing/Electrical | PDM-PLM artifact | /pdm/mfg/electrical/bonding/ | Work Instructions v1.0 | ICD-MFG-ELECTRICAL | MFG Team |
| Test/Lightning Lab | PDM-PLM artifact | /pdm/test/lightning/procedures/ | Test Procedures v1.0 | ICD-TEST-LIGHTNING | Lightning Test Team |
| QA/Electrical Testing | API | https://qa.api/electrical/bonding | JSON v1.0 | ICD-QA-ELECTRICAL | QA Team |

### 3.3 Cadence & Environments
- **Dev:** file:///dev/ata/20/20-40/ (ad hoc on PR)
- **Stage:** file:///stage/ata/20/20-40/ (daily 02:30 UTC)
- **Prod:** /pdm/ata/20/20-40/ (post-baseline release)

### 3.4 Controls & Reliability
- **Classification:** INTERNAL–EVIDENCE-REQUIRED
- **Access:** PDM role: `AAA.electrical` (read), `EEE.engineers` (write)
- **SLO:** publish ≤ 25 min after EEE approval; **Retries:** 3× exponential
- **Alerts:** #aaa-electrical on failure; **Escalation:** EEE on-call within 20 min
- **Change route:** via EEE approval + CN; MRB for lightning protection changes

### 3.5 Artifacts
- **Schemas/ICDs:** `../contracts/electrical/`
- **Manifests:** `../io/electrical.manifest.yaml`

## 4) Interfaces

**Inputs:** Electrical schematics, grounding requirements, EMI test standards
**Outputs:** Bonding procedures, EMI test criteria, lightning protection maps
**Contracts:** Links to ICD-AAA-ELECTRICAL-020, bonding resistance checks

## 5) Evidence & QA

- QS forms: `FORM-QA-20-40-01` (Bonding/EMI Continuity)
- Hashes/manifests: `electrical-bonding.manifest.json`, SHA256 checksums
- Test/validation reports: Bond resistance measurements, EMI test results, lightning strike test data

## 6) Lifecycle & Ownership

**Status:** Baseline
**Maintainer:** Electrical Systems Team (primary), EMI Test Team (secondary)
**Change policy:** EEE approval required for all changes; link to CN-ELECTRICAL-001

## 7) Cross-References

- Parent module: [ATA-20 Standard Practices](../README.md)
- Related ATA chapters: ATA-24 (Electrical Power), ATA-33 (Lights)
- Electrical specifications: ES-BWB-BONDING-001, ES-BWB-LIGHTNING-001

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*