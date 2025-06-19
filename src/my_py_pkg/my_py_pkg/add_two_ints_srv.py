#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("Add two ints server is now initiated!")

    def callback_add_two_ints(self, request: AddTwoInts.Request, response: AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()


'''
Once created the server go to the ros2_ws give: colcon build --packages-selct my_py_pkg
then once done ros2 run my_py_pkg add_two_ints_srv

this will run the server node we can also give basic inputs for these from CLI
for that:in new terminal

ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: integer_val,b: integer_val}"


'''