# Step 1
# initial the file import, get the frame, loop, etc

import cv2
import time
import datetime


cap = cv2.VideoCapture(0)

# Step 2
# Define the face_cascade for detect the face, this is build in from open cv library
# Also for body cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_fullbody.xml")

# Step 7. 
# Define the variable for record the frame
recording = True
frame_size = (int(cap.get(3)), int(cap.get(4))) #get the width and height
fourcc = cv2.VideoWriter_fourcc(*"mp4v") #it means four character code -> "m" + "p" + "4" + "v"
# 20  means fps
out = cv2.VideoWriter("Video.mp4", fourcc, 20, frame_size) 

while True:
    res, frame = cap.read()

    # Step 3.
    # Convert the frame to grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 4
    # Detect the face 
    # 1.3 means scale factor the numbers determines the accuracy and speed of this algorithm (between 1.01 (slower) - 1.5 (faster))
    # 5 means minimum number of neighbor (this means there is 5 boxes overlapping in the face to recognize that this is the face)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # To detect body
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    # Step 6.
    # If detect the face / body, we will record it
    if len(faces) + len(bodies) > 0:
        recording = True

    # To record a video
    out.write(frame)

    # Step 5
    # Draw rectangle in the face

    for (x,y, width, height) in faces:
        # Draw rectangle
        # cv2.rectangle(frame, (x,y), (x+width,y+height), (255,0,0), 2)
        pass


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if(key == ord('q')):
        break


out.release()
cap.release()
cv2.destroyAllWindows()