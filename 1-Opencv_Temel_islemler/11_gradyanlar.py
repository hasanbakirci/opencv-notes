# Gradyanlar : görüntüdeki yoğunluk veya renkteki yönlü bir değişiktir Kenar algılamada kullanılır
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Photos/sudoku.jpg',0)
plt.figure(), plt.imshow(img, cmap="gray") , plt.axis("off"), plt.title("Orjinal Img")

# x gradyan
sobelx = cv.Sobel(img,ddepth = cv.CV_16S, dx = 1, dy = 0, ksize=5)
plt.figure(), plt.imshow(sobelx, cmap="gray") , plt.axis("off"), plt.title("Sobel X Img")

# y gradyan
sobely = cv.Sobel(img,ddepth = cv.CV_16S, dx = 0, dy = 1, ksize=5)
plt.figure(), plt.imshow(sobely, cmap="gray") , plt.axis("off"), plt.title("Sobel Y Img")

# laplacian gradyan
laplacian = cv.Laplacian(img, ddepth= cv.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap="gray") , plt.axis("off"), plt.title("Laplacian Img")

plt.show()