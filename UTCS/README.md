# UTCS - CXP (Context eXchange Points)

This directory contains machine-readable context for ASI-T2 repository, enabling structured knowledge exchange with other repositories.

## Files

### context.manifest.json
**Purpose**: Repository metadata, interfaces, and dependencies

**Schema**: `context.schema.json`

**Contents**:
- Repository information (name, URL, license, topics)
- Canon references (GENESIS, FLOW, UTCS, PAx, DOMAINS)
- Lifecycle Level Context (LLC) definitions
- Interface exports and imports
- Dependency declarations (internal and external)
- Provenance information (hash, timestamp, generator)

**Used by**: 
- `cxp-publish` workflow for validation and stamping
- External repositories for context consumption

### context.schema.json
**Purpose**: JSON Schema for validating context.manifest.json

**Specification**: JSON Schema Draft 2020-12 compatible

**Used by**: 
- GitHub Actions workflow `cardinalby/schema-validator-action`
- Local validation tools

### links.map.json
**Purpose**: Track inbound and outbound relationships

**Structure**:
- `outbound`: Links we expose to others (manifest, docs)
- `inbound`: Links we consume from others (upstream manifests)

**Updated by**:
- Manually when adding new exports
- `cxp-consume` workflow when ingesting external context

## Workflows

### Publishing Context (Outbound)
Automatic on push to main via `.github/workflows/cxp-publish.yml`:
1. Generates SBOM with anchore/sbom-action
2. Stamps manifest with commit hash and timestamp
3. Validates against context.schema.json
4. Credits TeknIA Tokens (TT) reward
5. Uploads artifacts

### Consuming Context (Inbound)
Manual trigger via `.github/workflows/cxp-consume.yml`:
1. Fetches remote manifest URL
2. Validates against context.schema.json
3. Updates links.map.json
4. Charges TeknIA Tokens (TT) cost
5. Uploads updated map

## Usage

### Check Current Manifest
```bash
jq . UTCS/context.manifest.json
```

### Validate Locally
```bash
# Install dependencies
pip install jsonschema

# Validate
python -c "
import json, jsonschema
schema = json.load(open('UTCS/context.schema.json'))
manifest = json.load(open('UTCS/context.manifest.json'))
jsonschema.validate(manifest, schema)
print('✓ Valid')
"
```

### Add New Export
Edit `context.manifest.json`:
```json
{
  "interfaces": {
    "exports": [
      {
        "name": "cxp:new-export",
        "path": "docs/NEW_DOCUMENT.md",
        "format": "markdown"
      }
    ]
  }
}
```

### View Links Map
```bash
jq . UTCS/links.map.json
```

## Integration

### With UTCS_BUNDLE/
This CXP structure complements the existing UTCS_BUNDLE/ evidence system:
- **UTCS_BUNDLE/**: Full evidence artifacts (schemas, SBOMs, signatures)
- **UTCS/**: Lightweight context manifest for cross-repo exchange

### With TeknIA TOKENS
Context operations trigger TT transactions:
- **Publish**: +3 TT reward to publisher
- **Consume**: -2 TT cost from treasury

See `docs/TOKENS.md` for details.

## Decision Points

### Q: What should I export?
**A**: Export interfaces that other repos might need:
- Architecture documentation
- Interface contracts
- SBOM for dependency tracking
- Schemas for data exchange

### Q: When to update the manifest?
**A**: Update when:
- Adding/removing interfaces
- Changing dependencies
- Updating architecture
- Releasing major versions

### Q: How to version the manifest?
**A**: Follow semver in manifest `version` field:
- MAJOR: Breaking interface changes
- MINOR: New exports/features
- PATCH: Bug fixes, clarifications

## See Also

- [docs/GENESIS.md](../docs/GENESIS.md) - Canon reference
- [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md) - System architecture
- [docs/INTERFACES.md](../docs/INTERFACES.md) - CXP specifications
- [docs/TOKENS.md](../docs/TOKENS.md) - TeknIA TOKENS rules
- [UTCS_BUNDLE/](../UTCS_BUNDLE/) - Full evidence system
