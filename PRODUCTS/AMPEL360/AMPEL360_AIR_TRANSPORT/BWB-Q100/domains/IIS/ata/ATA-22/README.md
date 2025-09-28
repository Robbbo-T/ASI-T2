---
id: ATA-22-OV-0001
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/IIS/ata/22/README.md
llc: SYSTEMS
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "0.2.0"
release_date: 2025-09-27
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# ATA-22 — Auto Flight (BWB-Q100)  
**ES:** Publicaciones y evidencia para **ATA-22**.  
**EN:** Publications and evidence for **ATA-22 (Auto Flight)**.

> Scope: flight guidance, autopilot, autothrottle, autoland interfaces, mode logic, monitoring (BITE), and safety/ethics gates under **IIS** (Integrated Intelligence & Software).

---

## 0) Path Root (TFA)
`PRODUCTS/AMPEL360/BWB-Q100/domains/IIS/ata/22/`

---

## 1) Directory Map
```
22/
├── S1000D/
│   ├── brex/                                  # BREX rules
│   │   └── DMC-BWB1-A-00-00-00-00A-022A-D-EN-US.xml
│   ├── dmrl/                                  # Data Module Requirements List
│   │   └── DMRL-BWB1-A-22-00-00-00A-001A-D-EN-US.xml
│   └── data_modules/
│       ├── front_matter/                      # General/intro DMs
│       ├── descriptive/                       # 040A Description
│       ├── procedural/                        # 720A/721A Tasks (On-Aircraft/Shop)
│       ├── fault/                             # 940A Fault Isolation
│       └── illustrated_parts/                 # IPC/IPD if applicable
├── tests/
│   ├── ground/                                # ENG/APU power, taxi checks
│   └── flight/                                # AFCS enroute/approach/autoland checks
├── evidence/                                  # UTCS/QS proofs, log extracts
└── references/                                # ARINC 653/429/664, AFDX, HMI, FMS, etc.
```

---

## 2) System Breakdown (ATA-22)
- **22-10** Autopilot (AP)
- **22-11** Flight Director (FD)
- **22-12** Autothrottle / Thrust Management (A/T)
- **22-15** Altitude/Speed Alerting & Protections
- **22-18** Autoland / Approach Capability (as applicable)
- **22-20** AFCS Monitoring & BITE (Built-In Test)
- **22-90** Interfaces (FMS, QAFbW, NAVSYS, HMI)

> Cross-domain links: `INFRANET/AQUA_OS_AIRCRAFT/components/QAFbW/`, `NAVSYS/`, `HMI_BRIDGE/`, `NET_STACK/`.

---

## 3) S1000D Conventions
- **ModelIdentCode:** `BWB1` (program-local)
- **Language:** `EN-US` primary (Spanish mirrors allowed)
- **Info codes:** `020` General, `040` Description, `720/721` Procedures, `940` Faults
- **BREX:** see `S1000D/brex/DMC-BWB1-A-00-00-00-00A-022A-D-EN-US.xml`

---

## 4) Deliverables
- Descriptive DMs: AFCS architecture, mode logic, protections
- Procedural DMs: engagement checks, autoland preflight, go-around tests
- Fault DMs: mode drops, sensor mis-compare, servo runaway
- DMRL: authoritative list of required DMs with issue/lanes
- UTCS/QS evidence: canonical hashes, signatures, test logs
- Interface specs: A653 partitions, timing, A429 labels, A664 VLinks

---

## 5) Safety, Ethics & Security
- **MAL-EEM:** prioritise passenger/crew safety; bias-free mode naming; human factors in alerts
- **Least privilege:** AFCS partitions with deterministic timing; read-only rootfs; signed images
- **UTCS/QS:** all releases stamped with `canonical_hash` and cosign/in-toto attestations

---

## 6) CI Hooks
```bash
# Validate S1000D XML well-formedness (xmllint suggested locally)
# (Your repo guards)
python CAD/scripts/link_check.py . --json-report artifacts/link-ata22.json
python CAD/scripts/naming_guard.py . --json-report artifacts/naming-ata22.json
python CAD/scripts/validate_json.py CAD/schemas . --strict --junit artifacts/json-ata22.junit.xml
```

---

## 7) Changelog

* **v0.2.0 (2025-09-27):** Full skeleton, BREX seed, DMRL seed, sample procedure/fault DMs, interfaces.
* **v0.1.0 (2025-09-24):** Initial stub.