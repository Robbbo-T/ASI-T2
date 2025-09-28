# S1000D Data Modules

This directory contains the S1000D XML data modules that comprise the ATA-20 Standard Practices documentation.

## Structure

- [`descriptive/`](./descriptive/) — Descriptive data modules (Info Code 040A) containing technical descriptions, specifications, and practice definitions

## Data Module Organization

Data modules are organized by information code:
- **040A**: General descriptive information including overviews, specifications, and practice definitions

All data modules follow S1000D 6.0 compliance standards with proper:
- DMC (Data Module Code) naming conventions
- XML structure with dmIdent, dmAddressItems, and dmStatus sections
- UTCS canonical hash placeholders for quality assurance
- Cross-references to other ATA chapters where applicable

## Usage

These XML files are the authoritative source for ATA-20 practices and can be:
- Validated against S1000D schemas and BREX rules
- Processed by S1000D-compliant authoring tools
- Published to various output formats (HTML, PDF, etc.)
- Integrated into Interactive Electronic Technical Publications (IETP)