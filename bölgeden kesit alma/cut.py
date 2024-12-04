import cv2
import numpy as np

resimchıldren= cv2.imread("chıldren.jpeg")

cutresim=resimchıldren[30:200,200:400] #kesinilecek alan

resimchıldren[0:170,0:200]=cutresim #resmi yapıştırma

#resimchıldren[ :,:,0]=255 #effect
resimchıldren[400:450,300:350]=(0,150,225) #bir alanın rengini değiştirme

resimchıldren[0:170,0:200,0]=200# kesitin rengini değiştirme

#cv2.imshow("cut",cutresim)# kesiti gösterme
cv2.imshow("23 april",resimchıldren)


cv2.waitKey(0)
cv2.destroyAllWindows()
