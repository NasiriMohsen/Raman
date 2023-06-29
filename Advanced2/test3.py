import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    frame2 = np.copy(frame)

    Canny = cv.Canny(frame,200,900)

    Lines = cv.HoughLinesP(Canny,1,np.pi/180,100,np.array([]),minLineLength=150,maxLineGap=500)


    try:
        lines = []
        for line in Lines:
            x1,y1,x2,y2= line[0]
            lines.append([x1,y1,x2,y2])
            cv.line(frame2,(x1,y1),(x2,y2),(0,255,255),3)
        
        X1a,Y1a,X2a,Y2a = np.average(lines,axis=0)
        cv.line(frame2,(int(X1a),int(Y1a)),(int(X2a),int(Y2a)),(0,0,255),3)





    except:
        pass


    cv.imshow("Frame",Canny)
    cv.imshow("Canny",frame2)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break