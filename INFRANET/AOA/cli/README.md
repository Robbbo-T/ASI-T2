# AOA CLI Tools

Command-line interface for the INFRANET/AOA App-of-Apps system.

## aoactl.py

The primary CLI tool for interacting with the AOA system. Provides commands for:

- **Capability Management**: Publish capability manifests to the registry
- **Composition Orchestration**: Execute composition dry-runs and planning
- **Policy Validation**: Test policy compliance for compositions

### Usage

```bash
# Publish capabilities
python aoactl.py cap publish ../manifests/capabilities/gaia_sound.detect.yaml

# Run composition dry-run
python aoactl.py compose run ../manifests/compositions/mission.bwb100.sea.health.yaml --dry-run

# Test policy validation
python aoactl.py policy test ../manifests/compositions/mission.bwb100.sea.health.yaml
```

### Environment Variables

- `AOA_URL`: AOA server base URL (default: http://127.0.0.1:8000)

### Dependencies

- Python 3.9+
- requests
- PyYAML
- argparse (stdlib)