# Architecture (LLC/MAL)

## Overview
This document describes the architecture of ASI-T2 using Lifecycle Level Context (LLC) and Model Abstraction Layers (MAL).

## LLC (Lifecycle Level Context)
- **LLC**: levels and boundaries (program/system/subsystem/module/component).
- **Program Level**: BWB-Q100 overall program context
- **System Level**: Major subsystems (domains: AAA, PPP, LCC, etc.)
- **Subsystem Level**: Functional groupings within domains
- **Module Level**: Discrete functional units
- **Component Level**: Individual implementable artifacts

## MAL (Domain PLC)
- **MAL (domain PLC)**: logical control by domain (AAA…PPP).
- Domain-specific Product Lifecycle Management
- Each domain maintains:
  - `cax/` - Classical engineering
  - `qox/` - Quantum optimization
  - `ata/` - Documentation (S1000D)
  - `pax/` - Deployment orientation

## Interfaces
- **Interfaces**: contracts and PAx flows (ONB/OUT).
- ONB (Onboard): Internal system interfaces
- OUT (Outbound): External system interfaces
- Contract-based integration points

## Traceability
- **Traceability**: QS→FWD→UE→FE→CB→QB.
- QS: Quality System
- FWD: Forward chain
- UE: User Experience
- FE: Front End
- CB: Context Bridge
- QB: Quality Bridge

## UTCS Integration
All architecture elements are traced through UTCS v5.0 manifest system, ensuring:
- Evidence preservation
- Hash-based integrity
- SBOM tracking
- Digital provenance
