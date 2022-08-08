# Camera and Video Capture

import cv2
import numpy as np
# install default when u install cv2

cap = cv2.VideoCapture(0)
# if you dont have camera and then u can use it using internal video from your folder
# instead place 0 in parameter u can using string in the parameters it and then store the location where u put the video
# Example cap = cv2.VideoCapture('assets/video.mp3')

while True:
    # ret is for check if there webcam is used or not, if used it will return false and then it cannot operate
    # frame is the image from the camera
    ret, frame = cap.read()

    width = int(cap.get(3)) 
    # three means is the code for property width

    height = int(cap.get(4))
    # four means is the code for get property height

    # when u passing image variabel to imshow it will display a black screen but with the same shape as the camera
    image = np.zeros(frame.shape, np.uint8)
    little_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    # for the top left
    # when u trying rotate the image 90 degree then will comes and error because the size is not the same could not broadcast input array from shape (320,240,3) into shape (240,320,3)
    # image[:height//2, :width//2] = cv2.rotate(little_frame, cv2.ROTATE_90_CLOCKWISE) 
    image[:height//2, :width//2] = cv2.rotate(little_frame, cv2.ROTATE_180)  
    # for the bottom left
    image[height//2:, :width//2] = little_frame 
    # for the top right
    image[:height//2, width//2:] = cv2.rotate(little_frame, cv2.ROTATE_180) 
    # for the bottom right
    image[height//2:, width//2:] = little_frame 





    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('q'):
        break;

# to make sure to turn off the camera resource so the other app can use it
cap.release()
cv2.destroyAllWindows()

