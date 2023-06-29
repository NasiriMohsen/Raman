import cv2 as cv #import kardan ketabkhane opencv

image_addr = "Hello.jpg"
image = cv.imread(image_addr) 

image_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) #Tabdil range aks

cv.imshow("window",image)
cv.imshow("window2",image_gray) 
cv.waitKey(0) 