---
id: GAIA-DS2-LIGHTVIBES-OV-0001
project: GAIA-DS2 / LIGHTVIBES
artifact: LIGHTVIBES/README.md
llc: SECURITY
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: 2025-09-23
maintainer: "GAIA DS2 — Data Science for Deep Space"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# LIGHTVIBES — Quantum Micropulse Keying (QMK)

**One-liner:** LIGHTVIBES is a just-in-time key service that streams **single-use quantum "micropulses"** (photonic symbols) to establish fresh session keys on demand for **GAIA DS2** air/space links.

> **Org note:** *GAIA DS2 — GAIA Data Science for Deep Space* is the overarching organization for this repository.

## What it is
- **Paradigm:** QKD-inspired "micropulse" key feed + classical auth hardening  
- **Scope:** Space (inter-sat, sat–ground), Air (UAV/UAM→ground), cross-domain relays  
- **Outcome:** No static keys at rest; every session bootstraps with ephemeral, quantum-anchored entropy

## Why it's different
- **Micropulse keys:** Each pulse contributes one-time bits; once measured, it's gone (tamper-evident)  
- **Zero standing secrets:** Keys are derived → used → binned  
- **Graceful degrade:** If quantum channel drops, fall back to PQC KEM with audit flag

## High-level flow
1. **Sync & Auth** — Classical mutual auth (PQC certs)  
2. **Micropulse Exchange** — Photon stream encodes raw key bits; eavesdropping ⇒ QBER spike  
3. **Sifting & EC** — Basis reconciliation + error correction (LDPC)  
4. **Privacy Amplification** — Hashing (e.g., Toeplitz) to distill final key  
5. **Key Hand-off** — Inject into AEAD (AES-GCM/ChaCha20-Poly1305)

### Minimal interface
```
POST /lightvibes/session
→ { peer_id, policy:{min_keybits:256, ttl_s:120}, fallback:"PQC" }
← { session_id, key_ref, health:{qber, rate_bps}, mode:"QMK"|"PQC" }

GET /lightvibes/key/{key_ref}
→ ephemeral key (sealed to HSM/TEE), usage=one-shot
```

## Trust & safety
- **Tamper signal:** Monitor QBER; above threshold ⇒ quarantine channel, rotate mode, raise QS event  
- **Evidence:** UTCS/QS attaches run IDs, QBER, sifting stats, PA hash seeds  
- **Ethics guard:** MAL-EEM blocks disallowed contexts; logs are immutable

## Deployment profiles
- **GAIA-SPACE:** Sat↔sat lasercom QMK; ground stations as entropy relays  
- **GAIA-AIR:** UAV swarm ↔ ground backhaul, with urban fiber QMK taps  
- **Cross-domain:** Store-and-forward **key capsules** (signed & time-boxed)

## KPIs
Secure key rate (bps) · QBER · Time-to-key (256/512b) · Fallback ratio (PQC/QMK) · Energy/bit

## Roadmap
M0: Lab fiber demo, PQC fallback, UTCS hooks  
M1: Air-ground pilot (fiber + free-space)  
M2: Sat-emulator + moving-platform tests (adaptive PA)  
M3: In-orbit pathfinder (inter-sat QMK)

---

## Diagrams

### Sequence — QMK session (Mermaid)
```mermaid
sequenceDiagram
  participant A as Node A (GAIA link)
  participant B as Node B (Peer)
  participant Q as Quantum Channel
  participant C as Classical Channel (PQC/TLS)
  A->>C: 1) Mutual auth (PQC certs)
  A->>Q: 2) Send/receive micropulses (raw bits)
  B-->>Q: 2) Measure pulses (basis choices)
  A-->>C: 3) Sifting (basis recon)
  B-->>C: 3) Sifting + Error Correction (LDPC)
  A->>B: 4) Privacy Amplification (seed exchange)
  A->>A: 5) Seal key in HSM/TEE (key_ref)
  B->>B: 5) Seal key in HSM/TEE (key_ref)
  A->>B: Data plane starts (AEAD with fresh key)
  Note over A,B: Monitor QBER; if high → switch to PQC KEM, raise QS event
```

### Components — reference (Mermaid)

```mermaid
flowchart TB
  subgraph Edge[GAIA DS2 Edge/Flight]
    AgentA[Agent A<br/>HSM/TEE]
    QRxA[Q Photonics Rx/Tx]
  end
  subgraph Peer[Remote Peer]
    AgentB[Agent B<br/>HSM/TEE]
    QRxB[Q Photonics Rx/Tx]
  end
  subgraph Control[Control Plane]
    API[LIGHTVIBES API]
    KMS[Key Vault (sealed refs only)]
    QS[UTCS/QS Evidence Bus]
  end

  QRxA <-- quantum pulses --> QRxB
  AgentA <-- TLS/PQC --> API
  AgentB <-- TLS/PQC --> API
  API --> KMS
  API --> QS
  AgentA -. data AEAD .- AgentB
```

## Quickstart (dev)

* OpenAPI: `LIGHTVIBES/api/openapi.yaml`
* Reference server (dev): `uvicorn LIGHTVIBES.api.server:app --reload`
* Env: `LIGHTVIBES/.env.example` for knobs (QBER thresholds, key TTL)

## Evidence & Compliance

UTCS/QS evidence is mandatory for each session init and key hand-off (hashes, operator, policy/model/data). MAL-EEM ethics guard is enforced at the API gateway and within mission policies.