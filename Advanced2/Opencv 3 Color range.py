import cv2 as cv
import numpy as np

address = "ColorBall.jpg"
image = cv.imread(address)
imageHSV = cv.cvtColor(image,cv.COLOR_BGR2HSV)

imagebin = cv.inRange(imageHSV,np.array([101,67,0]),np.array([118,255,255]))

cv.imshow("Window",image)
cv.imshow("Window2",imageHSV)
cv.imshow("Window3",imagebin)
cv.waitKey(0)





