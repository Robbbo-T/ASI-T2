# MAL Topic Grammar & Path Conventions

## Overview

MAL uses a standardized topic grammar for message routing across all transport layers (NATS, MQTT5, DDS, AMQP, Kafka). This document defines the canonical naming conventions.

## Topic Structure

### General Pattern

```
mal/<major>/<contract>/<product>/<domain>/<component>/<stream>
```

### Components

- **`mal`**: Fixed prefix identifying MAL protocol messages
- **`<major>`**: MAL protocol major version (e.g., `1`, `2`)
- **`<contract>`**: Contract type: `control`, `telemetry`, `health`, `log`
- **`<product>`**: Product identifier (e.g., `BWB-Q100`, `GAIA-AIR`, `H2-AIRPORT`)
- **`<domain>`**: Domain code (AAA-PPP, 15 canonical domains)
- **`<component>`**: Component or subsystem identifier (e.g., `ATA-57`, `flight_ctl`)
- **`<stream>`**: Stream or signal name (e.g., `wing/left`, `mode_status`)

## Contract-Specific Patterns

### Control Topics

Pattern: `mal/1/control/<product>/<domain>/<component>/<unit>`

Examples:
```
mal/1/control/BWB-Q100/AAA/flight_ctl/primary
mal/1/control/GAIA-AIR/PPP/propulsion/engine_1
mal/1/control/H2-AIRPORT/HHH/fueling/station_3
```

### Telemetry Topics

Pattern: `mal/1/telemetry/<product>/<domain>/<component>/<signal>`

Examples:
```
mal/1/telemetry/BWB-Q100/AAA/ATA-57/wing/left
mal/1/telemetry/BWB-Q100/AAA/ATA-49/power/bus_a
mal/1/telemetry/GAIA-AIR/EEE/environment/cabin_pressure
```

### Health Topics

Pattern: `mal/1/health/<product>/<service>`

Examples:
```
mal/1/health/BWB-Q100/flight_control
mal/1/health/BWB-Q100/telemetry_aggregator
mal/1/health/H2-AIRPORT/fueling_controller
```

### Log Topics

Pattern: `mal/1/log/<product>/<domain>/<component>`

Examples:
```
mal/1/log/BWB-Q100/AAA/flight_ctl
mal/1/log/GAIA-AIR/PPP/propulsion
mal/1/log/H2-AIRPORT/HHH/safety_monitor
```

## TFA Repository Path Mapping

MAL topics map to TFA repository structure:

```
domains/<DOMAIN>/ATA-XX/<XX-XX>_<DESCRIPTION>/S1000D/<LAYER>/<PACK>/<SUBPACK>
```

### Layer Codes
- **QS**: Primordial / Quantum State
- **FWD**: Forward Wave Dynamics / Prediction
- **UE**: Unit Element / Collapse
- **FE**: Federation Entanglement / Contracting
- **CB**: Classical Bit / Companion Binary
- **QB**: Bit Cubic (non-quantumised)

### Pack Codes
- **CAx**: Computer Aided (design, analysis, etc.)
- **QOx**: Quantum Optimizations
- **PAx**: Packaging & Assemblies
  - **OB**: Onboard (only allowed orientation)
  - **OFF**: Outboard (only allowed orientation)

## Wildcards and Subscriptions

### Single-level Wildcard
Use `+` for single-level wildcards:
```
mal/1/telemetry/BWB-Q100/+/ATA-57/wing/left    # All domains
mal/1/control/+/AAA/flight_ctl/primary          # All products
```

### Multi-level Wildcard
Use `#` (MQTT) or `>` (NATS) for multi-level:
```
mal/1/telemetry/BWB-Q100/AAA/#                  # All AAA telemetry
mal/1/health/BWB-Q100/>                         # All BWB-Q100 health
```

## Topic Access Control

Topics follow hierarchical access control patterns:
- Product-level isolation: `mal/1/+/<product>/#`
- Domain-level isolation: `mal/1/+/<product>/<domain>/#`
- Component-level isolation: `mal/1/+/<product>/<domain>/<component>/#`

## Best Practices

1. **Use hierarchical structure**: Organize topics from general to specific
2. **Avoid dynamic segments**: Keep topic structure predictable
3. **Document custom streams**: Register new stream names in domain specifications
4. **Consider retention**: Apply appropriate retention policies by contract type
5. **Plan for scale**: Design subscriptions to minimize cross-product traffic

## Naming Conventions

- Use **lowercase** for domains and components
- Use **uppercase** for products
- Use **underscores** for multi-word identifiers (e.g., `flight_ctl`)
- Use **forward slashes** for hierarchy (e.g., `wing/left`)
- Keep segments **short** (≤ 20 characters when possible)
- Avoid special characters except `-`, `_`, `/`

## Validation

Topic names MUST match this regex:
```regex
^mal/\d+/(control|telemetry|health|log)/[A-Z0-9_-]+/[A-Z]{3}/[a-z0-9_-]+(/[a-z0-9_/-]+)*$
```

Validate using:
```bash
echo "mal/1/telemetry/BWB-Q100/AAA/ATA-57/wing/left" | \
  grep -E '^mal/[0-9]+/(control|telemetry|health|log)/[A-Z0-9_-]+/[A-Z]{3}/[a-z0-9_-]+(/[a-z0-9_/-]+)*$'
```

## References

- Master Whitepaper #2: MAL Technical Specification
- TFA-V2 Framework Documentation
- Domain Reference Guide (AAA-PPP)
- ATA Chapter Mapping Reference
