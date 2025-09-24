#!/usr/bin/env python3
"""
ROS2 Launch file for UAV bridge connecting DDS topics to Meta-OS orchestrator
Demonstrates middleware layer integration with deterministic QoS
"""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'asset_id',
            default_value='UAV-01',
            description='Asset identifier for this UAV instance'
        ),
        
        DeclareLaunchArgument(
            'qos_profile',
            default_value='crit-telemetry',
            description='QoS profile from middleware/dds/qos_policies.yaml'
        ),
        
        # IMU sensor bridge (high priority telemetry)
        Node(
            package='meta_os_bridges',
            executable='imu_bridge',
            name='imu_bridge',
            parameters=[{
                'asset_id': LaunchConfiguration('asset_id'),
                'topic_out': '/uav01/imu',
                'qos_profile': LaunchConfiguration('qos_profile'),
                'deadline_ms': 5,
                'priority_bits': 0b1110,  # 0x0E hex
                'partition': 'DAL-A'
            }]
        ),
        
        # GNSS bridge (navigation data)
        Node(
            package='meta_os_bridges',
            executable='gnss_bridge',
            name='gnss_bridge',
            parameters=[{
                'asset_id': LaunchConfiguration('asset_id'),
                'topic_out': '/uav01/gnss',
                'qos_profile': 'navigation',
                'deadline_ms': 100,
                'fdir_timeout_ms': 1000  # Triggers LOST_GNSS rule
            }]
        ),
        
        # Health monitoring bridge
        Node(
            package='meta_os_bridges',
            executable='health_bridge',
            name='health_bridge',
            parameters=[{
                'asset_id': LaunchConfiguration('asset_id'),
                'topic_out': '/uav01/health',
                'status_flags_mask': 0x0F,  # 4 bits: OK|WARN|CRIT|MAINT
                'error_code_base': 0x2A00   # UAV-specific error code range
            }]
        ),
        
        # Command bridge (actuator commands)
        Node(
            package='meta_os_bridges',
            executable='command_bridge',
            name='command_bridge',
            parameters=[{
                'asset_id': LaunchConfiguration('asset_id'),
                'topic_in': '/uav01/command',
                'safety_partition': 'DAL-A',
                'max_command_rate_hz': 500,
                'watchdog_timeout_ms': 50
            }]
        )
    ])