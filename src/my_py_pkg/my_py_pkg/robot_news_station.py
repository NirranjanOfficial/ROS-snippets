#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station") #i have named my node here

        self.robot_name = str("C3-PO") #just for fun we have given the name to the robot

        self.publisher_ = self.create_publisher(String,"robot_news",10) #this is hte topic name
        self.timer_ = self.create_timer(0.5,self.publisher_news)
        
        self.get_logger().info("Yep!thr topic is created here!")

    def publisher_news(self): #a func to hold the data of the topic
        msg = String()
        msg.data = "The name of the robot is :" +self.robot_name + " & wants to say hello!"
        self.publisher_. publish(msg)


'''
                <in ref to line 11>
Here the robot_news is the topic name and 10 is the size of the queue
When we recieve an message from an node some might get processed a bit slower so we add it to the queue, its similar to buffer
After the 10 messsages, 11th message might get lost as the count ends at 10
'''
    

def main (args=None):
    rclpy.init(args=args)
    node=RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
