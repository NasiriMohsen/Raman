import cv2 as cv
import numpy as np

def Nothing(x):
    pass

cv.namedWindow("Window",cv.WINDOW_NORMAL)

cv.createTrackbar("Hmin","Window",0,255,Nothing)
cv.createTrackbar("Hmax","Window",0,180,Nothing)
cv.createTrackbar("Smin","Window",0,255,Nothing)
cv.createTrackbar("Smax","Window",0,255,Nothing)
cv.createTrackbar("Vmin","Window",0,255,Nothing)
cv.createTrackbar("Vmax","Window",0,255,Nothing)

cv.setTrackbarPos("Hmax","Window",180)
cv.setTrackbarPos("Smax","Window",255)
cv.setTrackbarPos("Vmax","Window",255)

address = "ColorBall.jpg"

while True:
    Image = cv.imread(address)
    ImageHSV = cv.cvtColor(Image,cv.COLOR_BGR2HSV)

    Hmin = cv.getTrackbarPos("Hmin","Window")
    Smin = cv.getTrackbarPos("Smin","Window") 
    Vmin = cv.getTrackbarPos("Vmin","Window") 
    Hmax = cv.getTrackbarPos("Hmax","Window")
    Smax = cv.getTrackbarPos("Smax","Window") 
    Vmax = cv.getTrackbarPos("Vmax","Window") 

    rangemin = np.array([Hmin,Smin,Vmin])
    rangemax = np.array([Hmax,Smax,Vmax])

    ImageBin = cv.inRange(ImageHSV,rangemin,rangemax)

    Filtered = cv.bitwise_and(Image,Image,mask = ImageBin)

    cv.imshow("Window",Filtered)
    key = cv.waitKey(1)
    if ord("q") == key:
        print(rangemin,rangemax)
        cv.destroyAllWindows()
        break
