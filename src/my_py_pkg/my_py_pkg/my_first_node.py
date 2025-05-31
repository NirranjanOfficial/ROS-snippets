#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#class My Node inherits form Node obj

class MyNode(Node): #should be named after the function it must do

    def __init__(self):
        super().__init__("py_test") # we have created an node named py_test
        self.count_num = 0
        self.get_logger().info("Hello ROS2!!!")
        self.create_timer(0.5,self.timer_callback) #create_timer is used to call the enterd func every entered secs time interval

    def timer_callback(self):
        self.count_num +=1
        self.get_logger().info("The number is" + str(self.count_num)) #this is my own func to rpint some info
        #the get_logger().info takes only one args

def main( args=None):
    rclpy.init(args=args) #it is an main linewhich initialises ros2 communication
    node=MyNode()
    rclpy.spin(node)#to keep te node active
    rclpy.shutdown() #ends the communication line


if __name__=="__main__":
    main()

#main thing to understand here is the node is not the file ,but the node is created inside an file & name of the node =! name of the file!



