---
id: ASIT2-MAL-README
project: ASI-T2
artifact: Master Application Layer (MAL)
classification: INTERNAL–EVIDENCE-REQUIRED
version: "1.0.0"
release_date: "2025-01-01"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: pending
---

# MAL — Master Application Layer

**MAL** acts as the "PLC of domain" for the entire ASI-T2 ecosystem, providing common services, messaging, telemetry, health monitoring, and governance across all products.

## Overview

MAL is the foundational layer that enables:
- **Unified messaging** across all products (AMPEL360, GAIA SPACE, Swarms, etc.)
- **Telemetry collection** and routing to Data Plane
- **Health monitoring** and watchdogs
- **Registry and discovery** of services and components
- **Version control and signatures** for all artifacts

## Architecture

MAL follows the TFA (Top Federation Algorithm / Threading Final Assembly) pattern:

```
CB (Conceptual Boundary)
  → QB (Quantum Boundary)
    → UE (Unit Execution)
      → FE (Final Execution)
        → FWD (Forward Deployment)
          → QS (Quantum Seal)
```

## Components

### 1. Drivers (`drivers/`)
Low-level interfaces to hardware and external systems:
- Hardware abstraction layers
- Communication protocol implementations
- Sensor/actuator drivers

### 2. Messaging (`messaging/`)
Message bus and pub-sub system:
- Topic-based messaging
- Schema validation
- Message versioning
- Guaranteed delivery

### 3. Telemetry (`telemetry/`)
Telemetry collection and streaming:
- Metrics collection
- Time-series data
- Data aggregation
- Stream processing

### 4. Health (`health/`)
Health monitoring and watchdogs:
- Service health checks
- Failure detection
- Recovery mechanisms
- Alerting

### 5. Registry (`registry/`)
Service discovery and configuration:
- Service registration
- Configuration management
- Version tracking
- Dependency resolution

## Planes Architecture

MAL orchestrates four operational planes:

### Data Plane (`INFRA/DATA-PLANE`)
- Ingestión/telemetría (streams)
- Almacenamiento inmutable con UTCS
- Data lakes and warehouses

### Control Plane (`INFRA/CONTROL-PLANE`)
- Orquestación de misiones
- Seguridad, llaves, políticas
- MAL-EEM enforcement

### Model Plane (`INFRA/MODEL-PLANE`)
- Gemelos digitales (SIL/HIL)
- Simulación y V&V
- Digital twin synchronization

### Evidence Plane (`INFRA/EVIDENCE-PLANE`)
- SBOMs, DOIs, atestaciones
- QS/UTCS provenance
- Audit trails

## Interfaces

All products must implement canonical interfaces:

### Control Bus: `MAL.v1.control`
- Command/control messages
- Mission orchestration
- Safety overrides

### Telemetry Bus: `MAL.v1.telemetry`
- Real-time telemetry streams
- Health status updates
- Event notifications

### Data Schema: `schemas/v1/*.json`
- JSON Schema validation
- Version compatibility
- Schema evolution

## MAL-EEM (Ethics & Empathy Module)

MAL-EEM provides ethical guardrails for all operations:
- Mission rules validation
- Safety constraints enforcement
- Human oversight requirements
- Fail-closed behavior

## Integration

Each product must provide:

1. **`spec/PRODUCT.yaml`**: Product specification with interfaces
2. **`evidence/`**: SBOM, hashes, tags firmadas, logs
3. **Message schemas**: JSON schemas for all messages
4. **Health endpoints**: Health check implementations

## Version

Current version: **v1.0.0**

See `RELEASE.md` for version history and `CHANGELOG.md` for detailed changes.

## See Also

- [INFRA Architecture](../INFRA/README.md)
- [UTCS/QS Documentation](../HALL-OF-RECORDS/README.md)
- [Product Specifications](../PRODUCTS/README.md)
