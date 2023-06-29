import cv2 as cv
import numpy as np

address = "ColorBall.jpg"
image = cv.imread(address)

imageHSV = cv.cvtColor(image,cv.COLOR_BGR2HSV)

imagebin = cv.inRange(imageHSV,np.array([101,67,0]),np.array([118,255,255]))
imagebin2 = cv.inRange(imageHSV,np.array([0,129,0]),np.array([6,255,255]))
Filtered = cv.bitwise_or(imagebin,imagebin2)
Filtered2 = cv.bitwise_and(image,image,mask=Filtered)



cv.imshow("Window",image)
cv.imshow("Window2",imageHSV)
cv.imshow("Window3",imagebin)
cv.imshow("Window4",Filtered2)
cv.waitKey(0)





#imagecopy = np.copy(image)