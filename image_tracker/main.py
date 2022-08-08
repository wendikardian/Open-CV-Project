# The image tracker first of all you need to tract what object you wanna follow, and then press enter ,, so the tracking is began

# The detail tracker blog how it works
# https://ehsangazar.com/object-tracking-with-opencv-fd18ccdd7369?gi=998b35a127d7



# STEP 1. Initialization camera packages and many more

import cv2

cap = cv2.VideoCapture(0)

# U need install opencv opencv-contrib-python

# STEP 4. Create a tracker using this one
# Try using it first
# tracker = cv2.TrackerMOSSE_create()

# If it's doesnt work try with this one


tracker = cv2.legacy.TrackerMOSSE_create()



res, frame = cap.read()

# STEP 5. Create a bounding box using selectROI, after that start initialization the tracking of the frame using the bounding box
# Create a bounding box to select where the tracker is gonna tract the area
# So the mouse can using for tracking an frame

boundingBox = cv2.selectROI("Frame", frame, False)

# start initialization the frame using the bounding box 
tracker.init(frame, boundingBox)

# STEP 8. Declare a draw box function to create a box inside the frame
def drawBox(frame, boundingBox):

    # STEP 9. before draw the box, we need convert the bounding box (tuple) to an integer value
    # The bounding box is the tuple where is contain 4 value, the x coordinates, the y coordinates, the width, and then the hight
    x, y, w, h = int(boundingBox[0]), int(boundingBox[1]), int(boundingBox[2]), int(boundingBox[3])

    # STEP 10. Draw a rectangle and then put the text
    cv2.rectangle(frame, (x,y), ((x+w), (y+h)), (255,0,255), 3,1 )
    cv2.putText(frame, "TRACKING", (100,100), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
    


while True:

    # STEP 2 create a timer, and FPS, and then dont forget to put text on the frame
    timer = cv2.getTickCount()
    res, frame = cap.read()

    # STEP 6.Get a bounding box from the tracker
    # Update the tracker
    res, boundingBox = tracker.update(frame)

    # STEP 7 . Check the conditional if the bounding box of the tracker is successfully catch the fram
    # If success it will draw the box, other than that it will write text LOST

    if res:
        drawBox(frame, boundingBox)
    else:
        cv2.putText(frame, "LOST", (100,100), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 2)

    # Get the FPS
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    # Get the FPS of the camera
    cv2.putText(frame, str(int(fps)), (20,20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 2)

    # STEP 3. Show The image
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break;