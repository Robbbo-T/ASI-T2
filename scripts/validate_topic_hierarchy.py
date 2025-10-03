#!/usr/bin/env python3
"""
Topic Hierarchy Validator

Validates ASI-T2 MAP topic naming conventions and hierarchy structure.
Ensures compliance with integration whitepaper specifications.

Usage:
  python validate_topic_hierarchy.py <topic_or_file>
  python validate_topic_hierarchy.py --batch topics.txt
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Tuple, List, Dict, Any

# Valid domain codes (from TFA domains/)
VALID_DOMAINS = {
    "AAA", "AAP", "CCC", "CQH", "DDD", "EDI", "EEE", "EER",
    "IIF", "IIS", "LCC", "LIB", "MEC", "OOO", "PPP", "FLEET"
}

# Valid bridge layers
VALID_LAYERS = {"QS", "FWD", "UE", "FE", "CB", "QB"}

# Valid contracts
VALID_CONTRACTS = {"control", "telemetry", "health", "log"}

# Topic pattern: map/<major>/<contract>/<program>/<domain>/<group>/<llc>/<layer>
TOPIC_PATTERN = re.compile(
    r'^map/(?P<major>\d+)/(?P<contract>[a-z]+)/(?P<program>[A-Z0-9_-]+)'
    r'/(?P<domain>[A-Z]{3,5})/(?P<group>[A-Z0-9_]+)/'
    r'(?P<llc>[A-Z]{2,3})/(?P<layer>[A-Z]{2,3})$'
)

# Simplified patterns for health and log (no layer required)
HEALTH_PATTERN = re.compile(
    r'^map/(?P<major>\d+)/health/(?P<program>[A-Z0-9_-]+)(/[A-Z0-9_]+)*$'
)

LOG_PATTERN = re.compile(
    r'^map/(?P<major>\d+)/log/(?P<program>[A-Z0-9_-]+)(/[A-Z0-9_]+)*$'
)


def validate_topic(topic: str) -> Tuple[bool, List[str]]:
    """
    Validate a single topic string against MAP conventions.
    
    Returns:
        (is_valid, issues_list)
    """
    issues = []
    
    # Check basic structure
    if not topic.startswith("map/"):
        issues.append("Topic must start with 'map/'")
        return False, issues
    
    parts = topic.split("/")
    
    # Must have at least 3 parts: map/<major>/<contract>
    if len(parts) < 3:
        issues.append(f"Topic too short: {len(parts)} parts, minimum 3 required")
        return False, issues
    
    # Validate major version
    try:
        major = int(parts[1])
        if major != 1:
            issues.append(f"Major version must be 1, got {major}")
    except ValueError:
        issues.append(f"Invalid major version: {parts[1]}")
        return False, issues
    
    # Validate contract
    contract = parts[2]
    if contract not in VALID_CONTRACTS:
        issues.append(f"Invalid contract '{contract}', must be one of {VALID_CONTRACTS}")
        return False, issues
    
    # Special handling for health and log topics
    if contract == "health":
        match = HEALTH_PATTERN.match(topic)
        if not match:
            issues.append("Health topic format invalid")
            return False, issues
        return len(issues) == 0, issues
    
    if contract == "log":
        match = LOG_PATTERN.match(topic)
        if not match:
            issues.append("Log topic format invalid")
            return False, issues
        return len(issues) == 0, issues
    
    # Full validation for control and telemetry topics
    match = TOPIC_PATTERN.match(topic)
    if not match:
        issues.append(f"Topic does not match expected pattern: {topic}")
        issues.append("Expected: map/1/<contract>/<PROGRAM>/<DOMAIN>/<GROUP>/<LLC>/<LAYER>")
        return False, issues
    
    groups = match.groupdict()
    
    # Validate domain
    domain = groups["domain"]
    if domain not in VALID_DOMAINS:
        issues.append(f"Invalid domain '{domain}', must be one of {VALID_DOMAINS}")
    
    # Validate layer
    layer = groups["layer"]
    if layer not in VALID_LAYERS:
        issues.append(f"Invalid layer '{layer}', must be one of {VALID_LAYERS}")
    
    # Check program format (uppercase, alphanumeric, hyphens, underscores)
    program = groups["program"]
    if not re.match(r'^[A-Z0-9_-]+$', program):
        issues.append(f"Program '{program}' must contain only uppercase letters, digits, hyphens, and underscores")
    
    # Check group format
    group = groups["group"]
    if not re.match(r'^[A-Z0-9_]+$', group):
        issues.append(f"Group '{group}' must contain only uppercase letters, digits, and underscores")
    
    # Check LLC format
    llc = groups["llc"]
    if not re.match(r'^[A-Z]{2,3}$', llc):
        issues.append(f"LLC '{llc}' must be 2-3 uppercase letters")
    
    return len(issues) == 0, issues


def validate_layer_consistency(topics: List[str]) -> Tuple[bool, List[str]]:
    """
    Validate that layer ordering is consistent across related topics.
    
    Checks that layers follow bridge semantics: QS → FWD → UE → FE → CB → QB
    """
    issues = []
    layer_order = ["QS", "FWD", "UE", "FE", "CB", "QB"]
    
    # Group topics by program and domain
    groups: Dict[Tuple[str, str], List[str]] = {}
    
    for topic in topics:
        match = TOPIC_PATTERN.match(topic)
        if match:
            program = match.group("program")
            domain = match.group("domain")
            layer = match.group("layer")
            
            key = (program, domain)
            if key not in groups:
                groups[key] = []
            groups[key].append(layer)
    
    # Check ordering within each group
    for (program, domain), layers in groups.items():
        unique_layers = list(set(layers))
        
        # Get indices in canonical order
        try:
            indices = [layer_order.index(layer) for layer in unique_layers]
            sorted_indices = sorted(indices)
            
            if indices != sorted_indices:
                issues.append(
                    f"Layer ordering violation in {program}/{domain}: "
                    f"expected {[layer_order[i] for i in sorted_indices]}, "
                    f"got {unique_layers}"
                )
        except ValueError as e:
            issues.append(f"Unknown layer in {program}/{domain}: {e}")
    
    return len(issues) == 0, issues


def validate_file(filepath: Path) -> Tuple[int, int, List[str]]:
    """
    Validate topics from a file (one topic per line).
    
    Returns:
        (valid_count, invalid_count, issues_list)
    """
    valid_count = 0
    invalid_count = 0
    all_issues = []
    topics = []
    
    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                topic = line.strip()
                if not topic or topic.startswith('#'):
                    continue
                
                topics.append(topic)
                valid, issues = validate_topic(topic)
                
                if valid:
                    valid_count += 1
                else:
                    invalid_count += 1
                    all_issues.append(f"Line {line_num}: {topic}")
                    for issue in issues:
                        all_issues.append(f"  ❌ {issue}")
        
        # Check layer consistency across all topics
        if topics:
            consistent, consistency_issues = validate_layer_consistency(topics)
            if not consistent:
                all_issues.append("\n🔍 Layer Consistency Issues:")
                all_issues.extend(f"  ❌ {issue}" for issue in consistency_issues)
    
    except Exception as e:
        all_issues.append(f"Error reading file: {e}")
        return valid_count, invalid_count, all_issues
    
    return valid_count, invalid_count, all_issues


def main():
    parser = argparse.ArgumentParser(
        description='Validate ASI-T2 MAP topic hierarchy and naming conventions'
    )
    parser.add_argument(
        'topic_or_file',
        type=str,
        help='Single topic string or path to file with topics (one per line)'
    )
    parser.add_argument(
        '--batch',
        action='store_true',
        help='Treat input as file path'
    )
    
    args = parser.parse_args()
    
    print("🔍 ASI-T2 MAP Topic Hierarchy Validation")
    print("=" * 60)
    
    if args.batch or Path(args.topic_or_file).is_file():
        # Validate file
        filepath = Path(args.topic_or_file)
        valid_count, invalid_count, issues = validate_file(filepath)
        
        print(f"\nFile: {filepath}")
        print(f"Valid topics: {valid_count}")
        print(f"Invalid topics: {invalid_count}")
        
        if issues:
            print("\nIssues found:")
            for issue in issues:
                print(issue)
        
        if invalid_count == 0 and not any("consistency" in i.lower() for i in issues):
            print("\n✅ SUCCESS: All topics are valid")
            sys.exit(0)
        else:
            print("\n❌ FAILURE: Some topics are invalid")
            sys.exit(1)
    else:
        # Validate single topic
        topic = args.topic_or_file
        valid, issues = validate_topic(topic)
        
        print(f"\nTopic: {topic}")
        print(f"Status: {'VALID ✅' if valid else 'INVALID ❌'}")
        
        if issues:
            print("\nIssues:")
            for issue in issues:
                print(f"  ❌ {issue}")
        
        sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()
