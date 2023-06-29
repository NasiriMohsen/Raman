import cv2 as cv
import numpy as np

cv.namedWindow("Window",cv.WINDOW_NORMAL)

address = "BBall.mp4"
Video = cv.VideoCapture(address)

rangemin = np.array([30,100,200])
rangemax = np.array([40,155,255])

while True:
    try:
        _,frame = Video.read()
        frameHSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        frameBin = cv.inRange(frameHSV,rangemin,rangemax)
        Filtered = cv.bitwise_and(frame,frame,mask = frameBin)
        Highlighted = cv.addWeighted(frame,0.5,Filtered,1,1)
   


        Contours = cv.findContours(frameBin,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[0]     
        if len(Contours) > 0:
            Contour = max(Contours,key=cv.contourArea)            
            
            Contourcricle = cv.minEnclosingCircle(Contour)
            Contourrect = cv.boundingRect(Contour)
            
            (Xr,Yr,W,H) = Contourrect
            ((Xc,Yc),R) = Contourcricle

            #cv.rectangle(Highlighted,(Xr,Yr),(Xr+W,Yr+H),(0,0,255),3)
            cv.circle(Highlighted,(int(Xc),int(Yc)),int(R),(0,255,0),3)
            cv.circle(Highlighted,(int(Xc),int(Yc)),1,(0,0,0),5)

        else:
            print("Contour not found")

    
        cv.imshow("Window",Highlighted)
        key = cv.waitKey(3)
        if ord("q") == key:
            print(rangemin,rangemax)
            cv.destroyAllWindows()
            break
    except Exception as err:
        print(err)
        break
