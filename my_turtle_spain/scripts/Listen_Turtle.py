#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import String

class TurtleBot:
	
    def __init__(self):
 
	print ("initialize node")
        rospy.init_node('spain_controller', anonymous= False) #ROS unique name if True 


        self.comm_vel_subscriber = rospy.Subscriber('cmd_vel_mux/input/navi',
                                                Twist, self.wheel_calc)

	self.kinematic_publisher = rospy.Publisher('DIFFERENTIAL_INVERSE_KINEMATICS_OUTPUT',Vector3, queue_size=10)
	
        self.twist = Twist()
	print ("variable twist created")
	print(self.twist)
        self.rate = rospy.Rate(5) 	# Go through 5x/second

	rospy.spin() 			# runs until Ctrl + V


    #print("update function time")
    def wheel_calc(self, data):
	#print("Houston we made it")
	#inverse Kinematics were from the class lecture 				   		        	#EdX_Wheeled_Kinematics_part4_differential_drive
	r = 0.5 			# wheel radius = 0.05m	
	b = 0.5				# b = 0.5m

	move_cmd = Twist()
	self.twist = data
	#wheel_msg = self.twist.	
	d_phi = Vector3()
	d_phi.x = self.twist.linear.x* (1/r) + self.twist.angular.z* (b/r)
	d_phi.y = self.twist.linear.x* (1/r) + self.twist.angular.z* (-b/r)
	d_phi.z = 0
	
	self.kinematic_publisher.publish(d_phi) # Publishes [phi_r phi_l 0]



if __name__ == '__main__':
    try:
        TurtleBot()
    except rospy.ROSInterruptException:
    	pass
