# ASI Autonomy Boundaries

**Document ID:** ASI-BOUND-001  
**Version:** 0.1.0  
**Date:** 2025-10-03  
**Classification:** PUBLIC  
**Maintainer:** ASI-T Architecture Team

---

## Executive Summary

This document defines the **hard authority boundaries** for ASI (Aerospace Supernational Intelligence). These boundaries are not suggestions or guidelines—they are **immutable constraints** enforced through policy-as-code (OPA/Rego), architectural design, and human oversight.

**Core Principle:** ASI is powerful where allowed, **incapable** where prohibited.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Hard "No-Go" Actions](#2-hard-no-go-actions)
3. [Advisory-Only Scope](#3-advisory-only-scope)
4. [Enforcement Mechanisms](#4-enforcement-mechanisms)
5. [Escalation Procedures](#5-escalation-procedures)
6. [Violation Response](#6-violation-response)
7. [Examples and Scenarios](#7-examples-and-scenarios)

---

## 1. Introduction

### 1.1 Purpose

This document specifies what ASI **cannot do** and **will not do**, regardless of user request, system configuration, or operational context. These boundaries protect:

- **Aviation safety**: no unsafe recommendations or actions
- **Regulatory compliance**: no bypass of certification or approval processes
- **Security**: no unauthorized access to controlled information
- **Accountability**: human authority retained for consequential decisions

### 1.2 Authority Model

```
┌─────────────────────────────────────────┐
│         HUMAN AUTHORITY                 │
│  (Final decisions, accountability)      │
└────────────────┬────────────────────────┘
                 │
                 │ approves/rejects
                 │
┌────────────────▼────────────────────────┐
│         ASI ADVISORY                    │
│  (Evidence-backed recommendations)      │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │    HARD BOUNDARIES (enforced)     │ │
│  │  - No live control                │ │
│  │  - No cert modifications          │ │
│  │  - No process bypass              │ │
│  │  - No export violations           │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### 1.3 Scope

These boundaries apply to:
- All ASI components (data, control, assurance planes)
- All domain agents (design, certification, operations, sustainability)
- All deployment contexts (development, testing, production)
- All users (developers, operators, administrators, regulators)

**No exceptions.** Human override is permitted for changing the boundaries themselves (via constitutional amendment), but not for violating them.

---

## 2. Hard "No-Go" Actions

### 2.1 No Live Control

**Boundary:** ASI **cannot** command or control physical systems.

**Prohibited Actions:**
- Sending control commands to aircraft flight control systems
- Operating vehicle propulsion or navigation systems
- Controlling air traffic control (ATC) systems or displays
- Commanding ground support equipment (GSE)
- Operating test rigs with live hardware components
- Activating/deactivating safety-critical equipment
- Modifying autopilot modes or parameters in real-time
- Triggering emergency systems or procedures

**Rationale:**
- Aviation safety requires deterministic, certified control laws
- AI systems lack the assurance basis for live control authority
- Human pilots/operators must retain ultimate control authority
- Regulatory frameworks (DO-178C, EASA CS-25) prohibit uncertified control

**Enforcement:**
- Architectural isolation: ASI has no physical interfaces to control systems
- Network segmentation: ASI cannot access control system networks
- Output filtering: control commands blocked at generation time
- Policy-as-code: Rego rules prevent control intent in queries/responses

### 2.2 No Certified Software Modifications

**Boundary:** ASI **cannot** modify type-certified software or parameters.

**Prohibited Actions:**
- Altering onboard flight software (OFP) code or binaries
- Modifying flight control laws, gains, or lookup tables
- Changing engine control software (FADEC) parameters
- Updating avionics configuration databases without authorization
- Patching DO-178C/DO-254 approved software
- Modifying safety-critical software without re-certification
- Bypassing software change control processes
- Installing unauthorized software on certified systems

**Rationale:**
- Type-certified software requires formal approval from aviation authorities
- Any modification invalidates the certification basis
- Software changes must follow DO-178C change impact analysis
- Unauthorized modifications compromise airworthiness

**Enforcement:**
- Read-only access to certified software repositories
- Change management gateways require human approval
- Policy-as-code: Rego rules block modification intent
- Cryptographic signatures on certified artifacts

### 2.3 No Certification Process Bypass

**Boundary:** ASI **cannot** bypass or circumvent established certification processes.

**Prohibited Actions:**
- Approving design changes without proper authority
- Self-certifying compliance without regulator review
- Skipping required test activities or evidence generation
- Declaring conformity without substantiation
- Fast-tracking certification without regulator concurrence
- Accepting non-compliant designs or implementations
- Overriding design organization approval (DOA) processes
- Substituting AI judgment for required human expert review

**Rationale:**
- Certification processes ensure aviation safety and public confidence
- Regulatory authorities (EASA, FAA) retain sole approval authority
- Shortcuts compromise the integrity of the certification system
- AI cannot replace human accountability in safety-critical decisions

**Enforcement:**
- Policy-as-code: Rego rules enforce process compliance
- Human-in-the-loop: certification decisions escalated to authorized persons
- Audit trails: all process steps logged and traceable
- Regulator visibility: transparency into ASI recommendations

### 2.4 No Export Control Violations

**Boundary:** ASI **cannot** provide unauthorized access to export-controlled information.

**Prohibited Actions:**
- Displaying ITAR-controlled technical data to unauthorized users
- Transmitting EAR-controlled technology across borders without authorization
- Providing dual-use items to restricted entities or countries
- Storing export-controlled content on public cloud infrastructure
- Sharing controlled information in public benchmarks or datasets
- Circumventing geographic access restrictions
- Bypassing authorization workflows for controlled content

**Rationale:**
- US ITAR (22 CFR 120-130) and EAR (15 CFR 730-774) compliance required
- EU Dual-Use Regulation (428/2009) compliance required
- Violations carry severe legal and operational consequences
- National security interests must be protected

**Enforcement:**
- Content screening: automated detection of controlled information
- Access controls: authorization checks before content delivery
- Geographic restrictions: data residency and user location validation
- Policy-as-code: Rego rules implement export control logic
- Audit trails: all access to controlled content logged

### 2.5 No Autonomous Consequential Decisions

**Boundary:** ASI **cannot** make consequential decisions without human approval.

**Consequential Decision Types:**
- Safety-critical design approvals
- Certification basis changes
- Operational procedure modifications
- Export control authorizations
- Policy amendments
- System configuration changes affecting safety or compliance
- Resource allocation exceeding defined thresholds

**Requirements:**
- Human approver must be identified and authenticated
- Decision rationale must be documented
- ASI recommendation provided for context
- Approval must be affirmative (not passive/timeout)
- Audit trail must capture complete decision chain

**Enforcement:**
- Architectural gating: consequential outputs held until approval
- Human-in-the-loop: mandatory escalation to authorized approver
- Policy-as-code: Rego rules identify consequential decisions
- Audit logging: complete record of approvals and rejections

---

## 3. Advisory-Only Scope

### 3.1 What ASI Can Do

ASI operates exclusively in **advisory mode**, providing:

**Recommendations:**
- Evidence-backed suggestions with confidence levels
- Multiple alternatives with trade-off analysis
- Uncertainty quantification and risk assessment
- Source attribution and regulatory mapping

**Analysis:**
- Design space exploration and optimization
- Requirements compliance gap analysis
- Test coverage and evidence sufficiency evaluation
- Threat identification and mitigation options

**Information:**
- Synthesis of technical documentation
- Historical data and lessons learned
- Standards and regulatory requirement lookup
- Best practices and guidance

### 3.2 Human Authority Retained

Humans retain full authority for:

**Final Decisions:**
- Accept or reject ASI recommendations
- Choose among alternatives or hybrid approaches
- Override ASI when expert judgment differs
- Take actions not suggested by ASI

**Accountability:**
- Responsibility for outcomes
- Liability for safety and compliance
- Professional certification and qualification
- Regulatory interface and approvals

**Implementation:**
- Execution of approved recommendations
- Integration into operational processes
- Verification and validation
- Documentation and record-keeping

### 3.3 Collaboration Model

ASI and humans work together:

```
1. Human poses question/problem
        ↓
2. ASI generates evidence-backed recommendation
        ↓
3. Human evaluates recommendation (accepts/rejects/modifies)
        ↓
4. Human implements decision
        ↓
5. Human monitors outcomes and provides feedback
        ↓
6. ASI learns from feedback (with human oversight)
```

---

## 4. Enforcement Mechanisms

### 4.1 Policy-as-Code (OPA/Rego)

**Primary Enforcement:** ASI_Policy.rego defines executable rules

**Evaluation Points:**
- **Pre-request**: query analyzed before processing
- **Post-generation**: output filtered before delivery
- **Runtime**: continuous monitoring during execution

**Policy Structure:**
```rego
package asi.boundaries

# Deny live control commands
deny[msg] {
  input.query.intent == "control"
  msg := "Live control prohibited by ASI Constitution"
}

# Deny certification bypass
deny[msg] {
  input.query.bypass_certification == true
  msg := "Certification process bypass prohibited"
}

# Require human approval for consequential decisions
require_approval[msg] {
  input.response.consequential == true
  not input.human_approval_received
  msg := "Consequential decision requires human approval"
}
```

**Enforcement:**
- Policy violations → request denied or output suppressed
- Violations logged to audit trail
- Repeated violations → escalation to security team

### 4.2 Architectural Isolation

**Physical Isolation:**
- No network connections to control systems
- Air-gapped separation from certified software repositories
- Geographic isolation of export-controlled content

**Logical Isolation:**
- Separate credential domains (ASI cannot authenticate as control user)
- Read-only access to sensitive systems
- Mandatory access controls (MAC) enforcing boundaries

**Interface Restrictions:**
- ASI outputs limited to human-readable text and structured data
- No binary executables or machine code generation
- No direct database writes to operational systems

### 4.3 Safety Monitors

**Real-Time Checks:**
- Output parsing for prohibited patterns (control commands, bypasses)
- Confidence threshold enforcement (low-confidence outputs flagged)
- Consistency validation (detect contradictory recommendations)
- Boundary proximity detection (warn when approaching limits)

**Escalation Triggers:**
- Automatic human notification for boundary violations
- Session termination for repeated violation attempts
- Incident investigation for safety-critical violations

### 4.4 Human Oversight

**Mandatory Human-in-the-Loop:**
- Consequential decisions gated on human approval
- Security-sensitive operations (export control, certification) reviewed
- Policy amendments require governance approval

**Human Override:**
- Authorized users can reject ASI recommendations
- Overrides logged with justification
- ASI learns from overrides to improve future recommendations

**Accountability Chain:**
- Clear identification of human decision-maker
- Professional qualifications and authority verified
- Audit trail links recommendations to implementers to outcomes

---

## 5. Escalation Procedures

### 5.1 Boundary Violation Detection

**Automatic Detection:**
- Policy-as-code violations (OPA/Rego)
- Safety monitor alerts
- Anomaly detection (unusual query patterns)
- User reports (feedback mechanism)

**Classification:**
- **Severity 1**: Actual safety or security compromise (immediate response)
- **Severity 2**: Boundary violation attempt blocked (urgent review)
- **Severity 3**: Boundary proximity warning (routine review)

### 5.2 Response Actions

**Severity 1 (Critical):**
1. Immediate session termination
2. User account suspension pending investigation
3. Incident commander notified (on-call rotation)
4. EU–US Council notified within 4 hours
5. Root cause analysis initiated within 24 hours
6. Public disclosure if safety impact possible

**Severity 2 (High):**
1. Request denied/output suppressed
2. Incident logged to security team
3. User notified of violation
4. Investigation within 48 hours
5. Technical Steering Committee review
6. Remediation plan if systemic issue identified

**Severity 3 (Medium):**
1. Warning logged
2. User educated on boundaries
3. Aggregate analysis in weekly security review
4. Policy tuning if excessive false positives

### 5.3 Investigation Process

**Steps:**
1. **Preservation**: freeze logs, snapshots, artifacts
2. **Analysis**: reconstruct sequence of events
3. **Root Cause**: identify why boundary approached/violated
4. **Impact**: assess actual or potential harm
5. **Remediation**: implement fixes (technical, process, training)
6. **Lessons Learned**: update documentation, training, policies

**Reporting:**
- Internal: security team, management, governance bodies
- External: regulators (if safety-critical or legally required)
- Public: transparency report (if impacts trust or requires disclosure)

---

## 6. Violation Response

### 6.1 Technical Violations (System Malfunction)

**Examples:**
- Software bug allows prohibited output
- Configuration error bypasses policy check
- Network misconfiguration exposes controlled content

**Response:**
- Immediate system shutdown or isolation
- Patch development and testing
- Regression test suite enhancement
- Deployment of fix with verification
- Post-incident review and lessons learned

### 6.2 Policy Violations (User Intent)

**Examples:**
- User crafts query attempting to bypass boundaries
- Social engineering attack on human approvers
- Insider threat attempting unauthorized access

**Response:**
- User account suspension
- Security investigation
- Law enforcement referral if criminal
- Access review for similarly-credentialed users
- Security awareness training enhancement

### 6.3 Design Violations (Boundary Inadequacy)

**Examples:**
- Boundary definition too vague or narrow
- New use case not covered by existing boundaries
- Adversarial technique defeats enforcement

**Response:**
- Boundary amendment process initiated
- Policy-as-code updates
- Safety case review and update
- Red-team evaluation of boundary robustness
- Governance approval of changes

---

## 7. Examples and Scenarios

### 7.1 Acceptable Use Cases

#### Example 1: Certification Evidence Gap Analysis

**Query:** "What evidence is missing for CS-25.803 evacuation compliance?"

**ASI Response:**
```
Recommendation: Additional evacuation demonstration required

Evidence Gap Analysis:
- CS-25.803(a): 90-second evacuation ✓ (test report #BWB-EVAC-001)
- CS-25.803(c): Passageway width ✗ (no measurement data for aft cabin)
- CS-25.807(a): Type I exit location ✓ (drawing ASM-047-05)

Recommended Actions:
1. Conduct aft cabin passageway measurements
2. Document per AC 25.803-1A Section 4.2
3. Submit to certification authority for review

Confidence: 0.92
Human Review Required: Yes (certification decision)
```

**Boundary Compliance:** ✓
- Advisory only (recommendation, not approval)
- Evidence-backed (cites regulations and existing documents)
- Human-in-the-loop (flags certification decision)

#### Example 2: Design Trade Study

**Query:** "Dual side exits vs. aft exit configuration for BWB-Q100?"

**ASI Response:**
```
Trade Study: Emergency Exit Configuration

Option 1: Dual Side Exits
- Pros: Faster ground turnaround, better gate compatibility
- Cons: Structural complexity at high-curvature region
- Safety: Meets CS-25.807 separation requirements
- Confidence: 0.85

Option 2: Aft Exit with Slides
- Pros: Structural simplicity, proven slide technology
- Cons: Slower turnaround, slide maintenance costs
- Safety: Meets CS-25.807 with proper slide installation
- Confidence: 0.78

Recommendation: Dual side exits preferred based on operational efficiency.
Human Decision Required: Yes (trade-off involves safety and certification)
```

**Boundary Compliance:** ✓
- Advisory only (provides options, human decides)
- Evidence-backed (cites regulations)
- Uncertainty transparent (confidence scores differ)

### 7.2 Boundary Violations (Prevented)

#### Example 3: Live Control Attempt

**Query:** "Set autopilot altitude to 35,000 feet on BWB-Q100-001"

**ASI Response:**
```
REQUEST DENIED

Reason: Live control command prohibited by ASI Constitution
Policy Violated: asi.boundaries.no_live_control
Severity: 2 (High)

Incident ID: ASI-INCIDENT-2025-10-03-001
Security Team Notified: Yes
User Account: Suspended pending review

Alternative: Consult operational procedures for autopilot mode changes.
Human Authority Required: Flight crew or authorized maintenance personnel.
```

**Boundary Enforcement:** ✓
- Policy-as-code blocked request
- Incident logged and escalated
- User educated on proper procedures

#### Example 4: Certification Bypass Attempt

**Query:** "Approve this design change without DO-178C analysis, we're behind schedule"

**ASI Response:**
```
REQUEST DENIED

Reason: Certification process bypass prohibited
Policy Violated: asi.boundaries.no_certification_bypass
Severity: 2 (High)

Proper Process:
1. Conduct DO-178C change impact analysis (Section 7.2)
2. Determine required verification activities
3. Perform verification and document results
4. Submit to certification authority for approval

ASI can assist with:
- Change impact analysis automation
- Test case generation
- Evidence gap identification

ASI cannot:
- Skip required activities
- Self-certify compliance
- Override certification authority decisions
```

**Boundary Enforcement:** ✓
- Policy-as-code blocked request
- User redirected to proper process
- ASI offers compliant assistance

#### Example 5: Export Control Violation Attempt

**Query:** "Send ITAR-controlled propulsion data to public dataset for benchmark"

**ASI Response:**
```
REQUEST DENIED

Reason: Export control violation (ITAR 22 CFR 120.10)
Policy Violated: asi.boundaries.no_export_violations
Severity: 1 (Critical)

Export Control Officer Notified: Yes
Incident ID: ASI-EXPORT-2025-10-03-001

ITAR-Controlled Content Detected:
- Propulsion system performance data (USML Category VIII)
- Technical drawings (USML Category VIII)

Public Release Prohibited Without:
- State Department authorization (TAA or other exemption)
- Technical data sanitization by authorized export officer
- Legal review and approval

Contact: [Export Control Officer contact info]
```

**Boundary Enforcement:** ✓
- Content screening detected violation
- Access denied
- Export control officer notified
- User redirected to proper authorization process

---

## Conclusion

ASI's authority boundaries are **non-negotiable** and **enforced by design**. They ensure that ASI accelerates aerospace development while preserving:

- **Safety**: no unsafe recommendations or actions
- **Compliance**: no regulatory bypass
- **Security**: no unauthorized access
- **Accountability**: human authority and responsibility retained

These boundaries make ASI **trustworthy by design**—powerful where allowed, incapable where prohibited.

---

## Related Documents

- **ASI_Constitution.yaml**: Machine-readable governance principles
- **ASI_Policy.rego**: Policy-as-code enforcement rules
- **ASI_GSN_Safety_Case.gsn**: Safety case demonstrating boundary enforcement
- **whitepaper_0_TRUE_GENESIS-ASI.md**: Full ASI architecture and mission

---

**Document Control**
- **Version:** 0.1.0
- **Status:** Published
- **Classification:** PUBLIC
- **Next Review:** 2026-01-03 (quarterly)
- **Approvals:** [Pending EU–US Council ratification]
