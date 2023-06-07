import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer_ = self.create_timer(1.0, self.publish_joint_states)
        self.get_logger().info('Joint State Publisher node initialized')

    def publish_joint_states(self):
        joint_state_msg = JointState()
        # Fill in joint_state_msg with your joint information
        joint_state_msg.header.stamp = self.get_clock().now().to_msg()

        # Populate joint names
        joint_state_msg.name = ["joint1", "joint2", "joint3"]
        
        # Populate joint positions
        joint_state_msg.position = [0.0, 0.0, 0.0]

        # Publish the joint state message
        self.publisher_.publish(joint_state_msg)
        self.get_logger().info('Publishing joint states')

def main(args=None):
    rclpy.init(args=args)
    joint_state_publisher = JointStatePublisher()
    rclpy.spin(joint_state_publisher)
    joint_state_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
