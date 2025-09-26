---
id: ASIT-BWBQ100-AAA-FORM-QA-20-10-01
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_CompositeFasteningRecord.md
llc: EVIDENCE
title: "FORM-QA-20-10-01 — Composite Fastening Record (BWB-Q100)"
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "AAA Quality Assurance (Structures)"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# FORM-QA-20-10-01 — Composite Fastening Record

**Program:** BWB-Q100  
**ATA:** 20-10 Structural Practices  
**Governing Spec:** [`SPM-20-10-0001_CompositeFastening.md`](../SPM-20-10-0001_CompositeFastening.md)  
**ATA Index:** [`../../README.md`](../../README.md)

> Use this form to capture **evidence for each composite fastening/bonded-fastener operation** (holes, inserts, collars, wet installs). Attach photos, gauge screenshots, cure logs, and NDT outputs. One form per assembly or work order unless otherwise specified.

---

## A) Job & Configuration

| Field | Entry |
|---|---|
| Work Order / Router |  |
| Assembly / Subassembly |  |
| Part Number / Serial |  |
| Drawing Rev / ECN |  |
| Config Baseline (PDM tag) |  |
| Location on Structure (station/stringer/bay) |  |
| Operation Type (check) | ☐ Dry Fastener ☐ Wet Install (primer/sealant) ☐ Bonded Insert ☐ Core Potting ☐ Rework/Oversize |
| Quantity (holes/inserts) |  |
| Technician |  |
| QA Inspector |  |
| Date (Start–End) |  |
| Station / Cell |  |

**Linked Records:**  
SBOM/Kit ID: ____  |  Tool Calibration Pack: ____  |  Cleanroom Log: ____  |  Photo Set: ____

---

## B) Materials & Lots (traceability)

> Record every **lot/expiry** actually used. If not applicable, mark “N/A”.

| Material / Consumable | Spec / Part | Lot | Expiry | Cond. (OK/NOK) |
|---|---|---|---|---|
| Fastener (type/size) |  |  |  |  |
| Collars / Nuts |  |  |  |  |
| Isolation Sleeves/Washers |  |  |  |  |
| Primer / Activator |  |  |  |  |
| Adhesive (film/paste) |  |  |  |  |
| Potting Compound |  |  |  |  |
| Sealant |  |  |  |  |
| Solvent / Cleaner |  |  |  |  |

**Environmental Controls (if bonding / wet install):**  
Temp: ___ °C | RH: ___ % | OOC start: ___ | OOC end: ___ | Within limits? ☐ Yes ☐ No (attach NCR)

---

## C) Tooling & Calibration

| Tool / Gauge | ID | Cal Due | OK/NOK |
|---|---|---|---|
| Torque Wrench / Driver |  |  |  |
| Microstop / Countersink Cage |  |  |  |
| Reamer / Drill (type) |  |  |  |
| Flushness Gauge |  |  |  |
| Depth Gauge |  |  |  |
| Vacuum Pump / Gauge |  |  |  |
| Thermocouples (if cure) |  |  |  |

Attachments: ☐ Cal certs ☐ Tool app photos ☐ Logger exports

---

## D) Surface Prep & Cleanliness

Checklist (tick all that apply):

- ☐ Masking applied to non-bond areas (if bonding)  
- ☐ Abrasive prep to uniform matte (no fiber cut-through)  
- ☐ Two-cloth solvent wipe completed; **WBT** result: ☐ Pass ☐ Fail (reclean)  
- ☐ Primer applied per spec (flash-off observed)  
- ☐ Cleanliness preserved (gloves only; protected staging)

Notes: ______________________________________________________________________

---

## E) Hole Preparation Record (per-feature)

> Add rows or attach CSV export. For sandwich: confirm countersink only in solid fill/insert.

| # | Coord/Ref | Stack-up (ply/core) | Pilot Ø | Final Ø (gauge) | Ream? | CSK depth (±0.05) | Ra | Visual (fray/burn) | Clean/WBT |
|---:|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  | ☐ |  |  | ☐ OK ☐ NOK | ☐ OK ☐ NOK |
| 2 |  |  |  |  | ☐ |  |  | ☐ OK ☐ NOK | ☐ OK ☐ NOK |
| 3 |  |  |  |  | ☐ |  |  | ☐ OK ☐ NOK | ☐ OK ☐ NOK |

Deviations / MRB refs (if any): __________________________________________________

---

## F) Potting & Inserts (if applicable)

| Core Window Ref | Pre-wet | Potting Lot | Cure (time/temp) | Machined Flush | Insert ID | Adhesive Lot | Bondline ctrl (mm) |
|---|---|---|---|---|---|---|---|
|  | ☐ Yes ☐ No |  |  | ☐ Yes ☐ No |  |  | 0.__ |

Edge seal re-established? ☐ Yes ☐ N/A

---

## G) Adhesive Application & Cure (wet install / bonded insert)

- Adhesive: **film / paste** (circle) | Mix ratio (if paste): ___ : ___ | Pot life observed: ☐  
- Bondline control: ☐ Beads (0.20–0.30 mm) ☐ Scrim ☐ Shims  
- Fixturing: ☐ Clamp ☐ Vacuum bag | Vacuum: ___ kPa | Bag stack ID: ____  
- Cure: Ramp ___ °C/min → Hold ___ °C for ___ h → Cool ___ °C/min  
- Cure Log IDs: ______________________  Thermocouples: TC-A ___ °C | TC-B ___ °C

---

## H) Fastener Installation

| # | Fastener Type/Size | Install Mode | Isolation Stack | Torque / Swage | Gauge/Readback | Head Flushness (+0.10 max) | Sealant Applied |
|---:|---|---|---|---|---|---|---|
| 1 |  | ☐ Dry ☐ Wet |  |  |  |  | ☐ Yes ☐ No |
| 2 |  | ☐ Dry ☐ Wet |  |  |  |  | ☐ Yes ☐ No |
| 3 |  | ☐ Dry ☐ Wet |  |  |  |  | ☐ Yes ☐ No |

**Caution noted?** ☐ Over-torque ☐ Collar over-swage ☐ None → If any, stop & NCR.

---

## I) Acceptance Criteria (per SPM-20-10-0001)

> Tick each metric when verified. Record measured values or attach gauge exports.

- ☐ Hole diameter per drawing (typ +0.05/−0.00 mm) — **meas**: ______  
- ☐ Roundness/runout ≤ 0.03 mm — **meas**: ______  
- ☐ CSK depth within ±0.05 mm — **meas**: ______  
- ☐ Head flushness 0.00 to +0.10 mm — **meas**: ______  
- ☐ Delamination halo ≤ 1.0 mm; none to free edge — **insp**: ☐ OK  
- ☐ FOD-free; no resin burn/whitening — **insp**: ☐ OK  
- ☐ Bondline 0.20–0.30 mm (if bonding) — **meas**: ______  
- ☐ Voids: no single > 1 mm²; cum < 0.5% (UT/thermo) — **result**: ______  
- ☐ Insert pull-out ≥ allowable (if sampled) — **test**: ______

**Result:** ☐ ACCEPT ☐ REJECT → NCR ID(s): ____________________

---

## J) NDT & Evidence

| Modality | Scope / Map | Instrument | File / Image Ref | Result |
|---|---|---|---|---|
| UT (C-scan) |  |  |  | ☐ Pass ☐ Fail |
| Active Thermography |  |  |  | ☐ Pass ☐ Fail |
| Tap Test (if allowed) |  |  |  | ☐ Pass ☐ Fail |

Attachments: ☐ C-scan ☐ Thermography ☐ Photos ☐ Logger CSV

---

## K) Nonconformances / Rework (if applicable)

- Description: ______________________________________________________________  
- Disposition: ☐ Use-as-is ☐ Repair ☐ Scrap | MRB #: ______  
- Repair Spec / Drawing: ____________________ | Oversize/Bushing: ☐ Yes ☐ No  
- Post-repair NDT result: ☐ Pass ☐ Fail | Evidence files: ____________

---

## L) Sign-off & QS

| Role | Name | Signature / Stamp | Date |
|---|---|---|---|
| Technician |  |  |  |
| QA Inspector |  |  |  |
| M&P (if bonding) |  |  |  |

**UTCS / QS Sealing**  
- canonical_hash (this form): `________________________`  
- evidence_bundle_hash (photos/NDT/logs): `________________________`  
- utcs_signature (attestation ID): `________________________`

---

## M) Routing & Links

- Back to **ATA-20** index → [`../../README.md`](../../README.md)  
- Governing SPM → [`../SPM-20-10-0001_CompositeFastening.md`](../SPM-20-10-0001_CompositeFastening.md)  
- Related: ATA-57 TPS gaps (ref) → `../../../57/57-30_TPS_Integration/`  
- PDM/PLM Release: __link or ID__

---

## N) Revision History

| Rev | Date | Change | Author |
|---|---|---|---|
| 0 | 2025-09-26 | Initial release | AAA QA |

> **Privacy & Ethics (MAL-EEM):** Attach only operationally necessary data. Remove personal identifiers from photos/logs. Comply with export controls for material/process specs.
