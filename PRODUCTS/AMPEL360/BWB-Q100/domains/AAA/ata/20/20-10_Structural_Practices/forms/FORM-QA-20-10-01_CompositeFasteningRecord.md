---
id: ASIT-BWBQ100-AAA-FORM-QA-20-10-01
rev: 0
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_CompositeFasteningRecord.md
llc: EVIDENCE
title: "FORM-QA-20-10-01 — Composite Fastening Record (BWB-Q100)"
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "AAA Quality Assurance (Structures)"
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
  operator_id: "UTCS:OP:line-qa"
---

> **Routing:**  
> Back to ATA-20 → [`../.. /README.md`](../.. /README.md)  
> Back to 20-10 Structural Practices → [`../README.md`](../README.md)  
> Governing spec: **SPM-20-10-0001 Composite Fastening & Bonding** → (same folder)

# FORM-QA-20-10-01 — Composite Fastening Record (BWB-Q100)

Use this form to capture **in-process and final evidence** for composite hole prep, bonding (if applicable), and fastener installation per **SPM-20-10-0001**. One form per work order/zone (or as directed by the router). Attach photos, cure logs, torque readbacks, and NDT results.

---

## A) Job & Part Identification

| Field | Value |
|---|---|
| Program / Config | BWB-Q100 / `conf_000_baseline` |
| Work Order (WO) |  |
| Router / Op Step |  |
| Part Number / Rev |  |
| Part Serial / Lot |  |
| Assembly Zone |  |
| Drawing / CAD Hash |  |
| Panel/Stack Description | (e.g., CFRP [0/±45/90]s + Ti insert) |

**Station**:  ☐ Cleanroom ☐ Bond room ☐ General bay — **ESD**: ☐ Yes ☐ N/A  **FOD**: ☐ Cleared

---

## B) Personnel & Tools

| Role | Name/ID | Stamp/Sign | Time |
|---|---|---|---|
| Operator |  |  |  |
| Inspector (In-process) |  |  |  |
| QA (Final) |  |  |  |

**Calibrated Tools** (enter ID & last calibration):
- Drill/Driver: __________  Cal: __________
- Reamer: __________  Cal: __________
- Countersink (micro-stop): __________  Cal: __________
- Torque Tool: __________  Cal: __________
- Temp/RH Logger (if bonding): __________  Cal: __________

---

## C) Environment (record at start & as required)

| Timestamp | Temp (°C) | RH (%) | Cleanliness | Notes |
|---|---:|---:|---|---|
|  |  |  | ☐ Class 10k ☐ Gen |  |

> **Rule:** For bonding/surface prep use **20–25 °C**, **RH ≤ 45%** unless material spec states otherwise.

---

## D) Materials & Lots

| Category | Material / Spec | Lot / Batch | Expiry | OOC Start | OOC End |
|---|---|---|---|---|---|
| Fastener |  |  |  |  |  |
| Collar/Nut |  |  |  |  |  |
| Isolation Sleeve/Washer |  |  |  |  |  |
| Primer/Activator |  |  |  |  |  |
| Adhesive (film/paste) |  |  |  |  |  |
| Potting (if HC insert) |  |  |  |  |  |
| Sealant (edge/hole) |  |  |  |  |  |

> **Check:** ☐ OOC times within limit ☐ Certificates on file (PDM-PLM)

---

## E) Hole Preparation Record

> Use one line per hole or range. Attach additional pages if needed.

| Hole ID | Stack Nominal | Pilot Ø (mm) | Final Ø / Ream (mm) | y/n Backup Support | Speed/Feed Note | Deburr OK | Clean (WBT) |
|---|---|---:|---:|:---:|---|:---:|:---:|
|  |  |  |  | ☐ |  | ☐ | ☐ |

**Countersink (if applicable)**

| Hole ID | CS Type | Target Depth (mm) | Measured (mm) | Ra ≤ 3.2 µm | In Solid/Potted Zone |
|---|---|---:|---:|:---:|:---:|
|  |  |  |  | ☐ | ☐ |

**Notes:** Avoid open-core countersinks; ream to finish; vacuum extract; no air blow over prepped surfaces.

---

## F) Honeycomb Core Potting & Inserts (if applicable)

| Insert ID | Core Window Size | Potting Spec | Cure Cycle | Post-Machined to | NDT (UT/Thermo) | Accept |
|---|---|---|---|---|---|:---:|
|  |  |  |  |  |  | ☐ |

Edge sealing completed: ☐ Yes ☐ N/A

---

## G) Surface Preparation & Priming (for bonding or wet-install)

- Masking applied: ☐ Yes  
- Abrasion (180–320 grit, no fiber cut): ☐ Yes  
- Clean (two-cloth): ☐ Yes → **WBT pass**: ☐ Yes / ☐ No (re-clean)  
- Primer/Activator: __________  Lot: __________  Flash-off: ______ min

---

## H) Adhesive Application & Cure (if bonding / wet install)

| Adhesive | Form | Mix Ratio / Film Code | Bondline Control | Fixturing |
|---|---|---|---|---|
|  | ☐ Film ☐ Paste |  | ☐ Beads ☐ Scrim ☐ Shims | ☐ Vacuum bag ☐ Clamps |

**Cure Log** (attach chart if autoclave/oven):
- Setpoint / Duration: __________ / __________  
- Ramp / Cool: ≤2 °C/min / ≤3 °C/min (unless spec)  
- Vacuum/Pressure: __________ / __________  
- Thermocouples: #____ (min 2 on joint)

Witness coupons included: ☐ Yes ☐ N/A  —  Results attached: ☐

---

## I) Fastener Installation

| Hole ID | Fastener PN | Grip/Len | Install | Isolation Used | Torque/Spec | Torque Readback | Head Flushness (mm) | Wet Seal |
|---|---|---|---|---|---|---|---:|---|
|  |  |  | ☐ Dry ☐ Wet | ☐ Sleeve ☐ Washer ☐ Primer |  |  |  | ☐ Yes |

> **Caution:** Over-torque crush risk in composites. Stop if over-swage/over-torque >10% is observed.

---

## J) Acceptance Criteria — Summary (per SPM-20-10-0001)

- Hole diameter within drawing: ☐ Pass / ☐ Fail  
- Roundness/runout ≤ 0.03 mm (finish reamed): ☐ Pass / ☐ Fail  
- Countersink depth ±0.05 mm; no fiber breakout: ☐ Pass / ☐ Fail  
- Head flushness 0.00 to +0.10 mm (unless otherwise specified): ☐ Pass / ☐ Fail  
- Delamination halo ≤ 1.0 mm; none connected to edge: ☐ Pass / ☐ Fail  
- Bondline thickness 0.20–0.30 mm (if bonded): ☐ Pass / ☐ Fail  
- Bond voids ≤ limits (no single >1 mm²; cum <0.5%): ☐ Pass / ☐ Fail

**Inspection Evidence**

| Method | Scope | Result | Ref Attachment |
|---|---|---|---|
| Visual | All features | ☐ Accept ☐ Reject |  |
| UT | Bonded areas / potted | ☐ Accept ☐ Reject |  |
| Thermography | As directed | ☐ Accept ☐ Reject |  |
| Tap test (where allowed) | Secondary | ☐ Accept ☐ Reject |  |

Nonconformance? ☐ No ☐ Yes → **NCR ID**: __________  **MRB Dispo**: __________

---

## K) Attachments Checklist

- ☐ Photos (pre/post)  
- ☐ Cure log charts / vacuum record  
- ☐ Torque tool readbacks / data dump  
- ☐ NDT reports (UT/Thermo/Tap)  
- ☐ Certificates (materials/consumables)  
- ☐ Additional hole/fastener tables

---

## L) UTCS / QS Traceability

| Field | Value |
|---|---|
| Work Packet QS Seal (QS) |  |
| Evidence Canonical Hash |  |
| PDM-PLM Record / ECO |  |
| Mesh/Model Hash (if applicable) |  |

---

## M) Final Sign-off

| Role | Name / ID | Stamp / Signature | Date |
|---|---|---|---|
| Operator |  |  |  |
| Inspector |  |  |  |
| QA Release |  |  |  |

> **Data Handling:** No PII. All lots, calibrations, and logs must be referenceable in PDM-PLM. Submit electronically to QA vault; physical prints are uncontrolled.

