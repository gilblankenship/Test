import itertools
import sys
import cv2
import os
import numpy as np
ProjectDirectory = 'C:\\Users\\gilbl\\PycharmProjects\\Test'
os.chdir(ProjectDirectory)
ImageDirectory=os.getcwd() + "\\TestImages\\"
print(ImageDirectory)

# image variables
name = "ImageArray" + ".jpg" #Name of the exported file
margin = 10 #Margin between pictures in pixels
w = 4 # Width of the matrix (nb of images)
h = 2 # Height of the matrix (nb of images)
n = w*h

filename_list = []

for file in os.listdir(ImageDirectory):
    if file.endswith(".jpg"):
        filename_list.append(file)

#filename_list.sort()

print(filename_list)

imgs = [cv2.imread(ImageDirectory+"/"+file) for file in filename_list]

#Define the shape of the image to be replicated (all images should have the same shape)
img_h, img_w, img_c = imgs[0].shape

#Define the margins in x and y directions
m_x = margin
m_y = margin

#Size of the full size image
mat_x = img_w * w + m_x * (w - 1)
mat_y = img_h * h + m_y * (h - 1)

#Create a matrix of zeros of the right size and fill with 255 (so margins end up white)
imgmatrix = np.zeros((mat_y, mat_x, img_c),np.uint8)
imgmatrix.fill(255)

#Prepare an iterable with the right dimensions
positions = itertools.product(range(h), range(w))

for (y_i, x_i), img in zip(positions, imgs):
    x = x_i * (img_w + m_x)
    y = y_i * (img_h + m_y)
    imgmatrix[y:y+img_h, x:x+img_w, :] = img

resized = cv2.resize(imgmatrix, (mat_x//4,mat_y//4), interpolation = cv2.INTER_AREA)
compression_params = [cv2.IMWRITE_JPEG_QUALITY, 99]
#cv2.imwrite(name, resized, compression_params)

cv2.imshow('Image Array',resized)
cv2.moveWindow('Image Array',100,200)

# Exit on key press
cv2.waitKey(0)
cv2.destroyAllWindows()