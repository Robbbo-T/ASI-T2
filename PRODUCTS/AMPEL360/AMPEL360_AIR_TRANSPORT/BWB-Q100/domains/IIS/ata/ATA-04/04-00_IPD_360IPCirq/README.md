---
id: "IIS-ATA-04-360IPCirq-README"
project: "PRODUCTS/AMPEL360/BWB-Q100"
artifact: "360IPCirq — Illustrated Parts Catalog with Interchangeability/Replaceability & Reusability"
llc: "SYSTEMS"
title: "360IPCirq Configuration Breakdown — IPC + IRQ + Circular Reuse"
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

# 360IPCirq — Configuration Breakdown (CBS → CI → CO)

**360IPCirq** — *Illustrated Parts Catalog (IPC) + Interchangeability/Replaceability qualifier & Reusability for removal-for-repair scenarios ("360" circularity)*.

---

## Purpose

Unify IPD/IPC content, removal/installation (R/I) tasks, interchangeability/replaceability rules, and circular-reuse controls with UTCS/QS evidence. This system integrates:

- **IPD Catalog** (S1000D standard) for exploded views, part callouts, and assemblies
- **Removal/Installation Tasks** with procedural steps, tooling, and parameters
- **Repair & Reuse Routes** for circular economy and lifecycle management
- **Effectivity & Options** for aircraft configuration control
- **Interchangeability/Replaceability (IRQ)** rules and constraints
- **Serialization & Unit State** tracking throughout lifecycle
- **Evidence & QA Forms** linked to ATA-20 standards
- **Data Interfaces & Schemas** for system integration
- **Governance, QS & Attestations** for quality assurance

---

## Table of Contents

1. [Capability System (L0)](#l0--capability-system)
2. [Major Configuration Groups (L1)](#l1--major-configuration-groups)
3. [Subsystems & Containers (L2)](#l2--subsystems--containers)
4. [Leaf Configurable Objects (L3)](#l3--leaf-configurable-objects-co)
5. [Directory Structure](#directory-structure)
6. [Removal-for-Repair Flow](#removal-for-repair-flow)
7. [JSON Schemas](#json-schemas)
8. [ATA-20 Form Links](#ata-20-form-links)
9. [Routing & Interfaces](#routing--interfaces)
10. [Governance & QS](#governance--qs)

---

## L0 — Capability (System)

**CI-0.0**: `360IPCirq` — IPC + IRQ + Reusability for removal/repair & reinstall

**Purpose**: Unify IPD/IPC content, removal/installation (R/I) tasks, interchangeability/replaceability rules, and circular-reuse controls with UTCS/QS evidence.

---

## L1 — Major Configuration Groups

| CI ID | Group Name | Description |
|-------|------------|-------------|
| **CI-1.1** | IPD Catalog (S1000D/IPD) | Illustrated parts data, figures, items, callouts |
| **CI-1.2** | Removal/Installation Tasks (R/I) | Task modules for removal and installation procedures |
| **CI-1.3** | Repair & Reuse Routes | Shop visit routes, repair operations, reuse logic |
| **CI-1.4** | Effectivity & Options | Aircraft effectivity, variant packages, configuration gates |
| **CI-1.5** | Interchangeability / Replaceability (IRQ) | Part interchange classes, mapping tuples, alternates |
| **CI-1.6** | Serialization & Unit State | Serialized unit registry, lifecycle states, provenance |
| **CI-1.7** | Evidence & QA Forms (ATA-20) | Mandatory forms, test traces, compliance logs |
| **CI-1.8** | Data Interfaces & Schemas | PDM/PLM adapters, API endpoints, JSON schemas |
| **CI-1.9** | Governance, QS & Attestations | Workflows, UTCS/QS anchors, roles & permissions |

---

## L2 — Subsystems & Containers

### CI-1.1 IPD Catalog (S1000D/IPD)

- **CI-2.1**: Figures (exploded views)
- **CI-2.2**: Items (callouts)
- **CI-2.3**: Alternate/Supersedure lists
- **CI-2.4**: Kits & Assemblies references
- **CI-2.5**: Tools/Consumables cross-refs

### CI-1.2 Removal/Installation Tasks (R/I)

- **CI-2.6**: Task modules (Removal)
- **CI-2.7**: Task modules (Installation)
- **CI-2.8**: Safety, cautions, PPE blocks
- **CI-2.9**: Tooling/Material lines (per task)
- **CI-2.10**: Torque/cure/seal parameters

### CI-1.3 Repair & Reuse Routes

- **CI-2.11**: Shop visit routes (L1/L2/L3)
- **CI-2.12**: Operation codes (inspect/repair/overhaul)
- **CI-2.13**: Acceptance limits (post-repair)
- **CI-2.14**: Reuse decision logic (R-score)

### CI-1.4 Effectivity & Options

- **CI-2.15**: Aircraft effectivity sets (MSN, block)
- **CI-2.16**: Option/variant packages
- **CI-2.17**: Conditional expressions (software/config gates)

### CI-1.5 Interchangeability / Replaceability (IRQ)

- **CI-2.18**: Interchangeability classes (Full/Backward/Forward/None)
- **CI-2.19**: PN↔PN mapping tuples with reason codes
- **CI-2.20**: Qualified alternates with constraints (weight, software, maintenance level)

### CI-1.6 Serialization & Unit State

- **CI-2.21**: Serialized unit registry (by PN/SN)
- **CI-2.22**: Lifecycle states (New/Removed/Under-Repair/Serviceable/Suspect/Scrap)
- **CI-2.23**: Provenance chain (owner, shop, time at status)

### CI-1.7 Evidence & QA Forms (ATA-20)

- **CI-2.24**: Mandatory forms linkset (20-10/20-20/20-30/20-40)
- **CI-2.25**: Test traces (pressure/bond/continuity)
- **CI-2.26**: OOC, torque, cure logs

### CI-1.8 Data Interfaces & Schemas

- **CI-2.27**: PDM/PLM link adapters
- **CI-2.28**: IETP/IPD export (viewer packages)
- **CI-2.29**: API endpoints (read/resolve/commit)
- **CI-2.30**: JSON Schemas (manifest/evidence/effectivity/IRQ)

### CI-1.9 Governance, QS & Attestations

- **CI-2.31**: Workflows (deviation/MRB, approvals)
- **CI-2.32**: UTCS/QS anchors & signatures
- **CI-2.33**: Roles & permissions

---

## L3 — Leaf Configurable Objects (CO)

These are the **last configuration & configurable objects** (atomic/leaf). Each row shows **Object → Key configuration fields**.

| CO ID | Object Name | Key Configuration Fields |
|-------|-------------|--------------------------|
| **CO-3.1** | IPD Figure | `fig_id`, `chapter/section`, `ICN refs[]`, `effectivity_expr` |
| **CO-3.2** | IPD Item/Callout | `item_no`, `PN`, `Nomenclature`, `QTY`, `UOM`, `IPC_note`, `effectivity_expr` |
| **CO-3.3** | Alternate PN Map | `from_PN`, `to_PN`, `class{full/back/forw/none}`, `reason_code`, `limits` |
| **CO-3.4** | Supersession Chain Node | `PN`, `supersedes[]`, `superseded_by`, `effective_date` |
| **CO-3.5** | Kit Line | `kit_id`, `child_PN`, `qty`, `mandatory{Y/N}`, `notes` |
| **CO-3.6** | Task Step (Removal) | `step_id`, `preconditions`, `action_text`, `hazards[]`, `refs(IPD item/tool)` |
| **CO-3.7** | Task Step (Installation) | `step_id`, `sealant/adhesive_ref`, `torque_ref`, `bond_test_ref`, `acceptance` |
| **CO-3.8** | Tool Reference | `tool_code`, `description`, `alt_tool[]`, `calibration_due` |
| **CO-3.9** | Material Line | `mat_code`, `spec`, `batch_required{Y/N}`, `shelf_life`, `storage_class` |
| **CO-3.10** | Torque Parameter | `fastener_code`, `torque_Nm`, `angle_deg?`, `lubrication_cond`, `witness_req{Y/N}` |
| **CO-3.11** | Cure Parameter | `adhesive_code`, `temp_profile`, `time_profile`, `pressure_profile`, `coupon_req{Y/N}` |
| **CO-3.12** | Seal Parameter | `sealant_code`, `bead_size`, `surface_prep_method`, `WBT_req{Y/N}` |
| **CO-3.13** | Repair Operation | `op_code`, `level(L1/L2/L3)`, `inputs[]`, `outputs[]`, `acceptance_limit_ref` |
| **CO-3.14** | Acceptance Limit | `metric`, `threshold`, `method`, `evidence_ref` |
| **CO-3.15** | Reuse Decision Rule | `rule_id`, `R_score_formula`, `min_score_for_reuse`, `overrides[]` |
| **CO-3.16** | Effectivity Rule | `expr`(MSN ranges, options), `start`, `end`, `exclude[]` |
| **CO-3.17** | Option/Variant Flag | `option_code`, `name`, `dependencies[]`, `exclusions[]` |
| **CO-3.18** | IRQ Tuple | `pair_id`, `from_PN`, `to_PN`, `class`, `constraints`, `note` |
| **CO-3.19** | Qualified Alternate Constraint | `constraint_id`, `type`(performance/weight/software), `limit`, `verification_method` |
| **CO-3.20** | Serialized Unit Record | `PN`, `SN`, `CAGE`, `date_code`, `state`, `location` |
| **CO-3.21** | Unit State Transition | `from_state`, `to_state`, `trigger`, `evidence_req`, `approver_role` |
| **CO-3.22** | Provenance Edge | `SN`, `event`, `timestamp`, `actor`, `hash_anchor` |
| **CO-3.23** | Evidence File Ref | `type`, `uri`, `sha256`, `form_link` |
| **CO-3.24** | QA Form Link | `form_id`, `rev`, `path`, `required_in_steps[]` |
| **CO-3.25** | API Endpoint Config | `endpoint`, `verb`, `schema_ref`, `auth_scope`, `rate_limit` |
| **CO-3.26** | Schema Version Pin | `schema_name`, `version`, `uri`, `checksum` |
| **CO-3.27** | Role Permission | `role`, `action`, `scope`, `constraints` |
| **CO-3.28** | Approval Step | `workflow_id`, `step_no`, `role`, `SLA`, `escalation` |
| **CO-3.29** | QS/UTCS Anchor | `canonical_hash`, `sbom_uri`, `signer`, `timestamp` |
| **CO-3.30** | IETP Package Ref | `pub_id`, `format`, `locale`, `effectivity_expr`, `download_uri` |

---

## Directory Structure

```
PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-04/
├── README.md (this file — ATA-04 index)
├── 04-00_IPD_360IPCirq/
│   ├── README.md (360IPCirq configuration breakdown)
│   ├── S1000D/               # IPD figures/items per S1000D; 4-digit pattern respected
│   │   ├── figures/          # CO-3.1: IPD figures
│   │   ├── items/            # CO-3.2: IPD items/callouts
│   │   ├── alternates/       # CO-3.3: Alternate PN maps
│   │   ├── supersessions/    # CO-3.4: Supersession chains
│   │   └── kits/             # CO-3.5: Kit lines
│   ├── irq/                  # Interchangeability rules & tuples
│   │   ├── tuples/           # CO-3.18: IRQ tuples
│   │   ├── constraints/      # CO-3.19: Qualified alternate constraints
│   │   └── classes/          # CI-2.18: Interchangeability class definitions
│   ├── effectivity/          # Effectivity and option management
│   │   ├── rules/            # CO-3.16: Effectivity rules
│   │   └── options/          # CO-3.17: Option/variant flags
│   ├── ri_tasks/             # Removal/Installation tasks
│   │   ├── removal/          # CO-3.6: Removal task steps
│   │   ├── installation/     # CO-3.7: Installation task steps
│   │   ├── safety/           # CI-2.8: Safety, cautions, PPE blocks
│   │   ├── tooling/          # CO-3.8: Tool references
│   │   ├── materials/        # CO-3.9: Material lines
│   │   ├── torque/           # CO-3.10: Torque parameters
│   │   ├── cure/             # CO-3.11: Cure parameters
│   │   └── seal/             # CO-3.12: Seal parameters
│   ├── repair_reuse/         # Repair routes and reuse logic
│   │   ├── operations/       # CO-3.13: Repair operations
│   │   ├── limits/           # CO-3.14: Acceptance limits
│   │   └── rules/            # CO-3.15: Reuse decision rules
│   ├── evidence/             # Links to ATA-20 forms; no duplication
│   │   ├── file_refs/        # CO-3.23: Evidence file references
│   │   ├── qa_forms/         # CO-3.24: QA form links
│   │   └── logs/             # CI-2.26: OOC, torque, cure logs
│   ├── interfaces/           # API, schemas, integrations
│   │   ├── api/              # CO-3.25: API endpoint configs
│   │   ├── pdm_plm/          # CI-2.27: PDM/PLM adapters
│   │   └── ietp/             # CO-3.30: IETP package references
│   ├── contracts/            # ICD + JSON schemas
│   │   ├── governance/       # CI-2.31, CO-3.27, CO-3.28: Workflows, roles
│   │   └── qis/              # CO-3.29: QS/UTCS anchors
│   ├── schemas/              # JSON schemas for validation
│   │   ├── ipd.item.schema.json          # Validates CO-3.2
│   │   ├── irq.tuple.schema.json         # Validates CO-3.18
│   │   ├── effectivity.rule.schema.json  # Validates CO-3.16
│   │   ├── evidence.file.schema.json     # Validates CO-3.23
│   │   └── schema.manifest.yaml          # CO-3.26: Schema version pins
│   └── io/
│       └── routing.manifest.yaml         # Routing and interface definitions
```

---

## Removal-for-Repair Flow

This flow demonstrates how the leaf objects (CO) connect to enable the removal-for-repair lifecycle:

### Step-by-Step Process

1. **Identify Part** via IPD figure/item (**CO-3.1**/**CO-3.2**) under current **effectivity** (**CO-3.16**/**CO-3.17**)
   
2. **Check IRQ Tuples** (**CO-3.18**/**CO-3.19**) for acceptable alternates if replacement is needed

3. **Execute Removal Task Steps** (**CO-3.6**) with:
   - **Tools/Materials** (**CO-3.8**/**CO-3.9**)
   - **Parameters** (**CO-3.10**–**CO-3.12**) for torque, cure, seal

4. **Log Evidence** (**CO-3.23**) using the **ATA-20 Forms** (**CO-3.24**):
   - Composite Fastening (FORM-QA-20-10-01)
   - Adhesive Bonding (FORM-QA-20-10-02)
   - Cabin Integrity/Leak Test (FORM-QA-20-20-01)
   - Material Handling & OOC Log (FORM-QA-20-30-01)
   - Bonding/EMI Continuity (FORM-QA-20-40-01)

5. **Route to Repair/Reuse** (**CO-3.13**–**CO-3.15**):
   - Shop visit routes (L1/L2/L3)
   - Operation codes (inspect/repair/overhaul)
   - Update **serialized unit** & **state** (**CO-3.20**/**CO-3.21**/**CO-3.22**)

6. **For Re-install**:
   - Validate **acceptance limits** (**CO-3.14**)
   - Apply **Installation steps** (**CO-3.7**)
   - Seal with **QS/UTCS** (**CO-3.29**)

### Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                     360IPCirq Removal-for-Repair Flow                 │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  1. Identify Part             │
                    │  CO-3.1/3.2 + CO-3.16/3.17    │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  2. Check IRQ for Alternates  │
                    │  CO-3.18/3.19                 │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  3. Execute Removal Tasks     │
                    │  CO-3.6 + CO-3.8/3.9/3.10-12  │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  4. Log Evidence              │
                    │  CO-3.23 + CO-3.24 (ATA-20)   │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  5. Route to Repair/Reuse     │
                    │  CO-3.13/3.14/3.15            │
                    │  Update Unit State            │
                    │  CO-3.20/3.21/3.22            │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  6. Re-install                │
                    │  CO-3.7 + CO-3.14 + CO-3.29   │
                    └───────────────────────────────┘
```

---

## JSON Schemas

Minimal JSON schemas validate each leaf configurable object (CO). These schemas are version-pinned (**CO-3.26**) and sealed (**CO-3.29**) in the `artifact.manifest.yaml`.

### Schema Files

Located in `./schemas/`:

- **`ipd.item.schema.json`** → validates **CO-3.2** (IPD Item/Callout)
- **`irq.tuple.schema.json`** → validates **CO-3.18** (IRQ Tuple)
- **`effectivity.rule.schema.json`** → validates **CO-3.16** (Effectivity Rule)
- **`evidence.file.schema.json`** → validates **CO-3.23** (Evidence File Reference)
- **`schema.manifest.yaml`** → version pins for all schemas (**CO-3.26**)

### Schema Validation

All data objects must pass JSON Schema validation before being accepted into the system. The validation process is enforced at:

- **Data Entry**: Before any new object is created
- **Integration**: When objects are imported from external systems
- **CI/CD**: Automated validation in the build pipeline

---

## ATA-20 Form Links

**Canonical ATA-20 form references** — no duplication, links only:

### Form Locations

All ATA-20 forms reside in the **AAA domain** under standard practices. The 360IPCirq system references these forms but does not duplicate them:

| Form ID | Form Name | Canonical Path |
|---------|-----------|----------------|
| **FORM-QA-20-10-01** | Composite Fastening | `../../../../AAA/ata/ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-01_Composite_Fastening.md` |
| **FORM-QA-20-10-02** | Adhesive Bonding | `../../../../AAA/ata/ATA-20/20-10_Structural_Practices/forms/FORM-QA-20-10-02_Adhesive_Bonding.md` |
| **FORM-QA-20-20-01** | Cabin Integrity / Leak Test | `../../../../AAA/ata/ATA-20/20-20_Sealing_and_Pressurization/forms/FORM-QA-20-20-01_Cabin_Integrity_Leak_Test.md` |
| **FORM-QA-20-30-01** | Material Handling & OOC Log | `../../../../AAA/ata/ATA-20/20-30_Material_Handling/forms/FORM-QA-20-30-01_Material_Handling_OOC_Log.md` |
| **FORM-QA-20-40-01** | Bonding / EMI Continuity | `../../../../AAA/ata/ATA-20/20-40_Electrical_Bonding/forms/FORM-QA-20-40-01_Bonding_EMI_Continuity.md` |

### Evidence Collection

Evidence collected during removal/installation tasks must:

1. Reference the appropriate ATA-20 form(s)
2. Be stored with proper provenance tracking (**CO-3.22**)
3. Be sealed with QS/UTCS anchor (**CO-3.29**)
4. Include SHA-256 checksums for integrity verification

---

## Routing & Interfaces

### Upstream (Inputs)

| Source | Transport | Path/Endpoint | Format | Cadence | Owner |
|--------|-----------|---------------|--------|---------|-------|
| PDM/PLM | Artifact sync | `/pdm/ipc/parts/` | S1000D XML | On-update | PDM Team |
| Engineering | API | `/api/engineering/bom/` | JSON v2.0 | Daily | Eng Team |
| Maintenance | Database sync | `/maint/shop/units/` | DB Records | Real-time | Maint Ops |

### Downstream (Outputs)

| Consumer | Transport | Path/Endpoint | Format | Contract | Owner |
|----------|-----------|---------------|--------|----------|-------|
| IETP Viewers | Export | `/ietp/packages/` | S1000D+SGML | ICD-IETP-001 | Pub Team |
| Maintenance Systems | API | `/api/ipc/query/` | JSON v2.0 | ICD-MAINT-001 | IT Team |
| Repair Shops | Web Portal | `/portal/repair/tasks/` | HTML5 | ICD-REPAIR-001 | MRO Team |

### Cadence & Environments

- **Dev**: `file:///dev/ata/04/` (ad hoc on PR)
- **Stage**: `file:///stage/ata/04/` (nightly 02:00 UTC)
- **Prod**: `/pdm/ata/04/` (post-baseline release)

### Controls & Reliability

- **Classification**: INTERNAL–EVIDENCE-REQUIRED
- **Access**: PDM role: `IIS.contributors` (read), `ASI-T.arch` (write)
- **SLO**: Publish ≤ 30 min after upstream seal; **Retries**: 3× exponential
- **Alerts**: #iis-ata04 on failure; **Escalation**: on-call @maintainer within 15 min
- **Change route**: via CN; MRB approval required

---

## Governance & QS

### Workflows (CO-3.28)

All changes to 360IPCirq configuration follow structured approval workflows:

1. **Proposal**: Engineer/Designer creates change request
2. **Review**: Technical review by domain experts
3. **MRB**: Material Review Board for non-standard changes
4. **Approval**: Final approval by authorized roles
5. **Implementation**: Controlled deployment with QS seal
6. **Verification**: Post-deployment validation

### Roles & Permissions (CO-3.27)

| Role | View | Edit | Approve | Override |
|------|------|------|---------|----------|
| Engineer | ✓ | ✓ | - | - |
| Lead Engineer | ✓ | ✓ | ✓ | - |
| Quality Assurance | ✓ | - | ✓ | - |
| System Admin | ✓ | ✓ | ✓ | ✓ |
| MRB Member | ✓ | - | ✓ | ✓ |

### QS/UTCS Anchors (CO-3.29)

Every configuration artifact is sealed with:

- **Canonical hash**: SHA-256 of normalized content
- **SBOM URI**: Software/Data Bill of Materials reference
- **Signer**: Authorized signer identity
- **Timestamp**: UTC timestamp of sealing event

### Compliance

- Conform to **S1000D** for IPD content structure
- Follow **ATA-20** practices for all physical work
- Maintain **UTCS/QS** evidence chains
- Support **MAL-EEM** ethics guard requirements

---

## Cross-References

### Internal (IIS Domain)

- **[ATA-22 — Autoflight](../ATA-22/)**: Software integration for automated part tracking
- **[ATA-42 — IMA](../ATA-42/)**: Avionics integration for electronic cataloging
- **[ATA-45 — CMS](../ATA-45/)**: Central maintenance system integration
- **[ATA-46 — Information Systems](../ATA-46/)**: Data management and distribution

### External (Other Domains)

- **[AAA — ATA-20](../../../AAA/ata/ATA-20/)**: Standard practices (canonical forms)
- **[AAA — ATA-51/53/55/57](../../../AAA/ata/)**: Structural chapters (part users)
- **[PDM/PLM](../../../README.md)**: Configuration management system
- **[QOx](../../qox/)**: Optimization integration for part selection

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-01 | ASI-T Architecture Team | Initial configuration breakdown |

---

*Part of the BWB-Q100 technical baseline. Subject to configuration control under UTCS/QS v5.0.*
