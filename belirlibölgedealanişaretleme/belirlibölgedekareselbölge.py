import cv2
import numpy as np

resim=cv2.imread("habamam.jpeg")
#effect oluşturma [y,x]
#resim[50:100,230:310,0]=255
#resim[y,x,renkkodu]=pigmenti 
#print(resim[50,50]) #bölgedeki pigmenti verir

cv2.rectangle(resim,(50,100),(150,30),[0,0,225],3)
#cv2.rectangle(resim,(x in aralığ),(y nin aralığı),[blue,green,red]renk pigmenti],kaşınlık 0 dan 10 kadae değerle)

cv2.imshow("habamam",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()