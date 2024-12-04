import cv2
import numpy as np

# İlk resmi yükle ,#0 siyah yapar renk olmadı için kanal sayısı 1
resim1 = cv2.imread("Görüntü.jpg")
# İkinci resmi yükle
resim2 = cv2.imread("resim.jpg")

# Resmi göster
#imwrite("newresim,resim1") resim1() 0 olursa resmi siyah yapar) adını newresim yapar
cv2.imshow("kuş", resim1)

# Matris hali
print(resim1)
print("..........")
# Matris boyutu
print(resim1.size)
print("..........")
# Veri tipi
print(resim1.dtype)
print("..........")
# Matrisin şekli (m*n)
print(resim1.shape)

# Klavyeden bir tuşa basılana kadar bekle
cv2.waitKey(0)
# Tüm pencereleri kapat
cv2.destroyAllWindows()
