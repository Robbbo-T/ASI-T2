---
id: ASIT2-OPTIME-MARK
project: ASI-T2
artifact: OPTIME Mark Specification
classification: PUBLIC-DRAFT
version: 0.1.0
release_date: "2025-10-04"
maintainer: "ASI-T Architecture Team"
bridge: "CB→QB→UE→FE→FWD→QS"
ethics_guard: MAL-EEM
canonical_hash: pending
---

# OPTIME — Optimised Policies for Technology Instructions Execution

**Purpose.** OPTIME is a lightweight assurance **mark** for any ASI-T2 artifact (code, service, workflow, doc) that executes "instructions". It guarantees: (1) policy-as-code gating, (2) evidence-on-output, (3) human-in-the-loop for consequential actions, (4) export/privacy compliance, and (5) immutable audit via QS/UTCS — while measuring and minimizing overhead ("optimised").

## Levels
- **OPTIME-Ready (L1):** Policies in place; tests pass; evidence attached; QS logging enabled.
- **OPTIME-Verified (L2):** As L1 + red-team suite, perf budget met, external review recorded.
- **OPTIME-Critical (L3):** As L2 + regulator-witnessed tests or accredited third-party audit.

## Minimal Criteria (checklist)
1. **Deny-by-default** OPA/Rego gate for instruction execution.
2. **Boundaries enforced** (no live control; no uncertified change).
3. **HITL required** for `risk == "consequential"`.
4. **Evidence weave** present in every response (sources, calc, mapping).
5. **QS state** snapshot on exec + UTCS anchor per release.
6. **Export/privacy** filters active; pointers-only for controlled content.
7. **Perf budget** documented (≤ X% added latency at p95).
8. **Reproducible** CI with SBOM + SLSA attestations.
9. **Red-team tests** (L2+) included in CI.
10. **Badge + metadata** present in artifact.

## How to claim (front-matter)
```yaml
marks:
  - name: OPTIME
    level: L2
    policy_pkg: data.asi.optime
    evidence: true
    qs_anchor: required
```

## Badge

```markdown
[![OPTIME](https://img.shields.io/badge/OPTIME-L2_verified-0e7c86)](./OPTIME_MARK.md)
```

## Rego stub (enforce essentials)

```rego
package asi.optime

default allow := false
default deny := true

risk := input.meta.risk  # "informational" | "consequential"
evidence_ok { input.evidence.summary; input.evidence.sources }
qs_ok       { input.qs.capture == true }

hitl_ok {
  risk == "consequential"
  some a
  a := input.approvals[_]
  a.role == "human_approver"
  a.status == "approved"
}

allow {
  input.policy_version >= "1.0.0"
  evidence_ok
  qs_ok
  not input.flags.export_violation
  not input.flags.privacy_violation
  (risk == "informational") or hitl_ok
}
deny { not allow }
```

## Recording verification

Add to release notes:

```yaml
optime_verification:
  level: L2
  date: 2025-10-04
  ci_job: "ci/optime-verify#1842"
  redteam_report: "pax/OFF/attestations/optime_redteam_2025Q4.pdf"
  perf_budget_p95_ms: 18
  reviewer: "IndependentAeroConsulting"
```

---

**Relation to ASI-T2 Architecture:**

OPTIME complements the existing policy-as-code framework (ASI_Policy.rego) by providing a focused certification profile for instruction-execution paths. It ensures that any component processing user commands or generating code/configuration changes operates within the Constitutional Guardrails defined in the Master Whitepaper.

**Integration Points:**
- **Policy-as-Code:** Extends ASI_Policy.rego with optime-specific rules
- **Evidence Weave:** Leverages existing evidence-weave structure (Appendix B)
- **QS/UTCS:** Uses existing provenance infrastructure
- **CI/CD:** Integrates with existing validation workflows

**Next Steps:**
1. Create `ci/optime-verify` workflow for automated checks
2. Add OPTIME validation to existing CI pipelines
3. Develop Rego unit tests for optime policy package
4. Document performance budgets per component type
5. Establish red-team test suite for L2+ certification

---

*This specification is maintained by the ASI-T Architecture Team and versioned alongside the Master Whitepaper suite.*
