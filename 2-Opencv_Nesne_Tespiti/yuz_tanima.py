import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../Photos/barisKel.png",0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# sınıflandırıcı
face_cascade = cv.CascadeClassifier("../Xml/haarcascade_frontalface_default.xml")
face_rect = face_cascade.detectMultiScale(img)

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,255,255),10)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# img2 = cv.imread("../Photos/group 2.jpg",0)
# plt.figure(), plt.imshow(img2, cmap="gray"), plt.axis("off")

# # sınıflandırıcı
# face_cascade = cv.CascadeClassifier("../Xml/haarcascade_frontalface_default.xml")
# face_rect = face_cascade.detectMultiScale(img2, minNeighbors=5)

# for (x,y,w,h) in face_rect:
#     cv.rectangle(img2,(x,y),(x+w,y+h),(255,255,255),10)
# plt.figure(), plt.imshow(img2, cmap="gray"), plt.axis("off")



#video
# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     if ret:
#         face_rect = face_cascade.detectMultiScale(img2)
#         for (x,y,w,h) in face_rect:
#             cv.rectangle(img,(x,y),(x+w,y+h),(255,150,150),10) 
#         cv.imshow("Face detect", frame)
#     if cv.waitKey(1) & 0xFF == ord("q"):break
    
# cap.release()
# cv.destroyAllWindows()

plt.show()