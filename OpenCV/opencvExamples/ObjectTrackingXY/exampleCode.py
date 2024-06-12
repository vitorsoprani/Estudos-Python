import cv2
import numpy as np
# print(cv2.__version__)


def onTrack1(value):
    global hueLow
    hueLow = value


def onTrack2(value):
    global hueHigh
    hueHigh = value


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

    # forma simples de pegar os contornos externos
    contornos, lixo = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 0:
        # ordena os contornos em ordem decrescente de área
        contornos = sorted(
            contornos, key=lambda x: cv2.contourArea(x), reverse=True)
        # desenha o primeiro contorno
        cv2.drawContours(frame, contornos, 0, (255, 0, 0), 3)

        contorno = contornos[0]  # seleciona somente o contorno principal
        # gera as coordenadas de um retangulo em torno do contorno
        x, y, w, h = cv2.boundingRect(contorno)
        # desenha o retangulo
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

    # cv2.imshow("Result", result)
    cv2.imshow("Mask", mask)
    cv2.imshow("Capture", frame)
    cv2.moveWindow("Capture", 0, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
