import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Photos/img1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # gri çevirme

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#eşikleme
#_, thresh_img = cv.threshold(img, thresh = 60, maxval = 255, type = cv.THRESH_BINARY) # 60 -255 arası 0 yapcak yani beyaz
_, thresh_img = cv.threshold(img, thresh = 60, maxval = 255, type = cv.THRESH_BINARY_INV) # 60 - 255 arası 255 yapcak yani siyah

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# uyarlamalı eşik değeri

# cv.ADAPTIVE_THRESH_MEAN_C ---> kullanılan yöntem   11 --> pixel toplulugu
thresh_img2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()