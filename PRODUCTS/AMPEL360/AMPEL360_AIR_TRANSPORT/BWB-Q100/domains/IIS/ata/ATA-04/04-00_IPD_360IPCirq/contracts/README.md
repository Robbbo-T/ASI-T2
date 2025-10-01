# Contracts & Governance

This directory contains Interface Control Documents (ICDs), workflow definitions, and QS/UTCS anchoring.

## Structure

- **governance/** — Workflows, roles, approval steps (CI-2.31, CO-3.27, CO-3.28)
- **qis/** — QS/UTCS anchors (CO-3.29) — Quality sealing and provenance

## Interface Control Documents (ICDs)

ICDs define formal agreements between systems and teams:

### Internal ICDs
- **ICD-MAINT-001**: 360IPCirq ↔ Maintenance Systems
- **ICD-IETP-001**: 360IPCirq ↔ IETP Viewers
- **ICD-REPAIR-001**: 360IPCirq ↔ Repair Shop Portals
- **ICD-SPARES-001**: 360IPCirq ↔ Spare Parts Management
- **ICD-TRAIN-001**: 360IPCirq ↔ Training Systems

### External ICDs
- **ICD-PDM-IPC-001**: PDM/PLM ↔ 360IPCirq (Parts Catalog)
- **ICD-ENG-BOM-001**: Engineering ↔ 360IPCirq (Bill of Materials)
- **ICD-QA-EVID-001**: Quality Assurance ↔ 360IPCirq (Evidence)

Each ICD includes:
1. **Purpose & Scope**: What the interface covers
2. **Data Structures**: Message formats and schemas
3. **Transport**: Communication protocol and security
4. **Timing**: Cadence, latency requirements, SLOs
5. **Error Handling**: Retry logic, escalation
6. **Versioning**: Interface version management
7. **Change Control**: How interface changes are managed

## Governance (CI-2.31)

### Workflows

#### Change Request Workflow
1. **Submit**: Engineer creates change request
2. **Review**: Technical review by domain experts
3. **Impact Analysis**: Assess downstream effects
4. **MRB (if needed)**: Material Review Board evaluation
5. **Approval**: Authorized approval
6. **Implementation**: Controlled deployment
7. **Verification**: Post-deployment validation
8. **Close**: Final documentation and lessons learned

#### Deviation Workflow
1. **Identify**: Deviation from standard detected
2. **Document**: Deviation report created
3. **Assess**: Engineering assessment of impact
4. **Approve**: Authority approval or rejection
5. **Track**: Monitor deviation lifetime
6. **Resolve**: Return to standard or permanent change
7. **Close**: Documentation and lessons learned

#### Evidence Approval Workflow
1. **Capture**: Evidence collected during work
2. **Validate**: Schema and business rule validation
3. **Review**: Quality assurance review
4. **Seal**: QS/UTCS cryptographic sealing
5. **Archive**: Long-term retention
6. **Audit**: Periodic compliance audits

### Service Level Agreements (SLAs)

| Service | Target | Measurement |
|---------|--------|-------------|
| API Response Time | < 500ms (p95) | Application monitoring |
| Evidence Processing | < 30 min | End-to-end tracking |
| Change Approval | < 5 business days | Workflow system |
| PDM Sync Latency | < 1 hour | Data freshness checks |

## Roles & Permissions (CO-3.27)

### Role Definitions

**Engineer**
- **View**: All technical data
- **Edit**: Assigned work items
- **Approve**: None
- **Override**: None

**Lead Engineer**
- **View**: All technical data
- **Edit**: All work items in domain
- **Approve**: Standard changes
- **Override**: None

**Quality Assurance**
- **View**: All data + evidence packages
- **Edit**: QA records only
- **Approve**: Evidence packages, standard changes
- **Override**: None

**System Administrator**
- **View**: All data + system configuration
- **Edit**: All data + system configuration
- **Approve**: Standard and non-standard changes
- **Override**: With justification and logging

**MRB Member**
- **View**: All data + deviation reports
- **Edit**: MRB decisions only
- **Approve**: Non-standard changes, deviations
- **Override**: Major deviations with board approval

### Permission Scopes
- **Chapter**: ATA chapter level (e.g., ATA-04)
- **Figure**: IPD figure level
- **Item**: Individual part level
- **Task**: Specific procedure
- **Evidence**: Evidence package

## Approval Steps (CO-3.28)

Each workflow includes approval steps with:
- **Workflow ID**: Unique workflow identifier
- **Step Number**: Sequence in workflow
- **Role**: Required approver role
- **SLA**: Time limit for decision
- **Escalation**: Path if SLA breached

Example: Change Request Approval
```yaml
workflow_id: "WF-CHANGE-001"
steps:
  - step_no: 1
    role: "Lead Engineer"
    sla: "2 business days"
    escalation: "Engineering Manager"
  - step_no: 2
    role: "Quality Assurance"
    sla: "1 business day"
    escalation: "QA Manager"
  - step_no: 3
    role: "Configuration Manager"
    sla: "1 business day"
    escalation: "Chief Engineer"
```

## QS/UTCS Anchoring (CO-3.29)

Quality Sealing and Universal Traceability Configuration Sealing:

### Canonical Hash
- SHA-256 of normalized content
- Deterministic computation
- Version-independent where appropriate

### SBOM (Software Bill of Materials)
- Complete dependency list
- Version pins for all components
- License information
- Vulnerability status

### Signer
- Authorized signer identity
- Digital signature (RSA/ECDSA)
- Certificate chain validation
- Timestamp authority

### Provenance Chain
- Complete history of changes
- Actor identification
- Timestamp (RFC 3339 UTC)
- Evidence references
- Hash chain linking

### Ethics Guard (MAL-EEM)
- Multi-agent Alignment with Ethical Evaluation Matrix
- Automated ethical compliance checking
- Human-in-the-loop for critical decisions
- Audit trail of ethical assessments

### Bridge (CB→QB→UE→FE→FWD→QS)
- **CB**: Configuration Baseline
- **QB**: Quality Baseline
- **UE**: Unit Evidence
- **FE**: Functional Evidence
- **FWD**: Final Working Documentation
- **QS**: Quality Seal

## Compliance & Auditing

All governance activities are:
- **Logged**: Complete audit trail
- **Timestamped**: UTC timestamps for all events
- **Sealed**: Cryptographic integrity protection
- **Retained**: Per regulatory requirements
- **Auditable**: Regular compliance audits

---

*Part of 360IPCirq — Configuration controlled under UTCS/QS v5.0*
