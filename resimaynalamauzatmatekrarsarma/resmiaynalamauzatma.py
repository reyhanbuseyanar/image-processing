import cv2
import numpy as np

resim= cv2.imread("adile.jpeg")

#sınır çerçeveleme copymake border
aynalamaresim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
#cv2.border_reflect sınırları,kenarlıkları tekrarla aynalanan resme özel durum
uzatmaresim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
#cv2.BORDER_REPLICATE tekrarlama
tekrarresim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
#cv2.BORDER_WRAP paketleme üste alta sağa sola paketler
çerçeveresim=cv2.copyMakeBorder(resim,20,20,20,20,cv2.BORDER_CONSTANT,value=(70,100,255))
#cv2.BORDER_CONSTANT çerçeve oluşturur value renk belirlenir orjinal siyahtır

cv2.imshow("aynalanan adile fotoğraf",aynalamaresim)#aynalanan resmi göstermek için
cv2.imshow("uzatma adile resim",uzatmaresim)
cv2.imshow("tekrarlanan adile",tekrarresim)
cv2.imshow("çerçeveli resim",çerçeveresim)

cv2.waitKey(0)
cv2.destroyAllWindows()