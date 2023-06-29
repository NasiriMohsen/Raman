import cv2 as cv
import numpy as np

def Nthing(x):
    pass

cv.namedWindow("Canny")
cv.namedWindow("frame2")

webcam = cv.VideoCapture(0)

cv.createTrackbar("Cmin","Canny",0,500,Nthing)
cv.createTrackbar("Cmax","Canny",0,5000,Nthing)
cv.createTrackbar("gap","frame2",0,500,Nthing)
cv.createTrackbar("length","frame2",0,500,Nthing)
cv.setTrackbarPos("Cmax","Canny",5000)


while True:
    _,frame = webcam.read()
    frame2 = np.copy(frame)

    Cmin = 200#cv.getTrackbarPos("Cmin","Canny")
    Cmax = 900#cv.getTrackbarPos("Cmax","Canny")
    gap = cv.getTrackbarPos("gap","frame2")
    length = cv.getTrackbarPos("length","frame2")
    Canny = cv.Canny(frame,Cmin,Cmax)


    Lines = cv.HoughLinesP(Canny,1,np.pi/180,100,np.array([]),minLineLength=length,maxLineGap=gap)

    try:
        for line in Lines:
            x1,y1,x2,y2= line[0]
            cv.line(frame2,(x1,y1),(x2,y2),(0,255,255),3)
    except:
        pass

    cv.imshow("Frame",frame)
    cv.imshow("frame2",frame2)
    cv.imshow("Canny",Canny)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break