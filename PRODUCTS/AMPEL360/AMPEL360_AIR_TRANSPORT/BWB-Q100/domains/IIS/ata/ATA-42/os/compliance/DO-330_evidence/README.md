# DO-330 Tool Qualification Evidence

This directory contains DO-330 tool qualification evidence for development and verification tools used in the AQUA-OS project.

## Evidence Files

| Document | Description | File |
|----------|-------------|------|
| Tool Qualification Report | Complete tool qualification data | [tool_qualification_report.md](./tool_qualification_report.md) |

## Qualified Tools

### TQL-1 Tools (Critical)

| Tool | Version | Purpose | Status |
|------|---------|---------|--------|
| GCC PowerPC | 11.3.0 | Code generation | ✅ Qualified |
| GNU Binutils | 2.38 | Linking, assembly | ✅ Qualified |
| gcov | 11.3.0 | Code coverage | ✅ Qualified |
| Bullseye Coverage | 8.25 | MC/DC coverage | ✅ Qualified |
| LDRA Testbed | 9.7.1 | Static analysis | ✅ Qualified |
| VectorCAST | 2023 | Unit testing | ✅ Qualified |

### TQL-2 Tools

| Tool | Version | Purpose | Status |
|------|---------|---------|--------|
| Polyspace | R2023a | Runtime error detection | ✅ Qualified |
| Coverity | 2023.3 | Static analysis | ✅ Qualified |

## Qualification Status

All development and verification tools have been qualified in accordance with DO-330 requirements.

## Related Documents

- [DO-178C Evidence](../DO-178C_evidence/)
- [Main README](../../README.md)
