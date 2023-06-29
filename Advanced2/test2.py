import cv2 as cv

cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_smile.xml')

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    target = cascade.detectMultiScale(gray,1.2,4)
    for (x,y,w,h) in target:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        cv.rectangle(frame, (x+w,y+h), (x,y+h+35), (255, 255, 0), cv.FILLED)
        cv.putText(frame, 'target', (x,y+h+28), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    cv.imshow("frame",frame)
    key = cv.waitKey(1)
    if ord("q") == key:
        break

print('Option 1: Face #1 frontalface_alt')
print('Option 2: Face #2 frontalface_alt2')
print('Option 3: Face #3 frontalface_alt_tree')
print('Option 4: Face #4 frontalface_default')
print('Option 5: Face #5 profileface')
print('Option 6: Eye #1 eye_tree_eyeglasses')
print('Option 7: Eye #2 eye')
print('Option 10: Cat face #1 frontalcatface_extended')
print('Option 11: Cat face #2 frontalcatface')
print('Option 12: Body #1 fullbody')
    