# Descriptive Data Modules

Technical descriptions and specifications for ATA-22 Auto Flight Control System.

## Key Files

- **DMC-BWB1-A-22-10-00-00A-040A-D-EN-US.xml** - AFCS Architecture and System Overview - comprehensive description of autopilot, flight director, autothrottle, and protection functions with ARINC 653/664 integration

## Hyperlinkable Index — BWB-Q100 (ATA-22 · S1000D)

**Path Root:**  
`PRODUCTS/AMPEL360/BWB-Q100/domains/IIS/ata/ATA-22/S1000D/data_modules/descriptive/`

### Data Modules (DMs)

- [`DMC-BWB1-A-22-10-00-00A-040A-D-EN-US.xml`](./DMC-BWB1-A-22-10-00-00A-040A-D-EN-US.xml)

## Contents

This directory contains descriptive data modules covering:

### 22-10-00 Autopilot (AP)
- Autopilot system architecture descriptions
- Control law specifications and mode logic
- Engagement/disengagement criteria and protections
- Interface definitions with QAFbW and FMS

### 22-11-00 Flight Director (FD)
- Flight director display and guidance descriptions
- Command generation and presentation logic
- Mode annunciation and pilot interface specifications
- HMI_BRIDGE integration documentation

### 22-12-00 Autothrottle/Thrust Management (A/T)
- Autothrottle system operation descriptions
- Thrust command generation and limiting functions
- Engine interface specifications and FADEC integration
- Performance optimization algorithms

### 22-15-00 Altitude/Speed Alerting & Protections
- Altitude and speed alerting system descriptions
- Protection envelope specifications and alert logic
- Crew alerting system integration
- MAL-EEM ethics guard implementation

### 22-18-00 Autoland/Approach Capability
- Autoland system architecture (where applicable)
- Approach mode specifications and guidance laws
- Ground proximity and runway sensing integration
- Fail-operational and fail-passive capabilities

### 22-20-00 AFCS Monitoring & BITE
- Built-In Test Equipment (BITE) specifications
- Health monitoring and fault detection descriptions
- System performance monitoring capabilities
- Maintenance data collection and reporting

### 22-90-00 Interfaces
- ARINC 653 partition interface specifications
- ARINC 664 virtual link definitions and timing
- ARINC 429 label assignments and data formats
- Cross-domain integration with NET_STACK and NAVSYS

## Data Module Template

Each descriptive data module includes:
- AFCS subsystem technical description
- System specifications and performance parameters
- Interface definitions (A653/A664/A429)
- Safety requirements and MAL-EEM compliance
- UTCS/QS evidence integration points
- Cross-references to INFRANET/AQUA_OS_AIRCRAFT components

## S1000D Issue 6.0 Compliance

All data modules in this directory:
- Use Model Identification Code "BWB1" (mapped to "BWB-Q100")
- Validate against XSD schemas (no DTD)
- Reference the project BREX for Auto Flight business rules
- Use proper information codes (040 for descriptions, 034 for technical data)
- Include UTCS-MI v5.0 headers with canonical hashes for traceability
- Support deterministic timing requirements for ARINC 653 partitions
- Integrate with AQUA_OS_AIRCRAFT partition manager for DAL-A compliance