import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1) #lê a imagem
# gera uma tela preta com o numpy (uma matriz, na verdade, quem gera a tela é o opencv)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.arrowedLine(img, (0, 0), (255, 255), (0, 0, 255), 5)  # cria uma seta

img = cv2.rectangle(img, (384, 0), (510, 128),
                    (255, 0, 0), 5)  # cria um retangulo

img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)  # cria um circulo

font = cv2.FONT_HERSHEY_COMPLEX  # define o a fonte
img = cv2.putText(img, 'Hello world!!!', (10, 500), font,
                  2, (255, 255, 255), 4, cv2.LINE_AA)  # escrev ena tela

cv2.imshow("imagem", img)  # """"imprime"""" a imagem

cv2.waitKey(0) & 0xFF  # espera alguma tecla ser apertada
cv2.destroyAllWindows()  # apaga tudo
