#!/usr/bin/env bash
set -euo pipefail

BASE="domains/AAA/cax/CAD/assemblies"

# Airframes-only list
IDS=(001 002 003 004 005 006 007 008 009 010 012 016 017 018 019 026 027 028 031 032)

for i in "${IDS[@]}"; do
  asm_id=$(printf "ASM-%03d" $((10#$i)))
  dir="$BASE/$asm_id"
  mkdir -p "$dir"/{models,drawings,icd}

  # Copy template metadata if missing
  if [[ ! -f "$dir/metadata.yaml" ]]; then
    cp "$BASE/template/metadata.yaml" "$dir/metadata.yaml"
    # sed portability (BSD/macOS vs GNU)
    if sed --version >/dev/null 2>&1; then
      sed -i "s/ASM-XXX/$asm_id/g" "$dir/metadata.yaml"
    else
      sed -i '' -e "s/ASM-XXX/$asm_id/g" "$dir/metadata.yaml"
    fi
  fi

  # Minimal READMEs
  : > "$dir/models/README.md"
  echo "# $asm_id Drawings" > "$dir/drawings/README.md"
  echo "# $asm_id Interface Control" > "$dir/icd/README.md"
done

echo "✅ Created airframes assembly folder structure"