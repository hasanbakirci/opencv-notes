# Erozyon : ön plandaki nesnenin sınırlarını aşındırır
# Genişleme : görüntüdeki beyaz bölgeyi arttırır (erozyon tersi)
# Açma :  erozyon + genişlemedir, gürültünün arındırılmasında etkilidir
# Kapatma : genişleme + erozyon , ön plandaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için
# Morfolojik gradyan : Bir görüntünün genişlemesi ve erozyonu arasındaki farktır

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Photos/yazi.png',0) # gürültü ile birleştirince hata vermemesi için 0 yazarak siyah  beyaz yaptık
plt.figure(), plt.imshow(img, cmap="gray") , plt.axis("off"), plt.title("Orjinal Img")

#erozyon
kernel = np.ones((5,5), dtype= np.uint8)
result = cv.erode(img, kernel, iterations= 1) # iterasyona göre oranı bi noktadan sonra bütün yazı yok olur
plt.figure(), plt.imshow(result, cmap="gray") , plt.axis("off"), plt.title("Erozyon Img")
#genişleme
result2 = cv.dilate(img, kernel , iterations=1)
plt.figure(), plt.imshow(result2, cmap="gray") , plt.axis("off"), plt.title("Genisleme Img")
                    #white noise  beyaz gürültü ekliyelim
whiteNoise = np.random.randint(0,2,size = img.shape[:2]) # 0-2 arasında sayılar olusturuyoruz
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap="gray") , plt.axis("off"), plt.title("Gürültü beyaz")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap="gray") , plt.axis("off"), plt.title("Gürültülü Img beyaz")
#Açma
opening = cv.morphologyEx(noise_img.astype(np.float32), cv.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap="gray") , plt.axis("off"), plt.title("Açma Img")


                    #black noise  beyaz gürültü ekliyelim
blackNoise = np.random.randint(0,2,size = img.shape[:2]) # 0-2 arasında sayılar olusturuyoruz
blackNoise = whiteNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap="gray") , plt.axis("off"), plt.title("Gürültü siyah")

noise_img2 = blackNoise + img
noise_img2[noise_img2 <= -245] = 0
plt.figure(), plt.imshow(noise_img2, cmap="gray") , plt.axis("off"), plt.title("Gürültülü Img siyah")

#Kapatma
closing =  cv.morphologyEx(noise_img.astype(np.float32), cv.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap="gray") , plt.axis("off"), plt.title("Kapatma")


#Gradient
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap="gray") , plt.axis("off"), plt.title("Gradient")




plt.show()