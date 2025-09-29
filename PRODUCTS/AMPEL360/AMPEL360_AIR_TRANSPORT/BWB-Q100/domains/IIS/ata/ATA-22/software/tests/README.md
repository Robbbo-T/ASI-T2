# ATA-22 Test Suite

This directory contains unit tests for the ATA-22 Autoflight system Python modules.

## Contents

- `test_mode_logic.py` — Unit tests for mode manager functionality

## Test Structure

### Mode Logic Tests (`test_mode_logic.py`)
- **test_engage_interlocks_ok()**: Validates engage conditions
- **test_select_lnav_requires_fms_valid()**: Tests FMS dependency
- **test_disengage_reason()**: Verifies disengage event handling

## Test Framework

### pytest Configuration
- Configured in `../pyproject.toml`
- Source path set to `src/` directory
- Automatic test discovery for `test_*.py` files

### Test Execution
```bash
# Run all tests
pytest -q

# Run with verbose output
pytest -v

# Run specific test file
pytest PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22/software/tests/test_mode_logic.py

# Run with coverage analysis
pytest --cov=ata22 --cov-report=html
```

## Test Categories

### Unit Tests
- Individual function and method testing
- Boundary condition validation
- Error handling verification
- Configuration parameter testing

### Integration Tests
- Module interaction verification
- Interface contract validation
- End-to-end scenario testing
- Performance benchmarking

### Safety Tests
- Failure mode testing
- Interlock validation
- Redundancy verification
- Certification compliance

## Coverage Requirements

Following DO-178C DAL A requirements:
- **Statement Coverage**: 100% of executable statements
- **Decision Coverage**: 100% of decision outcomes
- **MC/DC Coverage**: Modified Condition/Decision Coverage for complex logic
- **Boundary Testing**: All input ranges and limits validated

## Continuous Integration

Tests are automatically executed in CI pipeline:
- Pull request validation
- Merge verification
- Nightly regression testing
- Release qualification