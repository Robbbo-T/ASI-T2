#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TeknIA TOKENS (TT) CLI Tool
Manage the append-only ledger for knowledge exchange budget tracking.
"""
import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CONF = ROOT / "finance" / "teknia.tokenomics.json"
LEDG = ROOT / "finance" / "ledger" / "tt-ledger.jsonl"
BADG = ROOT / "finance" / "badges" / "tt-balance.json"

def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def read_conf():
    return json.loads(CONF.read_text(encoding="utf-8"))

def iter_ledger():
    if not LEDG.exists():
        return
    with LEDG.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)

def last_tx():
    last = None
    for tx in iter_ledger() or []:
        last = tx
    return last

def sha256_of(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def append_tx(tx):
    LEDG.parent.mkdir(parents=True, exist_ok=True)
    with LEDG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(tx, ensure_ascii=False) + "\n")

def balances():
    bal = {}
    for tx in iter_ledger() or []:
        frm, to, amt = tx.get("from"), tx.get("to"), tx.get("amount", 0.0)
        if frm not in ("mint", None):
            bal[frm] = bal.get(frm, 0.0) - amt
        if to:
            bal[to] = bal.get(to, 0.0) + amt
    return bal

def verify_chain():
    prev_id = "genesis"
    prev_hash = "genesis"
    for tx in iter_ledger() or []:
        # 1) continuity by id
        if tx.get("prev") != prev_id:
            return False, f"Prev mismatch at {tx.get('id')}: {tx.get('prev')} != {prev_id}"
        # 2) continuity by hash
        if tx.get("prev_hash") != prev_hash:
            return False, f"Prev hash mismatch at {tx.get('id')}"
        # 3) integrity of current record
        payload = {k: v for k, v in tx.items() if k != "hash"}
        h = sha256_of(payload)
        if h != tx.get("hash"):
            return False, f"Hash mismatch at {tx.get('id')}"
        prev_id = tx.get("id")
        prev_hash = tx.get("hash")
    return True, "OK"

def new_id():
    lt = last_tx()
    if not lt:
        return "ttx_000001"
    n = int(lt["id"].split("_")[1]) + 1
    return f"ttx_{n:06d}"

def tx_record(t_type, amount, frm, to, ref, memo):
    lt = last_tx()
    pid = lt["id"] if lt else "genesis"
    phash = lt["hash"] if lt else "genesis"
    rec = {
        "id": new_id(),
        "ts": now(),
        "prev": pid,
        "prev_hash": phash,
        "type": t_type.upper(),
        "from": frm,
        "to": to,
        "amount": round(float(amount), 3),
        "unit": "TT",
        "ref": ref,
        "memo": memo
    }
    rec["hash"] = sha256_of({k: v for k, v in rec.items() if k != "hash"})
    return rec

def cmd_init(args):
    if LEDG.exists() and not args.force:
        print("Ledger exists. Use --force to re-generate.", file=sys.stderr)
        sys.exit(1)
    conf = read_conf()
    tx = tx_record("MINT", conf["initial_mint"], "mint", "treasury",
                   {"event": "init", "run_id": 0, "pr": 0}, "genesis mint")
    LEDG.unlink(missing_ok=True)
    append_tx(tx)
    print("Initialized:", tx["id"])

def cmd_tx(args):
    rec = tx_record(args.type, args.amount, args.from_holder, args.to_holder,
                    {"event": "manual", "run_id": 0, "pr": args.pr}, args.memo or "")
    append_tx(rec)
    print("OK:", rec["id"])

def cmd_auto(args):
    conf = read_conf()
    event = args.event
    actor = args.actor or "user/unknown"
    ref = {"event": event, "run_id": int(args.run_id or 0), "pr": int(args.pr or 0)}

    if event == "cxp-publish" and conf["auto"].get("reward_on_publish", False):
        amt = conf["prices"]["cxp_publish_reward"]
        rec = tx_record("CREDIT", amt, "treasury", f"user/{actor}", ref, "CXP publish reward")
        append_tx(rec)
        print("CREDIT:", rec["id"])

    if event == "cxp-consume" and conf["auto"].get("charge_on_consume", True):
        amt = conf["prices"]["cxp_consume_cost"]
        rec = tx_record("DEBIT", amt, "treasury", "sink:consume", ref, "CXP consume cost")
        append_tx(rec)
        print("DEBIT:", rec["id"])

def cmd_balance(_):
    bal = balances()
    print(json.dumps(bal, indent=2, ensure_ascii=False))

def cmd_verify(_):
    ok, msg = verify_chain()
    if not ok:
        print(msg)
        sys.exit(1)
    print("OK")
    # badge
    try:
        conf = read_conf()
        if conf.get("badges", {}).get("enabled"):
            bals = balances()
            total = float(bals.get("treasury", 0.0))
            BADG.parent.mkdir(parents=True, exist_ok=True)
            BADG.write_text(json.dumps({
                "schemaVersion": 1,
                "label": conf["badges"]["label"],
                "message": f"{total:.3f} TT",
                "color": conf["badges"]["color"]
            }), encoding="utf-8")
    except Exception as e:
        print("badge skipped:", e, file=sys.stderr)

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    
    p = sub.add_parser("init")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_init)
    
    p = sub.add_parser("tx")
    p.add_argument("--type", required=True, choices=["mint", "burn", "debit", "credit", "transfer"])
    p.add_argument("--amount", required=True, type=float)
    p.add_argument("--from", dest="from_holder", required=True)
    p.add_argument("--to", dest="to_holder", required=True)
    p.add_argument("--pr", type=int, default=0)
    p.add_argument("--memo")
    p.set_defaults(func=cmd_tx)
    
    p = sub.add_parser("auto")
    p.add_argument("--event", required=True, choices=["cxp-publish", "cxp-consume"])
    p.add_argument("--actor")
    p.add_argument("--run-id")
    p.add_argument("--pr")
    p.set_defaults(func=cmd_auto)
    
    p = sub.add_parser("balance")
    p.set_defaults(func=cmd_balance)
    
    p = sub.add_parser("verify")
    p.set_defaults(func=cmd_verify)
    
    args = ap.parse_args()
    if not hasattr(args, "func"):
        ap.print_help()
        sys.exit(2)
    args.func(args)

if __name__ == "__main__":
    main()
