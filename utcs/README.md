---
id: ASIT2-UTCS-ROOT
project: ASI-T2
artifact: utcs/README.md
llc: GOVERNANCE
classification: PUBLIC
version: 0.1.0
release_date: "2025-10-03"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# ASI-T2 Root UTCS Manifest

This directory contains the root-level UTCS (Universal Trust and Certification System) manifest for the ASI-T2 repository, establishing deterministic bundling for all repository artifacts.

## Purpose

The root UTCS manifest provides:

- **Deterministic bundling** - Canonical references to all repository documentation and artifacts
- **Context tracking** - Operational and governance metadata
- **Content integrity** - Funding, policy, and principle documentation
- **Traceability** - Complete provenance chain for all repository changes

## Manifest Structure

### `manifest.yaml`

The root manifest organizes repository artifacts into six UTCS categories:

#### Context
Operational and governance metadata:
- `README.md` - Repository master README
- `CITATION.cff` - Citation metadata

#### Content
Policy and documentation:
- `FINANCE/SPONSORSHIP.md` - Sponsorship and funding policy (IDEALE-EU, MAL-EEM)
- `FINANCE/README.md` - Sustainable finance framework
- `FINANCE/PRINCIPLES.md` - Economic principles and mechanisms

#### Cache
Build artifacts and provenance (TBD)

#### Structure
Architectural specifications (TBD)

#### Style
Design and presentation (TBD)

#### Sheet
Data models and schemas (TBD)

## UTCS Integration

The root manifest integrates with:
- **Product-level UTCS** - Domain-specific evidence packages (BWB-Q100, GAIA, etc.)
- **CI/CD Pipeline** - Automated validation and evidence generation
- **Governance** - Policy and ethics compliance tracking
- **Funding** - Sponsorship and transparency documentation

## Usage

Access manifest content:
```bash
# View manifest structure
cat utcs/manifest.yaml

# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('utcs/manifest.yaml'))"

# Check funding documentation
cat FINANCE/SPONSORSHIP.md
```

## Standards

The root UTCS manifest complies with:
- **UTCS v5.0** - Universal Trust and Certification System standards
- **IDEALE-EU** - Intelligence, Defense, Energy, Aerospace, Logistics framework
- **MAL-EEM** - Ethics guard for non-weaponisation and decision logging
- **TFA Architecture** - Bridge pattern (QS→FWD→UE→FE→CB→QB)

## Related Documentation

- [FINANCE/SPONSORSHIP.md](../FINANCE/SPONSORSHIP.md) - Sponsorship policy
- [FINANCE/README.md](../FINANCE/README.md) - Financial framework
- [README.md](../README.md) - Repository master README

---

*Root UTCS manifest for ASI-T2 repository governance and traceability*
