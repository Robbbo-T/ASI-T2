---
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/LCC/utcs/README.md
bridge: CB→QB→UE→FE→FWD→QS
canonical_hash: TBD
classification: INTERNAL–EVIDENCE-REQUIRED
ethics_guard: MAL-EEM
id: LCC-UTCS-OV-0001
llc: SYSTEMS
maintainer: ASI-T Architecture Team
project: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100
release_date: '2025-01-22'
utcs_mi: v5.0
version: 0.1.0
---

# LCC UTCS Evidence Package

This directory contains UTCS (Universal Trust and Certification System) evidence manifests for the BWB-Q100 QAFbW autopilot system, providing comprehensive provenance and verification data.

## Purpose

Provides UTCS evidence for:

- **Build provenance** - Complete toolchain and source verification
- **Test verification** - HIL execution results and coverage metrics
- **QB advisory evidence** - Quantum boundary interaction statistics
- **Certification support** - Evidence package for type certificate

## Evidence Files

### `utcs.manifest.json`
**Extended UTCS Evidence Manifest**

Comprehensive evidence package with BWB-Q100 specific extensions:

#### Build Provenance
```json
{
  "artifact": "qafbw_flight_ctrl.bin",
  "canonical_hash": "sha256:...",
  "inputs": {
    "commit": "GIT_SHA",
    "params": "cfg/qafbw_params.yaml#sha256:...",
    "toolchain": "gcc-12.3 -O2 -fno-fast-math"
  }
}
```

#### Verification Metrics
```json
{
  "verification": {
    "mcdc": 1.0,                    // MC/DC coverage requirement
    "hil_runs": 1200,               // Hardware-in-loop test count
    "deadline_misses": 0,           // Real-time compliance
    "jitter_us_p999": 80,           // p99.9 timing jitter
    "cross_axis_coupling_max": 0.14, // BWB coupling limit
    "sync_skew_ms_p95": 3.8,        // Surface sync timing
    "allocator_recovery_cycles_max": 2 // Post-failure recovery
  }
}
```

#### QB Advisory Statistics
```json
{
  "qb_advisory": {
    "enabled": true,
    "accept_predicates": 2,         // Safety predicate count
    "adopted_pct": 0.31,           // Advice adoption rate
    "rejected_pct": 0.69           // Safety rejection rate
  }
}
```

#### Provenance Chain
```json
{
  "provenance": {
    "ci_run": "GH-12345",
    "timestamp_utc": "2025-09-28T11:03:12Z"
  },
  "qs": {
    "sig": "cosign://…/qafbw:1.0.0.sig",
    "intoto": "oci://…/qafbw:1.0.0.intoto"
  }
}
```

## BWB-Q100 Extensions

The manifest includes BWB-specific evidence fields:

### Control System Metrics
- **Cross-axis coupling**: Maximum |Gij/Gii| across flight envelope
- **Surface synchronization**: p95 timing skew between paired surfaces
- **Allocator performance**: Post-failure recovery cycle count

### Real-Time Compliance
- **MC/DC coverage**: 1.0 (100% decision/condition coverage)
- **Deadline compliance**: 0 misses across all testing
- **Jitter analysis**: p99.9 timing variation under multicore interference

### QB Integration Evidence
- **Advisory adoption**: Statistical analysis of QB recommendation acceptance
- **Safety rejection**: Rate of advice discarded due to predicate failures
- **Boundary compliance**: Quantum isolation verification

## Integration

UTCS evidence integrates with:
- **CI/CD Pipeline** - Automated evidence generation and validation
- **AQUA OS VCRM** - Component verification and release management
- **TFA Gates** - Bridge pattern evidence requirements
- **Type Certificate** - Certification authority evidence submission

## Validation

Evidence integrity is ensured by:
- **Cryptographic hashing** - SHA-256 canonical hash verification
- **Digital signatures** - Cosign attestation and verification
- **SBOM integration** - Software Bill of Materials linkage
- **Audit trail** - Complete provenance from source to deployment

## Usage

Evidence is accessed through:
```bash
# Verify UTCS manifest integrity
utcs verify utcs.manifest.json

# Extract build provenance
jq '.inputs' < utcs.manifest.json

# Validate signature chain
cosign verify --key public.pem qafbw:1.0.0

# Check evidence completeness
python scripts/validate_evidence.py utcs.manifest.json
```

## Evidence Standards

All evidence complies with:
- **UTCS v5.0** - Universal Trust and Certification System standards
- **NIST SSDF** - Secure Software Development Framework
- **SLSA Level 3** - Supply-chain Levels for Software Artifacts
- **BWB-Q100 Requirements** - Aircraft-specific evidence criteria

---

*UTCS evidence package for BWB-Q100 autopilot certification and deployment*