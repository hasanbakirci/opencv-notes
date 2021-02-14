# Köşe Algılama
# Şuan bulununan konum ile bir sonraki konumdaki yoğunluk farkı fazlaysa orası kösedir.
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('../Photos/sudoku.jpg',0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# harris correr detection
dst = cv.cornerHarris(img, blockSize=2, ksize= 3, k= 0.04) # blokSize bakılacak komşu
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")


# genisletme yöntemi kullanalım
dst = cv.dilate(dst, None)
img[dst>0.2*dst.max()]= 1
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")


# shi tomasi detection
img = cv.imread('../Photos/sudoku.jpg',0)
img = np.float32(img)
corners = cv.goodFeaturesToTrack(img,120,0.01,10) #120 kose bulmaya calıscak
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img, (x,y),3,(124,125,125),cv.FILLED)
plt.imshow(img), plt.axis("off")


plt.show()
