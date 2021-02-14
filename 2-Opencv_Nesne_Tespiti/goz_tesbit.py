
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../Photos/8.jpg",0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# sınıflandırıcı
eye_cascade = cv.CascadeClassifier("../Xml/haarcascade_eye.xml")
eye_rect = eye_cascade.detectMultiScale(img)

for (x,y,w,h) in eye_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
    cv.putText(img, "goz",(x,y-5),cv.FONT_HERSHEY_SIMPLEX, 0.30,(0,255,255),1)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")


plt.show()
