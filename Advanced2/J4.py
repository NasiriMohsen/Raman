import cv2 as cv
import numpy as np

address = "ColorBall.jpg"
image = cv.imread(address)

cv.imshow("Window",image)
key = cv.waitKey(0) #daryaft Asci Keyboard
if ord("q") == key: 
    cv.destroyAllWindows() # bastan tamama window haye opencv
    











#[101  67   0] [118 255 255]

