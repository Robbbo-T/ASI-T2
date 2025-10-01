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

Primary load-bearing wing structure: forward/rear spars, ribs, skins, stringers and fittings, including their interfaces, inspections, R/I procedures, repairs, and IPD.  
**Golden rule:** knowledge lives here (ATA); compute lives in **CAX/QOX**; deployable packages live in **PAx**.

---

## Quick Nav

- [Scope & Applicability](#scope--applicability)
- [Pattern Compliance](#pattern-compliance)
- [Directory Breakdown](#directory-breakdown)
- [S1000D Data Modules (DMRL-driven)](#s1000d-data-modules-dmrl-driven)
- [Interfaces & Dependencies](#interfaces--dependencies)
- [Mandatory Forms (ATA-20)](#mandatory-forms-ata20)
- [360IPCirq (R/I → IPC Reusability Bridge)](#360ipcirs-ri--ipc-reusability-bridge)
- [Evidence & QS](#evidence--qs)
- [Validation & CI](#validation--ci)
- [Change Control](#change-control)

---

## Scope & Applicability

**Includes**
- Forward & rear spars (caps, webs, splices), ribs, skin panels, stringers, major fittings.
- Inspections (visual/NDT), removal & installation (R/I), standard repairs, and IPD.
- Interfaces to control surfaces (57-20), fuselage structure (53), systems provisions (57-50).

**Excludes**
- Flight control functionality (ATA-27), hydraulic/electric actuation systems (ATA-29/24).
- Aerodynamic performance analyses (referenced via CAx/ICDs).

---

## Pattern Compliance

- **ATA pattern:** `ATA-57/57-10_<Subject>/` *(4-digit subchapter)*, with **S1000D folders placed below the 4-digit node**.  
- **Do not store** heavy CAx/QOx data here—reference via `io/routing.manifest.yaml` and S1000D cross-refs.

---

## Directory Breakdown

> Canonical layout with S1000D content organized under the 4-digit subchapter.

```

57-10_Wing_Primary_Structure/
├── S1000D/
│   ├── BREX/
│   │   ├── BREX.xml                           # Business Rules Exchange - S1000D validation rules
│   │   └── README.md
│   ├── DMRL/
│   │   ├── DMRL.xml                           # Data Module Requirements List
│   │   └── README.md
│   ├── data_modules/
│   │   ├── descriptive/
│   │   │   ├── 57-10-10_Forward_Spar/
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-00-00A-040A-D-EN-US.xml  # Forward Spar - General Description & Architecture
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-01-00A-040A-D-EN-US.xml  # Forward Spar Inboard Section LH - Material, geometry, fastener pattern
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-02-00A-040A-D-EN-US.xml  # Forward Spar Inboard Section RH - Material, geometry, fastener pattern
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-03-00A-040A-D-EN-US.xml  # Forward Spar Mid Section LH - Splice joints, load transfer
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-04-00A-040A-D-EN-US.xml  # Forward Spar Mid Section RH - Splice joints, load transfer
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-05-00A-040A-D-EN-US.xml  # Forward Spar Outboard Section LH - Taper, tip attachment
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-06-00A-040A-D-EN-US.xml  # Forward Spar Outboard Section RH - Taper, tip attachment
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-07-00A-040A-D-EN-US.xml  # Forward Spar Upper Cap - Composite layup, stringer runouts
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-08-00A-040A-D-EN-US.xml  # Forward Spar Lower Cap - Composite layup, fuel seal interface
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-09-00A-040A-D-EN-US.xml  # Forward Spar Web - Shear panel, stiffeners, lightening holes
│   │   │   │   └── README.md
│   │   │   ├── 57-10-20_Rear_Spar/
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-00-00A-040A-D-EN-US.xml  # Rear Spar - General Description & Load Paths
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-01-00A-040A-D-EN-US.xml  # Rear Spar Inboard Section LH - Landing gear beam interface
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-02-00A-040A-D-EN-US.xml  # Rear Spar Inboard Section RH - Landing gear beam interface
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-03-00A-040A-D-EN-US.xml  # Rear Spar Mid Section LH - Control surface hinge locations
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-04-00A-040A-D-EN-US.xml  # Rear Spar Mid Section RH - Control surface hinge locations
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-05-00A-040A-D-EN-US.xml  # Rear Spar Outboard Section LH - Aileron support structure
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-06-00A-040A-D-EN-US.xml  # Rear Spar Outboard Section RH - Aileron support structure
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-07-00A-040A-D-EN-US.xml  # Rear Spar Upper Cap - Tension loads, splice design
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-08-00A-040A-D-EN-US.xml  # Rear Spar Lower Cap - Compression loads, anti-buckling
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-09-00A-040A-D-EN-US.xml  # Rear Spar Web - Shear transfer, actuator cutouts
│   │   │   │   └── README.md
│   │   │   ├── 57-10-30_Ribs/
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-00-00A-040A-D-EN-US.xml  # Ribs - General Description, Numbering System, Load Distribution
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-01-00A-040A-D-EN-US.xml  # Main Ribs LH (RIB 1-10) - Heavy ribs, fuel tank boundaries
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-02-00A-040A-D-EN-US.xml  # Main Ribs RH (RIB 1-10) - Heavy ribs, fuel tank boundaries
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-03-00A-040A-D-EN-US.xml  # Intermediate Ribs LH - Stiffening, skin panel support
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-04-00A-040A-D-EN-US.xml  # Intermediate Ribs RH - Stiffening, skin panel support
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-05-00A-040A-D-EN-US.xml  # Auxiliary Ribs - Local reinforcements, system provisions
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-06-00A-040A-D-EN-US.xml  # Rib Attachments/Fittings - Spar clips, flange connections
│   │   │   │   └── README.md
│   │   │   ├── 57-10-40_Skin_Panels/
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-00-00A-040A-D-EN-US.xml  # Skin Panels - General Description, Panel Layout, Access Doors
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-01-00A-040A-D-EN-US.xml  # Upper Skin Inboard LH - Panel boundaries, thickness schedule
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-02-00A-040A-D-EN-US.xml  # Upper Skin Inboard RH - Panel boundaries, thickness schedule
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-03-00A-040A-D-EN-US.xml  # Upper Skin Mid LH - Splice joints, inspection access
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-04-00A-040A-D-EN-US.xml  # Upper Skin Mid RH - Splice joints, inspection access
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-05-00A-040A-D-EN-US.xml  # Upper Skin Outboard LH - Anti-icing provisions, lightning protection
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-06-00A-040A-D-EN-US.xml  # Upper Skin Outboard RH - Anti-icing provisions, lightning protection
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-07-00A-040A-D-EN-US.xml  # Lower Skin Inboard LH - Fuel tank sealing, drain provisions
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-08-00A-040A-D-EN-US.xml  # Lower Skin Inboard RH - Fuel tank sealing, drain provisions
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-09-00A-040A-D-EN-US.xml  # Lower Skin Mid LH - Landing gear door interface
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-10-00A-040A-D-EN-US.xml  # Lower Skin Mid RH - Landing gear door interface
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-11-00A-040A-D-EN-US.xml  # Lower Skin Outboard LH - Outer wing panel, navigation light
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-12-00A-040A-D-EN-US.xml  # Lower Skin Outboard RH - Outer wing panel, navigation light
│   │   │   │   └── README.md
│   │   │   ├── 57-10-50_Stringers/
│   │   │   │   ├── DMC-BWQ1-A-57-10-50-00-00A-040A-D-EN-US.xml  # Stringers - General Description, Spanwise Arrangement
│   │   │   │   ├── DMC-BWQ1-A-57-10-50-01-00A-040A-D-EN-US.xml  # Upper Stringers LH - Compression members, section properties
│   │   │   │   ├── DMC-BWQ1-A-57-10-50-02-00A-040A-D-EN-US.xml  # Upper Stringers RH - Compression members, section properties
│   │   │   │   ├── DMC-BWQ1-A-57-10-50-03-00A-040A-D-EN-US.xml  # Lower Stringers LH - Tension members, splices
│   │   │   │   ├── DMC-BWQ1-A-57-10-50-04-00A-040A-D-EN-US.xml  # Lower Stringers RH - Tension members, splices
│   │   │   │   └── README.md
│   │   │   ├── 57-10-60_Attachments/
│   │   │   │   ├── DMC-BWQ1-A-57-10-60-00-00A-040A-D-EN-US.xml  # Attachments - General Description, Fitting Design Philosophy
│   │   │   │   ├── DMC-BWQ1-A-57-10-60-01-00A-040A-D-EN-US.xml  # Wing-to-Fuselage Fittings - Center section, main pins
│   │   │   │   ├── DMC-BWQ1-A-57-10-60-02-00A-040A-D-EN-US.xml  # Engine Mount Fittings - Thrust/vertical load transfer
│   │   │   │   ├── DMC-BWQ1-A-57-10-60-03-00A-040A-D-EN-US.xml  # Landing Gear Beam Fittings - Main gear attachment points
│   │   │   │   ├── DMC-BWQ1-A-57-10-60-04-00A-040A-D-EN-US.xml  # Control Surface Hinge Fittings - Moment transfer, bushing details
│   │   │   │   └── README.md
│   │   │   └── README.md
│   │   ├── procedural/
│   │   │   ├── inspection/
│   │   │   │   ├── 57-10-10_Forward_Spar/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-00-00A-520A-D-EN-US.xml  # Forward Spar Inspection - Visual, NDT methods, intervals
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-01-00A-520A-D-EN-US.xml  # Inboard Section LH Inspection - Critical zones, crack initiation sites
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-02-00A-520A-D-EN-US.xml  # Inboard Section RH Inspection - Critical zones, crack initiation sites
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-03-00A-520A-D-EN-US.xml  # Mid Section LH Inspection - Splice joint eddy current
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-04-00A-520A-D-EN-US.xml  # Mid Section RH Inspection - Splice joint eddy current
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-05-00A-520A-D-EN-US.xml  # Outboard Section LH Inspection - Tip attachment ultrasonic
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-06-00A-520A-D-EN-US.xml  # Outboard Section RH Inspection - Tip attachment ultrasonic
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-20_Rear_Spar/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-00-00A-520A-D-EN-US.xml  # Rear Spar Inspection - Visual, UT, thermography procedures
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-01-00A-520A-D-EN-US.xml  # Inboard Section LH Inspection - Gear beam bolt holes
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-02-00A-520A-D-EN-US.xml  # Inboard Section RH Inspection - Gear beam bolt holes
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-03-00A-520A-D-EN-US.xml  # Mid Section LH Inspection - Hinge fitting integrity
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-04-00A-520A-D-EN-US.xml  # Mid Section RH Inspection - Hinge fitting integrity
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-30_Ribs/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-30-00-00A-520A-D-EN-US.xml  # Ribs Inspection - Visual, tap test, access requirements
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-30-01-00A-520A-D-EN-US.xml  # Main Ribs Inspection - Corrosion check, fastener condition
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-30-02-00A-520A-D-EN-US.xml  # Intermediate Ribs Inspection - Web buckling, flange cracks
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-40_Skin_Panels/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-40-00-00A-520A-D-EN-US.xml  # Skin Panels Inspection - Surface condition, delamination check
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-40-01-00A-520A-D-EN-US.xml  # Upper Skin Inspection - Lightning strike damage, erosion
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-40-02-00A-520A-D-EN-US.xml  # Lower Skin Inspection - Impact damage, fuel leak evidence
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-50_Stringers/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-50-00-00A-520A-D-EN-US.xml  # Stringers Inspection - Debond detection, runout condition
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-60_Attachments/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-60-00-00A-520A-D-EN-US.xml  # Fittings Inspection - Visual, dye penetrant schedule
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-60-01-00A-520A-D-EN-US.xml  # Critical Fittings NDT - UT/MPI at life limits
│   │   │   │   │   └── README.md
│   │   │   │   └── README.md
│   │   │   ├── removal_installation/
│   │   │   │   ├── 57-10-10_Forward_Spar/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-00-00A-720A-D-EN-US.xml  # Forward Spar R/I - General precautions, tooling requirements
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-01-00A-720A-D-EN-US.xml  # Inboard Section LH R/I - Fuel drain, fastener sequence
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-02-00A-720A-D-EN-US.xml  # Inboard Section RH R/I - Fuel drain, fastener sequence
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-20_Rear_Spar/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-00-00A-720A-D-EN-US.xml  # Rear Spar R/I - Hinge removal, gear beam support
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-01-00A-720A-D-EN-US.xml  # Inboard Section LH R/I - Heavy lift procedure
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-40_Skin_Panels/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-40-00-00A-720A-D-EN-US.xml  # Skin Panel R/I - Sealing, torque values, inspection access
│   │   │   │   │   └── README.md
│   │   │   │   └── README.md
│   │   │   ├── repair/
│   │   │   │   ├── 57-10-10_Forward_Spar/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-10-00-00A-520A-D-EN-US.xml  # Forward Spar Repair - Allowable damage limits, doubler design
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-20_Rear_Spar/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-20-00-00A-520A-D-EN-US.xml  # Rear Spar Repair - Composite patch procedures
│   │   │   │   │   └── README.md
│   │   │   │   ├── 57-10-40_Skin_Panels/
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-40-00-00A-520A-D-EN-US.xml  # Skin Panel Repair - Damage categories, repair schemes
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-40-01-00A-520A-D-EN-US.xml  # Doubler Installation - Bonded, bolted, hybrid
│   │   │   │   │   ├── DMC-BWQ1-A-57-10-40-02-00A-520A-D-EN-US.xml  # Panel Replacement - Full panel change, sealing
│   │   │   │   │   └── README.md
│   │   │   │   └── README.md
│   │   │   └── README.md
│   │   ├── ipd/
│   │   │   ├── 57-10-10_Forward_Spar/
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-00-00A-941A-D-EN-US.xml  # Forward Spar IPD - Parts catalog, applicability
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-01-00A-941A-D-EN-US.xml  # Inboard Sections IPD - Part numbers, quantities
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-02-00A-941A-D-EN-US.xml  # Mid Sections IPD - Splice kit components
│   │   │   │   ├── DMC-BWQ1-A-57-10-10-03-00A-941A-D-EN-US.xml  # Outboard Sections IPD - Tip attachments
│   │   │   │   └── README.md
│   │   │   ├── 57-10-20_Rear_Spar/
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-00-00A-941A-D-EN-US.xml  # Rear Spar IPD - Parts catalog, hinge kits
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-01-00A-941A-D-EN-US.xml  # Inboard Sections IPD - Gear beam hardware
│   │   │   │   ├── DMC-BWQ1-A-57-10-20-02-00A-941A-D-EN-US.xml  # Mid Sections IPD - Control surface brackets
│   │   │   │   └── README.md
│   │   │   ├── 57-10-30_Ribs/
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-00-00A-941A-D-EN-US.xml  # Ribs IPD General - Part numbers by station
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-01-00A-941A-D-EN-US.xml  # Main Ribs IPD - Heavy rib assemblies
│   │   │   │   ├── DMC-BWQ1-A-57-10-30-02-00A-941A-D-EN-US.xml  # Intermediate Ribs IPD - Standard rib kit
│   │   │   │   └── README.md
│   │   │   ├── 57-10-40_Skin_Panels/
│   │   │   │   ├── DMC-BWQ1-A-57-10-40-00-00A-941A-D-EN-US.xml  # Skin Panels IPD - Panel P/Ns, fastener kits
│   │   │   │   └── README.md
│   │   │   ├── 57-10-50_Stringers/
│   │   │   │   ├── DMC-BWQ1-A-57-10-50-00-00A-941A-D-EN-US.xml  # Stringers IPD - Stringer assemblies by zone
│   │   │   │   └── README.md
│   │   │   ├── 57-10-60_Attachments/
│   │   │   │   ├── DMC-BWQ1-A-57-10-60-00-00A-941A-D-EN-US.xml  # Fittings IPD - Critical fitting P/Ns, hardware
│   │   │   │   └── README.md
│   │   │   └── README.md
│   │   └── README.md
│   └── README.md
├── compliance/
│   ├── allowables/
│   │   ├── README.md
│   │   └── index.md                            # Material allowables database index
│   ├── loads/
│   │   ├── README.md
│   │   └── index.md                            # Design load cases, limit/ultimate loads
│   ├── stress/
│   │   ├── README.md
│   │   └── index.md                            # Stress analysis reports, margin of safety
│   └── README.md
├── contracts/
│   ├── schemas/
│   │   ├── README.md
│   │   ├── acceptance.metric.schema.json       # Acceptance criteria data structure
│   │   ├── attachment.fitting.schema.json      # Fitting interface definition
│   │   ├── fastener.set.schema.json            # Fastener specification format
│   │   ├── joint.schema.json                   # Joint design parameters
│   │   └── laminate.stack.schema.json          # Composite layup definition
│   ├── ICD-AAA-ATA-57-10.md                    # Master ICD for wing primary structure
│   └── README.md
├── evidence/
│   ├── coupons/
│   │   ├── README.md
│   │   └── index.md                            # Coupon test results, material qualification
│   ├── ndt/
│   │   ├── README.md
│   │   └── index.md                            # NDT reports, calibration records
│   ├── tests/
│   │   ├── README.md
│   │   └── index.md                            # Component tests, full-scale testing
│   └── README.md
├── icd/
│   ├── ICD-57-10-53_Fuselage_Attachments.md    # Interface to ATA-53 fuselage structure
│   ├── ICD-57-10-57-20_Control_Surfaces.md     # Interface to ATA-57-20 control surfaces
│   ├── ICD-57-10-57-50_Systems_Provisions.md   # Interface to ATA-57-50 systems installations
│   └── README.md
├── io/
│   ├── README.md
│   └── routing.manifest.yaml                   # Data flow routing configuration
└── README.md

```

---

## S1000D Data Modules (DMRL-driven)

- **Information codes:**  
  - **040A** Descriptive; **520A** Inspection/Repair Procedures; **720A** Removal/Installation; **941A** IPD.  
- **Master list:** controlled in `S1000D/DMRL/DMRL.xml`. Each DMC above is *seeded* by the DMRL and must validate against **BREX**.

> **Estimated total:** ~85–90 DMs across descriptive, inspection, R/I, and IPD, per breakdown above.

---

## Interfaces & Dependencies

- **ATA-57-20 Control Surfaces:** hinge & bracket locations, stiffness/clearances (see `icd/ICD-57-10-57-20_Control_Surfaces.md`).  
- **ATA-53 Fuselage:** center section & wing-to-body attachments (`ICD-57-10-53_Fuselage_Attachments.md`).  
- **ATA-57-50 Systems Provisions:** actuator cutouts, cable/pipe penetrations (`ICD-57-10-57-50_Systems_Provisions.md`).  
- **ATA-20 Standard Practices:** fastening, bonding, sealing, OOC, EMI (forms linked below).

---

## Mandatory Forms (ATA-20)

Use canonical forms—**do not duplicate** inside ATA-57. Link from DMs and acceptance records:

- Composite Fastening — `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md`  
- Adhesive Bonding — `../../20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md`  
- Cabin Integrity / Leak Test — `../../20/20-20_Sealing_and_Pressurization/forms/FORM-QA-20-20-01_Cabin_Integrity_Leak_Test.md`  
- Material Handling & OOC Log — `../../20/20-30_Material_Handling/forms/FORM-QA-20-30-01_Material_Handling_OOC_Log.md`  
- Bonding / EMI Continuity — `../../20/20-40_Electrical_Bonding/forms/FORM-QA-20-40-01_Bonding_EMI_Continuity.md`

---

## 360IPCirq (R/I → IPC Reusability Bridge)

- **Intent:** every **720A** R/I DM enumerates removal kits, torque sequences, sealants, and fittings **with the same item keys** used by **941A IPD** figures/items to enable **“removal for repair → IPC 360 reusability”**.  
- **Where:** See `S1000D/data_modules/removal_installation/**` and corresponding `ipd/**`.  
- **Contracts:** The mapping keys and effectivity rules are defined in `contracts/ICD-AAA-ATA-57-10.md` and the JSON schemas under `contracts/schemas/`.

---

## Evidence & QS

- **Traceability:** material lots, OOC timers, torque values, sealant batches, NDT results, test coupons → indexed under `evidence/**` and cross-referenced from DMs.  
- **QS seal:** applied only when *all* applicable ATA-20 practices and acceptance metrics (per `contracts/schemas/acceptance.metric.schema.json`) are fully evidenced and referenced.

---

## Validation & CI

- **S1000D validation:** BREX rules (`S1000D/BREX/BREX.xml`) applied on each DM; DMRL conformance required.  
- **Schema validation:** JSON instances referenced by DMs must pass:
  - `contracts/schemas/laminate.stack.schema.json`
  - `contracts/schemas/joint.schema.json`
  - `contracts/schemas/fastener.set.schema.json`
  - `contracts/schemas/attachment.fitting.schema.json`
  - `contracts/schemas/acceptance.metric.schema.json`
- **Routing manifest:** `io/routing.manifest.yaml` records CAx/QOx/PAX inputs/outputs and UTCS/QS anchors. CI fails closed if any reference is missing or unverifiable.

---

## Change Control

Any deviation from ATA-20 or drawing/spec requires **M&P** and **MRB** approval and is recorded here. Releases follow **PDM-PLM** change notices; manifests and signatures are updated under `io/` and `evidence/`.

---

*Part of the BWB-Q100 technical baseline. Subject to configuration control.*
```

