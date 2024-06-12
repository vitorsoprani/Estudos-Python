import cv2
import numpy as np


def nothing(x):
    print(x)


# cria uma imgame preta de 521x300
img = np.zeros((300, 512, 3), np.uint8)
# cria uma janela com o nome 'img'
cv2.namedWindow('img')

cv2.createTrackbar('B', 'img', 0, 255, nothing)
cv2.createTrackbar('G', 'img', 0, 255, nothing)
cv2.createTrackbar('R', 'img', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'img', 0, 1, nothing)

while (True):
    cv2.imshow('img', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    b = cv2.getTrackbarPos('B', 'img')
    g = cv2.getTrackbarPos('G', 'img')
    r = cv2.getTrackbarPos('R', 'img')
    s = cv2.getTrackbarPos(switch, 'img')

    if not s:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
