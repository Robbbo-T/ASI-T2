---
id: ASIT-PLUS-AAA-SPM-20-10-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/20/20-10_Structural_Practices/SPM-20-10-0001_CompositeFastening.md
llc: PROCESS
title: "Standard Practice Manual: Composite Fastening & Bonding"
configuration: baseline
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "1.0.0"
release_date: 2025-09-26
maintainer: "Structures Engineering Team"
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

# Standard Practice Manual: Composite Fastening & Bonding

## 1. Purpose
This manual establishes **mandatory practices** for the preparation, fastening, and adhesive bonding of composite structural components for the **AMPEL360 PLUS** vehicle. It ensures structural integrity, repeatability, and traceability across manufacturing, integration, and maintenance operations.

## 2. Scope
Applies to primary and secondary composite structures (**CFRP**, **C/C**, and **sandwich panels with honeycomb cores**) including:
- **Mechanical joints:** bolts, lockbolts, blind fasteners, threaded inserts, bonded-in fittings.  
- **Adhesive joints:** film & paste adhesives for **co-bond**, **secondary-bond**, and **repair**.  
- **Core potting** and **insert installation** in honeycomb.  
- **TPS & sealant interfaces** at structural joints (interface-level only; detailed TPS processes are in ATA-57/ATA-32).

**Exclusions:** Design allowables, certification basis, and control-law impacts (see ATA-51/53/55/57; LCC/ATA-27).

## 3. Normative References
- **ATA-20:** Standard Practices – Airframe (this chapter).  
- **PS-20-20-0001:** *Ablative Sealant Application* (joint sealing at thermal gaps).  
- **SPM-20-40-0001:** *Plasma Shielding & Structural Bonding* (electrical continuity).  
- **ATA-51:** Structures – General (design criteria).  
- **ATA-53/57:** Fuselage/Wings (structural interfaces).

## 4. Materials & Equipment

### 4.1. Fasteners (Space-Qualified)
- **Primary bolts:** Ti-6Al-4V, A-286, Inconel 718 (per AS7469, NAS1351, etc.)
- **Blind fasteners:** Titanium lockbolts (Huck BobTail, Cherry MaxiBolt)
- **Threaded inserts:** Keenserts, Heli-Coil (stainless steel, titanium)
- **Washers & spacers:** Ti, A-286, or phenolic per application

### 4.2. Adhesives & Sealants
- **Structural film adhesives:** FM 300-2K, EA 9394, Redux 312 (350°F service)
- **Paste adhesives:** EC 3960, Hysol EA 9514 (gap-filling, room-temp cure)
- **Core potting compounds:** EC 3445, Redux 326 (honeycomb inserts)
- **Interface sealants:** PR-1440, Sylgard 184 (TPS gap sealing coordination)

### 4.3. Tools & Equipment
- **Drilling:** Carbide bits, PCD-tipped (delamination control)
- **Countersinking:** Piloted microstop tools (depth control)
- **Torque tools:** Electronic wrenches with data logging (±2% accuracy)
- **Pressure/vacuum:** Autoclave, vacuum bag, heated platens (±5°F control)

## 5. Procedures

### 5.1. Hole Preparation (Mechanical Joints)
1. **Drilling:** Use sharp carbide bits at 300-800 RPM. Support exit side with backup material.
2. **Deburring:** Hand deburr with 220-grit paper. No powered tools on composite surfaces.
3. **Inspection:** Borescope for internal delamination, cracks, fiber pull-out.
4. **Cleanliness:** Solvent wipe (IPA) and compressed air. Verify water-break test.

### 5.2. Fastener Installation
1. **Fit-up:** Check hole alignment, edge distance, bearing stress capability.
2. **Sealant (if req'd):** Apply interfay sealant per PS-20-20-0001 (thermal gaps).
3. **Installation:** Insert fastener, apply specified torque in 3 increments (33%, 67%, 100%).
4. **Verification:** Torque check after 24 hours. Document torque values in QS log.

### 5.3. Adhesive Bonding
1. **Surface prep:** Grit blast (80-120 mesh Al2O3), solvent clean, primer (if specified).
2. **Adhesive application:** Film adhesive with 0.005" minimum bondline, paste for gaps >0.010".
3. **Assembly:** Align parts, apply pressure (10-50 psi), cure per manufacturer's cycle.
4. **Inspection:** Tap test, bond-line thickness measurement, cure verification (DSC if critical).

### 5.4. Core Potting & Inserts
1. **Hole preparation:** Drill core, remove debris, ensure clean core cells.
2. **Potting compound:** Mix per ratio, inject to 0.050" below surface, cure.
3. **Machining:** Drill/tap potted insert hole to final dimension.
4. **Insert installation:** Thread insert with specified torque, verify engagement.

## 6. Quality Control & Acceptance

### 6.1. Inspection Requirements
- **Visual:** 100% for surface defects, joint alignment, sealant continuity.
- **Dimensional:** Hole size, countersink depth, fastener protrusion.
- **Non-destructive:** Tap test (bonded joints), ultrasonic (critical bonds).
- **Torque verification:** All torque-critical fasteners (data logging required).

### 6.2. Acceptance Criteria
- **Hole quality:** No delamination >0.010", no fiber pull-out >0.005".
- **Fastener fit:** Interference fit 0.000"-0.003", no side loading.
- **Bond integrity:** No disbonds >0.25" diameter, tap test "coin ring" response.
- **Torque values:** Within ±10% of specified value, no relaxation >5% after 24hr.

### 6.3. Rejection & Rework
- **Minor defects:** Re-drill oversize holes, insert repair, re-torque loose fasteners.
- **Major defects:** Scarf repair (bonded structures), doubler installation, engineering disposition.
- **Documentation:** Non-conformance report (NCR) in UTCS/QS system, rework approval required.

## 7. Documentation & Traceability

### 7.1. Required Records
- **Material certificates:** Fastener/adhesive lot numbers, cure dates, storage conditions.
- **Process records:** Torque values, cure cycles, ambient conditions during bonding.
- **Inspection results:** Visual, dimensional, NDT findings with accept/reject disposition.
- **Rework history:** NCRs, engineering disposition, re-inspection after repair.

### 7.2. QS Integration
- All records sealed via UTCS/QS evidence system with blockchain provenance.
- Configuration control through PDM-PLM integration.
- Automatic alerts for material shelf-life expiration, calibration due dates.

## 8. Safety & Environmental

### 8.1. Personnel Safety
- **PPE:** Safety glasses, respirator (adhesive fumes), nitrile gloves.
- **Ventilation:** Local exhaust for solvents/adhesives, general ventilation >10 ACH.
- **Training:** Certified technicians only for structural joints, annual recertification.

### 8.2. Environmental Controls
- **Temperature:** 70±10°F for room-temperature cure, controlled for elevated cure.
- **Humidity:** <60% RH during bonding operations, <50% for critical bonds.
- **Contamination:** Clean room practices for critical structures, positive pressure areas.

## 9. Revision Control

This SPM is subject to configuration control. Changes require engineering approval and update of training materials. Current revision status is maintained in the UTCS/QS system with automatic distribution to qualified personnel.