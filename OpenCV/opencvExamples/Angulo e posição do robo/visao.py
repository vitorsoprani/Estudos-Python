import cv2
import numpy as np
from math import degrees, atan2


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


def onTrack8(x):
    global modo
    modo = x


def ClickEvent(event, x, y, flags, param):
    variacao = 20
    if event == cv2.EVENT_LBUTTONDOWN:
        if modo == 0:
            cv2.setTrackbarPos("HL", "Config", hsvFrame[y, x, 0] - variacao)
            cv2.setTrackbarPos("HH", "Config", hsvFrame[y, x, 0] + variacao)
            cv2.setTrackbarPos("SL", "Config", hsvFrame[y, x, 1] - variacao)
            cv2.setTrackbarPos("SH", "Config", hsvFrame[y, x, 1] + variacao)
            cv2.setTrackbarPos("VL", "Config", hsvFrame[y, x, 2] - 50)
            cv2.setTrackbarPos("VH", "Config", hsvFrame[y, x, 2] + 50)
            print("cliquei")
        elif modo == 1:
            print("movimento")


def DefineCentroide(contorno):
    M = cv2.moments(contorno)
    if M["m00"] != 0:
        # acha o x do centroide a partir dos momentos
        cx = int(M['m10']/M['m00'])
        # acha o y do centroide a partir dos momentos
        cy = int(M['m01']/M['m00'])
        return (cx, cy)


def PontoMedio(p1, p2):
    return (int((p1[0] + p2[0])/2), int((p1[1] + p2[1])/2))


def Angulo(p1, p2):
    deltaX = p2[0] - p1[0]
    deltaY = - (p2[1] - p1[1])

    return round((degrees(atan2(deltaY, deltaX))), 2)


cap = cv2.VideoCapture(2)

cv2.namedWindow("Config")
cv2.moveWindow("Config", 720, 0)

cv2.createTrackbar("HL", "Config", 0, 179, onTrack1)
cv2.createTrackbar("HH", "Config", 179, 179, onTrack2)
cv2.createTrackbar("SL", "Config", 0, 255, onTrack3)
cv2.createTrackbar("SH", "Config", 255, 255, onTrack4)
cv2.createTrackbar("VL", "Config", 0, 255, onTrack5)
cv2.createTrackbar("VH", "Config", 255, 255, onTrack6)

cv2.createTrackbar("MODO", "Config", 0, 1, onTrack8)

hueLow = 0
hueHigh = 179
satLow = 0
satHigh = 255
valLow = 0
valHigh = 255

modo = 0

cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", ClickEvent)

while True:
    _, frame = cap.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])

    mask = cv2.inRange(hsvFrame, lowerBound, upperBound)

    contornos, lixo = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 1:
        # ordena os contornos em ordem decrescente de área
        contornos = sorted(
            contornos, key=lambda x: cv2.contourArea(x), reverse=True)

        contorno1 = contornos[0]
        contorno2 = contornos[1]

        p1 = DefineCentroide(contorno1)
        p2 = DefineCentroide(contorno2)

        cv2.arrowedLine(frame, p1, p2, (0, 0, 255), 4)

        cRobo = PontoMedio(p1, p2)

        cv2.circle(frame, cRobo, 4, (0, 255, 0), -1)

        texto = "Pos: " + str(cRobo)
        cv2.putText(frame, texto, (p1[0], p1[1] + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        angulo = Angulo(p1, p2)

        texto = "Ang: " + str(angulo)
        cv2.putText(frame, texto, (p1[0], p1[1] + 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Camera", frame)
    cv2.imshow("Mascara", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
