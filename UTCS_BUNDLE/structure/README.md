# Structure

This directory contains grammar definitions, mappings, and path validators for the UTCS v5.0 bundle.

## Purpose

The **Structure** section of the UiX Threading model stores:
- Directory grammar and path validation rules
- Topic and DMC mappings (crosswalks)
- Hierarchical structures
- Naming conventions
- Validation patterns

## Contents

### TFA Grammar

**File:** `tfa_grammar.md`

Defines the canonical TFA V2 path grammar following ATA/S1000D standards:

```
domains/<DOMAIN_CODE>/ATA-XX/<XX-XX>_<DESCRIPTION>/S1000D/<LAYER>/<PACK>/<SUBPACK>
```

**Key Elements:**

- **Domain Codes:** Three-letter codes (AAA, AAP, AAQ, ..., PPP)
- **ATA Chapters:** Standard aviation chapters (ATA-22, ATA-53, ATA-57, etc.)
- **TFA Layers:** QS, FWD, UE, FE, CB, QB
- **Packages:**
  - **CAx** — Computer-Aided X (CAD, CAE, CAM, CAT, CFD)
  - **QOx** — Quantum Optimizations (OPT, ANNEAL, QAOA, VQE, QUBO)
  - **PAx** — Packaging & Assemblies (**OB/OFF only**)

**Validation Rules:**

- Path pattern regex validation
- Subpackage constraints (PAx uses ONLY OB/OFF)
- ATA chapter alignment requirements
- CI gate enforcement (FCR-1/FCR-2)

**Usage:**

```bash
# Validate paths against grammar
python sheet/ci/validate_utcs.py --manifest manifest.utcs.yaml --check-crosswalk
```

### Topic Hierarchy

**File:** `topic_hierarchy.md`

Complete crosswalk mapping between three naming systems:

1. **MAP Topics** — ASI-T2 MAP contract topic paths
   - Format: `map/<major>/<contract>/<program>/<domain>/<component>/<stream>/<layer>`
   - Example: `map/1/log/BWB-Q100/AAA/STATES/QS/QS`

2. **TFA Paths** — Physical repository paths
   - Format: `domains/<DOMAIN>/ATA-XX/<SUBCHAPTER>/S1000D/<LAYER>/<PACK>/<SUBPACK>`
   - Example: `domains/AAA/ATA-57/57-10_Wing/S1000D/QS/PAx/OB/`

3. **S1000D DMCs** — Data Module Codes for structured documentation
   - Format: `DMC-<PROGRAM>-<DOMAIN>-<ATA>-<SUBATA>-<VARIANT>-<INFOCODE>-<LAYER><ITEM>-<TYPE>`
   - Example: `DMC-BWB-Q100-A-57-10-00-00A-QS0A-D`

**Coverage:**

- BWB-Q100 AAA domain (airframe, aerodynamics, avionics)
- GAIA-SAT AAP domain (space systems)
- All six TFA bridge layers (QS/FWD/UE/FE/CB/QB)

**Validation Requirements:**

- Topic coverage completeness
- Path validity per TFA grammar
- DMC format correctness
- Bidirectional mapping consistency

## UiX Threading Model

The **Structure** is part of the **Binding** (output) layer in UTCS v5.0:

```
Threading (Input):
  - Context  — narrative documents
  - Content  — schemas, code
  - Cache    — examples, test data

Binding (Output):
  - Structure — grammar, mappings  ← YOU ARE HERE
  - Style     — formatting, legal
  - Sheet     — build, CI
```

## Integration

Structure files are validated by:

```bash
# From sheet directory
cd UTCS_BUNDLE/sheet
make validate-full

# Or directly
python ci/validate_utcs.py --manifest ../manifest.utcs.yaml --check-crosswalk
```

## Adding Mappings

When adding new systems or components:

1. **Choose ATA chapter** for the component
2. **Select TFA layer** based on function (QS/FWD/UE/FE/CB/QB)
3. **Select pack** (CAx/QOx/PAx) and valid subpack
4. **Generate S1000D DMC** following naming convention
5. **Add entry** to `topic_hierarchy.md` crosswalk table
6. **Update manifest** `uix.structure` if adding new files
7. **Validate** with `make validate-full`

## References

- [Master Whitepaper #1](../context/MASTER_WHITEPAPER_1.md) — §3.2 Bridge Grammar
- [Master Whitepaper #3](../context/MASTER_WHITEPAPER_3_UTCS.md) — §4 Mappings
- [Bundle README](../README.md) — Quick start guide
- [Manifest](../manifest.utcs.yaml) — See `uix.structure` section
- [ATA Spec 2200](https://www.ata.org/resources/specifications) — ATA chapter definitions
- [S1000D](http://www.s1000d.org/) — International specification for technical publications
