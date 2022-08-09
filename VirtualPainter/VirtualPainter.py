# Step 1
# Declare and initialization

import cv2
import numpy as np
import time
import os # We need to access the file
import HandTrackingModule as htm #import the file that contain class we need to use


# Step 2. List the directory that we're going use to collect the image file
myListDirectory = os.listdir("header")
print(myListDirectory)

overlayList = []


# Step 3
# Load the image one by one using for loop and append it to list called overlayList
for imPath in myListDirectory:
    image = cv2.imread(f'header/{imPath}')
    overlayList.append(image)

# print(len(overlayList))

# Step 4
# initial default header
header = overlayList[0]

# Step 12
# Initialization the initial color for the first time to purple
drawColor = (0,0,255)

brushThickness = 7
xp, yp = 0,0 

# Step 14
# We will declare a new canvas for drawing
# Instead of drawing on the layout, we can create a new canvas
imgCanvas = np.zeros((720, 1280, 3), np.uint8) 


cap = cv2.VideoCapture(0)
cap.set(3, 1280) # Setting the width of the window
cap.set(4, 720)

# Step 6 find hand landmark
detector = htm.handDetector(detectionConfidence = 0.85)

while True:
    res, frame = cap.read()

    # Step 7. Flip the images
    # Make it easier and accurate for drawing 
    frame = cv2.flip(frame, 1) 

    # Step 6
    # Find Hand Landmark
    frame = detector.findHands(frame) #To activate the hand detector
    # Create a new list that will contain all hand landmark id and position
    lmList = detector.findPosition(frame, draw=False)
    
    if len(lmList) != 0:
        # print(lmList)

        # Tip of the index and middle finger
        x1, y1 = lmList[8][1:] # utnuk menemukan ujung jari telunjuk
        x2, y2 = lmList[12][1:] #untuk jari tengah 

        # Step 8
        # Check if the fingers are up
        fingers = detector.fingersUp()
        # Example output, it means 3 fingers up (jempol, telunjuk, tengah)
        # [1, 1, 1, 0, 0]
        # print(fingers)

        # Step 9
        # If selection mode (2 finger ups)
        if fingers[1] and fingers[2]:
            print("Selection mode")
            # If on selection mode there is rectangle on the finger
            cv2.rectangle(frame, (x1,y1-25), (x2, y2+25), drawColor, cv2.FILLED)

            # Step 11. We're going work with selection mode first
            # Check the location of the selection mode
            if y1<125:
                if 320 < x1 < 480:
                    header = overlayList[0]
                    drawColor = (0,0,255)
                elif 480 < x1 < 630:
                    header = overlayList[1]
                    drawColor = (0,255,0)
                elif 650 < x1 < 840:
                    header = overlayList[2]
                    drawColor = (255,0,0)
                elif x1> 1000:
                    header = overlayList[3]
                    drawColor = (0,0,0)
        

        # Step 10
        if fingers[1] and fingers[2] == False:
            print("Drawing Mode")
            # If on selection mode there is circle on the finger
            cv2.circle(frame, (x1, y1), 15, drawColor, cv2.FILLED)
            # the logic by drawing circle
            # Logic at drawing, if you on drawing mode u will draw a circle (if move), 
            # Otherwise, if you dont move your finger it will not draw a circle

            # Other than that, you can draw using a line'

            # Step 13
            # this case if the first time run the program initial value is 0, it will be bad if we doest add this
            # So we need to change first
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv2.line(frame, (xp, yp), (x1,y1), drawColor, brushThickness)
            cv2.line(imgCanvas, (xp, yp), (x1,y1), drawColor, brushThickness)
            xp, yp = x1, y1 #keep updating if the finger move, so the previous will contain the last coordinates

            # As you can see if you just add this code, it will just draw and the remove it as soon as possible, 
            # We will keep it forever, unless it's deleted using eraser

    #Step 5
    # Overlapping the frame with the header to draw the line
    # Setting the header image
    frame[0: 125, 0:1280] = header

    cv2.imshow("Frame", frame)

    # Try to add this to see the result of the canvas
    cv2.imshow("Canvas", imgCanvas)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()