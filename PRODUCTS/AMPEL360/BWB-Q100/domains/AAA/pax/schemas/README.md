---
id: ASIT-BWBQ100-AAA-PAX-SCHEMAS-OV-0001
rev: 0
project: PRODUCTS/AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/schemas/README.md
llc: SYSTEMS
title: "PAx Schemas — Packaging (AAA Domain, BWB-Q100)"
configuration: baseline
classification: "INTERNAL–EVIDENCE-REQUIRED"
version: "0.1.0"
release_date: 2025-09-26
maintainer: "ASI-T Architecture Team"
licenses:
  docs: "CC-BY-4.0"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
provenance:
  policy_hash: "sha256:TBD"
  model_sha: "sha256:TBD"
  data_manifest_hash: "sha256:TBD"
  operator_id: "UTCS:OP:copilot-gen"
---

# PAx Schemas — Packaging

Schema definitions for **BWB-Q100 / AAA** packaging & containerization. These schemas validate PAx manifests, enforce metadata, and encode QS/UTCS evidence requirements.

---

## Routing

- Up one level (PAx): [`../`](../)  
- On-Board manifests: [`../OB/manifests/`](../OB/manifests/)  
- Off-Board OCI descriptors: [`../OFF/oci/`](../OFF/oci/)  
- PAx validation scripts: [`../scripts/`](../scripts/)  
- Product index: [`../../../../../../..`](../../../../../../..) → `PRODUCTS/AMPEL360/BWB-Q100/`

> **Link policy:** All links are relative; folder links end with `/`, file links include the filename.

---

## Contents & Registry

This directory currently contains:

| File | Purpose | Draft | $id (suggested) |
|---|---|---:|---|
| [`package.schema.json`](./package.schema.json) | Top-level PAx package/manifest schema (common for OB/OFF) | 2020-12 | `urn:asi-t:pax:schemas:package:0-1-0` |

> Add new schemas here following the naming pattern `name.schema.json`. Keep one **registry table** entry per schema with suggested `$id` URN.

---

## Schema Structure

### Evidence Block Requirements

All PAx manifests must include an `evidence` block with:

```json
{
  "evidence": {
    "canonical_hash": "sha256:...",
    "sbom": {
      "path": "relative/path/to/sbom.spdx",
      "hash": "sha256:..."
    },
    "signatures": [
      {
        "path": "relative/path/to/signature.sig",
        "type": "cosign|in-toto|x509",
        "keyid": "..."
      }
    ],
    "security_policy_id": "policy-identifier"
  }
}
```

### Validation Workflow

1. **JSON Schema Draft 2020-12** validation using [`../scripts/validate_pax.py`](../scripts/validate_pax.py)
2. **Evidence field completeness** check (all required fields present)
3. **Hash pattern validation** (`sha256:` prefix + 64 hex chars)
4. **File reference validation** (all referenced files exist)

---

## Integration

### CI/CD Pipeline

```bash
# Validate all manifests in OB/OFF subdirectories
python ../scripts/validate_pax.py ../OB/manifests/*.yaml ../OFF/oci/*.yaml
```

### Development Workflow

1. Create manifest file (JSON or YAML)
2. Include required `evidence` block
3. Reference SBOM and signature files
4. Run validation script before commit
5. CI pipeline validates on PR/merge

---

## Quality Standards

- **SBOM mandatory**: SPDX/CycloneDX format required
- **Digital signatures**: sigstore/cosign, in-toto attestations, SLSA-L3 compliance
- **UTCS traceability**: canonical_hash links to configuration baseline
- **File integrity**: All referenced artifacts must exist and match hashes