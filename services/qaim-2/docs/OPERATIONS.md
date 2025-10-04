# QAIM-2 Operations Manual

## Deployment

### Prerequisites

- Python 3.8+
- YAML configuration parser
- For QB: NumPy, SciPy
- For QC: Quantum provider SDKs (optional)

### Installation

```bash
# Install core dependencies
pip install pyyaml numpy scipy

# For quantum (optional)
pip install qiskit dwave-ocean-sdk
```

### Configuration Selection

Choose deployment configuration based on environment:

```bash
# Edge (UAVs, embedded systems)
cp config/deployment-edge.yaml config/active-config.yaml

# Site (regional data centers)
cp config/deployment-site.yaml config/active-config.yaml

# Hub (HPC, research)
cp config/deployment-hub.yaml config/active-config.yaml
```

### Starting the Service

```bash
# Python SDK mode
python example.py

# Future: REST API mode
python -m qaim_2.server --config config/active-config.yaml
```

## Operations

### Monitoring

#### Check Service Status

```bash
# View logs
tail -f /var/log/qaim-2/qaim-2.log

# Check evidence generation
ls -la /data/qaim-2/evidence/
```

#### Performance Metrics

Monitor key metrics:
- Solve time per request
- Solver selection accuracy
- Resource utilization (CPU, memory)
- Evidence generation time

### Maintenance

#### Evidence Cleanup

```bash
# Archive old evidence (keep last 90 days)
find /data/qaim-2/evidence/ -mtime +90 -exec mv {} /archive/ \;
```

#### Cache Management

```bash
# Clear PCAN cache
rm -rf /var/cache/qaim-2/pcan/*

# Clear model cache
rm -rf /var/cache/qaim-2/models/*
```

### Troubleshooting

#### Solver Not Available

```
Error: Solver cb_gurobi not available
```

**Solution:** Check solver configuration and license:
```bash
# Verify Gurobi license
export GRB_LICENSE_FILE=/opt/gurobi/gurobi.lic
gurobi_cl --license
```

#### High Memory Usage

**Solution:** Reduce cache sizes in config:
```yaml
pcan:
  cache_size: 1000  # Reduce from 10000
```

#### Slow Optimization

**Solution:** 
1. Use simpler solvers for small problems
2. Reduce time limits
3. Enable QB approximations

#### Evidence Generation Failure

```
Error: Failed to generate UTCS evidence
```

**Solution:** Check evidence path permissions:
```bash
chmod 755 /data/qaim-2/evidence/
chown qaim-2:qaim-2 /data/qaim-2/evidence/
```

## Security

### Authentication

Configure MAP broker authentication:
```yaml
map:
  broker: 'broker:8883'
  username: 'qaim-2'
  password_file: '/secrets/map-password'
  tls_enabled: true
```

### Evidence Signing

Enable cryptographic signing:
```yaml
utcs:
  signing_enabled: true
  signing_key: '/keys/qaim-2-private.pem'
```

Generate signing key:
```bash
openssl genrsa -out qaim-2-private.pem 2048
openssl rsa -in qaim-2-private.pem -pubout -out qaim-2-public.pem
```

### Access Control

Restrict file permissions:
```bash
chmod 600 /keys/qaim-2-private.pem
chmod 600 /secrets/*
```

## Backup & Recovery

### Evidence Backup

```bash
# Daily backup
tar -czf evidence-$(date +%Y%m%d).tar.gz /data/qaim-2/evidence/

# Upload to S3 (example)
aws s3 cp evidence-*.tar.gz s3://asi-t2-backups/qaim-2/
```

### Configuration Backup

```bash
# Backup configs
cp -r config/ /backup/qaim-2-config-$(date +%Y%m%d)/
```

### Recovery

```bash
# Restore evidence
tar -xzf evidence-20251003.tar.gz -C /data/qaim-2/

# Verify integrity
utcs verify /data/qaim-2/evidence/*.json
```

## Scaling

### Horizontal Scaling

Deploy multiple instances with load balancer:

```yaml
# instance-1.yaml
deployment: site
instance_id: 'qaim-2-site-1'

# instance-2.yaml  
deployment: site
instance_id: 'qaim-2-site-2'
```

### Vertical Scaling

Adjust resource limits:

```yaml
resources:
  memory_limit: '16G'  # Increase for larger problems
  cpu_limit: 32        # More threads for classical solvers
```

### Solver Pool Scaling

Add more solvers to pool:

```yaml
cb_solvers:
  - name: 'gurobi-1'
    endpoint: 'solver-pool-1:9001'
  - name: 'gurobi-2'
    endpoint: 'solver-pool-2:9001'
```

## Performance Optimization

### Solver Selection Tuning

Adjust exploration rate:
```yaml
strategy:
  exploration_rate: 0.05  # Reduce for more exploitation
```

### Model Caching

Enable aggressive caching:
```yaml
surrogate:
  cache_predictions: true
  cache_ttl: 3600  # seconds
```

### Async Processing

Configure async workers:
```yaml
async:
  workers: 16
  queue_size: 1000
```

## Compliance & Audit

### Ethics Checks

Enable strict mode:
```yaml
ethics:
  map_eem: true
  mal_eem: true
  audit_mode: 'strict'
  review_required: true
```

### Evidence Audit

```bash
# Generate audit report
python scripts/audit_evidence.py --start 2025-10-01 --end 2025-10-03

# Verify all signatures
for f in /data/qaim-2/evidence/*.json; do
  cosign verify --key qaim-2-public.pem "$f"
done
```

### Standards Compliance

Verify compliance:
```bash
# Check S1000D integration
python scripts/validate_s1000d.py

# Check ATA mapping
python scripts/validate_ata.py

# Generate compliance report
python scripts/compliance_report.py --output report.pdf
```

## Emergency Procedures

### Service Restart

```bash
# Graceful restart
systemctl restart qaim-2

# Force restart
systemctl kill -s KILL qaim-2
systemctl start qaim-2
```

### Fallback Mode

Enable emergency fallback:
```yaml
emergency:
  fallback_solver: 'cb_glpk'
  bypass_ai_bridges: true
  minimal_evidence: true
```

### Incident Response

1. Stop service: `systemctl stop qaim-2`
2. Backup evidence: `tar -czf incident-evidence.tar.gz /data/qaim-2/`
3. Review logs: `grep ERROR /var/log/qaim-2/*.log`
4. Contact support with incident ID

---

*For API details, see [API.md](API.md)*  
*For configuration reference, see [../config/](../config/)*
