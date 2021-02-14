# opencv kütüphanesini içe aktaralım
# ...
import cv2 as cv

# matplotlib kütüphanesini içe aktaralım
# ...
import matplotlib.pyplot as plt
# resmi siyah beyaz olarak içe aktaralım
# ...
img = cv.imread('../Photos/cat.jpg',0)
# resmi çizdirelim
# ...
cv.imshow('CAT',img)

# resmin boyutuna bakalım
# ...
print(img.shape)
# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
# ...
# ...
imgR = cv.resize(img,(int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
cv.imshow('CAT Boyutlu',imgR)
cv.waitKey(0)
# orijinal resme bir yazı ekleyelim mesela "kedi" ve resmi çizdirelim
# ...
# ...
cv.putText(img,"CAT",(200,150),cv.FONT_HERSHEY_COMPLEX,0.9,(25,100,100),3)
cv.imshow('CAT',img)
cv.waitKey(0)
# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
# ...
# ...
_, thresh_img = cv.threshold(img, thresh = 50, maxval = 255, type = cv.THRESH_BINARY)
cv.imshow('CAT thresh', thresh_img)
cv.waitKey(0)
# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
# ...
# ...
gb = cv.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"),plt.title("Gauss Blur")

# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
# ...
# ...
laplacian = cv.Laplacian(img, ddepth= cv.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap="gray") , plt.axis("off"), plt.title("Laplacian Img")
# orijinal resmin histogramını çizdirelim
# ...
# ...
img_vis = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_hist = cv.calcHist([img], channels = [0],mask= None, histSize= [256], ranges=[0,256])
plt.figure(), plt.plot(img_hist)



plt.show()















