import cv2
import numpy as np

resim=cv2.imread("efekt.jpg")


#resim[:,:,0]=255 blue =0  boşluk olması bütün resme effet uygulanmasını sağlar
#resim[:,:,1]=255 green=1
#resim[:,:,2]=255 red=2
#turuncu
#resim[:,:,1]=150
#resim[:,:,2]=255
#mor
#resim[:,:,1]=200
#resim[:,:,1]=80
#resim[:,:,2]=150

#göz effect
resim[150:220,350:600,0]=255
resim[150:220,350:600,1]=200
cv2.imshow("kemal sunal ", resim)



cv2.waitKey(0)
cv2.destroyAllWindows()