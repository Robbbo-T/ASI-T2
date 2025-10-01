
---
id: ASIT2-GAIA-AIR-IDROWALL-IIS-ATA42-0001
rev: 2
project: PRODUCTS/GAIA-AIR/IDRO_WALL
artifact: PRODUCTS/GAIA-AIR/IDRO_WALL/domains/IIS/ata/ATA-42/README.md
llc: SYSTEMS
title: "ATA-42 — Integrated Modular Avionics (IIS — Information & Intelligence Systems)"
classification: INTERNAL–EVIDENCE-REQUIRED
version: "0.2.0"
release_date: 2025-10-01
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "pending"
---
# ATA-42 — Integrated Modular Avionics (IIS)

IMA platform & software architecture for the **Information & Intelligence Systems (IIS)** domain in IDRO WALL. Defines **partitions**, **APEX interfaces**, **ARINC-653 schedule**, **safety/ethics boundaries** (MAL-EEM fail-closed), configuration artefacts, and evidence mapping to DO-178C/DO-297 and DO-326A/356A where applicable.

<!-- COPILOT:IMAGE
title: "ATA-42 IMA Overview (IIS)"
save_to: "assets/diagrams/ata42_ima_overview_v1.png"
prompt: "Technical system diagram for ATA-42 Integrated Modular Avionics in the IIS domain (IDRO_WALL). Show IMA chassis, partitions (SwarmCore, MAL-EEM Ethics Gate, MissionPlanner, CMSAdapter/Telemetry), APEX ports/queues, health manager, and bridges to LCC/EDI/OOO. Clean monochrome blueprint style, vector look, 16:9."
notes: "Use exact partition and interface names from the tables below."
-->

## Quick Nav
Scope & Responsibilities • Standard Directory Layout • Partitions & APEX Interfaces • Timing & Resources • Configuration Artefacts • Compliance Mapping • Evidence & QS • Change Control • Revision History

## Scope & Responsibilities
**In scope (IIS within ATA-42)**
- IMA software architecture for IIS services (Swarm coordination, Mission planning, MAL-EEM gate, Telemetry/CMS hooks).
- Partitioning, **APEX ports** (queues, sampling, blackboards, buffers), and health monitoring integration.
- ARINC-653 schedule and **time/space budgets**.  
- Security/ethics boundaries with **fail-closed** command gating (MAL-EEM).

**Out of scope (owned elsewhere)**
- Low-level I/O drivers, radios, buses → **LCC**  
- Sensor acquisition chains → **EDI**  
- Detailed CMS/PHM/CBM logic → **ATA-45**

## Standard Directory Layout
```

domains/IIS/ata/ATA-42/
├── README.md
├── governance/                 # approvals, risks, baselines
├── os/
│   ├── S1000D/                 # IETP/IETM data modules
│   ├── configuration/
│   │   ├── manifests/          # manifest.yaml (hashes, SBOM, sign-off)
│   │   ├── a653/               # partition.xml / schedule.xml
│   │   └── rtos/               # board/RTOS config
│   ├── testing/                # plans, procedures, coverage
│   └── compliance/             # DO-178C, DO-297, DO-326A/356A
├── manufacturing/              # fixtures, test benches (if applicable)
├── sustainment/                # service, diagnostics, obsolescence
├── assets/                     # diagrams, images
├── scripts/                    # validators, exporters
└── docs/                       # supplementary notes

```

<!-- COPILOT:IMAGE
title: "Repo Layout — ATA-42"
save_to: "assets/diagrams/ata42_repo_layout_v1.png"
prompt: "Folder map for ATA-42 showing governance, os/{S1000D,configuration{manifests,a653,rtos},testing,compliance}, manufacturing, sustainment, assets, scripts, docs. Monochrome, vector, 16:9."
-->

## Partitions & APEX Interfaces
**Partitions (proposed baseline)**  

Partition | DAL | Purpose | Key APEX Ports (dir/type) | Notes
--|--|--|--|--
`IIS.SwarmCore` | B | Swarm coordination & resilient consensus | `c2.swarm.v1` (SRC/queue), `sync.state.v1` (DST/sampling) | heals partitions, leader election
`IIS.MAL-EEM` | A | Ethics gate (pre-action assessment; **fail-closed**) | `eth.rules.v1` (DST/sampling), `eth.audit.v1` (SRC/queue) | dual-control updates; signed policy packs
`IIS.MissionPlanner` | B | Planning, tasking, replanning | `sens.bus.v1` (DST/sampling), `sens.task.v1` (SRC/queue) | ROI scheduling to EDI
`IIS.CMSAdapter` | C | Health/telemetry export to CMS | `cms.health.v1` (SRC/queue), `cms.export.v1` (SRC/queue) | feeds ATA-45

> APEX abbreviations: SRC=Source, DST=Destination; types are ARINC-653 **Sampling** or **Queueing** ports (others by exception).

<!-- COPILOT:IMAGE
title: "APEX Port Map — ATA-42 / IIS"
save_to: "assets/diagrams/ata42_apex_port_map_v1.png"
prompt: "Matrix-style diagram listing partitions vs APEX ports with direction (SRC/DST) and port type (Sampling/Queueing). Include c2.swarm.v1, sync.state.v1, sens.bus.v1, sens.task.v1, eth.rules.v1, eth.audit.v1, cms.health.v1, cms.export.v1. Monochrome, vector, 16:9."
notes: "Match port names exactly."
-->

## Timing & Resources (ARINC-653)
**Major frame:** 100 ms (example baseline); **Health manager** executes asynchronously in platform context.

Window | Partition | Start (ms) | Duration (ms)
--|--|--:|--:|
W1 | `IIS.MAL-EEM` | 0 | 20
W2 | `IIS.SwarmCore` | 20 | 40
W3 | `IIS.MissionPlanner` | 60 | 40

**Resource budgets (initial)**
- `IIS.SwarmCore`: CPU 5%, Mem 5120 KB  
- `IIS.MAL-EEM`: CPU 3%, Mem 4096 KB  
- `IIS.MissionPlanner`: CPU 4%, Mem 4096 KB  
- `IIS.CMSAdapter`: CPU 2%, Mem 2048 KB

<!-- COPILOT:IMAGE
title: "A653 Schedule — ATA-42"
save_to: "assets/diagrams/ata42_a653_schedule_v1.png"
prompt: "Timeline (0–100 ms) with windows for MAL-EEM (0–20), SwarmCore (20–60), MissionPlanner (60–100). Monochrome blueprint, vector, 16:9."
-->

## Configuration Artefacts
- `os/configuration/a653/partition.xml` — partition definitions, APEX ports, budgets.  
- `os/configuration/a653/schedule.xml` — major frame & windows.  
- `os/configuration/manifests/manifest.yaml` — hashes, SBOM references, sign-off, QS anchor.  
- `os/rtos/*` — board/RTOS configuration.

## Compliance Mapping (excerpt)
- **DO-178C / DO-297:** plans, standards, CM, and verification (see `os/compliance/`).  
- **DO-326A/356A:** security risk assessment & objectives for partitions and APEX channels.  
- **S1000D:** data modules in `os/S1000D/` for IETP/IETM references.

<!-- COPILOT:IMAGE
title: "Compliance Matrix — ATA-42"
save_to: "assets/diagrams/ata42_compliance_matrix_v1.png"
prompt: "Matrix mapping Artefacts (partition.xml, schedule.xml, tests, manifests) to DO-178C/DO-297 and DO-326A/356A objectives. Monochrome, vector, 16:9."
-->

## Evidence & QS
**Evidence bundle (minimum):**
- Config artefacts (`partition.xml`, `schedule.xml`) with **SHA-256** hashes.  
- Test/coverage reports (health monitoring, APEX channel checks).  
- Signed manifest with reviewers, MAL-EEM guard, UTCS-MI version, **QS anchor**.

## Work Packages
WP | Deliverable | Location hint | Done
-- | -- | -- | --
WP-01 | IMA Architecture Overview | `docs/ima_overview.md` | ☐
WP-02 | Partition Definition & ACLs | `os/configuration/a653/partition.xml` | ☐
WP-03 | APEX Interface Spec (Ports, Modes) | `docs/apex_interfaces.md` | ☐
WP-04 | ARINC-653 Schedule & Budgets | `os/configuration/a653/schedule.xml` | ☐
WP-05 | Health Monitoring & Recovery (hooks to ATA-45) | `os/testing/health/` | ☐
WP-06 | Security & Ethics Boundaries (MAL-EEM) | `os/compliance/ethics_security/` | ☐
WP-07 | DO-178C Planning/Standards Mapping | `os/compliance/do178c/` | ☐
WP-08 | Verification Artefacts (MC/DC if applicable) | `os/testing/coverage/` | ☐
WP-09 | Evidence Manifest (hashes, QS seal) | `os/configuration/manifests/manifest.yaml` | ☐

## Change Control
- RFCs, risks, and approvals tracked under `ata/ATA-42/governance/`.  
- Any change that touches safety/ethics paths must include an **ethics note** and pass MAL-EEM tests before merge.

## Revision History
Rev | Date | Description | QS/UTCS Ref
-- | -- | -- | --
0 | 2025-10-01 | Initial placeholder (pre-standardization) | n/a
1 | 2025-10-01 | Standardized ATA-42 README (IIS) | pending
2 | 2025-10-01 | Added Copilot placeholders; clarified APEX/schedule | pending
```


