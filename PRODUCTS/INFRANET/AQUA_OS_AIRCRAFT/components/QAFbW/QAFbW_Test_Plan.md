---
id: ASIT2-AQUAOS-AIR-QAFBW-TP
project: ASI-T2
artifact: QAFbW Control Stack Test Plan
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0
release_date: 2024-09-23
maintainer: OOO (OS), LCC (Control Laws), EDI (Avionics/Net), IIS (Software), MEC (Actuation)
bridge: CB→QB→UE→FE→FWD→QS
ethics_guard: MAL-EEM
utcs_mi: |
  test_scope: conformance_verification
  coverage_target: MC/DC=100%
  evidence_sealing: UTCS/QS
canonical_hash: pending
---

# QAFbW Conformance Test Plan

## 1. Test Objectives

This test plan validates the QAFbW Control Stack component against its specification within the AQUA OS Aircraft Extension. The primary objectives are:

1. **Platform Conformance**: Verify operation within AQUA OS partition and scheduling contracts
2. **Safety Assurance**: Validate DAL-A safety requirements and fault handling
3. **Performance Validation**: Confirm timing, latency, and throughput requirements
4. **Quantum Boundary Isolation**: Ensure quantum services remain out-of-loop

## 2. Verification Environment

### 2.1 Time Sync & Calibration
- PTP/TTE GM switchover test performed before timing runs; drift < 50 ns/s.
- HIL clock aligned to AQUA OS monotonic clock; calibration log sealed via UTCS/QS.

### 2.2 Deterministic Network Impairment Profiles
- Nominal, A-fail, B-fail, GM-switchover, burst-loss(≤3 frames), latency-step(+300 µs).

### 2.3 Logging Schema (all campaigns)
- **Format**: JSONL
- **Common fields**: `ts`, `test_id`, `frame_seq`, `latency_us`, `jitter_us`, `cpu_pct`, `mode`, `event`, `result`
- **Seal**: Each log -> SHA-256 + UTCS/QS anchor; include SBOM id of test harness.

## 3. Test Campaigns

### Campaign A: Performance & Determinism (HIL)

#### Test A1: Timing & Jitter Analysis (QAFBW-T-001)
- **Objective**: Validate end-to-end latency and jitter budgets
- **Method**: 10,000-frame timing analysis under worst-case system load
- **Environment**: HIL with full sensor suite and actuator simulation
- **Pass Criteria**: p95 latency ≤10 ms, p100 ≤15 ms; per-topic jitter ≤ 500 µs; no deadline misses; CPU headroom ≥20%; zero dropped frames on active VLs.

#### Test A2: CPU & Memory Resource Analysis (QAFBW-T-007)
- **Objective**: Validate resource usage within partition boundaries
- **Method**: Load testing with concurrent partition stress
- **Pass Criteria**: No partition boundary violations; memory usage ≤64 MiB; CPU ≤30% sustained

### Campaign B: Safety, Modes & FDIR (HIL/Iron Bird)

#### Test B1: Mode Transitions (QAFBW-T-002)
- **Objective**: Validate flight control mode transitions
- **Method**: Pilot-in-the-loop evaluation of all mode transitions
- **Pass Criteria**: Transitions complete < 2 s; no oscillation (≤1 transition per fault); correct aural/visual cues; no hazardous behavior (per FHA).

#### Test B2: 2oo3 Voter & Fault Handling (QAFBW-T-003)
- **Objective**: Validate voting logic and fault response
- **Method**: Injected faults across sensor channels
- **Pass Criteria**: Voter enters `DISAGREE_FREEZE` within policy window; freeze holds until manual clear or health restore; actuator defaults commanded ≤ 20 ms after timeout.

#### Test B3: Envelope Protection (QAFBW-T-004)
- **Objective**: Validate flight envelope protection algorithms
- **Method**: HIL with envelope exceedance scenarios
- **Pass Criteria**: AoA, nZ, bank, Vmo/Mmo not exceeded; engagement rate-limited; pilot long-press override honored in DIRECT; no PIO introduced.

#### Test B4: Fault Detection & Mitigation (QAFBW-T-011)
- **Objective**: Validate fault detection timing
- **Method**: Injected critical faults with timing measurement
- **Pass Criteria**: Critical faults detected and mitigated ≤50 ms

### Campaign C: Quantum Boundary & Negative Testing (HIL)

#### Test C1: QAS Loss/Degradation (QAFBW-T-005)
- **Objective**: Validate quantum services remain out-of-loop
- **Method**: QAS service interruption during flight control operation
- **Pass Criteria**: Mode unchanged; latency/jitter budgets respected; malformed frames dropped with counter increment; security monitor raises event; no effect on actuator outputs.

#### Test C2: Security & Authentication (QAFBW-T-006)
- **Objective**: Validate secure boot and message authentication
- **Method**: Positive and negative security testing
- **Pass Criteria**: Secure boot validation; message authentication working; replay attacks detected

### Campaign D: Network & I/O Validation (HIL)

#### Test D1: Network Failover (QAFBW-T-008)
- **Objective**: Validate A/B network redundancy
- **Method**: Controlled network failures during operation
- **Pass Criteria**: Seamless failover; no control disruption; jitter budgets maintained

#### Test D2: Health & Diagnostics API (QAFBW-T-010)
- **Objective**: Validate health monitoring interfaces
- **Method**: API exerciser with health status verification
- **Pass Criteria**: All health parameters correctly reported; structured logs generated

## 4. Entry & Exit Criteria

### Entry Criteria
- QAFbW software build available with SBOM
- HIL environment calibrated and verified
- Test harness validated and sealed
- All test procedures reviewed and approved

### Exit Criteria
- 100% procedures executed; all VCRM items `PASS` or `DEFERRED` with risk acceptance; MC/DC=100% for DAL-A code; all Category 1/2 anomalies resolved; UTCS/QS bundle (`anchors/qseal_manifest.json`) produced with logs, configs, harness SBOM.

## 5. Evidence & Traceability

All test artifacts are sealed via UTCS/QS and linked through the VCRM matrix. Evidence includes:
- Test procedures and results
- Timing and performance logs
- Configuration snapshots
- Anomaly reports and resolutions
- Software build artifacts and SBOMs

---

*Part of INFRANET AQUA OS Aircraft Extension under ASI-T2 portfolio*