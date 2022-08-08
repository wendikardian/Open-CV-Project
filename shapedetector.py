# Contours / Shape Detection

import cv2
import cvzone
import numpy as np

def getContours(img):

    # To find contours
    # parameter -> frame, method, method
    contours, Hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # find the edges
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        # Draw contours
        # Parameter -> frame, contour, contour index, color, and thickness
        # -1 because we want draw all the contour
        # cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)

        # Check the minimum area give a threshold
        # So if you cannot detect any noise of the images

        # if area:
        if area > 200:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)

            # Calculate the curve length
            # to help aproximate the edges of the area
            params = cv2.arcLength(cnt, True)
            # print(params)

            # Calculate how many corner are we have
            approx = cv2.approxPolyDP(cnt, 0.02*params, True)

            # It will display approx how many corner are we have
            print(len(approx))
            objCor = len(approx)

            # Create a boundingBox
            # it will x,y, width, height of the object
            x , y , w, h = cv2.boundingRect(approx)
            objectType = ""
            if objCor == 3:
                objectType = "Tri"

            # If the shape is circle, circle probably has a lot of object corner
            elif objCor >7 :
                objectType = "Circle"
            elif objCor == 4:
                # There is 2 possibility in this case between square or rect
                # if the aspect ratio == 1 (or maybe a little bit more or lesser ) it square, other than that is rectangle
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio <1.05:
                    objectType = "Square"
                else:
                    objectType = "Rect"
                    
            else:
                objectType = "Dont know"
                

            # After we found the boundingRect tangle location of the contours,
            # we will draw a rectangle between it 
            # and then try to run let see if there is a new rectangle between the object
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,0,255), 2)

            # We will place a text in the center of the object
            cv2.putText(imgContour, objectType,(x + (w//2) -10, y+(h//2) -10 ), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255), 2)






img = cv2.imread('assets/shape.jpg')
imgContour = img.copy()

imgGrayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Parameter for imgBlur -> the picture, the kernel, the sigma
imgBlur = cv2.GaussianBlur(imgGrayScale, (7,7), 1)

# Parameter for Canny -> frame, threshold,
# create an image canny that will return the black and white using threshold
imgCanny = cv2.Canny(imgBlur, 50,50)
getContours(imgCanny)

# Create a stack image
imgStack1 = cvzone.stackImages([img,imgGrayScale],2, 1)
imgStack2 = cvzone.stackImages([imgStack1,imgCanny],2, 1)
imgStack3 = cvzone.stackImages([imgStack2,imgBlur],2, 1)
imgStack = cvzone.stackImages([imgStack3,imgContour],2, 1)


cv2.resize(imgStack, (300,100))


# cv2.imshow("Original Picture", img)
# cv2.imshow("Blue Picture", imgGrayScale)
# cv2.imshow("Blue Picture", imgBlur)
cv2.imshow("Stack Picture", imgStack)



cv2.waitKey(0)