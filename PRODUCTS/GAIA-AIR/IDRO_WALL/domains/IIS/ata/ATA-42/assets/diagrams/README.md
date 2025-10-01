# Diagrams

Technical diagrams and visualizations for ATA-42 IMA system.

## Generated Diagrams

Diagrams are generated from COPILOT:IMAGE placeholders in documentation:

### System Architecture
- `ata42_ima_overview_v1.png` — Complete IMA system with partitions, APEX ports, bridges
- `ata42_apex_port_map_v1.png` — Matrix of partitions and APEX ports with directions
- `ata42_a653_schedule_v1.png` — Timeline showing partition windows in major frame

### Repository Structure
- `ata42_repo_layout_v1.png` — Directory tree showing folder organization

### Compliance
- `ata42_compliance_matrix_v1.png` — Mapping of artifacts to DO-178C/DO-297/DO-326A objectives

## Style Guide

All diagrams follow consistent style:
- **Format:** PNG or SVG
- **Style:** Monochrome, blueprint/technical
- **Aspect ratio:** 16:9
- **Versioning:** v1, v2, etc. suffix for revisions

## Updating Diagrams

1. Update specification in source documentation (README.md)
2. Regenerate diagram from COPILOT:IMAGE specification
3. Increment version number if significant changes
4. Update references in documentation
5. Commit updated diagram with descriptive message

## Source Files

Where applicable, maintain source files (e.g., .drawio, .svg) alongside PNG exports for future editing.
