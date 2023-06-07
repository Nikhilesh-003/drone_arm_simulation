import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt

class JointStatePublisherGui(Node):
    def __init__(self):
        super().__init__('joint_state_publisher_gui')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.joint_names_ = ['joint1', 'joint2', 'joint3']
        self.joint_positions_ = [0.0, 0.0, 0.0]
        self.create_gui()

    def create_gui(self):
        app = QApplication([])
        main_window = QMainWindow()
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_window.setCentralWidget(central_widget)

        for joint_name in self.joint_names_:
            label = QLabel(joint_name)
            position_line_edit = QLineEdit()
            position_line_edit.setAlignment(Qt.AlignRight)
            position_line_edit.setText('0.0')
            position_line_edit.returnPressed.connect(self.update_joint_position)
            main_layout.addWidget(label)
            main_layout.addWidget(position_line_edit)

        send_button = QPushButton('Send')
        send_button.clicked.connect(self.send_joint_states)
        main_layout.addWidget(send_button)

        main_window.show()
        app.exec_()

    def update_joint_position(self):
        sender = self.sender()
        joint_index = sender.property('joint_index')
        joint_position = float(sender.text())
        self.joint_positions_[joint_index] = joint_position

    def send_joint_states(self):
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = self.get_clock().now().to_msg()
        joint_state_msg.name = self.joint_names_
        joint_state_msg.position = self.joint_positions_
        self.publisher_.publish(joint_state_msg)

def main(args=None):
    rclpy.init(args=args)
    joint_state_publisher_gui = JointStatePublisherGui()
    rclpy.spin(joint_state_publisher_gui)
    joint_state_publisher_gui.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
