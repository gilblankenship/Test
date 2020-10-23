#https://stackoverflow.com/questions/31460267/python-opencv-color-tracking/31465462#31465462
import numpy as np
import cv2

sensitivity = 15
lower_white = np.array([0, 0, 255 - sensitivity])
upper_white = np.array([180, sensitivity, 255])

# For other colors:
green = 60
blue = 120
yellow = 30

# Set a color for testing
color = green

# Define thresholds
lower_color = np.array([color - sensitivity, 100, 100])
upper_color = np.array([color + sensitivity, 255, 255])

# Red H value is 0, so you need to take two ranges and "OR" them together:
lower_red_0 = np.array([0, 100, 100])
upper_red_0 = np.array([sensitivity, 255, 255])
lower_red_1 = np.array([180 - sensitivity, 100, 100])
upper_red_1 = np.array([180, 255, 255])

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, lower_red_0 , upper_red_0);
    mask2 = cv2.inRange(hsv, lower_red_1 , upper_red_1 );

    mask = cv2.bitwise_or(mask1, mask2)

    cv2.imshow('Mask', mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
