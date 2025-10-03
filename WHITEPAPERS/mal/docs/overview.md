# MAL (Master Application Layer) - Architecture Overview

## Introduction

MAL (Master Application Layer/Logic) is the foundational communication and control framework for the ASI-T2 ecosystem. It provides a standardized, transport-agnostic contract suite that enables deterministic, verifiable, and secure messaging across all products and domains.

## Design Philosophy

### Core Principles

1. **Transport Agnostic**: Works with NATS, MQTT5, Kafka, DDS, AMQP
2. **Schema Versioned**: Every message carries its contract version
3. **Policy Driven**: MAL-EEM governs authorization and ethics
4. **Evidence Native**: Built-in UTCS hooks for provenance and attestation
5. **Zero Trust**: Verify every message, assume breach

### Architecture Goals

- **Simplicity**: Minimal contracts covering essential operations
- **Composability**: Mix and match transports, serializers, security layers
- **Observability**: Every interaction produces audit trail
- **Reproducibility**: Same inputs yield same outputs with proof
- **Safety**: Fail-secure defaults, defensive validation

## System Architecture

### Four Planes Model

```
┌─────────────────────────────────────────────────────────┐
│                    Evidence Plane                        │
│  SBOM · Signatures · UTCS Bundles · DOIs · Audit Logs  │
└─────────────────────────────────────────────────────────┘
                            ↑
┌─────────────────┬─────────────────┬─────────────────────┐
│  Control Plane  │   Data Plane    │    Model Plane      │
│  Commands       │   Telemetry     │    SIL/HIL         │
│  Policies       │   Ingestion     │    Scenarios       │
│  Keys           │   Storage       │    Assertions      │
└─────────────────┴─────────────────┴─────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│              MAL Transport Adapters                      │
│    NATS · MQTT5 · Kafka · DDS · AMQP · Custom          │
└─────────────────────────────────────────────────────────┘
```

### Component Stack

```
Application Layer
    ↓
┌────────────────────────────────────┐
│ MAL Contracts (Control/Telemetry/  │
│              Health/Log)            │
├────────────────────────────────────┤
│ mal-sec (Sign/Verify/Encrypt)      │
├────────────────────────────────────┤
│ mal-ver (Schema Evolution)         │
├────────────────────────────────────┤
│ mal-bus (Transport Adapters)       │
├────────────────────────────────────┤
│ mal-evd (Evidence Emission)        │
└────────────────────────────────────┘
    ↓
Transport Layer (NATS/MQTT/DDS/etc.)
```

## MAL Contracts

### Contract Types

MAL defines four core contracts:

1. **Control (`MAL.v1.control`)**
   - Purpose: Command execution with idempotency
   - Use cases: Mode changes, parameter updates, maneuvers
   - Guarantees: Exactly-once execution, timeout handling, ack/nack

2. **Telemetry (`MAL.v1.telemetry`)**
   - Purpose: Time-series data collection
   - Use cases: Sensor readings, system metrics, mission data
   - Guarantees: Ordered delivery, signed integrity, tagged filtering

3. **Health (`MAL.v1.health`)**
   - Purpose: Liveness and readiness monitoring
   - Use cases: Service discovery, load balancing, failure detection
   - Guarantees: Periodic heartbeats, dependency tracking

4. **Log (`MAL.v1.log`)**
   - Purpose: Structured logging with flight-recorder support
   - Use cases: Debugging, compliance, incident analysis
   - Guarantees: Immutable segments, hash chains, distributed tracing

### Message Flow

```
Producer                  Transport                  Consumer
   │                         │                          │
   │  1. Create message      │                          │
   │─────────────────────────┤                          │
   │                         │                          │
   │  2. Sign with Ed25519   │                          │
   │─────────────────────────┤                          │
   │                         │                          │
   │  3. Publish to topic    │                          │
   │────────────────────────→│                          │
   │                         │                          │
   │                         │  4. Route by topic       │
   │                         │─────────────────────────→│
   │                         │                          │
   │                         │  5. Verify signature     │
   │                         │  6. Validate schema      │
   │                         │  7. Check policy         │
   │                         │  8. Process message      │
   │                         │                          │
   │  9. Ack (if required)   │                          │
   │←────────────────────────┼──────────────────────────│
```

## Deployment Profiles

### Edge-Micro (Vehicles, Test Benches)

- **Characteristics**: Resource-constrained, real-time requirements
- **Components**: mal-io, mal-ctl, mal-tmx, mal-hlth, mal-sec (minimal)
- **Transport**: MQTT5 or DDS for low latency
- **Retention**: Limited (hours to days)
- **Evidence**: Sign and forward to hub

### Site-Node (Ground Stations, Airports)

- **Characteristics**: Moderate resources, local aggregation
- **Components**: Full MAL stack with local storage
- **Transport**: NATS or MQTT5 for reliability
- **Retention**: Medium (days to weeks)
- **Evidence**: Local UTCS bundles + forward to hub

### Control-Hub (Mission Control, Evidence Repository)

- **Characteristics**: High resources, central coordination
- **Components**: Full MAL stack + evidence plane
- **Transport**: Kafka for high throughput, NATS for control
- **Retention**: Long-term (months to years)
- **Evidence**: Complete UTCS bundles, SBOM, DOIs, audit logs

## Topic Hierarchy

MAL uses hierarchical topic naming for routing and access control:

```
mal/<major>/<contract>/<product>/<domain>/<component>/<stream>
```

Examples:
```
mal/1/control/BWB-Q100/AAA/flight_ctl/primary
mal/1/telemetry/BWB-Q100/AAA/ATA-57/wing/left
mal/1/health/BWB-Q100/telemetry_aggregator
mal/1/log/BWB-Q100/AAA/flight_ctl
```

See [Topic Grammar](topic_grammar.md) for complete specification.

## Security Model

### Defense in Depth

1. **Identity Layer**: Attestable device/service identities
2. **Cryptographic Layer**: Ed25519 signatures, X25519 encryption
3. **Policy Layer**: MAL-EEM authorization engine
4. **Transport Layer**: TLS 1.3, mTLS where applicable
5. **Audit Layer**: Comprehensive security event logging

### Threat Mitigations

- **Replay**: Nonce + monotonic sequence + timestamp validation
- **Impersonation**: PKI + signature verification + key rotation
- **MITM**: TLS + end-to-end encryption + certificate pinning
- **Downgrade**: Minor-compat floor negotiation
- **Schema Poisoning**: Signed schema distribution + strict validation

See [Security Model](security_model.md) for complete specification.

## Versioning & Evolution

### SemVer Compliance

```
MAL Protocol: MAJOR.MINOR.PATCH
Schemas:      vMAJOR (breaking) / vMAJOR.MINOR (compatible)
```

### Compatibility Rules

- **MINOR** versions: Backward-compatible on the wire
- **MAJOR** versions: Breaking changes with migrators
- **Schema headers**: Every frame declares version and compatibility floor
- **Negotiation**: Responders accept any `compat-minor` ≤ their minor

### Migration Strategy

1. Deploy new version alongside old (dual-stack)
2. Provide migrators for major version transitions
3. Monitor adoption metrics
4. Deprecate old version with 90-day sunset
5. Remove old version after sunset period

## Evidence & Provenance

### UTCS Integration

MAL integrates with UTCS v5.0 for deterministic bundling:

- **Context**: Whitepaper, overview docs
- **Content**: Schemas, contracts
- **Cache**: Examples, test vectors
- **Structure**: Topic grammar, versioning rules
- **Style**: Citation format (CSL)
- **Sheet**: Build scripts (Makefile)

### Evidence Pipeline

```
1. Git tag (signed):        git tag -s v1.0.0
2. Generate SBOM:           syft dir:. -o spdx-json
3. Create UTCS bundle:      bundle schemas + docs
4. Sign artifacts:          cosign sign-blob
5. Publish DOI:             Zenodo or DataCite
6. Update Hall of Records:  index in evidence registry
```

## Performance Targets

### H0 (0-90 days) SLOs

- **Control latency**: p95 ≤ 25ms (edge), ≤ 120ms (site)
- **Telemetry throughput**: ≥ 10k pts/s (edge), ≥ 50k pts/s (hub)
- **Health heartbeat loss**: ≤ 0.1% per 24h
- **Uptime**: ≥ 99.5%
- **Evidence lag**: ≤ 30s from segment close

### Scalability Targets

- **Nodes**: Support 10k+ edge nodes per hub
- **Messages**: 1M+ messages/second at hub
- **Topics**: 100k+ unique topics
- **Retention**: Years of telemetry at hub

## Integration Patterns

### Pub/Sub Pattern

```python
import mal

# Initialize MAL client
client = mal.Client(transport='nats', endpoint='nats://hub:4222')

# Publish telemetry
await client.telemetry.publish(
    topic='mal/1/telemetry/BWB-Q100/AAA/ATA-57/wing/left',
    points=[
        {'k': 'load.kN', 'v': 12.7}
    ],
    tags={'mission': 'H0-sim-001'}
)

# Subscribe to control commands
async for msg in client.control.subscribe('mal/1/control/BWB-Q100/+/+/+'):
    if msg.cmd == 'set_mode':
        await execute_mode_change(msg.args['mode'])
        await msg.ack()
```

### Request/Reply Pattern

```python
# Send control command with reply
response = await client.control.request(
    topic='mal/1/control/BWB-Q100/AAA/flight_ctl/primary',
    cmd='set_mode',
    args={'mode': 'AUTO'},
    timeout=3000
)

if response.status == 'ack':
    print('Command executed successfully')
else:
    print(f'Command failed: {response.reason}')
```

## Compliance & Standards

- **ARP4754A/ARP4761**: Safety assessment (scoped)
- **DO-178C**: Software considerations (Level C/D guidance)
- **DO-254**: Hardware considerations (when applicable)
- **ECSS**: Space engineering standards (progressive)
- **IEC 62443**: Industrial control systems security
- **ISO/IEC 27001**: Information security management

## Roadmap

### H0 (0-90 days)
- Core contracts (ctl, tmx, hlth, log)
- NATS and MQTT5 adapters
- Ed25519 signing
- UTCS hooks
- SBOM pipeline

### H1 (3-9 months)
- DDS/RTPS adapter
- Envelope encryption (X25519)
- Mission planner API
- Timeline visualizer
- Observability dashboards

### H2 (9-24 months)
- Multi-org federation
- Hardware roots (TPM, SE)
- Formal verification suite
- Third-party audits
- ECSS/DO-178C certification paths

## Getting Started

### Installation

```bash
# Python SDK
pip install mal-sdk

# Go SDK
go get github.com/asi-t2/mal-go

# Rust SDK
cargo add mal-rs
```

### Quick Start

See [MAL Deployment Guide](mal_deployment_guide.md) for complete setup instructions.

## References

- [Master Whitepaper #2](../../MASTER_WHITEPAPER_2_MAL.md) - Complete MAL specification
- [Topic Grammar](topic_grammar.md) - Naming conventions
- [Security Model](security_model.md) - Security architecture
- [UTCS Manifest](../utcs/manifest.yaml) - Bundle specification
- [Schemas](../../schemas/mal/) - JSON Schema definitions

## Support

- **Issues**: https://github.com/Robbbo-T/ASI-T2/issues
- **Discussions**: https://github.com/Robbbo-T/ASI-T2/discussions
- **Email**: asi-t-arch@example.org

---

**MAL** — Simple contracts, verifiable evidence, trustworthy systems.
