# Kontur algılama : aynı renk veya yoğunluğa sahip tüm kesintisiz noktaları (sınırla birlikte) birleştirmeyi amaçlayan yöntemdir.
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../Photos/shapes.jpg")
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")


contours ,hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):
    #external
    if hierarch[0][i][3] == -1:
        cv.drawContours(external_contour, i, 255, -1) # son parametre kalınlık ama -1 yazınca alanı dolduruyor
    else:
        cv.drawContours(internal_contour,conturs,i,255,-1)
plt.figure(), plt.imshow(external_contour, cmap="gray"), plt.axis("off")
plt.figure(), plt.imshow(internal_contour, cmap="gray"), plt.axis("off")

plt.show()
