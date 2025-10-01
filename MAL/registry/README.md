# MAL Registry

Service discovery and configuration management for ASI-T2 ecosystem.

## Purpose

Provides centralized registry for:
- Service discovery and location
- Configuration management
- Version tracking
- Dependency resolution
- Dynamic service routing

## Service Registration

### Registration Format

```json
{
  "service_id": "ampel360-bwb-sim",
  "service_type": "simulator",
  "version": "1.0.0",
  "endpoints": {
    "control": "tcp://localhost:5001",
    "telemetry": "tcp://localhost:5002",
    "health": "http://localhost:8080/health"
  },
  "capabilities": ["SIL", "flight_control", "telemetry"],
  "dependencies": ["MAL.messaging", "MAL.telemetry"],
  "metadata": {
    "product": "AMPEL360_BWB",
    "trl": 4,
    "maintainer": "ASI-T"
  }
}
```

### Registration Lifecycle

1. **Register**: Service announces itself to registry
2. **Heartbeat**: Periodic health updates
3. **Deregister**: Graceful shutdown notification
4. **Expire**: Automatic removal if heartbeat stops

## Service Discovery

### Discovery Queries

```python
# Find service by type
services = registry.find(service_type="simulator")

# Find service by capability
services = registry.find(capabilities=["flight_control"])

# Find service by product
services = registry.find(product="AMPEL360_BWB")

# Get specific service
service = registry.get("ampel360-bwb-sim")
```

## Configuration Management

### Configuration Schema

```yaml
service: ampel360-bwb-sim
version: 1.0.0
config:
  simulation:
    timestep: 0.01
    duration: 3600
  control:
    pid_gains:
      pitch: {p: 2.0, i: 0.1, d: 0.5}
      roll: {p: 1.5, i: 0.1, d: 0.3}
  telemetry:
    sample_rate: 100
    buffer_size: 10000
```

### Configuration Updates

- **Static**: Configuration loaded at startup
- **Dynamic**: Hot-reload without restart
- **Versioned**: Configuration version tracking
- **Validated**: Schema validation before apply

## Version Management

### Semantic Versioning

Services use semantic versioning: `MAJOR.MINOR.PATCH`

```
1.0.0 → 1.0.1  (patch: bug fix, backward compatible)
1.0.0 → 1.1.0  (minor: new features, backward compatible)
1.0.0 → 2.0.0  (major: breaking changes)
```

### Version Resolution

- **Exact match**: Request specific version
- **Compatible**: Request compatible versions (^1.2.3)
- **Latest**: Use latest stable version

## Dependency Resolution

### Dependency Graph

```
AMPEL360_BWB_SIM
├── MAL.messaging v1.0.0
├── MAL.telemetry v1.0.0
└── INFRA.MODEL-PLANE v1.0.0
    ├── MAL.drivers v1.0.0
    └── MAL.health v1.0.0
```

### Circular Dependency Detection

Registry detects and prevents circular dependencies.

## Implementation

**H0**: Simple in-memory registry  
**H1**: Distributed registry (Consul/etcd)  
**H2**: Advanced service mesh integration
