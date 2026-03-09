import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class RobotStateNode(Node):

    def __init__(self):
        super().__init__('robot_state_node')

        self.last_velocity = None
        self.last_battery = None
        self.current_state = None

        # ======================== SUBS
        self.create_subscription(Float32, '/robot_velocity',
            self.velocity_callback, 10)

        self.create_subscription(Float32, '/robot_battery',
            self.battery_callback, 10)

        # ====================== PUBS
        self.state_pub = self.create_publisher(
            String, '/robot_state', 10 )

    def velocity_callback(self, msg):
        self.last_velocity = msg.data
        self.evaluate_state()

    def battery_callback(self, msg):
        self.last_battery = msg.data
        self.evaluate_state()

    def evaluate_state(self):

        if self.last_velocity is None or self.last_battery is None:
            return

        v = self.last_velocity
        b = self.last_battery

        # ========== ===== REGLAS
        if b < 10:
            new_state = "CRITICAL"
        elif b < 20:
            new_state = "LOW_BATTERY"
        elif v > 2.0:
            new_state = "OVER_SPEED"
        else:
            new_state = "NORMAL"

        
        
        if new_state != self.current_state:
            self.current_state = new_state

            msg = String()
            msg.data = new_state

            self.state_pub.publish(msg)

            self.get_logger().info(
                f'Robot state → {new_state}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = RobotStateNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()