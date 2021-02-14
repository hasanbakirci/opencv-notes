import cv2 as cv
import numpy as np
from collections import deque

buffer_size = 16
pts = deque(maxlen= buffer_size)

# mavi renk aralıgı
#paint programında renkleri düzenle bölümünden renk tonlarını seçiyoruz
blueLower = (84,98,0)
blueUpper = (179,255,255)
# capture
cap = cv.VideoCapture(1)
cap.set(3,690)
cap.set(4,480)
while True:
    success, imgOriginal = cap.read()
    if success:
        #normal
        cv.imshow("Orjinal",imgOriginal)
        #blur
        blured = cv.GaussianBlur(imgOriginal, (11,11),0)
        #hsv
        hsv = cv.cvtColor(blured, cv.COLOR_BGR2HSV)
        cv.imshow("HSV",hsv)
        # mavi için maske olusturalım
        mask = cv.inRange(hsv,blueLower,blueUpper)
        cv.imshow("mask Image",mask)
        # maskenin etrafında kalan gürültüleri sil
        mask = cv.erode(mask, None,iterations=2)
        mask = cv.dilate(mask, None,iterations=2)
        cv.imshow("Mask + Erozyon + Genisleme",mask)
        # kontur
        contours ,hierarchy = cv.findContours(mask.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        center = None
        if len(contours) > 0:
            # en buyuk konturu al
            c = max(contours, key = cv.contourArea)
            # dikdörtgene çevir
            rect = cv.minAreaRect(c)
            ((x,y),(width,height),rotation) = rect
            s = "x: {}, y:{}, width: {} , height: {}, rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)
            #kutucuk
            box = cv.boxPoints(rect)
            box = np.int64(box)
            #moment görüntünün merkezini bulmaya yarar
            M = cv.moments(c)
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            # konturu çizdirelim
            cv.drawContours(imgOriginal, [box], 0,(0,255,255),2)
            # merkeze bir tane nokta çizelim
            cv.circle(imgOriginal,center,5,(255,0,255),-1)
            #bilgileri yazalim
            cv.putText(imgOriginal,s,(50,50),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
            
        # deque  nesnenin hareketine göre arkada cizgi çizer
        pts.appendleft(center)
        for i in range(1, len(pts)):
            if pts[i-1] is None or pts[i] is None: continue
            cv.line(imgOriginal,pts[i-1],pts[i],(0,255,0),3)
        cv.imshow("Orjinal Tespit", imgOriginal)



    if cv.waitKey(1) & 0xFF == ord("q"): break