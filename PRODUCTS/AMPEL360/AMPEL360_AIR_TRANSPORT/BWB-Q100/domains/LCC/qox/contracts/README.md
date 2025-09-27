---
id: LCC-QOX-CONTRACTS-OV-0001
project: AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/LCC/qox/contracts/README.md
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

# LCC QOx Contracts

This directory contains Quantum Boundary (QB) contracts for the BWB-Q100 autopilot system, defining the interface and safety constraints for quantum-assisted advisory functions.

## Purpose

Provides QB layer contracts for:

- **Advisory isolation** - Strict quantum boundary enforcement with no control authority
- **Safety constraints** - Physics-based validation predicates for fuel, separation, terrain
- **Time budgets** - Maximum age limits and adoption criteria for QB recommendations
- **Evidence requirements** - UTCS signature and backend recording for auditability

## Contract Files

### `qb_autopilot_contract.yaml`
**QB Autopilot Boundary Contract**

Defines the quantum boundary interface for BWB-Q100 autopilot advisory functions.

#### Key Properties
- **Role**: `advisory` (no direct control authority)
- **Max Age**: 20 seconds (QB advice expires after 20s)
- **Topics In**: Weather nowcast, ATC slots, winds aloft, company efficiency
- **Topics Out**: LCC plan advice (advisory trajectory recommendations)

#### Safety Predicates
QB advice is accepted only when ALL predicates are true:
```yaml
accept_predicates:
  - "Δfuel_pct <= 3.0 && min_separation_nm >= 5 && terrain_clear == true"
  - "time_to_conflict >= 600"   # seconds
```

**Predicate Validation:**
- **Fuel impact**: ≤3% fuel consumption change
- **Separation**: ≥5nm minimum separation from other aircraft
- **Terrain clearance**: Must be terrain clear
- **Conflict time**: ≥600 seconds before any predicted conflict

#### Fallback Mechanism
- **Fallback**: `"retain current plan"`
- QB failures or violations → system retains existing flight plan
- No degradation of autopilot capability on QB unavailability

#### UTCS Requirements
- **Signature required**: All QB recommendations must be cryptographically signed
- **Backend recording**: Complete audit trail of QB interactions and decisions
- **Evidence chain**: Full provenance from QB input to autopilot decision

## Integration

The contract integrates with:
- **CB Layer** - Classical control laws receive advisory input only
- **UE Layer** - Package validation enforces contract compliance
- **FE Layer** - Safety federation monitors QB boundary violations
- **QS Layer** - Evidence recording and signature verification

## Validation

Contract is validated by:
- `scripts/validate_qb_contract.py` - Safety predicate and boundary validation
- `.github/workflows/lcc_qafbw_gate.yml` - Automated CI contract verification
- **Runtime monitoring** - Continuous QB boundary compliance checking

## Safety Philosophy

The QB contract implements **defense in depth**:
1. **Isolation**: QB has no direct control authority
2. **Validation**: Physics-based predicates filter unsafe recommendations
3. **Time limits**: Stale advice is automatically discarded
4. **Fallback**: System degradation is graceful with plan retention
5. **Auditability**: Complete evidence chain for certification

---

*Quantum boundary contract for safe BWB-Q100 autopilot advisory integration*