# import open cv first
import cv2 

# load img from the directory
# the second parameter from imgread method can contain -1, 0, and 1
img = cv2.imread('assets/img1.png', 0)

# Resize the image based on the width or height you want
# img = cv2.resize(img, (800,400))

# Resize the image based on the scale you want
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# rotate the image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# write the file to a folder save it to your computer after manipulation process of the images
cv2.imwrite('assets/new_img.jpg', img)

# for show the images
cv2.imshow('Image', img )

# initialization for user to press the key
cv2.waitKey(0)
cv2.destroyAllWindows()