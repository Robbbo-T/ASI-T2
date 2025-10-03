# IDEALE-EU Governance Model

**Version:** 1.0.0  
**Last Updated:** 2025-01-01

---

## Overview

IDEALE-EU operates as a **neutral commons** with distributed decision-making, technical meritocracy, and multi-stakeholder oversight. This document defines roles, responsibilities, decision processes, and escalation paths.

---

## Organizational Structure

```
┌─────────────────────────────────┐
│      IDEALE Council             │
│  (Strategic Oversight)          │
└────────────┬────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼────┐      ┌────▼─────┐      ┌──────────┐      ┌──────────┐
│AIR TSC │      │SEA TSC   │      │SPACE TSC │      │INFRA TSC │
└───┬────┘      └────┬─────┘      └────┬─────┘      └────┬─────┘
    │                │                  │                  │
┌───▼──────────────┐ │                  │                  │
│ Working Groups   │ │                  │                  │
│ - BWB-Q100       │ │                  │                  │
│ - ETHICS-EMPATHY │ │                  │                  │
└──────────────────┘ └──────────────────┴──────────────────┘
```

---

## Roles & Responsibilities

### IDEALE Council

**Composition:**
- 5-7 voting members representing:
  - Civil aviation authorities (2 seats: FAA region, EASA region)
  - Research institutions (1 seat: universities/national labs)
  - Industry (1 seat: rotating OEM/supplier representative)
  - Public interest (1 seat: environmental/labor/passenger advocacy)
- Non-voting secretary (operational support)

**Term:** 2 years, staggered renewal

**Powers:**
- Approve/modify charter (supermajority)
- Appoint/remove TSC chairs
- Approve annual strategic roadmap
- Resolve conflicts escalated by TSCs
- Authorize new lines of effort (AIR/SEA/SPACE/INFRANET)

**Meetings:** Quarterly, public minutes published

**Decision Process:**
- Simple majority for operational decisions
- Supermajority (2/3) for charter/governance changes
- Unanimous for dissolution

---

### Technical Steering Committees (TSC)

One TSC per line of effort: **AIR**, **SEA**, **SPACE**, **INFRANET**

**Composition:**
- 3-5 technical experts appointed by Council
- Nominated by working groups or Council members
- Expertise in relevant domains (aerodynamics, avionics, quantum computing, etc.)

**Term:** 1 year, renewable up to 3 consecutive terms

**Powers:**
- Define technical roadmap for assigned LoE
- Review and approve RFCs (Request for Comments)
- Maintain CODEOWNERS for LoE repositories
- Set CI/CD quality gates (test coverage, linting, BREX validation)
- Approve release candidates
- Initiate working groups for specific products/problems

**Meetings:** Monthly, agendas published 1 week in advance

**Decision Process:**
- Consensus preferred (all members agree or abstain)
- Fallback: simple majority vote
- Escalate to Council if TSC cannot reach agreement after 2 meetings

---

### Working Groups

Self-organized teams focused on specific products or problem domains.

**Formation:**
- Any 3+ contributors can propose a WG via RFC
- TSC approves formation, assigns scope, and appoints initial lead

**Lead Responsibilities:**
- Coordinate development activities
- Maintain product/domain README and roadmap
- Triage issues and pull requests
- Report progress to TSC quarterly
- Ensure CODEOWNERS file is current

**Membership:**
- Open to all contributors meeting CLA requirements
- Active participants (1+ contribution in past 90 days) have voting rights
- Inactive members may be moved to emeritus status

**Examples:**
- **BWB-Q100 WG**: Blended-wing-body aircraft
- **AQUA-OS WG**: Avionics operating system
- **QAIM WG**: Quantum-accelerated manufacturing
- **LH2-CORRIDOR WG**: Hydrogen infrastructure

---

### Contributors

Anyone may contribute subject to:
- **Contributor License Agreement (CLA)**: Grants IP rights necessary for federation operation
- **Code of Conduct**: Respectful, inclusive, professional behavior
- **Technical Standards**: Pass CI/CD gates, follow coding conventions

**Types:**
- **Individual Contributor**: Personal contributions, own copyright
- **Corporate Contributor**: Employer retains copyright, grants federation license
- **Institutional Contributor**: Government/academic, public domain or open license

**Recognition:**
- Listed in product/domain CONTRIBUTORS.md
- Acknowledgment in release notes
- Annual contributor awards (decided by TSCs)

---

## Decision-Making Processes

### Request for Comments (RFC)

**When Required:**
- New feature impacting multiple domains
- Changes to CI/CD gates or quality standards
- Modifications to governance or charter
- Introduction of new dependencies (libraries, tools)

**Process:**
1. **Draft**: Author creates RFC document in `/rfcs/` directory
2. **Review Period**: 14-30 days depending on scope
3. **Discussion**: GitHub issues, mailing list, TSC meetings
4. **Revision**: Author incorporates feedback
5. **Decision**: Relevant TSC votes (consensus preferred, majority fallback)
6. **Implementation**: Merged as accepted RFC

**Template:**
```markdown
# RFC-NNNN: <Title>

**Status:** Draft | Under Review | Accepted | Rejected | Superseded
**TSC:** AIR | SEA | SPACE | INFRANET | Council
**Author:** <Name> <email>
**Created:** YYYY-MM-DD

## Summary
## Motivation
## Proposal
## Alternatives Considered
## Implementation Plan
## Security Considerations
## Export Control Implications
## References
```

---

### Architecture Decision Records (ADR)

**When Required:**
- Significant technical decisions affecting multiple products
- Changes to domain structure or naming conventions
- Selection of standards, tools, or frameworks

**Location:** `/docs/adr/NNNN-title.md`

**Template:**
```markdown
# ADR-NNNN: <Title>

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXXX
**Date:** YYYY-MM-DD
**Deciders:** <TSC name or WG name>

## Context
## Decision
## Consequences
## Alternatives Rejected
```

---

### Conflict Resolution

**Level 1: Working Group**
- Informal discussion, seek consensus
- Lead facilitates, documents outcome

**Level 2: TSC**
- Escalate if WG cannot resolve in 2 meetings
- TSC discusses, seeks external input if needed
- Vote if consensus not reached

**Level 3: Council**
- Escalate if TSC vote is contested or involves governance
- Council decision is final

**Emergency Decisions:**
- Security vulnerabilities or export control violations
- TSC chair or Council member may make immediate decision
- Retroactive review at next scheduled meeting

---

## Code Review & Approval

### CODEOWNERS

Each product/domain directory contains a `CODEOWNERS` file specifying:
- Mandatory reviewers for pull requests
- Domain experts for technical questions
- Security/export control reviewers for sensitive changes

**Example:**
```
# BWB-Q100 Domains
/PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/  @air-tsc @bwb-q100-wg @aerodynamics-experts
/PRODUCTS/AMPEL360/BWB-Q100/domains/IIS/  @infranet-tsc @aqua-os-wg @security-team

# Sensitive Areas
/policies/EXPORT_CONTROL.md  @council @export-control-officer
/.github/workflows/          @infranet-tsc @ci-maintainers
```

### Pull Request Requirements

**All PRs Must:**
1. Pass CI/CD gates (lint, build, test, BREX validation)
2. Include ADR or RFC reference for significant changes
3. Obtain approval from CODEOWNERS
4. Update documentation if behavior changes
5. Include evidence links for CAX/QOX/PAX artifacts

**Merge Criteria:**
- 1+ approvals from CODEOWNERS
- All CI checks green
- No unresolved comments from reviewers
- Squash merge preferred (keep history clean)

**Fast-Track (Emergency):**
- Security patches may bypass normal review
- Must be reviewed retroactively within 48 hours
- Council approval required for fast-track merge

---

## Product Lifecycle

### Incubation
- New product proposals start as RFCs
- TSC approves formation of working group
- Initial code in `/PRODUCTS/<LOE>/<PRODUCT>/` with README declaring **INCUBATION** status
- Relaxed quality gates, experimentation encouraged

### Active Development
- TSC promotes to **ACTIVE** status when:
  - Working group has 5+ active contributors
  - CI/CD pipeline established
  - First release candidate published with SBOM
- Full quality gates enforced
- Regular releases (semantic versioning)

### Maintenance
- Mature products with stable API/ABI
- Only bugfixes and security patches
- Reduced release cadence

### Archived
- No active development or user base
- Read-only repository access
- TSC may restore to ACTIVE if interest resumes

---

## Transparency & Communication

### Public Channels
- **GitHub Discussions**: Technical Q&A, brainstorming
- **Mailing Lists**: [ideale-air@lists.example.org], [ideale-council@...]
- **Monthly Newsletters**: Progress updates, RFC summaries, contributor spotlight
- **Annual Report**: Published by Council, covers progress, membership, financials

### Private Channels
- **Security Disclosures**: security@ideale-eu.example (coordinated disclosure, NIS2 reporting)
- **Export Control Reviews**: export-control@ideale-eu.example (RESTRICTED/CONTROLLED inquiries)
- **Legal/IP Issues**: legal@ideale-eu.example (CLA, licensing questions)

---

## Amendments

This governance document may be amended by:
1. RFC proposing changes
2. Public comment period (30 days)
3. Council vote (supermajority required)
4. Effective 14 days after approval

---

**Version History:**
- **1.0.0** (2025-01-01): Initial governance model
