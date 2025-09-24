---
id: AAA-PAX-OV-0001
project: AMPEL360/BWB-Q100
artifact: PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/README.md
llc: SYSTEMS
classification: INTERNAL–EVIDENCE-REQUIRED
version: 0.1.0
release_date: "2025-01-23"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
utcs_mi: v5.0
canonical_hash: "TBD"
---

# PAx — Packaging & Applications (on-board / off-board)

**Propósito:** transformar salidas de **CAx/QOx** en **paquetes desplegables** con **SBOM**, **firmas**, y **evidencia UTCS/QS**:
- **On-Board (OB):** particiones **ARINC 653/IMA**, A661 CDS, redes **A664/AFDX**, puertos A429.
- **Off-Board (OFF):** imágenes **OCI** (edge/cloud/ground), servicios EFB/MRO/DT/QAUDIT.

**Entradas:** `domains/.../cax/*` y `domains/.../qox/*`  
**Salidas:** paquetes firmados + **manifiestos PAx** + SBOM + anclajes QS.

## Estructura

```
pax/
├─ OB/ # On-Board
│ ├─ manifests/ # Manifiestos de partición ARINC653, A661, etc.
│ ├─ artifacts/ # Binarios/particiones resultantes (no versionar si son grandes)
│ ├─ sbom/ # SPDX/CycloneDX
│ └─ certificates/ # Firmas (cosign/in-toto), cadenas X.509
├─ OFF/ # Off-Board (OCI/edge/cloud)
│ ├─ oci/ # Descriptores de imagen/attestations
│ ├─ services/ # Charts/compose/kustomize (si aplica)
│ └─ sbom/ # SPDX/CycloneDX
├─ schemas/ # Esquemas JSON de manifiestos PAx
└─ scripts/ # Validadores/linters PAx
```

## Política mínima
- **SBOM obligatorio** (SPDX/CycloneDX) para OB/OFF.
- **Firmas/attestations** (sigstore/cosign, in-toto, SLSA-L3 objetivo).
- **Trazabilidad UTCS**: cada manifest incluye `canonical_hash` y ruta QS.
- **Seguridad**: principios de mínimo privilegio (OFF: `readOnlyRootFilesystem`, `runAsNonRoot`; OB: particiones con límites de CPU/mem y HM definido).

## Rutas QS recomendadas
- QS de producto: `PRODUCTS/AMPEL360/BWB-Q100/QS/`
- Colocar allí manifiestos firmados y hashes de release.