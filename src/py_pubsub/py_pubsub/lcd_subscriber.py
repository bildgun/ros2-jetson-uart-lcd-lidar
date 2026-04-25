#!/usr/bin/env python3

import liquidcrystal_i2c
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class LcdSubscriber(Node):
    def __init__(self):
        super().__init__('lcd_subscriber')

        self.declare_parameter('i2c_address', 0x27)
        self.declare_parameter('i2c_bus', 1)
        self.declare_parameter('cols', 16)
        self.declare_parameter('rows', 2)
        self.declare_parameter('topic', '/lcd/text')

        self.i2c_address = int(self.get_parameter('i2c_address').value)
        self.i2c_bus = int(self.get_parameter('i2c_bus').value)
        self.cols = int(self.get_parameter('cols').value)
        self.rows = int(self.get_parameter('rows').value)
        self.topic = str(self.get_parameter('topic').value)

        self.lcd = liquidcrystal_i2c.LiquidCrystal_I2C(
            self.i2c_address,
            self.i2c_bus,
            numlines=self.rows,
        )

        self.write_lines('ROS2 LCD', 'subscriber')

        self.subscription = self.create_subscription(
            String,
            self.topic,
            self.listener_callback,
            10,
        )

        self.get_logger().info(
            f'Subscribed to topic: {self.topic}, '
            f'LCD address={hex(self.i2c_address)}, bus={self.i2c_bus}'
        )

    def listener_callback(self, message: String):
        text = message.data if message.data is not None else ''

        lines = text.split('\n', 1)
        line_1 = lines[0] if len(lines) > 0 else ''
        line_2 = lines[1] if len(lines) > 1 else ''

        self.write_lines(line_1, line_2)

        self.get_logger().info(f"LCD <= '{line_1}' | '{line_2}'")

    def write_lines(self, line_1: str, line_2: str):
        formatted_line_1 = line_1[:self.cols].ljust(self.cols)
        formatted_line_2 = line_2[:self.cols].ljust(self.cols)

        self.lcd.printline(0, formatted_line_1)

        if self.rows > 1:
            self.lcd.printline(1, formatted_line_2)


def main(args=None):
    rclpy.init(args=args)

    node = LcdSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
