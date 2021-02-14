import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#uyarıları kapatıyoruz hata ile karışmasın diye
import warnings
warnings.filterwarnings("ignore")

#blurring   detayı azaltır, gürültüyü engeller

img = cv.imread('../Photos/park.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img), plt.axis("off"), plt.title("orjinal")

####   Ortalama Bulanıklastırma Yontemı
dst2 = cv.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Ortalama Blur")
#######################################

#### Gaussian blur
gb = cv.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"),plt.title("Gauss Blur")
#######################################

#### Medyan blur
mb = cv.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Medyan Blur")
#######################################


def gaussinNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy

# Gürültü eklemek için 0-255 arasında olan değerleri 0-1 arasına çevirmeliyiz

img = cv.imread('../Photos/park.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)/255  # 0-1 arası için
plt.figure()
plt.imshow(img), plt.axis("off"), plt.title("orjinal 0-1 arası")

gaussinNoiseImage = gaussinNoise(img)
plt.figure(),plt.imshow(gaussinNoiseImage), plt.axis("off"), plt.title("gaussinNoise")

# gauss blur
gb2 = cv.GaussianBlur(gaussinNoiseImage, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("with Gauss Blur")

def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5 # resimdeki siyah beyaz noktacıkların oranı %50
    amount = 0.004
    noisy = np.copy(image)
    # salt   beyaz nokta eklemek
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    # pepper siyah nokta eklemek
    num_salt = np.ceil(amount * image.size * (1 - s_vs_p)) # s_vs_p değerini 1 e tamamlamak için
    coords = [np.random.randint(0, i - 1,int(num_salt)) for i in image.shape]
    noisy[coords] = 0

    return noisy

spImage = saltPepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP Image")

mb2 = cv.medianBlur(spImage.astype(np.float32), ksize = 3) # resmin float32 olması lazim
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with Median Blur")

plt.show()