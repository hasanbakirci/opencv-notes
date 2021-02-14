# Kenar Algılama: götünrü parlaklığının keskin bir şekilde değiştiği noktaları tanımlamayı amaçlayan bir yöntemdir.
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Photos/london.jpg',0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

edges = cv.Canny(image = img, threshold1 = 0, threshold2 = 255)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")
# threshold ayarlaması ile daha iyi bi secim yapalım

med_val = np.median(img)
print(med_val)

low = int(max(0,(1 - 0.33)*med_val))
high = int(min(255,(1 + 0.33)*med_val))
print("low: ",low ,"high ", high)
edges = cv.Canny(image = img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

#Tüm resme blur uygulayıp suyu yok etmeyi deniyelim
blurred_img = cv.blur(img, ksize=(3,3)) # ksize artarsa daha az nesne görünür
plt.figure(), plt.imshow(blurred_img, cmap="gray"), plt.axis("off")
med_val = np.median(blurred_img)
low = int(max(0,(1 - 0.33)*med_val))
high = int(min(255,(1 + 0.33)*med_val))
print("blur low: ",low ,"blur high ", high)
edges = cv.Canny(image = blurred_img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")


plt.show()