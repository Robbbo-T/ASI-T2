# MAL Messaging

Topic-based publish-subscribe messaging system for ASI-T2 ecosystem.

## Purpose

Provides reliable message passing between all ASI-T2 components:
- Product-to-product communication
- Component-to-MAL communication
- Telemetry distribution
- Command/control messages

## Architecture

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  Publisher  │─────►│   Message   │─────►│ Subscriber  │
│   (AMPEL)   │      │    Broker   │      │  (GAIA)     │
└─────────────┘      └─────────────┘      └─────────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │ Data Plane  │
                     │  (Archive)  │
                     └─────────────┘
```

## Message Format

All messages use standardized format:
```json
{
  "header": {
    "topic": "MAL.v1.telemetry.ampel360",
    "timestamp": "2025-01-01T00:00:00Z",
    "schema_version": "1.0",
    "message_id": "uuid",
    "source": "AMPEL360_BWB"
  },
  "payload": {
    // schema-validated content
  },
  "signature": "optional_signature"
}
```

## Topics

Standard topic hierarchy:
- `MAL.v1.control.*` - Control commands
- `MAL.v1.telemetry.*` - Telemetry streams
- `MAL.v1.health.*` - Health updates
- `MAL.v1.mission.*` - Mission orchestration

## Quality of Service

- **At-least-once**: Default delivery guarantee
- **Exactly-once**: For critical messages
- **Fire-and-forget**: For non-critical logs

## Implementation

### H0: Simple Pub-Sub
- In-memory message passing
- Basic topic routing
- Local persistence

### H1: Distributed Messaging
- MQTT or NATS broker
- Persistent queues
- Cross-network messaging

### H2: Production-Grade
- Kafka for high-throughput
- Stream processing
- Multi-region replication
