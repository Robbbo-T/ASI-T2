#!/usr/bin/env python3
import argparse, sys, json, yaml, pathlib

def cmd_deploy(args):
    p = pathlib.Path(args.manifest)
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    print(f"[deploy] Manifest: {p}")
    print(f"[deploy] missionId={data.get('missionId')} assets={len(data.get('assets', []))}")
    if args.require_attestation:
        print("[deploy] Attestation REQUIRED → (stub) verifying TPM/TEE evidence... OK")
    print("[deploy] Placement policy:", data.get("placement",{}).get("policy"))
    print("[deploy] DONE (stub).")

def cmd_qos(args):
    q = yaml.safe_load(pathlib.Path('middleware/dds/qos_policies.yaml').read_text(encoding="utf-8"))
    profile = q.get('profiles',{}).get(args.profile)
    if not profile:
        print(f"[qos] Profile '{args.profile}' not found", file=sys.stderr); sys.exit(1)
    print(f"[qos] Profile: {args.profile} → {profile}")
    if args.asset: print(f"[qos] (stub) Auditing asset {args.asset} against profile... OK")

def cmd_fdir(args):
    rules = yaml.safe_load(pathlib.Path(args.rules).read_text(encoding="utf-8"))
    print(f"[fdir] Loaded {len(rules)} rules.")
    if args.inject:
        print(f"[fdir] Injecting event {args.inject} → evaluating...")
        print("[fdir] Plan: set_mode(FAILSAFE) → publish → plan_rtl → attest  (stub OK)")

def main():
    ap = argparse.ArgumentParser(prog="metaosctl")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_dep = sub.add_parser("deploy")
    ap_dep.add_argument("manifest")
    ap_dep.add_argument("--require-attestation", action="store_true")
    ap_dep.set_defaults(func=cmd_deploy)

    ap_qos = sub.add_parser("qos")
    sub_q = ap_qos.add_subparsers(dest="qcmd", required=True)
    ap_qos_audit = sub_q.add_parser("audit")
    ap_qos_audit.add_argument("--profile", required=True)
    ap_qos_audit.add_argument("--asset")
    ap_qos_audit.set_defaults(func=cmd_qos)

    ap_fdir = sub.add_parser("fdir")
    sub_f = ap_fdir.add_subparsers(dest="fcmd", required=True)
    ap_fdir_test = sub_f.add_parser("test")
    ap_fdir_test.add_argument("rules")
    ap_fdir_test.add_argument("--inject")
    ap_fdir_test.set_defaults(func=cmd_fdir)

    args = ap.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()