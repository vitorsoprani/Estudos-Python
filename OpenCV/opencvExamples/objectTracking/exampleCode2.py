import cv2
import numpy as np
# print(cv2.__version__)


def onTrack1(value):
    global hueLow
    hueLow = value


def onTrack2(value):
    global hueHigh
    hueHigh = value


def onTrack7(value):
    global hueLow2
    hueLow2 = value


def onTrack8(value):
    global hueHigh2
    hueHigh2 = value


def onTrack3(value):
    global satLow
    satLow = value


def onTrack4(value):
    global satHigh
    satHigh = value


def onTrack5(value):
    global valLow
    valLow = value


def onTrack6(value):
    global valHigh
    valHigh = value


cam = cv2.VideoCapture(0)

cv2.namedWindow("Mask Settings")
cv2.moveWindow("Mask Settings", 720, 0)

cv2.createTrackbar("HL", "Mask Settings", 0, 179, onTrack1)
cv2.createTrackbar("HH", "Mask Settings", 179, 179, onTrack2)
cv2.createTrackbar("HL2", "Mask Settings", 0, 179, onTrack7)
cv2.createTrackbar("HH2", "Mask Settings", 179, 179, onTrack8)

cv2.createTrackbar("SL", "Mask Settings", 0, 255, onTrack3)
cv2.createTrackbar("SH", "Mask Settings", 255, 255, onTrack4)
cv2.createTrackbar("VL", "Mask Settings", 0, 255, onTrack5)
cv2.createTrackbar("VH", "Mask Settings", 255, 255, onTrack6)

hueLow = 0
hueHigh = 179
satLow = 0
satHigh = 255
valLow = 0
valHigh = 255

while True:
    _, frame = cam.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])

    mask = cv2.inRange(hsvFrame, lowerBound, upperBound)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Result", result)
    # cv2.imshow("Mask", mask)
    cv2.imshow("Capture", frame)
    cv2.moveWindow("Capture", 0, 0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
