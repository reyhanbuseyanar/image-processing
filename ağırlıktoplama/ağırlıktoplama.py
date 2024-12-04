import cv2
import numpy as np

resim1=cv2.imread("ozan1.jpeg")
resim2=cv2.imread("ozan2.jpeg")


cv2.imshow("ozan1",resim1)#resim boyutları aynı olmalı
cv2.imshow("ozan2",resim2)

toplamı=cv2.add(resim1,resim2)
ağırlıklıtoplama=cv2.addWeighted(resim1,0.7,resim2,0.3,0) # resim1 %70 resin2%30toplamı 1 olmalı

cv2.imshow("toplanmış resim",toplamı)
cv2.imshow("ağırlıklı toplam",ağırlıklıtoplama)

cv2.waitKey(0)
cv2.destroyAllWindows()