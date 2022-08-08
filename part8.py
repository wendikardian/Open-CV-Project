#  Face and eye detection

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# features already contain in cv2 library
# features is used from model that contain in open cv library to detect where is face and where is eye
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# features in cv2 -> classified where is face in eye
while True:
    ret, frame = cap.read()

    # convert it to grey scale video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect the face
    # Read the materials about detechMultiScale parameters in here
    # https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # Draw the rectangle
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 5 )

        # row first and then column
        # split the video
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+w, x:x+w]

        # detect the eye from the face based on grey scale 
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        # find the eye of the face
        for(ex, ey, ew, eh) in eyes:
            # draw the rectangle
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()