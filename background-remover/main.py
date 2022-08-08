import cv2
import cvzone
# selfisegmentation using mediapipe
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# to make camera up to 60FPS -> to make increase the framerate
cap.set(cv2.CAP_PROP_FPS, 60)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

# if you fail to load an image u can use this as a path of image
path = r'D:\Another Practice\open-cv practice\background-remover\assets\bg1.jpg'

# import img
# it should have the same size as the camera (640, 480)
# so we should resize image first
# make sure u open it in right directory

# if u cannot open it
# imgBg = cv2.imread(path)

imgBg = cv2.imread('assets/bg1.jpg')
imgBg = cv2.resize(imgBg, (640,480))
print(imgBg)
# cv2.imshow("HEI", imgBg)


# get all the image from directory
listImg = os.listdir('assets')

# calculate the length of the list
print(listImg)

# create list for every path in assets
imgList = []
for imgPath in listImg:
    # dont forget to load an image and then resize it as the same as the camera frame
    img = cv2.imread(f'assets/{imgPath}')
    img = cv2.resize(img, (640,480))
    imgList.append(img)

# print(len(imgList))
# print(imgList)
imageIndex = 0

 
while True:
    ret, frame = cap.read()
    print(imageIndex)
    # to remove background
    # output = segmentor.removeBG(frame, (255,0,255))


    # the parameter of removeBG () -> frame, color, threshold
    # threshold can contain 0 - 1, this can make u better crop in vbg, it's recommended using value 0.1
    # try to change threshold value
    # output = segmentor.removeBG(frame, (255,0,255), threshold=0.2)

    # using images as vitual background
    output = segmentor.removeBG(frame, imgList[imageIndex], threshold=0.2)

    # Find the framerate

    # make stack 2 column and 1 row
    imgStack = cvzone.stackImages([frame, output], 2,1)

    # display the FPS
    # fpsReader.update(imgStack)

    # to change the color of FPS fonts
    _,imgStack = fpsReader.update(imgStack, color=(0,0,255))

    cv2.imshow("image", imgStack)
    # cv2.imshow("image out", output)
    if cv2.waitKey(1) == ord('q'):
        break;
    elif cv2.waitKey(1) == ord('a'):
        if imageIndex>0:
            imageIndex -= 1
    elif cv2.waitKey(1) == ord('d'):
        if imageIndex < len(imgList)-1:
            imageIndex += 1


# cv2.waitKey(1)