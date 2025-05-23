#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray


pub_j1 =  rospy.Publisher('/assembly_toby/joint1_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
pub_j2 =  rospy.Publisher('/assembly_toby/joint2_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
#pub_j3 =  rospy.Publisher('/Assembly_Toby/joint1_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
pub_j4 =  rospy.Publisher('/assembly_toby/joint4_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
pub_j5 =  rospy.Publisher('/assembly_toby/joint5_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
pub_j6 =  rospy.Publisher('/assembly_toby/joint6_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
pub_j7 =  rospy.Publisher('/assembly_toby/joint7_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'

twist = Float64MultiArray()


def turn_push(data):
    rospy.loginfo(rospy.get_caller_id() + "data received %f", data.data[0])
    pub_j1.publish(data.data[0])
    pub_j2.publish(data.data[1])
    pub_j4.publish(data.data[2])
    pub_j5.publish(data.data[3])
    pub_j6.publish(data.data[4])
    pub_j7.publish(data.data[5])
    
    
def listener():
 
    rospy.init_node('motor_controller', anonymous=True)

    rospy.Subscriber("turn", Float64MultiArray, turn_push)

    rospy.spin()
 
if __name__ == '__main__':
    listener()
