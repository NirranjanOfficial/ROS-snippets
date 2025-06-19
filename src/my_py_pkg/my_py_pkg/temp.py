#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class MyCustomNode (Node): # MODIFY NAME
	def init (self):
		super(). init ("node_name") #MODIFY NAME


def main(args=None):
	rclpy.init(args=args)
	node=MyCustomNode() # MODIFY NAME
	rclpy.spin (node)
	rclpy.shutdown ( )
if "__name__" == "__main__":
	main()
