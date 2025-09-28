import yaml
from ata22.mode_manager import ModeManager
import pathlib

def load_cfg():
    config_path = pathlib.Path(__file__).parent.parent.parent / "config" / "modes.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def test_engage_interlocks_ok():
    m = ModeManager(load_cfg())
    ok = m.can_engage(
        sensors={"att_valid": True, "airdata_valid": True},
        pitch_deg=2.0, bank_deg=5.0, ias_mps=70.0
    )
    assert ok

def test_select_lnav_requires_fms_valid():
    m = ModeManager(load_cfg())
    assert not m.select_lat("LNAV", {"fms_lnav_path_valid": False})
    assert m.select_lat("LNAV", {"fms_lnav_path_valid": True})

def test_disengage_reason():
    m = ModeManager(load_cfg())
    m.engage()
    evt = m.disengage("manual")
    assert evt["reason"] == "manual"
    assert not m.state.ap_engaged