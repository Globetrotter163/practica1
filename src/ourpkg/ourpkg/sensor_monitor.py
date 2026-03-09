import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class RobotMonitor(Node):

    def __init__(self):
        super().__init__('robot_monitor')

        self.last_velocity = None
        self.last_battery = None

        self.create_subscription(Float32,
            '/robot_velocity', self.velocity_callback, 10)

        self.create_subscription(Float32,
            '/robot_battery', self.battery_callback, 10)

    def velocity_callback(self, msg):
        self.last_velocity = msg.data
        self.evaluate_velocity()

    def battery_callback(self, msg):
        self.last_battery = msg.data
        self.evaluate_battery()

    def evaluate_velocity(self):
        v = self.last_velocity

        if v > 2.0:
            self.get_logger().warn(
                f'Velocity: {v:.2f} → WARNING'
            )
        else:
            self.get_logger().info(
                f'Velocity: {v:.2f} → OK'
            )

    def evaluate_battery(self):
        b = self.last_battery

        if b < 10:
            self.get_logger().error(
                f'Battery: {b:.1f} → CRITICAL BATTERY'
            )
        elif b < 20:
            self.get_logger().warn(
                f'Battery: {b:.1f} → LOW BATTERY'
            )
        else:
            self.get_logger().info(
                f'Battery: {b:.1f} → OK'
            )


def main(args=None):
    rclpy.init(args=args)

    node = RobotMonitor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()