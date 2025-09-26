---
id: ATA-20-OV-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: /home/runner/work/Robbbo-T/Robbbo-T/PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/20/README.md
llc: SYSTEMS
title: "ATA-20: Standard Practices — Airframe (BWB-Q100)"
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

# ATA-20 — Standard Practices (BWB-Q100)

ATA-20 defines the **mandatory, program-wide practices** for documentation, materials, fastening/bonding, sealing/pressurization, material handling, electrical bonding/EMI, inspection/NDT, and evidence capture. Conformance to ATA-20 is a **pre-requisite** for QS (Quality Seal) on all downstream ATA chapters.

---

## 1) Scope & Applicability

- **Applies to:** All BWB-Q100 airframe work (design, manufacturing, integration, maintenance), covering metallics, composites, and sandwich structures; pressurized and non-pressurized volumes; EMI/ESD practices.
- **Includes:** Drawing & data standards, GD&T/tolerances, fastener systems, adhesive bonding, sealants & leak checks, TPS or thermal barriers *at interface level*, electrical bonding/grounding, cleanliness/FOD/ESD controls, evidence & traceability.
- **Excludes:** Chapter-specific functional requirements (handled by their ATA chapter), certification basis selection, and control-law content.

---

## 2) Index of Deliverables

### 20-10 Structural Practices  
> Mechanical fastening, adhesive bonding, scarf/patch repairs, inserts & potting for sandwich.
- **[SPM-20-10-0001]** Standard Practice Manual — Composite Fastening & Bonding  
  `./20-10_Structural_Practices/SPM-20-10-0001_CompositeFastening.md`

### 20-20 Sealing & Pressurization  
> Surface prep for seals, sealant application, proof/hold tests, leak detection.
- **[PS-20-20-0001]** Process Spec — Ablative/Barrier Sealant Application  
  `./20-20_Sealing_and_Pressurization/PS-20-20-0001_AblativeSealantApplication.md`
- **[SPM-20-20-0002]** Standard Practice Manual — Pre-Flight/Pre-Close Cabin Integrity Checks  
  `./20-20_Sealing_and_Pressurization/SPM-20-20-0002_CabinIntegrityChecks.md`

### 20-30 Material Handling  
> Storage, shelf-life, freezer/fridge controls, hazardous handling, kitting & traceability.
- **[MS-20-30-0001]** Material Spec — Handling & Inspection (e.g., TPS tiles, pre-pregs)  
  `./20-30_Material_Handling/MS-20-30-0001_TPS_TileHandling.md`

### 20-40 Electrical Bonding / EMI  
> Structural bonding to ground, lightning/ESD controls, shield terminations.
- **[SPM-20-40-0001]** Standard Practice Manual — Plasma/EMI Shielding & Structural Bonding  
  `./20-40_Electrical_Bonding/SPM-20-40-0001_PlasmaShieldingBonding.md`

> **Note:** File names/paths above are program-relative; ensure PDM-PLM links resolve to the current controlled revisions.

---

## 3) Routing

### 3.1 Upstream (Inputs)
| Source (ID) | Transport | Path/Topic/Endpoint | Format/Schema | Cadence/Trigger | Owner |
|---|---|---|---|---|---|
| AAA/CAX/CAD (OML v2.3) | PDM-PLM artifact | /pdm/cad/oml/2.3/ | STEP • OML-2.3 | on-release | CAD Team |
| AAA/CAE/Structural | PDM-PLM artifact | /pdm/cae/structural/loads/ | FEA Results v1.2 | post-analysis | CAE Team |
| QA/Standards | PDM-PLM artifact | /pdm/qa/standards/ata20/ | PDF/XML v1.0 | on-update | QA Team |

### 3.2 Downstream (Outputs)
| Consumer (ID) | Transport | Path/Topic/Endpoint | Format/Schema | Contract/ICD | Owner |
|---|---|---|---|---|---|
| AAA/ATA/51-57 | PDM-PLM artifact | /pdm/ata/practices/20/ | SPM/PS/MS v1.0 | ICD-AAA-ATA-020 | ATA Team |
| Manufacturing | PDM-PLM artifact | /pdm/mfg/practices/20/ | Work Instructions | ICD-MFG-ATA-020 | MFG Team |
| QA/Inspection | API | https://qa.api/practices/ata20 | JSON v1.0 | ICD-QA-ATA-020 | QA Team |

### 3.3 Cadence & Environments
- **Dev:** file:///dev/ata/20/ (ad hoc on PR)
- **Stage:** file:///stage/ata/20/ (nightly 02:00 UTC)
- **Prod:** /pdm/ata/20/ (post-baseline release)

### 3.4 Controls & Reliability
- **Classification:** INTERNAL–EVIDENCE-REQUIRED
- **Access:** PDM role: `AAA.contributors` (read), `ASI-T.arch` (write)
- **SLO:** publish ≤ 30 min after upstream seal; **Retries:** 3× exponential
- **Alerts:** #aaa-ata20 on failure; **Escalation:** on-call @maintainer within 15 min
- **Change route:** via CN; MRB approval required

### 3.5 Artifacts
- **Schemas/ICDs:** `./contracts/`  
- **Manifests:** `./io/routing.manifest.yaml`

---

## 4) Governing Standards & References

- **Drawing/GD&T:** ASME Y14.x series (or program standard), title-block metadata & rev control enforced by PDM-PLM.
- **Units:** SI primary; any secondary units must be explicitly tagged and conversion-audited.
- **Calibration:** All torque, pressure, temperature, and NDT instruments under calibrated control.
- **Regulatory context:** Conform to applicable aviation/space authorities (e.g., FAA/EASA/AST); chapter-specific regs appear in their ATA indices.

---

## 5) Roles & Responsibilities

- **Manufacturing/Integration:** Execute procedures, maintain environmental controls, complete QS records.
- **M&P Engineering:** Own materials & process specs, approve deviations, define cure/cycle windows.
- **Quality:** Tool calibration, in-process/final inspections, NDT plans and execution, MRB.
- **Configuration Management (PDM-PLM):** Baselines, BoM/router linkage, effectivity, evidence retention.

---

## 6) Safety, Environment & Cleanliness

- **PPE:** As specified per material/process (solvents, VOCs, cryogenic storage, hot-bonding).
- **Ventilation:** Local exhaust for solvents/adhesives; VOC monitoring where required.
- **ESD/FOD:** ESD-safe handling near avionics; FOD controls at all stations; bag & tag foreign material.
- **Environmental windows:** Unless superseded by spec: **20–25 °C**, **RH ≤ 45%** for bonding/sealing/prep; record out-of-cold (OOC) times for limited-life materials.

---

## 7) Core Practices (Process Overviews)

### 7.1 Fastening & Bonding (20-10)
- **Hole quality:** Pilot → step drill → ream; countersink with depth stop; vacuum removal; WBT (water-break test) for clean surfaces.  
- **Galvanic isolation:** Isolation sleeves/washers/primers or "wet-install" sealant per callouts.  
- **Bonding:** Controlled bondline (scrim/beads/shims); vacuum bagging or fixtures; cure/post-cure per M&P; cure logs mandatory.  
- **Sandwich & inserts:** Core potting with approved compounds; bonded inserts with bondline controls; seal re-exposed core.

### 7.2 Sealing & Pressurization (20-20)
- **Sealants:** Approved chemistries; surface activation/primers; profile control.  
- **Pressure/Leak tests:** Proof/hold, ΔP decay, tracer gas (e.g., He/MS), acoustic sniff; acceptance thresholds per SPM-20-20-0002.  
- **Records:** Pressure profiles, leak rates, ambient conditions, sensor calibration.

### 7.3 Material Handling (20-30)
- **Storage:** Freezer/fridge/humidity cabinets; log OOC; FIFO by batch/lot; quarantine non-conforming.  
- **Kitting & ID:** Barcode/QR with lot, expiry, storage class; link to work order and router.

### 7.4 Electrical Bonding / EMI (20-40)
- **Continuity:** Bond resistance targets per location class; verify surface prep and protective finishes.  
- **Lightning/ESD:** Down-bond paths and shield terminations per spec; inspection & re-test after rework.

---

## 8) Inspection, NDT & Acceptance (General)

| Feature                        | Minimum Requirement (unless drawing/spec overrides)            | Method                   |
| ---                            | ---                                                            | ---                      |
| Hole diameter & roundness      | As drawing; reamed finish; roundness ≤ 0.03 mm                 | Plug/bore gauge, CMM     |
| Countersink depth/finish       | ±0.05 mm; no fiber breakout; Ra ≤ 3.2 µm                       | Depth gauge, visual      |
| Head flushness                 | 0.00 to +0.10 mm proud (typical)                               | Flushness gauge          |
| Bondline thickness             | Per spec (typ. 0.20–0.30 mm)                                   | Shims/coupons            |
| Bond voids                     | No void > 1 mm²; cum. area < 0.5%                              | UT/thermography          |
| Leak rate (pressurized vols.)  | Per SPM-20-20-0002 table for ΔP/hold                           | ΔP decay / tracer gas    |
| Bond resistance (grounding)    | Per location class (ref. SPM-20-40-0001)                       | Bond meter               |

> Drawing/model **governs** where it conflicts with generic limits.

---

## 9) Evidence, Records & QS

- **Mandatory forms (program examples):**  
  - `FORM-QA-20-10-01` (Composite Fastening)  
  - `FORM-QA-20-10-02` (Adhesive Bonding)  
  - `FORM-QA-20-20-01` (Cabin Integrity / Leak Test)  
  - `FORM-QA-20-30-01` (Material Handling & OOC Log)  
  - `FORM-QA-20-40-01` (Bonding/EMI Continuity)
- **Traceability:** Material lots, OOC timers, mix ratios, cure logs, torque values, pressure traces, NDT results, inspector stamps → all linked to part/serial/work order and **PDM-PLM** baseline.
- **QS Seal:** Applied only when applicable ATA-20 practices and acceptance criteria are **fully evidenced** and cross-referenced in the chapter-specific artifact.

---

## 10) Compliance & Certification Notes

- Conform to the **applicable authority** (e.g., FAA/EASA/AST) and customer/prime requirements.  
- Chapter-specific compliance guidance appears in ATA-51/53/55/57, etc.; this index enforces the **how** (process rigor & evidence), not the **what** (functional requirements).

---

## 11) Cross-References

- **ATA-51/53/55/57:** Apply ATA-20 tolerances, fastening/bonding, sealing, EMI/bonding practices to structures, fuselage, stabilizers, and lifting surfaces.  
- **CAx (CAD/CAE/CFD/VP):** Data standards, report templates, revision control, and evidence retention.  
- **PDM-PLM:** Configuration baselines, effectivity, controlled release/changes.  
- **QOx (QUBO/BQM/QAOA/Annealing):** If discrete design choices are optimized, their **manufacturability and compliance** must still pass ATA-20 checks.

---

## 12) Change Control

Any deviation from ATA-20 practices requires **M&P approval** and formal deviation/MRB documentation. Revisions are released via **PDM-PLM** change notices and sealed with **UTCS/QS** evidence.

---

## 13) Glossary (selected)

- **OOC:** Out-of-Cold (time while a limited-life material is outside controlled storage)  
- **WBT:** Water-Break Test (cleanliness verification)  
- **QS:** Quality Seal (deterministic evidence package approval)  
- **FOD/ESD:** Foreign Object Debris / Electrostatic Discharge

---
*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
