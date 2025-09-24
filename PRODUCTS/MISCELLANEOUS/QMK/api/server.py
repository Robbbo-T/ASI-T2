from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os, secrets, time

app = FastAPI(title="LIGHTVIBES QMK API", version="0.1.0")

QBER_THRESHOLD = float(os.getenv("LIGHTVIBES_QBER_THRESHOLD", "0.08"))

class Policy(BaseModel):
    min_keybits: int = Field(default=256, ge=128, le=4096)
    ttl_s: int = Field(default=120, ge=10, le=3600)

class SessionReq(BaseModel):
    peer_id: str
    policy: Policy
    fallback: str = "PQC"  # or "DISABLE"

class SessionResp(BaseModel):
    session_id: str
    key_ref: str
    health: dict
    mode: str  # "QMK" | "PQC"

# naive in-memory store (replace with HSM/TEE+KMS)
KEYS = {}

def _gen_key(bits: int) -> bytes:
    return secrets.token_bytes(bits // 8)

@app.post("/lightvibes/session", response_model=SessionResp, status_code=201)
def create_session(req: SessionReq):
    # Simulate quantum health (replace with real QBER/rate from photonics stack)
    simulated_qber = 0.03
    simulated_rate = 2000  # bits per second available

    mode = "QMK" if simulated_qber <= QBER_THRESHOLD else "PQC"
    keybits = max(req.policy.min_keybits, 256)
    key_ref = secrets.token_hex(16)
    session_id = secrets.token_hex(12)

    # seal: here we just store raw; real impl stores device-sealed blob
    KEYS[key_ref] = {
        "blob": _gen_key(keybits),
        "ttl_s": req.policy.ttl_s,
        "exp": time.time() + req.policy.ttl_s,
        "mode": mode,
        "consumed": False
    }

    # TODO: emit UTCS/QS event with qber/rate/session_id/key_ref
    return SessionResp(
        session_id=session_id,
        key_ref=key_ref,
        health={"qber": simulated_qber, "rate_bps": simulated_rate},
        mode=mode
    )

@app.get("/lightvibes/key/{key_ref}")
def get_key(key_ref: str):
    item = KEYS.get(key_ref)
    if not item or item["consumed"] or item["exp"] < time.time():
        raise HTTPException(status_code=404, detail="key_ref invalid or expired")
    item["consumed"] = True
    # In production: return hardware-sealed blob only
    # For now, we return a placeholder sealed blob (do NOT use in production)
    sealed_blob_placeholder = secrets.token_hex(32)
    return {
        "key_ref": key_ref,
        "key_sealed": sealed_blob_placeholder,
        "ttl_s": int(item["exp"] - time.time()),
        "mode": item["mode"]
    }