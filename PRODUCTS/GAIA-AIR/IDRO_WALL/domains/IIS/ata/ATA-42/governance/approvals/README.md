# Approvals Register

This directory contains structured approval records and sign-offs for ATA-42 IMA configuration changes.

## Files

- **register.yaml** — Structured list of all approvals with metadata (approver, date, artifact hash, decision)
- **decision_log.md** — Human-readable narrative of key decisions and their rationale

## Approval Process

1. RFC submitted with technical proposal
2. Safety/security impact analysis conducted
3. Stakeholder review (System Eng, Safety, Security, MAL-EEM lead)
4. Decision recorded with artifact hashes
5. QS anchor generated for traceability

## Example Entry

```yaml
- id: APPR-ATA42-001
  date: 2025-10-15
  artifact: os/configuration/a653/partition.xml
  artifact_hash: sha256:abc123...
  decision: APPROVED
  approver: J.Smith (System Lead)
  rationale: "Budget increase validated via timing analysis"
```
