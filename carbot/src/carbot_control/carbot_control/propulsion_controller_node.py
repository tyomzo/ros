from rclpy.node import Node

from std_msgs.msg import String


class PropulsionControllerNode(Node):

    def __init__(self):
        super().__init__('propulsion_controller_node')


def main(args=None):
    print("Propulsion Controller Node Started")


if __name__ == '__main__':
    main()