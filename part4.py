import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # parameter of line, the frame, the start coordinates, the last coordinates, the color of the line, the last one is line thickness
    img = cv2.line(frame, (0,0), (width, height), (0,0,255), 10)
    img = cv2.line(img, (width,0), (0, height), (0,0,255), 10)

    # parameter of the rectangle, the frame, the first start rec coordinates, the last coordinates, the color, and the thickness
    img = cv2.rectangle(img, (100, 100), (200,200), (0,0,0), 10)

    # circle
    # when u pass thickness of the circle -1 it's gonna fill the color for the whole circle
    # parameters of the circle, the frame, the coordinates of the center of the circle, the radius, the color, and the thickness of the circles
    img = cv2.circle(img, (300,300 ), 60, (0,0,100), -1)

    # Draw the text

    font = cv2.FONT_HERSHEY_SIMPLEX

    # the parameter of put text the frame, the text, the coordinates, the font, scale, color, thickness, the extra arguments to make your font better (line type)
    img = cv2.putText(img, "Hello my name is Wendi", (50, height - 20), font,1, (0,0,200), 3, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()