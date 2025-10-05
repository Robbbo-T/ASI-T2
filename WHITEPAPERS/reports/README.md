# BWB Certification Reports

This directory contains certification evidence and compliance tracking artifacts for the AMPEL360 BWB Q100 aircraft certification program under EASA CS-25.

## Contents

### Core Certification Artifacts

1. **[moc_matrix.csv](./moc_matrix.csv)** - Means of Compliance Matrix
   - Maps CS-25 requirements to evidence artifacts
   - Includes owner assignments and UTCS IDs
   - Status tracking for each requirement

2. **[compliance_statements.csv](./compliance_statements.csv)** - Compliance Statements Register
   - Detailed compliance claims per regulation paragraph
   - Evidence links and verification methods
   - Review status and approval tracking

3. **[open_issues.csv](./open_issues.csv)** - Open Issues and Risks Register
   - Active certification issues and risks
   - Owner assignments and target resolution dates
   - UTCS anchors for traceability

## Usage

### MoC Matrix

The Means of Compliance (MoC) matrix defines how each CS-25 requirement will be met:

- **Rule ID**: CS-25 paragraph reference (e.g., CS-25.301)
- **Subject**: Brief description of requirement
- **MoC Type**: Method of compliance (Analysis, Test, Inspection, SSA, etc.)
- **Evidence Artifact**: Path to evidence in UTCS/SBOM structure
- **Owner**: Domain responsible (AAA, PPP, IIS, CCC, etc.)
- **Status**: Current status (TBD, Planned, In Progress, Complete, Accepted)
- **UTCS ID**: Unique UTCS anchor for evidence traceability
- **Notes**: Additional information or special conditions

### Compliance Statements

Detailed compliance claims at the paragraph level:

- **Rule ID**: CS-25 paragraph reference
- **Paragraph**: Specific sub-paragraph if applicable
- **Statement**: Concise claim of compliance
- **Method**: Verification method
- **Evidence UTCS ID**: Link to specific evidence artifact
- **Status**: Planned, In Progress, Complete, Accepted
- **Reviewer**: Assigned reviewer
- **Date**: Review/approval date
- **Notes**: Special conditions or additional context

### Open Issues

Risk and issue tracking:

- **Issue ID**: Unique identifier (CERT-###)
- **Title**: Brief description
- **Description**: Detailed issue description
- **Category**: Safety, Software, Structures, Systems, Operations
- **Severity**: Critical, High, Medium, Low
- **Owner**: Responsible domain
- **Status**: Open, In Progress, Resolved, Closed
- **UTCS ID**: Traceability anchor
- **Opened Date**: Issue creation date
- **Target Resolution**: Sprint or date target
- **Notes**: Additional context

## Integration with UTCS

All artifacts reference UTCS IDs following the pattern:

```
UTCS-MI:v5.0:AMPEL360:BWB:Q100:<domain>:<topic>[:<subtopic>]
```

Examples:
- `UTCS-MI:v5.0:AMPEL360:BWB:Q100:AAA:loads`
- `UTCS-MI:v5.0:AMPEL360:BWB:Q100:PPP:hydrogen:safety`
- `UTCS-MI:v5.0:AMPEL360:BWB:Q100:IIS:safety:ssa`

## Workflow

1. **Planning Phase**
   - Populate MoC matrix with requirements
   - Assign owners and methods
   - Create initial compliance statements

2. **Execution Phase**
   - Generate evidence artifacts
   - Update status in MoC matrix
   - Complete compliance statements with evidence links
   - Track issues and risks

3. **Review Phase**
   - Independent review of compliance statements
   - Verification of evidence completeness
   - Resolution of open issues

4. **Acceptance Phase**
   - Regulator review
   - Address findings
   - Update status to "Accepted"

## CI Integration

These files are referenced by:
- `.github/workflows/validate-manifests.yml` - Schema validation
- `.github/workflows/sbom-attest.yml` - SBOM generation with compliance refs
- `.github/workflows/s1000d-checks.yml` - S1000D data module validation

## References

- **Master Whitepaper**: [MASTER_WHITEPAPER_5_BWB_CERTIFICATION.md](../MASTER_WHITEPAPER_5_BWB_CERTIFICATION.md)
- **Safety Case**: [ASI_GSN_Safety_Case.gsn](../ASI_GSN_Safety_Case.gsn)
- **Policy**: [ASI_Policy.rego](../ASI_Policy.rego)
- **Product README**: [BWB-Q100 README](../../PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/README.md)

## Governance

- **Chief Engineer**: Overall certification plan and strategy
- **Safety Lead**: ARP4761 artifacts and DAL allocations
- **Systems Lead**: ARP4754A flow and ICDs
- **Hydrogen Lead**: CQH PPP safety and special conditions
- **Flight Test Lead**: Test readiness and compliance demonstration
- **Documentation Lead**: S1000D ATA and compliance statements
- **CI Stewards**: UTCS Verify SBOM badges and policy gates

---

*Part of the IDEALE-EU TFA profile certification evidence package*
