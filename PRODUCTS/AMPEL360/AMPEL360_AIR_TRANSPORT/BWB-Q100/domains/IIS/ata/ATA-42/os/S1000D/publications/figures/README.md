# ATA-42 OS Publication Figures

This directory contains generated figures for the ATA-42 OS General Manual publication.

## Contents

All figures are generated from text descriptions in the publication markdown file. They use a blueprint-style technical diagram aesthetic consistent with aerospace documentation standards.

### Generated Figures

1. `fig-01-platform-stack.png` - AQUA-OS platform stack overview
2. `fig-02-context-diagram.png` - Aircraft systems context diagram  
3. `fig-03-architecture-layers.png` - Layered architecture diagram
4. `fig-04-design-principles.png` - Design principles tile grid
5. `fig-05-scheduling-timeline.png` - Major/minor frame timeline
6. `fig-06-memory-map.png` - Address space schematic
7. `fig-07-hm-concept.png` - Health monitoring concept view
8. `fig-08.png` - Sampling vs Queuing comparison
9. `fig-09.png` - I/O virtualization overview
10. `fig-10.png` - Boot flow state machine
11. `fig-11.png` - Annotated schedule example
12. `fig-12.png` - Overrun handling sequence
13. `fig-13.png` - Sampling port timing chart
14. `fig-14.png` - Queuing port behavior
15. `fig-15.png` - Time synchronization topology
16. `fig-16.png` - AFDX mapping view
17. `fig-17.png` - ARINC 429 bus map
18. `fig-18.png` - HM escalation ladder
19. `fig-19.png` - Configuration integrity chain
20. `fig-20.png` - Compliance matrix heatmap
21. `fig-21.png` - Traceability chain
22. `fig-22.png` - Glossary acronym wall

## Generation

Figures are automatically generated using the `generate_figures.py` script from text descriptions embedded in the markdown publication file.

### Regenerating Figures

To regenerate all figures:

```bash
python3 scripts/generate_publication_figures.py \
  PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-42/os/S1000D/publications/PUB-A42-OS-GEN-00000-00.md
```

## Style Guide

All figures use a consistent blueprint aesthetic:
- **Background**: Dark navy blue (#0d1b2a)
- **Foreground**: Off-white (#e0e1dd)
- **Accent**: Gray-blue (#778da9)
- **Highlight**: Blue-gray (#415a77)

This palette is optimized for technical documentation and maintains readability in both digital and print formats.

## Dependencies

Figure generation requires:
- Python 3.8+
- matplotlib
- pillow (PIL)

## Related Documents

- [Parent Publication](../PUB-A42-OS-GEN-00000-00.md)
- [Source Data Modules](../dmodule/)
