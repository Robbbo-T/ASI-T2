# Interfaces & Integrations

This directory contains API definitions, PDM/PLM adapters, and IETP export configurations.

## Structure

- **api/** — API endpoint configs (CO-3.25) — RESTful API definitions
- **pdm_plm/** — PDM/PLM adapters (CI-2.27) — Product data management integrations
- **ietp/** — IETP package references (CO-3.30) — Interactive electronic technical publications

## API Integration

The 360IPCirq system exposes RESTful APIs for:

### Query Operations
- **GET /api/v2/ipd/items** — Query IPD items by part number, figure, etc.
- **GET /api/v2/irq/tuples** — Query interchangeability rules
- **POST /api/v2/effectivity/check** — Check effectivity for given MSN/options
- **GET /api/v2/tasks/removal** — Get removal task procedures
- **GET /api/v2/tasks/installation** — Get installation task procedures

### Data Submission
- **POST /api/v2/evidence/submit** — Submit evidence packages
- **POST /api/v2/units/state** — Update serialized unit state
- **POST /api/v2/provenance/event** — Log provenance events

### Configuration
- Endpoint: Path and HTTP verb
- Schema: Reference to validation schema
- Auth Scope: Required OAuth2 scope
- Rate Limit: Requests per hour/minute

See [routing.manifest.yaml](../io/routing.manifest.yaml) for complete API specifications.

## PDM/PLM Integration (CI-2.27)

Bidirectional synchronization with Product Data Management systems:

### From PDM/PLM (Upstream)
- Part master data
- Bill of Materials (BOM)
- Engineering changes (ECO/ECN)
- Configuration baselines
- Drawing releases

### To PDM/PLM (Downstream)
- As-maintained configuration
- Serialized unit states
- Repair history
- Evidence packages
- Quality records

### Adapter Architecture
- **Pull Mode**: Scheduled polling of PDM/PLM
- **Push Mode**: Event-driven updates from PDM/PLM
- **Transform Layer**: Data mapping and validation
- **Audit Log**: Complete transaction history

## IETP Export (CO-3.30)

Interactive Electronic Technical Publication packages for viewer systems:

### Export Formats
- **S1000D XML** — Structured technical content
- **SGML** — Legacy format compatibility
- **HTML5** — Web-based viewers
- **PDF** — Static documentation

### Package Contents
1. **IPD Figures** — Exploded view graphics (ICN format)
2. **Part Lists** — Item callouts with part numbers
3. **Task Procedures** — Removal/installation steps
4. **Tool References** — Required tooling with specifications
5. **Material References** — Materials and consumables
6. **Safety Information** — Warnings, cautions, notes
7. **Evidence Forms** — Blank QA forms for completion

### Effectivity Filtering
Packages are filtered by:
- Aircraft type and variant
- MSN or block number
- Option codes
- Modification status
- Software version

### Localization
- Multi-language support
- Unit system conversion (SI/Imperial)
- Region-specific regulations
- Local maintenance practices

### Distribution
- **Download URI**: Direct download link
- **Checksum**: SHA-256 for integrity verification
- **Signature**: Digital signature for authenticity
- **Metadata**: Version, date, applicability

## Security & Access Control

All interfaces enforce:
- **Authentication**: OAuth2 + mTLS
- **Authorization**: Role-based access control (RBAC)
- **Rate Limiting**: Protection against abuse
- **Audit Logging**: Complete access history
- **Encryption**: TLS 1.3 for transport, at-rest encryption

## Monitoring & Observability

Interface health is monitored via:
- **Health Checks**: /health endpoint for each service
- **Metrics**: Request rate, latency, error rate
- **Alerts**: Automatic notification on degradation
- **Tracing**: Distributed tracing for debugging

---

*Part of 360IPCirq — Configuration controlled under UTCS/QS v5.0*
