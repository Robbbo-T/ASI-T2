# AOA Data Schemas

Schema definitions for data formats used in the PRODUCTS/INFRANET/AOA system.

## Schema Files

### detections.schema.json
JSON Schema for marine species detection data output from GAIA-SOUND capabilities.

**Structure**:
```json
{
  "detections": [
    {
      "species": "string",
      "confidence": 0.0-1.0,
      "timestamp_utc": "ISO 8601 datetime",
      "location": {
        "lat": number,
        "lon": number
      }
    }
  ]
}
```

**Usage**: Validates detection outputs from acoustic analysis capabilities and inputs to compliance reporting.

### acoustic.proto
Protocol Buffers schema for acoustic data frames used in marine audio processing.

**Structure**:
```protobuf
message AcousticFrame {
  string stream_id = 1;
  uint64 timestamp_utc_ms = 2;
  bytes payload_pcm = 3;     // Raw or compressed audio
  uint32 sample_rate_hz = 4;
  uint32 channels = 5;
}
```

**Usage**: Defines the interface for audio data flowing between acoustic sensors and processing capabilities.

## Schema Validation

Schemas are referenced in capability manifests for input/output validation:
```yaml
spec:
  inputs:
    - name: audio_stream
      schemaRef: schemas/acoustic.proto#AcousticFrame
  outputs:
    - name: detections
      schemaRef: schemas/detections.schema.json
```

## Future Schemas

Additional schemas will be added for:
- Beamforming parameters and optimization results
- Compliance report formats (EER-SEA-2025)
- QKM session and key exchange formats
- Evidence and attestation envelope structures