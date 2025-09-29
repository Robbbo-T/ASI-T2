# Software-in-the-Loop (SITL) Testing

This directory contains the SITL test harness for ATA-22 Autoflight system integration testing.

## Contents

- `run_sitl.py` — Main SITL execution script

## SITL Overview

The Software-in-the-Loop harness provides:
- Simulated aircraft dynamics for BWB-Q100
- Sensor data injection and validation
- Autopilot mode testing in realistic scenarios
- Integration verification between system components

## Test Scenarios

### Basic Functionality
- Autopilot engage/disengage sequences
- Mode transitions (lateral and vertical)
- Safety interlock validation
- Flight Director command generation

### BWB-Q100 Specific Tests
- Elevon control coordination
- Differential spoiler operation
- Yaw damper effectiveness
- Control coupling characteristics

### Failure Mode Testing
- Sensor failure detection and response
- Control surface failures
- Communication link degradation
- Redundancy management validation

## Usage

```bash
# Run basic SITL demonstration
python PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22/sitl/run_sitl.py

# Run with specific test scenario
python PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22/sitl/run_sitl.py --scenario approach

# Run with failure injection
python PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22/sitl/run_sitl.py --inject-failure sensor_invalid
```

## Integration

The SITL harness integrates with:
- Python unittest framework for automated testing
- CI/CD pipeline for regression testing
- HIL (Hardware-in-the-Loop) systems for validation
- Flight test data for correlation