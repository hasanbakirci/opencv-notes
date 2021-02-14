import cv2 as cv
import numpy as np


img = cv.imread('../Photos/cats.jpg') ## Dosya seçme
imgHor = np.hstack((img,img)) # yatayda birleştir
imgVer = np.vstack((img,img)) # dikeyde birleştir
cv.imshow("Horizontal", imgHor)
cv.imshow("Vertical", imgVer)

cv.waitKey(0)