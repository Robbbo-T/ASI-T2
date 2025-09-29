# Architecture Documentation

This directory contains system architecture documentation for ATA-22 Autoflight system.

## Contents

- `system_arch.md` — Core system architecture, redundancy patterns, and safety design

## Architecture Overview

The ATA-22 system implements a triple-redundant Flight Control Computer (FCC) architecture with:
- DAL A partitioning for safety-critical functions
- ARINC 429/664 interfaces for data exchange
- Cross-monitoring between redundant channels
- Deterministic timing for real-time performance

## Design Patterns

- **Redundancy**: Triple FCC configuration (A/B/C channels)
- **Partitioning**: DO-178C/DO-297 compliant separation
- **Monitoring**: Continuous cross-channel verification
- **Safety**: Built-in test equipment (BITE) and failure detection