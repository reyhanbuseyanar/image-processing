import cv2
import numpy as np

resim=cv2.imread("ozan1.jpeg",0)#2 paremetriye 0 diyince gri olur
#cvtColor resmi dönüştürek  cv2.COLOR_BG2GRAY resim değişkenini al  gray haline dönüştürüp resmi ata
#resimgri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)#Kanal sayısını 3 dem 1 düşürür siyah beyaz oluşumu 

#yükseklik,genişlik,kanalsayısı=resim.shape # shape değişkenini yükseklik,genişlik,kanalsayısı
#print("orjinal",yükseklik,genişlik,kanalsayısı)

#yükseklik,genişlik,kanalsayısı=resimgri.shape# yükseklik,genişlik,kanalsayısı kanalsayı 1 kanal sayısını tutmaz hata verir o yüzden
#print("gri resim",yükseklik,genişlik,kanalsayısı)

#cv2.imshow("orjinal",resim)
#cv2.imshow("grirsim",resimgri)

cv2.imshow("gri resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

