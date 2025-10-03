#!/usr/bin/env python3
"""
Bridge Flow Validator

Validates TFA V2 bridge flow semantics (QS→FWD→UE→FE→CB→QB).
Ensures layer dependencies and data flow are correct.

Usage:
  python validate_bridge_flow.py <config_file>
"""

import argparse
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any, Tuple, Set

# Bridge layer order (canonical)
BRIDGE_ORDER = ["QS", "FWD", "UE", "FE", "CB", "QB"]

# Valid layer transitions (directed edges)
VALID_TRANSITIONS = {
    "QS": ["FWD", "UE"],  # QS can feed FWD or directly to UE
    "FWD": ["UE", "FE"],  # FWD feeds UE or FE
    "UE": ["FE", "CB"],   # UE feeds FE or CB
    "FE": ["CB", "QB"],   # FE coordinates CB/QB
    "CB": ["QB", "FE"],   # CB can optimize with QB or coordinate with FE
    "QB": []              # QB is terminal (advisory only)
}

# Layer semantics (for validation)
LAYER_SEMANTICS = {
    "QS": {
        "description": "Primordial state - origin/reference",
        "role": "state_management",
        "properties": ["immutable", "versioned", "signed"]
    },
    "FWD": {
        "description": "Forward Wave Dynamics - prediction/probability",
        "role": "prediction",
        "properties": ["probabilistic", "time_bounded", "confidence_scored"]
    },
    "UE": {
        "description": "Unit Element - atomic state decision and collapse",
        "role": "execution",
        "properties": ["atomic", "deterministic", "timeout_bounded"]
    },
    "FE": {
        "description": "Federation Entanglement - inter-system coordination",
        "role": "coordination",
        "properties": ["consensus_based", "slo_governed", "multi_party"]
    },
    "CB": {
        "description": "Classical Bit - deterministic computation",
        "role": "computation",
        "properties": ["deterministic", "validated", "certified"]
    },
    "QB": {
        "description": "Bit Cubic (non-quantum) - discrete 3D optimization",
        "role": "advisory",
        "properties": ["advisory_only", "safety_bounded", "fallback_required"]
    }
}


def load_flow_config(filepath: Path) -> Dict[str, Any]:
    """Load bridge flow configuration from YAML file."""
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading config {filepath}: {e}")
        sys.exit(1)


def validate_layer_definitions(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate that all layer definitions are correct."""
    issues = []
    
    layers = config.get('layers', {})
    if not layers:
        issues.append("No layers defined in configuration")
        return False, issues
    
    for layer_name, layer_config in layers.items():
        # Check layer name is valid
        if layer_name not in BRIDGE_ORDER:
            issues.append(f"Invalid layer name: {layer_name}")
            continue
        
        # Check required fields
        required_fields = ['description', 'role']
        for field in required_fields:
            if field not in layer_config:
                issues.append(f"Layer {layer_name}: missing required field '{field}'")
        
        # Validate role matches expected semantics
        expected_role = LAYER_SEMANTICS[layer_name]['role']
        actual_role = layer_config.get('role')
        if actual_role and actual_role != expected_role:
            issues.append(
                f"Layer {layer_name}: role mismatch - "
                f"expected '{expected_role}', got '{actual_role}'"
            )
    
    return len(issues) == 0, issues


def validate_flow_graph(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate the data flow graph between layers."""
    issues = []
    
    flows = config.get('flows', [])
    if not flows:
        issues.append("No flows defined in configuration")
        return False, issues
    
    # Build flow graph
    flow_graph: Dict[str, Set[str]] = {layer: set() for layer in BRIDGE_ORDER}
    
    for flow in flows:
        source = flow.get('from')
        target = flow.get('to')
        
        if not source or not target:
            issues.append(f"Flow missing 'from' or 'to': {flow}")
            continue
        
        # Check layers are valid
        if source not in BRIDGE_ORDER:
            issues.append(f"Invalid source layer in flow: {source}")
            continue
        
        if target not in BRIDGE_ORDER:
            issues.append(f"Invalid target layer in flow: {target}")
            continue
        
        # Check transition is allowed
        if target not in VALID_TRANSITIONS[source]:
            issues.append(
                f"Invalid transition {source} → {target}. "
                f"Valid targets from {source}: {VALID_TRANSITIONS[source]}"
            )
        
        flow_graph[source].add(target)
    
    # Check for cycles (should not have cycles in bridge flow)
    if has_cycle(flow_graph):
        issues.append("Flow graph contains cycles - bridge flow must be acyclic")
    
    # Check that QB is terminal (no outgoing edges)
    if "QB" in flow_graph and flow_graph["QB"]:
        issues.append(f"QB must be terminal (advisory only), found outgoing flows: {flow_graph['QB']}")
    
    return len(issues) == 0, issues


def has_cycle(graph: Dict[str, Set[str]]) -> bool:
    """Check if directed graph has cycles using DFS."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    
    def visit(node):
        if color[node] == GRAY:
            return True  # Back edge found - cycle!
        if color[node] == BLACK:
            return False  # Already visited
        
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if visit(neighbor):
                return True
        color[node] = BLACK
        return False
    
    return any(visit(node) for node in graph if color[node] == WHITE)


def validate_layer_properties(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate that layer properties match expected semantics."""
    issues = []
    
    layers = config.get('layers', {})
    
    for layer_name, layer_config in layers.items():
        if layer_name not in LAYER_SEMANTICS:
            continue
        
        expected_props = LAYER_SEMANTICS[layer_name]['properties']
        actual_props = layer_config.get('properties', [])
        
        # Check QB specific constraints
        if layer_name == "QB":
            # QB must be advisory
            role = layer_config.get('role')
            if role != 'advisory':
                issues.append(f"QB role must be 'advisory', got '{role}'")
            
            # QB must have safety constraints
            if 'safety' not in layer_config:
                issues.append("QB layer must define 'safety' constraints")
            else:
                safety = layer_config['safety']
                required_safety = ['max_age_s', 'fallback', 'accept_predicates']
                for field in required_safety:
                    if field not in safety:
                        issues.append(f"QB safety must define '{field}'")
        
        # Check QS specific constraints
        if layer_name == "QS":
            # QS must be immutable
            if 'immutable' not in actual_props:
                issues.append("QS must have 'immutable' property")
        
        # Check CB specific constraints
        if layer_name == "CB":
            # CB must be deterministic
            if 'deterministic' not in actual_props:
                issues.append("CB must have 'deterministic' property")
    
    return len(issues) == 0, issues


def validate_utcs_requirements(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate UTCS evidence requirements."""
    issues = []
    
    utcs = config.get('utcs', {})
    if not utcs:
        issues.append("UTCS configuration not defined")
        return False, issues
    
    # Check required UTCS fields
    required = ['require_signature', 'record_backend', 'bundle_format']
    for field in required:
        if field not in utcs:
            issues.append(f"UTCS missing required field: {field}")
    
    # Signature and backend recording should be enabled
    if not utcs.get('require_signature', False):
        issues.append("UTCS signatures should be enabled for evidence")
    
    if not utcs.get('record_backend', False):
        issues.append("UTCS backend recording should be enabled for audit trail")
    
    # Check bundle format
    bundle_format = utcs.get('bundle_format')
    if bundle_format != 'UTCS-v5.0':
        issues.append(f"Expected UTCS bundle format 'UTCS-v5.0', got '{bundle_format}'")
    
    return len(issues) == 0, issues


def main():
    parser = argparse.ArgumentParser(
        description='Validate TFA V2 bridge flow semantics'
    )
    parser.add_argument(
        'config_file',
        type=Path,
        help='Bridge flow configuration file (YAML)'
    )
    
    args = parser.parse_args()
    
    print("🔍 TFA V2 Bridge Flow Validation")
    print(f"Config: {args.config_file}")
    print("=" * 60)
    
    # Load configuration
    config = load_flow_config(args.config_file)
    
    all_passed = True
    validators = [
        ("Layer Definitions", validate_layer_definitions),
        ("Flow Graph", validate_flow_graph),
        ("Layer Properties", validate_layer_properties),
        ("UTCS Requirements", validate_utcs_requirements)
    ]
    
    for name, validator in validators:
        valid, issues = validator(config)
        status = "PASS ✅" if valid else "FAIL ❌"
        print(f"\n{name}: {status}")
        
        if not valid:
            for issue in issues:
                print(f"  ❌ {issue}")
            all_passed = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ SUCCESS: Bridge flow configuration is valid")
        print("\nBridge Order: " + " → ".join(BRIDGE_ORDER))
        sys.exit(0)
    else:
        print("❌ FAILURE: Bridge flow validation failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
