import cv2
import numpy as np
import os
path = os.getcwd()
#print(path) # C:\Users\gilbl\PycharmProjects
os.chdir(path + '\\Test\\')

# Load in image
img = cv2.imread('RedRose.jpg')

cv2.imshow('Original Image', img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower mask (0-10)
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join my masks
mask = mask0 + mask1

# set my output img to zero everywhere except my mask
output_img = img.copy()
output_img[np.where(mask == 0)] = 0

# or your HSV image
output_hsv = img_hsv.copy()
output_hsv[np.where(mask == 0)] = 0

cv2.imshow('mask', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
