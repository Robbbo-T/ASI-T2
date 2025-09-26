from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
import hashlib, json, time

# In-memory stores (replace with DB later)
CAPS: Dict[str, dict] = {}
COMPS: Dict[str, dict] = {}

app = FastAPI(title="ASI-T2 AoA", version="0.1.0")

@app.get("/healthz")
def healthz():
    return {"ok": True, "caps": len(CAPS), "comps": len(COMPS)}

class PublishResult(BaseModel):
    id: str
    status: str = "accepted"

class PolicyDecision(BaseModel):
    allowed: bool
    reasons: List[str] = Field(default_factory=list)

class ComposeRequest(BaseModel):
    comp: Optional[dict] = None
    comp_id: Optional[str] = None

def _sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def _simple_policy_check(comp: dict) -> PolicyDecision:
    """Tiny ethics/data residency stub until OPA integration."""
    reasons = []
    allowed = True

    intent = comp.get("metadata", {}).get("intent", "")
    constraints = comp.get("spec", {}).get("constraints", {})
    ethics = str(constraints.get("ethics", "")).lower()
    evidence_req = str(constraints.get("evidence", "")).lower()

    # Example: marine protection flag must be true in protected contexts
    if "marine" in intent.lower() and "strict" in ethics:
        flags = comp.get("metadata", {}).get("flags", {})
        if not flags.get("MARINE_PROTECTED", True):
            allowed = False
            reasons.append("Ethics gate: MARINE_PROTECTED must be true in protected zones")

    # Example: EU residency
    dr = comp.get("metadata", {}).get("dataResidency", "EU")
    if dr != "EU":
        allowed = False
        reasons.append("Data residency must remain in EU for this mission")

    # Evidence requirement present
    if "qs:required" in evidence_req or "utcs:required" in evidence_req:
        pass  # ok (enforced later during sealing)

    return PolicyDecision(allowed=allowed, reasons=reasons)

def _plan(comp: dict) -> dict:
    """Very small DAG builder that checks capability availability and orders by 'after' edges."""
    nodes = comp["spec"]["graph"]
    # Index by alias or id
    name = lambda n: n.get("as") or n["use"]

    # Verify all caps exist
    missing = [n["use"] for n in nodes if n["use"] not in CAPS]
    if missing:
        raise HTTPException(400, f"Missing capabilities in registry: {missing}")

    # Build adjacency & topo order
    deps = {name(n): set(n.get("after") if isinstance(n.get("after"), list) else ([n["after"]] if n.get("after") else [])) for n in nodes}
    order, ready = [], [k for k,v in deps.items() if not v]
    while ready:
        cur = ready.pop()
        order.append(cur)
        for k in deps:
            if cur in deps[k]:
                deps[k].remove(cur)
                if not deps[k]:
                    ready.append(k)
    if any(deps[k] for k in deps):
        raise HTTPException(400, f"Cycle or unresolved deps: {deps}")
    return {"order": order, "nodes": nodes}

def _evidence_envelope(comp: dict) -> dict:
    """Create a QS/UTCS-like envelope (placeholder)."""
    art = [{"id": f"{n['use']}@v1", "sha256": _sha256_str(n['use'])} for n in comp["spec"]["graph"]]
    ts = int(time.time())
    utcs = "utcs:" + _sha256_str(json.dumps(comp, sort_keys=True))[:16]
    qs = "qs:" + _sha256_str("".join(a["sha256"] for a in art))[:16]
    return {
        "compositionId": comp["metadata"]["id"],
        "artifacts": art,
        "timestamps": {"planned": ts},
        "attestation": {},
        "utcs_anchor": utcs,
        "qs_anchor": qs,
        "signatures": []
    }

@app.get("/api/v1/registry/capabilities")
def list_caps():
    return {"capabilities": sorted(CAPS.keys())}

@app.post("/api/v1/registry/capabilities", response_model=PublishResult)
def publish_cap(cap: dict):
    cap_id = cap.get("metadata", {}).get("id")
    if not cap_id:
        raise HTTPException(400, "Capability metadata.id required")
    CAPS[cap_id] = cap
    return PublishResult(id=cap_id)

@app.post("/api/v1/registry/compositions", response_model=PublishResult)
def publish_comp(comp: dict):
    comp_id = comp.get("metadata", {}).get("id")
    if not comp_id:
        raise HTTPException(400, "Composition metadata.id required")
    COMPS[comp_id] = comp
    return PublishResult(id=comp_id)

@app.post("/api/v1/policy/admit", response_model=PolicyDecision)
def policy_admit(body: dict):
    return _simple_policy_check(body)

@app.post("/api/v1/compose/dry-run")
def compose_dry_run(request: ComposeRequest):
    comp = request.comp
    comp_id = request.comp_id
    
    if comp_id:
        comp = COMPS.get(comp_id)
        if not comp:
            raise HTTPException(404, f"Composition {comp_id} not found")
    if not comp:
        raise HTTPException(400, "Provide comp or comp_id")

    decision = _simple_policy_check(comp)
    if not decision.allowed:
        return {"admitted": False, "policy": decision}

    plan = _plan(comp)
    env = _evidence_envelope(comp)
    return {"admitted": True, "policy": decision, "plan": plan, "evidence": env}