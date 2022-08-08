# HSV Color

# there is a lot of type color 
# RGB , BRG, HSV (Hue Saturation and Lightness)

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # you can pick your own color from here https://colorpicker.me/#020719

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255,255])

    # this code using for masked the image, so the code tell the python which color is needed to keep 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # in this case the pixel who has color blue will keep and then the others will turn to black
    result = cv2.bitwise_and(frame, frame, mask = mask)
    # bitwise_and mean it operates the and operator where it will return 1 when the all value is 1
    # it compare the frame with the mask that we made, if the color same it will keep, but when it does'nt it will turn into black
    cv2.imshow('frame', result)

    # if the mask displayed 
    # if the only mask that contains it will display just black and white
    # cv2.imshow('frame', mask)



    if(cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()


# If you want to pick your own color, u can use this method 
# using numpy array and then you can pass it using BRG color
# using this method you can get HSV value using numpy array

# BGR_color = np.array([[[255,0,0]]])
# x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
# print(x[0][0])