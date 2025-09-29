#!/usr/bin/env bash
set -euo pipefail
BASE="PRODUCTS/AMPEL360/AMPEL360_AIR_TRANSPORT/BWB-Q100/domains/IIS/ata/ATA-22"
mkdir -p "$BASE"/{architecture,requirements/LLR,icd,config/gains,software/src/ata22,software/tests,sitl,qox}
touch "$BASE/software/src/ata22/__init__.py"
echo "✅ ATA-22 scaffold created at $BASE"