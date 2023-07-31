import cv2   #Gerekli kütüphaneler import edilir.
import matplotlib.pyplot as plt
import numpy as np

# resmi siyah-beyaz olarak içe aktar ve görselleştir.
img = cv2.imread("contour.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

# cv2.findContours() fonksiyonu ile konturlar tespit edilir. ilk parametre olarak görüntüyü alır
# ikinci parametre, hem iç hemde dış konturları bulmayı sağlar ve konturların hiyerarşik yapısını döndürür.
# üçüncü parametre, yatay dikey ve çapraz bölümleri sıkıştırmamızı sağlıyor ve yalnızca uç noktaları bırakıyor. 
contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# sıfırlardan oluşan bu diziler iç ve dış konturları temsil etmek için kullanılır.
external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):
    
    # konturun hiyerarşik yapısını kontrol eder eğer değer -1 ise kontur externaldir.
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contour,contours, i, 255, -1)   # ve beyaz renkli kontur doldurulur
    else: # external değilse internaldir ve beyaz renkle doldurulur
        cv2.drawContours(internal_contour,contours, i, 255, -1)

# ve ayrı ayrı görselleştirmesi yapılır.
plt.figure(), plt.imshow(external_contour, cmap = "gray"),plt.axis("off")
plt.figure(), plt.imshow(internal_contour, cmap = "gray"),plt.axis("off")
