#!/usr/bin/env bash
set -euo pipefail
# Generate reproducible sha256 list for given paths (files or dirs).
# Usage: ./generate_checksums.sh <path> [<path>...]
# Output: checksums.sha256 in current directory.

tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT

# collect files
for target in "$@"; do
  if [ -d "$target" ]; then
    find "$target" -type f -print0
  else
    printf '%s\0' "$target"
  fi
done | LC_ALL=C sort -z | xargs -0 -I{} sha256sum "{}" > "$tmp"

mv "$tmp" checksums.sha256
echo "Wrote checksums.sha256"
