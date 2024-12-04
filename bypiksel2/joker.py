import cv2
import numpy as np
resim= cv2.imread("joker.jpg")

resim[50,30]=[225,225,225] #piksel beyaz

for i in range(200): #çizgi halinde beyaz çizgi
    resim[10,i]=[225,225,225]


cv2.imshow("joker",resim)

print(resim.size)
print(resim.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()