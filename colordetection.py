# Trackbar and Color detection

import cv2
import cvzone
import numpy as np

# function that empty will not doing anything, just pass it
def empty(a):
    pass

# Creating a trackbar
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)

# Create a trackbar with minimum value 0 and the maximum value is 179
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)

# the parameter is : the name of the bar, the windows, default value, max value, and then empty function
# cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
# cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
# cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
# cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
# cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

# After trying to find the best value of the bar, save the data and the try change the default value
cv2.createTrackbar("Hue Min", "Trackbars", 10, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 92, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 70, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 40, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

# After all of the setting, the color will make it the best HSV value


while True:

    img = cv2.imread('assets/img1.png')

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # get trackbar value
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # Create a mask using numpy array
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)


    # Create a result based on mask
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # Create stack images
    imgStack1 = cvzone.stackImages([img,imgHSV],2, 1)
    imgStack2 = cvzone.stackImages([mask,imgResult],2, 1)
    imgStack = cvzone.stackImages([imgStack1,imgStack2], 1, 2)
    imgStack = cv2.resize(imgStack, (800, 400))

    cv2.imshow('Frame', imgStack)
    # cv2.imshow('Frame', img)
    # cv2.imshow('Frame 2', imgHSV)
    # cv2.imshow('Frame 2', mask)
    # cv2.imshow('Frame 2 Max', imgResult)

    cv2.waitKey(1)