import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow('TRACKING')
cv2.createTrackbar('LH', 'TRACKING', 0, 255, nothing)
cv2.createTrackbar('LS', 'TRACKING', 0, 255, nothing)
cv2.createTrackbar('LV', 'TRACKING', 0, 255, nothing)
cv2.createTrackbar('UH', 'TRACKING', 255, 255, nothing)
cv2.createTrackbar('US', 'TRACKING', 255, 255, nothing)
cv2.createTrackbar('UV', 'TRACKING', 255, 255, nothing)

while True:
    frame = cv2.imread('smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'TRACKING')
    l_s = cv2.getTrackbarPos('LS', 'TRACKING')
    l_v = cv2.getTrackbarPos('LV', 'TRACKING')

    u_h = cv2.getTrackbarPos('UH', 'TRACKING')
    u_s = cv2.getTrackbarPos('US', 'TRACKING')
    u_v = cv2.getTrackbarPos('UV', 'TRACKING')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('FRAME', frame)
    cv2.imshow('MASK', mask)
    cv2.imshow('RESULT', res)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows
