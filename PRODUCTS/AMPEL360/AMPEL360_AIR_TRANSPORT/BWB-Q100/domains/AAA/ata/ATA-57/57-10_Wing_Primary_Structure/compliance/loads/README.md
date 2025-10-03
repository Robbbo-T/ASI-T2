# Loads

This directory contains references to all load cases and load sets used in wing primary structure design.

## Purpose

Catalogs and references:
- Design load cases (limit and ultimate)
- Load distributions and envelopes
- Fatigue load spectra
- Combined loading conditions

## Contents

- **index.md** — Master index of loads with references to detailed FEA results

## Load Categories

### Flight Loads
- Maneuver loads (symmetric, asymmetric, roll, yaw)
- Gust loads (discrete, continuous turbulence)
- Limit and ultimate load factors

### Ground Loads
- Landing loads (symmetric, asymmetric, hard landing)
- Taxi loads (turning, braking, bumps)
- Towing loads

### Cabin Pressure Loads
- Maximum differential pressure
- Depressurization scenarios

### Environmental Loads
- Temperature effects (hot day, cold day, gradients)
- Lightning strike (structural provisions)

### Fatigue Loads
- Design service goal (DSG) spectra
- Flight-by-flight loading sequences
- Damage tolerance analysis inputs

## References

Detailed loads data maintained in:
- `../../../cax/FEA/loads/wingbox/` — FEA load distributions
- Flight loads analysis reports

## Traceability

All loads are traceable to:
- Certification basis (CS-25, Part 25)
- Flight test data or validated simulations
- Loads analysis reports
- Stress analysis inputs

---

*Part of ATA-57-10 Wing Primary Structure — Configuration controlled under UTCS/QS v5.0*
