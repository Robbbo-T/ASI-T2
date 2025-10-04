# Style

This directory contains citation styles, formatting rules, and legal notices for the UTCS v5.0 bundle.

## Purpose

The **Style** section of the UiX Threading model stores:
- Citation styles (CSL)
- Legal notices and disclaimers
- License information
- Formatting rules and lints
- Attribution requirements

## Contents

### Citation Style

**File:** `citation.csl`

**Format:** Citation Style Language (CSL) XML

Custom citation style for ASI-T2 UTCS bundles and technical documentation:

- **Format:** Numeric citation style
- **Category:** Engineering field
- **Features:**
  - Author name sorting (last, first)
  - Italicized book titles
  - Quoted article titles
  - DOI inclusion when available
  - ISO 8601 dates

**Usage:**

Reference managers and citation tools (Zotero, Mendeley, Pandoc) can use this style for consistent citations.

**Example Output:**

```
[1] Pelliccia, A. QS/UTCS Provenance & Evidence Framework. v0.1.0. 2025. DOI: TBA.
```

### Legal Notice

**File:** `NOTICE`

Comprehensive legal and ethical notice covering:

- **Copyright:** Bundle ownership and attribution
- **Ethics & Responsible Use:** Weaponization prohibitions, MAL-EEM/MAP-EEM controls
- **Compliance:** EU 2021/821, ITAR/EAR, AS9100-lite, privacy/security requirements
- **Attribution:** Citation requirements
- **Third-Party Components:** SBOM reference
- **Contact:** Repository and maintainer information
- **Disclaimer:** Liability limitations

**Key Requirements:**

1. **Ethics:** MUST NOT be used to facilitate weaponization
2. **Attribution:** Must cite when using in research or commercial applications
3. **Dual-Use:** Controlled under MAL-EEM/MAP-EEM
4. **Decision Logging:** Immutable records required

### License

**Status:** Proprietary with Responsible Use clause

**Details:** See `NOTICE` file for complete license terms and responsible use requirements.

## UiX Threading Model

The **Style** is part of the **Binding** (output) layer in UTCS v5.0:

```
Threading (Input):
  - Context  — narrative documents
  - Content  — schemas, code
  - Cache    — examples, test data

Binding (Output):
  - Structure — grammar, mappings
  - Style     — formatting, legal  ← YOU ARE HERE
  - Sheet     — build, CI
```

## Citation

To cite this bundle or the UTCS framework:

**Plain Text:**

> Pelliccia, A. (2025). *QS/UTCS Provenance & Evidence Framework*. v0.1.0. DOI: TBA.

**BibTeX:**

```bibtex
@techreport{pelliccia2025utcs,
  author = {Pelliccia, Amedeo},
  title = {QS/UTCS Provenance \& Evidence Framework},
  institution = {ASI-T Architecture Team},
  year = {2025},
  version = {0.1.0},
  doi = {TBA},
  url = {https://github.com/Robbbo-T/ASI-T2}
}
```

**Machine-Readable:** See `/CITATION.cff` in repository root

## Adding Style Files

When adding new style files:

1. **Citation Styles:** Use CSL format, follow existing pattern
2. **Legal Notices:** Update for program-specific requirements
3. **Formatting Rules:** Document linting and style requirements
4. **Update Manifest:** Add to `uix.style` section in `manifest.utcs.yaml`

## References

- [Master Whitepaper #3](../context/MASTER_WHITEPAPER_3_UTCS.md) — §10 Ethics & Compliance, §11 How to Cite
- [Bundle README](../README.md) — Quick start guide
- [Manifest](../manifest.utcs.yaml) — See `uix.style` section
- [CITATION.cff](/CITATION.cff) — Repository citation metadata
- [CSL Specification](https://citationstyles.org/) — Citation Style Language standard
