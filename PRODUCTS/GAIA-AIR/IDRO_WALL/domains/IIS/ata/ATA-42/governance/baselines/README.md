# Baselines

Configuration baselines and immutable snapshots for ATA-42 IMA system.

## Files

- **baseline_index.yaml** — Index of all baselines with paths, hashes, and metadata

## Purpose

Baselines represent frozen, approved configurations of the IMA system. Each baseline includes:
- Configuration files (partition.xml, schedule.xml, manifest.yaml)
- SHA-256 hashes for integrity verification
- Approval references
- Test results and evidence
- QS/UTCS anchors for immutability

## Baseline Process

1. Configuration reaches stable, tested state
2. All required approvals obtained
3. Evidence bundle compiled
4. Hashes computed and recorded
5. QS anchor generated
6. Baseline locked (immutable)

## Usage

Baselines serve as reference points for:
- Regression testing
- Rollback scenarios
- Compliance audits
- Configuration comparison
- Change impact analysis
