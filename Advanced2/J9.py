import cv2 as cv
import numpy as np

addr =  "Har/frontalface_alt.xml"
addr2 =  "Har/eye.xml"
addr3 =  "Har/smile.xml"
Cascade = cv.CascadeClassifier(addr)
Cascade2 = cv.CascadeClassifier(addr2)
Cascade3 = cv.CascadeClassifier(addr3)


webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    face = Cascade.detectMultiScale(gray,1.2,4)
    eyes = Cascade2.detectMultiScale(gray,1.2,10)
 

    for i,(x,y,w,h) in enumerate(face):
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        smile = Cascade3.detectMultiScale(gray[y:y+h,x:x+w],1.1,8)
        for z,(xs,ys,ws,hs) in enumerate(smile):
            cv.rectangle(frame[y:y+h,x:x+w],(xs,ys),(xs+ws,ys+hs),(0,0,255),2)
    for j,(x,y,w,h) in enumerate(eyes):
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        

    cv.imshow("Windows",frame)
    key = cv.waitKey(1)
    if ord("q") == key:
        cv.destroyAllWindows()
        break



