#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node=Node("add_two_ints_client_no_oop")
    client = node.create_client(AddTwoInts, "add_two_ints")
    while not client.wait_for_service(1.0):  #an 1.0 is waiting for timeout
        node.get_logger().warn("Waiting for add_two_ints server to respond....")   #in general when an server is not found an eeror is acqired

    request = AddTwoInts.Request()
    request.a = int(input("Num1:"))
    request.b = int(input("Num2:"))
    future = client.call_async(request)  #asyncronis return of output

    rclpy.spin_until_future_complete(node,future)   #it means that it will keep holding the client until the value is returned
    response = future.result() # the final or required output is stored here
    node.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
    rclpy.shutdown()


if __name__ =="__main__":
    main()
