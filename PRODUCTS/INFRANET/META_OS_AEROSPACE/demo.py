#!/usr/bin/env python3
"""
Meta-OS Aerospace Demo Script
Complete demonstration of the Meta-OS system capabilities
"""

import subprocess
import time
import os
from pathlib import Path

def run_command(cmd, description, cwd=None):
    """Run a command and display results"""
    print(f"\n{'='*60}")
    print(f"Demo: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
        print(result.stdout)
        if result.stderr:
            print(f"STDERR: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    base_path = Path(__file__).parent
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    Meta-OS Aerospace Demo                    ║
    ║              Operating System of Systems                     ║
    ║                                                              ║
    ║  A comprehensive aerospace coordination platform integrating ║
    ║  UAVs, satellites, and ground systems with full safety      ║
    ║  certification and quantum optimization capabilities.        ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("\n🚀 Starting Meta-OS Aerospace Demo...")
    time.sleep(2)
    
    # 1. Validate system integrity
    success = run_command([
        "python3", "tooling/cli/test_framework.py", "--test", "all"
    ], "System Integrity Validation", cwd=base_path)
    
    if not success:
        print("❌ System validation failed. Aborting demo.")
        return
    
    # 2. Deploy UAV+Satellite mission
    success = run_command([
        "python3", "tooling/cli/metaosctl.py", "deploy",
        "orchestrator/manifests/mission/uav_sat_demo.yaml",
        "--require-attestation"
    ], "Mission Deployment with Hardware Attestation", cwd=base_path)
    
    # 3. Audit QoS configuration
    run_command([
        "python3", "tooling/cli/metaosctl.py", "qos", "audit",
        "--profile", "crit-telemetry", "--asset", "UAV-01"
    ], "Quality of Service Audit", cwd=base_path)
    
    # 4. Test fault detection and recovery
    run_command([
        "python3", "tooling/cli/metaosctl.py", "fdir", "test",
        "security/fdir/rules/uav_fdir.yaml", "--inject", "LOST_GNSS"
    ], "Fault Detection, Isolation & Recovery Test", cwd=base_path)
    
    # 5. Run system simulation
    print(f"\n{'='*60}")
    print("Demo: Live System Simulation (30 seconds)")
    print("Command: System will simulate UAV+Satellite+Ground coordination")
    print(f"{'='*60}")
    
    telemetry_file = "/tmp/demo_telemetry.json"
    success = run_command([
        "python3", "tooling/cli/metaos_simulator.py",
        "--duration", "30", "--export", telemetry_file
    ], "30-Second Live Simulation", cwd=base_path)
    
    if success and os.path.exists(telemetry_file):
        # Display telemetry summary
        import json
        with open(telemetry_file, 'r') as f:
            telemetry_data = json.load(f)
        
        print(f"\n📊 Telemetry Analysis:")
        print(f"  • Total Messages: {len(telemetry_data)}")
        
        topics = {}
        priorities = {}
        for msg in telemetry_data:
            topic = msg.get('topic', 'unknown')
            priority = msg.get('priority', '0x00')
            topics[topic] = topics.get(topic, 0) + 1
            priorities[priority] = priorities.get(priority, 0) + 1
        
        print(f"  • Message Topics:")
        for topic, count in sorted(topics.items()):
            print(f"    - {topic}: {count} messages")
        
        print(f"  • Priority Distribution:")
        for priority, count in sorted(priorities.items()):
            priority_name = {
                '0x0F': 'EMERGENCY',
                '0x0E': 'HIGH (Critical Telemetry)',
                '0x0A': 'MEDIUM (Health Data)',
                '0x06': 'LOW (Position Data)'
            }.get(priority, 'UNKNOWN')
            print(f"    - {priority} ({priority_name}): {count} messages")
    
    # 6. Display system architecture
    print(f"\n{'='*60}")
    print("System Architecture Overview")
    print(f"{'='*60}")
    
    print("""
    📡 Meta-OS Aerospace Architecture:
    
    Layer 6: Mission Applications & Cockpit
             ├── UI/UX Interfaces
             ├── Mission Control Systems  
             └── Third-party API Integration
    
    Layer 5: Intelligence & Optimization
             ├── Edge ML (Computer Vision, Health Monitoring)
             ├── Autonomous Planning & Decision Making
             └── Quantum Optimization (QOx QAOA/Annealing)
    
    Layer 4: Digital Thread & Digital Twins
             ├── MBSE/PLM Integration (Design ↔ Operations)
             ├── SIL/HIL Testing Integration
             └── Real-time Digital Twin (Live State Mirror)
    
    Layer 3: Certification, Security & Resilience
             ├── PKI & Zero-Trust Architecture
             ├── FDIR (Fault Detection/Isolation/Recovery)
             ├── DO-178C/DO-326A/ISO-26262 Compliance
             └── Cryptographic OTA Updates
    
    Layer 2: Middleware & Interoperability
             ├── DDS/ROS2 with Deterministic QoS
             ├── Protocol Gateways (ARINC/MIL-STD/CAN/SpaceWire)
             └── Time Synchronization (GNSS/PTP)
    
    Layer 1: Core & Orchestration
             ├── Hybrid Kernels (seL4/QNX/VxWorks + Linux-RT)
             ├── ARINC-653 Partitioning & Scheduling
             ├── Federated Asset Orchestration
             └── Heterogeneous Resource Management
    
    Layer 0: Hardware Platforms
             ├── UAV (ARM Cortex + FPGA + Sensors)
             ├── Satellite (Space-qualified + RadHard)
             └── Ground (High-availability + Redundancy)
    """)
    
    # Display key capabilities
    print(f"\n{'='*60}")
    print("Key Capabilities Demonstrated")
    print(f"{'='*60}")
    
    print("""
    ✅ Multi-Asset Coordination
       • UAV, Satellite, Ground Station integration
       • Heterogeneous platform support (FreeRTOS/ROS2, RTEMS, Linux)
       • Real-time deterministic communication with QoS guarantees
    
    ✅ Safety & Certification
       • ARINC-653 temporal/spatial partitioning (20ms major frame)
       • DO-178C DAL-A/B compliance framework
       • Hardware attestation with TPM/TEE integration
    
    ✅ Security & Resilience
       • Zero-trust architecture with PKI authentication
       • Automated FDIR with configurable response rules
       • Cryptographically signed OTA updates with rollback
    
    ✅ Mission Operations
       • Declarative mission manifests with asset requirements
       • Dynamic resource allocation and task scheduling
       • Real-time telemetry with priority-based QoS
    
    ✅ Simulation & Testing
       • Complete system simulation with physics models
       • Comprehensive test framework with validation
       • Hardware-in-the-Loop (HIL) and Software-in-the-Loop (SIL)
    
    ✅ Development Tools
       • Full SDK with multi-language bindings (C/C++, Rust, Python, Ada)
       • Command-line tools for deployment and management
       • Automated testing and validation frameworks
    """)
    
    print(f"\n{'='*60}")
    print("Demo Complete - Meta-OS Aerospace MVP")
    print(f"{'='*60}")
    
    print("""
    🎯 Next Steps for Production Deployment:
    
    1. Hardware Integration
       • Deploy on target aerospace hardware platforms
       • Complete DO-178C/DO-326A certification process
       • Integrate with real sensors and actuators
    
    2. Mission Integration
       • Connect with existing mission control systems
       • Integrate with air traffic control and regulatory systems
       • Deploy in controlled test environments
    
    3. Security Hardening
       • Complete penetration testing and vulnerability assessment
       • Deploy production PKI infrastructure
       • Implement full zero-trust network architecture
    
    4. Operational Deployment
       • Staged rollout with pilot programs
       • Operator training and certification
       • Production monitoring and maintenance procedures
    
    📚 Documentation: See docs/ directory for complete technical specifications
    🔧 Tools: Use tooling/cli/ for ongoing system management
    🧪 Testing: Run tooling/cli/test_framework.py for validation
    """)

if __name__ == "__main__":
    main()