#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8

rospy.init_node("pub", anonymous=True)

pub = rospy.Publisher("topic", Int8, queue_size=3)
msg = Int8()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish(msg)
    msg.data += 1
    if msg.data == 128:
        msg.data = 0

    rate.sleep()
