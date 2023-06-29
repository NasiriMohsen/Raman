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

        yframe = len(frame)
        xframe = len(frame[0])

        print(xframe,yframe)

        cv.line(frame,(int(xframe/2),0),(int(xframe/2),yframe),(0,0,0),5)
        cv.line(frame,(0,int(yframe/2)),(xframe,int(yframe/2)),(0,0,0),5)
        cv.circle(frame,(int(xframe/2),int(yframe/2)),1,(0,0,255),5)

        print(xframe,yframe)

        frameHSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        blur = cv.blur(frameHSV,(10,10))
        frameBin = cv.inRange(blur,rangemin,rangemax)
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

            if Xc == xframe/2:
                statex = "Vasat"
            elif Xc > xframe/2 :
                statex = "Rast"
            else:
                statex = "Chap"

            if Yc == yframe/2:
                statey = "Vasat"
            elif Yc > yframe/2 :
                statey = "Paeen"
            else:
                statey = "Bala"

            state = statey + statex


            cv.putText(frame,state,(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv.LINE_4)
            
            cv.circle(frame,(int(Xc),int(Yc)),int(R),(0,255,0),3)
            cv.circle(frame,(int(Xc),int(Yc)),1,(0,0,0),5)

        else:
            print("Contour not found")

    
        cv.imshow("Window" ,frame)
        key = cv.waitKey(3)
        if ord("q") == key:
            print(rangemin,rangemax)
            cv.destroyAllWindows()
            break
    except Exception as err:
        print(err)
        break


#np.zeros_like()

