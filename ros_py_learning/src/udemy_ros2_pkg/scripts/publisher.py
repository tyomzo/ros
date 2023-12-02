#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldPublisher(Node):
    def __init__(self):
        super().__init__('hello_world_publisher_node')
        self.pub = self.create_publisher(String, 'hello_world_topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World {self.counter}'
        self.pub.publish(msg)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldPublisher()
    print('Hello World Publisher has started')

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Hello World Publisher has stopped')
        node.destroy_node()

if __name__ == '__main__':
    main()