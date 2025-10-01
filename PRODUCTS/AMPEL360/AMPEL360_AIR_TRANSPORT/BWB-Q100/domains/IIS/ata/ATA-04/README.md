---
id: "IIS-ATA-04-README"
project: "PRODUCTS/AMPEL360/BWB-Q100"
artifact: "ATA-04 — Illustrated Parts Data"
llc: "SYSTEMS"
title: "ATA-04 — Illustrated Parts Data (BWB-Q100)"
configuration: "baseline"
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "1.0.0"
release_date: "2025-10-01"
maintainer: "ASI-T Architecture Team"
licenses:
  docs: "CC-BY-4.0"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: "MAL-EEM"
utcs_mi: "v5.0"
canonical_hash: "TBD"
provenance:
  policy_hash: "sha256:TBD"
  model_sha: "sha256:TBD"
  data_manifest_hash: "sha256:TBD"
  operator_id: "UTCS:OP:copilot-gen"
---

# ATA-04 — Illustrated Parts Data (BWB-Q100)

This chapter contains illustrated parts catalogs (IPC/IPD), interchangeability/replaceability qualifiers (IRQ), and circular reuse controls for the BWB-Q100 aircraft.

---

## Scope & Purpose

**ATA-04** provides:

- **Illustrated Parts Data (IPD)** following S1000D standards
- **Interchangeability/Replaceability Qualifiers (IRQ)** for part substitution
- **Circular Economy Integration** for removal-for-repair scenarios
- **Evidence Linkage** to ATA-20 standard practices
- **Effectivity Management** for aircraft configuration control
- **Serialization & Lifecycle Tracking** for repairable units

This chapter serves as the authoritative source for:

1. Part identification and nomenclature
2. Exploded views and assembly relationships
3. Part interchange rules and constraints
4. Removal and installation procedures
5. Repair routing and reuse decision logic
6. Evidence collection and quality assurance

---

## Index of Systems

### 04-00 — 360IPCirq (Primary System)

**[360IPCirq — IPC + IRQ + Circular Reuse](./04-00_IPD_360IPCirq/)**

The 360IPCirq system integrates:

- **IPD Catalog** (S1000D standard) for exploded views and part callouts
- **Removal/Installation Tasks** with procedural steps, tooling, and parameters
- **Repair & Reuse Routes** for circular economy lifecycle management
- **Effectivity & Options** for aircraft configuration control
- **Interchangeability/Replaceability (IRQ)** rules and constraints
- **Serialization & Unit State** tracking throughout lifecycle
- **Evidence & QA Forms** linked to ATA-20 standards (canonical references)
- **Data Interfaces & Schemas** for system integration
- **Governance, QS & Attestations** for quality assurance

**Key Features:**

- **360° Circularity**: Complete lifecycle tracking from installation through removal, repair, and reinstallation
- **S1000D Compliant**: Full compliance with S1000D Issue 5.0 data structure
- **ATA-20 Integration**: Direct linkage to standard practices and QA forms
- **UTCS/QS Sealed**: Full provenance and quality sealing
- **API-Enabled**: RESTful APIs for system integration

**Directory Structure:**

```
04-00_IPD_360IPCirq/
├── README.md                    # Configuration breakdown (CBS → CI → CO)
├── artifact.manifest.yaml       # Artifact version pinning and QS sealing
├── S1000D/                      # IPD figures/items per S1000D
├── irq/                         # Interchangeability rules & tuples
├── effectivity/                 # Effectivity and option management
├── ri_tasks/                    # Removal/Installation tasks
├── repair_reuse/                # Repair routes and reuse logic
├── evidence/                    # Evidence file references (links to ATA-20)
├── interfaces/                  # API, schemas, integrations
├── contracts/                   # ICD + governance
├── schemas/                     # JSON schemas for validation
└── io/                          # Routing and interface definitions
```

---

## Configuration Breakdown Summary

The 360IPCirq system is organized into **3 levels**:

### L0 — Capability (System)
- **CI-0.0**: 360IPCirq — IPC + IRQ + Reusability for removal/repair & reinstall

### L1 — Major Configuration Groups (9 groups)
- CI-1.1: IPD Catalog (S1000D/IPD)
- CI-1.2: Removal/Installation Tasks (R/I)
- CI-1.3: Repair & Reuse Routes
- CI-1.4: Effectivity & Options
- CI-1.5: Interchangeability / Replaceability (IRQ)
- CI-1.6: Serialization & Unit State
- CI-1.7: Evidence & QA Forms (ATA-20)
- CI-1.8: Data Interfaces & Schemas
- CI-1.9: Governance, QS & Attestations

### L2 — Subsystems & Containers (33 subsystems)
Detailed breakdown in the [360IPCirq README](./04-00_IPD_360IPCirq/README.md)

### L3 — Leaf Configurable Objects (30 objects)
Atomic configuration objects including:
- IPD Figure (CO-3.1)
- IPD Item/Callout (CO-3.2)
- Alternate PN Map (CO-3.3)
- IRQ Tuple (CO-3.18)
- Effectivity Rule (CO-3.16)
- Evidence File Ref (CO-3.23)
- QS/UTCS Anchor (CO-3.29)
- [Full list in 360IPCirq README](./04-00_IPD_360IPCirq/README.md#l3--leaf-configurable-objects-co)

---

## Routing & Interfaces

### Upstream (Inputs)

| Source | Transport | Cadence | Owner |
|--------|-----------|---------|-------|
| PDM/PLM | Artifact sync | On-update | PDM Team |
| Engineering BOM | REST API | Daily | Engineering |
| Maintenance Units | Database sync | Real-time | Maintenance Ops |

### Downstream (Outputs)

| Consumer | Transport | Format | Contract |
|----------|-----------|--------|----------|
| IETP Viewers | Export package | S1000D+SGML | ICD-IETP-001 |
| Maintenance Systems | REST API | JSON v2.0 | ICD-MAINT-001 |
| Repair Shops | Web portal | HTML5 | ICD-REPAIR-001 |

Full routing details: [io/routing.manifest.yaml](./04-00_IPD_360IPCirq/io/routing.manifest.yaml)

---

## ATA-20 Integration

All physical work performed during removal/installation tasks must follow **ATA-20 Standard Practices**. The 360IPCirq system references (but does not duplicate) ATA-20 forms:

| Form ID | Form Name | Canonical Path |
|---------|-----------|----------------|
| FORM-QA-20-10-01 | Composite Fastening | `../../AAA/ata/ATA-20/20-10_Structural_Practices/forms/` |
| FORM-QA-20-10-02 | Adhesive Bonding | `../../AAA/ata/ATA-20/20-10_Structural_Practices/forms/` |
| FORM-QA-20-20-01 | Cabin Integrity / Leak Test | `../../AAA/ata/ATA-20/20-20_Sealing_and_Pressurization/forms/` |
| FORM-QA-20-30-01 | Material Handling & OOC Log | `../../AAA/ata/ATA-20/20-30_Material_Handling/forms/` |
| FORM-QA-20-40-01 | Bonding / EMI Continuity | `../../AAA/ata/ATA-20/20-40_Electrical_Bonding/forms/` |

---

## JSON Schemas & Validation

All data objects must pass JSON Schema validation:

| Schema | Validates | Version |
|--------|-----------|---------|
| `ipd.item.schema.json` | CO-3.2: IPD Item/Callout | 1.0.0 |
| `irq.tuple.schema.json` | CO-3.18: IRQ Tuple | 1.0.0 |
| `effectivity.rule.schema.json` | CO-3.16: Effectivity Rule | 1.0.0 |
| `evidence.file.schema.json` | CO-3.23: Evidence File Ref | 1.0.0 |

Schema versions: [schemas/schema.manifest.yaml](./04-00_IPD_360IPCirq/schemas/schema.manifest.yaml)

---

## Removal-for-Repair Flow

The 360IPCirq system enables a complete removal-for-repair lifecycle:

```
1. Identify Part → IPD figure/item (CO-3.1/3.2) + effectivity (CO-3.16/3.17)
2. Check IRQ → Alternate parts (CO-3.18/3.19)
3. Execute Removal → Task steps (CO-3.6) + tools/materials (CO-3.8/3.9/3.10-12)
4. Log Evidence → Evidence files (CO-3.23) + ATA-20 forms (CO-3.24)
5. Route to Repair → Repair operations (CO-3.13/3.14/3.15) + unit state (CO-3.20/3.21/3.22)
6. Re-install → Installation steps (CO-3.7) + acceptance (CO-3.14) + QS seal (CO-3.29)
```

Full flow diagram: [360IPCirq README](./04-00_IPD_360IPCirq/README.md#removal-for-repair-flow)

---

## Governance & Quality Assurance

### Change Control

- **Process**: Change Notice (CN)
- **Approval**: MRB required for non-standard changes
- **Documentation**: Mandatory for all changes

### Roles & Permissions

| Role | View | Edit | Approve | Override |
|------|------|------|---------|----------|
| Engineer | ✓ | ✓ | - | - |
| Lead Engineer | ✓ | ✓ | ✓ | - |
| Quality Assurance | ✓ | - | ✓ | - |
| System Admin | ✓ | ✓ | ✓ | ✓ |
| MRB Member | ✓ | - | ✓ | ✓ |

### QS/UTCS Anchoring

Every configuration artifact is sealed with:
- Canonical hash (SHA-256)
- SBOM URI
- Authorized signer identity
- UTC timestamp

---

## Standards & References

### Primary Standards

- **S1000D Issue 5.0** — International specification for technical publications
- **ATA iSpec 2200** — Information standards for aviation maintenance
- **UTCS-MI v5.0** — Universal Traceability and Configuration Sealing
- **MAL-EEM** — Multi-agent Alignment with Ethical Evaluation Matrix

### Related ATA Chapters

- **[ATA-20](../../AAA/ata/ATA-20/)** — Standard Practices (AAA domain)
- **[ATA-22](../ATA-22/)** — Autoflight (IIS domain)
- **[ATA-42](../ATA-42/)** — Integrated Modular Avionics (IIS domain)
- **[ATA-45](../ATA-45/)** — Central Maintenance System (IIS domain)
- **[ATA-46](../ATA-46/)** — Information Systems (IIS domain)

### External Systems

- **PDM/PLM** — Product Data Management / Product Lifecycle Management
- **IETP** — Interactive Electronic Technical Publications
- **MRO** — Maintenance, Repair, and Overhaul systems

---

## Cross-References

### Within IIS Domain

- **[CAI](../../cax/CAI/)** — Computer-aided intelligence integration
- **[CASE](../../cax/CASE/)** — Computer-aided software engineering
- **[QOx](../../qox/)** — Quantum optimization integration

### Other Domains

- **[AAA Domain](../../../AAA/)** — Aerodynamics & Airframes (ATA-20 owner)
- **[CQH Domain](../../../CQH/)** — Crew, Quarters, Hydraulics
- **[LCC Domain](../../../LCC/)** — Logic, Communications, Control

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-01 | ASI-T Architecture Team | Initial ATA-04 chapter structure with 360IPCirq |

---

## Quick Links

- **[360IPCirq Configuration Breakdown](./04-00_IPD_360IPCirq/README.md)** — Complete system documentation
- **[Artifact Manifest](./04-00_IPD_360IPCirq/artifact.manifest.yaml)** — Version pinning and QS sealing
- **[Routing Manifest](./04-00_IPD_360IPCirq/io/routing.manifest.yaml)** — Data flows and interfaces
- **[Schema Manifest](./04-00_IPD_360IPCirq/schemas/schema.manifest.yaml)** — Schema version control
- **[JSON Schemas](./04-00_IPD_360IPCirq/schemas/)** — Validation schemas directory

---

*Part of the BWB-Q100 technical baseline. Subject to configuration control under UTCS/QS v5.0.*
