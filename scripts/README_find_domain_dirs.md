# Domain Directory Finder Utilities

This directory contains utilities for finding directories under the standard domain structure:
`PRODUCTS/.../domains/<DOMAIN>/{ata,cax,qox,pax}/`

## Problem Statement

The `find` command with regex pattern `.*/domains/[^/]+/(ata|cax|qox|pax)/.*` doesn't work with default settings because it requires either:
1. Escaping special regex characters: `.*/domains/[^/]+/\(ata\|cax\|qox\|pax\)/.*`
2. Using POSIX extended regex: `find PRODUCTS -type d -regextype posix-extended -regex ".*/domains/[^/]+/(ata|cax|qox|pax)/.*"`

## Solutions

We provide two equivalent utilities:

### 1. Bash Script (`find_domain_dirs.sh`)

Best for command-line usage and shell scripts.

```bash
# Find all subdirectories under ata/cax/qox/pax
./scripts/find_domain_dirs.sh

# Find only ATA directories
./scripts/find_domain_dirs.sh --type ata

# Find CAx directories
./scripts/find_domain_dirs.sh --type cax

# Find QOx directories
./scripts/find_domain_dirs.sh --type qox

# Find PAx directories
./scripts/find_domain_dirs.sh --type pax

# Search in a different root
./scripts/find_domain_dirs.sh --root /path/to/products
```

### 2. Python Script (`find_domain_dirs.py`)

Best for cross-platform compatibility and integration with other Python tools.

```bash
# Find all subdirectories under ata/cax/qox/pax
python3 scripts/find_domain_dirs.py

# Find only ATA directories
python3 scripts/find_domain_dirs.py --type ata

# Enable verbose output
python3 scripts/find_domain_dirs.py --verbose

# Search in a different root
python3 scripts/find_domain_dirs.py --root /path/to/products
```

## Directory Types

- **ata**: ATA (Air Transport Association) chapter directories for aircraft systems documentation
- **cax**: CAx (Computer-Aided X) tool directories for CAD, CAE, CAM, PDM, PLM, etc.
- **qox**: QOx (Quantum Optimization X) directories for quantum computing problems and solutions
- **pax**: PAx (Packaging & Applications) directories for on-board and off-board packages

## Integration Examples

### In Shell Scripts

```bash
#!/bin/bash
# Process all CAD directories
for dir in $(./scripts/find_domain_dirs.sh --type cax); do
    echo "Processing: $dir"
    # Your processing logic here
done
```

### In Python Scripts

```python
from pathlib import Path
import subprocess

# Find all PAx directories
result = subprocess.run(
    ["python3", "scripts/find_domain_dirs.py", "--type", "pax"],
    capture_output=True,
    text=True
)
pax_dirs = [Path(line) for line in result.stdout.strip().split('\n') if line]

# Process directories
for dir_path in pax_dirs:
    print(f"Processing: {dir_path}")
    # Your processing logic here
```

### In Makefile

```makefile
.PHONY: lint-cax
lint-cax:
	@for dir in $$(./scripts/find_domain_dirs.sh --type cax); do \
		echo "Linting $$dir"; \
		# Your linting command here \
	done
```

## Direct `find` Command

If you prefer to use `find` directly without the helper scripts:

### Option 1: POSIX Extended Regex (Recommended)

```bash
find PRODUCTS -type d -regextype posix-extended -regex ".*/domains/[^/]+/(ata|cax|qox|pax)/.*"
```

### Option 2: Basic Regex with Escaped Characters

```bash
find PRODUCTS -type d -regex ".*/domains/[^/]+/\(ata\|cax\|qox\|pax\)/.*"
```

## Common Use Cases

1. **Finding all CAD model directories:**
   ```bash
   ./scripts/find_domain_dirs.sh --type cax | grep CAD
   ```

2. **Counting ATA chapters:**
   ```bash
   ./scripts/find_domain_dirs.sh --type ata | wc -l
   ```

3. **Listing all quantum optimization problems:**
   ```bash
   ./scripts/find_domain_dirs.sh --type qox | grep problems
   ```

4. **Finding PAx manifests:**
   ```bash
   ./scripts/find_domain_dirs.sh --type pax | grep manifests
   ```

## Notes

- Both scripts produce identical output
- Both scripts support filtering by directory type
- The Python version is more portable and easier to integrate with other Python tools
- The Bash version is faster for simple command-line usage
- Both scripts sort the output for consistency
