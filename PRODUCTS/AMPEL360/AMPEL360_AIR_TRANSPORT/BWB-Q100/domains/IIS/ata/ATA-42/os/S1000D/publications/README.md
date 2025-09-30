# S1000D Publications (Markdown)

This directory contains generated publications in Markdown format for easy viewing on GitHub.

## Publications

| Publication | Description | Source DMs | File |
|-------------|-------------|------------|------|
| General Manual | Overview of IMA OS | DMC-42-00, DMC-42-10 | [PUB-A42-OS-GEN-00000-00.md](./PUB-A42-OS-GEN-00000-00.md) |
| Design Specification | Detailed design information | DMC-42-11, DMC-42-12, DMC-42-20 | [PUB-A42-OS-DES-00000-00.md](./PUB-A42-OS-DES-00000-00.md) |
| Test Documentation | Test procedures and results | DMC-42-30, DMC-42-40 | [PUB-A42-OS-TST-00000-00.md](./PUB-A42-OS-TST-00000-00.md) |

## Assets

The `assets/` directory contains technical diagrams and visualizations supporting the publications:

- **12 Technical Diagrams** for Test Documentation (PUB-A42-OS-TST-00000-00.md)
  - Verification V-model, test bench wiring, boot timeline, partition maps
  - Performance metrics, coverage heatmaps, traceability matrices
  - Professional blueprint color scheme (150 DPI PNG format)
- See [assets/README.md](./assets/README.md) for detailed image catalog and specifications

## Generation Process

Publications are generated from S1000D data modules:

1. Extract content from XML DMs
2. Convert to Markdown format
3. Add GitHub-compatible formatting
4. Include hyperlinks to source DMs
5. Validate against BREX rules

## Benefits

- **GitHub-Native**: Viewable directly on GitHub
- **Searchable**: Full-text search enabled
- **Hyperlinked**: Cross-references to source data
- **Version Controlled**: Complete change history

## Validation

```bash
# Check all Markdown files
markdownlint *.md

# Verify links to source DMs
grep -r "DMC-Q100-A-42" . --include="*.md"
```

## Related Documents

- [Source Data Modules](../dmodule/)
- [Main README](../../README.md)
