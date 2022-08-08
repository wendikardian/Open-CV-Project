import cv2
import random

img = cv2.imread('assets/img1.png', -1)
# print(type(img))

# print(img)

# print(img.shape)

# manipulated image using random to make random color in the first 100 row of the image matrix
# for i in range(100):
#     for j in range(img.shape[1]):
#          img[i][j] = [random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)]


# how to copy img and crop it
print(img.shape)
img2 = img[100: 300, 200 : 400]

# paste an image 
img[0:200, 0:200] = img2
img[100:300, 100:300] = img2

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()