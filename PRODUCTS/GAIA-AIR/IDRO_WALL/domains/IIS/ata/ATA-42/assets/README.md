### ✅ Versión unificada (pega esto en tu `README.md` del directorio `assets`/`ATA-42` o donde corresponda)

````markdown
# ATA-42 Assets

Diagrams, images, and visual artifacts for the **ATA-42 Integrated Modular Avionics (IIS)** documentation.

## Structure

- **diagrams/** — Technical diagrams and system visualizations (generated)
- (optional) **sources/** — Diagram sources / specs (if maintained separately)

## Contents

### Diagrams (generated)

All diagrams are generated using Python (matplotlib) with a blueprint-style technical aesthetic suitable for aerospace documentation.

| File                         | Description                                                                                                             | Aspect Ratio |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------|
| `ata42_ima_overview_v1.png` | IMA system overview showing chassis, partitions (SwarmCore, MAL-EEM, MissionPlanner, CMSAdapter), APEX ports/queues, health manager, and bridges to LCC/EDI/OOO | 16:9 |
| `ata42_repo_layout_v1.png`  | Repository directory structure showing governance, OS, manufacturing, sustainment, assets, scripts, and docs folders     | 16:9 |
| `ata42_apex_port_map_v1.png`| Matrix-style diagram listing partitions vs APEX ports with direction (SRC/DST) and type (Sampling/Queueing)             | 16:9 |
| `ata42_a653_schedule_v1.png`| ARINC-653 schedule timeline (0–100 ms) with windows for MAL-EEM, SwarmCore, and MissionPlanner, plus resource budgets   | 16:9 |
| `ata42_compliance_matrix_v1.png` | Compliance matrix mapping artefacts to DO-178C/DO-297 and DO-326A/356A objectives                                | 16:9 |

## Generation

Many diagrams are generated from `COPILOT:IMAGE` placeholders in the parent **README.md**.

### Regeneration

```bash
python3 scripts/generate_ata42_diagrams.py PRODUCTS/GAIA-AIR/IDRO_WALL/domains/IIS/ata/ATA-42/README.md
````

The script:

1. Parses **COPILOT:IMAGE** placeholders from the README
2. Generates blueprint-style technical diagrams with exact partition and interface names
3. Saves images to the paths specified in the placeholders' `save_to` fields
4. Uses a consistent monochrome blueprint color scheme (#0d1b2a background, #e0e1dd foreground)

## Design Standards

* **Style:** Blueprint / technical drawing aesthetic
* **Colors:** Monochrome blue/grey palette
* **Resolution:** 2400 × 1350 px (150 DPI)
* **Format:** PNG (RGBA)
* **Aspect Ratio:** 16:9 (presentation-ready)

## Diagram Types (reference)

* **System Diagrams**

  * `ata42_ima_overview_v1.png` — IMA system overview
  * `ata42_apex_port_map_v1.png` — APEX port connectivity
  * `ata42_a653_schedule_v1.png` — ARINC-653 schedule
* **Repository Diagrams**

  * `ata42_repo_layout_v1.png` — Directory structure
* **Compliance Diagrams**

  * `ata42_compliance_matrix_v1.png` — Standards mapping

## Usage in Documentation

Images are referenced from:

* Parent **README.md** (via `![...](assets/diagrams/...)`)
* Technical documentation and S1000D data modules
* Presentations and reports

Example:

```markdown
![ATA-42 IMA Overview](assets/diagrams/ata42_ima_overview_v1.png)
```

## Maintenance

* Keep diagrams synchronized with configuration changes
* Bump version suffix (`_v1`, `_v2`, …) for significant changes
* Maintain source files where applicable
* Ensure consistent naming conventions

## Compliance

These visualizations support the ATA-42 IMA architecture documentation and are maintained as part of the **IIS (Information & Intelligence Systems)** evidence package. The diagrams reflect:

* Partition configurations (IIS.SwarmCore, IIS.MAL-EEM, IIS.MissionPlanner, IIS.CMSAdapter)
* APEX port interfaces and types
* ARINC-653 schedule and resource budgets
* Compliance mappings to DO-178C/DO-297 and DO-326A/356A standards

---

**Last Updated:** 2025-10-01
**Maintainer:** ASI-T Architecture Team
**Related Document:** [ATA-42 README](../README.md)
