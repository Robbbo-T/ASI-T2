# Loads Index

**Path:** `PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/AAA/ata/ATA-57/57-10_Wing_Primary_Structure/compliance/loads/`

## Purpose

This index references all load cases and load sets used in wing primary structure design.

## Load Categories

### Flight Loads
- **Limit Loads:** Maximum operational loads (1g to design limit load factors)
- **Ultimate Loads:** Limit loads × 1.5 safety factor
- **Gust Loads:** Discrete gust, continuous turbulence
- **Maneuver Loads:** Symmetric pull-up, roll, yaw, asymmetric

### Ground Loads
- **Landing:** Symmetric, asymmetric, hard landing, spring-back
- **Taxi:** Turning, braking, bumps
- **Towing:** Maximum tow loads

### Cabin Pressure Loads
- **Pressurization:** Maximum differential pressure
- **Depressurization:** Rapid decompression scenarios

### Environmental Loads
- **Temperature:** Hot day, cold day, temperature gradients
- **Lightning Strike:** Direct effects, indirect effects (structural provisions)

### Fatigue Loads
- **Spectra:** Design service goal (DSG) flight-by-flight loading
- **Load Sequences:** Representative flight profiles
- **Crack Growth:** Damage tolerance analysis inputs

## Load Sets

| Load Set ID | Description | Analysis Type | Source |
|------------|-------------|---------------|--------|
| LS-57-10-001 | Symmetric 2.5g pull-up | Static ultimate | FEA |
| LS-57-10-002 | Asymmetric roll | Static ultimate | FEA |
| LS-57-10-003 | Gust envelope | Static limit/ultimate | FEA |
| LS-57-10-004 | Pressure + maneuver | Combined loads | FEA |
| LS-57-10-005 | Fatigue spectrum | Fatigue/damage tolerance | FEA |

## References

Load data is maintained in CAX/FEA and referenced via:
- `../../../cax/FEA/loads/wingbox/` (detailed load distributions)
- Flight loads document (project baseline)

## Traceability

All loads must be traceable to:
1. Certification basis (CS-25, Part 25)
2. Flight test data or simulation
3. Loads analysis reports
4. Stress analysis inputs

---
*Loads are version-controlled and require Loads & Dynamics group approval for changes.*
