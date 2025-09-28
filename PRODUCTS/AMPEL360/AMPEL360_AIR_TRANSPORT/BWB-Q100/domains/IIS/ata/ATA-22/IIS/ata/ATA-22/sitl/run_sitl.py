import time, yaml, math
import os
from ata22.mode_manager import ModeManager

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "modes.yaml")
with open(config_path) as f:
    cfg = yaml.safe_load(f)

mm = ModeManager(cfg)
sensors = {"att_valid": True, "airdata_valid": True}

# fake initial conditions
pitch, bank, ias = 0.0, 0.0, 80.0
if mm.can_engage(sensors, pitch, bank, ias):
    mm.engage()
    mm.select_lat("HDG", {})
    mm.select_vert("ALT", {"fms_vnav_path_valid": False})

print("AP engaged:", mm.state.ap_engaged, "LAT:", mm.state.lat, "VERT:", mm.state.vert)

# simulate 5 seconds of loop
for i in range(50):
    bank = 10.0 * math.sin(i/10.0)
    time.sleep(0.1)
print("Done.")