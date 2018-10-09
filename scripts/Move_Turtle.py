#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

class My_TurtleBot():
	def __init__(self):
	    	rospy.init_node('Move_Turtle', anonymous=False)
	    	
	    	self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
	    	speed = 0.2

		
	 	while not rospy.is_shutdown():
    			move_cmd = Twist()
    			move_cmd.linear.x = -speed
    			self.cmd_vel.publish(move_cmd)
				
		
	def shutdown( self ):
		rospy.loginfo ( "Stop !")
	    	self.cmd_vel.publish(Twist())
	    	rospy.sleep (1)
        
if __name__ == '__main__':
	try:
		My_TurtleBot() # Test your functions
	except rospy.ROSInterruptException:
       		pass
