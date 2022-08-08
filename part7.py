# Template matching or Object detection
import numpy as np
import cv2

# if you want load the image as a grey scale just add 0 at the second parameter

# if the picture just too big u can resize the image
# but if you resize the base image, u also need to resize the template image too
img = cv2.imread('assets/avanger.jpg',0 )
imgClear = cv2.imread('assets/avanger.jpg' )


# u can change this one using the other image
thor = cv2.imread('assets/thor.jpg', 0)
h, w = thor.shape

# if you print the img it will display 2 dimensions list because is grey scale
# try to delete the 0 at the imread parameter, and it will display 3 dimensions list
# print(img)

# there is a lot of template matching algorithm out there to find the image,
# with the different method it will perform different based on speed and the result

# when you try to create a template project u can search another method that give you the best performance and give you the best result, so it can use for afterwards

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, thor, method)
    # it's called convolution, taking our template img and the sliding it around in the base image and then find the most close to the template img
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # this is print where is the exactly location the template img where it is
    # print(min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    # after find the location where the template is in the main img, just drawing a rectangle between the template

    # the location variable is contain the top left coordinates
    # after find the top left coordinates you need to find bottom right coordinates to draw rectangle 
    # you can find it based on the variable width and height of the image template

    btm_right = (location[0]+ w, location[1] + h)
    # cv2.rectangle(img2, location, btm_right, 255, 5 )

    # if you want show the clear one
    cv2.rectangle(imgClear, location, btm_right, (0,0,255), 5 )

    cv2.imshow('Match', imgClear)

    # sometimes the method is not always perfect u just need the perfect one where can be used for matching the template to the image

    # the picture display  6 times because there is 6 methods to matchTemplate
    cv2.waitKey(0)
    cv2.destroyAllWindows()
