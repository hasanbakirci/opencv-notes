import cv2 as cv
import numpy as np

img = cv.imread("../Photos/kart.png")


width = 400
height = 500

# açılı resimi düz hale getirecez
# paint ile resmi açıp kartın köşelerinin kordinatını bulduk
pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
# olması gereken resim kordinatları
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matris = cv.getPerspectiveTransform(pts1,pts2)
print(matris)
imgOutput = cv.warpPerspective(img,matris,(width,height))

cv.imshow("Orjinal",img)
cv.imshow("Donusturulmus",imgOutput)
cv.waitKey(0)