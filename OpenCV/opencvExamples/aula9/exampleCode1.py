import numpy as np
import cv2

# gambiara pra ver todoso os eventos na livraria
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        coloredImg = np.zeros([512, 512, 3], np.uint8)
        coloredImg[:] = [blue, green, red]
        print(str(blue), str(green), str(red))

        cv2.imshow("color", coloredImg)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

points = []
# executa a função quando clica no mouse
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
