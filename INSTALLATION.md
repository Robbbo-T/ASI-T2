# ASI-T2 Installation Guide

This document provides comprehensive installation instructions for the ASI-T2 repository dependencies.

## Quick Start

### Option 1: Using requirements.txt (Recommended)
```bash
# Install all dependencies
pip install -r requirements.txt

# Verify installation
python verify_installation.py
```

### Option 2: Using pyproject.toml (Modern Python)
```bash
# Install base dependencies
pip install .

# Install with optional development tools
pip install .[dev]

# Install with documentation tools
pip install .[docs]

# Install with high-performance XML processing
pip install .[xml]
```

## Dependencies

### Core Runtime Dependencies

- **FastAPI** (≥0.104.0) - Modern, fast web framework for building APIs
- **Uvicorn** (≥0.24.0) - ASGI server for running FastAPI applications
- **Pydantic** (≥2.4.0) - Data validation using Python type annotations
- **Requests** (≥2.31.0) - HTTP library for making API calls (OpenAI integration)
- **Starlette** (≥0.27.0) - ASGI toolkit (included with FastAPI)
- **jsonschema** (≥4.17.0) - JSON Schema validation for PAX manifests
- **PyYAML** (≥6.0) - YAML parser for configuration files and manifests
- **defusedxml** (≥0.7.1) - Secure XML processing (S1000D data modules)

### Standard Library Usage

The codebase makes extensive use of Python's standard library:
- **pathlib** - Modern path handling
- **xml.etree.ElementTree** - XML processing (with defusedxml as security fallback)
- **json** - JSON data processing
- **subprocess** - External command execution
- **datetime** - Date/time handling
- **re** - Regular expressions
- **html** - HTML escaping
- **shutil** - File operations
- **zipfile** - Archive creation (DTP packages)
- **argparse** - Command-line argument parsing

## Component-Specific Requirements

### GenCMS (Generative Content Management System)
```bash
cd PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-57/S1000D/gen_cms/server
pip install fastapi uvicorn requests pydantic defusedxml
```

**Required Environment Variables:**
- `GENCMS_PROVIDER` - Set to "openai" or "mock"  
- `OPENAI_API_KEY` - Your OpenAI API key (if using OpenAI provider)
- `GENCMS_OPENAI_MODEL` - Model name (optional, defaults to "gpt-4o-mini")

### PAX Validation
```bash
pip install jsonschema pyyaml
```

### S1000D Processing
```bash
pip install defusedxml  # Secure XML processing
```

## Verification

Run the verification script to ensure all dependencies are correctly installed:

```bash
python verify_installation.py
```

Expected output:
```
🎉 All dependencies verified successfully!
✅ Ready to run ASI-T2 applications
```

## Development Setup

### For Development Work
```bash
# Install with development dependencies
pip install .[dev]

# This includes:
# - pytest (≥7.4.0) - Testing framework
# - pytest-asyncio (≥0.21.0) - Async test support
# - httpx (≥0.25.0) - HTTP client for testing FastAPI
```

### For Documentation
```bash
# Install documentation tools
pip install .[docs]

# This includes:
# - mkdocs (≥1.5.0) - Documentation generator
# - mkdocs-material (≥9.4.0) - Material Design theme
```

## Running Applications

### GenCMS API Server
```bash
cd PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-57/S1000D/gen_cms/server

# Mock provider (no API key required)
export GENCMS_PROVIDER=mock
python -c "import uvicorn; from app import app; uvicorn.run(app, host='0.0.0.0', port=8000)"

# OpenAI provider
export GENCMS_PROVIDER=openai
export OPENAI_API_KEY=your-key-here
python -c "import uvicorn; from app import app; uvicorn.run(app, host='0.0.0.0', port=8000)"
```

### Static Site Generation
```bash
# Generate GitHub Pages site
python scripts/ghpages_build.py

# Build IETP (Interactive Electronic Technical Publication)
python PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-57/S1000D/ietp/build_ietp.py
```

### Validation Scripts
```bash
# Validate PAX manifests
python PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/scripts/validate_pax.py \
  --schema PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax/schemas/package.schema.json \
  --root PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/pax

# Derive structure from README files
python scripts/derive_struct_from_readmes.py --dry-run

# Validate CSDB (S1000D)
python PRODUCTS/AMPEL360/BWB-Q100/domains/AAA/ata/ATA-57/S1000D/validation/validators/validate_csdb.py
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'fastapi'**
   ```bash
   pip install fastapi uvicorn
   ```

2. **XML processing errors**
   ```bash
   pip install defusedxml
   ```

3. **JSON Schema validation fails**
   ```bash
   pip install jsonschema
   ```

4. **YAML parsing issues**
   ```bash
   pip install pyyaml
   ```

### Dependency Conflicts
If you encounter dependency conflicts, try creating a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Version Requirements
- **Python**: ≥3.9 (recommended: 3.11+)
- **Operating System**: Cross-platform (Linux, macOS, Windows)

## Architecture Notes

The repository follows a modular architecture:

- **Web Services**: FastAPI-based APIs (GenCMS)
- **Data Processing**: JSON Schema validation, YAML configuration
- **XML Processing**: S1000D data modules with secure parsing
- **Static Generation**: GitHub Pages and IETP builders
- **Validation**: Multi-format data validation pipelines

All components are designed to work with minimal dependencies and graceful fallbacks where possible.