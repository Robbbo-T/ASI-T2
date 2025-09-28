# Policy Manifests

Rego policy definitions for ethics, compliance, and governance validation in the AOA system.

## Available Policies

### ethics.rego
Core ethics and data residency policy for marine operations.

**Package**: `aoa.ethics`

**Policy Rules**:
1. **Marine Protection**: Compositions with marine-related intent and strict ethics must have `MARINE_PROTECTED=true`
2. **Data Residency**: All mission data must remain within EU jurisdiction
3. **Evidence Requirements**: UTCS and QS evidence anchoring is required for compliance

**Example Violations**:
```yaml
# This would be denied:
metadata:
  intent: "Assess marine habitat health..."
  flags:
    MARINE_PROTECTED: false  # ❌ Required for marine operations
  dataResidency: US         # ❌ Must be EU
```

## Policy Integration

Currently implemented as simple validation in `core/app.py`. Future integration will include:
- **OPA Integration**: Real-time Rego policy evaluation via REST API or WASM
- **Policy Versioning**: Support for multiple policy versions and rollback
- **Audit Logging**: Complete policy decision audit trail
- **Dynamic Policies**: Runtime policy updates without system restart

## Policy Structure

Rego policies follow standard Open Policy Agent format:
```rego
package aoa.ethics

deny[msg] {
  # Policy conditions
  condition1
  condition2
  msg := "Violation description"
}
```

## Testing Policies

Use the AOA CLI to test policy compliance:
```bash
python PRODUCTS/INFRANET/AOA/cli/aoactl.py policy test composition.yaml
```