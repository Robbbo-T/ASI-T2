# ASI-T2 Release Notes

This document tracks major releases and milestones for the ASI-T2 ecosystem.

---

## Release Strategy

ASI-T2 follows a **horizon-based release strategy** aligned with the master plan:

- **H0 (0-90 days)**: MVP releases with basic demos (v0.x.x)
- **H1 (3-9 months)**: Validated releases with HIL/external validation (v1.x.x)
- **H2 (9-24 months)**: Integrated releases with cross-product validation (v2.x.x)

Each release includes:
- ✅ Signed Git tag
- ✅ SBOM (Software Bill of Materials)
- ✅ UTCS anchor with canonical hash
- ✅ Release manifest
- ✅ Demo artifacts (when applicable)

---

## Upcoming Releases

### v0.1.0 — H0 Gate (Target: Q1 2025)

**Theme**: Foundation MVPs - First demonstrations of all core products

#### Products

**AMPEL360 BWB**
- [ ] SIL (Software-in-Loop) gemelo digital
- [ ] Control básico + aerodinámica inicial
- [ ] Telemetría básica
- [ ] Demo video

**GAIA SPACE**
- [ ] Simulador de órbitas
- [ ] Perfiles de misión básicos
- [ ] Integración con Data Plane
- [ ] Downlink simulado

**Defense Wall Swarm**
- [ ] Simulador multi-agente (10-20 nodos)
- [ ] Reglas de misión básicas
- [ ] Anti-colisión básica
- [ ] Demo de coordinación

**MAL v1.0**
- [ ] Drivers básicos
- [ ] Sistema de mensajería
- [ ] Telemetría
- [ ] Health monitoring
- [ ] Registry

**AMPEL360PLUS (Tourism)**
- [ ] Prototipo visual
- [ ] Cabin mockup
- [ ] Requisitos de seguridad lite

**H₂/LH₂ Airport**
- [ ] Modelo de capacidad
- [ ] Layouts conceptuales
- [ ] Análisis de riesgos inicial

**Finance Model**
- [ ] Whitepaper anti-especulación
- [ ] Spec económica
- [ ] Modelo de control de riesgos

#### Gate Criteria (FCR-1)
- [x] SBOM generado
- [x] Tests básicos
- [x] Video demos
- [x] RELEASE.md actualizado
- [x] Tag firmado
- [ ] DOI solicitado
- [x] UTCS anchor

---

## Past Releases

### v0.0.1 — Repository Foundation (2025-01-01)

**Initial Setup**
- ✅ Repository structure created
- ✅ MAL architecture defined
- ✅ Product specifications templates
- ✅ Evidence generation scripts
- ✅ HALL-OF-RECORDS with CLAIM.md
- ✅ CITATION.cff
- ✅ TFA methodology documented

**Infrastructure**
- ✅ `MAL/` directory structure
- ✅ `INFRA/` with 4 planes (Data, Control, Model, Evidence)
- ✅ `HALL-OF-RECORDS/` for provenance
- ✅ `FINANCE/` for economic model
- ✅ `AIRPORT_H2_LH2/` for infrastructure

**Documentation**
- ✅ Product specs: AMPEL360.yaml, GAIA_SPACE.yaml, DEFENSE_WALL_SWARM.yaml, AMPEL360PLUS.yaml
- ✅ MAL README with architecture
- ✅ Evidence scripts
- ✅ Claim documentation

---

## Version Numbering

ASI-T2 uses **Semantic Versioning** with horizon alignment:

```
MAJOR.MINOR.PATCH

MAJOR = Horizon number (0=H0, 1=H1, 2=H2)
MINOR = Feature releases within horizon
PATCH = Bug fixes and minor updates
```

Examples:
- `v0.1.0` — H0 first feature release
- `v0.2.0` — H0 second feature release
- `v1.0.0` — H1 first release (HIL validated)
- `v2.0.0` — H2 first release (integrated)

---

## Release Process

### 1. Prepare Release

```bash
# Update version in relevant files
# Update CHANGELOG.md
# Update this RELEASE.md
```

### 2. Generate Evidence

```bash
./scripts/make_evidence.sh v0.1.0
```

### 3. Review Artifacts

```bash
ls -la evidence/
git tag -v v0.1.0
cat evidence/utcs_anchor.json
```

### 4. Push Release

```bash
git push origin v0.1.0
# Create GitHub release
# Upload artifacts
```

### 5. Register DOI (Optional)

For major releases, register a DOI via:
- Zenodo
- Figshare
- Institutional repository

---

## Changelog

Detailed changes for each release are tracked in `CHANGELOG.md`.

---

## Evidence Archives

All release artifacts are stored in:
- Git tags: `git tag -l`
- Evidence directory: `evidence/`
- GitHub Releases: https://github.com/Robbbo-T/ASI-T2/releases

---

## Contact

For questions about releases:
- GitHub Issues: https://github.com/Robbbo-T/ASI-T2/issues
- GitHub Discussions: https://github.com/Robbbo-T/ASI-T2/discussions

---

**Last Updated**: 2025-01-01  
**Next Review**: H0 Gate (v0.1.0)
