import cv2 as cv 
import numpy as np

cascade = cv.CascadeClassifier("Har/frontalcatface.xml")

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv.imshow("Frame",frame)
    key = cv.waitKey(1)
    if ord("q") == key:
        cv.destroyAllWindows()
        break