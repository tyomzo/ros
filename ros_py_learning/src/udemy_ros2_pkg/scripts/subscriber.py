import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldSubscriber(Node):
    def __init__(self):
        super().__init__('hello_world_subscriber_node')
        self.sub = self.create_subscription(String, 'hello_world_topic', self.sub_callback, 10)

    def sub_callback(self, msg):
        print(msg.data)

def main (args=None):
    rclpy.init(args=args)
    node = HelloWorldSubscriber()
    print('Hello World Subscriber has started')

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Hello World Subscriber has stopped')
        node.destroy_node()

if __name__ == '__main__':
    main()