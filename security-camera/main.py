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
detection = True
detection_stop_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4))) #get the width and height
fourcc = cv2.VideoWriter_fourcc(*"mp4v") #it means four character code -> "m" + "p" + "4" + "v"
# 20  means fps
# out = cv2.VideoWriter("Video.mp4", fourcc, 20, frame_size) 

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
        if detection:
            timer_started = False
        else:
            detection = True
            # Get the current time for the name of the video time
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size) 
            print("Started recording")
    elif detection: #if we not get faces or bodies but we still on detect previous time, we will still record it until that period of time
        if timer_started:
            # If the frame did not detect any face for 5 second, it will stop recording and then save the video
            if time.time() - detection_stop_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stop Recording")
        else:
            timer_started = True
            detection_stop_time = time.time()


    # To record a video
    # Only if we detect something
    if detection:
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