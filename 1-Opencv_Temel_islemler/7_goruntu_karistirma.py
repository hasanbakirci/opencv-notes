import cv2 as cv
import matplotlib.pyplot as plt

# OpenCV de resimler BGR plt ile çizince resimde farklılık oluyor cv.COLOR_BGR2RGB kullanıp RGB ye çevirecez
img1 = cv.imread('../Photos/img1.jpg')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

img2 = cv.imread('../Photos/img2.jpg')
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

# Birleştirme icin iki resmin boyutuda aynı olmalı
print(img1.shape)
print(img2.shape)
img1 = cv.resize(img1,(600,600))
img2 = cv.resize(img2,(600,600))
print("Sonra ",img1.shape)
print("Sonra ",img2.shape)


# Karıstırılmıs resim = alpha * img1 + beta * img2
blended = cv.addWeighted(src1 = img1,alpha=0.5, src2 = img2,beta = 0.5 , gamma = 0)
plt.figure()
plt.imshow(blended)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

plt.show()