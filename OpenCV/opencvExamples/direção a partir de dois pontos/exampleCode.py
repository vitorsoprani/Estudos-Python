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


def desenhaRetangulo(contorno):
    # gera as coordenadas de um retangulo em torno do contorno
    x, y, w, h = cv2.boundingRect(contorno)
    # desenha o retangulo
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)


cap = cv2.VideoCapture(2)

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

    if len(contornos) > 1:
        # ordena os contornos em ordem decrescente de área
        contornos = sorted(
            contornos, key=lambda x: cv2.contourArea(x), reverse=True)
        # desenha o primeiro contorno

        contorno1 = contornos[0]  # seleciona somente o contorno principal
        contorno2 = contornos[1]

        # desenhaRetangulo(contorno1)
        # desenhaRetangulo(contorno2)

        M1 = cv2.moments(contorno1)  # extrai os momentos do contorno (????)
        M2 = cv2.moments(contorno2)

        if M1["m00"] != 0:
            # acha o x do centroide a partir dos momentos
            c1x = int(M1['m10']/M1['m00'])
            # acha o y do centroide a partir dos momentos
            c1y = int(M1['m01']/M1['m00'])

            texto = "X: " + str(c1x) + "Y: " + str(c1y)
            fonte = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, texto, (c1x, c1y+20),
                        fonte, 0.8, (255, 0, 255), 2)
            cv2.circle(frame, (c1x, c1y), 3, (255, 0, 255), -1)

        if M2["m00"] != 0:
            # acha o x do centroide a partir dos momentos
            c2x = int(M2['m10']/M2['m00'])
            # acha o y do centroide a partir dos momentos
            c2y = int(M2['m01']/M2['m00'])

            texto = "X: " + str(c2x) + "Y: " + str(c2y)
            fonte = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, texto, (c2x, c2y+20),
                        fonte, 0.8, (255, 0, 255), 2)
            cv2.circle(frame, (c2x, c2y), 3, (255, 0, 255), -1)

        cv2.arrowedLine(frame, (c1x, c1y), (c2x, c2y), (0, 0, 255), 4)

        xRobo = int((c1x + c2x)/2)
        yRobo = int((c1y + c2y)/2)
        cv2.circle(frame, (xRobo, yRobo), 4, (0, 255, 0), -1)

    cv2.imshow("Camera", frame)
    cv2.imshow("Mascara", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
