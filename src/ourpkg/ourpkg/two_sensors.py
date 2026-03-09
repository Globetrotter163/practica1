import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class RobotSensorsPublisher(Node):

    def __init__(self):
        super().__init__('robot_sensor_publisher')

        self.velocity_pub = self.create_publisher(
            Float32,'/robot_velocity', 10)

        self.battery_pub = self.create_publisher(
            Float32, '/robot_battery',10 )
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # ==================================== VALUES 
        velocity = random.uniform(0.0, 2.5)
        battery = random.uniform(0.0, 100.0)

        # ...........................................
        
        velocity_msg = Float32()
        battery_msg = Float32()

        velocity_msg.data = velocity
        battery_msg.data = battery

        # Publicar
        self.velocity_pub.publish(velocity_msg)
        self.battery_pub.publish(battery_msg)

        # Log en consola
        self.get_logger().info(
            f'Velocity: {velocity:.2f} m/s | Battery: {battery:.1f} %'
        )


def main(args=None):
    rclpy.init(args=args)

    node = RobotSensorsPublisher()

    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()