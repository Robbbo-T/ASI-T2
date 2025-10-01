# ASI-T2 Master Plan Structure

**Version**: 0.1.0  
**Date**: 2025-01-01  
**Status**: H0 Foundation

This document describes the complete structure of the ASI-T2 ecosystem implementation.

---

## Directory Structure

```
asi-t2/
├── MAL/                          # Master Application Layer (PLC de dominio)
│   ├── drivers/                  # Hardware drivers and HAL
│   ├── messaging/                # Pub-sub messaging system
│   ├── telemetry/                # Telemetry collection
│   ├── health/                   # Health monitoring and watchdogs
│   ├── registry/                 # Service discovery and config
│   └── README.md                 # MAL architecture documentation
│
├── INFRA/                        # Infrastructure Layer (4 planes)
│   ├── DATA-PLANE/              # Ingestión, storage, UTCS
│   ├── CONTROL-PLANE/           # Mission orchestration, policies, MAL-EEM
│   ├── MODEL-PLANE/             # Digital twins, SIL/HIL, simulation
│   ├── EVIDENCE-PLANE/          # SBOMs, DOIs, attestations, QS/UTCS
│   └── README.md                # Infrastructure architecture
│
├── PRODUCTS/                     # Product portfolio
│   ├── AMPEL360/
│   │   ├── AMPEL360_AIR_TRANSPORT/
│   │   │   └── BWB-Q100/
│   │   │       ├── spec/AMPEL360.yaml     # Product specification
│   │   │       ├── evidence/              # Test reports, demos
│   │   │       ├── sim/                   # SIL simulators
│   │   │       ├── hil/                   # HIL configurations
│   │   │       └── tests/                 # Test suites
│   │   └── AMPEL360_SPACE_TOURISM/
│   │       ├── spec/AMPEL360PLUS.yaml
│   │       └── evidence/
│   │
│   ├── GAIA-SPACE/
│   │   ├── spec/GAIA_SPACE.yaml          # Constellation specs
│   │   ├── evidence/                      # Mission demos
│   │   ├── ORBITAL-MACHINES/
│   │   └── SAT-CONSTELLATIONS/
│   │
│   ├── GAIA-AIR/
│   │   ├── IDRO_WALL/
│   │   │   ├── spec/DEFENSE_WALL_SWARM.yaml
│   │   │   └── evidence/
│   │   ├── HYDROBOTS/
│   │   └── ETHICS-EMPATHY-UAV/
│   │
│   └── INFRANET/                          # Digital infrastructure products
│       ├── META_OS_AEROSPACE/
│       ├── AQUA_OS_AIRCRAFT/
│       └── LH2_CORRIDOR/
│
├── AIRPORT_H2_LH2/               # H₂/LH₂ airport infrastructure
│   ├── models/                   # Capacity and flow models
│   ├── layouts/                  # Physical layouts and designs
│   ├── ops/                      # Operations procedures
│   └── README.md
│
├── FINANCE/                      # Sustainable finance model
│   ├── whitepaper/
│   │   └── SUSTAINABLE_FINANCE_MODEL.md
│   ├── specs/                    # Economic model specifications
│   └── testnet/                  # Testnet configurations
│
├── HALL-OF-RECORDS/             # Provenance and evidence archive
│   ├── CLAIM.md                 # Master claim document
│   ├── README.md                # Archive documentation
│   ├── horizons/                # Evidence by horizon (H0/H1/H2)
│   ├── attestations/            # Third-party attestations
│   ├── reviews/                 # External reviews
│   └── audits/                  # Audit reports
│
├── scripts/                      # Automation scripts
│   ├── make_evidence.sh         # Evidence generation (SBOM, UTCS, tags)
│   ├── verify_structure.py      # Structure validation
│   └── ...                      # Other utility scripts
│
├── .github/
│   └── workflows/
│       ├── evidence_validation.yml  # Evidence CI/CD
│       └── ...                      # Other workflows
│
├── CITATION.cff                 # Citation metadata
├── RELEASE.md                   # Release notes and roadmap
├── COMPLIANCE.md                # Compliance framework
├── README.md                    # Main repository README
└── .gitignore                   # Excludes evidence artifacts, etc.
```

---

## Core Concepts

### TFA (Top Federation Algorithm / Threading Final Assembly)

All products follow the TFA pattern:
```
CB (Conceptual Boundary) → Design and requirements
  → QB (Quantum Boundary) → Validation and advisories
    → UE (Unit Execution) → Component execution
      → FE (Final Execution) → System integration
        → FWD (Forward Deployment) → Deployment
          → QS (Quantum Seal) → Evidence and provenance
```

### MAL-EEM (Ethics & Empathy Module)

Ethical guardrails for all autonomous systems:
- Fail-closed by default
- Human oversight required
- Mission rules validation
- Safety constraints enforcement

### UTCS v5.0 (Universal Traceability & Configuration System)

Complete provenance tracking:
- Canonical hashes (SHA-256)
- Immutable timestamps
- Signature verification
- Evidence chains

---

## Product Specifications

Each product has a `spec/PRODUCT.yaml` file with:

```yaml
product: PRODUCT_NAME
trl: 3-4                        # Technology Readiness Level
maturity: "MVP → HIL → Production"
interfaces:
  control_bus: "MAL.v1.control"
  telemetry_bus: "MAL.v1.telemetry"
  data_schema: "schemas/v1/product.json"
standards_lite: ["safety-lite", "quality-lite"]
artifacts: ["SRS", "SDD", "V&V-plan", "SBOM", "demos"]
evidence:
  doi: "TBD"
  utcs_anchor: "TBD"
  signed_tag: "v0.1.0"
demos:
  - name: "Demo_Name"
    inputs: "inputs/scenarios/*.json"
    outputs: "evidence/demos/Demo_Name/"
    metrics: ["metric1", "metric2"]
horizons:
  H0_0_90_days:
    objectives: [...]
    deliverables: [...]
  H1_3_9_months:
    objectives: [...]
    deliverables: [...]
  H2_9_24_months:
    objectives: [...]
    deliverables: [...]
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: "MAL-EEM"
```

---

## Evidence Generation

### Automated Evidence

Run the evidence generation script:
```bash
./scripts/make_evidence.sh v0.1.0
```

Generates:
- SBOM (Software Bill of Materials) in SPDX 2.3 format
- SHA-256 checksums
- UTCS v5.0 anchor with canonical hash
- Release manifest
- Signed Git tag (if GPG configured)

### Manual Evidence

Add to appropriate horizon directory:
```
HALL-OF-RECORDS/horizons/H0/PRODUCT_NAME/
├── demo_video.mp4
├── test_report.md
├── utcs_anchor.json
└── README.md
```

---

## Horizon Roadmap

### H0 (0-90 days): MVPs Demostrables

**AMPEL360 BWB**:
- [x] Product spec created
- [ ] SIL gemelo digital
- [ ] Control básico + aerodinámica
- [ ] Demo video

**GAIA SPACE**:
- [x] Product spec created
- [ ] Orbit simulator
- [ ] Mission profiles
- [ ] Data Plane integration

**Defense Wall Swarm**:
- [x] Product spec created
- [ ] Multi-agent simulator (10-20 nodes)
- [ ] Mission rules engine
- [ ] Anti-collision basic

**MAL v1.0**:
- [x] Architecture defined
- [ ] Messaging system
- [ ] Telemetry collection
- [ ] Health monitoring

**AMPEL360PLUS Tourism**:
- [x] Product spec created
- [ ] Visual prototype
- [ ] Cabin mockup
- [ ] Safety requirements

**H₂/LH₂ Airport**:
- [x] Conceptual model
- [ ] Capacity calculations
- [ ] Layout designs
- [ ] Risk analysis

**Finance Model**:
- [x] Whitepaper created
- [ ] Economic simulations
- [ ] Smart contract specs

**Gate H0 → H1 (FCR-1)**:
- [x] All product specs defined
- [x] Evidence framework established
- [ ] Basic demos complete
- [ ] SBOM + UTCS for all products

### H1 (3-9 months): Enhanced Validation

- [ ] HIL (Hardware-in-Loop) for AMPEL360
- [ ] SDR bench for GAIA SPACE
- [ ] 50-100 nodes for Swarm
- [ ] External reviews (2+)
- [ ] Safety cases v1

**Gate H1 → H2 (FCR-2)**:
- [ ] Test coverage >70%
- [ ] Reproducibility verified
- [ ] 2+ external validations

### H2 (9-24 months): Integration & Public Demos

- [ ] Cross-product integration
- [ ] Public demonstrations
- [ ] Third-party audits
- [ ] Regulatory engagement

---

## Compliance Framework

See [COMPLIANCE.md](../COMPLIANCE.md) for full details.

Key standards:
- **Aerospace**: ARP4754A, ARP4761, DO-178C, DO-254, S1000D
- **Space**: ECSS, NASA standards
- **Defense**: MIL-STD, DO-326A/356A
- **Quality**: ISO 9001, AS9100
- **Ethics**: MAL-EEM framework

---

## CI/CD Pipeline

Automated workflows:
- **evidence_validation.yml**: Validates specs, structure, evidence format
- **structure-guard.yml**: Enforces directory structure
- **static.yml**: Static analysis
- Other product-specific workflows

---

## Getting Started

### For Contributors

1. **Clone repository**:
   ```bash
   git clone https://github.com/Robbbo-T/ASI-T2.git
   cd ASI-T2
   ```

2. **Review structure**:
   ```bash
   tree -L 2 MAL/ INFRA/ PRODUCTS/
   ```

3. **Read key documents**:
   - `README.md` - Main overview
   - `COMPLIANCE.md` - Standards framework
   - `HALL-OF-RECORDS/CLAIM.md` - Master claim
   - Product specs in `PRODUCTS/*/spec/*.yaml`

4. **Generate evidence** (for releases):
   ```bash
   ./scripts/make_evidence.sh v0.1.0
   ```

### For Auditors

1. **Verify structure**:
   ```bash
   python scripts/verify_structure.py
   ```

2. **Check signatures**:
   ```bash
   git tag -v v0.1.0
   ```

3. **Review evidence**:
   ```bash
   cd HALL-OF-RECORDS/horizons/H0/
   # Review product evidence
   ```

4. **Verify UTCS anchors**:
   ```bash
   cat evidence/utcs_anchor.json
   ```

---

## Key Files

| File | Purpose |
|------|---------|
| `CITATION.cff` | Citation metadata for academic use |
| `RELEASE.md` | Release notes and version history |
| `COMPLIANCE.md` | Compliance and standards framework |
| `HALL-OF-RECORDS/CLAIM.md` | Master claim document |
| `MAL/README.md` | MAL architecture |
| `INFRA/README.md` | Infrastructure planes |
| `scripts/make_evidence.sh` | Evidence generation script |

---

## Contact

- **Repository**: https://github.com/Robbbo-T/ASI-T2
- **Issues**: https://github.com/Robbbo-T/ASI-T2/issues
- **Author**: Amedeo Pelliccia (Robbbo-T)

---

**Last Updated**: 2025-01-01  
**Version**: 0.1.0  
**Status**: H0 Foundation Phase
