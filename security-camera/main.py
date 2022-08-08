# Step 1
# initial the file import, get the frame, loop, etc

import cv2
import time
import datetime


cap = cv2.VideoCapture(0)

while True:
    res, frame = cap.read()
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if(key == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()