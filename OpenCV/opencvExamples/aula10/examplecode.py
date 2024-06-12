import numpy as np
import cv2

img = cv2.imread('leuvenB.jpg')
img2 = cv2.imread('opencv-logo.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img.shape)  # imprime uma tupla com o numero de colunas, linhas e camadas
print(img.size)  # imprime o numero total de pixels
print(img.dtype)  # datatype

b, g, r = cv2.split(img)  # separa os canais da imagem
img = cv2.merge((b, g, r))

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .3, img2, .7, 0)
cv2.imshow('image', dst)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
