---
id: INFRANET-TEMPLATES-README
project: ASI-T2
artifact: Shared Templates Directory
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 1.0.0
release_date: "2025-10-01"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# Shared Templates

This directory contains standardized templates for the ASI-T2 repository, ensuring consistency across all products, domains, and artifacts.

## Available Templates

### 1. artifact.manifest.yaml

**Purpose:** UTCS-MI v5.0 compliant manifest template for computational artifacts

**Usage:** Required for all CAX, QOX, and PAX artifacts to ensure traceability

**Fields:**
- `id`: UTCS-MI identifier following the pattern `UTCS-MI:v5.0:<PRODUCT>:<CAX|QOX|PAX>:<DOMAIN>:<ATA>:<artifact-id>`
- `llc`: Lifecycle classification (typically SYSTEMS)
- `bridge`: Evidence bridge chain (CB→QB→UE→FE→FWD→QS)
- `source`: Repository path and commit information
- `inputs`: List of input artifacts
- `outputs`: List of output artifacts with types
- `evidence`: ATA data module references
- `provenance`: SBOM and QS signatures
- `ethics_guard`: MAL-EEM confirmation

**Documentation:** See main [README.md](../../../../README.md) "Mandatory Traceability" section

**Example usage:**
```bash
# Copy template to your artifact directory
cp PRODUCTS/INFRANET/Shared/_templates/artifact.manifest.yaml \
   PRODUCTS/<PRODUCT>/<PATH>/artifact.manifest.yaml

# Fill in all <...> placeholders
# Ensure SBOM is generated
# Validate with CI before publishing
```

### 2. ata_chapter_template.md

**Purpose:** Standardized template for ATA chapter documentation

**Usage:** Use when creating new ATA chapter documentation in `domains/<CODE>/ata/ATA-XX/`

**Features:**
- S1000D-compatible structure
- UTCS/QS evidence integration points
- CS-25 compliance matrices
- Hazard log references (ARP4761)

### 3. qox_problem_template.json

**Purpose:** Template for quantum optimization problem definitions

**Usage:** Use when encoding CAX problems to QOX in `domains/<CODE>/qox/<PHASE>/problems/`

**Features:**
- QUBO/BQM problem specification
- Variable definitions
- Objective function
- Constraints
- Solver configuration

## Integration Points

All templates are integrated with:
- CI/CD validation pipelines (`.github/workflows/`)
- Structure verification scripts (`scripts/verify_structure.py`)
- UTCS/QS evidence system
- MAL-EEM ethics gates

## Template Maintenance

**Update policy:**
- Templates follow semantic versioning
- Breaking changes require repository-wide migration
- Template version is tracked in UTCS canonical_hash
- Changes must pass all CI validation gates

## Related Documentation

- [Main README](../../../../README.md) — Repository master documentation
- [Product Architecture](../../../../README.md#product-architecture-domain--process--ata) — Domain structure
- [Mandatory Traceability](../../../../README.md#mandatory-traceability) — Evidence requirements
- [PAx Standards](../../../../README.md#pax--packaging--applications) — Packaging guidelines

---

*Part of IDEALE — Intelligence · Defense · Energy/Ecology · Aerospace · Logistics · Europe*
