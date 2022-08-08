# Using Yolo algorithm to detect the object
# To get the data visit this https://pjreddie.com/darknet/yolo/

# https://www.youtube.com/watch?v=9AycYn9gj1U&list=PLMoSUbG1Q_r8nz4C5Yvd17KaXy8p0ufPH&index=2
# Complete these series, last episode 2 --> next day

# The .cfg file is the configuration and architecture file of yolo 3 to run our network

# STEP 1. Initialization the package and the cap until video display on the window
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# width, height, Target ... because using yolo 320
whT = 320

# Define confidence threshold value , the standard for the confidence that we need
confThreshold = 0.5

# define the nms threshold
nmsThreshold = 0.3


# STEP 2. Read the file from coco.names and store the data
# Define an empty list to collect object name 
file = 'coco.names'
classNames = []

# STEP 3. Open the data and then store the data one by one every line
with open(file, 'r') as f:
    # Extract the information on the file coco.names and then store it on className

    # read the data and then seperate it using enter or ('\n') and then split the data
    classNames = f.read().rstrip('\n').split()

print(classNames)
# Try to display the name
# print(className)
# print(len(className))


# STEP 4. Add configuration file

modelConfiguration = 'yolo3-320.cfg'
modelWeights = 'yolov3.weights'

# So if the speed of your detector quit slow or with low fps, u can use yolo3-tiny instead of yolo3-320

# Add network configuration

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

# STEP 5.
# Use OpenCV as a backend
# And we are going to use CPU

net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


# The method to find the object
def findObjects(outputs, frame):
    h, w, t = frame.shape
    boundingBox = []
    classIds = []
    confidences = []

    for output in outputs:
        for det in output:
            # Because the first 5 elements is only contain data from the bounding box, we need to destroy that, other than that is the object with their confidence
            # After we remove first 5 elements, we need to find the index with highest confidence
            # Remove first 5 value
            scores = det[5:]

            # Find the maximum value of the index
            classId = np.argmax(scores)
            # After find the maximum value store it con confidence list
            confidence = scores[classId]

            # Filtering the objects
            # If the confidence is higher than 0.5 we will keep it
            if confidence > confThreshold:

                # After find the area with good confidence we need to get width and height
                # 2 is the dimension for the width
                # 3 is the dimension for the height
                # After that we need multiply it by the width and height of the our camera frame, so we can get the actual width and height
                # because it returning a floating point, we need to convert to into an integer value
                wT, hT = int(det[2]*w), int(det[3] * h)
                
                # To find the actual coordinates of the object, we need calculate with this formula
                # 0 is dimension for the center x coordinates (so we need to subtract it to find top left)
                # 1 is dimension for the center y coordinates (so we need to subtract it to find bottom right)
                x, y = int((det[0] *w)-wT/2), int((det[1] *h) - hT/2)

                # After find the value add it to boundingBox list
                boundingBox.append([x,y,w,h])
                classIds.append(classId)
                confidences.append(confidence)

    # try to print the length of the boundingBox
    # print(len(boundingBox))

    # STEP 13. 
    # We need to tell the cv2 which boundingBox we need to keep and then store it in variable called indices
    indices = cv2.dnn.NMSBoxes(boundingBox, confidences, confThreshold, nmsThreshold)

    # Check the value of the indices 
    print(indices)

    # After find the indices, we just need to draw out bounding boxes using for loop
    for i in indices:
        box = boundingBox[i]

        # Get the dimension of the detected object of the bounding boxes
        x, y, w, h = box[0], box[1], box[2], box[3]

        # Draw the rectangle 
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 2)

        # Put the text
        # classNames[classIds[i]].upper() -> will return a object name 
        # int(confidences[i]*100) -> will return the accuracy of confidence -> because it return a floating value we need to multiply it by 100 and convert it to an integer
        cv2.putText(frame, f'{classNames[classIds[i]].upper()} {int(confidences[i]*100)} %', (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,0), 2)






while True:
    res, frame = cap.read()

    # STEP 5.  Convert the frame into blob
    blob = cv2.dnn.blobFromImage(frame, 1/255, (whT, whT), [0,0,0], 1, crop= False)
    net.setInput(blob)

    # Because there is 3 layer between blob image architechture, we need to get the layer that we want to detect 
    layerNames = net.getLayerNames()

    # After get the layer try to print it 
    # print(layerNames)

    # We only need the output layer, so to do that, we need to extract the layers first using net.getUnconnectedOutLayers()
    outputLayer = net.getUnconnectedOutLayers()
    # Try to print it, but we only get the index value out the output layer
    print(outputLayer)

    # STEP 6. get the output layer name
    # Because the getUnconnectedOutLayers return an array value of the index we need find it on layerNames
    # Because array start from number 1 we need to subtract the index first
    # We need to loop the indexes from output layer, because the length of the list is 3, so we need to iterate them
    outputNames = [layerNames[i-1] for i in outputLayer]

    # Try to print outputNames and see the result
    # So this is the output names of our layer
    print(outputNames)

    # STEP 7. Send the output names 
    outputs = net.forward(outputNames)

    # STEP 8. Try to see the output length
    print(len(outputs))

    # STEP 9. Try to see the type of the outputs
    # it will return a list // tuple
    print(type(outputs))

    # STEP 10. if you try to find out what is inside the list or tuple you just need to print the index of number0
    # It will return numpy.ndarray
    print(type(outputs[0]))

    # STEP 11. After you find out this is the ndarray u also can see the shape of the object -> it will return the dimension width and height of the object
    # Because we have 3 outputs we can see each one by one
    # print(outputs[0].shape)
    # print(outputs[1].shape)
    # print(outputs[2].shape)


    # Or you just need print it using a for loop

    # for i in range(3):
    #     print(outputs[i].shape)
    
    # The output example is (300, 85) -> 300 means it produce 300 bounding boxes and then

    # STEP 12. After find the bounding box, u just need find the value of each bounding box by access the index one 
    # U can see the image on whatsapp doc, about the table of bounding boxes
    # print(outputs[0][0])
    # It will print [6.4129271e-02 4.7940008e-02 3.3911458e-01 2.4004607e-01 4.0008019e-09 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 ...... ]

    # One of the value of bounding boxes is the confidence, it means how confidence about this object on bounding box based on coco.names
    # The next step is, we only need to find the good confidence based on coco.names object, so the bounding boxes will keep, other than that it will be removed
    # Using findObjects()
    # we passing outputs and the frame from camera as the parameters
    findObjects(outputs, frame)


    cv2.imshow("Frame", frame)
    cv2.waitKey(1)