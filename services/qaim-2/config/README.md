# QAIM-2 Deployment Configurations

This directory contains YAML configuration files for deploying QAIM-2 across different environments: Edge, Site, and Hub.

## Overview

Each configuration is optimized for specific deployment scenarios with appropriate resource allocations, solver portfolios, and feature sets.

## Configuration Files

### 1. Edge Deployment (`deployment-edge.yaml`)

**Target:** UAVs, embedded systems, edge devices  
**Resources:** 512MB RAM, 2 CPUs  
**Solvers:** Classical only (CBC, GLPK)

**Characteristics:**
- Minimal resource footprint
- No ML models (lightweight)
- Fast response time (< 100ms target)
- Local decision making
- Limited connectivity requirements

**Use Cases:**
- UAV mission planning
- On-board route optimization
- Real-time tactical decisions
- Field operations

**Key Settings:**
```yaml
deployment: edge
bridge: 'CB→QB'
surrogate:
  enabled: false  # No ML overhead
cb_solvers:
  - name: 'cbc'
    time_limit: 10
  - name: 'glpk'
    time_limit: 5
qb_solvers:
  enabled: false  # Not needed on edge
```

### 2. Site Deployment (`deployment-site.yaml`)

**Target:** Regional data centers, factories  
**Resources:** 4GB RAM, 16 CPUs  
**Solvers:** Classical + Cubic-bit (CB + QB)

**Characteristics:**
- Balanced resource usage
- Basic ML models (GP)
- Mixed solver portfolio
- Batch and interactive modes
- Regional optimization

**Use Cases:**
- Factory scheduling
- Regional logistics
- Supply chain optimization
- Manufacturing planning

**Key Settings:**
```yaml
deployment: site
bridge: 'FWD→UE→FE→CB→QB'
surrogate:
  enabled: true
  models:
    - type: 'gp'
qb_solvers:
  enabled: true
  methods:
    - 'tensor_decomposition'
    - 'lifted_relaxation'
```

### 3. Hub Deployment (`deployment-hub.yaml`)

**Target:** HPC centers, research facilities, cloud  
**Resources:** 64GB RAM, 64 CPUs, 2 GPUs  
**Solvers:** Full suite (CB + QB + QC)

**Characteristics:**
- Maximum performance
- Full ML suite (GNN, GP, Transformer)
- All solvers including quantum
- Large-scale optimization
- Research and development

**Use Cases:**
- Aircraft design optimization
- Constellation scheduling
- Large-scale logistics
- Portfolio optimization
- R&D experiments

**Key Settings:**
```yaml
deployment: hub
bridge: 'QS→FWD→UE→FE→CB→QB→QC'
surrogate:
  enabled: true
  models:
    - type: 'gnn'
      device: 'cuda'
    - type: 'gp'
    - type: 'transformer'
      device: 'cuda'
qc_gateway:
  enabled: true
  providers:
    - name: 'ibm_quantum'
    - name: 'dwave'
```

## Configuration Structure

Each configuration file includes:

```yaml
version: '1.0'
deployment: <edge|site|hub>
bridge: 'QS→FWD→UE→FE→CB→QB'

# Bridge configurations
pcan:
  enabled: true
  cache_size: <size>
  s1000d_aware: <bool>
  ata_mapping: <bool>

surrogate:
  enabled: <bool>
  models: [...]

strategy:
  enabled: <bool>
  algorithm: <algorithm>
  exploration_rate: <rate>

arbitration:
  enabled: <bool>
  algorithm: <algorithm>

translator:
  enabled: true
  formats: [...]

# Solver pools
cb_solvers: [...]
qb_solvers: {...}
qc_gateway: {...}

# Integration
map:
  enabled: true
  topics: [...]

utcs:
  enabled: true
  version: 'v5.0'
  evidence_path: <path>
  signing_enabled: <bool>

ethics:
  map_eem: true
  mal_eem: true
  audit_mode: <mode>

# Resources
resources:
  memory_limit: <size>
  cpu_limit: <count>
```

## Selecting a Configuration

Choose based on your deployment environment:

| Scenario | Configuration | Key Factor |
|----------|--------------|------------|
| Drone/UAV | Edge | Limited resources, real-time |
| Factory floor | Site | Balanced performance |
| Regional DC | Site | Moderate workloads |
| HPC cluster | Hub | Maximum capability |
| Cloud research | Hub | Full features + quantum |

## Customization

To create a custom configuration:

1. Copy the closest matching configuration
2. Adjust resource limits
3. Enable/disable solver pools
4. Configure ML models
5. Set evidence paths
6. Test thoroughly

**Example:**
```bash
# Copy site config as base
cp deployment-site.yaml deployment-custom.yaml

# Edit as needed
vim deployment-custom.yaml

# Validate
python scripts/validate_config.py deployment-custom.yaml
```

## Validation

Validate configuration before deployment:

```bash
# Check syntax
yamllint deployment-*.yaml

# Validate against schema (when available)
python scripts/validate_config.py config/deployment-hub.yaml
```

## Environment Variables

Override configuration values via environment variables:

```bash
export QAIM2_DEPLOYMENT=hub
export QAIM2_MAP_BROKER=broker.example.com:1883
export QAIM2_EVIDENCE_PATH=/data/qaim-2/evidence
```

## Security Considerations

### Secrets Management

Never commit secrets to configuration files:

```yaml
# DON'T: Inline secrets
map:
  password: 'secret123'  # BAD

# DO: Reference secret files
map:
  password_file: '/secrets/map-password'  # GOOD
```

### Key Management

```yaml
utcs:
  signing_key: '/keys/qaim-2-private.pem'  # Restrict to 600
qc_gateway:
  providers:
    - name: 'ibm_quantum'
      token_file: '/keys/ibm_token'  # Restrict to 600
```

## Performance Tuning

### Edge Optimization
- Minimize cache sizes
- Use lightweight solvers only
- Disable ML models
- Reduce time limits

### Hub Optimization
- Enable GPU acceleration
- Increase cache sizes
- Enable all ML models
- Use aggressive parallelization

## References

- [README.md](../README.md) - Service overview
- [OPERATIONS.md](../docs/OPERATIONS.md) - Deployment procedures
- [MASTER_WHITEPAPER_4.md](../../WHITEPAPERS/MASTER_WHITEPAPER_4.md) - Configuration details

---

*QAIM-2 Configuration Management*  
*Version: 1.0*  
*Last Updated: 2025-10-03*
