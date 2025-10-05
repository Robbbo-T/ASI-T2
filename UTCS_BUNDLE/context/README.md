# Context

This directory contains narrative documents, whitepapers, and overview documentation for the UTCS v5.0 bundle.

## Purpose

The **Context** section of the UiX Threading model stores:
- Whitepapers and technical specifications
- Narrative documentation
- Overview documents
- Background and rationale
- System architecture descriptions

## Contents

**Note:** The canonical whitepapers are maintained in the repository's [WHITEPAPERS/](../../WHITEPAPERS/) directory. This context directory contains references and may have local snapshots for bundling purposes.

### Master Whitepaper #1: TFA V2 Architecture

**Canonical Location:** [../../WHITEPAPERS/MASTER_WHITEPAPER_1.md](../../WHITEPAPERS/MASTER_WHITEPAPER_1.md)

Foundational document describing the ASI-T2 ecosystem architecture:

- System-of-systems overview (AMPEL360, GAIA SPACE, etc.)
- TFA V2 bridge flow (QS→FWD→UE→FE→CB→QB)
- ATA/S1000D path grammar
- CAx/QOx/PAx package definitions
- MAL (Master Application Layer) specification
- FCR-1/FCR-2 gate requirements

**Key Topics:**
- Bridge layer definitions
- Path validation rules
- Evidence requirements
- Ethical governance (MAL-EEM)

### Master Whitepaper #3: QS/UTCS Provenance & Evidence Framework

**Canonical Location:** [../../WHITEPAPERS/MASTER_WHITEPAPER_3_UTCS.md](../../WHITEPAPERS/MASTER_WHITEPAPER_3_UTCS.md)

Complete UTCS v5.0 specification:

- UiX Threading model (Context/Content/Cache & Structure/Style/Sheet)
- Bundle layout and manifest schema
- Evidence plane and lifecycle
- Cryptography and policy requirements
- TFA bridge mappings
- S1000D/ATA crosswalks
- Validation and CI requirements
- IDEALE-EU alignment
- Ethics and compliance guidance

**Key Topics:**
- Deterministic bundling
- Hash-stable releases
- Evidence hooks
- MAL-EEM/MAP-EEM policy enforcement
- H0/H1/H2 roadmap

## UiX Threading Model

The **Context** is part of the **Threading** (input) layer in UTCS v5.0:

```
Threading (Input):
  - Context  — narrative documents  ← YOU ARE HERE
  - Content  — schemas, code
  - Cache    — examples, test data

Binding (Output):
  - Structure — grammar, mappings
  - Style     — formatting, legal
  - Sheet     — build, CI
```

## Adding Documents

When adding new context documents:

1. **Format:** Use Markdown (.md) for consistency
2. **Front Matter:** Include YAML front matter with:
   - `id`: Unique document identifier
   - `project`: ASI-T2
   - `version`: Semantic version
   - `author`: Document author
   - `release_date`: ISO 8601 date

3. **Structure:** Follow the pattern:
   ```markdown
   ---
   id: ASIT2-DOC-ID
   project: ASI-T2
   version: X.Y.Z
   ---
   
   # Document Title
   
   ## Executive Summary
   ...
   ```

4. **References:** Update manifest.utcs.yaml `uix.context` section

## Integration

These documents are self-contained within the bundle, enabling:
- Offline review and validation
- Complete provenance trail
- Reproducible evidence
- Auditable documentation lineage

## References

- [Canonical Whitepapers](../../WHITEPAPERS/) — Repository's authoritative whitepaper collection
- [Master Whitepaper #3](../../WHITEPAPERS/MASTER_WHITEPAPER_3_UTCS.md) — §1 Conceptual Model
- [Bundle README](../README.md) — Quick start guide
- [Manifest](../manifest.utcs.yaml) — See `uix.context` section
