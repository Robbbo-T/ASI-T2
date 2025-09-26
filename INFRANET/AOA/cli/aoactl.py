#!/usr/bin/env python3
import argparse, requests, sys, yaml, json, os

BASE = os.environ.get("AOA_URL", "http://127.0.0.1:8000")

def post(path, payload):
    r = requests.post(BASE + path, json=payload)
    r.raise_for_status()
    return r.json()

def cmd_cap_publish(args):
    for p in args.paths:
        data = yaml.safe_load(open(p, "r"))
        out = post("/api/v1/registry/capabilities", data)
        print(f"published: {out['id']}")

def cmd_compose_run(args):
    comp = yaml.safe_load(open(args.path, "r"))
    # publish composition on the fly
    post("/api/v1/registry/compositions", comp)
    res = post("/api/v1/compose/dry-run", comp)
    print(json.dumps(res, indent=2))

def cmd_policy_test(args):
    comp = yaml.safe_load(open(args.path, "r"))
    res = post("/api/v1/policy/admit", comp)
    print(json.dumps(res, indent=2))

def main():
    ap = argparse.ArgumentParser(prog="aoactl")
    sub = ap.add_subparsers(required=True)

    sp = sub.add_parser("cap", help="capability ops")
    sp_sub = sp.add_subparsers(required=True)

    spp = sp_sub.add_parser("publish")
    spp.add_argument("paths", nargs="+")
    spp.set_defaults(func=cmd_cap_publish)

    cmp = sub.add_parser("compose", help="composition ops")
    cmp_sub = cmp.add_subparsers(required=True)

    cmpr = cmp_sub.add_parser("run")
    cmpr.add_argument("path")
    cmpr.add_argument("--dry-run", action="store_true", default=True)
    cmpr.set_defaults(func=cmd_compose_run)

    pol = sub.add_parser("policy")
    polt = pol.add_subparsers(required=True)
    poltest = polt.add_parser("test")
    poltest.add_argument("path")
    poltest.set_defaults(func=cmd_policy_test)

    args = ap.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()