import cv2 as cv
import numpy as np

def Nothing(x):
    pass

cv.namedWindow("Window",cv.WINDOW_FREERATIO)

cv.createTrackbar("Hmin","Window",0,255,Nothing)
cv.createTrackbar("Hmax","Window",0,180,Nothing)
cv.createTrackbar("Smin","Window",0,255,Nothing)
cv.createTrackbar("Smax","Window",0,255,Nothing)
cv.createTrackbar("Vmin","Window",0,255,Nothing)
cv.createTrackbar("Vmax","Window",0,255,Nothing)

cv.setTrackbarPos("Hmax","Window",180)
cv.setTrackbarPos("Smax","Window",255)
cv.setTrackbarPos("Vmax","Window",255)

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    frameHSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    Hmin = cv.getTrackbarPos("Hmin","Window")
    Smin = cv.getTrackbarPos("Smin","Window") 
    Vmin = cv.getTrackbarPos("Vmin","Window") 
    Hmax = cv.getTrackbarPos("Hmax","Window")
    Smax = cv.getTrackbarPos("Smax","Window") 
    Vmax = cv.getTrackbarPos("Vmax","Window") 

    rangemin = np.array([Hmin,Smin,Vmin])
    rangemax = np.array([Hmax,Smax,Vmax])

    frameBin = cv.inRange(frameHSV,rangemin,rangemax)

    Filtered = cv.bitwise_and(frame,frame,mask = frameBin)

    cv.imshow("Window",Filtered)
    key = cv.waitKey(1)
    if ord("q") == key:
        print(rangemin,rangemax)
        cv.destroyAllWindows()
        break


#[ 70 120   0] [ 95 255 255]