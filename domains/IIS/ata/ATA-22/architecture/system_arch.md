# ATA-22 System Architecture

## Redundancy & Partitions
- Triple Flight Control Computers (FCC-A/B/C) with cross-monitoring
- ARINC-429/664 for ATA-34/46; deterministic channel to ATA-27
- Partitioning per DO-178C/DO-297; AP (DAL A), FD (DAL B), YD (DAL A)

## Function Blocks
- **Mode Manager**: state machine, engages/disengages, mode priority
- **Lateral Path**: HDG/TRK, LNAV (FMS)
- **Vertical Path**: ALT/VS, VNAV (FMS)
- **Stability Aug**: Yaw Damper
- **Annunciation**: to ATA-46 EFIS/MFD; CAS messages via 46

## Interfaces (see ICDs)
- To **ATA-27**: attitude/axial commands (roll_deg, pitch_deg, yaw_rate_cmd), AP servos enable, trim bias
- From **ATA-34**: attitude, rates, airspeed, altitude, position, FMS lateral/vertical targets
- To **ATA-46**: AP/FD mode annunciations, aural/inhibit flags

## Safety Patterns
- Engage interlocks: valid sensors, no trim runaway, stick-shake inhibit, WOW gating
- Monitors: attitude limits, rate limits, control authority limits
- Disengage: stick force, TOGA, trim runaway, excessive deviation