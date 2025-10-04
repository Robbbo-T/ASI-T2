#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# find_domain_dirs.sh
#
# Utility to find directories under PRODUCTS/.../domains/<DOMAIN>/{ata,cax,qox,pax}/
# that match specific patterns for ATA chapters, CAx tools, QOx problems, and PAx packages.
#
# Usage:
#   ./find_domain_dirs.sh [OPTIONS]
#
# Options:
#   -r, --root DIR      Root directory to search (default: PRODUCTS)
#   -t, --type TYPE     Filter by type: ata, cax, qox, pax, or all (default: all)
#   -h, --help          Show this help message
#
# Examples:
#   # Find all subdirectories under ata/cax/qox/pax
#   ./find_domain_dirs.sh
#
#   # Find only ATA directories
#   ./find_domain_dirs.sh --type ata
#
#   # Search in a different root
#   ./find_domain_dirs.sh --root /path/to/products
#

set -euo pipefail

# Default values
ROOT="PRODUCTS"
TYPE="all"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Help function
show_help() {
    sed -n '3,26p' "$0" | sed 's/^# //' | sed 's/^#//'
    exit 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -r|--root)
            ROOT="$2"
            shift 2
            ;;
        -t|--type)
            TYPE="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            ;;
        *)
            echo -e "${RED}Error: Unknown option $1${NC}" >&2
            echo "Use --help for usage information" >&2
            exit 1
            ;;
    esac
done

# Validate root directory
if [[ ! -d "$ROOT" ]]; then
    echo -e "${RED}Error: Root directory '$ROOT' does not exist${NC}" >&2
    exit 1
fi

# Validate type
if [[ "$TYPE" != "all" && "$TYPE" != "ata" && "$TYPE" != "cax" && "$TYPE" != "qox" && "$TYPE" != "pax" ]]; then
    echo -e "${RED}Error: Invalid type '$TYPE'. Must be: all, ata, cax, qox, or pax${NC}" >&2
    exit 1
fi

# Build regex pattern based on type
if [[ "$TYPE" == "all" ]]; then
    PATTERN=".*/domains/[^/]+/(ata|cax|qox|pax)/.*"
else
    PATTERN=".*/domains/[^/]+/${TYPE}/.*"
fi

# Find directories matching the pattern
# Using -regextype posix-extended to support modern regex syntax with ()|
echo -e "${GREEN}Searching for ${TYPE} directories under ${ROOT}/...${NC}" >&2
find "$ROOT" -type d -regextype posix-extended -regex "$PATTERN" 2>/dev/null | sort

# Exit with appropriate status
if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
    echo -e "${RED}Error: find command failed${NC}" >&2
    exit 1
fi
