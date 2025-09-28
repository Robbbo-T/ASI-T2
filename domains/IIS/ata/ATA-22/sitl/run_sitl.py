import time, yaml, math
from ata22.mode_manager import ModeManager

with open("domains/IIS/ata/ATA-22/config/modes.yaml") as f:
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