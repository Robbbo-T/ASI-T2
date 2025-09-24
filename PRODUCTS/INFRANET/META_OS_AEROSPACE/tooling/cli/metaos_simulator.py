#!/usr/bin/env python3
"""
Meta-OS Aerospace Simulator
Complete system simulator for UAV+Satellite+Ground coordination testing
"""

import argparse
import json
import time
import threading
import random
import math
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime, timedelta

@dataclass
class AssetState:
    id: str
    asset_type: str
    position: tuple  # (lat, lon, alt)
    velocity: tuple  # (vx, vy, vz)
    health: int      # 0xF = OK, 0xE = WARN, 0xC = CRIT, 0x8 = MAINT
    power_w: float
    temperature_c: float
    last_update: datetime

@dataclass
class TelemetryMessage:
    topic: str
    payload: dict
    timestamp: datetime
    priority: int  # 0x0E = high, 0x0A = medium, 0x06 = low

class MetaOSSimulator:
    def __init__(self):
        self.assets: Dict[str, AssetState] = {}
        self.telemetry_bus: List[TelemetryMessage] = []
        self.mission_active = False
        self.simulation_time = 0.0
        self.lock = threading.Lock()
        
    def add_asset(self, asset_id: str, asset_type: str, initial_pos: tuple):
        """Add an asset to the simulation"""
        with self.lock:
            self.assets[asset_id] = AssetState(
                id=asset_id,
                asset_type=asset_type,
                position=initial_pos,
                velocity=(0, 0, 0),
                health=0x0F,  # All systems OK
                power_w=100.0,
                temperature_c=25.0,
                last_update=datetime.now()
            )
            print(f"[SIM] Added {asset_type} {asset_id} at {initial_pos}")
    
    def update_physics(self):
        """Update asset positions and states based on physics"""
        dt = 0.1  # 100ms simulation step
        
        with self.lock:
            for asset in self.assets.values():
                if asset.asset_type == "uav":
                    # UAV flight dynamics (simplified)
                    lat, lon, alt = asset.position
                    vx, vy, vz = asset.velocity
                    
                    # Simple circular patrol pattern
                    radius = 0.01  # degrees
                    angular_vel = 0.001  # rad/s
                    center_lat, center_lon = 37.7749, -122.4194  # San Francisco
                    
                    angle = self.simulation_time * angular_vel
                    new_lat = center_lat + radius * math.cos(angle)
                    new_lon = center_lon + radius * math.sin(angle)
                    new_alt = alt + random.uniform(-5, 5)  # altitude variation
                    
                    asset.position = (new_lat, new_lon, max(100, new_alt))
                    
                elif asset.asset_type == "satellite":
                    # Satellite orbital mechanics (simplified LEO)
                    lat, lon, alt = asset.position
                    orbital_period = 90 * 60  # 90 minutes
                    angular_vel = 2 * math.pi / orbital_period
                    
                    # Update longitude (ground track)
                    new_lon = lon + angular_vel * dt * 180 / math.pi
                    if new_lon > 180:
                        new_lon -= 360
                    
                    asset.position = (lat, new_lon, alt)
                
                # Update health and power consumption
                asset.power_w += random.uniform(-5, 5)
                asset.temperature_c += random.uniform(-2, 2)
                
                # Simulate health degradation
                if random.random() < 0.001:  # 0.1% chance per update
                    asset.health = 0x0E  # Warning state
                
                asset.last_update = datetime.now()
    
    def generate_telemetry(self):
        """Generate telemetry messages from all assets"""
        with self.lock:
            for asset in self.assets.values():
                # IMU telemetry (high priority for UAV)
                if asset.asset_type == "uav":
                    imu_data = {
                        "timestamp": asset.last_update.isoformat(),
                        "gyro": [random.uniform(-0.1, 0.1) for _ in range(3)],
                        "accel": [random.uniform(-1, 1) for _ in range(3)],
                        "flags": asset.health
                    }
                    self.telemetry_bus.append(TelemetryMessage(
                        topic=f"/{asset.id.lower()}/imu",
                        payload=imu_data,
                        timestamp=asset.last_update,
                        priority=0x0E  # High priority
                    ))
                
                # Health telemetry (all assets)
                health_data = {
                    "status_flags": asset.health,
                    "error_code": 0x0000 if asset.health == 0x0F else 0x2A01,
                    "monotonic_ms": int(self.simulation_time * 1000)
                }
                self.telemetry_bus.append(TelemetryMessage(
                    topic=f"/{asset.id.lower()}/health",
                    payload=health_data,
                    timestamp=asset.last_update,
                    priority=0x0A  # Medium priority
                ))
                
                # Position telemetry
                pos_data = {
                    "latitude": asset.position[0],
                    "longitude": asset.position[1],
                    "altitude": asset.position[2],
                    "velocity": asset.velocity
                }
                self.telemetry_bus.append(TelemetryMessage(
                    topic=f"/{asset.id.lower()}/position",
                    payload=pos_data,
                    timestamp=asset.last_update,
                    priority=0x06  # Low priority
                ))
    
    def process_fdir(self):
        """Process Fault Detection, Isolation, and Recovery"""
        with self.lock:
            for asset in self.assets.values():
                if asset.asset_type == "uav":
                    # Check for GNSS timeout (simulate LOST_GNSS scenario)
                    time_since_update = (datetime.now() - asset.last_update).total_seconds()
                    if time_since_update > 10:  # 10 second timeout
                        print(f"[FDIR] LOST_GNSS detected for {asset.id}")
                        print(f"[FDIR] Executing recovery: set_mode(FAILSAFE) → plan_rtl()")
                        asset.health = 0x0C  # Critical state
                        
                        # Add emergency telemetry
                        emergency_data = {
                            "event": "GNSS_LOST",
                            "action": "FAILSAFE_RTL",
                            "timestamp": datetime.now().isoformat()
                        }
                        self.telemetry_bus.append(TelemetryMessage(
                            topic=f"/{asset.id.lower()}/events",
                            payload=emergency_data,
                            timestamp=datetime.now(),
                            priority=0x0F  # Emergency priority
                        ))
    
    def simulate_mission(self, duration_seconds: int):
        """Run complete mission simulation"""
        print(f"[SIM] Starting mission simulation for {duration_seconds} seconds")
        self.mission_active = True
        start_time = time.time()
        
        # Add sample assets
        self.add_asset("UAV-01", "uav", (37.7749, -122.4194, 500))  # San Francisco
        self.add_asset("SAT-LEO-7", "satellite", (37.7749, -122.4194, 550000))  # LEO
        self.add_asset("GS-SF", "ground_station", (37.7849, -122.4094, 10))
        
        telemetry_count = 0
        
        while self.mission_active and (time.time() - start_time) < duration_seconds:
            self.update_physics()
            self.generate_telemetry()
            self.process_fdir()
            
            # Print telemetry summary every 10 seconds
            if int(self.simulation_time) % 10 == 0 and len(self.telemetry_bus) > telemetry_count:
                new_messages = len(self.telemetry_bus) - telemetry_count
                print(f"[SIM] T+{int(self.simulation_time):03d}s: {new_messages} telemetry messages, {len(self.assets)} assets active")
                telemetry_count = len(self.telemetry_bus)
            
            self.simulation_time += 0.1
            time.sleep(0.1)  # Real-time simulation
        
        print(f"[SIM] Mission simulation completed")
        print(f"[SIM] Total telemetry messages: {len(self.telemetry_bus)}")
        print(f"[SIM] Average message rate: {len(self.telemetry_bus)/duration_seconds:.1f} msg/s")
    
    def export_telemetry(self, filename: str):
        """Export all telemetry data to JSON file"""
        with open(filename, 'w') as f:
            telemetry_data = []
            for msg in self.telemetry_bus:
                telemetry_data.append({
                    "topic": msg.topic,
                    "payload": msg.payload,
                    "timestamp": msg.timestamp.isoformat(),
                    "priority": f"0x{msg.priority:02X}"
                })
            json.dump(telemetry_data, f, indent=2)
        print(f"[SIM] Exported {len(telemetry_data)} telemetry messages to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Meta-OS Aerospace Simulator")
    parser.add_argument("--duration", type=int, default=60, help="Simulation duration in seconds")
    parser.add_argument("--export", type=str, help="Export telemetry data to JSON file")
    parser.add_argument("--scenario", choices=["patrol", "emergency", "convoy"], default="patrol")
    
    args = parser.parse_args()
    
    simulator = MetaOSSimulator()
    
    try:
        simulator.simulate_mission(args.duration)
        
        if args.export:
            simulator.export_telemetry(args.export)
            
    except KeyboardInterrupt:
        print("\n[SIM] Simulation interrupted by user")
        simulator.mission_active = False

if __name__ == "__main__":
    main()