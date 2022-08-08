# Corner Detection

import numpy as np
import cv2 

img = cv2.imread('assets/chequerboard.jpg')
img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)

# when u need to detected the edges or corners u need to converting to grey scale before, because is lot of easy to detect
# make the new variable for contain a grey scale image
grayImages = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# it doest change anything because the image already black and white so it's a grey scale

# using shi-tomasi corner detector
# the parameters for goodFeaturesToTrack source image, number of corners, minimum quality(value between 0 - 1), and minimum euclidean distance
# euclidean distance is the distance between 2 value absolute distance between 2 point on a graph or  
# formula for calculate euclidean distance sqrt((x2-x1)^2 + (y2-y1)^2)

corners = cv2.goodFeaturesToTrack(grayImages, 20, 0.5, 10)
# because goodFeaturesToTrack return floating point we need to convert it into integer


corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    # what rovel does is conver multidimentional list into list [[x,y]] -> [x,y]

    # after get the corner and then the next step is just to draw the corners
    # draw the circle to every coordinates where the corners is exist
    cv2.circle(img, (x,y), 5, (255,0,0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):

        # why we need [0] because the list is multidimentional list, so u need took the first value of the array
        node1 = tuple(corners[i][0])
        node2 = tuple(corners[j][0])

        # because we only need 8 bit python int instead of numpy int (32/64 bit) we need to convert it into a regular int using map method builtin in python
        # and then after the mapping proccess is done u need to convert it into tuple
        color = tuple(map(lambda x: int(x),np.random.randint(0, 255, size=3)))
        cv2.line(img, node1, node2, color, 1)

# print(corners)
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()