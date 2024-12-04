import cv2
import numpy as np


kurtresmi=cv2.imread("kurt.jpg")

cv2.imshow("kurt resmi",kurtresmi)

print(kurtresmi[(100,80)]) # (100,80) renk piksel kodu print(kurtresmi[(230,80)])
print("size"+str(kurtresmi.size))
print("shape"+str(kurtresmi.shape))
print("type"+str(kurtresmi.dtype))


cv2.waitKey(0)
cv2.destroyMacos()
