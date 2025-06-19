#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(AddTwoInts,"add_two_ints")
    def call_add_two_ints(self,a,b):
        while not self.client.wait_for_service(1.0):  #an 1.0 is waiting for timeout
            self.get_logger().warn("Waiting for add_two_ints server to respond....")   #in general when an server is not found an eeror is acqired      
        request = AddTwoInts.Request()
        request.a = int(input("Num1:"))
        request.b = int(input("Num2:"))
        future = self.client.call_async(request)  #asyncronis return of output
        future.add_done_callback()

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()