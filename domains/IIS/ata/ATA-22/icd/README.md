# Interface Control Documents (ICDs)

This directory contains interface specifications for ATA-22 Autoflight system external communications.

## Contents

- `ata22_to_ata27.yaml` — Interface to ATA-27 Flight Controls (command outputs)
- `ata22_to_ata34.yaml` — Interface from ATA-34 Navigation/Air Data (sensor inputs)
- `ata22_to_ata46.yaml` — Interface to ATA-46 Information Systems (annunciations)

## Interface Architecture

### ATA-22 → ATA-27 (Flight Controls)
- Attitude command outputs (roll, pitch, yaw)
- Autopilot engage/disengage signals
- Flight Director mode status
- Control surface coordination commands

### ATA-22 ← ATA-34 (Navigation/Air Data)
- Attitude and rate data from inertial reference
- Air data (airspeed, altitude, vertical speed)
- Navigation solution (position, track, ground speed)
- FMS guidance commands (LNAV/VNAV)

### ATA-22 → ATA-46 (Information Systems)
- Autopilot mode annunciations
- Flight Director command bar data
- Caution and advisory messages
- System status indicators

## Communication Protocols

- **Bus Type**: AFDX (Avionics Full Duplex Switched Ethernet)
- **Backup**: ARINC 429 for critical functions
- **Update Rates**: 50Hz for control loops, 10Hz for annunciations
- **Integrity**: CRC protection and validity flags