import cv2

img = cv2.imread('lena.jpg', -1)

print(img)

cv2.imshow('teste', img)
k = cv2.waitKey(0) & 0xFF  # a variável k recebe a tecla que foi pressionada.
# a documentação recomenda usar a máscara & 0xFF em máquinas 64bit

if k == ord('q'):  # se k == q
    cv2.destroyAllWindows()  # fecha as janelas sem salvar nada

elif k == ord('s'):  # se k == s
    cv2.imwrite('lena_copia.png', img)  # salva a imagem
    cv2.destroyAllWindows()     # fecha as janelas
