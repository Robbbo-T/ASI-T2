# ASI-T2 App-of-Apps (AoA)

Meta-application that composes, governs, and orchestrates capabilities across products.
This MVP provides:
- Capability **Registry** (publish/list)
- **Composer** (dry-run planner)
- **Policy** gate (ethics/data residency stub)
- **Evidence** envelope (UTCS/QS anchor stub)
- CLI (`aoactl`) to publish/run

### Run (dev)
uvicorn INFRANET.AOA.core.app:app --reload

### CLI examples
python INFRANET/AOA/cli/aoactl.py cap publish INFRANET/AOA/manifests/capabilities/gaia_sound.detect.yaml
python INFRANET/AOA/cli/aoactl.py compose run INFRANET/AOA/manifests/compositions/mission.bwb100.sea.health.yaml --dry-run
python INFRANET/AOA/cli/aoactl.py policy test INFRANET/AOA/manifests/policies/ethics.rego