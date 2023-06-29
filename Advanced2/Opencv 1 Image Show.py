import cv2 as cv #import kardan ketabkhane opencv

cv.namedWindow("window",cv.WINDOW_FULLSCREEN) #Sakht ye panjere be name window wa tanzim no e on

image_addr = "Hello.jpg"   #adrese aks mord nazar
image = cv.imread(image_addr) #aks ro be onvan ye list baz kardim

cv.imshow("window",image) #namayesh aks dakhele panjere ee be name window 
cv.waitKey(0) #window ra baz negah midrd ta vaghti kod estop shavad