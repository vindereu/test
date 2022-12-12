#!/usr/bin/env python3
import sys
import cv2 as cv

cap = cv.VideoCapture("/dev/video0")
if not cap.isOpened():
    sys.exit("Camera open failed!")

hsv_name = "Hmin", "Smin", "Vmin", "Hmax", "Smax", "Vmax"
hsv_count = 180, 255, 255, 180, 255, 255
hsv_value = [0, 0, 0, 180, 255, 255]

def track(pos):
    for i in range(6):
        hsv_value[i] = cv.getTrackbarPos(hsv_name[i], "TRACKBAR")

cv.namedWindow("TRACKBAR")
for i in range(6):
    cv.createTrackbar(hsv_name[i], "TRACKBAR", hsv_value[i], hsv_count[i], track)

while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        binary = cv.inRange(hsv, tuple(hsv_value[0:3]),
                                tuple(hsv_value[3:6]))

        contour, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for cnt in contour:
            area = cv.contourArea(cnt)
            if area > 1000:
                cv.drawContours(frame, [cnt], -1, (255, 0, 0), 3)

        cv.imshow("frame", frame)
        cv.imshow("binary", binary)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
