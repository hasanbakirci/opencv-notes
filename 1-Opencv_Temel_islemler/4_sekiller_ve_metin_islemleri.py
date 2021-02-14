import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8) # siyah bir resim
# print(img)
# img[:200] = 255,0,0 # bölgenin rengini değiştirir mavi,yeşil,kırmızı

# cv.line(img,(0,0),(300,300),(0,255,0),1) # çizgi çizer:  resim , başlangıç , bitiş , renk(BlueGreenRed) , kalınlık

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1) # resim mesela 400,400 ise oraya kadar çizer
#cv.line(img,(50,50),(100,200),(0,0,200),1) # 

cv.rectangle(img,(0,0),(250,350),(0,0,255),2) # kare

# cv.rectangle(img,(0,0),(250,350),(0,0,255),cv.FILLED) # kare içi dolu

#cv.circle(img,(400,50),30,(255,255,0),5) # çember
cv.circle(img,(400,50),30,(255,255,0),cv.FILLED) # daire

   # resim , yazı , konumu , font , buyukluk , renk , kalınlık
cv.putText(img,"Open CV Deneme",(200,150),cv.FONT_HERSHEY_COMPLEX,0.9,(25,100,100),3) # yazı ekler

cv.imshow("Image",img)
cv.waitKey(0)