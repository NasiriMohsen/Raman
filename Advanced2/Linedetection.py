import cv2 as cv
import numpy as np

def mokhtasat(Khat,ymin,ymax):
    Shib,Arz = Khat
    Y1 = ymax
    Y2 = ymin
    X1 = int((Y1-Arz)/Shib)
    X2 = int((Y2-Arz)/Shib)
    return int(abs(X1)),int(abs(Y1)),int(abs(X2)),int(abs(Y2))

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    
    #Cannyrgb = cv.cvtColor(Canny,cv.COLOR_GRAY2BGR)

    yframe = len(frame)
    xframe = len(frame[0])

    frame2 = np.copy(frame)
    
    #frameroi = np.array([[(0,yframe),(xframe,yframe),(xframe-50,0),(50,0)]])
    #blankframe = np.zeros_like(frame)
    #cv.fillPoly(blankframe,frameroi,(255,255,255))
    
    Canny = cv.Canny(frame,200,500)
    #ROI = cv.bitwise_and(Cannyrgb,blankframe)
    #CannyROI = cv.Canny(ROI,200,500)


    

    Lines = cv.HoughLinesP(Canny,2,np.pi/180,100,np.array([]),minLineLength=50,maxLineGap=400)


    try:
        Smosbat = []
        Smanfi = []
        for line in Lines:
            x1,y1,x2,y2= line[0]
            shib,Arz = np.polyfit((x1,x2),(y1,y2),1)
            if shib > 0:
                Smosbat.append([shib,Arz])
            elif shib <0:
                Smanfi.append([shib,Arz])
            else:
                pass
            #cv.line(frame2,(x1,y1),(x2,y2),(0,255,0),3)

        Khatrast = np.average(Smosbat,axis=0)
        Xr1,Yr1,Xr2,Yr2 = mokhtasat(Khatrast,0,yframe)
        cv.line(frame2,(Xr1,Yr1),(Xr2,Yr2),(0,0,255),3)

        Khatchap = np.average(Smanfi,axis=0)
        Xl1,Yl1,Xl2,Yl2 = mokhtasat(Khatchap,0,yframe)
        cv.line(frame2,(Xl1,Yl1),(Xl2,Yl2),(255,0,0),3)

        X1 = int((Xr1+Xl1)/2)
        X2 = int((Xr2+Xl2)/2)
        Y1 = int((Yr1+Yl1)/2)
        Y2 = int((Yr2+Yl2)/2)

        cv.line(frame2,(X1,Y1),(X2,Y2),(0,255,0),3)
        
    except:
        pass


    cv.imshow("Frame",frame2)
    #cv.imshow("Canny",CannyROI)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break