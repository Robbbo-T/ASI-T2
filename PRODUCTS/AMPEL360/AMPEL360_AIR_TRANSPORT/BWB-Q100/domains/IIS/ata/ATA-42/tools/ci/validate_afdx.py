#!/usr/bin/env python3
"""AFDX VL Table Validator for BWB-Q100 IMA (ATA-42)"""
import csv
import sys
import pathlib

# Path resolution: from tools/ci/ up to ATA-42 root, then down to buses/afdx/
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
ATA42_ROOT = SCRIPT_DIR.parent.parent
CSV = ATA42_ROOT / "buses/afdx/vl_table.csv"

ALLOWED_BAGS = {1, 2, 4, 8, 16, 32, 64, 128}
LINK_KBPS = 100_000  # 100 Mbps per network
WARN_UTIL = 0.75

def rows():
    """Yield non-comment rows from the CSV"""
    with open(CSV, newline="") as f:
        for r in csv.reader(f):
            if not r or r[0].startswith("#"):
                continue
            yield r

ok, agg = True, 0.0
for r in rows():
    if len(r) < 13:
        print(f"::error ::Row has {len(r)} columns, expected ≥13 → {r}")
        ok = False
        continue
    
    (vl, src, sinks, tclass, bag_ms, frames, l2bytes, udp, red, queue, qos, bw_decl, *_) = r
    
    # Validate BAG
    try:
        bag = int(bag_ms)
        assert bag in ALLOWED_BAGS
    except:
        print(f"::error ::{vl} BAG_ms must be one of {sorted(ALLOWED_BAGS)}")
        ok = False
    
    # Validate frames per BAG
    try:
        nfrm = int(frames)
        assert nfrm >= 1
    except:
        print(f"::error ::{vl} Frames_per_BAG must be ≥1")
        ok = False
    
    # Validate L2 bytes
    try:
        l2 = int(l2bytes)
        assert 64 <= l2 <= 1518
    except:
        print(f"::error ::{vl} Max_L2_Bytes must be 64..1518")
        ok = False
    
    # Calculate and validate bandwidth
    try:
        bw_calc = (nfrm * l2 * 8) / bag
        bw_stated = float(bw_decl)
        if abs(bw_calc - bw_stated) > 1.0:
            print(f"::warning ::{vl} BW mismatch: calculated {bw_calc:.1f} kbps vs stated {bw_stated} kbps")
        agg += bw_calc
    except:
        print(f"::error ::{vl} Cannot calculate bandwidth")
        ok = False

# Check aggregate utilization
util = agg / LINK_KBPS
if util > 1.0:
    print(f"::error ::Aggregate BW {agg:.0f} kbps exceeds link capacity {LINK_KBPS} kbps ({util*100:.1f}%)")
    ok = False
elif util > WARN_UTIL:
    print(f"::warning ::Aggregate BW {agg:.0f} kbps is {util*100:.1f}% of link (warn threshold {WARN_UTIL*100:.0f}%)")

if ok:
    print(f"✅ AFDX VL table valid. Aggregate BW: {agg:.0f} kbps ({util*100:.1f}% utilization)")
    sys.exit(0)
else:
    print("❌ AFDX VL table validation FAILED")
    sys.exit(1)
