# Composition Manifests

YAML definitions of mission compositions that orchestrate multiple capabilities through the AOA system.

## Available Compositions

### mission.bwb100.sea.health.yaml
BWB-Q100 marine habitat health assessment mission composition.

**Mission Intent**: Assess marine habitat health during BWB-Q100 coastal approach

**Capabilities Used**:
- `cap.gaia_sound.detect` (as detect_species) - Marine acoustic detection
- `cap.qaim.optimize_beamforming` - Beamforming optimization (after detection)
- `cap.infranet.compliance_report` - Environmental compliance reporting (after detection)

**Policy Requirements**:
- Ethics: MAL-EEM:strict with MARINE_PROTECTED=true
- Data Residency: EU
- Evidence: UTCS:required, QS:required

**Execution Flow**:
1. `detect_species` (GAIA-SOUND acoustic detection)
2. Parallel execution:
   - `cap.qaim.optimize_beamforming` (power optimization)
   - `cap.infranet.compliance_report` (EER-SEA-2025 standard)

## Composition Structure

Each composition manifest follows the AOA v1 specification:
```yaml
apiVersion: aoa.v1
kind: Composition
metadata:
  id: cmp.example.mission
  intent: "Mission description"
  bridge: "CB→QB→UE→FE→FWD→QS"
  flags: {...}
  dataResidency: EU
spec:
  graph:
    - use: cap.example.service
      as: alias_name
      with: {...}
      after: [dependency_list]
  constraints:
    fabrics: [...]
    ethics: "policy_level"
    evidence: "requirements"
```

## Execution Planning

The AOA system performs:
1. **Dependency Resolution**: Validates all capabilities exist in registry
2. **Topological Sorting**: Orders execution based on 'after' dependencies
3. **Policy Validation**: Enforces ethics and data residency requirements
4. **Evidence Generation**: Creates UTCS/QS anchors for compliance tracking