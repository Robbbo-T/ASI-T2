# ASM-003 — Mid-Span Wing Box

**ATA Chapter:** ATA-57 (Wing)

## Overview

Mid-span wing box structure providing primary bending and torsional load paths for the BWB-Q100 wing.

## Contents

- **models/**: 3D CAD models and structural definitions
- **drawings/**: 2D technical drawings and documentation  
- **icd/**: Interface Control Documents
- **metadata.yaml**: Assembly metadata and configuration

## Description

The mid-span wing box is a critical structural element that:

- Transfers loads between centerbody and outboard sections
- Houses fuel systems and equipment
- Provides mounting for control surfaces
- Integrates with carry-through spars

## Related Assemblies

- ASM-002: Centerbody Primary Box
- ASM-004: Outboard Wing Box
- ASM-006: Leading-Edge Primary Structure
- ASM-007: Trailing-Edge Primary Structure
- ASM-018: Wing Carry-Through Spars

## QOx Optimization Variables

- **rib_spacing**: [600, 700, 800, 900, 1000] mm
- **panel_configuration**: discrete optimization choices

## Manufacturing

Composite construction with integrated ribs and spars for optimal load distribution and weight efficiency.