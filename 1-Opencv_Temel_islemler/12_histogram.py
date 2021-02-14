# Histogram: Görüntü histogramı, dijital görüntüdeki ton dağılımının grafiksel olarak işlev gören bir histogram türüdür.
# Herbir ton değeri için piksel sayısını içerir
# Belirli bir görüntü için histograma bakılarak, ton dağılımı anlaşılabilir.
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Photos/red_blue.jpg')
img_vis = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis)
print(img.shape)

img_hist = cv.calcHist([img], channels = [0],mask= None, histSize= [256], ranges=[0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist)

#renklerin dağılımlarını grafikte gösteriyoruz
color = ["b","g","r"]
plt.figure()
for i, c in enumerate(color):
    hist = cv.calcHist([img], channels = [i],mask= None, histSize= [256], ranges=[0,256])
    plt.plot(hist,color = c)


#
golden_gate = cv.imread("../Photos/goldenGate.jpg")
golden_gate_vis = cv.cvtColor(golden_gate, cv.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate_vis)
print(golden_gate.shape)

# siyah renkte maske olusturuyoruz
mask = np.zeros(golden_gate.shape[:2],np.uint8)
plt.figure(), plt.imshow(mask, cmap="gray")
# resim üzerinde bir alan belirleyip, o alan hariç siyah olacak
mask[1500:2000,1000:2000]= 255
plt.figure(), plt.imshow(mask, cmap="gray")
masked_img_vis = cv.bitwise_and(golden_gate_vis,golden_gate_vis, mask=mask)
plt.figure(), plt.imshow(masked_img_vis, cmap="gray")

# histogram eşitleme
# karşıtlık arttırma
img = cv.imread("../Photos/hist_equ.jpg",0)
plt.figure(), plt.imshow(img, cmap="gray")
img_hist = cv.calcHist([img], channels = [0],mask= None, histSize= [256], ranges=[0,256])
plt.figure(), plt.plot(img_hist)

eq_hist = cv.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap="gray")
plt.show()