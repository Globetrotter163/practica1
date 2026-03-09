from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ourpkg',
            namespace='sensors_pub',
            executable='sensors_pub',
        )
    ])