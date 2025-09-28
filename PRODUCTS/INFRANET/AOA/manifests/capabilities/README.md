# Capability Manifests

YAML definitions of capabilities that can be composed into missions through the AOA system.

## Available Capabilities

### gaia_sound.detect.yaml
Marine species acoustic detection capability from GAIA-SEA/GAIA-SOUND.
- **Inputs**: Audio streams (acoustic.proto#AcousticFrame)
- **Outputs**: Species detections (detections.schema.json)
- **SLOs**: 120ms p95 latency, 99.5% availability
- **Runtime**: ROS2 DDS adapter

### qaim_beamforming.yaml
Quantum-inspired beamforming optimization from QAIM/OPTIMIZERS.
- **Inputs**: Signal input (acoustic.proto#AcousticFrame)
- **Outputs**: Optimized beam parameters
- **SLOs**: 50ms p95 latency, 99.9% availability
- **Runtime**: ROS2 DDS adapter

### infranet_compliance.yaml
Environmental compliance reporting from INFRANET/COMPLIANCE.
- **Inputs**: Detection data (detections.schema.json)
- **Outputs**: Compliance reports
- **SLOs**: 200ms p95 latency, 99.5% availability
- **Runtime**: HTTP adapter

### lightvibes_qkm.yaml
Quantum Micropulse Keying service from MISCELLANEOUS/LIGHTVIBES_QKM.
- **Inputs**: Session requests
- **Outputs**: Ephemeral cryptographic keys
- **SLOs**: 100ms p95 latency, 99.9% availability
- **Runtime**: HTTP adapter

## Manifest Structure

Each capability manifest follows the AOA v1 specification:
```yaml
apiVersion: aoa.v1
kind: Capability
metadata:
  id: cap.example.service
  owner: PRODUCT/COMPONENT
spec:
  summary: Brief description
  inputs: [...]
  outputs: [...]
  slos: {...}
  policies: {...}
  runtime: {...}
```