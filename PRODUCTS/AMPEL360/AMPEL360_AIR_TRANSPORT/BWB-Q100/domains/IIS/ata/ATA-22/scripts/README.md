# Build and Development Scripts

This directory contains automation scripts for ATA-22 Autoflight system development.

## Contents

- `scaffold.sh` — Directory structure creation script

## Available Scripts

### Scaffold Creation
The `scaffold.sh` script creates the complete ATA-22 directory structure:

```bash
#!/usr/bin/env bash
set -euo pipefail
BASE="PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22"
mkdir -p "$BASE"/{architecture,requirements/LLR,icd,config/gains,software/src/ata22,software/tests,sitl,qox}
touch "$BASE/software/src/ata22/__init__.py"
echo "✅ ATA-22 scaffold created at $BASE"
```

### Usage

```bash
# Create initial directory structure
./PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22/scripts/scaffold.sh
```

## Development Workflow

1. **Setup**: Run scaffold script to create directory structure
2. **Development**: Implement modules in the software/ directory
3. **Testing**: Run tests using pytest framework
4. **Integration**: Use SITL harness for system-level testing
5. **Validation**: Execute CI pipeline for automated verification

## Future Scripts

Additional scripts may be added for:
- Code generation from requirements
- Automated test case generation
- Configuration validation
- Documentation generation
- Certification artifact collection