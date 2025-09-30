---
id: ATA-42-OV-0001
project: AMPEL360_AIR_TRANSPORT / BWB-Q100
artifact: domains/IIS/ata/ATA-42/README.md
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: 2025-09-28
maintainer: IIS (Avionics / IMA)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# ATA-42 — Avionics (IMA)

This README is the Single Source of Truth for the Integrated Modular Avionics (IMA) stack of BWB‑Q100. It anchors architecture, interfaces, certification evidence, and CI rules under UTCS/QS.

**Scope** — IMA platform (ARINC 653), core services, partitions (applications), data buses (ARINC 664/AFDX, ARINC 429), computing modules, safety/security, and verification artifacts. Flight‑critical apps (e.g., QAFbW control stack) live here as DAL‑A partitions with strict segregation.

---

## 1) Architecture Snapshot

| Layer | Content | Notes |
|-------|---------|-------|
| Platform | IMA chassis, CM/CCMs, backplane, power & cooling | HW configuration & DO‑254 lineage |
| Kernel/OS | ARINC 653 RTOS with time/space partitioning | Health monitoring, MMU/MPU setup, HM API |
| Core Services | Clock sync (IEEE‑1588/PTP), file/log, maintainers, BIT/BIST | Deterministic scheduling windows |
| Partitions (Apps) | P‑FBW (DAL‑A), P‑NAV (DAL‑B), P‑DISP (DAL‑C), P‑MAINT (DAL‑D), P‑SEC (DAL‑B) | Each with budget (CPU %, RAM, I/O) |
| I/O & Buses | AFDX (ARINC 664 p7), ARINC 429, discrete I/O, A‑CAN (if used) | Virtual Links, BAGs, L2/L3 segregation |
| Maintenance | CMS/ACMS, snapshots, crash dumps | UTCS DET anchors for every log |

**True North:** partitions are immutable contracts. Any change to budgets, ports or VLs must pass CI policy + safety impact analysis.

---

## 2) Directory Map (hyperlinked)

```
platform/     — chassis, LRUs, CCAs, backplane, wiring..
os/           — ARINC‑653 configuration (schedules, HM tables, memory maps)
partitions/   — application partitions (FBW, NAV, DISP, MAINT, SEC)
interfaces/   — ICDs and port maps (sampling/queueing)
buses/        — AFDX/ARINC429 definitions & tools
  afdx/       — VL table, BAGs, policing, redundancy
  a429/       — RX/TX channels, labels, refresh
safety/       — ARP4754A/4761, FHA/PSSA/SSA, DAL mapping
security/     — DO‑326A/356A/355A, threat models, mitigations
verification/ — DO‑178C plans (PSAC/SDP/SVP/SCMP/SCS), SVP cases & results
cert/         — conformity, means of compliance, Stage of Involvement
configs/      — parameter sets, SBOMs, UTCS manifests
tools/        — build chains, linters, simulators, recorders
```

---

## 3) Interfaces & Buses (authoritative extracts)

### AFDX (ARINC 664 p7)

| VL | Source Partition | Sink(s) | BAG | Max L2 (B) | Redund. | QoS |
|----|------------------|---------|-----|------------|---------|-----|
| VL‑FBW‑CMD | P‑FBW | Actuation GW | 2 ms | 256 | A/B | High |
| VL‑NAV‑ATT | P‑NAV | P‑FBW, P‑DISP | 8 ms | 512 | A/B | Medium |
| VL‑MAINT‑LOG | P‑MAINT | Recorder | 100 ms | 1500 | A | Low |

Full table lives in `buses/afdx/vl_table.csv`. CI validates BAG/size/policing.

### ARINC 429

| Channel | Rate | Label(s) | Producer → Consumer |
|---------|------|----------|-------------------|
| RX‑1 | 12.5 kHz | 203, 204 (AoA) | Sensors → P‑FBW |
| TX‑2 | 12.5 kHz | 312 (CAS), 320 (ALT) | P‑NAV → Displays |

See `buses/a429/channel_map.csv` for the complete mapping.

---

## 4) Partition Budget (example seed)

| Partition | DAL | CPU % | RAM (MiB) | Ports (S/Q) | Windows (ms) | Notes |
|-----------|-----|-------|-----------|-------------|--------------|-------|
| P‑FBW | A | 35 | 64 | 8/6 | 2 | QAFbW control laws + monitors |
| P‑NAV | B | 20 | 48 | 6/6 | 8 | INS/GNSS fusion |
| P‑DISP | C | 15 | 64 | 4/8 | 16 | PFD/ND compositor |
| P‑MAINT | D | 10 | 32 | 2/6 | 50 | ACMS/CMS |
| P‑SEC | B | 10 | 32 | 2/4 | 10 | Crypto, attestation |

Budgets are locked by `os/schedule.xml` and validated in CI against this table.

---

## 5) Certification Mapping (evidence index)

| Objective Set | Standard | Evidence entry |
|---------------|----------|----------------|
| System development & allocation | ARP4754A | `safety/FHA_PSSA_SSA.md` |
| IMA cooperation & responsibilities | DO‑297/ED‑124 | `cert/DO297_Responsibility_Agreement.md` |
| SW life‑cycle (FBW DAL‑A, others B‑D) | DO‑178C | `verification/DO178C_PSAC.md` |
| Complex airborne electronic hardware | DO‑254 | `cert/DO254_Plan.md` |
| Security process | DO‑326A/ED‑202A + DO‑356A/ED‑203A | `security/SEC_Plans.md` |
| Environmental | DO‑160G | `cert/DO160G_Qual_Summary.md` |

All entries carry UTCS DET anchors and signers at merge‐time.

---

## 6) CI/QA Rules (fail closed)

- **Structure guard:** every link in this README must resolve.
- **AFDX police:** VL table validated (BAG, redundancy, payload) vs. schema.
- **ARINC 653:** schedule windows sum ≤ major frame; partition RAM/heap ≤ declared.
- **SBOM & provenance:** build artifacts signed (QS), SBOM diff allowed only with ticket.
- **Security:** cryptographic hardening checks (cipher suites, attestation keys) green.

CI templates in `tools/ci/`. Red = no merge.

---

## 7) Cross‑links

- **Flight controls (ATA‑27)** — QAFbW spec (interfaces to P‑FBW)
- **Displays (ATA‑31)** — Avionics displays
- **Electrical power (ATA‑24)** — Power & loads

---

## 8) Revision History

| Rev | Date | Author | Notes |
|-----|------|---------|-------|
| 0.1.0 | 2025‑09‑28 | IIS | Initial IMA README seed (hyperlinked, CI‑guarded) |
