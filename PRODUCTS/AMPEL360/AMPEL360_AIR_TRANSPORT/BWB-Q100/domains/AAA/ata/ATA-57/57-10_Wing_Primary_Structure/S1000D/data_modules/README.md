---
id: ATA-57-10-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-10_Wing_Primary_Structure/README.md
llc: SYSTEMS
title: "ATA-57-10: Wing Primary Structure — BWB-Q100"
configuration: baseline
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.1.0"
release_date: 2025-09-24
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# ATA-57-10 — Wing Primary Structure (BWB-Q100)

**Primary load-bearing wing structure:** forward/rear spars, ribs, skins, stringers, and fittings, including their interfaces, inspections, R/I procedures, repairs, and IPD.

> **Golden rule:** Knowledge lives here (ATA); compute lives in **CAX/QOX**; deployable packages live in **PAx**.

---

## At a Glance

| Aspect | Summary |
|--------|---------|
| **Scope** | Primary wing structure (spars, ribs, skins, stringers, fittings) |
| **Key Standards** | S1000D Issue 6.0, ATA-100, ARP4754A/4761-lite |
| **Data Modules** | 85 total (50 Descriptive, 21 Inspection, 6 R/I, 5 Repair, 16 IPD) |
| **Core Interfaces** | ATA-57-20 (Control Surfaces), ATA-53 (Fuselage), ATA-57-50 (Systems) |
| **Quality System** | BREX validation, UTCS/QS provenance, CI/CD enforced |

---

## Quick Start

This directory is the **single source of truth** for the BWB-Q100 wing primary structure. Here's how to use it:

1. **Find a Procedure:** Need to inspect a forward spar? Navigate to [`S1000D/data_modules/procedural/inspection/57-10-10_Forward_Spar/`](./procedural/inspection/57-10-10_Forward_Spar/).
2. **Find a Part Number:** Looking for a specific fitting? Check the Illustrated Parts Data (IPD) in [`S1000D/data_modules/ipd/`](./ipd/).
3. **Understand the Structure:** See the [Directory Breakdown](#directory-breakdown) for a map of all folders and their purpose.
4. **Validate Compliance:** All changes are validated by our CI pipeline against [BREX rules](../BREX/BREX.xml) and [JSON schemas](../../contracts/schemas/).

---

## Core Concepts

### The ATA Pattern
We follow the standard ATA 4-digit subchapter pattern (`ATA-57/57-10_*`) with S1000D content organized underneath. This ensures consistency and discoverability across the entire aircraft documentation set.

### The TFA Bridge
All work flows through the **TFA V2** process: `CB→QB→UE/FE→FWD→QS`. This framework governs everything from initial concepts (CB) to the final, cryptographically-sealed release state (QS).

### 360IPCirq
Our unique "Removal/Installation to Illustrated Parts Catalog" bridge ensures that any part removed for repair can be seamlessly tracked for reuse, maintenance, or replacement, linking procedural steps directly to part numbers in the IPD.

---

## Scope & Applicability

### Includes
- **Structural Components**
  - Forward & rear spars (caps, webs, splices)
  - Ribs (main, intermediate, auxiliary)
  - Skin panels (upper/lower, inboard/outboard)
  - Stringers (upper/lower, spanwise)
  - Major fittings (wing-to-fuselage, engine mount, landing gear, control surface hinges)
- **Documentation Types**
  - Technical descriptions and specifications
  - Inspection procedures (visual, NDT methods)
  - Removal & installation procedures
  - Standard repair procedures
  - Illustrated Parts Data (IPD)
- **Interfaces**
  - Control surface attachment points
  - System provisions (actuator cutouts, routing)
  - Fuel system interfaces

### Excludes
- Flight control functionality and signaling (see [ATA-27](../27_Flight_Controls/README.md))
- Hydraulic/electric actuation systems (see [ATA-29](../29_Hydraulics/README.md) / [ATA-24](../24_Electrical_Power/README.md))
- Aerodynamic performance analyses (referenced via CAx/ICDs)

### Effectivity
This documentation applies to all BWB-Q100 aircraft unless otherwise specified in the effectivity rules within individual data modules.

---

## Pattern Compliance

### ATA Pattern Structure
- **Root Level:** `ATA-57/57-10_Wing_Primary_Structure/` (4-digit subchapter)
- **S1000D Organization:** All S1000D content is placed below the 4-digit node
- **File Naming:** Follows S1000D Issue 6.0 DMC convention with 2-digit ATA fields
- **No Heavy Data:** CAx/QOx data is referenced via [`io/routing.manifest.yaml`](io/routing.manifest.yaml) and S1000D cross-refs

### Compliance Requirements
- All DMs must validate against [BREX rules](../BREX/BREX.xml)
- All DMs must be listed in [DMRL](../DMRL/DMRL.xml)
- All DMs must follow the corrected DMC pattern with 2-digit fields
- All procedural DMs must reference appropriate ATA-20 forms

---

## Directory Breakdown

```
57-10_Wing_Primary_Structure/
├── S1000D/                 # S1000D CSDB content (DMRL, BREX, Data Modules)
│   ├── data_modules/
│   │   ├── descriptive/   # Technical descriptions & specifications
│   │   ├── procedural/    # Inspection, R/I, and repair procedures
│   │   └── ipd/           # Illustrated Parts Catalog
├── compliance/             # Material allowables, loads, and stress analysis
├── contracts/              # JSON schemas and interface control documents
├── evidence/               # Test results, NDT reports, and quality records
├── icd/                    # Interface Control Documents with other systems
└── io/                     # Data flow and routing manifests
```

*See the [fully hyperlinked directory tree](#directory-tree) for complete navigation.*

---

## Directory Tree

*   [57-10_Wing_Primary_Structure/](../../)
    *   [S1000D/](../)
        *   [BREX/](../BREX/)
            *   [BREX.xml](../BREX/BREX.xml) *(Business Rules Exchange - S1000D validation rules)*
            *   [README.md](../BREX/README.md)
        *   [DMRL/](../DMRL/)
            *   [DMRL.xml](../DMRL/DMRL.xml) *(Data Module Requirements List)*
            *   [README.md](../DMRL/README.md)
        *   [data_modules/](./)
            *   [descriptive/](./descriptive/)
                *   [57-10-10_Forward_Spar/](./descriptive/57-10-10_Forward_Spar/)
                *   [57-10-20_Rear_Spar/](./descriptive/57-10-20_Rear_Spar/)
                *   [57-10-30_Ribs/](./descriptive/57-10-30_Ribs/)
                *   [57-10-40_Skin_Panels/](./descriptive/57-10-40_Skin_Panels/)
                *   [57-10-50_Stringers/](./descriptive/57-10-50_Stringers/)
                *   [57-10-60_Attachments/](./descriptive/57-10-60_Attachments/)
                *   [README.md](./descriptive/README.md)
            *   [procedural/](./procedural/)
                *   [inspection/](./procedural/inspection/)
                    *   [57-10-10_Forward_Spar/](./procedural/inspection/57-10-10_Forward_Spar/)
                    *   [57-10-20_Rear_Spar/](./procedural/inspection/57-10-20_Rear_Spar/)
                    *   [57-10-30_Ribs/](./procedural/inspection/57-10-30_Ribs/)
                    *   [57-10-40_Skin_Panels/](./procedural/inspection/57-10-40_Skin_Panels/)
                    *   [57-10-50_Stringers/](./procedural/inspection/57-10-50_Stringers/)
                    *   [57-10-60_Attachments/](./procedural/inspection/57-10-60_Attachments/)
                    *   [README.md](./procedural/inspection/README.md)
                *   [removal_installation/](./procedural/removal_installation/)
                *   [repair/](./procedural/repair/)
                *   [README.md](./procedural/README.md)
            *   [ipd/](./ipd/)
                *   [57-10-10_Forward_Spar/](./ipd/57-10-10_Forward_Spar/)
                *   [57-10-20_Rear_Spar/](./ipd/57-10-20_Rear_Spar/)
                *   [57-10-30_Ribs/](./ipd/57-10-30_Ribs/)
                *   [57-10-40_Skin_Panels/](./ipd/57-10-40_Skin_Panels/)
                *   [57-10-50_Stringers/](./ipd/57-10-50_Stringers/)
                *   [57-10-60_Attachments/](./ipd/57-10-60_Attachments/)
                *   [README.md](./ipd/README.md)
            *   [README.md](../README.md)
    *   [compliance/](../../compliance/)
        *   [allowables/](../../compliance/allowables/)
            *   [index.md](../../compliance/allowables/index.md) *(Material allowables database index)*
            *   [README.md](../../compliance/allowables/README.md)
        *   [loads/](../../compliance/loads/)
            *   [index.md](../../compliance/loads/index.md) *(Design load cases, limit/ultimate loads)*
            *   [README.md](../../compliance/loads/README.md)
        *   [stress/](../../compliance/stress/)
            *   [index.md](../../compliance/stress/index.md) *(Stress analysis reports, margin of safety)*
            *   [README.md](../../compliance/stress/README.md)
        *   [README.md](../../compliance/README.md)
    *   [contracts/](../../contracts/)
        *   [schemas/](../../contracts/schemas/)
            *   [acceptance.metric.schema.json](../../contracts/schemas/acceptance.metric.schema.json) *(Acceptance criteria data structure)*
            *   [attachment.fitting.schema.json](../../contracts/schemas/attachment.fitting.schema.json) *(Fitting interface definition)*
            *   [fastener.set.schema.json](../../contracts/schemas/fastener.set.schema.json) *(Fastener specification format)*
            *   [joint.schema.json](../../contracts/schemas/joint.schema.json) *(Joint design parameters)*
            *   [laminate.stack.schema.json](../../contracts/schemas/laminate.stack.schema.json) *(Composite layup definition)*
            *   [README.md](../../contracts/schemas/README.md)
        *   [ICD-AAA-ATA-57-10.md](../../contracts/ICD-AAA-ATA-57-10.md) *(Master ICD for wing primary structure)*
        *   [README.md](../../contracts/README.md)
    *   [evidence/](../../evidence/)
        *   [coupons/](../../evidence/coupons/)
            *   [index.md](../../evidence/coupons/index.md) *(Coupon test results, material qualification)*
            *   [README.md](../../evidence/coupons/README.md)
        *   [ndt/](../../evidence/ndt/)
            *   [index.md](../../evidence/ndt/index.md) *(NDT reports, calibration records)*
            *   [README.md](../../evidence/ndt/README.md)
        *   [tests/](../../evidence/tests/)
            *   [index.md](../../evidence/tests/index.md) *(Component tests, full-scale testing)*
            *   [README.md](../../evidence/tests/README.md)
        *   [README.md](../../evidence/README.md)
    *   [icd/](../../icd/)
        *   [ICD-57-10-53_Fuselage_Attachments.md](../../icd/ICD-57-10-53_Fuselage_Attachments.md) *(Interface to ATA-53 fuselage structure)*
        *   [ICD-57-10-57-20_Control_Surfaces.md](../../icd/ICD-57-10-57-20_Control_Surfaces.md) *(Interface to ATA-57-20 control surfaces)*
        *   [ICD-57-10-57-50_Systems_Provisions.md](../../icd/ICD-57-10-57-50_Systems_Provisions.md) *(Interface to ATA-57-50 systems installations)*
        *   [README.md](../../icd/README.md)
    *   [io/](../../io/)
        *   [README.md](../../io/README.md)
        *   [routing.manifest.yaml](../../io/routing.manifest.yaml) *(Data flow routing configuration)*


---

## Complete Data Module Index

### Descriptive Modules (040A) - 50 Modules

#### Forward Spar (10 Modules)
- [DMC-BWQ1-A-57-10-10-00-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-00-00A-040A-D-EN-US.xml) - Forward Spar - General Description and Architecture
- [DMC-BWQ1-A-57-10-10-01-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-01-00A-040A-D-EN-US.xml) - Forward Spar Inboard Section LH - Material, Geometry, Fastener Pattern
- [DMC-BWQ1-A-57-10-10-02-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-02-00A-040A-D-EN-US.xml) - Forward Spar Inboard Section RH - Material, Geometry, Fastener Pattern
- [DMC-BWQ1-A-57-10-10-03-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-03-00A-040A-D-EN-US.xml) - Forward Spar Mid Section LH - Splice Joints, Load Transfer
- [DMC-BWQ1-A-57-10-10-04-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-04-00A-040A-D-EN-US.xml) - Forward Spar Mid Section RH - Splice Joints, Load Transfer
- [DMC-BWQ1-A-57-10-10-05-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-05-00A-040A-D-EN-US.xml) - Forward Spar Outboard Section LH - Taper, Tip Attachment
- [DMC-BWQ1-A-57-10-10-06-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-06-00A-040A-D-EN-US.xml) - Forward Spar Outboard Section RH - Taper, Tip Attachment
- [DMC-BWQ1-A-57-10-10-07-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-07-00A-040A-D-EN-US.xml) - Forward Spar Upper Cap - Composite Layup, Stringer Runouts
- [DMC-BWQ1-A-57-10-10-08-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-08-00A-040A-D-EN-US.xml) - Forward Spar Lower Cap - Composite Layup, Fuel Seal Interface
- [DMC-BWQ1-A-57-10-10-09-00A-040A-D-EN-US.xml](./descriptive/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-09-00A-040A-D-EN-US.xml) - Forward Spar Web - Shear Panel, Stiffeners, Lightening Holes

#### Rear Spar (10 Modules)
- [DMC-BWQ1-A-57-10-20-00-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-00-00A-040A-D-EN-US.xml) - Rear Spar - General Description and Load Paths
- [DMC-BWQ1-A-57-10-20-01-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-01-00A-040A-D-EN-US.xml) - Rear Spar Inboard Section LH - Landing Gear Beam Interface
- [DMC-BWQ1-A-57-10-20-02-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-02-00A-040A-D-EN-US.xml) - Rear Spar Inboard Section RH - Landing Gear Beam Interface
- [DMC-BWQ1-A-57-10-20-03-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-03-00A-040A-D-EN-US.xml) - Rear Spar Mid Section LH - Control Surface Hinge Locations
- [DMC-BWQ1-A-57-10-20-04-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-04-00A-040A-D-EN-US.xml) - Rear Spar Mid Section RH - Control Surface Hinge Locations
- [DMC-BWQ1-A-57-10-20-05-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-05-00A-040A-D-EN-US.xml) - Rear Spar Outboard Section LH - Aileron Support Structure
- [DMC-BWQ1-A-57-10-20-06-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-06-00A-040A-D-EN-US.xml) - Rear Spar Outboard Section RH - Aileron Support Structure
- [DMC-BWQ1-A-57-10-20-07-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-07-00A-040A-D-EN-US.xml) - Rear Spar Upper Cap - Tension Loads, Splice Design
- [DMC-BWQ1-A-57-10-20-08-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-08-00A-040A-D-EN-US.xml) - Rear Spar Lower Cap - Compression Loads, Anti-Buckling
- [DMC-BWQ1-A-57-10-20-09-00A-040A-D-EN-US.xml](./descriptive/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-09-00A-040A-D-EN-US.xml) - Rear Spar Web - Shear Transfer, Actuator Cutouts

#### Ribs (7 Modules)
- [DMC-BWQ1-A-57-10-30-00-00A-040A-D-EN-US.xml](./descriptive/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-00-00A-040A-D-EN-US.xml) - Ribs - General Description, Numbering System, Load Distribution
- [DMC-BWQ1-A-57-10-30-01-00A-040A-D-EN-US.xml](./descriptive/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-01-00A-040A-D-EN-US.xml) - Main Ribs LH (RIB 1-10) - Heavy Ribs, Fuel Tank Boundaries
- [DMC-BWQ1-A-57-10-30-02-00A-040A-D-EN-US.xml](./descriptive/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-02-00A-040A-D-EN-US.xml) - Main Ribs RH (RIB 1-10) - Heavy Ribs, Fuel Tank Boundaries
- [DMC-BWQ1-A-57-10-30-03-00A-040A-D-EN-US.xml](./descriptive/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-03-00A-040A-D-EN-US.xml) - Intermediate Ribs LH - Stiffening, Skin Panel Support
- [DMC-BWQ1-A-57-10-30-04-00A-040A-D-EN-US.xml](./descriptive/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-04-00A-040A-D-EN-US.xml) - Intermediate Ribs RH - Stiffening, Skin Panel Support
- [DMC-BWQ1-A-57-10-30-05-00A-040A-D-EN-US.xml](./descriptive/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-05-00A-040A-D-EN-US.xml) - Auxiliary Ribs - Local Reinforcements, System Provisions
- [DMC-BWQ1-A-57-10-30-06-00A-040A-D-EN-US.xml](./descriptive/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-06-00A-040A-D-EN-US.xml) - Rib Attachments/Fittings - Spar Clips, Flange Connections

#### Skin Panels (13 Modules)
- [DMC-BWQ1-A-57-10-40-00-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-00-00A-040A-D-EN-US.xml) - Skin Panels - General Description, Panel Layout, Access Doors
- [DMC-BWQ1-A-57-10-40-01-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-01-00A-040A-D-EN-US.xml) - Upper Skin Inboard LH - Panel Boundaries, Thickness Schedule
- [DMC-BWQ1-A-57-10-40-02-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-02-00A-040A-D-EN-US.xml) - Upper Skin Inboard RH - Panel Boundaries, Thickness Schedule
- [DMC-BWQ1-A-57-10-40-03-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-03-00A-040A-D-EN-US.xml) - Upper Skin Mid LH - Splice Joints, Inspection Access
- [DMC-BWQ1-A-57-10-40-04-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-04-00A-040A-D-EN-US.xml) - Upper Skin Mid RH - Splice Joints, Inspection Access
- [DMC-BWQ1-A-57-10-40-05-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-05-00A-040A-D-EN-US.xml) - Upper Skin Outboard LH - Anti-icing Provisions, Lightning Protection
- [DMC-BWQ1-A-57-10-40-06-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-06-00A-040A-D-EN-US.xml) - Upper Skin Outboard RH - Anti-icing Provisions, Lightning Protection
- [DMC-BWQ1-A-57-10-40-07-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-07-00A-040A-D-EN-US.xml) - Lower Skin Inboard LH - Fuel Tank Sealing, Drain Provisions
- [DMC-BWQ1-A-57-10-40-08-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-08-00A-040A-D-EN-US.xml) - Lower Skin Inboard RH - Fuel Tank Sealing, Drain Provisions
- [DMC-BWQ1-A-57-10-40-09-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-09-00A-040A-D-EN-US.xml) - Lower Skin Mid LH - Landing Gear Door Interface
- [DMC-BWQ1-A-57-10-40-10-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-10-00A-040A-D-EN-US.xml) - Lower Skin Mid RH - Landing Gear Door Interface
- [DMC-BWQ1-A-57-10-40-11-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-11-00A-040A-D-EN-US.xml) - Lower Skin Outboard LH - Outer Wing Panel, Navigation Light
- [DMC-BWQ1-A-57-10-40-12-00A-040A-D-EN-US.xml](./descriptive/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-12-00A-040A-D-EN-US.xml) - Lower Skin Outboard RH - Outer Wing Panel, Navigation Light

#### Stringers (5 Modules)
- [DMC-BWQ1-A-57-10-50-00-00A-040A-D-EN-US.xml](./descriptive/57-10-50_Stringers/DMC-BWQ1-A-57-10-50-00-00A-040A-D-EN-US.xml) - Stringers - General Description, Spanwise Arrangement
- [DMC-BWQ1-A-57-10-50-01-00A-040A-D-EN-US.xml](./descriptive/57-10-50_Stringers/DMC-BWQ1-A-57-10-50-01-00A-040A-D-EN-US.xml) - Upper Stringers LH - Compression Members, Section Properties
- [DMC-BWQ1-A-57-10-50-02-00A-040A-D-EN-US.xml](./descriptive/57-10-50_Stringers/DMC-BWQ1-A-57-10-50-02-00A-040A-D-EN-US.xml) - Upper Stringers RH - Compression Members, Section Properties
- [DMC-BWQ1-A-57-10-50-03-00A-040A-D-EN-US.xml](./descriptive/57-10-50_Stringers/DMC-BWQ1-A-57-10-50-03-00A-040A-D-EN-US.xml) - Lower Stringers LH - Tension Members, Splices
- [DMC-BWQ1-A-57-10-50-04-00A-040A-D-EN-US.xml](./descriptive/57-10-50_Stringers/DMC-BWQ1-A-57-10-50-04-00A-040A-D-EN-US.xml) - Lower Stringers RH - Tension Members, Splices

#### Attachments (5 Modules)
- [DMC-BWQ1-A-57-10-60-00-00A-040A-D-EN-US.xml](./descriptive/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-00-00A-040A-D-EN-US.xml) - Attachments - General Description, Fitting Design Philosophy
- [DMC-BWQ1-A-57-10-60-01-00A-040A-D-EN-US.xml](./descriptive/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-01-00A-040A-D-EN-US.xml) - Wing-to-Fuselage Fittings - Center Section, Main Pins
- [DMC-BWQ1-A-57-10-60-02-00A-040A-D-EN-US.xml](./descriptive/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-02-00A-040A-D-EN-US.xml) - Engine Mount Fittings - Thrust/Vertical Load Transfer
- [DMC-BWQ1-A-57-10-60-03-00A-040A-D-EN-US.xml](./descriptive/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-03-00A-040A-D-EN-US.xml) - Landing Gear Beam Fittings - Main Gear Attachment Points
- [DMC-BWQ1-A-57-10-60-04-00A-040A-D-EN-US.xml](./descriptive/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-04-00A-040A-D-EN-US.xml) - Control Surface Hinge Fittings - Moment Transfer, Bushing Details

---

### Inspection Modules (520A) - 21 Modules

#### Forward Spar Inspection (7 Modules)
- [DMC-BWQ1-A-57-10-10-00-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-00-00A-520A-D-EN-US.xml) - Forward Spar Inspection - Visual, NDT Methods, Intervals
- [DMC-BWQ1-A-57-10-10-01-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-01-00A-520A-D-EN-US.xml) - Inboard Section LH Inspection - Critical Zones, Crack Initiation Sites
- [DMC-BWQ1-A-57-10-10-02-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-02-00A-520A-D-EN-US.xml) - Inboard Section RH Inspection - Critical Zones, Crack Initiation Sites
- [DMC-BWQ1-A-57-10-10-03-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-03-00A-520A-D-EN-US.xml) - Mid Section LH Inspection - Splice Joint Eddy Current
- [DMC-BWQ1-A-57-10-10-04-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-04-00A-520A-D-EN-US.xml) - Mid Section RH Inspection - Splice Joint Eddy Current
- [DMC-BWQ1-A-57-10-10-05-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-05-00A-520A-D-EN-US.xml) - Outboard Section LH Inspection - Tip Attachment Ultrasonic
- [DMC-BWQ1-A-57-10-10-06-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-06-00A-520A-D-EN-US.xml) - Outboard Section RH Inspection - Tip Attachment Ultrasonic

#### Rear Spar Inspection (5 Modules)
- [DMC-BWQ1-A-57-10-20-00-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-00-00A-520A-D-EN-US.xml) - Rear Spar Inspection - Visual, UT, Thermography Procedures
- [DMC-BWQ1-A-57-10-20-01-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-01-00A-520A-D-EN-US.xml) - Inboard Section LH Inspection - Gear Beam Bolt Holes
- [DMC-BWQ1-A-57-10-20-02-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-02-00A-520A-D-EN-US.xml) - Inboard Section RH Inspection - Gear Beam Bolt Holes
- [DMC-BWQ1-A-57-10-20-03-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-03-00A-520A-D-EN-US.xml) - Mid Section LH Inspection - Hinge Fitting Integrity
- [DMC-BWQ1-A-57-10-20-04-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-04-00A-520A-D-EN-US.xml) - Mid Section RH Inspection - Hinge Fitting Integrity

#### Ribs Inspection (3 Modules)
- [DMC-BWQ1-A-57-10-30-00-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-00-00A-520A-D-EN-US.xml) - Ribs Inspection - Visual, Tap Test, Access Requirements
- [DMC-BWQ1-A-57-10-30-01-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-01-00A-520A-D-EN-US.xml) - Main Ribs Inspection - Corrosion Check, Fastener Condition
- [DMC-BWQ1-A-57-10-30-02-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-02-00A-520A-D-EN-US.xml) - Intermediate Ribs Inspection - Web Buckling, Flange Cracks

#### Skin Panels Inspection (3 Modules)
- [DMC-BWQ1-A-57-10-40-00-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-00-00A-520A-D-EN-US.xml) - Skin Panels Inspection - Surface Condition, Delamination Check
- [DMC-BWQ1-A-57-10-40-01-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-01-00A-520A-D-EN-US.xml) - Upper Skin Inspection - Lightning Strike Damage, Erosion
- [DMC-BWQ1-A-57-10-40-02-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-02-00A-520A-D-EN-US.xml) - Lower Skin Inspection - Impact Damage, Fuel Leak Evidence

#### Stringers Inspection (1 Module)
- [DMC-BWQ1-A-57-10-50-00-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-50_Stringers/DMC-BWQ1-A-57-10-50-00-00A-520A-D-EN-US.xml) - Stringers Inspection - Debond Detection, Runout Condition

#### Attachments Inspection (2 Modules)
- [DMC-BWQ1-A-57-10-60-00-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-00-00A-520A-D-EN-US.xml) - Fittings Inspection - Visual, Dye Penetrant Schedule
- [DMC-BWQ1-A-57-10-60-01-00A-520A-D-EN-US.xml](./procedural/inspection/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-01-00A-520A-D-EN-US.xml) - Critical Fittings NDT - UT/MPI at Life Limits

---

### Removal/Installation Modules (720A) - 6 Modules

#### Forward Spar R/I (3 Modules)
- [DMC-BWQ1-A-57-10-10-00-00A-720A-D-EN-US.xml](./procedural/removal_installation/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-00-00A-720A-D-EN-US.xml) - Forward Spar R/I - General Precautions, Tooling Requirements
- [DMC-BWQ1-A-57-10-10-01-00A-720A-D-EN-US.xml](./procedural/removal_installation/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-01-00A-720A-D-EN-US.xml) - Inboard Section LH R/I - Fuel Drain, Fastener Sequence
- [DMC-BWQ1-A-57-10-10-02-00A-720A-D-EN-US.xml](./procedural/removal_installation/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-02-00A-720A-D-EN-US.xml) - Inboard Section RH R/I - Fuel Drain, Fastener Sequence

#### Rear Spar R/I (2 Modules)
- [DMC-BWQ1-A-57-10-20-00-00A-720A-D-EN-US.xml](./procedural/removal_installation/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-00-00A-720A-D-EN-US.xml) - Rear Spar R/I - Hinge Removal, Gear Beam Support
- [DMC-BWQ1-A-57-10-20-01-00A-720A-D-EN-US.xml](./procedural/removal_installation/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-01-00A-720A-D-EN-US.xml) - Inboard Section LH R/I - Heavy Lift Procedure

#### Skin Panels R/I (1 Module)
- [DMC-BWQ1-A-57-10-40-00-00A-720A-D-EN-US.xml](./procedural/removal_installation/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-00-00A-720A-D-EN-US.xml) - Skin Panel R/I - Sealing, Torque Values, Inspection Access

---

### Repair Modules (520A) - 5 Modules

#### Forward Spar Repair (1 Module)
- [DMC-BWQ1-A-57-10-10-00-00A-520A-D-EN-US.xml](./procedural/repair/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-00-00A-520A-D-EN-US.xml) - Forward Spar Repair - Allowable Damage Limits, Doubler Design

#### Rear Spar Repair (1 Module)
- [DMC-BWQ1-A-57-10-20-00-00A-520A-D-EN-US.xml](./procedural/repair/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-00-00A-520A-D-EN-US.xml) - Rear Spar Repair - Composite Patch Procedures

#### Skin Panels Repair (3 Modules)
- [DMC-BWQ1-A-57-10-40-00-00A-520A-D-EN-US.xml](./procedural/repair/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-00-00A-520A-D-EN-US.xml) - Skin Panel Repair - Damage Categories, Repair Schemes
- [DMC-BWQ1-A-57-10-40-01-00A-520A-D-EN-US.xml](./procedural/repair/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-01-00A-520A-D-EN-US.xml) - Doubler Installation - Bonded, Bolted, Hybrid
- [DMC-BWQ1-A-57-10-40-02-00A-520A-D-EN-US.xml](./procedural/repair/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-02-00A-520A-D-EN-US.xml) - Panel Replacement - Full Panel Change, Sealing

---

### IPD Modules (941A) - 16 Modules

#### Forward Spar IPD (4 Modules)
- [DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml](./ipd/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml) - Forward Spar IPD - Parts Catalog, Applicability
- [DMC-BWQ1-A-57-10-10-01-00A-941A-D-EN-US.xml](./ipd/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-01-00A-941A-D-EN-US.xml) - Inboard Sections IPD - Part Numbers, Quantities
- [DMC-BWQ1-A-57-10-10-02-00A-941A-D-EN-US.xml](./ipd/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-02-00A-941A-D-EN-US.xml) - Mid Sections IPD - Splice Kit Components
- [DMC-BWQ1-A-57-10-10-03-00A-941A-D-EN-US.xml](./ipd/57-10-10_Forward_Spar/DMC-BWQ1-A-57-10-10-03-00A-941A-D-EN-US.xml) - Outboard Sections IPD - Tip Attachments

#### Rear Spar IPD (3 Modules)
- [DMC-BWQ1-A-57-10-20-00-00A-941A-D-EN-US.xml](./ipd/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-00-00A-941A-D-EN-US.xml) - Rear Spar IPD - Parts Catalog, Hinge Kits
- [DMC-BWQ1-A-57-10-20-01-00A-941A-D-EN-US.xml](./ipd/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-01-00A-941A-D-EN-US.xml) - Inboard Sections IPD - Gear Beam Hardware
- [DMC-BWQ1-A-57-10-20-02-00A-941A-D-EN-US.xml](./ipd/57-10-20_Rear_Spar/DMC-BWQ1-A-57-10-20-02-00A-941A-D-EN-US.xml) - Mid Sections IPD - Control Surface Brackets

#### Ribs IPD (3 Modules)
- [DMC-BWQ1-A-57-10-30-00-00A-941A-D-EN-US.xml](./ipd/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-00-00A-941A-D-EN-US.xml) - Ribs IPD General - Part Numbers by Station
- [DMC-BWQ1-A-57-10-30-01-00A-941A-D-EN-US.xml](./ipd/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-01-00A-941A-D-EN-US.xml) - Main Ribs IPD - Heavy Rib Assemblies
- [DMC-BWQ1-A-57-10-30-02-00A-941A-D-EN-US.xml](./ipd/57-10-30_Ribs/DMC-BWQ1-A-57-10-30-02-00A-941A-D-EN-US.xml) - Intermediate Ribs IPD - Standard Rib Kit

#### Skin Panels IPD (1 Module)
- [DMC-BWQ1-A-57-10-40-00-00A-941A-D-EN-US.xml](./ipd/57-10-40_Skin_Panels/DMC-BWQ1-A-57-10-40-00-00A-941A-D-EN-US.xml) - Skin Panels IPD - Panel P/Ns, Fastener Kits

#### Stringers IPD (1 Module)
- [DMC-BWQ1-A-57-10-50-00-00A-941A-D-EN-US.xml](./ipd/57-10-50_Stringers/DMC-BWQ1-A-57-10-50-00-00A-941A-D-EN-US.xml) - Stringers IPD - Stringer Assemblies by Zone

#### Attachments IPD (1 Module)
- [DMC-BWQ1-A-57-10-60-00-00A-941A-D-EN-US.xml](./ipd/57-10-60_Attachments/DMC-BWQ1-A-57-10-60-00-00A-941A-D-EN-US.xml) - Fittings IPD - Critical Fitting P/Ns, Hardware

---

## Summary

| Module Type | Count | Description |
|-----------|-----------|
| **Descriptive (040A)** | 50 modules |
| **Inspection (520A)** | 21 modules |
| **R/I (720A)** | 6 modules |
| **Repair (520A)** | 5 modules |
| **IPD (941A)** | 16 modules |
| **Total** | **85 modules** |

---

## S1000D Data Modules

This chapter is managed as a complete S1000D CSDB (Common Source Data Base) with **85 data modules**.

- **Descriptive (040A):** 50 modules defining the "what" - technical specs, materials, and architecture.
- **Inspection (520A):** 21 modules defining the "how" - procedures for visual and NDT inspection.
- **Removal/Installation (720A):** 6 modules for maintenance tasks.
- **Repair (520A):** 5 modules for standard repair procedures.
- **IPD (941A):** 16 modules for the Illustrated Parts Catalog.

> **See the complete, hyperlinkable [S1000D Data Module List](./S1000D_Data_Module_List.md) for a detailed index of every module.

---

## Interfaces & Dependencies

This chapter does not exist in isolation. It has critical interfaces with:

- **[ATA-57-20 Control Surfaces](../57-20_Control_Surfaces/README.md):** Defines hinge & bracket locations, stiffness, and clearances.
- **[ATA-53 Fuselage Structure](../53_Fuselage/README.md):** Defines center section & wing-to-body attachments.
- **[ATA-57-50 Systems Provisions](../57-50_Systems_Provisions/README.md):** Defines actuator cutouts, cable/pipe penetrations, and system routing.

---

## 360IPCirq (R/I → IPC Reusability Bridge)

### Purpose
The 360IPCirq bridge enables seamless tracking of parts removed for repair, maintenance, or replacement by linking procedural steps directly to part numbers in the IPD.

### Implementation
- Every **720A** R/I DM enumerates removal kits, torque sequences, sealants, and fittings
- Uses the same item keys as **941A** IPD figures/items
- Enables "removal for repair → IPC 360 reusability"

### Key Benefits
- Complete traceability from procedure to part number
- Efficient inventory management
- Simplified maintenance workflows
- Reduced risk of part misidentification

### Where to Find It
- R/I procedures: [`S1000D/data_modules/procedural/removal_installation/`](./procedural/removal_installation/)
- IPD catalogs: [`S1000D/data_modules/ipd/`](./ipd/)
- Contract definitions: [`contracts/ICD-AAA-ATA-57-10.md`](../../contracts/ICD-AAA-ATA-57-10.md)

---

## Mandatory Forms (ATA-20)

We do not duplicate standard practice forms here. Instead, we link to the canonical sources in **ATA-20**:

- [Composite Fastening](../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md)
- [Adhesive Bonding](../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md)
- [Cabin Integrity / Leak Test](../../20/20-20_Sealing_and_Pressurization/forms/FORM-QA-20-20-01_Cabin_Integrity_Leak_Test.md)
- [Material Handling & OOC Log](../../20/20-30_Material_Handling/forms/FORM-QA-20-30-01_Material_Handling_OOC_Log.md)
- [Bonding / EMI Continuity](../../20/20-40_Electrical_Bonding/forms/FORM-QA-20-40-01_Bonding_EMI_Continuity.md)

---

## Evidence & QS

### Traceability System
Every action, from material lot numbers to torque values, is indexed under `evidence/` and cross-referenced from the relevant data modules. 

### Evidence Types
- **Material Evidence:** Material certificates, lot numbers, OOC timers
- **Process Evidence:** Torque values, sealant batches, process parameters
- **Test Evidence:** NDT results, test reports, calibration records
- **Inspection Evidence:** Visual inspection reports, photos, videos

### QS Seal Application
A **QS seal** is applied only when:
- All applicable ATA-20 practices are followed
- All acceptance metrics are fully evidenced and referenced
- All validation checks pass
- All required signatures are obtained

### Evidence Management
- Evidence is organized by type in subdirectories under `evidence/`
- Each evidence file is indexed in the respective `index.md` file
- Evidence is linked from data modules using standardized references
- Evidence is version-controlled and archived with UTCS anchors

---

## Validation & CI

### S1000D Validation
- All DMs must validate against [BREX rules](../BREX/BREX.xml)
- All DMs must be listed in [DMRL](../DMRL/DMRL.xml)
- All DMs must follow the corrected DMC pattern with 2-digit fields
- All procedural DMs must reference appropriate ATA-20 forms

### Schema Validation
- JSON instances must pass validation against schemas in [contracts/schemas/](../../contracts/schemas/)
- Schema validation is enforced in the CI pipeline
- Schema changes require version updates and backward compatibility checks

### CI Pipeline
- **Purpose:** Ensures all documentation meets quality standards before release
- **Trigger:** On every push and pull request to the repository
- **Actions:**
  - XML well-formedness checks
  - BREX validation
  - Schema validation
  - Cross-reference integrity checks
  - Evidence link verification
- **Failure:** CI fails closed if any reference is missing or unverifiable
- **Configuration:** See [`.github/workflows/struct-and-brex.yml`](../../../../../../../../../../../.github/workflows/struct-and-brex.yml)

---

## Change Control

### Change Process
1. **Change Request:** Submit a change request with detailed justification
2. **Technical Review:** Engineering review for technical impact
3. **M&P Approval:** Materials & Processes approval for material/process changes
4. **MRB Approval:** Material Review Board approval for structural changes
5. **Documentation Update:** Update all affected documentation
6. **CI Validation:** Pass all CI checks
7. **Release:** Create release tag and update manifests
8. **QS Seal:** Apply QS seal to approved release

### Documentation Updates
- All changes are tracked in the DMRL
- Version numbers follow semantic versioning
- Change notices are documented in release notes
- All changes require approval signatures

### Release Management
- Releases follow **PDM-PLM** change notices
- Manifests and signatures are updated under `io/` and `evidence/`
- Release notes are published with each release

---

## Working with This Documentation

### For Engineers
1. **Finding Information:** Use the directory structure to locate relevant data modules
2. **Understanding Standards:** Refer to [ATA-20](../../20/README.md) for standard practices
3. **Validation:** Run local validation checks before committing changes
4. **Traceability:** Ensure all evidence is properly linked and documented

### For Maintenance Personnel
1. **Procedures:** Follow step-by-step instructions in procedural DMs
2. **Parts Identification:** Use IPD to identify correct parts and quantities
3. **Inspection:** Follow inspection DMs for detailed procedures
4. **Repair:** Follow repair DMs for standard repair procedures

### For Quality Assurance
1. **Compliance:** Verify all procedures follow ATA-20 standards
2. **Evidence:** Ensure all evidence is properly documented and linked
3. **Validation:** Run validation checks on all changes
4. **Audits:** Participate in regular documentation audits

---

## Troubleshooting

### Common Issues
- **Broken Links:** Check file paths and update as needed
- **Validation Failures:** Check BREX rules and schema compliance
- **Missing Evidence:** Ensure all evidence is properly documented
- **Version Conflicts:** Resolve version conflicts in dependencies

### Getting Help
- Check [README.md](../README.md) for general help
- Check [FAQ.md](../FAQ.md) for frequently asked questions
- Contact the [ASI-T Architecture Team](mailto:asi-t-architecture@bwq100.com) for technical support


*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
