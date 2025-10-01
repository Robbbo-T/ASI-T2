# Contracts & Schemas

This directory contains Interface Control Documents (ICDs) and JSON schemas that define data exchange contracts for ATA-57-10 Wing Primary Structure.

## Purpose

Provides:
- JSON schemas for structural data definitions
- Interface control documents for data exchange
- Validation contracts for artifacts
- Integration specifications with CAX/QOX/PAX domains

## Contents

- **ICD-AAA-ATA-57-10.md** — Main ICD for data exchange interfaces
- **schemas/** — JSON Schema files (Draft 2020-12)

## JSON Schemas

Five comprehensive schemas define data contracts:
- `acceptance.metric.schema.json` — Inspection acceptance criteria
- `attachment.fitting.schema.json` — Wing attach fitting specifications
- `fastener.set.schema.json` — Fastener specifications and parameters
- `joint.schema.json` — Structural joint definitions
- `laminate.stack.schema.json` — Composite laminate layup specifications

All schemas include:
- Semantic versioning
- Detailed property descriptions
- Required fields and validation rules
- Cross-references to related schemas

## Data Exchange Patterns

### ATA ↔ CAX
- Geometry inputs (OML, structural definitions)
- Analysis results (stress, margins, buckling)

### ATA ↔ QOX
- Optimization problem definitions (QUBO, BQM)
- Optimized solutions (fastener layouts, ply orientations)

### ATA ↔ PAX
- Package definitions (on-board, off-board)
- SBOM and digital signatures

## Validation

All JSON artifacts must validate against referenced schemas using:
- `jsonschema` (Python)
- `ajv` (JavaScript)

## Change Control

Schema changes require:
- Multi-domain review
- Semantic versioning updates
- Impact assessment

---

*Part of ATA-57-10 Wing Primary Structure — Configuration controlled under UTCS/QS v5.0*
