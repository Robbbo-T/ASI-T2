# ASI-T2 Quick Reference Guide

Fast reference for common operations and key information.

---

## Quick Start

### Clone Repository
```bash
git clone https://github.com/Robbbo-T/ASI-T2.git
cd ASI-T2
```

### Directory Structure
```
MAL/              → Master Application Layer (common services)
INFRA/            → 4 operational planes (Data, Control, Model, Evidence)
PRODUCTS/         → Product portfolio (AMPEL360, GAIA, Swarm, etc.)
HALL-OF-RECORDS/  → Provenance and evidence archive
FINANCE/          → Sustainable finance model
AIRPORT_H2_LH2/   → H₂/LH₂ infrastructure
```

---

## Key Documents

| Document | Description |
|----------|-------------|
| `README.md` | Main repository overview |
| `MASTER_PLAN_STRUCTURE.md` | Complete directory structure guide |
| `COMPLIANCE.md` | Standards and compliance framework |
| `RELEASE.md` | Release notes and roadmap |
| `HALL-OF-RECORDS/CLAIM.md` | Master claim document |
| `CITATION.cff` | Citation metadata |

---

## Product Specifications

All products have specs in `PRODUCTS/*/spec/*.yaml`:

- **AMPEL360 BWB**: `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/spec/AMPEL360.yaml`
- **GAIA SPACE**: `PRODUCTS/GAIA-SPACE/spec/GAIA_SPACE.yaml`
- **Defense Swarm**: `PRODUCTS/GAIA-AIR/IDRO_WALL/spec/DEFENSE_WALL_SWARM.yaml`
- **AMPEL360PLUS**: `PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/spec/AMPEL360PLUS.yaml`

---

## Common Commands

### Generate Evidence
```bash
./scripts/make_evidence.sh v0.1.0
```

### Verify Structure
```bash
python scripts/verify_structure.py
```

### Check Git Status
```bash
git --no-pager status
```

### View Recent Commits
```bash
git --no-pager log --oneline -10
```

### Verify Tag Signature
```bash
git tag -v v0.1.0
```

---

## TFA Bridge Pattern

All products follow TFA (Top Federation Algorithm):

```
CB (Conceptual Boundary)
  → QB (Quantum Boundary)
    → UE (Unit Execution)
      → FE (Final Execution)
        → FWD (Forward Deployment)
          → QS (Quantum Seal)
```

Every artifact traces through this pipeline.

---

## MAL Components

**MAL** = Master Application Layer (PLC de dominio)

| Component | Purpose |
|-----------|---------|
| `drivers/` | Hardware abstraction and device drivers |
| `messaging/` | Pub-sub messaging system |
| `telemetry/` | Telemetry collection and streaming |
| `health/` | Health monitoring and watchdogs |
| `registry/` | Service discovery and configuration |

---

## INFRA Planes

| Plane | Purpose |
|-------|---------|
| **DATA-PLANE** | Ingestion, storage, analytics |
| **CONTROL-PLANE** | Mission orchestration, security, policies |
| **MODEL-PLANE** | Digital twins, SIL/HIL, V&V |
| **EVIDENCE-PLANE** | SBOMs, DOIs, attestations, UTCS |

---

## Horizons Roadmap

### H0 (0-90 days): MVPs
- Basic SIL demos
- Product specs complete
- Evidence framework

### H1 (3-9 months): Validation
- HIL testing
- External reviews
- Safety cases

### H2 (9-24 months): Integration
- Cross-product integration
- Public demos
- Regulatory engagement

---

## Key Standards

**Aerospace**: ARP4754A, ARP4761, DO-178C, DO-254, S1000D  
**Space**: ECSS, NASA standards  
**Defense**: MIL-STD, DO-326A/356A  
**Ethics**: MAL-EEM framework  
**Traceability**: UTCS v5.0

---

## MAL-EEM Guardrails

Ethics & Empathy Module ensures:
- ✅ Fail-closed by default
- ✅ Human oversight required
- ✅ Mission rules validation
- ✅ Safety constraints enforcement
- ✅ Emergency override available

---

## UTCS v5.0

Universal Traceability & Configuration System:
- Canonical hash (SHA-256)
- Immutable timestamp
- Provenance chain
- Signature verification
- Evidence anchoring

---

## Evidence Generation Workflow

1. Make changes
2. Test changes
3. Run `./scripts/make_evidence.sh vX.Y.Z`
4. Review generated artifacts in `evidence/`
5. Push tag: `git push origin vX.Y.Z`
6. Update `RELEASE.md`
7. Register DOI (if major release)

---

## File Naming Conventions

### Product Specs
`spec/PRODUCT_NAME.yaml`

### Evidence
`evidence/demos/DEMO_NAME/`

### UTCS Anchors
`evidence/utcs_anchor.json`

### SBOM
`evidence/sbom.spdx.json`

---

## Git Workflow

### Branch Naming
- `main` - Stable releases
- `develop` - Integration branch
- `feature/name` - Feature branches
- `fix/name` - Bug fix branches

### Commit Messages
```
<type>: <short description>

<longer description if needed>

Co-authored-by: Name <email>
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

---

## CI/CD Workflows

Located in `.github/workflows/`:

- `evidence_validation.yml` - Validate specs and evidence
- `structure-guard.yml` - Enforce directory structure
- `static.yml` - Static analysis
- Others for specific products

---

## Contact & Support

- **Repository**: https://github.com/Robbbo-T/ASI-T2
- **Issues**: https://github.com/Robbbo-T/ASI-T2/issues
- **Discussions**: https://github.com/Robbbo-T/ASI-T2/discussions

---

## Quick Troubleshooting

### Evidence script fails
- Check Python3 installed: `python3 --version`
- Check for GPG key (optional): `gpg --list-keys`
- Install syft for full SBOM: https://github.com/anchore/syft

### CI failing
- Check file paths are correct
- Validate YAML syntax
- Ensure required fields in specs
- Check TFA bridge format

### Can't find product spec
- Look in `PRODUCTS/*/spec/*.yaml`
- Check MASTER_PLAN_STRUCTURE.md for complete map

---

**Last Updated**: 2025-01-01  
**Version**: 0.1.0
