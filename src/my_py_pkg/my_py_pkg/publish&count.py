#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
from rclpy.executors import MultiThreadedExecutor
class NumberPubliher(Node):

    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int64,'number',10)
        self.timer_ = self.create_timer(1.0,self.publish_this)

    def publish_this(self):
        msg = Int64()
        msg.data = 1
        self.publisher_.publish(msg)

class NumberCounter(Node):
    def __init__(self):
        super().__init__('number_counter')
        self.subscribe_ = self.create_subscription (Int64,'number',self.printer,10)
        self.publishers_ = self.create_publisher(Int64,'number_count',10)
        self.server_ = self.create_service(SetBool,'/reset_counter',self.server_callback)
        self.counter = 0
        # self.timer_ = self.create_timer(1.0, self.publish_this2)
    
    def printer(self,msg):
        self.get_logger().info(str(msg.data))
        self.counter += msg.data  # Accumulate count (or just self.counter += 1 if you want number of msgs)
        self.get_logger().info(f"Counter: {self.counter}")

        new_msg = Int64()
        new_msg.data = msg.data
        new_msg.data = self.counter
        # self.get_logger().info(counter)
        self.publishers_.publish(new_msg)

    def server_callback(self, request, response):
        if request.data:
            self.counter = 0
            response.success = True
            response.message = "Counter reset to 0."
            self.get_logger().info("Counter reset by service call.")

        else:
            response.success = False
            response.message = "Reset flag was false. Counter not reset."
            self.get_logger().info("Reset request received with false flag.")

        return response

def main(args = None):

    rclpy.init(args = args)
    nodeC = NumberCounter()
    nodeP = NumberPubliher()
    ###Before we are executing the node , we first need to initialise the node
    executor = MultiThreadedExecutor()
    executor.add_node(nodeP)
    executor.add_node(nodeC)

    
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        nodeP.destroy_node()
        nodeC.destroy_node()
        rclpy.shutdown()
    # rclpy.spin()
    # rclpy.shutdown()

if __name__ == '__main__':
    main()


'''To execute this code run the below thing for sending message from the local!

ros2 service call /reset_counter example_interfaces/srv/SetBool "{data: true}"  true/false

'''