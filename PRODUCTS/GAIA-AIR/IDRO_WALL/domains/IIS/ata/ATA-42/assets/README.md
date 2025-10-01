# ATA-42 Assets

This directory contains visual assets and diagrams for the ATA-42 Integrated Modular Avionics (IIS) documentation.

## Contents

### Diagrams

Located in `diagrams/` subdirectory. All diagrams are generated using Python with matplotlib in a blueprint-style technical visualization suitable for aerospace documentation.

| File | Description | Aspect Ratio |
|------|-------------|--------------|
| `ata42_ima_overview_v1.png` | IMA system overview showing chassis, partitions (SwarmCore, MAL-EEM, MissionPlanner, CMSAdapter), APEX ports/queues, health manager, and bridges to LCC/EDI/OOO | 16:9 |
| `ata42_repo_layout_v1.png` | Repository directory structure showing governance, os, manufacturing, sustainment, assets, scripts, and docs folders | 16:9 |
| `ata42_apex_port_map_v1.png` | Matrix-style diagram listing partitions vs APEX ports with direction (SRC/DST) and type (Sampling/Queueing) | 16:9 |
| `ata42_a653_schedule_v1.png` | ARINC-653 schedule timeline (0–100 ms) with windows for MAL-EEM, SwarmCore, and MissionPlanner, plus resource budgets | 16:9 |
| `ata42_compliance_matrix_v1.png` | Compliance matrix mapping artefacts to DO-178C/DO-297 and DO-326A/356A objectives | 16:9 |

## Generation

These diagrams are automatically generated from COPILOT:IMAGE placeholders in the parent README.md file.

### Regeneration

To regenerate all diagrams, run:

```bash
python3 scripts/generate_ata42_diagrams.py PRODUCTS/GAIA-AIR/IDRO_WALL/domains/IIS/ata/ATA-42/README.md
```

The script:
1. Parses COPILOT:IMAGE placeholders from the README
2. Generates blueprint-style technical diagrams with exact partition and interface names
3. Saves images to the paths specified in the placeholders' `save_to` fields
4. Uses consistent monochrome blueprint color scheme (#0d1b2a background, #e0e1dd foreground)

## Design Standards

- **Style**: Blueprint/technical drawing aesthetic
- **Colors**: Monochrome with blue/grey palette
- **Resolution**: 2400 x 1350 pixels (150 DPI)
- **Format**: PNG with RGBA
- **Aspect Ratio**: 16:9 (suitable for presentations)

## Usage in Documentation

Images are referenced in the parent README.md file at the locations of the COPILOT:IMAGE placeholders.

Example:
```markdown
![ATA-42 IMA Overview](assets/diagrams/ata42_ima_overview_v1.png)
```

## Compliance

These visualizations support the ATA-42 IMA architecture documentation and are maintained as part of the IIS (Information & Intelligence Systems) evidence package. The diagrams accurately reflect:

- Partition configurations (IIS.SwarmCore, IIS.MAL-EEM, IIS.MissionPlanner, IIS.CMSAdapter)
- APEX port interfaces and types
- ARINC-653 schedule and resource budgets
- Compliance mappings to DO-178C/DO-297 and DO-326A/356A standards

---

**Last Updated**: 2025-10-01  
**Maintainer**: ASI-T Architecture Team  
**Related Document**: [ATA-42 README](../README.md)
