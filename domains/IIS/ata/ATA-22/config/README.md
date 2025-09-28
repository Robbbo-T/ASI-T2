# Configuration Management

This directory contains configuration files for the ATA-22 Autoflight system.

## Contents

- `modes.yaml` — Autopilot mode definitions, interlocks, and transitions
- `gains/` — Control law gain schedules for different flight envelopes

## Configuration Structure

### Mode Configuration
- Lateral modes: ROLL, HEADING, TRACK, LNAV
- Vertical modes: PITCH, ALTITUDE, VERTICAL SPEED, VNAV
- Engage/disengage interlocks and safety limits
- Mode transition logic and priority handling

### Gain Scheduling
- BWB-Q100 specific control gains
- Flight envelope dependent parameters
- Redundant gain sets for different channels

## Usage

Configuration files are loaded at system initialization and can be updated through certified configuration management processes following DO-178C guidelines.