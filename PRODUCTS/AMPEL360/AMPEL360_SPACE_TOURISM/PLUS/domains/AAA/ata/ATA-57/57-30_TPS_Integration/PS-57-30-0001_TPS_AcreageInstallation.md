---
id: ASIT-PLUS-AAA-PS-57-30-0001
rev: 0
project: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM
artifact: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/PLUS/domains/AAA/ata/ATA-57/57-30_TPS_Integration/PS-57-30-0001_TPS_AcreageInstallation.md
llc: PROCESS
title: "Process Specification — TPS Acreage Installation (ATA-57-30)"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: 2025-09-26
maintainer: "TPS Engineering Team"
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

# PS-57-30-0001 — TPS Acreage Installation

Process specification for installing **thermal protection system (TPS) acreage** on lifting surfaces (tiles, blankets, carrier panels, gap fillers, and thermal barriers) for **AMPEL360 PLUS**.

> **Related**: Primary structure requirements in [DS-57-10-0001](../57-10_Primary_Structure/DS-57-10-0001_LiftSurface_Primary.md), leading-edge high-temp components in [PS-57-20-0001](../57-20_Leading_Edges/PS-57-20-0001_RCC_Handling_Bonding.md), and overall chapter overview in [ATA-57 README](../README.md). General practices live in [ATA-20](../../20/README.md).

---

## 1. Purpose & Scope

- **Purpose**: Define auditable, repeatable steps to install TPS acreage with controlled bondlines, compliant gaps, and verified integrity for **reentry → approach/landing → turnaround**.
- **In scope**: TPS **tiles/panels**, **AFRSI/blankets**, **gap fillers**, **thermal barriers**, **carriers/substructure** prep, adhesive/primer application, cure, inspection, and NDI.
- **Out of scope**: Leading-edge RCC (see [PS-57-20-0001](../57-20_Leading_Edges/PS-57-20-0001_RCC_Handling_Bonding.md)), primary structure (see [DS-57-10-0001](../57-10_Primary_Structure/DS-57-10-0001_LiftSurface_Primary.md)), control-surface TPS (see ATA-55).

---

## 2. Materials & Equipment

### 2.1 TPS Materials

**Silica tiles** (acreage protection)
- **Type**: LI-900/LI-2200 (density 144/352 kg/m³), reusable surface insulation.
- **Size range**: 150×150 mm to 300×300 mm, thickness 12–75 mm per thermal analysis.
- **Properties**: Max service temp 1260°C, thermal conductivity ≤ 0.12 W/m·K at 1000°C.
- **Storage**: Humidity-controlled (≤45% RH), impact protection, serial number tracking.

**AFRSI blankets** (lower-temperature regions)
- **Type**: Advanced flexible reusable surface insulation, 0.16–0.32 kg/m².
- **Construction**: Silica batting + glass-fiber scrim + white silica coating.
- **Properties**: Max service temp 650°C, flexible, damage-tolerant, lightweight.
- **Handling**: Roll storage, minimize creasing, pre-installation conditioning.

**Gap fillers**
- **Type**: Ceramic fiber rope (Nextel/alumina), high-temp silicone putty.
- **Application**: Inter-tile gaps, penetration seals, thermal expansion joints.
- **Service limits**: 1200°C continuous, 1400°C peak, vacuum-compatible.

### 2.2 Adhesives & Primers

**Room-temperature vulcanizing (RTV) silicone**
- **Type**: RTV-560 or equivalent, single-component, moisture-cure.
- **Properties**: Service temp -65°C to +260°C, elongation >200%, vacuum-stable.
- **Pot life**: 4 hours (working time), 24 hours (handling cure), 7 days (full cure).
- **Storage**: Sealed containers, refrigerated, use within 6 months of manufacture.

**High-temperature primer**
- **Type**: Silicone-based, compatible with substrate and adhesive chemistry.
- **Application**: Brush/spray, thickness 25–50 μm, cure before adhesive application.
- **Purpose**: Adhesion promotion, substrate sealing, thermal barrier enhancement.

### 2.3 Installation Equipment

**Surface preparation**
- Abrasive blasting equipment (alumina grit, 120–220 mesh).
- Solvent cleaning (isopropyl alcohol, acetone), lint-free wipes.
- Compressed air (oil-free, moisture-separated), vacuum cleaning systems.

**Application tools**
- Adhesive dispensing guns (pneumatic, controlled bead size).
- Mixing paddles, application spatulas, smoothing tools.
- Thickness gauges, gap measurement tools, alignment fixtures.

**Curing environment**
- Temperature control: 18–25°C ±2°C during installation.
- Humidity control: 45–65% RH (optimal for RTV cure).
- Contamination control: Class 100,000 cleanroom or equivalent filtration.

---

## 3. Surface Preparation

### 3.1 Substrate Cleaning

**Degreasing** (mandatory first step)
1. Wipe with isopropyl alcohol using lint-free cloth.
2. Remove all oils, fingerprints, mold-release agents, previous adhesive residue.
3. Air-dry completely before proceeding (minimum 10 minutes).
4. **Acceptance**: Water-break-free surface, no visible contamination.

**Abrasive preparation** (for metallic substrates)
1. Light abrasive blast with 120-grit alumina, 2–3 bar pressure.
2. Remove oxide layers, create uniform surface texture (Ra 3.2–6.3 μm).
3. Compressed-air blow-off, followed by vacuum cleaning.
4. **Acceptance**: Uniform matte finish, no remaining loose particles.

**Composite substrate preparation**
1. Light sanding with 220-grit paper, uniform cross-hatch pattern.
2. Remove sanding dust with tack cloth, followed by solvent wipe.
3. Avoid deep scratches that could compromise structural integrity.
4. **Acceptance**: Smooth, slightly textured surface ready for primer.

### 3.2 Priming (where specified)

**Primer application**
1. Apply high-temp primer in thin, uniform coat using brush or spray.
2. Coverage: 100% of bonding area, thickness 25–50 μm.
3. Cure per manufacturer's instructions (typically 30 min at 23°C).
4. **Quality check**: Uniform coverage, no pinholes, proper adhesion.

**Primer inspection**
- **Visual**: Complete coverage, uniform thickness, no contamination.
- **Adhesion**: Tape test (ASTM D3359), no primer removal acceptable.
- **Thickness**: Eddy-current gauge where applicable, document readings.

---

## 4. TPS Installation Procedures

### 4.1 Tile Installation

**Pre-installation checks**
1. Verify tile part number matches installation drawing.
2. Inspect tile for damage: cracks, chips, contamination, dimensional compliance.
3. Test-fit in installation location, check gap requirements (2–6 mm nominal).
4. **Hold point**: Engineering approval required for any nonconforming tiles.

**Adhesive application**
1. Apply RTV-560 to substrate in continuous bead pattern per drawing.
2. Bead dimensions: 6 mm wide × 3 mm high, 15 mm spacing between parallel beads.
3. Coverage: 40–60% of tile back surface for structural tiles, 25–40% for thermal-only.
4. **Time limit**: Install tile within 30 minutes of adhesive application.

**Tile placement & alignment**
1. Position tile using alignment fixtures, avoid sliding/smearing adhesive.
2. Apply uniform pressure (0.5–1.0 psi) for 60 seconds minimum.
3. Verify gap dimensions, adjust neighboring tiles if necessary.
4. **Final check**: Tile flush with surrounding surface ±2 mm, gaps within tolerance.

**Cure monitoring**
1. Mark installation time, maintain cure environment conditions.
2. No disturbance for first 4 hours (initial set), 24 hours (handling strength).
3. Document ambient temperature/humidity during cure period.
4. **Acceptance**: Full cure achieved before flight operations (minimum 7 days).

### 4.2 AFRSI Blanket Installation

**Pattern cutting** (if required)
1. Use sharp knife/scissors, avoid fraying edges.
2. Allow 10 mm overlap at seams, account for thermal expansion.
3. Mark installation orientation to maintain fiber alignment.

**Adhesive pattern**
1. Apply RTV in strips parallel to predominant load direction.
2. Spacing: 75 mm centers for low-load areas, 50 mm for high-load regions.
3. Avoid continuous adhesive lines that could restrict thermal expansion.

**Installation technique**
1. Position blanket carefully, avoid wrinkles or air pockets.
2. Work from center outward, smooth progressively to edges.
3. Maintain 2–5 mm gap at structural interfaces for expansion.
4. **Quality check**: Smooth surface, proper overlap, no lifting edges.

### 4.3 Gap Filling & Sealing

**Gap measurement**
1. Use feeler gauges to verify gap width at multiple points.
2. Document gap dimensions for installation record.
3. **Specification**: 2–6 mm nominal, 1–8 mm acceptable range.

**Gap filler installation**
1. **Ceramic rope**: Press into gap, compress to 70–80% of original diameter.
2. **Silicone putty**: Tool smooth, slightly proud of surface, cure fully.
3. Ensure gap filler does not impede thermal expansion.
4. **Acceptance**: Complete gap coverage, no voids, smooth transition.

---

## 5. Quality Control & Inspection

### 5.1 In-Process Inspection

**Adhesive application checks**
- **Coverage**: 40–60% of tile area, continuous bead pattern.
- **Thickness**: 2–4 mm after tile installation, no squeeze-out excess.
- **Quality**: No air bubbles, contamination, or incomplete mixing.

**Installation verification**
- **Alignment**: Tile edges within ±2 mm of design position.
- **Gaps**: 2–6 mm nominal, uniform around tile perimeter.
- **Surface**: Flush within ±2 mm, no high/low spots, smooth transitions.

**Cure environment monitoring**
- **Temperature**: 18–25°C throughout cure period, log continuously.
- **Humidity**: 45–65% RH, no condensation on surfaces.
- **Contamination**: No dust settling, foreign objects, traffic restrictions.

### 5.2 Final Inspection

**Visual inspection** (100% coverage)
1. Examine all tiles/blankets for proper installation, damage, contamination.
2. Verify gap filler installation, smooth transitions, complete coverage.
3. Check for adhesive squeeze-out, clean excess per approved procedure.
4. **Documentation**: Photograph any nonconformances, note corrective actions.

**Dimensional verification**
1. Measure installed thickness at designated points (per drawing).
2. Check overall surface smoothness using straightedge/gap gauges.
3. Verify thermal expansion joint functionality where applicable.
4. **Acceptance**: All dimensions within drawing tolerances.

**Adhesion testing** (sampling basis)
1. Pull-test selected tiles using calibrated equipment (50 N minimum).
2. Test frequency: 1% of installed tiles, minimum 3 per batch.
3. **Acceptance**: No adhesive failures, substrate failure mode acceptable.
4. **Nonconformance**: If any test fails, increase sample size and investigate.

### 5.3 Non-Destructive Inspection

**Thermal imaging** (infrared thermography)
1. Heat substrate to 60–80°C using radiant heaters.
2. Scan installed TPS with calibrated IR camera.
3. **Detection**: Debonds show as hot spots, voids as cold spots.
4. **Acceptance**: No indications >25 mm diameter, <2% total area affected.

**Ultrasonic inspection** (for critical areas)
1. Use through-transmission technique where substrate access permits.
2. Frequency: 1–5 MHz depending on tile thickness and substrate.
3. **Calibration**: Reference standards with known good/bad bond conditions.
4. **Documentation**: Map all indications, correlate with thermal imaging.

---

## 6. Rework & Repair Procedures

### 6.1 Tile Removal

**Heating method** (preferred)
1. Apply localized heat (60–80°C) to soften RTV adhesive.
2. Use heat gun or radiant panel, avoid overheating tile (>100°C).
3. Work removal tool under tile edges progressively.
4. **Caution**: Support tile weight, avoid damage to adjacent tiles.

**Chemical softening** (alternative)
1. Apply RTV removal solvent to bondline edges.
2. Allow 30–60 minutes penetration time.
3. Work removal progressively, reapply solvent as needed.
4. **Cleanup**: Remove all solvent residue before reinstallation.

**Adhesive cleanup**
1. Remove all old adhesive from substrate using scraper/abrasive.
2. Clean surface per Section 3.1 preparation requirements.
3. Inspect for substrate damage, repair if necessary.
4. **Acceptance**: Surface ready for new installation per this specification.

### 6.2 Repair Criteria

**Repairable damage**
- **Tile cracks**: Length ≤50 mm, depth ≤25% of thickness.
- **Edge chipping**: Area ≤25 mm², depth ≤10 mm.
- **Surface contamination**: Removable without tile damage.

**Non-repairable damage** (requires replacement)
- **Through cracks**: Any crack extending completely through tile.
- **Large chips**: Area >25 mm² or depth >10 mm.
- **Delamination**: Any internal separation detected by NDI.
- **Thermal damage**: Discoloration, sintering, property degradation.

---

## 7. Documentation & Records

### 7.1 Installation Records

**For each tile/blanket installed**
- Part number, serial number, installation location (grid reference).
- Installation date/time, technician ID, inspector signature.
- Adhesive batch number, cure conditions (temp/humidity log).
- Any nonconformances, rework actions, final acceptance status.

### 7.2 Quality Records

**Inspection data**
- Visual inspection checklist, dimensional measurements.
- NDI results (thermal/ultrasonic), pull-test data where performed.
- Photographic record of completed installation.
- **Retention**: Permanent record, accessible for maintenance/investigation.

**Material traceability**
- TPS material certifications, adhesive batch test reports.
- Storage/handling logs, shelf-life compliance verification.
- **UTCS integration**: All records linked to vehicle serial number, flight history.

---

## 8. Maintenance & Service

### 8.1 Post-Flight Inspection

**Visual examination** (every flight)
1. Inspect all TPS surfaces for damage: cracks, missing tiles, debonds.
2. Check gap filler condition, thermal barrier integrity.
3. **Acceptance**: No new damage >25 mm, no safety-of-flight impact.

**Detailed inspection** (periodic)
1. NDI scan per schedule (typically every 10 flights).
2. Pull-test sampling of suspect areas.
3. **Trending**: Track damage growth, bondline degradation over time.

### 8.2 Refurbishment Criteria

**Tile replacement triggers**
- Any through-crack or delamination detected.
- Edge damage >25 mm² cumulative area.
- Debond area >15% of tile back surface.
- Thermal damage affecting structural properties.

**Blanket replacement**
- Tearing, fraying beyond repair capability.
- Debond area >25% of blanket surface.
- Contamination not removable by approved cleaning.

---

## 9. Safety & Environmental

### 9.1 Personnel Safety

**Hazardous materials**
- **RTV adhesive**: Use adequate ventilation, avoid skin contact.
- **Solvents**: Fire hazard, vapor inhalation risk, use approved PPE.
- **Abrasives**: Respiratory protection during blasting operations.

**Handling precautions**
- **Tile fragility**: Use proper lifting techniques, avoid point loads.
- **Sharp edges**: Cut-resistant gloves during cutting/fitting operations.
- **Elevated work**: Fall protection, stable work platforms required.

### 9.2 Environmental Controls

**Waste disposal**
- **Adhesive waste**: Cure fully before disposal, follow local regulations.
- **Solvent-contaminated materials**: Hazardous waste procedures.
- **Damaged tiles**: Recycle silica content where possible.

**Emissions control**
- **VOC limits**: Monitor solvent vapor levels, maintain below exposure limits.
- **Particulate control**: HEPA filtration during abrasive operations.

---

## 10. Compliance & Traceability

**Regulatory compliance**
- **FAA/AST**: 14 CFR Parts 450/460 reusable launch vehicle requirements.
- **OSHA**: Workplace safety standards for hazardous materials, confined spaces.
- **EPA**: Environmental regulations for waste disposal, air emissions.

**Quality system integration**
- **UTCS/QS**: All processes auditable, evidence-linked, configuration-controlled.
- **AS9100**: Aerospace quality management system compliance.
- **ISO 14001**: Environmental management system integration.

**Evidence management**: All installation records, inspection results, and maintenance actions permanently stored in UTCS database with digital signatures, approval chains, and full configuration traceability to vehicle operations.

---

*This process specification ensures reliable, repeatable TPS acreage installation supporting safe AMPEL360 PLUS suborbital operations with verifiable quality and full regulatory compliance.*