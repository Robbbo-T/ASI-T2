# 2-DOMAINS-LEVELS — Canonical ATA Home

This directory contains the **canonical ATA chapter folders** organized by domain. Each canonical ATA is the **single source of truth** for that chapter's content.

## Structure

```
2-DOMAINS-LEVELS/
├── AAA/              # Airframe & Structures
│   └── ata/
│       ├── ATA-20/   # Standard Practices - Airframe
│       ├── ATA-51/   # Standard Practices - Structures
│       ├── ATA-52/   # Doors
│       ├── ATA-53/   # Fuselage
│       ├── ATA-54/   # Nacelles/Pylons
│       ├── ATA-55/   # Stabilizers
│       ├── ATA-56/   # Windows
│       └── ATA-57/   # Wings
├── CCC/              # Cabin & Cargo
│   └── ata/
│       ├── ATA-25/   # Equipment/Furnishings
│       └── ATA-44/   # Cabin Systems
├── EEE/              # Electrical & Environmental
│   └── ata/
│       ├── ATA-21/   # Air Conditioning
│       ├── ATA-24/   # Electrical Power
│       ├── ATA-26/   # Fire Protection
│       ├── ATA-30/   # Ice and Rain Protection
│       ├── ATA-33/   # Lights
│       ├── ATA-35/   # Oxygen
│       └── ATA-38/   # Water/Waste
├── IIF/              # Integrated Flight Systems
│   └── ata/
│       └── ATA-27/   # Flight Controls
├── IIS/              # Integrated Information Systems
│   └── ata/
│       ├── ATA-22/   # Auto Flight
│       ├── ATA-23/   # Communications
│       ├── ATA-31/   # Indicating/Recording Systems
│       ├── ATA-34/   # Navigation
│       ├── ATA-42/   # Integrated Modular Avionics
│       ├── ATA-45/   # Central Maintenance System
│       └── ATA-46/   # Information Systems
├── MMM/              # Mechanisms & Actuation
│   └── ata/
│       └── ATA-32/   # Landing Gear
├── OOO/              # Operations & Maintenance
│   └── ata/          # (shared ATAs only)
└── PPP/              # Propulsion & Power
    └── ata/
        ├── ATA-28/   # Fuel
        ├── ATA-29/   # Hydraulic Power
        ├── ATA-36/   # Pneumatic
        ├── ATA-49/   # Airborne Auxiliary Power
        ├── ATA-70/   # Standard Practices - Powerplant
        ├── ATA-71/   # Power Plant
        ├── ATA-72/   # Engine
        ├── ATA-73/   # Engine Fuel and Control
        ├── ATA-74/   # Ignition
        ├── ATA-75/   # Air
        ├── ATA-76/   # Engine Controls
        ├── ATA-77/   # Engine Indicating
        ├── ATA-78/   # Exhaust
        ├── ATA-79/   # Oil
        └── ATA-80/   # Starting
```

## Purpose

**Canonical ATA folders** serve as:

1. **Single Source of Truth** - Authoritative content for each ATA chapter
2. **Domain Ownership** - Clear responsibility and change control
3. **Reusability** - Products reference canonical via symlinks, no duplication
4. **Governance** - Formal change control, baselines, and traceability
5. **Compliance** - Standard structure for certification and audits

## Standard ATA Directory Structure

Each canonical ATA follows this structure (see `8-RESOURCES/ATA_CANONICAL/ATA_README_TEMPLATE.md`):

```
<DOMAIN>/ata/<ATA>/
├── README.md                     # Canonical home page
├── CONVENTIONS.md                # Domain/ATA-specific conventions
├── governance/
│   ├── change_control/           # PR policy, versioning, commits
│   ├── baselines/                # BL-0, BL-1..., signed hashes
│   ├── risk_management/          # FHA/FTA/FMEA, mitigations
│   ├── cross_references.yaml     # Cross-domain references
│   └── audits/                   # CAR/PAR records, evidence
├── os/                           # Operating System / Design
│   ├── S1000D/                   # DMRL, BREX, data modules
│   ├── design/                   # Architecture, ICDs, diagrams
│   ├── configuration/            # Manifests, schedule.xml
│   ├── testing/                  # Test plans, results, traces
│   └── compliance/               # Certification evidence
├── manufacturing/
│   ├── bom/                      # EBOM/MBOM
│   ├── process/                  # Routings, travelers
│   ├── quality/                  # Control plans, FAIRs
│   ├── tooling/                  # Jigs, fixtures
│   ├── test/                     # ATP/QTP
│   └── packaging/                # Handling, logistics
├── sustainment/
│   ├── service_mro/              # Maintenance plans
│   ├── spares/                   # Provisioning
│   ├── reliability/              # FRACAS, MTBF
│   ├── obsolescence/             # DMSMS, alternates
│   ├── cas_security/             # Continued airworthiness
│   └── recycling_disposal/       # WEEE/ROHS, data sanitization
├── assets/                       # Images, CGM, CAD exports
├── scripts/                      # Local automation
└── docs/                         # Design notes, whitepapers
```

## Creating a New Canonical ATA

Use the standardization script:

```bash
# Create canonical structure for ATA-42 in IIS domain
python scripts/standardize_ata_structure.py --atas ATA-42 --create

# Create with symlinks from products
python scripts/standardize_ata_structure.py --atas ATA-42 --create --symlinks

# Dry run to preview
python scripts/standardize_ata_structure.py --atas ATA-42 --create --dry-run --verbose
```

## Validation

Validate canonical structure and relationships:

```bash
# Validate specific ATA
python scripts/standardize_ata_structure.py --atas ATA-42 --validate

# List all canonical ATAs
python scripts/standardize_ata_structure.py --list

# Verify uniqueness (one canonical per ATA)
python scripts/verify_canonical_uniqueness.py

# Validate cross-references
python scripts/validate_cross_references.py --all

# Check compliance mappings
python scripts/map_compliance.py --ata ATA-42
```

## Product Integration

Products **must not duplicate** canonical content. Instead, use **relative symlinks**:

```bash
# Example: BWB-Q100 references IIS/ATA-42
cd PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/

# Create symlink to canonical (relative path)
ln -s ../../../../../../2-DOMAINS-LEVELS/IIS/ata/ATA-42 ATA-42

# Validate symlinks
python scripts/validate_symlinks.py
```

## Cross-Domain References

When an ATA is shared across domains or references another domain's ATA, document in `governance/cross_references.yaml`:

```yaml
xrefs:
  - from: 
      ata: ATA-42
      domain: IIS
    to:
      ata: ATA-45
      domain: IIS
    type: dependency
    reason: "IMA platform depends on CMS for health monitoring"
    status: active
```

Schema: `8-RESOURCES/ATA_CANONICAL/XREF_MASTER.yaml`

## Governance Model

### Change Control

1. **Baseline Management** - Tag releases: `<DOMAIN>-<ATA>-BL-<N>`
2. **Pull Requests** - All changes via PR with peer review
3. **Semantic Commits** - `feat(ata-XX):`, `fix(ata-XX):`, `docs(ata-XX):`
4. **UTCS Traceability** - All artifacts have UTCS metadata

### Evidence & QS

- Critical artifacts have **QS (Quantum Seal) hashes** in `governance/baselines/`
- Link evidence in `governance/audits/`
- SBOM in `os/configuration/manifests/`

### Compliance

- Inherit from `8-RESOURCES/ATA_CANONICAL/COMPLIANCE_MATRIX.yaml`
- Add per-ATA specifics in `os/compliance/`
- Map with: `python scripts/map_compliance.py --ata <ATA>`

## Domain Definitions

See `8-RESOURCES/ATA_CANONICAL/ATA_REGISTRY.yaml` for:
- ATA-to-Domain mappings
- Canonical domain ownership
- Shared domain relationships
- Domain descriptions

## Tools & Scripts

All located in `scripts/`:

- **standardize_ata_structure.py** - Create/validate canonical structure
- **validate_cross_references.py** - Validate cross_references.yaml
- **map_compliance.py** - Render compliance requirements
- **verify_canonical_uniqueness.py** - Ensure one canonical per ATA
- **validate_symlinks.py** - Validate product symlinks

## Resources

- [ATA Canonical Resources](../8-RESOURCES/ATA_CANONICAL/README.md)
- [Repository README](../README.md)
- ATA 100 Specification (industry standard)

## Examples

### ATA-42 (Integrated Modular Avionics - IIS)

Canonical: `2-DOMAINS-LEVELS/IIS/ata/ATA-42/`

Key compliance: DO-178C (DAL A), DO-254, DO-297, ARINC-653

Product reference:
```
PRODUCTS/.../IIS/ata/ATA-42 → ../../../../../../2-DOMAINS-LEVELS/IIS/ata/ATA-42
```

### ATA-32 (Landing Gear - MMM)

Canonical: `2-DOMAINS-LEVELS/MMM/ata/ATA-32/`

Key compliance: CS-25 Subpart D, maintenance task cards

Focus: EBOM/MBOM for gear/doors/actuation

### ATA-57 (Wings - AAA)

Canonical: `2-DOMAINS-LEVELS/AAA/ata/ATA-57/`

Key compliance: CS-25 structural certification

Focus: Structural design, loads, materials, manufacturing

---

**Note:** Empty canonical directories are not committed to Git. They're created on-demand by the standardization script or manually as needed.
