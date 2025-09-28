from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ModeState:
    lat: str = "ROL"
    vert: str = "PIT"
    ap_engaged: bool = False
    yd_active: bool = False

class ModeManager:
    def __init__(self, modes_cfg: Dict[str, Any]):
        self.cfg = modes_cfg
        self.state = ModeState()

    def can_engage(self, sensors: Dict[str, bool], pitch_deg: float, bank_deg: float, ias_mps: float) -> bool:
        inter = self.cfg["engage_interlocks"]
        if ias_mps < inter["min_ias_mps"]:
            return False
        if abs(bank_deg) > inter["max_bank_deg"]:
            return False
        if abs(pitch_deg) > inter["max_pitch_deg"]:
            return False
        return all(sensors.get(k, False) for k in inter["sensors_required"])

    def engage(self):
        self.state.ap_engaged = True
        self.state.yd_active = True

    def disengage(self, reason: str):
        self.state.ap_engaged = False
        self.state.yd_active = False
        return {"event": "AP_DISENGAGE", "reason": reason}

    def select_lat(self, mode: str, context: Dict[str, Any]) -> bool:
        m = self.cfg["lateral_modes"].get(mode)
        if not m:
            return False
        if any(not context.get(req, False) for req in m.get("requires", [])):
            return False
        self.state.lat = mode
        return True

    def select_vert(self, mode: str, context: Dict[str, Any]) -> bool:
        m = self.cfg["vertical_modes"].get(mode)
        if not m:
            return False
        if any(not context.get(req, False) for req in m.get("requires", [])):
            return False
        self.state.vert = mode
        return True