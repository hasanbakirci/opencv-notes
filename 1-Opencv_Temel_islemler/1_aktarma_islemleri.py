import cv2 as cv
import time

## resim okutma
img = cv.imread('../Photos/cats.jpg',0) ## Dosya seçme / ,0 siyah beyaz yapar.
print(img)
cv.imshow('FOTO',img) 

cv.waitKey(0) ## devam etmek için tuş basılma bekler


# Harici veya dahili kamera açma

# capture = cv.VideoCapture(0) # 0 kamera 1 harici kamera
# capture.set(3,640)
# capture.set(4,420)


## video okutma
capture = cv.VideoCapture('../Videos/dog.mp4')  ## Dosya seçme
print("Video genişlik: ",capture.get(3))
print("Video yükseklik: ",capture.get(4))

if capture.isOpened() == False:
    print("Video açılamadı!")

while True:
    isTrue, frame = capture.read()
    # time.sleep(0.1) # video yavaşlatma 
    cv.imshow('Video',frame)
    if cv.waitKey(1) & 0xFF==ord('q'): ## q ile kapatır
        break
capture.release() # video yakalamayı bırak
cv.destroyAllWindows() ## kodlar bitince kapatır



# Kameradan video kaydetme
capture = cv.VideoCapture(0)
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
print(width, height)
# Video kaydet

writer = cv.VideoWriter("video_ismi.mp4",cv.VideoWriter_fourcc(*"DIVX"),20,(width,height))
# fourcc --> windows için çerçeveleri sıkıştırma
while True:
    ret,frame = capture.read()
    cv.imshow("Video",frame)

    #save
    writer.write(frame)
    if cv.waitKey(1) & 0xFF == ord("q"): break
capture.release()
writer.release()
cv.destroyAllWindows()

