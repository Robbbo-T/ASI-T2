---
id: ATA-57-OV-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/README.md
llc: SYSTEMS
title: "ATA-57: Wings — BWB-Q100 (AAA Domain)"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "ASI-T Architecture Team"
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

# ATA-57 — Wings (BWB-Q100)

ATA-57 defines the **authoritative knowledge** for BWB-Q100 wings and integrated lifting surfaces.  
**Golden rule:** knowledge lives in **ATA**; compute lives in **CAX/QOX**; deployables live in **PAX**.

- **CAX (design/analysis):** [`../../cax/`](../../cax/)
- **QOX (optimization):** [`../../qox/`](../../qox/)
- **PAX (packages):** [`../../pax/`](../../pax/)

> **Pattern compliance:** S1000D structures (**BREX/DMRL/DMC/ICN**) are **inside each 4-digit subchapter** (e.g., `57-10_.../S1000D/`), not at the chapter root.

---

## 1) Scope & Applicability

- **Includes:** Wingbox (skins/spars/ribs), control surfaces (elevons/flaperons/spoilers), joints/attachments, fairings and access panels, structural provisions for routed systems, lightning/ESD **structural bonds**, pressurization interfaces on structure.
- **Excludes:** Functional system behavior (ATA-22/27/28), propulsion (ATA-72/PPP). Structural **provisions** for these systems are covered here.
- **Dependencies:** **ATA-20** (Standard Practices) and structural chapters (ATA-51/53/55) as applicable.

---

## 2) Directory Layout (ATA pattern)

```
ATA-57/
├── 57-00_General/
│   ├── S1000D/           # BREX/DMRL/DMC/ICN under the 4-digit folder
│   ├── compliance/
│   ├── icd/
│   └── evidence/
├── 57-10_Wing_Primary_Structure/
│   ├── S1000D/
│   ├── compliance/
│   ├── icd/
│   └── evidence/
├── 57-20_Control_Surfaces/
│   ├── S1000D/
│   ├── compliance/
│   ├── icd/
│   └── evidence/
├── 57-30_Joints_Fasteners_Bonding/
│   ├── S1000D/
│   ├── compliance/
│   ├── icd/
│   └── evidence/
├── 57-40_Access_Panels_Fairings/
│   ├── S1000D/
│   ├── compliance/
│   ├── icd/
│   └── evidence/
├── 57-50_Systems_Provisions_Interfaces/
│   ├── S1000D/
│   ├── compliance/
│   ├── icd/
│   └── evidence/
├── 57-90_Repairs_Alterations/
│   ├── S1000D/
│   ├── compliance/
│   ├── icd/
│   └── evidence/
├── contracts/             # schemas, ICDs, templates shared by 57-xx
├── io/                    # routing manifests, CI I/O snapshots
└── README.md              # this file
```

**Notes**
- Put **S1000D** only **below the 4-digit level** (`57-xx_*`), not at root.
- CI-generated annexes (figures, traces) live under each subchapter's `evidence/`.

---

## 3) Subchapter Index & Cross-Links

- **57-00 General** → program rules, global assumptions, references to ATA-20  
  `./57-00_General/`
- **57-10 Wing Primary Structure** → wingbox, ribs/spars/skins, local substantiation  
  `./57-10_Wing_Primary_Structure/`
- **57-20 Control Surfaces** → elevons/flaperons/spoilers structure & hinges  
  `./57-20_Control_Surfaces/`
- **57-30 Joints, Fasteners & Bonding** → structural joints, composite/metal stackups  
  `./57-30_Joints_Fasteners_Bonding/`
- **57-40 Access Panels & Fairings** → covers, fairings, attachments  
  `./57-40_Access_Panels_Fairings/`
- **57-50 Systems Provisions & Interfaces** → brackets, conduits, cut-outs, lightning bonds  
  `./57-50_Systems_Provisions_Interfaces/`
- **57-90 Repairs & Alterations** → repair philosophy, allowable damage, S1000D DMs  
  `./57-90_Repairs_Alterations/`

---

## 4) Standard Practices (ATA-20) — Mandatory Forms

The following **ATA-20 forms** are mandatory where applicable in ATA-57 work.  
(Links point to the authoritative forms under ATA-20 by program pattern.)

- **Composite Fastening** — `FORM-QA-20-10-01`  
  [`../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`](../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md)
- **Adhesive Bonding** — `FORM-QA-20-10-02`  
  [`../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`](../ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md)
- **Cabin Integrity / Leak Test** — `FORM-QA-20-20-01`  
  [`../ATA-20/20-20_Sealing_and_Pressurization/forms/FORM-QA-20-20-01_Cabin_Integrity_Leak_Test.md`](../ATA-20/20-20_Sealing_and_Pressurization/forms/FORM-QA-20-20-01_Cabin_Integrity_Leak_Test.md)
- **Material Handling & OOC Log** — `FORM-QA-20-30-01`  
  [`../ATA-20/20-30_Material_Handling/forms/FORM-QA-20-30-01_Material_Handling_OOC_Log.md`](../ATA-20/20-30_Material_Handling/forms/FORM-QA-20-30-01_Material_Handling_OOC_Log.md)
- **Bonding / EMI Continuity** — `FORM-QA-20-40-01`  
  [`../ATA-20/20-40_Electrical_Bonding/forms/FORM-QA-20-40-01_Bonding_EMI_Continuity.md`](../ATA-20/20-40_Electrical_Bonding/forms/FORM-QA-20-40-01_Bonding_EMI_Continuity.md)

> Use the forms above; **do not duplicate** in ATA-57. Link evidence from the relevant `57-xx/evidence/` folder.

---

## 5) Routing, I/O & Controls

**Upstream inputs (examples)**  
| Source | Transport | Path | Format | Trigger |
|---|---|---|---|---|
| AAA/CAX/CAD (OML) | PDM-PLM | /pdm/cax/cad/oml/ | STEP/OML-v2.x | on-release |
| AAA/CAE/Loads | PDM-PLM | /pdm/cae/loads/envelope/ | CSV/NPZ | post-analysis |
| ATA-20 Practices | PDM-PLM | /pdm/ata/20/ | SPM/PS/MS | on-update |

**Downstream outputs (examples)**  
| Consumer | Transport | Path | Format | Contract |
|---|---|---|---|---|
| Manufacturing | PDM-PLM | /pdm/mfg/wing/ | Work Instr. | ICD-MFG-57 |
| QA/NDT | API | https://qa.api/wing/ | JSON v1.0 | ICD-QA-57 |
| Certification | PDM-PLM | /pdm/compliance/wing/ | Matrices/Reports | ICD-CERT-57 |

- **Manifests:** `./io/routing.manifest.yaml`  
- **Contracts/Schemas:** `./contracts/`  
- **Controls:** Classification **INTERNAL–EVIDENCE-REQUIRED**; CI fail-closed for missing `artifact.manifest.yaml`, SBOM, UTCS/QS anchor.

---

## 6) Acceptance & Evidence (summary)

- **Evidence lives in** each `57-xx/evidence/` (pressure traces, bond resistance, NDT results, torque/cure logs).  
- **Acceptance criteria** live in S1000D DMCs within each `57-xx/S1000D/`.  
- **QS Seal** applies only when ATA-20 practices and ATA-57 acceptance are fully evidenced and cross-referenced.

---

## 7) Change Control

Deviations require **M&P approval** and MRB documentation. Releases are via PDM-PLM CN with **UTCS/QS** evidence.

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
