"""Sensor data structures and validation for ATA-22."""

from dataclasses import dataclass

@dataclass
class AttitudeData:
    pitch_deg: float
    roll_deg: float
    yaw_rate_dps: float
    valid: bool = True

@dataclass
class AirData:
    tas_mps: float
    altitude_m: float
    vs_mps: float
    valid: bool = True

@dataclass
class NavigationData:
    lat_deg: float
    lon_deg: float
    track_deg: float
    gs_mps: float
    fms_lnav_valid: bool = False
    fms_vnav_valid: bool = False

class SensorValidator:
    """Validates sensor data for autopilot engagement."""
    
    @staticmethod
    def validate_attitude(att: AttitudeData) -> bool:
        """Check attitude data validity."""
        if not att.valid:
            return False
        if abs(att.pitch_deg) > 90:
            return False
        if abs(att.roll_deg) > 180:
            return False
        return True
    
    @staticmethod
    def validate_airdata(air: AirData) -> bool:
        """Check air data validity."""
        if not air.valid:
            return False
        if air.tas_mps < 0 or air.tas_mps > 300:  # Reasonable speed range
            return False
        return True