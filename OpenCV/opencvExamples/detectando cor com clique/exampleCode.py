import cv2
import numpy as np


def onTrack1(x):
    global hueLow
    hueLow = x


def onTrack2(x):
    global hueHigh
    hueHigh = x


def onTrack3(x):
    global satLow
    satLow = x


def onTrack4(x):
    global satHigh
    satHigh = x


def onTrack5(x):
    global valLow
    valLow = x


def onTrack6(x):
    global valHigh
    valHigh = x


def clickEvent(event, x, y, flags, param):
    variacao = 20
    if event == (cv2.EVENT_RBUTTONDOWN):
        cv2.setTrackbarPos("HL", "Config Masc", hsvFrame[y, x, 0] - variacao)
        cv2.setTrackbarPos("HH", "Config Masc", hsvFrame[y, x, 0] + variacao)
        cv2.setTrackbarPos("SL", "Config Masc", hsvFrame[y, x, 1] - variacao)
        cv2.setTrackbarPos("SH", "Config Masc", hsvFrame[y, x, 1] + variacao)
        cv2.setTrackbarPos("VL", "Config Masc", hsvFrame[y, x, 2] - 50)
        cv2.setTrackbarPos("VH", "Config Masc", hsvFrame[y, x, 2] + 50)
        print("cliquei")


cap = cv2.VideoCapture(0)

cv2.namedWindow("Config Masc")
cv2.moveWindow("Config Masc", 720, 0)

cv2.createTrackbar("HL", "Config Masc", 0, 179, onTrack1)
cv2.createTrackbar("HH", "Config Masc", 179, 179, onTrack2)
cv2.createTrackbar("SL", "Config Masc", 0, 255, onTrack3)
cv2.createTrackbar("SH", "Config Masc", 255, 255, onTrack4)
cv2.createTrackbar("VL", "Config Masc", 0, 255, onTrack5)
cv2.createTrackbar("VH", "Config Masc", 255, 255, onTrack6)

hueLow = 0
hueHigh = 179
satLow = 0
satHigh = 255
valLow = 0
valHigh = 255

cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", clickEvent)

while True:
    _, frame = cap.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])

    mask = cv2.inRange(hsvFrame, lowerBound, upperBound)

    contornos, lixo = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contornos:
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

    cv2.imshow("Camera", frame)
    cv2.imshow("Mascara", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
