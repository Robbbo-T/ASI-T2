---
id: LCC-TESTS-FAILURES-OV-0001
project: AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/LCC/tests/failures/README.md
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: "2025-01-22"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# LCC Test Failure Scenarios

This directory contains failure injection scenarios for BWB-Q100 autopilot testing, covering surface failures, sensor anomalies, and multi-failure conditions with acceptance criteria.

## Purpose

Provides comprehensive failure test scenarios for:

- **Surface failure validation** - Stuck, runaway, and loss-of-feedback conditions
- **Multi-failure testing** - Paired and cascading failure sequences
- **FDIR verification** - Fault Detection, Isolation, and Reconfiguration validation
- **Safety margin assessment** - Stability, PIO, and performance limit verification

## Test Scenario Files

### `sp2_l_stuck.json`
**SP2_L Surface Stuck Failure**

Tests spoiler SP2_L stuck at +8° during AP_ALT_HOLD mode.

**Acceptance Criteria:**
- Stability margin ≥ 6.0 dB
- PIO index < 0.5
- Allocator recovery ≤ 2 cycles
- Cross-coupling ≤ 0.15

**Expected Response:**
- FDIR action: `SURF_RECONF`
- Alert: `LCC-SURF-STUCK`
- Recovery time: ≤ 0.4s

### `elevon_runaway.json`
**EL2_L Elevon Runaway**

Tests elevon EL2_L runaway at -15°/s during NAV mode approach.

**Acceptance Criteria:**
- Stability margin ≥ 6.0 dB
- PIO index < 0.5
- Allocator recovery ≤ 2 cycles
- Runway tracking error ≤ 3.0m

**Expected Response:**
- FDIR action: `SURF_ISOLATE`
- Alert: `LCC-ELEVON-RUNAWAY`
- Recovery time: ≤ 0.3s

### `paired_failure.json`
**Paired Surface Failure**

Tests combined SP1_L stuck + SP1_R hydraulic pressure loss during APPROACH mode.

**Acceptance Criteria:**
- Stability margin ≥ 4.0 dB (reduced for multi-failure)
- PIO index < 0.6
- Allocator recovery ≤ 2 cycles
- Approach path deviation ≤ 50 ft

**Expected Response:**
- FDIR action: `AP_RECONFIG`
- Alert: `LCC-MULTI-SURF-FAIL`
- Recovery time: ≤ 0.8s

## Test Matrix Coverage

**Autopilot Modes:**
- `AP_ALT_HOLD` - Altitude hold with level flight
- `NAV` - Navigation mode with lateral guidance
- `APPROACH` - Precision approach with coupled guidance
- `GO_AROUND` - Go-around with climb and lateral guidance

**Failure Types:**
- `stuck` - Surface jammed at fixed angle
- `runaway` - Uncontrolled surface movement
- `loss_of_feedback` - Position sensor failure
- `hyd_press_low` - Hydraulic system degradation

**Multi-Failure Combinations:**
- **Paired failures** - One per wing side
- **Triple failures** - Adjacent spoilers
- **Cascading failures** - Secondary failures triggered by primary

## Integration

Test scenarios integrate with:
- **HIL Testing** - Hardware-in-the-Loop execution with BWB iron bird
- **CI Pipeline** - Automated execution via `run_hil_matrix.sh`
- **Evidence Package** - UTCS-anchored results in test reports
- **FDIR Validation** - Fault handling and recovery verification

## Usage

Scenarios are executed by:
```bash
# Single scenario HIL test
./scripts/run_hil_scenario.sh sp2_l_stuck.json

# Full failure matrix
./scripts/run_hil_matrix.sh --failures domains/LCC/tests/failures

# CI integration
# (automatically executed in lcc_qafbw_gate.yml workflow)
```

## Metrics Validation

Each test validates:
- **Control Performance** - Stability margins, PIO indices, tracking errors
- **Timing Compliance** - Recovery times, allocator cycles, sync skew
- **Safety Boundaries** - Cross-coupling limits, envelope protection
- **FDIR Response** - Correct fault identification and reconfiguration

---

*Comprehensive failure scenarios for BWB-Q100 autopilot certification testing*