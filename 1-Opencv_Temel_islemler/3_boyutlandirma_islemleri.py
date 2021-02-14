import cv2 as cv
import numpy as np

## resim okutma
img = cv.imread('../Photos/lady.jpg') ## Dosya seçme
print(img.shape) # resmin boyutu

# Resmi boyutlandırma
imgResize = cv.resize(img,(700,700))
print(imgResize.shape)

# Kırpma işlemleri
imgCropped = imgResize[0:700,500:700]
imgCropped2 = imgResize[0:700,310:500]
imgCropped3 = imgResize[0:400,0:310]
imgCropped4 = imgResize[400:700,0:310]


cv.imshow('GRAY IMAGE',img) 
cv.imshow('GRAY IMAGE RESIZE',imgResize) 
cv.imshow('GRAY IMAGE CROPPED',imgCropped) 
cv.imshow('GRAY IMAGE CROPPED2',imgCropped2) 
cv.imshow('GRAY IMAGE CROPPED3',imgCropped3) 
cv.imshow('GRAY IMAGE CROPPED4',imgCropped4) 

cv.waitKey(0)