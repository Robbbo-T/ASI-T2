---
id: ASIT-PLUS-AAA-PS-20-20-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/20/20-20_Sealing_and_Pressurization/PS-20-20-0001_AblativeSealantApplication.md
llc: PROCESS
title: "Process Specification: Ablative Sealant Application on Thermal Expansion Joints"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "Materials & Process Engineering Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
provenance:
  canonical_hash: "sha256:TBD"
---

# Process Specification: Ablative Sealant Application

## 1. Purpose
This document establishes the mandatory procedure for the surface preparation, application, curing, and inspection of the `MAT-ABL-S78B` ablative sealant on the thermal expansion joints between the TPS tiles and the airframe structure of the AMPEL360 PLUS.

## 2. Materials and Equipment
- **Sealant**: `MAT-ABL-S78B` (store at -10°C ± 2°C).
- **Surface Activator**: `CHEM-PRIME-9A`.
- **Application Equipment**: `TOOL-EXT-P45` pneumatic extrusion gun with `NOZ-T3-F` nozzle.
- **Inspection Equipment**: `TOOL-US-SCAN-M2` ultrasonic probe.
- **PPE**: Cryogenic gloves, eye protection, respirator with VOC filter.

## 3. Procedure

### 3.1. Surface Preparation
1. Clean the joint with `SOLV-ISO-99` solvent and a lint-free cloth.
2. Perform a water break test to verify cleanliness. The surface must be free of contaminants.
3. Apply a thin, uniform layer of `CHEM-PRIME-9A` activator with a natural bristle brush.
4. Allow to dry for 60 minutes (± 5 min) in a humidity-controlled environment (< 40% RH).

### 3.2. Sealant Application
1. Acclimate the sealant cartridge to room temperature (22°C ± 2°C) for 2 hours before use.
2. Install the cartridge and nozzle on the extrusion gun. Purge the first 5 cm of material.
3. Apply a continuous bead of sealant at the base of the joint, ensuring a complete fill with no air pockets.
4. Use a Teflon spatula to tool the bead to a concave profile as per drawing `DWG-AAA-20-20-101`.

### 3.3. Curing
1. Initial cure: 24 hours at 22°C ± 2°C.
2. Final cure (post-cure): 4 hours in an oven at 80°C.

## 4. Inspection and Acceptance
1. **Visual Inspection**: Verify absence of cracks, bubbles, or discontinuities.
2. **Ultrasonic Inspection**: Scan the joint with the `TOOL-US-SCAN-M2` probe to verify adhesion and absence of internal voids.
3. **Acceptance Criteria**: Any void > 1mm² or lack of adhesion over > 5% of the joint length is cause for rejection.
4. **Documentation**: Record inspection results on form `FORM-QA-20-20-01` and seal with QS.