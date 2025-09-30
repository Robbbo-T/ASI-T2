# Standards Mapping for BWB-Q100 IMA Certification

## Standards Hierarchy

```
ARP4754B (System Development)
    ├── ARP4761A (Safety Assessment)
    │   ├── FHA → Function-level hazards
    │   ├── PSSA → Preliminary safety requirements
    │   └── SSA → Final safety compliance
    │
    ├── DO-178C (Software)
    │   ├── DAL A objectives
    │   └── DO-330 (Tool Qualification)
    │
    ├── DO-254 (Hardware)
    │   ├── DAL A objectives
    │   └── DO-330 (Tool Qualification)
    │
    ├── DO-297 (IMA Specific)
    │   ├── Partitioning
    │   └── Responsibility agreements
    │
    └── Security Standards
        ├── DO-326A (Security Process)
        ├── DO-356A (Security Methods)
        └── DO-355 (Continuing Airworthiness)
```

## Requirements Traceability

| System Requirement | Standard | Evidence Location |
|-------------------|----------|-------------------|
| Software Assurance | DO-178C | evidence/DO-178C/ |
| Hardware Assurance | DO-254 | evidence/DO-254/ |
| IMA Partitioning | DO-297 | evidence/DO-297/ |
| Safety Assessment | ARP4761A | evidence/ARP4761A/ |
| Security Assurance | DO-326A/356A/355 | evidence/DO-326A/, DO-356A/, DO-355/ |
| Tool Qualification | DO-330 | evidence/DO-330/ |

## Compliance Matrix

Evidence packages map directly to certification objectives defined in each applicable standard.
