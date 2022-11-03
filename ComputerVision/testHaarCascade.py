import numpy as np
import cv2

cat_cascade = cv2.CascadeClassifier('haarcascade_default.xml')

img = cv2.imread('default.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cat_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
