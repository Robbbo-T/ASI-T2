# MAL Telemetry

Real-time telemetry collection, aggregation, and streaming for all ASI-T2 products.

## Purpose

Collects and distributes telemetry data from:
- AMPEL360 BWB (flight parameters)
- GAIA SPACE (satellite telemetry)
- Defense Wall Swarm (agent states)
- Infrastructure systems (health metrics)

## Data Types

### Flight Telemetry (AMPEL360)
- Position, velocity, acceleration
- Attitude (roll, pitch, yaw)
- Control surface positions
- Engine parameters
- Fuel levels (H₂/LH₂)

### Satellite Telemetry (GAIA)
- Orbital parameters
- Attitude and control
- Power systems
- Payload status
- Communication metrics

### Swarm Telemetry (Defense Wall)
- Agent positions and velocities
- Coordination state
- Communication links
- Mission status
- Threat detection

### System Telemetry (Infrastructure)
- CPU, memory, disk usage
- Network metrics
- Service health
- Error rates

## Architecture

```
┌──────────┐
│ Sensors  │───┐
└──────────┘   │
               ▼
┌──────────┐   ┌────────────┐   ┌──────────────┐
│ Actuators│──►│ Telemetry  │──►│  Data Plane  │
└──────────┘   │  Collector │   │  (Storage)   │
               └────────────┘   └──────────────┘
┌──────────┐       │                    │
│ Systems  │───────┘                    │
└──────────┘                            ▼
                                ┌──────────────┐
                                │   Analytics  │
                                │   Queries    │
                                └──────────────┘
```

## Data Flow

1. **Collection**: Gather from sources at configured rates
2. **Validation**: Check ranges, types, completeness
3. **Aggregation**: Combine from multiple sources
4. **Enrichment**: Add metadata, calculations
5. **Distribution**: Publish to subscribers
6. **Archival**: Store in Data Plane

## Sampling Rates

- **Critical parameters**: 100 Hz (e.g., control loops)
- **Standard parameters**: 10 Hz (e.g., position, attitude)
- **Slow parameters**: 1 Hz (e.g., fuel levels)
- **Status parameters**: 0.1 Hz (e.g., system health)

## Storage Format

Time-series data in efficient format:
- **InfluxDB**: Time-series database
- **Parquet**: Columnar storage for archives
- **Protocol Buffers**: Wire format

## Queries

Support common queries:
- Time range queries
- Aggregations (min, max, avg)
- Downsampling
- Interpolation
- Anomaly detection

## Implementation Roadmap

**H0**: Basic telemetry collection and logging  
**H1**: Real-time streaming and dashboards  
**H2**: Advanced analytics and ML integration
