# Code to find the color of a pixel selected with the mouse
# From Stackoverflow.com : https://tinyurl.com/y23cal7h
import cv2

def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)

cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

capture = cv2.VideoCapture(0) # The builtin webcam

while(True):
    ret, frame = capture.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('mouseRGB', frame)

    k = cv2.waitKey(0)
    if k == 27:  # press ESC key to exit
        capture.release()
        cv2.destroyAllWindows()
