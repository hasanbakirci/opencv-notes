import cv2 as cv
import numpy as np

## resim okutma
img = cv.imread('../Photos/cat.jpg') ## Dosya seçme
kernel = np.ones((5,5),np.uint8)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) ## griye çevirme
imgBlur = cv.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv.Canny(img,250,250)
imgDilation = cv.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv.erode(imgDilation,kernel,iterations=1)

cv.imshow('GRAY IMAGE',imgGray) 
cv.imshow('BLUR IMAGE',imgGray) 
cv.imshow('CANNY IMAGE',imgCanny) 
cv.imshow('DILATION IMAGE',imgDilation)  
cv.imshow('ERPDED IMAGE',imgEroded)  

cv.waitKey(0)