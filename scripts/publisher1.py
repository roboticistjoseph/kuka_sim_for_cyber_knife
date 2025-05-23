#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def testrun():
    rospy.init_node('publish_node', anonymous=True) # defining the ros node - publish node
    turning = rospy.Publisher('turn', Float64MultiArray, queue_size=10) 
    rate = rospy.Rate(10) # 10hz # fequency at which the publishing occurs
    rospy.loginfo("Data is being sent")  # to print on the terminal
    while not rospy.is_shutdown():
        twist = Float64MultiArray() #Float64()
        twist.data = [1,1,1,1,1,1] #15
        turning.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        testrun()
    except rospy.ROSInterruptException: 
        pass
