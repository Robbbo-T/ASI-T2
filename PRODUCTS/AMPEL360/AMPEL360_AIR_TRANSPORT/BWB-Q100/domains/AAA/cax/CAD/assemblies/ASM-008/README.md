# ASM-008 — Elevon/Flap Boxes

**ATA Chapter:** ATA-57 (Wing)

## Overview

Primary control surface boxes for elevons and flaps providing pitch and roll control for the BWB-Q100.

## Contents

- **models/**: 3D CAD models and structural definitions
- **drawings/**: 2D technical drawings and documentation  
- **icd/**: Interface Control Documents
- **metadata.yaml**: Assembly metadata and configuration

## Description

This assembly includes structural boxes for:

- Primary elevon surfaces (EL1_L/R, EL2_L/R, EL3_L/R)
- High-lift flap surfaces (FLAP1_L/R, FLAP2_L/R)
- Actuator mounting provisions
- Control system integration

## Control Surface Mapping

**Elevons:** EL1_L, EL1_R, EL2_L, EL2_R, EL3_L, EL3_R  
**Flaps:** FLAP1_L, FLAP1_R, FLAP2_L, FLAP2_R

**Configuration Files:**
- [elevons.yaml](../../wing_baseline_model/control_surfaces/elevons.yaml)
- [flaperons.yaml](../../wing_baseline_model/control_surfaces/flaperons.yaml)

## Related Assemblies

- ASM-007: Trailing-Edge Primary Structure  
- ASM-009: Spoiler/Airbrake Boxes
- ASM-010: Trim/Tab Structure

## QOx Optimization Variables

- **hinge_line_optimization**: discrete optimization choices
- **actuator_placement**: discrete optimization choices

## Manufacturing

Precision composite construction with integrated actuator mounts and control system provisions.