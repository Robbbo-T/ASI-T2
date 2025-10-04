# Governance

## Overview
ASI-T2 follows a structured governance model aligned with UTCS v5.0, TFA V2, and IDEALE-EU framework.

## Roles

### Maintainers
- **Lead Maintainer**: @amedeo.pelliccia
- **Architecture Team**: ASI-T Architecture Team
- **Domain Owners**: Assigned per domain (AAA, PPP, LCC, etc.)

#### Responsibilities
- Approve architectural changes
- Ensure UTCS compliance
- Maintain quality standards
- Review PRs for technical correctness
- Enforce ethics guard (MAL-EEM)

### Contributors
- Submit PRs following contribution guidelines
- Participate in technical discussions
- Report issues and suggest improvements
- Maintain code quality standards

### Reviewers
- Technical expertise in specific domains
- Conduct code reviews
- Verify UTCS evidence
- Validate test coverage

## Technical Reviews

### PR Acceptance Criteria
- [ ] Follows TFA V2 architecture
- [ ] UTCS manifest updated if needed
- [ ] Tests pass (if applicable)
- [ ] Documentation updated
- [ ] SBOM regenerated for dependency changes
- [ ] No breaking changes without migration plan
- [ ] MAL-EEM ethics guard compliance
- [ ] CXP checklist completed (for CXP changes)

### Review Process
1. **Initial Triage**: Within 48 hours
2. **Technical Review**: Domain experts assigned
3. **Architecture Review**: For structural changes
4. **Approval**: Requires maintainer sign-off
5. **Merge**: After all checks pass

## Release Management

### Release Calendar
- **Major Releases**: Quarterly (with planning phase)
- **Minor Releases**: Monthly (feature additions)
- **Patch Releases**: As needed (bug fixes, security)

### Release Process
1. Version bump following semver
2. CHANGELOG update
3. UTCS manifest update
4. SBOM regeneration
5. Signature generation
6. Tag creation
7. Artifact publication

### Version Numbering
- **MAJOR.MINOR.PATCH** (semver 2.0)
- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes, documentation

## Area Ownership

### Core Areas
- **UTCS/CXP**: @amedeo.pelliccia
- **Domains**: Per-domain assignment
- **CAX**: Classical engineering lead
- **QOX**: Quantum optimization lead
- **ATA**: Documentation lead
- **PAX**: Deployment lead

### Decision Making
- Technical decisions: Area owner with maintainer approval
- Architecture decisions: Consensus among maintainers
- Breaking changes: Require lead maintainer approval
- Security issues: Immediate action by security contacts

## Communication

### Channels
- **GitHub Issues**: Bug reports, feature requests
- **Pull Requests**: Code contributions
- **Discussions**: General questions, proposals
- **Security**: Private email (see SECURITY.md)

### Meeting Schedule
- Architecture reviews: Monthly
- Release planning: Quarterly
- Ad-hoc: As needed for critical issues

## Conflict Resolution
1. Discussion in GitHub issue/PR
2. Area owner decision
3. Escalation to maintainers if unresolved
4. Final decision by lead maintainer

## Code of Conduct
All participants must follow the project's Code of Conduct (CODE_OF_CONDUCT.md).
