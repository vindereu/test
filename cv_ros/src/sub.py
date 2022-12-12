#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8

def callback(msg):
    print(msg)

rospy.init_node("sub", anonymous=True)
rospy.Subscriber("topic", Int8, callback)
rospy.spin()
