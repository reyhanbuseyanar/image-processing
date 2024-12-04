import cv2
import numpy as np

resim=cv2.imread("ozan2.jpeg")
#pyrUp büyütmek iki kat yapmak genişliğinden 2 kat boyutundan 2 kat
ikikat=cv2.pyrUp(resim)

ikikatküçük=cv2.pyrDown(resim)

print("orjinal rsim",resim.shape)
print("iki kat resim",ikikat.shape)
print("iki kat küçük",ikikatküçük.shape)

cv2.imshow("orjinal",resim)
cv2.imshow("iki kat büyütülmüş",ikikat)
cv2.imshow("iki kat küçük",ikikatküçük)


cv2.waitKey(0)
cv2.destroyAllWindows()