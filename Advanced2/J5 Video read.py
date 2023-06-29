import cv2 as cv
import numpy as np

address = "BBall.mp4"
video = cv.VideoCapture(address)

while True:
    _,frame = video.read()
    
    cv.imshow("Window",frame)
    key = cv.waitKey(3)
    if ord("q") == key:
        cv.destroyAllWindows()
        break