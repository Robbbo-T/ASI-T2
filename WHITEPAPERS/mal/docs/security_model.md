# MAL Security Model (MAL-SEC)

## Overview

The MAL Security Model (MAL-SEC) provides defense-in-depth across the TFA-V2 bridge, ensuring that all MAL contracts are protected against common attack vectors while maintaining operational performance.

## Security Principles

1. **Zero Trust**: Verify every request, never assume trust
2. **Least Privilege**: Minimum necessary permissions for each entity
3. **Defense in Depth**: Multiple layers of security controls
4. **Fail Secure**: Default to secure state on error
5. **Audit Everything**: Comprehensive logging of security events

## Identity & Authentication

### Device/Service Identities

All MAL participants MUST have unique, attestable identities:

```
<product>.<domain>.<component>.<instance>
```

Examples:
```
BWB-Q100.AAA.flight_ctl.primary
GAIA-AIR.PPP.engine_ctrl.engine_1
H2-AIRPORT.HHH.fueling.station_3
```

### Identity Attestation

Identities are established through:
1. **Hardware roots** (TPM, Secure Enclave) where available
2. **Certificate-based** authentication (X.509)
3. **Key-based** authentication (Ed25519 signing keys)

### Authentication Flow

```
1. Service generates identity keypair (Ed25519)
2. Certificate signed by domain CA or hardware root
3. Identity registered in MAL registry
4. Service presents signed identity in message headers
5. Recipient validates signature and checks revocation
```

## Cryptographic Primitives

### Signing (Integrity & Non-repudiation)

- **Algorithm**: Ed25519 (RFC 8032)
- **Key Length**: 256 bits
- **Purpose**: Message signatures, identity attestation
- **Key ID Format**: `ed25519:<layer>:<domain>:<sequence>`

Example:
```
key-id: ed25519:QS:core:0001
```

### Encryption (Confidentiality)

- **Algorithm**: X25519 (ECDH) + ChaCha20-Poly1305 (AEAD)
- **Key Length**: 256 bits (ephemeral session keys)
- **Purpose**: Envelope encryption for sensitive payloads
- **Key Exchange**: Elliptic Curve Diffie-Hellman

### Hashing (Integrity Verification)

- **Algorithm**: SHA-256
- **Purpose**: Content addressing, chain linking, SBOM verification
- **Format**: Hex-encoded or base64

## Message Security

### Frame Envelope Security

Every MAL frame includes security metadata in the header:

```json
{
  "hdr": {
    "mid": "9d1b...f1",
    "ts": "2025-10-03T09:12:11.456Z",
    "seq": 102934,
    "src": "BWB-Q100.AAA.ATA-57",
    "sig": "base64(ed25519(signature))",
    "key-id": "ed25519:QS:core:0001",
    "nonce": "random-nonce-value",
    "compat-minor": 2
  }
}
```

### Signature Coverage

Signatures cover:
1. Message body (canonical JSON)
2. Header fields: `mid`, `ts`, `seq`, `src`, `contract`
3. Nonce (replay protection)

### Signature Verification

Recipients MUST:
1. Verify signature using sender's public key
2. Check key-id is not revoked
3. Validate timestamp is within acceptable skew (±30s)
4. Verify sequence number is monotonically increasing
5. Check nonce has not been seen (replay protection)

## Threat Model & Mitigations

### Replay Attacks

**Threat**: Attacker captures and retransmits valid messages

**Mitigations**:
- Idempotency keys (`idempKey`) for control messages
- Monotonic sequence numbers per stream
- Nonce tracking with time-bounded cache
- Timestamp validation (reject messages > 30s old)

### Impersonation

**Threat**: Attacker claims false identity

**Mitigations**:
- Mandatory signature verification
- Public key infrastructure (PKI) with CA validation
- Hardware-backed keys where available
- Regular key rotation

### Schema Poisoning

**Threat**: Malicious schema causes parser vulnerabilities

**Mitigations**:
- Schema versioning with cryptographic hashes
- Schema distribution through trusted channels only
- JSON schema validation before processing
- Strict parsing (reject unknown fields)

### Downgrade Attacks

**Threat**: Force use of older, vulnerable protocol versions

**Mitigations**:
- `compat-minor` floor negotiation
- Minimum version enforcement policies
- Reject connections below security baseline
- Monitor for downgrade attempts

### Side-Channel Attacks

**Threat**: Timing or power analysis reveals secrets

**Mitigations**:
- Constant-time cryptographic operations
- No secret-dependent branching in validators
- Uniform response times for auth failures
- Key material protected in secure memory

### Man-in-the-Middle (MITM)

**Threat**: Attacker intercepts and modifies messages

**Mitigations**:
- TLS 1.3 for transport layer
- End-to-end envelope encryption for sensitive data
- Mutual authentication (mTLS) where supported
- Certificate pinning for critical paths

## Authorization (MAL-EEM Policy Engine)

### Policy Model

Authorization evaluates:
```
ALLOW/DENY = f(subject, action, resource, context)
```

Where:
- **Subject**: Identity making the request
- **Action**: Operation (read, write, execute, subscribe, publish)
- **Resource**: Target topic or component
- **Context**: Mission constraints, SLOs, time, location

### Policy Examples

```yaml
policies:
  - name: "flight-control-commands"
    subjects: ["BWB-Q100.AAA.mission_planner.*"]
    actions: ["publish"]
    resources: ["mal/1/control/BWB-Q100/AAA/flight_ctl/*"]
    effect: "allow"
    conditions:
      - "mission.phase in ['pre-flight', 'flight', 'landing']"
      - "time.now < mission.deadline"

  - name: "telemetry-read-only"
    subjects: ["*.*.monitoring.*"]
    actions: ["subscribe"]
    resources: ["mal/1/telemetry/*/*/*/*"]
    effect: "allow"

  - name: "emergency-override"
    subjects: ["*.*.safety_officer.*"]
    actions: ["publish"]
    resources: ["mal/1/control/*/*/*/*"]
    effect: "allow"
    priority: 100  # Higher priority overrides other rules
```

### Policy Enforcement Points

1. **Message bus**: Subscribe/publish authorization
2. **MAL gateway**: Cross-domain message filtering
3. **Component input**: Inbound command validation
4. **Evidence plane**: Audit log generation

## Key Management

### Key Lifecycle

1. **Generation**: Hardware-backed or cryptographically secure RNG
2. **Distribution**: Secure channels (mTLS, sealed envelopes)
3. **Storage**: Encrypted at rest, protected in memory
4. **Rotation**: Automatic on schedule or usage threshold
5. **Revocation**: Certificate revocation lists (CRLs), OCSP
6. **Destruction**: Secure erasure from all storage

### Rotation Policy

Keys MUST rotate when:
- Scheduled interval reached (e.g., 90 days for signing keys)
- Usage threshold exceeded (e.g., 1M signatures)
- Security incident detected
- Administrative revocation requested

### Secret Storage

**Secrets MUST NEVER**:
- Appear in message payloads (use references instead)
- Be logged or printed
- Be stored in version control
- Be transmitted over unencrypted channels

**Secrets SHOULD**:
- Be fetched from secure vaults (HashiCorp Vault, AWS Secrets Manager)
- Use sealed envelope encryption
- Have access audit trails
- Support emergency revocation

## Access Control Lists (ACLs)

### Topic ACLs

```yaml
acls:
  - topic: "mal/1/control/BWB-Q100/AAA/flight_ctl/*"
    allow_publish:
      - "BWB-Q100.AAA.mission_planner.*"
      - "BWB-Q100.AAA.safety_officer.*"
    allow_subscribe:
      - "BWB-Q100.AAA.flight_ctl.*"
      - "BWB-Q100.AAA.telemetry_logger.*"

  - topic: "mal/1/telemetry/BWB-Q100/AAA/*"
    allow_publish:
      - "BWB-Q100.AAA.*"
    allow_subscribe:
      - "*.*.*.*"  # Anyone can read telemetry
```

## Security Event Logging

### Audit Events

Log all security-relevant events:
- Authentication success/failure
- Authorization denials
- Key rotations
- Policy changes
- Anomalous patterns (rate limiting, unusual access)

### Log Format

```json
{
  "event": "auth_failure",
  "timestamp": "2025-10-03T09:12:11.456Z",
  "subject": "unknown.AAA.rogue_component.instance_1",
  "action": "publish",
  "resource": "mal/1/control/BWB-Q100/AAA/flight_ctl/primary",
  "reason": "invalid_signature",
  "context": {
    "src_ip": "10.0.1.42",
    "key_id": "ed25519:QS:unknown:9999"
  }
}
```

## Compliance & Standards

- **NIST SP 800-53**: Security and Privacy Controls
- **DO-326A**: Airworthiness Security Process Specification
- **IEC 62443**: Industrial Automation and Control Systems Security
- **ISO/IEC 27001**: Information Security Management
- **EU 2021/821**: Export control compliance

## Security Testing

Required security tests:
1. **Penetration testing**: Quarterly by independent team
2. **Fuzzing**: Continuous message format fuzzing
3. **Replay tests**: Verify idempotency and nonce tracking
4. **Timing analysis**: Constant-time verification
5. **Key rotation drills**: Operational readiness

## Incident Response

On security incident:
1. **Contain**: Isolate affected components
2. **Analyze**: Forensic analysis of logs and evidence
3. **Remediate**: Apply patches, rotate keys
4. **Document**: Incident report with timeline
5. **Learn**: Update policies and tests

## References

- Master Whitepaper #2: MAL Technical Specification
- MAL-EEM Ethics & Policy Framework
- NIST Cryptographic Standards (FIPS 140-3)
- RFC 8032 (Ed25519)
- RFC 7539 (ChaCha20-Poly1305)
