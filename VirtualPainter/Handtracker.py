# Step 1, initialization the file (import, webcam, etc)

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

# Step 2. 
# Define the tracker for hands that we are going to use for tracking a hand from mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    res, frame = cap.read()

    # Step 3
    # Because the frame is BGR color, we need to convert it to RGB color because hands on MP only can work for RGB color
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Step 4
    # After we convert it into RGB color, we need to process it using the hands variable that already created before
    results = hands.process(frameRGB)

    # Step 5
    # Try to print the results, to find out what is inside the results
    # The results print, it print class mediapipe solitionOutput
    # print(results)
    # To detect if there some hands on the camera using this one
    # print(results.multi_hand_landmarks)

    # Step 6
    # If there is a hand detected on the camera
    if results.multi_hand_landmarks:
        # We will loop it, because maybe there is much more than 1 hand on the camera
        for handLms in results.multi_hand_landmarks:

    cv2.imshow("Frame", frame)

   


    key= cv2.waitKey(1)
    if key == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()