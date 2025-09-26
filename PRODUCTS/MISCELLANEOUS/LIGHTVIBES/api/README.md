# LIGHTVIBES API

**FastAPI implementation of the Quantum Micropulse Keying (QMK) control plane for GAIA-DS2.**

This API provides the core endpoints for establishing quantum key distribution sessions and retrieving ephemeral cryptographic keys.

## Overview

The LIGHTVIBES API implements a QKD-inspired micropulse key service with the following capabilities:

- **Session Management**: Create QMK sessions with configurable security policies
- **Key Distribution**: Retrieve one-time-use ephemeral keys sealed for HSM/TEE environments
- **Quantum Health Monitoring**: Real-time QBER monitoring with automatic fallback to PQC
- **Evidence Integration**: Full UTCS/QS evidence anchoring for compliance and audit

## API Endpoints

### POST /lightvibes/session

Creates a new QMK session between peers.

**Request Body:**
```json
{
  "peer_id": "string",
  "policy": {
    "min_keybits": 256,
    "ttl_s": 120
  },
  "fallback": "PQC"
}
```

**Response (201):**
```json
{
  "session_id": "string",
  "key_ref": "string", 
  "health": {
    "qber": 0.03,
    "rate_bps": 2000
  },
  "mode": "QMK"
}
```

### GET /lightvibes/key/{key_ref}

Retrieves an ephemeral key (one-time use only).

**Response (200):**
```json
{
  "key_ref": "string",
  "key_sealed": "string",
  "ttl_s": 60,
  "mode": "QMK"
}
```

**Response (404):** Key already consumed or expired

## Files

- **`server.py`**: FastAPI application with endpoint implementations
- **`openapi.yaml`**: OpenAPI 3.1 specification
- **`__init__.py`**: Python package initialization

## Development

### Running the Server

```bash
# From repository root
uvicorn LIGHTVIBES.api.server:app --reload --host 127.0.0.1 --port 8000
```

### Environment Variables

Configure via `LIGHTVIBES/.env.example`:

```bash
LIGHTVIBES_QBER_THRESHOLD=0.08
LIGHTVIBES_DEFAULT_TTL_S=120
```

### Testing

The API includes comprehensive test coverage via GitHub Actions. See `.github/workflows/lightvibes_validation.yml` for validation pipeline.

## Security Model

### Quantum Channel Monitoring

- **QBER Threshold**: Monitors quantum bit error rate; falls back to PQC when exceeded
- **Tamper Detection**: Automatic channel quarantine on tampering evidence
- **Evidence Logging**: All operations logged via UTCS/QS for audit trail

### Key Management

- **Zero Standing Secrets**: No static keys stored at rest
- **One-Time Use**: Keys consumed after single retrieval
- **HSM/TEE Sealing**: Keys sealed for hardware security modules (production)

### Compliance

- **MAL-EEM Ethics Guard**: Enforced at API gateway level
- **UTCS/QS Evidence**: Mandatory evidence anchoring for all operations
- **Audit Trail**: Immutable logging of all key operations

## Integration Points

### UTCS/QS Evidence

The API emits evidence events for:
- Session creation with QBER/rate metrics
- Key generation and sealing
- Key consumption events
- Mode transitions (QMK ↔ PQC)

### Hardware Integration

Production deployment requires:
- **Quantum Photonics Stack**: For QBER measurement and pulse generation
- **HSM/TEE Integration**: For hardware key sealing
- **PQC KEM Module**: For fallback cryptography

---

*Part of GAIA-DS2 LIGHTVIBES Quantum Micropulse Keying system*