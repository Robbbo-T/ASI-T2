# Certification Plans

This directory contains certification plans for the BWB-Q100 IMA system.

## Purpose

Provides detailed planning documents for:
- Overall certification strategy and objectives
- Software certification (DO-178C)
- Hardware certification (DO-254)
- Security certification (DO-326A/356A/355)

## Available Plans

| Plan | Standard | Description |
|------|----------|-------------|
| `certification_plan.yaml` | Multiple | Master certification plan covering all 11 standards |
| `do178c_plan.yaml` | DO-178C | Software development and certification plan |
| `do254_plan.yaml` | DO-254 | Hardware development and certification plan |
| `security_plan.yaml` | DO-326A/356A/355 | Comprehensive security certification plan |

## Master Certification Plan

The `certification_plan.yaml` file contains:
- System description and certification level (DAL A)
- Target authorities (FAA, EASA)
- All applicable standards
- Certification objectives with evidence locations
- Schedule and milestones (2025-2027)

## Plan Format

All plans are in YAML format for:
- Machine readability
- Easy integration with automation tools
- Version control friendly
- Validation against schemas

## Validation

Plans can be validated using:
```bash
make validate-plans
```

## See Also

- [Procedures](../procedures/README.md) - Detailed certification procedures
- [Schemas](../schemas/README.md) - Plan validation schemas
- [Evidence](../evidence/README.md) - Evidence referenced in plans
