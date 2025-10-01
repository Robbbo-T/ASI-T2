# Illustrated Parts Data (IPD) - Wing Primary Structure

This directory contains S1000D Illustrated Parts Data modules (Info Code 941A) providing part identification, illustrated breakdowns, and item-level information for wing primary structure components.

## Purpose

IPD modules provide:
- Illustrated component breakdowns
- Part number identification
- Quantity and applicability information
- Assembly relationships
- Item location and reference codes
- Nomenclature and description
- Interchangeability and alternates

## Organization

IPD modules are organized by component:
- **57-10-10** Forward Spar
- **57-10-20** Rear Spar
- **57-10-30** Ribs
- **57-10-40** Skin Panels
- **57-10-50** Stringers
- **57-10-60** Attachments

## Information Code

All modules in this directory use:
- **941A** - Illustrated Parts Data information code
- Content type: **D** (Descriptive with illustrations)

## IPD Content

Each IPD module typically includes:
- Exploded view illustrations (ICN - Illustration Control Numbers)
- Item callout numbers on figures
- Part number tables with:
  - Item number
  - Part number (P/N)
  - Nomenclature/description
  - Quantity per assembly
  - Unit of measure
  - Effectivity (MSN ranges, options)
  - Remarks (special notes, alternates)

## 360IPCirq Integration

IPD modules are tightly integrated with R/I procedures:
- **Item keys** match R/I procedure references
- **Consumables** (fasteners, sealants, shims) use same P/Ns in R/I
- **Tool callouts** align with R/I tool requirements
- **Removal kits** defined for common maintenance tasks
- Enables "removal for repair → IPC 360 reusability" philosophy

## Part Numbering

Part numbers follow BWB-Q100 numbering scheme:
- Format: `BWQ-XX-YYYY-ZZZ`
- Where:
  - **BWQ** = BWB-Q100 prefix
  - **XX** = ATA chapter (57)
  - **YYYY** = Component code
  - **ZZZ** = Piece part sequence

## Effectivity

Parts may have effectivity expressions:
- MSN ranges (e.g., "MSN 001 onwards")
- Configuration options (e.g., "Standard fuel capacity")
- Block modifications
- Service bulletins

## Interchangeability

IPD identifies:
- Direct alternates (form-fit-function equivalent)
- Approved substitutes (with restrictions)
- Superseded parts (replaced by newer P/N)
- Next higher assembly (NHA) relationships

## Validation Requirements

IPD modules must:
- Validate against S1000D 6.0 ipd.xsd schema (if applicable) or descript.xsd
- Comply with BREX rules (../../BREX/BREX.xml)
- Reference correct ICN illustrations
- Include proper effectivity expressions
- Align item numbers with figures

## Cross-References

IPD modules reference:
- **Descriptive modules** (../descriptive/) for technical details
- **Procedural modules** (../procedural/) for R/I and repair procedures
- **ATA-04 Master IPD** for aircraft-level catalog integration
- **Supply chain systems** for procurement and inventory

## Quality Control

IPD accuracy is critical for:
- Parts ordering and logistics
- Maintenance planning
- Configuration management
- Regulatory compliance (parts traceability)

Changes to IPD require:
- Engineering verification
- Configuration management approval
- Supply chain coordination
- Training material updates

## Related Documentation

- Descriptive modules: `../descriptive/`
- Procedural modules: `../procedural/`
- Contracts/schemas: `../../../contracts/schemas/`
- Evidence: `../../../evidence/`

---

*Part of ATA-57-10 S1000D documentation — Controlled under DMRL*
