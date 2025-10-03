---
id: ASIT2-WHITEPAPER-MAL-2
project: ASI-T2
artifact: Master Whitepaper #2 — MAL (Master Application Layer) · Technical Specification
llc: GENESIS
classification: PUBLIC-DRAFT
version: 0.1.0
release_date: "2025-10-03"
author: "Amedeo Pelliccia"
maintainer: "ASI-T Architecture Team"
bridge: "QS→FWD→UE→FE→CB→QB"
ethics_guard: MAL-EEM
utcs_mi: v5.0
framework: TFA-V2
status: "Public draft for technical review"
ssot: "ASI-T · Universal Injection Prompt (v1)"
canonical_hash: pending
doi: TBA
---

# MASTER WHITEPAPER #2 · MAL (Master Application Layer)  
**Technical Specification under TFA-V2 and UTCS Bundling**

> **IDEALE-EU — Intelligence, Defense, Energy, Aerospace, Logistics (ESG-EU):**  
> Strategy overlay guiding governance, disclosure and EU-centric impact.

---

## 0. Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY** are to be interpreted as normative requirements in this specification.

---

## 1. Executive Summary

**MAL (Master Application Layer/Logic)** is the **domain PLC** for ASI-T2: a compact, composable runtime and contract suite that standardises **IO drivers, messaging, telemetry, health, logging, key/policy**, and **evidence hooks** across products and domains. MAL ensures that **every artifact is shippable with proofs** (SBOM, signatures, UTCS bundles) and **converges** the TFA-V2 bridge:

> **QS → FWD → UE → FE → CB → QB**  
> (*QS* Primordial · *FWD* Prediction/Probability / Forward Wave Dynamics · *UE* Unit Element/Collapse · *FE* Federation Entanglement/Contracting · *CB* Classical Bit/Companion Binary · *QB* Bit Cubic, non-quantumised)

MAL is **transport-agnostic**, **schema-versioned**, **policy-driven**, and **evidence-native**. It powers AMPEL360 BWB-Q100 and the Digital Platform CSDBs while preserving **AMPEL360/ commons** semantics (ontology/deontology/source-data; no app code).

---

## 2. Scope & Objectives

### 2.1 Scope
- **Products:** AMPEL360 (commons + identities), GAIA-AIR/SPACE, H₂-AIRPORT, BITFINANCE, INTELLIGENCE-SECRETARY.  
- **Domains:** AAA…PPP (15 canonical domains).  
- **Docs:** ATA/S1000D CSDB integration, UTCS packaging.  
- **Evidence:** SBOM, signed tags, UTCS thread/bundle, DOIs.

### 2.2 Objectives
- Single **contract** for control, telemetry, health, logging.  
- Deterministic **message & schema evolution** (major/minor).  
- **Zero-trust** posture with key/policy enforcement.  
- **Reproducibility**: one-click builds, hashes, attestations.  
- **Bridge alignment**: observable flows across QS→…→QB.

---

## 3. Architecture Overview

### 3.1 Planes
- **Data Plane** — ingestion, telemetry, append-only storage with UTCS hooks.  
- **Control Plane** — missions, keys, policies (**MAL-EEM**), access.  
- **Model Plane** — SIL/HIL twins, assertions, scenario engines.  
- **Evidence Plane** — SBOM, in-toto/SLSA-lite, DOIs, signed tags.

### 3.2 Components
- **mal-io** (drivers/adapters)  
- **mal-bus** (pub/sub adapters: NATS, MQTT5, Kafka, RTPS/DDS, AMQP; selectable)  
- **mal-ctl** (commanding & idempotency)  
- **mal-tmx** (telemetry framing & timelines)  
- **mal-hlth** (health, heartbeats, liveness/readiness)  
- **mal-log** (structured logging + signed flight-recorder)  
- **mal-sec** (keys, identities, policy, envelopes)  
- **mal-ver** (versioning, migrators, compatibility gates)  
- **mal-evd** (UTCS + evidence emitters: SBOM, hashes, tag signing)

### 3.3 Deployment profiles
- **edge-micro** (vehicles, benches)  
- **site-node** (ground/airport/ops)  
- **control-hub** (mission & evidence)  
All profiles MUST expose the **same contracts**; only throughput and retention differ.

---

## 4. Versioning & Compatibility

- **SemVer:** `MAJOR.MINOR.PATCH`
  - **MINOR** versions MUST be **backward-compatible** on the wire.  
  - **MAJOR** versions MAY break compatibility but MUST ship **migrators**.  
- **Schema headers:** every frame MUST carry:
  - `mal-version`, `schema-id`, `schema-rev`, `contract`, `compat-minor`.  
- **Negotiation:** responders MUST accept any `compat-minor` ≤ **their** minor.

---

## 5. Contracts (wire-level)

### 5.1 Frame Envelopes (common)
```json
{
  "hdr": {
    "mid": "9d1b...f1",                // message id (UUIDv7)
    "ts": "2025-10-03T09:12:11.456Z",  // ISO-8601 (UTC)
    "seq": 102934,                     // per-stream monotonic
    "src": "BWB-Q100.AAA.ATA-57",      // source identity
    "contract": "MAL.v1.telemetry",    // or MAL.v1.control/log/health
    "schema-id": "ampel360/telemetry/v1",
    "schema-rev": 4,
    "mal-version": "1.2.0",
    "compat-minor": 2,
    "sig": "base64(ed25519(signature))",
    "key-id": "ed25519:QS:core:0001"
  },
  "body": { /* contract-specific payload */ }
}
```

### 5.2 Control (`MAL.v1.control`)

* **Command** MUST be **idempotent** with `idempKey`.
* **Ack/Nack** within `ackTimeout` with reason codes.

```json
{
  "cmd": "set_mode",
  "target": "BWB-Q100.flight_ctl",
  "args": { "mode": "AUTO" },
  "idempKey": "f1cf-...-b702",
  "ttlMs": 3000
}
```

**NACK reasons (non-exhaustive):**
`MAL-1001` invalid-schema · `MAL-1002` unauthorized · `MAL-1003` precondition-failed · `MAL-1004` deadline-exceeded.

### 5.3 Telemetry (`MAL.v1.telemetry`)

* **Clock:** UTC; sender MUST monotonic-increase `seq`.
* **Integrity:** per-packet signature; optional stream MAC window.

```json
{
  "points": [
    {"k":"bus.latency.p50.ms","v":3.9},
    {"k":"wing.load.left.kN","v":12.7},
    {"k":"fuel.h2.temp.K","v":20.1}
  ],
  "tags": {"sns":"57-10","unit":"SI","mission":"sim-H0-2025-10-03"}
}
```

### 5.4 Health (`MAL.v1.health`)

* **Liveness:** `alive=true` heartbeat each `Δt` ≤ 2s (edge-micro), ≤ 10s (site-node).
* **Readiness:** dependency graph; leaf failures annotate `reason`.

### 5.5 Logging (`MAL.v1.log`)

* **Levels:** TRACE/DEBUG/INFO/WARN/ERROR.
* **Flight-recorder:** segments MUST be **signed** and **sequence-linked** (hash chain).

---

## 6. Topic & Path Grammar

### 6.1 Topic naming (bus-agnostic)

```
mal/<major>/<contract>/<product>/<domain>/<component>/<stream>
```

Example:

```
mal/1/telemetry/BWB-Q100/AAA/ATA-57/wing/left
```

### 6.2 TFA repository path (normative)

```
domains/<DOMAIN>/ATA-XX/<XX-XX>_<DESCRIPTION>/S1000D/<LAYER>/<PACK>/<SUBPACK>
```

* `<LAYER>` ∈ {QS,FWD,UE,FE,CB,QB}
* `<PACK>` ∈ {CAx,QOx,PAx}; **PAx orientation markers**: **OB=Onboard**, **OFF=Outboard** **ONLY**.

---

## 7. Security Model (MAL-SEC)

* **Identities:** device/service identities MUST be unique and attestable.
* **Keys:** Ed25519 for signing, X25519 for E2E session (or equivalent strength).
* **Envelopes:** payloads MAY be envelope-encrypted; headers remain routable.
* **Policy:** **MAL-EEM** governs allow-lists, duty logs, kill-switches.
* **AuthZ:** policy engine evaluates **subject × action × resource × context** with SLO/mission constraints.
* **Secrets:** NEVER in payload; fetch via sealed channels; rotate keys on `N` uses or `T` days (whichever earlier).

**Threat model (summary):** replay, impersonation, schema-poisoning, downgrade, side-channel. Mitigations: `idempKey`, time-bound tokens, minor-negotiation floor, constant-time verifiers, per-stream MACs.

---

## 8. Observability & Evidence

* **Timelines:** every mission stream MUST produce a **timeline** (events + metrics).
* **UTCS hooks:** `mal-evd` MUST emit UTCS thread/bundle entries:

  * **Context/Content/Cache** ↔ **Structure/Style/Sheet**
* **SBOM:** `syft` or equivalent; SPDX-JSON stored under `evidence/`.
* **Sign & Tag:** `git tag -s vX.Y.Z` + SHA256 of artifacts.
* **DOI:** releases SHOULD publish a DOI (e.g., Zenodo).

---

## 9. Performance & SLOs (H0 targets)

* **End-to-end control latency:** p95 ≤ **25 ms** (edge-micro), ≤ **120 ms** (site-node).
* **Telemetry throughput:** ≥ **10 kPts/s** per node (edge), ≥ **50 kPts/s** (hub).
* **Health heartbeat loss:** ≤ **0.1%** per 24 h.
* **Uptime:** ≥ **99.5%** (H0), roadmap to **99.9%** (H1).
* **Evidence emission lag:** ≤ **30 s** from segment close.

---

## 10. Compliance & Ethics

* **Safety:** ARP4754A/ARP4761 (scoped), DO-178C level C/D guidance, DO-254 when HW programmable.
* **Space:** progressive ECSS.
* **Export:** EU 2021/821; ITAR/EAR if applicable.
* **Ethics:** **MAL-EEM** non-weaponisation, decision logging, revocation.

---

## 11. Reference Implementation

* **Languages:** C++ (edge), Rust (edge/site), Python/Go (hub tooling).
* **Adapters:** `mal-bus-nats`, `mal-bus-mqtt5`, `mal-bus-dds`.
* **SDK layout (common):**

```
sdk/<lang>/
  core/   # frames, headers, ids, time
  bus/    # adapters
  sec/    # keys, sign/verify, envelope
  ctl/    # commands
  tmx/    # telemetry writer/reader
  hlth/   # liveness/readiness
  log/    # structured + flight-recorder
  evd/    # utcs + evidence writers
```

---

## 12. Testing & V&V

* **SIL/HIL campaigns:** property-based assertions, scenario coverage, packet-fuzz.
* **Compatibility tests:** minor-compat matrix; major migrator tests.
* **Security tests:** replay/downgrade/impersonation harness.
* **Performance tests:** sustained throughput, burst, loss injection.

---

## 13. Roadmap

* **H0 (0–90d):** MAL v1.0 cores (ctl/tmx/hlth/log/sec), NATS/MQTT5 adapters, UTCS hooks, SBOM pipeline.
* **H1 (3–9m):** DDS/RTPS adapter, mission planner API, timeline visualiser, observability packs.
* **H2 (9–24m):** multi-org federation policies, hardware roots (TPM/SE), third-party audits.

---

## 14. Glossary (canon, MAL-focused)

* **MAL** — Master Application Layer/Logic (domain PLC).
* **UTCS** — **UiX Threading Context/Content/Cache & Structure/Style/Sheet** (deterministic bundling).
* **QS/FWD/UE/FE/CB/QB** — TFA flow (see Master Whitepaper #1). **QB ≠ qubit**.
* **QOx** — **Quantum Optimizations** (not "quality operations").
* **PAx** — Packaging & Assemblies (**OB = Onboard**, **OFF = Outboard** only).
* **AMPEL360 (commons)** — progenitor source (ontology/deontology/source-data), no app code.
* **CSDB** — S1000D Common Source DataBase.
* **DMC/SNS** — Data Module Code / Standard Numbering System.
* **IMA** — Integrated Modular Avionics (ATA-42).
* **UTCS Bundle** — the bound set of narrative/data with structure/style/sheet for reproducible builds.

---

## 15. Security & Error Codes (extract)

| Code     | Meaning                    | Action                                             |
| -------- | -------------------------- | -------------------------------------------------- |
| MAL-1001 | Invalid schema / revision  | Retry after fetching `schema-rev`; report evidence |
| MAL-1002 | Unauthorized               | Re-auth; check MAL-EEM policy & key-id             |
| MAL-1003 | Precondition failed        | Satisfy deps; re-issue UE; log reason              |
| MAL-1004 | Deadline exceeded          | Increase `ttlMs` or reduce path latency            |
| MAL-1101 | Signature mismatch         | Drop frame; rotate keys; alert                     |
| MAL-1201 | Minor-compat floor not met | Negotiate compatible minor; or use migrator        |

---

## 16. S1000D / ATA Integration

* **Mapping:** each MAL contract has a **DMC map** entry for CSDB publication.
* **Example:** `AMPEL360-BWBQ100-46-00-LOG-REC-A-01-EN-00` → Flight-Recorder Ops Manual, referencing `mal-log` chain semantics.
* **Issue trees:** CSDB **issue_map.yml** SHOULD include MAL control & telemetry annexes for repeatability.

---

## 17. UTCS Bundling Profile (MAL)

```yaml
utcs/manifest.yaml
bundles:
  context:
    - docs/mal/overview.md
  content:
    - schemas/mal.control.v1.json
    - schemas/mal.telemetry.v1.json
    - schemas/mal.health.v1.json
    - schemas/mal.log.v1.json
  cache:
    - cache/examples/mal_hello.pdf
  structure:
    - docs/mal/topic_grammar.md
    - docs/mal/security_model.md
  style:
    - style/mal.csl
  sheet:
    - sheet/Makefile
```

---

## 18. Appendices

### A) JSON Schemas (extract)

**`schemas/mal.control.v1.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MAL Control v1",
  "type": "object",
  "required": ["cmd","target","idempKey"],
  "properties": {
    "cmd": {"type":"string","minLength":1},
    "target":{"type":"string","pattern":"^[A-Z0-9_.-]+$"},
    "args":{"type":"object"},
    "idempKey":{"type":"string","minLength":8},
    "ttlMs":{"type":"integer","minimum":1}
  }
}
```

**`schemas/mal.telemetry.v1.json`**

```json
{
  "$schema":"https://json-schema.org/draft/2020-12/schema",
  "title":"MAL Telemetry v1",
  "type":"object",
  "required":["points"],
  "properties":{
    "points":{
      "type":"array",
      "items":{"type":"object","required":["k","v"],
        "properties":{"k":{"type":"string"},"v":{}}
      }
    },
    "tags":{"type":"object"}
  }
}
```

### B) Topic Grammar Cheatsheet

* Control: `mal/1/control/<product>/<domain>/<component>/<unit>`
* Telemetry: `mal/1/telemetry/<product>/<domain>/<component>/<signal>`
* Health: `mal/1/health/<product>/<service>`
* Log: `mal/1/log/<product>/<domain>/<component>`

### C) Example Session (pseudo)

```
Client → mal-ctl.set_mode(AUTO) [idempKey=K] → Ack ts=+9ms
Edge   → mal-tmx.points([...]) seq+=1        → Hub ts=+4ms
Hub    → mal-hlth.heartbeat(alive=true)      → Timeline append
Hub    → mal-evd.utcs_emit(bundle: release)  → Hash+SBOM+tag
```

### D) PAx Orientation

* **ONLY** `OB` (Onboard) and `OFF` (Outboard) markers are allowed within PAx paths and metadata.

### E) Compatibility Matrix (minor)

| Producer | Consumer | Result                                                   |
| -------- | -------- | -------------------------------------------------------- |
| 1.2.x    | 1.1.x    | **ACCEPT** if `compat-minor` ≤ 1; else **NACK MAL-1201** |
| 1.2.x    | 1.3.x    | **ACCEPT** (consumer supports ≥ producer minor)          |

---

## 19. How to Cite

> Pelliccia, A. (2025). *MAL (Master Application Layer) Technical Specification*. v0.1.0. DOI: TBA.
> Machine-readable citation to be added in `CITATION.cff`.

---

## 20. Licence & Responsible Use

Open draft under **responsible use**. Redistribution/modification MUST retain **MAL-EEM** references and peaceful-use restrictions.

---

**End of Master Whitepaper #2 — MAL Technical Specification**
