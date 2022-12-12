#!/usr/bin/env python3
import rospy
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage

def callback(img):
    frame = CvBridge().compressed_imgmsg_to_cv2(img)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow("frame", frame)

rospy.init_node("cv_ros_sub")
rospy.Subscriber("/usb_cam/image_rect_color/compressed",
                CompressedImage, callback)
rospy.spin()
