# Repair Procedures - Wing Primary Structure

This directory contains S1000D repair procedural data modules (Info Code 520A) for wing primary structure components.

## Purpose

Repair procedures define:
- Damage assessment and classification
- Allowable damage limits
- Standard repair schemes
- Repair material and process specifications
- Post-repair inspection and acceptance criteria
- Repair effectivity and configuration control

## Damage Categories

### Category 1: Allowable Damage (No Repair Required)
- Minor surface scratches, abrasions
- Small dents within limits
- Minor paint/coating damage
- Document and monitor

### Category 2: Minor Repair (Standard Repair Procedures)
- Skin/laminate damage within repair limits
- Fastener hole elongation/bearing damage
- Small delaminations
- Minor bond disbonds
- Use standard repair schemes from this directory

### Category 3: Major Repair (Engineering Disposition Required)
- Damage exceeding standard repair limits
- Critical structure damage
- Multiple/adjacent damage sites
- Requires stress analysis and engineering approval

## Standard Repair Types

### Composite Repairs

#### Scarf Repair
- External ply-by-ply removal to form taper
- Laminate replacement matching original layup
- Co-bonded or secondary bonded
- Suitable for small-to-medium damage

#### Patch Repair (External Doubler)
- External doublers bonded over damaged area
- Stepped or tapered edges
- Bolted or bonded attachment
- Suitable for damage in low-load areas

#### Injection Repair
- Resin injection for delaminations
- Through-hole drilling and vacuum infusion
- Minimal surface disturbance
- Suitable for small disbonds/delaminations

#### Core Replacement
- Honeycomb core removal and replacement
- Face sheet repair or replacement
- Bonding of new core
- Suitable for sandwich structure damage

### Metallic Repairs

#### Doubler Installation
- Bolted or bonded metallic doublers
- Fastener pattern per stress analysis
- Edge distance and spacing requirements

#### Insert Repair
- Bushing or insert installation
- Fastener hole repair
- Oversize fastener installation

## Component Coverage

### 57-10-10 Forward Spar
Standard repairs include:
- Cap laminate damage (scarf repair)
- Web delamination (injection repair)
- Splice joint fastener hole repair
- Doubler design for impact damage

### 57-10-20 Rear Spar
Standard repairs include:
- Actuator cutout reinforcement repair
- Hinge fitting crack repair/replacement
- Web damage composite patch

### 57-10-40 Skin Panels
Standard repairs include:
- Lightning strike damage repair
- Impact damage repair (hail, bird strike, tool drop)
- Delamination repair (injection or scarf)
- Panel replacement procedures
- Doubler installation (bonded, bolted, hybrid)

## Repair Process Steps

### Damage Assessment
1. Document damage (photos, measurements, sketches)
2. Classify damage category
3. Determine repair scheme
4. Obtain engineering approval (if required)

### Damage Removal
1. Mark repair area
2. Remove damaged material (grinding, routing, drilling)
3. Taper edges per repair scheme
4. Inspect for full extent of damage

### Surface Preparation
1. Clean repair area
2. Remove contaminants
3. Abrade or grit blast bonding surfaces
4. Apply primers or coupling agents (if required)

### Repair Material Installation
1. Cut repair plies to size and orientation
2. Apply adhesive or wet layup resin
3. Install repair plies or doublers
4. Apply vacuum bag and cure

### Post-Repair Operations
1. Trim and sand to final contour
2. Apply surface finishes
3. Install fasteners (if bolted repair)
4. Apply sealants
5. Restore lightning protection

### Post-Repair Inspection
1. Visual inspection (surface condition, flush)
2. NDT inspection (ultrasonic, thermography)
3. Verify acceptance criteria met
4. Document repair in aircraft records

## Acceptance Criteria

Post-repair acceptance defined in:
- `../../../../contracts/schemas/acceptance.metric.schema.json`
- Component-specific acceptance limits
- NDT acceptance standards

Common acceptance criteria:
- No voids > 1 mm² in bondlines
- Surface flush within ±0.5 mm
- No delaminations detectable by NDT
- Fastener torque per specification
- Lightning bond resistance within limits

## Material Specifications

Repair materials must match:
- Original material specifications (when possible)
- Approved substitute materials (when specified)
- Material batch tracking and OOC compliance

Common repair materials:
- Composite prepreg (same resin system as original)
- Wet layup fabrics and resins
- Adhesive films (FM-300, AF-163, etc.)
- Fasteners (same or approved substitute)
- Sealants (fuel-resistant for tank areas)

## ATA-20 Form References

- **FORM-QA-20-10-01**: Composite Fastening (if bolted repair)
- **FORM-QA-20-10-02**: Adhesive Bonding (bonded repairs)
- **FORM-QA-20-30-01**: Material Handling/OOC (repair materials)
- **FORM-QA-20-40-01**: EMI Continuity (lightning protection restoration)

## Engineering Approval

Repairs requiring engineering disposition:
- Damage exceeding standard repair limits
- Non-standard repair schemes
- Repairs in critical structure
- Multiple or adjacent repairs
- Repairs affecting other systems

Engineering package must include:
- Stress analysis and substantiation
- Repair drawing or procedure
- Material specifications
- Inspection requirements
- Configuration control

## Configuration Control

All repairs must be:
- Documented in aircraft maintenance records
- Captured in configuration management system
- Recorded with effectivity and applicability
- Tracked for recurring inspection requirements

## References

- **Descriptive modules**: `../../descriptive/` for component details
- **Acceptance criteria**: `../../../../contracts/schemas/acceptance.metric.schema.json`
- **Material specs**: `../../../../compliance/allowables/`
- **Evidence**: `../../../../evidence/` for repair records

---

*Part of ATA-57-10 procedural documentation*
