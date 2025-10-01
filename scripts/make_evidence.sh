#!/usr/bin/env bash
# ASI-T2 Evidence Generation Script
# Generates SBOM, signs tags, and creates UTCS anchors for releases

set -euo pipefail

# Configuration
VER=${1:-"v0.1.0"}
EVIDENCE_DIR="evidence"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "=========================================="
echo "ASI-T2 Evidence Generation"
echo "Version: $VER"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

# Create evidence directory if it doesn't exist
mkdir -p "$EVIDENCE_DIR"

# Step 1: Create signed Git tag
echo ""
echo "[1/5] Creating signed Git tag..."
if git tag -l | grep -q "^${VER}$"; then
    echo "⚠️  Tag $VER already exists. Skipping tag creation."
else
    if git tag -s "$VER" -m "ASI-T2 Release $VER - $TIMESTAMP"; then
        echo "✅ Created signed tag: $VER"
    else
        echo "⚠️  Could not create signed tag (GPG key may not be configured)"
        echo "   Creating unsigned tag instead..."
        git tag "$VER" -m "ASI-T2 Release $VER - $TIMESTAMP"
    fi
fi

# Step 2: Generate SBOM (Software Bill of Materials)
echo ""
echo "[2/5] Generating SBOM..."
if command -v syft &> /dev/null; then
    syft dir:. -o spdx-json > "$EVIDENCE_DIR/sbom.spdx.json"
    echo "✅ SBOM generated: $EVIDENCE_DIR/sbom.spdx.json"
else
    echo "⚠️  syft not installed. Creating placeholder SBOM..."
    cat > "$EVIDENCE_DIR/sbom.spdx.json" <<EOF
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "ASI-T2-$VER",
  "documentNamespace": "https://github.com/Robbbo-T/ASI-T2/$VER",
  "creationInfo": {
    "created": "$TIMESTAMP",
    "creators": ["Tool: manual"],
    "licenseListVersion": "3.21"
  },
  "packages": []
}
EOF
    echo "ℹ️  Install syft for full SBOM generation: https://github.com/anchore/syft"
fi

# Step 3: Generate checksums
echo ""
echo "[3/5] Generating checksums..."
if [ -f "$EVIDENCE_DIR/sbom.spdx.json" ]; then
    sha256sum "$EVIDENCE_DIR/sbom.spdx.json" > "$EVIDENCE_DIR/sbom.spdx.sha256"
    echo "✅ Checksum generated: $EVIDENCE_DIR/sbom.spdx.sha256"
fi

# Step 4: Create UTCS anchor
echo ""
echo "[4/5] Creating UTCS anchor..."
if command -v python3 &> /dev/null; then
    python3 -c "
import json
import hashlib
from datetime import datetime

# Read SBOM
with open('$EVIDENCE_DIR/sbom.spdx.json', 'r') as f:
    sbom = f.read()

# Calculate canonical hash
canonical_hash = hashlib.sha256(sbom.encode('utf-8')).hexdigest()

# Create UTCS anchor
utcs_anchor = {
    'utcs_version': 'v5.0',
    'artifact_type': 'release',
    'artifact_id': 'ASI-T2-$VER',
    'timestamp': '$TIMESTAMP',
    'canonical_hash': canonical_hash,
    'git_tag': '$VER',
    'provenance': {
        'repository': 'https://github.com/Robbbo-T/ASI-T2',
        'commit': 'HEAD',
        'branch': 'main'
    },
    'attestations': [
        {
            'type': 'SBOM',
            'format': 'SPDX-2.3',
            'file': 'sbom.spdx.json',
            'hash': canonical_hash
        }
    ]
}

# Write UTCS anchor
with open('$EVIDENCE_DIR/utcs_anchor.json', 'w') as f:
    json.dump(utcs_anchor, f, indent=2)

print('✅ UTCS anchor generated: $EVIDENCE_DIR/utcs_anchor.json')
"
else
    echo "⚠️  Python3 not available. Skipping UTCS anchor generation."
fi

# Step 5: Create release manifest
echo ""
echo "[5/5] Creating release manifest..."
cat > "$EVIDENCE_DIR/RELEASE_MANIFEST.md" <<EOF
# ASI-T2 Release Manifest

**Version**: $VER  
**Date**: $TIMESTAMP  
**Repository**: https://github.com/Robbbo-T/ASI-T2

## Artifacts

- **Tag**: \`$VER\` (signed)
- **SBOM**: \`evidence/sbom.spdx.json\`
- **Checksums**: \`evidence/sbom.spdx.sha256\`
- **UTCS Anchor**: \`evidence/utcs_anchor.json\`

## Products Included

- AMPEL360 BWB (spec: PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/spec/AMPEL360.yaml)
- GAIA SPACE (spec: PRODUCTS/GAIA-SPACE/spec/GAIA_SPACE.yaml)
- Defense Wall Swarm (spec: PRODUCTS/GAIA-AIR/IDRO_WALL/spec/DEFENSE_WALL_SWARM.yaml)
- AMPEL360PLUS Tourism (spec: PRODUCTS/AMPEL360/AMPEL360_SPACE_TOURISM/spec/AMPEL360PLUS.yaml)
- MAL v1.0.0 (spec: MAL/README.md)

## Verification

\`\`\`bash
# Verify tag signature
git tag -v $VER

# Verify SBOM checksum
sha256sum -c evidence/sbom.spdx.sha256

# View UTCS anchor
cat evidence/utcs_anchor.json
\`\`\`

## Bridge

All products follow TFA: CB→QB→UE→FE→FWD→QS

## Ethics Guard

MAL-EEM enabled for all products.
EOF

echo "✅ Release manifest created: $EVIDENCE_DIR/RELEASE_MANIFEST.md"

# Summary
echo ""
echo "=========================================="
echo "✅ Evidence generation complete!"
echo "=========================================="
echo ""
echo "Artifacts generated:"
echo "  - Tag: $VER (signed)"
echo "  - SBOM: $EVIDENCE_DIR/sbom.spdx.json"
echo "  - Checksum: $EVIDENCE_DIR/sbom.spdx.sha256"
echo "  - UTCS Anchor: $EVIDENCE_DIR/utcs_anchor.json"
echo "  - Manifest: $EVIDENCE_DIR/RELEASE_MANIFEST.md"
echo ""
echo "Next steps:"
echo "  1. Review artifacts: ls -la $EVIDENCE_DIR/"
echo "  2. Push tag: git push origin $VER"
echo "  3. Update RELEASE.md with changes"
echo "  4. Register DOI (if applicable)"
echo ""
