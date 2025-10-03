# MAL Service Examples

This directory contains example MAL service configurations demonstrating the integration architecture defined in **Integration Whitepaper #2**.

## Examples

### 1. MAL-QS Example (`mal-qs-example.yaml`)

**Primordial State Management Service**

Demonstrates:
- State snapshot management with immutable storage
- Merkle-tree based versioning
- UTCS v5.0 evidence bundling
- Forensic audit level compliance

**Usage:**
```bash
# Validate against schema
python3 -c "
import jsonschema, yaml, json
with open('WHITEPAPERS/artifacts/schemas/integration/mal-qs.schema.json') as f:
    schema = json.load(f)
with open('WHITEPAPERS/artifacts/examples/mal-services/mal-qs-example.yaml') as f:
    config = yaml.safe_load(f)
jsonschema.validate(config, schema)
print('✅ Valid MAL-QS configuration')
"
```

### 2. MAL-CB Example (`mal-cb-example.yaml`)

**Classical Bit Solver Service**

Demonstrates:
- Deterministic computation with multiple solvers (IPOPT, CPLEX)
- Redundant computation validation
- DO-178C Level C compliance
- Aerodynamic optimization use case

**Key Features:**
- Multiple solver backends
- Convergence and accuracy tracking
- Solution validation interface

### 3. MAL-QB Example (`mal-qb-example.yaml`)

**Bit Cubic (Non-Quantum) Advisory Optimization Service**

Demonstrates:
- QUBO/Ising optimization methods
- **Advisory-only role** (not for safety-critical decisions)
- Safety predicates and fallback mechanisms
- Max age constraints (30s)
- Non-quantum backends (simulator, quantum-inspired)

**Critical Safety Notes:**
- QB is **advisory only** and **non-quantum**
- All solutions must pass `accept_predicates`
- Solutions must be validated by CB layer before use
- Solutions expire after `max_age_s`
- Fallback to CB solution required

### 4. Bridge Flow Example (`bridge-flow-example.yaml`)

**Complete Bridge Flow Configuration**

Demonstrates:
- Full bridge layer definitions (QS→FWD→UE→FE→CB→QB)
- Valid flow transitions
- UTCS integration
- Safety constraints

**Validation:**
```bash
python scripts/validate_bridge_flow.py WHITEPAPERS/artifacts/examples/mal-services/bridge-flow-example.yaml
```

## Bridge Semantics

### Layer Order (Canonical)

**QS → FWD → UE → FE → CB → QB**

| Layer | Name | Role | Properties |
|-------|------|------|------------|
| QS | Primordial | State management | immutable, versioned, signed |
| FWD | Forward Wave Dynamics | Prediction | probabilistic, time_bounded |
| UE | Unit Element | Execution | atomic, deterministic |
| FE | Federation Entanglement | Coordination | consensus_based, slo_governed |
| CB | Classical Bit | Computation | deterministic, validated, certified |
| QB | Bit Cubic | Advisory | advisory_only, safety_bounded, fallback_required |

### Valid Transitions

```
QS  → FWD, UE
FWD → UE, FE
UE  → FE, CB
FE  → CB, QB
CB  → QB
QB  → (terminal)
```

## Topic Examples

### Control Topics
```
map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB
map/1/control/BWB-Q100/AAA/QUBITS/QB/QB
map/1/control/BWB-Q100/FLEET/ELEMENTS/FE/FE
```

### Telemetry Topics
```
map/1/telemetry/BWB-Q100/AAA/SYSTEMS/SI/CB
map/1/telemetry/BWB-Q100/AAA/STATES/QS/QS
map/1/telemetry/BWB-Q100/AAA/WAVES/FWD/FWD
```

### Log Topics
```
map/1/log/BWB-Q100/AAA/STATES/QS/QS
```

### Health Topics
```
map/1/health/BWB-Q100
map/1/health/BWB-Q100/AAA
```

## Validation Tools

### Topic Hierarchy Validator

```bash
# Single topic
python scripts/validate_topic_hierarchy.py "map/1/control/BWB-Q100/AAA/SYSTEMS/SI/CB"

# Batch validation
python scripts/validate_topic_hierarchy.py --batch topics.txt
```

### Bridge Flow Validator

```bash
python scripts/validate_bridge_flow.py bridge-flow-example.yaml
```

### Schema Validator

```bash
pip install jsonschema pyyaml

python3 << 'EOF'
import jsonschema, yaml, json

# Load schema
with open('WHITEPAPERS/artifacts/schemas/integration/mal-cb.schema.json') as f:
    schema = json.load(f)

# Load config
with open('WHITEPAPERS/artifacts/examples/mal-services/mal-cb-example.yaml') as f:
    config = yaml.safe_load(f)

# Validate
try:
    jsonschema.validate(config, schema)
    print('✅ Configuration is valid')
except jsonschema.exceptions.ValidationError as e:
    print(f'❌ Validation error: {e.message}')
EOF
```

## Creating Your Own Service

1. **Choose the appropriate layer** based on your service's role:
   - QS for state management
   - FWD for prediction/forecasting
   - UE for atomic execution
   - FE for multi-party coordination
   - CB for deterministic computation
   - QB for advisory optimization

2. **Copy the example** that best matches your needs

3. **Customize the configuration**:
   - Update `service_id`, `version`, `description`
   - Define appropriate topics (subscribe/publish)
   - Configure layer-specific properties
   - Add UTCS requirements
   - Define interfaces

4. **Validate against schema**:
   ```bash
   python3 validate_config.py your-service.yaml
   ```

5. **Test with validators**:
   ```bash
   python scripts/validate_topic_hierarchy.py "your/topic"
   python scripts/validate_bridge_flow.py your-flow.yaml
   ```

## Common Patterns

### State Management (QS)
- Immutable storage
- Content-addressed versioning
- Signature requirements
- Audit trails

### Prediction (FWD)
- Time-bounded forecasts
- Confidence intervals
- Model versioning
- Ensemble methods

### Execution (UE)
- Idempotency keys
- Timeout bounds
- Rollback support
- Deterministic results

### Coordination (FE)
- Consensus algorithms
- SLO management
- Multi-party protocols
- Quorum requirements

### Computation (CB)
- Deterministic solvers
- Solution validation
- Performance metrics
- Certification compliance

### Optimization (QB)
- Advisory role only
- Safety predicates
- Fallback mechanisms
- Age constraints

## References

* [Integration Whitepaper #2](../INTEGRATION_WHITEPAPER_2.md)
* [Integration Guide](../INTEGRATION_GUIDE.md)
* [Schema Documentation](../../schemas/integration/README.md)
* [Master Whitepaper #1](../MASTER_WHITEPAPER_1.md)

## Support

* **Issues:** https://github.com/Robbbo-T/ASI-T2/issues
* **Documentation:** WHITEPAPERS/artifacts/INTEGRATION_GUIDE.md
* **Maintainer:** ASI-T Architecture Team

---

*Part of ASI-T2 Integration Architecture*  
*Version: 0.1.0*  
*Last Updated: 2025-10-03*
