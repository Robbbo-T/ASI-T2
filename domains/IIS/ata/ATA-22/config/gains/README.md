# Control Gains

This directory contains control law gain schedules for the ATA-22 Autoflight system.

## Contents

- `bwb_q100_default.yaml` — Default gain set for BWB-Q100 configuration

## Gain Structure

### Control Loops
- **Roll Hold**: Proportional-Integral-Derivative (PID) gains for bank angle control
- **Heading Hold**: PID gains for heading tracking
- **Pitch Hold**: PID gains for pitch attitude control  
- **Altitude Hold**: PID gains for altitude capture and hold
- **Yaw Damper**: Stability augmentation gains for yaw axis

### BWB-Q100 Specific Tuning
- Optimized for Blended Wing Body aerodynamics
- Elevon-dominated control surface configuration
- Cross-coupling compensation for BWB characteristics
- Stability margins appropriate for passenger transport

## Gain Selection

Multiple gain sets can be defined for different:
- Flight phases (takeoff, cruise, approach, landing)
- Weight and balance configurations
- Weather conditions and turbulence levels
- Degraded modes and failure scenarios

Gain selection is managed by the flight management system based on current flight conditions.