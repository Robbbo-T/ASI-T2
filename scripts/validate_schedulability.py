#!/usr/bin/env python3
"""
Schedulability Validator for ARINC-653 Partitions

Validates that task schedules meet timing requirements with adequate margin.
Enforces CAST-32A methodology for multicore interference analysis.

Usage:
  python validate_schedulability.py --manifest <manifest_file> --wcet <wcet_csv> --jitter <jitter_json> --margin <margin_pct>
"""

import argparse
import json
import csv
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple

import yaml


def load_manifest(manifest_path: Path) -> Dict[str, Any]:
    """Load ARINC-653 partition manifest"""
    try:
        with open(manifest_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading manifest {manifest_path}: {e}")
        sys.exit(1)


def load_wcet_data(wcet_path: Path) -> Dict[str, float]:
    """Load WCET data from CSV file"""
    wcet_data = {}
    try:
        with open(wcet_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                task_name = row['task']
                wcet_ms = float(row['wcet_ms'])
                wcet_data[task_name] = wcet_ms
    except Exception as e:
        print(f"❌ Error loading WCET data {wcet_path}: {e}")
        sys.exit(1)
    
    return wcet_data


def load_jitter_data(jitter_path: Path) -> Dict[str, float]:
    """Load jitter data from JSON file"""
    try:
        with open(jitter_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading jitter data {jitter_path}: {e}")
        sys.exit(1)


def validate_schedulability(manifest: Dict[str, Any], wcet_data: Dict[str, float], 
                          jitter_data: Dict[str, float], margin_pct: float) -> Tuple[bool, List[str]]:
    """Validate schedulability according to CAST-32A methodology"""
    
    issues = []
    schedule = manifest.get('schedule', {})
    major_frame_ms = schedule.get('major_frame_ms', 0)
    windows = schedule.get('windows', [])
    
    if major_frame_ms <= 0:
        issues.append("Invalid major frame time")
        return False, issues
    
    total_budget = 0
    for window in windows:
        task_name = window.get('task', '')
        budget_ms = window.get('budget_ms', 0)
        
        if task_name not in wcet_data:
            issues.append(f"Missing WCET data for task {task_name}")
            continue
            
        wcet_ms = wcet_data[task_name]
        
        # Apply margin and jitter
        jitter_ms = jitter_data.get(task_name, 0.0)
        required_budget = wcet_ms * (1 + margin_pct / 100) + jitter_ms
        
        if budget_ms < required_budget:
            issues.append(f"Task {task_name}: budget {budget_ms}ms < required {required_budget:.2f}ms")
        
        total_budget += budget_ms
    
    # Check total schedulability
    if total_budget > major_frame_ms:
        issues.append(f"Total budget {total_budget}ms exceeds major frame {major_frame_ms}ms")
    
    # Check for adequate slack
    slack_pct = ((major_frame_ms - total_budget) / major_frame_ms) * 100
    if slack_pct < margin_pct:
        issues.append(f"Insufficient slack {slack_pct:.1f}% < required {margin_pct}%")
    
    return len(issues) == 0, issues


def validate_multicore_interference(jitter_data: Dict[str, float]) -> Tuple[bool, List[str]]:
    """Validate multicore interference meets CAST-32A requirements"""
    
    issues = []
    p999_threshold_us = 80  # From requirements
    
    for task, jitter_us in jitter_data.items():
        if jitter_us > p999_threshold_us:
            issues.append(f"Task {task}: p99.9 jitter {jitter_us}μs > threshold {p999_threshold_us}μs")
    
    return len(issues) == 0, issues


def main():
    parser = argparse.ArgumentParser(description='Validate ARINC-653 schedulability')
    parser.add_argument('--manifest', type=Path, required=True, help='Partition manifest YAML file')
    parser.add_argument('--wcet', type=Path, required=True, help='WCET data CSV file')
    parser.add_argument('--jitter', type=Path, required=True, help='Jitter data JSON file')
    parser.add_argument('--margin', type=float, required=True, help='Required margin percentage')
    
    args = parser.parse_args()
    
    print("🔍 Schedulability Validation (CAST-32A)")
    print(f"Manifest: {args.manifest}")
    print(f"WCET: {args.wcet}")
    print(f"Jitter: {args.jitter}")
    print(f"Margin: {args.margin}%")
    print("=" * 50)
    
    # Load data
    manifest = load_manifest(args.manifest)
    wcet_data = load_wcet_data(args.wcet)
    jitter_data = load_jitter_data(args.jitter)
    
    all_passed = True
    
    # Validate schedulability
    sched_ok, sched_issues = validate_schedulability(manifest, wcet_data, jitter_data, args.margin)
    print(f"Schedule Check: {'PASS' if sched_ok else 'FAIL'}")
    if not sched_ok:
        for issue in sched_issues:
            print(f"  ❌ {issue}")
        all_passed = False
    
    # Validate multicore interference
    mc_ok, mc_issues = validate_multicore_interference(jitter_data)
    print(f"Multicore Check: {'PASS' if mc_ok else 'FAIL'}")
    if not mc_ok:
        for issue in mc_issues:
            print(f"  ❌ {issue}")
        all_passed = False
    
    if all_passed:
        print("\n✅ SUCCESS: Schedulability validation passed")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: Schedulability validation failed")
        sys.exit(1)


if __name__ == "__main__":
    main()