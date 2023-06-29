import cv2 as cv
import numpy as np

cv.namedWindow("Window",cv.WINDOW_FREERATIO)

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    frame2= np.copy(frame)

    yframe = len(frame)
    xframe = len(frame[0])

    cv.line(frame2,(int(xframe/2),0),(int(xframe/2),yframe),(0,0,0),2)  
    cv.line(frame2,(0,int(yframe/2)),(xframe,int(yframe/2)),(0,0,0),2)  
    cv.circle(frame2,(int(xframe/2),int(yframe/2)),1,(0,0,255),1)

    frameHSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    rangemin = np.array([75,120,0])
    rangemax = np.array([95,255,255])

    frameBin = cv.inRange(frameHSV,rangemin,rangemax)
    Filtered = cv.bitwise_and(frame,frame,mask = frameBin)

    Contours = cv.findContours(frameBin,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[0]  

    if len(Contours) > 0:
        Contour = max(Contours,key=cv.contourArea)          
        
        Contourcricle = cv.minEnclosingCircle(Contour)
        Contourrect = cv.boundingRect(Contour)
        
        (Xr,Yr,W,H) = Contourrect
        ((Xc,Yc),R) = Contourcricle

        state = ''
        statex = ""
        statey = ""

        if int(Xc) == int(xframe/2):
            statex = "Vasat"
        elif int(Xc) > int(xframe/2) :
            statex = "Rast"
        else:
            statex = "Chap"

        if int(Yc) == int(yframe/2):
            statey = "Vasat"
        elif int(Yc) > int(yframe/2) :
            statey = "Paeen"
        else:
            statey = "Bala"

        state = statey + statex

        #cv.line(frame2,(int(Xc),0),(int(Xc),yframe),(0,0,0),2)  
        #cv.line(frame2,(0,int(Yc)),(xframe,int(Yc)),(0,0,0),2)  
        ##cv.line(frame2,(Xr,Yr),(Xr+W,Yr+H),(255,0,0),5)   
        ##cv.rectangle(frame2,(Xr,Yr),(Xr+W,Yr+H),(0,0,255),3)
        cv.circle(frame2,(int(Xc),int(Yc)),int(R),(0,0,255),3)
        cv.circle(frame2,(int(Xc),int(Yc)),1,(0,0,255),5)

        font = cv.FONT_HERSHEY_SIMPLEX 
        text = ( "X: " + str(int(Xc)) + " Y: " + str(int(Yc)) + " " + state)
        cv.putText(frame2,text,(50,50),font,1,(0,0,0),3)
    
    else:
        print("Contour not found")


    cv.imshow("Window",frame2)
    key = cv.waitKey(1)
    if ord("q") == key:
        cv.destroyAllWindows()
        break